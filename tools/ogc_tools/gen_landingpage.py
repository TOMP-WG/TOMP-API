#!/usr/bin/env python3
"""
Generate a fixed OGC API landing page JSON and a simple HTML page
from an OpenAPI specification that implements OGC API - Features and/or Processes.

Usage:
  python landingpage.py \
      --openapi openapi.yaml \
      --out-dir static_files \
      --out-landing landingpage.json \
      --out-html index.html \
      --base-url http://localhost:8080
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.parse import urljoin

def _load_openapi(path: str) -> dict:
    # JSON first; fall back to YAML if available
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Try JSON
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass

    # Try YAML
    try:
        import yaml  # type: ignore
    except Exception as e:
        raise SystemExit(
            "OpenAPI file is not valid JSON. To read YAML, install PyYAML:\n"
            "  pip install pyyaml\n"
            f"Original error: {e}"
        )

    return yaml.safe_load(content)

def _get_base_url(spec: dict, override: str | None) -> str:
    if override:
        return override.rstrip("/") + "/"

    servers = spec.get("servers") or []
    if servers and isinstance(servers, list) and isinstance(servers[0], dict) and servers[0].get("url"):
        return str(servers[0]["url"]).rstrip("/") + "/"

    # Fallback: relative base
    return "/"

def _has_path(spec: dict, path: str) -> bool:
    paths = spec.get("paths") or {}
    return path in paths

def _paths(spec: dict) -> set[str]:
    paths = spec.get("paths") or {}
    if isinstance(paths, dict):
        return set(paths.keys())
    return set()

def _detect_ogc_capabilities(spec: dict) -> dict:
    """Detect common OGC API endpoints from OpenAPI paths."""
    ps = _paths(spec)

    # Common
    has_landing = ("/" in ps) or _has_path(spec, "/landing")  # some implementations use / as landing
    has_api = "/api" in ps
    has_conformance = "/conformance" in ps

    # Features
    has_collections = "/collections" in ps
    has_items = any(p.startswith("/collections/") and ("/items" in p) for p in ps) or ("/collections/{collectionId}/items" in ps)

    # Processes
    has_processes = "/processes" in ps
    has_execute = any(p.startswith("/processes/") and ("/execution" in p or "/jobs" in p) for p in ps) \
                  or ("/processes/{processId}/execution" in ps) \
                  or ("/processes/{processId}/jobs" in ps)

    return {
        "common": {
            "landing": has_landing or True,  # we generate it anyway
            "api": has_api,
            "conformance": has_conformance,
        },
        "features": {
            "collections": has_collections,
            "items": has_items,
        },
        "processes": {
            "processes": has_processes,
            "execute": has_execute,
        },
    }

def _abs(base: str, path: str) -> str:
    # Ensure path doesn't double-slash
    path = path.lstrip("/")
    return urljoin(base, path)

def _guess_title_description(spec: dict) -> tuple[str, str]:
    info = spec.get("info") or {}
    title = info.get("title") or "OGC API"
    description = info.get("description") or ""
    return str(title), str(description)

def _make_links(base_url: str, spec: dict, caps: dict) -> list[dict]:
    title, _ = _guess_title_description(spec)

    links: list[dict] = []
    base_url = ""

    # Self landing page (we assume it will be served at "/")
    links.append({
        "href": _abs(base_url, "/?f=json"),
        "rel": "self",
        "type": "application/json",
        "title": f"{title} landing page (JSON)"
    })

    # Optional HTML landing page
    links.append({
        "href": _abs(base_url, "/?f=html"),
        "rel": "alternate",
        "type": "text/html",
        "title": f"{title} landing page (HTML)"
    })

    # OpenAPI
    if caps["common"]["api"] or True:
        # Many OGC APIs expose OpenAPI at /api; some also at /openapi or /api?f=json etc.
        # We add both a "service-desc" and "service-doc" entry to be helpful.
        # if _has_path(spec, "/api"):
        #     api_href = _abs(base_url, "/api")
        # else:
        #     # fallback guess; still useful for static landing page
        #     api_href = _abs(base_url, "/api")

        # links.append({
        #     "href": api_href,
        #     "rel": "service-desc",
        #     "type": "application/vnd.oai.openapi+json",
        #     "title": "OpenAPI definition (JSON)"
        # })
        # links.append({
        #     "href": api_href,
        #     "rel": "service-doc",
        #     "type": "text/html",
        #     "title": "OpenAPI documentation"
        # })
        links.append({
            "href": "/api?f=yaml",  # of f"{base_url}/openapi.yaml"
            "rel": "service-desc",
            #"type": "application/vnd.oai.openapi;version=3.0",
            "type": "text/yaml",
            "title": "OpenAPI definition (YAML)"
        })
        links.append({
            "href": "/api",  # of f"{base_url}/openapi.yaml"
            "rel": "service-desc",
            #"type": "application/vnd.oai.openapi;version=3.0",
            "type": "text/html",
            "title": "OpenAPI definition (HTML)"
        })

    # Conformance
    if caps["common"]["conformance"] or _has_path(spec, "/conformance"):
        links.append({
            "href": _abs(base_url, "/conformance?f=json"),
            "rel": "conformance",
            "type": "application/json",
            "title": "Conformance (JSON)"
        })
        links.append({
            "href": _abs(base_url, "/conformance"),
            "rel": "conformance",
            "type": "text/html",
            "title": "Conformance (HTML)"
        })

    # Features
    if caps["features"]["collections"]:
        links.append({
            "href": _abs(base_url, "/collections?f=json"),
            "rel": "data",
            "type": "application/json",
            "title": "Collections (JSON)"
        })
        links.append({
            "href": _abs(base_url, "/collections?f=html"),
            "rel": "alternate",
            "type": "text/html",
            "title": "Collections (HTML)"
        })

    # Processes
    if caps["processes"]["processes"]:
        links.append({
            "href": _abs(base_url, "/processes?f=json"),
            "rel": "processes",
            "type": "application/json",
            "title": "Processes (JSON)"
        })
        links.append({
            "href": _abs(base_url, "/processes?f=html"),
            "rel": "alternate",
            "type": "text/html",
            "title": "Processes (HTML)"
        })

    return links

def generate_landingpage(spec: dict, base_url: str) -> dict:
    title, description = _guess_title_description(spec)
    caps = _detect_ogc_capabilities(spec)

    landing = {
        "title": title,
        "description": description,
        "links": _make_links(base_url, spec, caps),
        # Extra (non-standard, but useful “fixed metadata” for debugging / ops)
        "generatedFrom": {
            "openapiVersion": spec.get("openapi", ""),
            "baseUrl": base_url.rstrip("/"),
            "detected": caps
        }
    }
    return landing

def generate_html(landing_json_filename: str, page_title: str) -> str:
    # This HTML expects landingpage.json to be served next to it (same folder).
    # If you serve it elsewhere, adjust LANDING_URL.
    return f"""<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{page_title} – Landing page</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }}
    code {{ background: #f3f3f3; padding: 0.1rem 0.3rem; border-radius: 4px; }}
    .muted {{ color: #666; }}
    ul {{ line-height: 1.6; }}
    a {{ text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 1rem; max-width: 900px; }}
  </style>
</head>
<body>
  <div class="card">
    <h1 id="title">{page_title}</h1>
    <p id="desc" class="muted"></p>

    <h2>Links</h2>
    <ul id="links"></ul>

    <p class="muted">
      Bron: <code>{landing_json_filename}</code>
    </p>
  </div>

  <script>
    const LANDING_URL = './{landing_json_filename}';

    function el(tag, attrs = {{}}, text = null) {{
      const e = document.createElement(tag);
      for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
      if (text !== null) e.textContent = text;
      return e;
    }}

    fetch(LANDING_URL)
      .then(r => {{
        if (!r.ok) throw new Error(`Failed to load landing page: ${{r.status}}`);
        return r.json();
      }})
      .then(j => {{
        document.getElementById('title').textContent = j.title || '{page_title}';
        document.getElementById('desc').innerHTML = j.description || '';

        const ul = document.getElementById('links');
        ul.innerHTML = '';

        (j.links || []).forEach(link => {{
          const li = el('li');
          const a = el('a', {{ href: link.href, rel: 'noopener noreferrer' }}, link.title || link.href);
          li.appendChild(a);

          const meta = [];
          if (link.rel) meta.push(`rel=${{link.rel}}`);
          if (link.type) meta.push(`type=${{link.type}}`);
          if (meta.length) {{
            li.appendChild(document.createTextNode(' '));
            li.appendChild(el('span', {{ class: 'muted' }}, `(${{meta.join(', ')}})`));
          }}

          ul.appendChild(li);
        }});
      }})
      .catch(err => {{
        document.getElementById('desc').textContent = String(err);
      }});
  </script>
</body>
</html>
"""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--openapi", required=True, help="Path to OpenAPI spec (YAML or JSON)")
    ap.add_argument("--out-dir", default="static_files", help="directory to write output files to")
    ap.add_argument("--out-landing", default="landingpage.json", help="Output landing page JSON filename")
    ap.add_argument("--out-html", default="index.html", help="Output HTML filename")
    ap.add_argument("--base-url", default=None, help="Override base URL (otherwise servers[0].url is used)")
    args = ap.parse_args()

    spec = _load_openapi(args.openapi)
    base_url = _get_base_url(spec, args.base_url)

    landing = generate_landingpage(spec, base_url)

    if not os.path.exists("./" + args.out_dir):
        os.makedirs("./" + args.out_dir)

    # Write landing JSON (fixed ordering for reproducibility)
    with open("./" + args.out_dir + "/" + args.out_landing, "w", encoding="utf-8") as f:
        json.dump(landing, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    title, _ = _guess_title_description(spec)
    html = generate_html(os.path.basename(args.out_landing), title)

    with open("./" + args.out_dir + "/"  + args.out_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote: {args.out_landing}")
    print(f"Wrote: {args.out_html}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())