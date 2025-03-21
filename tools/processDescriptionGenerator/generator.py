import logging
from typing import Optional

import prance

OPENAPI_SPEC_VALIDATOR = 'openapi-spec-validator'

logger = logging.getLogger(__name__)

class OpenAPIResolver:
    _resolver: prance.ResolvingParser

    def __init__(self, uri: Optional[str]) -> None:
        self._resolver = prance.ResolvingParser(
            uri,
            backend=OPENAPI_SPEC_VALIDATOR,
            strict=False,
            lazy=False
        )

    def resolve(self) -> dict:
        """Resolve OpenAPI specification with Prance parser

        Returns:
            dict: Normalized and parsed specification as a dictionary

        Raises:
            ParserError: If some validation or parsing error occurred
        """
        logger.debug(f"Resolving specification file")
        self._resolver.parse()
        return self._resolver.specification

parser: OpenAPIResolver = OpenAPIResolver('TOMP-API.yaml')
dict = parser.resolve()

# test: searchOfferInput

components = dict['components']
schemas = components['schemas']

def createJson(type, body):
    if type == 'allOf' or 'allOf' in body:
        return createJsonBasedOnAllOf(body)
    elif type == 'oneOf' or 'oneOf' in body:
        return createJsonBasedOnOneOf(body)
    elif 'type' in body:
        return createJsonBasedOnType(body)
    return {}        

def createJsonBasedOnType(body):
    type = body['type']
    if type == 'object':
        return createJsonObject(body)
    elif type == 'array':
        return createJsonArray(body)
    elif type == 'string':
        return createJsonString(body)
    elif type == 'number' or type == 'float':
        return createJsonNumber(body)

def createJsonBasedOnAllOf(body):
    # allOf:
    #     - type: object
    #     - type: object
    #     - type: object
    result = {}
    if len(body) == 1:
        for key, value in body.items():
            result = createJson(None, value[0])
    else:
        for item in body:
            json = createJson(None, item)
            for key, value in json.items():
                result[key] = value
    return result

def createJsonBasedOnOneOf(body):
    return {}

def createJsonObject(body):
    result = {}
    for name, property in body['properties'].items():
        json = createJson(None, property)
        result[name] = json
    return result

def createJsonArray(body):
    result = {}
    result['items'] = {}
    for k,v in body.items():
        if k != 'items':
            result[k] = v
        else:
            for k2,v2 in body['items'].items():
                result['items'] = createJson(k2, v2)
    return result

def createJsonString(body):
    return body

def createJsonNumber(body):
    return body

item = 'searchOfferInput'
json = {}
for type, schema in schemas[item].items():
    json = createJson(type, schema)

print(json)
