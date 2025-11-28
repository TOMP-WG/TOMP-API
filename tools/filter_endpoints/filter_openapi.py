#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from typing import Any, Dict, Set, Tuple, List, Optional

try:
    import yaml  # PyYAML
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

HTTP_METHODS = {"get","put","post","delete","options","head","patch","trace"}

def load_openapi(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        # YAML or JSON; yaml.safe_load handles both
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("OpenAPI file must contain a top-level object (dict).")
    if "openapi" not in data and "swagger" not in data:
        raise ValueError("Not an OpenAPI/Swagger spec (missing 'openapi' or 'swagger').")
    if "paths" not in data or not isinstance(data["paths"], dict):
        raise ValueError("Spec is missing 'paths'.")
    return data

def ask_yes_no(prompt: str, default: Optional[bool]=None) -> bool:
    yn = " [y/n] "
    if default is True:
        yn = " [Y/n] "
    elif default is False:
        yn = " [y/N] "
    while True:
        resp = input(prompt + yn).strip().lower()
        if not resp and default is not None:
            return default
        if resp in ("y","yes"):
            return True
        if resp in ("n","no"):
            return False
        print("Please answer with y/yes or n/no.")

def select_operations(spec: Dict[str, Any], preselect: Optional[List[str]]=None) -> Dict[str, Dict[str, Any]]:
    """
    preselect: list of filters (glob patterns), e.g.:
      - "/users*"
      - "post /login"
      - "get /users/{id}"
    """
    import fnmatch

    selected: Dict[str, Dict[str, Any]] = {}
    paths: Dict[str, Any] = spec["paths"]
    tags: Dict[str, Any] = spec["tags"]

    def op_matches_filter(method: str, path: str, filt: str) -> bool:
        filt = filt.strip()
        # formaten: "get /path", "/path*", of "*"
        if " " in filt:
            m, p = filt.split(" ", 1)
            if not fnmatch.fnmatch(method.lower(), m.lower()):
                return False
            return fnmatch.fnmatch(path, p)
        else:
            return fnmatch.fnmatch(path, filt)

    for tag in tags:
        tag_name = tag.get("name")
        print(f"\nModule: {tag_name}")
        for path, item in paths.items():
            if not isinstance(item, dict):
                continue
            for method, op in item.items():
                if method.lower() not in HTTP_METHODS:
                    continue
                default_select = None
                if preselect:
                    # Als een van de filters matcht, zet default op True, anders False
                    matched = any(op_matches_filter(method, path, f) for f in preselect)
                    default_select = True if matched else False
                summary = op.get("summary") if isinstance(op, dict) else None
                prompt = f"Include {method.upper()} {path}"
                if summary:
                    prompt += f" — {summary}"
                if tag_name in op.get("tags", []):
                    take = ask_yes_no(prompt, default=default_select)
                    if take:
                        selected.setdefault(path, {})[method] = op
    return selected

def prune_components(spec_full: Dict[str, Any], spec_filtered: Dict[str, Any]) -> None:
    """
    Reduce components to only those referenced from the filtered paths (schemas, parameters, responses,
    requestBodies, headers, securitySchemes, examples, links, callbacks, pathItems). Follows transitive $refs.
    """
    from collections import deque

    components = spec_full.get("components", {})
    if not components:
        return

    # Helper om $ref te itereren
    def iter_refs(node: Any) -> List[str]:
        found = []
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "$ref" and isinstance(v, str):
                    found.append(v)
                else:
                    found.extend(iter_refs(v))
        elif isinstance(node, list):
            for v in node:
                found.extend(iter_refs(v))
        return found

    # Verzamel initiële refs uit de gefilterde paths en top-level secties die we meenemen
    roots = []
    for section in ["paths", "security", "tags"]:
        if section in spec_filtered:
            roots.append(spec_filtered[section])

    # Volg $refs transitief
    queue = deque()
    seen: Set[str] = set()
    for root in roots:
        for r in iter_refs(root):
            if r not in seen:
                seen.add(r)
                queue.append(r)

    # Geldige component roots
    valid_prefixes = {
        "#/components/schemas/",
        "#/components/parameters/",
        "#/components/responses/",
        "#/components/requestBodies/",
        "#/components/headers/",
        "#/components/securitySchemes/",
        "#/components/examples/",
        "#/components/links/",
        "#/components/callbacks/",
        "#/components/pathItems/",
    }

    used: Dict[str, Dict[str, Any]] = {k: {} for k in components.keys()}

    def resolve_ref(ref: str) -> Optional[Tuple[str, str, Any]]:
        if not any(ref.startswith(p) for p in valid_prefixes):
            return None
        parts = ref.split("/")
        # "#", "components", "<section>", "<name...>"
        if len(parts) < 4:
            return None
        section = parts[2]
        name = "/".join(parts[3:])
        sect_obj = components.get(section, {})
        if not isinstance(sect_obj, dict):
            return None
        if name not in sect_obj:
            return None
        return section, name, sect_obj[name]

    while queue:
        ref = queue.popleft()
        resolved = resolve_ref(ref)
        if not resolved:
            continue
        section, name, obj = resolved
        if name in used.get(section, {}):
            continue
        used.setdefault(section, {})[name] = obj
        # zoek verdere refs binnen dit object
        for r in iter_refs(obj):
            if r not in seen:
                seen.add(r)
                queue.append(r)

    # Bouw gefilterde components
    filtered_components = {}
    for section, items in used.items():
        if items:
            filtered_components[section] = items

    if filtered_components:
        spec_filtered["components"] = filtered_components
    else:
        spec_filtered.pop("components", None)

def build_filtered_spec(spec: Dict[str, Any], selected_paths: Dict[str, Dict[str, Any]], keep_all_components: bool) -> Dict[str, Any]:
    out: Dict[str, Any] = {}

    # Kopieer basis metadata
    for k in ["openapi", "swagger"]:
        if k in spec:
            out[k] = spec[k]
    for k in ["info", "servers", "externalDocs", "tags", "security"]:
        if k in spec:
            out[k] = spec[k]

    # Paths toewijzen
    out["paths"] = {}
    for path, methods in selected_paths.items():
        out["paths"][path] = {}
        for method, op in methods.items():
            out["paths"][path][method] = op

    # Components
    if "components" in spec:
        if keep_all_components:
            out["components"] = spec["components"]
        else:
            out["components"] = {}  # tijdelijk; wordt gepruned
            prune_components(spec, out)
    return out

def main():
    parser = argparse.ArgumentParser(description="Interactively filter endpoints from an OpenAPI YAML/JSON file.")
    parser.add_argument("-i", "--input", type=Path, default=Path("../../TOMP-API.yaml"), help="Path to source OpenAPI file (YAML/JSON).")
    parser.add_argument("-o", "--output", type=Path, default=Path("TOMP-API-filtered.yaml"), help="Path for the filtered OpenAPI YAML.")
    parser.add_argument("--keep-all-components", action="store_true", help="Keep all components unchanged (no pruning).")
    parser.add_argument("--preselect", nargs="*", help='Preselection filters, e.g.: "/users*" "post /login" "get /pets/*"')
    args = parser.parse_args()

    try:
        spec = load_openapi(args.input)
    except Exception as e:
        print(f"Failed to load: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded: {args.input}")
    selected = select_operations(spec, preselect=args.preselect)

    if not selected:
        if not ask_yes_no("No endpoints selected. Still write an empty spec?", default=False):
            print("Aborted.")
            sys.exit(0)

    filtered = build_filtered_spec(spec, selected, keep_all_components=args.keep_all_components)

    try:
        with args.output.open("w", encoding="utf-8") as f:
            yaml.safe_dump(filtered, f, sort_keys=False, allow_unicode=True)
        print(f"Filtered OpenAPI written to: {args.output}")
    except Exception as e:
        print(f"Failed to write: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()