from __future__ import annotations

import argparse
import json
import os
import re
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


# ----------------------------
# $ref resolver (local only)
# ----------------------------
def deref(obj: Any, doc: Dict[str, Any]) -> Any:
    if not isinstance(obj, dict) or "$ref" not in obj:
        return obj
    ref = obj["$ref"]
    if not isinstance(ref, str) or not ref.startswith("#/"):
        return obj
    cur: Any = doc
    for part in ref[2:].split("/"):
        cur = cur[part]
    return cur

def deep_deref(obj: Any, doc: Dict[str, Any], max_depth: int = 30) -> Any:
    cur = obj
    for _ in range(max_depth):
        if isinstance(cur, dict) and "$ref" in cur and isinstance(cur["$ref"], str) and cur["$ref"].startswith("#/"):
            cur = deref(cur, doc)
        else:
            break
    return cur

def schema_props_required(schema: Dict[str, Any], doc: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    s = deep_deref(schema, doc)
    if not isinstance(s, dict):
        return {}, []
    props = s.get("properties") if isinstance(s.get("properties"), dict) else {}
    req = s.get("required") if isinstance(s.get("required"), list) else []
    return props, req

def pick_request_schema(post_op: Dict[str, Any], doc: Dict[str, Any]) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    rb = post_op.get("requestBody")
    if not rb:
        return None, None
    rb = deep_deref(rb, doc)
    content = rb.get("content")
    if not isinstance(content, dict) or not content:
        return None, None
    mt = "application/json" if "application/json" in content else next(iter(content.keys()))
    schema = content.get(mt, {}).get("schema")
    return mt, schema

def pick_first_2xx_schema(responses: Dict[str, Any], doc: Dict[str, Any]) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    if not isinstance(responses, dict):
        return None, None

    preferred = ["200", "201", "204"]
    codes = list(responses.keys())
    sorted_codes = [c for c in preferred if c in codes] + sorted([c for c in codes if str(c).startswith("2") and c not in preferred])

    for code in sorted_codes:
        resp = deep_deref(responses.get(code), doc)
        if not isinstance(resp, dict):
            continue
        content = resp.get("content")
        if not isinstance(content, dict) or not content:
            continue
        mt = "application/json" if "application/json" in content else next(iter(content.keys()))
        schema = content.get(mt, {}).get("schema")
        if schema:
            return mt, schema

    return None, None

def flatten_inputs(request_schema: Dict[str, Any], doc: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Request bodies in jouw spec zijn meestal: { "inputs": { ... } }
    We flattenen naar OGC inputs: { "<field>": inputDescription, ... }
    """
    req_props, _ = schema_props_required(request_schema, doc)
    inputs_schema = req_props.get("inputs")
    if not inputs_schema:
        return {}

    inputs_schema = deep_deref(inputs_schema, doc)
    in_props, in_required = schema_props_required(inputs_schema, doc)

    flat: Dict[str, Dict[str, Any]] = {}
    for name, prop_schema in in_props.items():
        desc = ""
        if isinstance(prop_schema, dict) and isinstance(prop_schema.get("description"), str):
            desc = prop_schema["description"]
        flat[name] = {
            "title": name,
            "description": desc,
            "minOccurs": 1 if name in in_required else 0,
            "maxOccurs": 1,
            "schema": prefix_schema(deepcopy(prop_schema)),  # refs blijven refs (prima)
        }
    return flat

def prefix_schema(schema: Any) -> Any:
    if isinstance(schema, dict):
        new_dict = {}
        for k, v in schema.items():
            if k == "$ref" and isinstance(v, str):
                new_dict[k] = "/api/#/components/schemas/" + v.split("/")[-1]
            else:
                new_dict[k] = prefix_schema(v)
        return new_dict
    elif isinstance(schema, list):
        return [prefix_schema(item) for item in schema]
    else:
        return schema

# ----------------------------
# Process extraction & expansion
# ----------------------------
@dataclass(frozen=True)
class ProcessDef:
    id: str
    title: str
    description: str
    execution_path: Optional[str]
    post_op: Optional[Dict[str, Any]]


PROCESS_EXEC_RE = re.compile(r"^/processes/([^/{}]+)/execution$")

def extract_explicit_processes(openapi: Dict[str, Any]) -> Dict[str, ProcessDef]:
    paths = openapi.get("paths", {}) or {}
    found: Dict[str, ProcessDef] = {}
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        m = PROCESS_EXEC_RE.match(path)
        if not m:
            continue
        pid = m.group(1)
        post = methods.get("post")
        if not isinstance(post, dict):
            continue
        found[pid] = ProcessDef(
            id=pid,
            title=post.get("summary") or pid,
            description=post.get("description") or "",
            execution_path=path,
            post_op=post,
        )
    return found

def _extract_enum_from_path_param(post_op: Dict[str, Any], param_name: str) -> List[str]:
    for p in post_op.get("parameters", []) or []:
        if not isinstance(p, dict):
            continue
        if p.get("in") != "path" or p.get("name") != param_name:
            continue
        schema = p.get("schema") or {}
        if isinstance(schema, dict):
            if isinstance(schema.get("enum"), list):
                return list(schema["enum"])
            if isinstance(schema.get("x-enum"), list):
                return list(schema["x-enum"])
    return []

def expand_templated_processes(openapi: Dict[str, Any]) -> Dict[str, ProcessDef]:
    paths = openapi.get("paths", {}) or {}
    out: Dict[str, ProcessDef] = {}

    # leg operations
    template_leg = paths.get("/processes/{legOperation}-leg/execution", {})
    post_leg = template_leg.get("post") if isinstance(template_leg, dict) else None
    if isinstance(post_leg, dict):
        for op in _extract_enum_from_path_param(post_leg, "legOperation"):
            pid = f"{op}-leg"
            out[pid] = ProcessDef(
                id=pid,
                title=post_leg.get("summary") or pid,
                description=post_leg.get("description") or "",
                execution_path=f"/processes/{op}-leg/execution",
                post_op=post_leg,
            )

    # asset operations
    template_asset = paths.get("/processes/{assetOperation}-asset/execution", {})
    post_asset = template_asset.get("post") if isinstance(template_asset, dict) else None
    if isinstance(post_asset, dict):
        for op in _extract_enum_from_path_param(post_asset, "assetOperation"):
            pid = f"{op}-asset"
            out[pid] = ProcessDef(
                id=pid,
                title=post_asset.get("summary") or pid,
                description=post_asset.get("description") or "",
                execution_path=f"/processes/{op}-asset/execution",
                post_op=post_asset,
            )

    # product operations
    template_product = paths.get("/processes/{productOperation}-product/execution", {})
    post_product = template_product.get("post") if isinstance(template_product, dict) else None
    if isinstance(post_product, dict):
        for op in _extract_enum_from_path_param(post_product, "productOperation"):
            pid = f"{op}-product"
            out[pid] = ProcessDef(
                id=pid,
                title=post_product.get("summary") or pid,
                description=post_product.get("description") or "",
                execution_path=f"/processes/{op}-product/execution",
                post_op=post_product,
            )

    return out

def declared_process_ids_from_enum(openapi: Dict[str, Any]) -> List[str]:
    paths = openapi.get("paths", {}) or {}
    get_op = paths.get("/processes/{processId}", {}).get("get")
    if not isinstance(get_op, dict):
        return []
    for p in get_op.get("parameters", []) or []:
        if not isinstance(p, dict):
            continue
        if p.get("in") == "path" and p.get("name") == "processId":
            schema = deep_deref(p.get("schema") or {}, openapi)
            if isinstance(schema, dict) and isinstance(schema.get("enum"), list):
                return list(schema["enum"])
    return []

def build_all_process_defs(openapi: Dict[str, Any]) -> Dict[str, ProcessDef]:
    explicit = extract_explicit_processes(openapi)
    templated = expand_templated_processes(openapi)
    declared = declared_process_ids_from_enum(openapi)

    all_ids = set(explicit.keys()) | set(templated.keys()) | set(declared)

    out: Dict[str, ProcessDef] = {}
    for pid in sorted(all_ids, key=lambda id_: id_.split("-")[1]):
        if pid in explicit:
            out[pid] = explicit[pid]
        elif pid in templated:
            out[pid] = templated[pid]
        else:
            # declared but no execution endpoint / no POST op: still generate description (without execute link)
            out[pid] = ProcessDef(id=pid, title=pid, description="", execution_path=None, post_op=None)

    return out


# ----------------------------
# OGC JSON builders
# ----------------------------
def build_process_list(openapi: Dict[str, Any], base_url: str, procs: Dict[str, ProcessDef]) -> Dict[str, Any]:
    version = openapi.get("info", {}).get("version", "unknown")

    processes: List[Dict[str, Any]] = []
    for pid, p in sorted(procs.items(), key=lambda kv: kv[0]):
        links = [
            {"rel": "self", "href": urljoin(base_url, f"/processes/{pid}"), "type": "application/json", "method": "GET"},
            # also provide HTML alternative for convenience
            {"rel": "alternate", "href": urljoin(base_url, f"/processes/{pid}?f=html"), "type": "text/html", "method": "GET"},
        ]
        if p.execution_path:
            links.append({"rel": "execute", "href": urljoin(base_url, p.execution_path), "type": "application/json", "method": "POST"})

        processes.append(
            {
                "id": pid,
                "version": version,
                "title": p.title,
                "description": p.description,
                "jobControlOptions": ["sync-execute"],
                "outputTransmission": ["value"],
                "links": links,
            }
        )

    return {
        "processes": processes,
        "links": [
            {"rel": "self", "href": urljoin(base_url, "/processes"), "type": "application/json", "method": "GET"},
            {"rel": "alternate", "href": urljoin(base_url, "/processes?f=html"), "type": "text/html", "method": "GET"},
        ],
    }


def build_process_description(openapi: Dict[str, Any], base_url: str, p: ProcessDef) -> Dict[str, Any]:
    version = openapi.get("info", {}).get("version", "unknown")

    links = [
        {"rel": "self", "href": urljoin(base_url, f"/processes/{p.id}"), "type": "application/json", "method": "GET"},
        {"rel": "alternate", "href": urljoin(base_url, f"/processes/{p.id}?f=html"), "type": "text/html", "method": "GET"},
    ]
    if p.execution_path:
        links.append({"rel": "execute", "href": urljoin(base_url, p.execution_path), "type": "application/json", "method": "POST"})

    inputs: Dict[str, Any] = {}
    outputs: Dict[str, Any] = {}

    if p.post_op:
        _, req_schema = pick_request_schema(p.post_op, openapi)
        if req_schema:
            inputs = flatten_inputs(req_schema, openapi)

        _, out_schema = pick_first_2xx_schema(p.post_op.get("responses", {}) or {}, openapi)
        if out_schema:
            outputs = {
                "result": {
                    "title": "result",
                    "description": f"Primary result of process '{p.id}'",
                    "schema": deepcopy(out_schema),
                }
            }

    return {
        "id": p.id,
        "version": version,
        "title": p.title,
        "description": p.description,
        "jobControlOptions": ["sync-execute"],
        "outputTransmission": ["value"],
        "links": links,
        "inputs": inputs,
        "outputs": outputs,
    }


# ----------------------------
# Static site writing
# ----------------------------
def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def write_json(path: str, obj: Any) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def write_html(path: str, html: str) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def render_templates(template_dir: str, process_list: Dict[str, Any], process_descs: Dict[str, Any]) -> Tuple[str, Dict[str, str]]:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "xml"]),
    )
    index_tpl = env.get_template("processes_index.html.j2")
    detail_tpl = env.get_template("process_detail.html.j2")

    def second_part(obj) -> str:
        parts = obj['id'].split("-", 1)
        return parts[1] if len(parts) == 2 else ""

    processes_sorted = sorted(process_list['processes'], key=second_part)

    process_list['processes'] = processes_sorted

    index_html = index_tpl.render(process_list=process_list)

    details_html: Dict[str, str] = {}
    for pid, desc in process_descs.items():
        details_html[pid] = detail_tpl.render(process=desc)

    return index_html, details_html


def build_static_bundle(openapi_path: str, base_url: str, out_root: str, template_dir: str) -> None:
    with open(openapi_path, "r", encoding="utf-8") as f:
        openapi = yaml.safe_load(f)

    procs = build_all_process_defs(openapi)

    process_list = build_process_list(openapi, base_url, procs)
    process_descs = {pid: build_process_description(openapi, base_url, p) for pid, p in procs.items()}

    processes_dir = out_root
    write_json(os.path.join(out_root, "processes.json"), process_list)
    for pid, desc in process_descs.items():
        write_json(os.path.join(out_root, f"{pid}.json"), desc)

    # HTML
    index_html, detail_html_map = render_templates(template_dir, process_list, process_descs)
    write_html(os.path.join(out_root, "processes.html"), index_html)
    for pid, html in detail_html_map.items():
        write_html(os.path.join(out_root, f"{pid}.html"), html)

    print("Generated static OGC process bundle:")
    print(f"- {processes_dir}/processes.json      (GET /processes)")
    print(f"- {processes_dir}/<id>.json       (GET /processes/{{id}})")
    print(f"- {processes_dir}/processes.html      (GET /processes?f=html)")
    print(f"- {processes_dir}/<id>.html       (GET /processes/{{id}}?f=html)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--openapi", required=True, help="Path to OpenAPI YAML (e.g. openapi.yaml)")
    ap.add_argument("--base-url", default="/", help="Base URL for link hrefs (e.g. https://example.to.eu/tomp/v2)")
    ap.add_argument("--out-dir", default="./static_files", help="Output root directory")
    ap.add_argument("--templates", default="./templates", help="Template directory containing *.j2")
    args = ap.parse_args()

    build_static_bundle(args.openapi, args.base_url, args.out_dir, args.templates)

if __name__ == "__main__":
    main()