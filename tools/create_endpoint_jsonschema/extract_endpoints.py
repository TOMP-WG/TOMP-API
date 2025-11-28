from openapi_spec_validator import validate_spec
import yaml
import json

# Laad je OpenAPI specificatie
def load_spec(file_path):
    with open(file_path, 'r') as spec_file:
        return yaml.safe_load(spec_file)

def validate_openapi_spec(spec):
    try:
        validate_spec(spec)
        print("Valid OpenAPI specification.")
    except Exception as e:
        print(f"Invalid OpenAPI specification: {e}")

def resolve_reference(spec, ref):
    parts = ref.lstrip("#/").split("/")
    ref_value = spec
    for part in parts:
        ref_value = ref_value.get(part)
    return ref_value

def resolve_all_references(spec, schema):
    """ Recursively resolve all $refs within a given schema """
    if isinstance(schema, dict):
        if '$ref' in schema:
            ref = schema['$ref']
            resolved = resolve_reference(spec, ref)
            return resolve_all_references(spec, resolved)
        else:
            return {key: resolve_all_references(spec, value) for key, value in schema.items()}
    elif isinstance(schema, list):
        return [resolve_all_references(spec, item) for item in schema]
    else:
        return schema

# Functie om het JSON schema van een endpoint op te halen
def extract_json_schema(spec, endpoint, method, response_code='200'):
    try:
        path_item = spec['paths'].get(endpoint)
        operation = path_item.get(method.lower()) if path_item else None
        
        if not operation:
            raise ValueError(f"Operation '{method}' not found for endpoint '{endpoint}'.")
        
        if response_code not in operation['responses']:
            return None

        response = operation['responses'].get(response_code)

        if '$ref' in response:
            response = resolve_reference(spec, response['$ref'])

        # Volg de $ref naar de content en vervolgens naar het schema, indien aanwezig
        if 'content' in response:
            content = response['content']
        else:
            return None
        if 'application/json' in content:
            content = content['application/json']
        elif 'application/geo+json' in content:
            content = content['application/geo+json']
        else:
            return None
        schema = content['schema']
        if '$ref' in schema:
            schema = resolve_reference(spec, schema['$ref'])

        # content = response['content']['application/json']
        
        return resolve_all_references(spec, schema)
    except Exception as e:
        raise ValueError(f"Error extracting schema: {e}")

# Laad de specificatie opnieuw
spec = load_spec('../../TOMP-API.yaml')
validate_openapi_spec(spec)

# Extract en print het schema
try:
    for path in spec['paths']:
        for method in ['get', 'post', 'patch', 'delete']:
            m = spec['paths'].get(path)
            if method in m:
                schema = extract_json_schema(spec, path, method)  # Pas het pad en de methode aan naar behoefte
                if schema != None:
                    with open(f'''../../static/jsonschemas/{m[method]['operationId']}_{method}.json''', 'w') as out:
                        out.write(json.dumps(schema, indent=2))
                        # out.write(yaml.dump(schema, sort_keys=False))
except Exception as e:
    print(f"Error: {e}")
