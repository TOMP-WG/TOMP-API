# Generate static OGC files 

## Install python 

We used version 3.11, but any newer python version could work as well.

## Python environmnent

optional
```bash
pyton -m venv . AND .\scripts\activate
```

```bash
pip install -r requirements.txt
```

## Generate content (all in /static files directory)

```bash
python gen_landingpage.py --openapi ./static_files/TOMP-API.yaml --out-dir ./static_files
```

```bash
python gen_conformance.py --openapi ./static_files/TOMP-API.yaml --out-dir ./static_files
```

```bash
python gen_collections.py --openapi ./static_files/TOMP-API.yaml --out-dir ./static_files
```

```bash
python gen_processes.py --openapi ./static_files/TOMP-API.yaml --out-dir ./static_files --templates ./templates
```

## Validate

```bash
python testserver.py
``` 

and navigate to http://localhost:8080/.