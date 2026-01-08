#!/usr/bin/env python3
from __future__ import annotations

import argparse
import mimetypes
import os
import yaml
import json
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote

mimetypes.add_type("application/json", ".json")
mimetypes.add_type("text/html", ".html")
mimetypes.add_type("text/yaml", ".yaml")

def pick_format(query_f: str | None, accept: str | None) -> str:
    """
    Return 'html' or 'json'.
    Priority:
      1) explicit ?f=html|json
      2) Accept header (very small heuristic)
      3) default html
    """
    if query_f:
        q = query_f.lower()
        if q in ("html", "text/html"):
            return "html"
        if q in ("json", "application/json"):
            return "json"
        if q in ("yaml", "application/x-yaml"):
            return "yaml"

    accept = (accept or "").lower()
    # If both exist, prefer the first match in header string
    html_pos = accept.find("text/html")
    json_pos = accept.find("application/json")
    yaml_pos = accept.find("application/x-yaml")
    if html_pos != -1 and json_pos != -1:
        return "html" if html_pos < json_pos else "json"
    if html_pos != -1:
        return "html"
    if json_pos != -1:
        return "json"
    if yaml_pos != -1:
        return "yaml"

    return "html"


class Handler(BaseHTTPRequestHandler):
    server_version = "OGC-TestServer/0.1"

    def do_GET(self):
        parsed = urlparse(self.path)
        raw_path = unquote(parsed.path)
        qs = parse_qs(parsed.query)
        f_param = (qs.get("f") or [None])[0]
        accept = self.headers.get("Accept")

        # Normalize path
        if raw_path == "":
            raw_path = "/"

        # If user requests an explicit file, serve it as-is.
        if raw_path.endswith(".html") or raw_path.endswith(".json"):
            return self.serve_file("./static_files/" + raw_path.lstrip("/"))

        # Map "/" to "index"
        base = raw_path.strip("/")
        if base == "":
            base = "index"

        fmt = pick_format(f_param, accept)

        # Special case: index JSON -> landingpage.json
        if base == "index" and fmt == "json":
            filename = "./static_files/landingpage.json"
        elif base == "api" and fmt == "html":
            filename = "api.html"
        elif base == "api" and fmt == "json":
            def load_openapi_yaml(path: str) -> dict:
                with open(path, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)
            spec = load_openapi_yaml("TOMP-API.yaml")
            filename = "TOMP-API.json"
            if not os.path.isfile(filename):
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(spec, f, indent=2)
        elif base == "api":
            filename = "TOMP-API.yaml"
        else:
            filename = f"./static_files/{base}.{fmt}"

        return self.serve_file(filename)

    def serve_file(self, filename: str):
        # Prevent path traversal
        safe = os.path.normpath(filename).lstrip(os.sep)
        if safe.startswith("..") or os.path.isabs(safe):
            return self.send_error(400, "Bad request")

        root = getattr(self.server, "root_dir", os.getcwd())
        fullpath = os.path.join(root, safe)

        if not os.path.isfile(fullpath):
            return self.send_error(404, f"Not found: {safe}")

        ctype, _ = mimetypes.guess_type(fullpath)
        ctype = ctype or "application/octet-stream"

        try:
            with open(fullpath, "rb") as f:
                data = f.read()
        except OSError as e:
            return self.send_error(500, f"Failed to read file: {e}")

        self.send_response(200)
        if ctype == "application/yaml":
            ctype = "text/yaml"
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        # Slightly nicer logs
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), fmt % args))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", default=8000, type=int)
    ap.add_argument("--root", default=".", help="Directory to serve files from")
    args = ap.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    httpd.root_dir = os.path.abspath(args.root)

    print(f"Serving {httpd.root_dir} on http://{args.host}:{args.port}")
    print("Examples:")
    print(f"  http://{args.host}:{args.port}/           -> index.html (default)")
    print(f"  http://{args.host}:{args.port}/?f=json    -> landingpage.json")
    print(f"  http://{args.host}:{args.port}/collections?f=html -> collections.html")
    print(f"  http://{args.host}:{args.port}/collections?f=json -> collections.json")
    print(f"  curl -H 'Accept: application/json' http://{args.host}:{args.port}/ -> landingpage.json")

    httpd.serve_forever()


if __name__ == "__main__":
    main()