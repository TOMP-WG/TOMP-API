import yaml
import json
import sys
from pathlib import Path

def resolve_schema(schema, components):
    """Recursief resolven van $ref, integreren van `allOf`, en verwerken van `required`, inclusief referenties in arrays."""
    if isinstance(schema, dict):
        # Als er een $ref is, volg die referentie en haal het schema op
        if '$ref' in schema:
            ref = schema['$ref'].split('/')[-1]  # Haal het laatste gedeelte van de $ref
            item = components.get('schemas', {}).get(ref, {})
            if item == {}:
                item = components.get('requestBodies', {}).get(ref, {})
            if item == {}:
                item = components.get('responses', {}).get(ref, {})
            return resolve_schema(item, components)
        
        # Als het schema een combinator zoals allOf, anyOf of oneOf bevat, los die dan op
        resolved_schema = {}
        if 'allOf' in schema:
            # Integreer alle objecten in allOf
            combined_properties = {}
            combined_required = []  # Lijst voor het combineren van de vereiste velden
            for subschema in schema['allOf']:
                resolved_subschema = resolve_schema(subschema, components)
                if 'properties' in resolved_subschema:
                    combined_properties.update(resolved_subschema['properties'])
                else:
                    resolved_schema = resolved_subschema
                if 'required' in resolved_subschema:
                    # Voeg de vereiste velden samen, maar zonder duplicaten
                    combined_required = list(set(combined_required + resolved_subschema['required']))              
            
            if len(combined_properties.items()) > 0:
                resolved_schema['properties'] = combined_properties
            if combined_required:
                resolved_schema['required'] = combined_required

        # Voeg andere eigenschappen van het schema toe, zoals type, description, etc.
        for key, value in schema.items():
            if key not in ['allOf', 'anyOf', 'oneOf']:
                if not key.startswith('x'):
                    resolved_schema[key] = value
            if key == 'discriminator':
                one_of = {}
                if 'mapping' in value:
                    for k,v in value['mapping'].items():
                        ref = v.split('/')[-1]  # Haal het laatste gedeelte van de $ref
                        ref_schema = components.get('schemas', {}).get(ref, {})
                        one_of[ref] = resolve_schema(ref_schema, components)
                    resolved_schema['oneOf'] = one_of

        # Recursief de properties controleren op $ref en andere constraints zoals pattern, minLength, etc.
        if 'properties' in resolved_schema:
            for prop_name, prop_schema in resolved_schema['properties'].items():
                s = resolve_schema(prop_schema, components)
                resolved_schema['properties'][prop_name] = s

        # Verwerk de 'required' eigenschap op objectniveau (zonder duplicaten)
        if 'required' in schema:
            if 'required' not in resolved_schema:
                resolved_schema['required'] = []
            resolved_schema['required'] = list(set(resolved_schema['required'] + schema['required']))

        # Verwerk arrays die referenties bevatten
        if 'items' in resolved_schema:
            resolved_schema['items'] = resolve_schema(resolved_schema['items'], components)

        return resolved_schema
    return schema

def extract_endpoints_from_openapi(openapi_file):
    # Lees de originele OpenAPI specificatie
    with open(openapi_file, 'r', encoding='UTF-16') as file:
        openapi_spec = yaml.safe_load(file)

    collections_json = {}
    processes_json = {}

    for path, methods in openapi_spec.get('paths', {}).items():
        if '/execute' in path or ('/items' in path and not '/items/' in path):
            for method, operation in methods.items():
                new_json_schema = {}
                if 'requestBody' in operation:
                    ref = operation['requestBody'].get('$ref', {})
                    if ref != {}:
                        content = resolve_schema(operation['requestBody'], openapi_spec['components']).get('content', {})
                    else:
                        content = operation['requestBody'].get('content', {})
                    for content_type, content_schema in content.items():
                        # Als het schema een referentie is, voeg die dan toe aan de JSON Schema
                        if '$ref' in content_schema.get('schema', {}):
                            ref = content_schema['schema']['$ref']
                            ref_schema = openapi_spec['components']['schemas'].get(ref.split('/')[-1])
                            if ref_schema:
                                new_json_schema[ref.split('/')[-1]] = resolve_schema(ref_schema, openapi_spec['components'])
                        else:
                            # Als het schema niet een $ref is, voeg het schema direct toe
                            new_json_schema['request'] = resolve_schema(content_schema['schema'], openapi_spec['components'])['properties']

                if 'responses' in operation:
                    for status, response in operation['responses'].items():
                        if status == '200':
                            ref = response.get('$ref', {})
                            if ref != {}:
                                content = resolve_schema(response, openapi_spec['components']).get('content', {})
                            else:
                                content = response.get('content', {})

                            responses_json = {}
                               
                            for content_type, content_schema in content.items():
                                # Als het schema een referentie is, voeg die dan toe aan de JSON Schema
                                if '$ref' in content_schema.get('schema', {}):
                                    ref = content_schema['schema']['$ref']
                                    ref_schema = openapi_spec['components']['schemas'].get(ref.split('/')[-1])
                                    if ref_schema:
                                        responses_json[ref.split('/')[-1]] = resolve_schema(ref_schema, openapi_spec['components'])
                                else:
                                    # Als het schema niet een $ref is, voeg het schema direct toe
                                    responses_json['response'] = resolve_schema(content_schema['schema'], openapi_spec['components'])

                            keys = responses_json.keys()
                            if len(keys) == 1:
                                k = list(keys)[0]
                                new_json_schema[k] = responses_json[k]
                            else:
                                new_json_schema['oneOf'] = responses_json

                with open('./output' + path.replace('/processes', '').replace('/collections','').replace('/execute','').replace('/items','') + '.json', 'w') as file:
                    json.dump(new_json_schema, file, indent=2)

    with open('./output/collections.json', 'w') as file:
        json.dump(collections_json, file, indent=2)
    with open('./output/processes.json', 'w') as file:
        json.dump(processes_json, file, indent=2)

    return new_json_schema

def main():

    if len(sys.argv) == 1:
        openapi_file = '../../TOMP-API.yaml'
    else:
        openapi_file = sys.argv[1] 

    directory = Path('./output')
    for file in directory.iterdir():
        if file.is_file():
            file.unlink()

    extract_endpoints_from_openapi(openapi_file)

if __name__ == '__main__':
    main()