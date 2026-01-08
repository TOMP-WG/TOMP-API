#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from typing import Any, Iterable


# -----------------------------
# OGC conformance class URIs
# -----------------------------
OGC_COMMON = {
    "core": "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core",
    "landing_page": "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/landing-page",
    "json": "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/json",
    "html": "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/html",
    "oas30": "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/oas30",
}

OGC_FEATURES_1 = {
    "core": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "html": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
    "geojson": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
    "gmlsf0": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/gmlsf0",
    "gmlsf2": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/gmlsf2",
    "oas30": "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
}

OGC_PROCESSES_1 = {
    "core": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
    "json": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json",
    "html": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html",
    "oas30": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30",
    "ogc_process_description": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description",
    "job_list": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list",
    # Optionele building blocks bestaan ook (callback/dismiss), maar die leiden we alleen af als de paden er zijn.
    "callback": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback",
    "dismiss": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss",
}


# -----------------------------
# Helpers
# -----------------------------
def load_openapi(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except Exception as e:
            raise SystemExit(
                "OpenAPI is not valid JSON. For YAML install PyYAML:\n"
                "  pip install pyyaml\n"
                f"Original error: {e}"
            )
        return yaml.safe_load(content)


def unique(seq: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for s in seq:
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def get_paths(spec: dict) -> dict[str, Any]:
    p = spec.get("paths") or {}
    return p if isinstance(p, dict) else {}


def has_path(spec: dict, path: str) -> bool:
    return path in get_paths(spec)


def any_path_startswith(spec: dict, prefix: str) -> bool:
    return any(p.startswith(prefix) for p in get_paths(spec).keys())


def iter_operations(spec: dict):
    """Yield (path, method, operationObject)."""
    for path, path_item in get_paths(spec).items():
        if not isinstance(path_item, dict):
            continue
        for method, op in path_item.items():
            if method.lower() not in {"get", "post", "put", "patch", "delete", "head", "options"}:
                continue
            if isinstance(op, dict):
                yield path, method.lower(), op


def collect_response_media_types(spec: dict) -> set[str]:
    media_types: set[str] = set()
    for _, _, op in iter_operations(spec):
        responses = op.get("responses") or {}
        if not isinstance(responses, dict):
            continue
        for _, resp in responses.items():
            if not isinstance(resp, dict):
                continue
            content = resp.get("content") or {}
            if not isinstance(content, dict):
                continue
            for mt in content.keys():
                if isinstance(mt, str):
                    media_types.add(mt.lower().strip())
    return media_types


def detect_common(spec: dict) -> dict[str, bool]:
    # Landing page: meestal GET op "/"
    has_root = has_path(spec, "/")
    has_conformance = has_path(spec, "/conformance")
    # API definition: OGC Common gebruikt vaak "/api", maar OpenAPI kan ook elders worden geserveerd.
    has_api = has_path(spec, "/api") or has_path(spec, "/openapi") or has_path(spec, "/openapi.json")
    return {
        "root": has_root,
        "conformance": has_conformance,
        "api": has_api,
    }


def detect_features_1(spec: dict) -> dict[str, bool]:
    return {
        "collections": has_path(spec, "/collections"),
        "items": has_path(spec, "/collections/{collectionId}/items")
                 or any_path_startswith(spec, "/collections/") and any(p.endswith("/items") for p in get_paths(spec).keys()),
    }


def detect_processes_1(spec: dict) -> dict[str, bool]:
    ps = get_paths(spec).keys()
    has_processes = "/processes" in ps
    has_process_desc = "/processes/{processId}" in ps
    has_execute = ("/processes/{processId}/execution" in ps) or ("/processes/{processId}/jobs" in ps)
    has_jobs = ("/jobs" in ps) or ("/processes/{processId}/jobs" in ps)
    has_dismiss = any(p.endswith("/dismiss") for p in ps)  # implementations verschillen; dit is een best-effort
    has_callback = any("callback" in p for p in ps)
    return {
        "processes": has_processes,
        "process_desc": has_process_desc,
        "execute": has_execute,
        "job_list": has_jobs,
        "dismiss": has_dismiss,
        "callback": has_callback,
    }


def derive_conforms_to(spec: dict) -> list[str]:
    media = collect_response_media_types(spec)
    common = detect_common(spec)
    feat = detect_features_1(spec)
    proc = detect_processes_1(spec)

    conforms: list[str] = []

    # 1) OGC API - Common (alle OGC APIs “leunen” hierop)
    # We claimen Common core+landing_page als er een root resource is.
    if common["root"]:
        conforms += [OGC_COMMON["core"], OGC_COMMON["landing_page"]]

    # Encodings (Common)
    if "application/json" in media or "application/geo+json" in media or "application/problem+json" in media:
        conforms.append(OGC_COMMON["json"])
    if "text/html" in media:
        conforms.append(OGC_COMMON["html"])

    # OpenAPI 3.0 conformance (Common): afleiden als de spec OpenAPI 3.x is
    # (en/of als er een /api-like endpoint is)
    openapi_version = str(spec.get("openapi") or "")
    if openapi_version.startswith("3.") or common["api"]:
        conforms.append(OGC_COMMON["oas30"])

    # 2) OGC API - Features - Part 1: Core
    if feat["collections"] or feat["items"]:
        conforms.append(OGC_FEATURES_1["core"])

        # Representaties/features encodings
        # GeoJSON conformance class: als OpenAPI expliciet application/geo+json aanbiedt
        if "application/geo+json" in media or "application/geojson" in media:
            conforms.append(OGC_FEATURES_1["geojson"])

        # HTML conformance class (Features)
        if "text/html" in media:
            conforms.append(OGC_FEATURES_1["html"])

        # OpenAPI 3.0 conformance class (Features)
        if openapi_version.startswith("3."):
            conforms.append(OGC_FEATURES_1["oas30"])

        # GML conformance classes: alleen claimen als er expliciete GML media types in responses zitten
        # (heel implementatie-afhankelijk; voeg hier toe als jij ze gebruikt)
        gml_media_markers = {"application/gml+xml", "text/xml", "application/xml"}
        if any(mt in media for mt in gml_media_markers):
            # Niet onderscheidbaar tussen gmlsf0 vs gmlsf2 op basis van media type alleen -> we claimen niets extra.
            pass

    # 3) OGC API - Processes - Part 1: Core
    if proc["processes"] or proc["execute"] or proc["process_desc"]:
        conforms.append(OGC_PROCESSES_1["core"])

        if proc["process_desc"]:
            conforms.append(OGC_PROCESSES_1["ogc_process_description"])
        if proc["job_list"]:
            conforms.append(OGC_PROCESSES_1["job_list"])

        if "application/json" in media:
            conforms.append(OGC_PROCESSES_1["json"])
        if "text/html" in media:
            conforms.append(OGC_PROCESSES_1["html"])
        if openapi_version.startswith("3."):
            conforms.append(OGC_PROCESSES_1["oas30"])

        # Optionele building blocks (alleen claimen als paden “duidelijk” aanwezig zijn)
        if proc["dismiss"]:
            conforms.append(OGC_PROCESSES_1["dismiss"])
        if proc["callback"]:
            conforms.append(OGC_PROCESSES_1["callback"])

    return unique(conforms)


def generate_conformance_json(conforms_to: list[str]) -> dict:
    return {"conformsTo": conforms_to}


def escape_html(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#39;"))


def generate_conformance_html(conforms_to: list[str]) -> str:
    items = "\n".join(f"<li><code>{escape_html(u)}</code></li>" for u in conforms_to) or "<li><em>Geen conformance classes afgeleid</em></li>"
    return f"""<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Conformance</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }}
    .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 1rem; max-width: 900px; }}
    .muted {{ color: #666; }}
    code {{ background: #f3f3f3; padding: 0.1rem 0.3rem; border-radius: 4px; }}
    ul {{ line-height: 1.6; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Conformance</h1>
    <h2>conforms to</h2>
    <ul>
      {items}
    </ul>
  </div>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--openapi", required=True, help="Path to OpenAPI spec (YAML or JSON)")
    ap.add_argument("--out-dir", default="static_files", help="directory to write output files to")
    ap.add_argument("--out-json", default="conformance.json")
    ap.add_argument("--out-html", default="conformance.html")
    args = ap.parse_args()

    spec = load_openapi(args.openapi)
    conforms_to = derive_conforms_to(spec)

    if not os.path.exists("./" + args.out_dir):
        os.makedirs("./" + args.out_dir)

    with open("./" + args.out_dir + "/" + args.out_json, "w", encoding="utf-8") as f:
        json.dump(generate_conformance_json(conforms_to), f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    with open("./" + args.out_dir + "/" + args.out_html, "w", encoding="utf-8") as f:
        f.write(generate_conformance_html(conforms_to))

    print(f"Wrote: {args.out_json}")
    print(f"Wrote: {args.out_html}")
    print(f"Derived {len(conforms_to)} conformance class URIs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())