#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from typing import Any, Iterable


# -----------------------------
# IO
# -----------------------------
def load_openapi(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # JSON first
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # YAML fallback
        try:
            import yaml  # type: ignore
        except Exception as e:
            raise SystemExit(
                "OpenAPI is not valid JSON. For YAML install PyYAML:\n"
                "  pip install pyyaml\n"
                f"Original error: {e}"
            )
        return yaml.safe_load(content)


def write_json(path: str, obj: dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_text(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# -----------------------------
# Helpers
# -----------------------------
def unique(seq: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for s in seq:
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#39;"))


def get_paths(spec: dict[str, Any]) -> dict[str, Any]:
    p = spec.get("paths") or {}
    return p if isinstance(p, dict) else {}


def iter_operations(spec: dict[str, Any]):
    """Yield (path, method, operationObject)."""
    for path, path_item in get_paths(spec).items():
        if not isinstance(path_item, dict):
            continue
        for method, op in path_item.items():
            if method.lower() not in {"get", "post", "put", "patch", "delete", "head", "options"}:
                continue
            if isinstance(op, dict):
                yield path, method.lower(), op


def find_operation(spec: dict[str, Any], path: str, method: str) -> dict[str, Any] | None:
    p = get_paths(spec).get(path)
    if not isinstance(p, dict):
        return None
    op = p.get(method.lower())
    return op if isinstance(op, dict) else None


def collect_parameters(spec: dict[str, Any], path: str, method: str) -> list[dict[str, Any]]:
    """Collect path-level + operation-level parameters (resolved minimally for $ref to components/parameters)."""
    paths = get_paths(spec)
    path_item = paths.get(path) if isinstance(paths.get(path), dict) else {}
    op = find_operation(spec, path, method) or {}

    params: list[Any] = []
    for where in (path_item, op):
        if isinstance(where, dict) and isinstance(where.get("parameters"), list):
            params.extend(where["parameters"])

    # resolve simple $ref -> components.parameters.*
    resolved: list[dict[str, Any]] = []
    comps = (spec.get("components") or {})
    comp_params = (comps.get("parameters") or {}) if isinstance(comps, dict) else {}

    for p in params:
        if isinstance(p, dict) and "$ref" in p and isinstance(p["$ref"], str):
            ref = p["$ref"]
            # format: "#/components/parameters/CollectionId"
            parts = ref.split("/")
            if len(parts) >= 4 and parts[0] == "#" and parts[1] == "components" and parts[2] == "parameters":
                key = parts[3]
                cp = comp_params.get(key)
                if isinstance(cp, dict):
                    resolved.append(cp)
                    continue
        if isinstance(p, dict):
            resolved.append(p)

    return resolved


# -----------------------------
# Derive collection IDs + metadata
# -----------------------------
def derive_collections(spec: dict[str, Any]) -> list[dict[str, Any]]:
    # 1) Vendor extension (best metadata)
    xcols = spec.get("x-collections")
    if isinstance(xcols, list):
        out = []
        for c in xcols:
            if isinstance(c, dict) and isinstance(c.get("id"), str) and c["id"].strip():
                out.append({
                    "id": c["id"].strip(),
                    # "title": c.get("title") or c["id"].strip(),
                    "description": c.get("description") or "",
                    # allow passing through optional OGC fields if present
                    **({ "extent": c["extent"] } if "extent" in c else {}),
                    **({ "crs": c["crs"] } if "crs" in c else {}),
                })
        if out:
            return out

    # 2) Enum/examples in collectionId parameter
    params = collect_parameters(spec, "/collections/{collectionId}", "get")
    col_param = None
    for p in params:
        if p.get("in") == "path" and p.get("name") == "collectionId":
            col_param = p
            break

    if not col_param:
        raise SystemExit(
            "Kan geen collections afleiden uit OpenAPI.\n\n"
            "Oplossingen:\n"
            "- Voeg schema.enum toe op de path-parameter 'collectionId' bij /collections/{collectionId}\n"
            "- of voeg 'x-collections' toe op rootniveau van de OpenAPI\n"
        )

    ids: list[str] = []

    schema = col_param.get("schema") if isinstance(col_param.get("schema"), dict) else {}
    enum = schema.get("enum")
    if isinstance(enum, list):
        ids += [str(x) for x in enum if str(x).strip()]

    examples = col_param.get("examples")
    if isinstance(examples, dict):
        for ex in examples.values():
            if isinstance(ex, dict) and "value" in ex:
                v = str(ex["value"]).strip()
                if v:
                    ids.append(v)

    # OpenAPI also allows "example" (singular)
    if "example" in col_param:
        v = str(col_param["example"]).strip()
        if v:
            ids.append(v)

    ids = unique([i for i in ids if i])

    if not ids:
        raise SystemExit(
            "Ik vond wel de parameter 'collectionId', maar geen enum/examples.\n"
            "Voeg schema.enum of examples toe, of gebruik x-collections."
        )

    # Minimal metadata: title defaults to id
    return [{"id": cid, "title": cid, "description": ""} for cid in ids]


# -----------------------------
# Generate OGC-ish outputs (relative from /collections)
# -----------------------------
def rel_link(href: str, rel: str, type_: str, title: str) -> dict[str, str]:
    return {"href": href, "rel": rel, "type": type_, "title": title}


def collection_links(cid: str) -> list[dict[str, str]]:
    # These hrefs are relative from /collections (as you requested)
    return [
        rel_link(f"{cid}?f=json", "self", "application/json", f"Collection {cid} (JSON)"),
        rel_link(f"{cid}?f=html", "alternate", "text/html", f"Collection {cid} (HTML)")
    ]


def collections_root_links() -> list[dict[str, str]]:
    # relative from /collections itself
    return [
        rel_link("?f=json", "self", "application/json", "Collections (JSON)"),
        rel_link("?f=html", "alternate", "text/html", "Collections (HTML)"),
    ]


def generate_collections_json(collections: list[dict[str, Any]]) -> dict[str, Any]:
    out_cols = []
    for c in collections:
        cid = c["id"]
        col = {
            "id": cid,
            # "title": c.get("title", cid),
            "description": c.get("description", ""),
            "itemType": "feature",
            "links": collection_links(cid),
        }
        if "extent" in c:
            col["extent"] = c["extent"]
        if "crs" in c:
            col["crs"] = c["crs"]
        out_cols.append(col)

    return {
        "links": collections_root_links(),
        "collections": out_cols,
        "numberMatched": len(out_cols),
        "numberReturned": len(out_cols),
    }


def generate_collections_html(collections: list[dict[str, Any]]) -> str:
    rows = []
    for c in collections:
        cid = esc(c["id"])
        desc = esc(str(c.get("description", "")))
        rows.append(f"""
          <tr>
            <td><code>{cid}</code></td>
            <td class="muted">{desc}</td>
            <td>
              <a href="{cid}?f=html">metadata (HTML)</a> |
              <a href="{cid}?f=json">metadata (JSON)</a>              
            </td>
          </tr>
        """)

    body = "\n".join(rows) if rows else "<tr><td colspan='3' class='muted'>Geen collections afgeleid.</td></tr>"

    return f"""<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Collections</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }}
    .muted {{ color: #666; }}
    table {{ border-collapse: collapse; width: 100%; max-width: 1100px; }}
    th, td {{ border: 1px solid #ddd; padding: 0.6rem; vertical-align: top; }}
    th {{ background: #f7f7f7; text-align: left; }}
    code {{ background: #f3f3f3; padding: 0.1rem 0.3rem; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>Collections</h1>
  <p class="muted">Relative links to <code>/collections</code>.</p>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>description</th>
        <th>links</th>
      </tr>
    </thead>
    <tbody>
      {body}
    </tbody>
  </table>
</body>
</html>
"""


def generate_collection_json(c: dict[str, Any]) -> dict[str, Any]:
    cid = c["id"]
    out = {
        "id": cid,
        "title": c.get("title", cid),
        "description": c.get("description", ""),
        "itemType": "feature",
        "links": collection_links(cid),
    }
    if "extent" in c:
        out["extent"] = c["extent"]
    if "crs" in c:
        out["crs"] = c["crs"]
    return out


def generate_collection_html(c: dict[str, Any]) -> str:
    cid = esc(c["id"])
    title = esc(str(c.get("title", c["id"])))
    desc = esc(str(c.get("description", "")))
    return f"""<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Collection {cid}</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }}
    .muted {{ color: #666; }}
    code {{ background: #f3f3f3; padding: 0.1rem 0.3rem; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>Collection: <code>{cid}</code></h1>
  <p><strong>{title}</strong></p>
  <p class="muted">{desc}</p>

  <h2>Links</h2>
  <ul>
    <li><a href="{cid}?f=json">self (JSON)</a></li>
    <li><a href="{cid}?f=html">alternate (HTML)</a></li>
  </ul>
</body>
</html>
"""


# -----------------------------
# Main
# -----------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--openapi", required=True, help="Path to OpenAPI spec (YAML or JSON)")
    ap.add_argument("--out-dir", default="static_files", help="Output directory (default: ./static_files)")
    args = ap.parse_args()

    spec = load_openapi(args.openapi)

    # Validate expected endpoints exist (at least structurally)
    if not find_operation(spec, "/collections", "get"):
        raise SystemExit("OpenAPI mist GET /collections (paths.'/collections'.get).")
    if not find_operation(spec, "/collections/{collectionId}", "get"):
        raise SystemExit("OpenAPI mist GET /collections/{collectionId} (paths.'/collections/{collectionId}'.get).")

    collections = derive_collections(spec)

    # Write root /collections
    write_json(os.path.join(args.out_dir, "collections.json"), generate_collections_json(collections))
    write_text(os.path.join(args.out_dir, "collections.html"), generate_collections_html(collections))

    # Write underlying collections (files under ./collections/<id>.*)
    for c in collections:
        cid = c["id"]
        write_json(os.path.join(args.out_dir, f"{cid}.json"), generate_collection_json(c))
        write_text(os.path.join(args.out_dir, f"{cid}.html"), generate_collection_html(c))

    print(f"Wrote: {os.path.abspath(os.path.join(args.out_dir, 'collections.json'))}")
    print(f"Wrote: {os.path.abspath(os.path.join(args.out_dir, 'collections.html'))}")
    print(f"Wrote: {len(collections)} collection files under: {os.path.abspath(os.path.join(args.out_dir, 'collections'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())