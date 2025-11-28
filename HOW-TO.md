# Create a JSONSchema for your endpoint?

A: take these steps:

* run .\merge-API.ps1 in a powershell
* select the modules you want to include, a 'TOMP-API.yaml' is produced
* open the TOMP-API.yaml, look for 'defaultInput:', it references to all known 'inputs', so it includes also inputs you don't want, remove them from the 'oneOf' list.
* Copy & paste the content of the complete file into '<https://editor-next.swagger.io/>'
* if it's correct, there will be no reported errors, only warnings ("All other properties in a "$ref" object are ignored", "Object includes not allowed fields")
* create the JSONSchema ( use 'file' > 'convert and save as JSON')
* store & open the downloaded file.
* take the JSON boiler template below, copy & paste it in a JSONSchema validator like '<https://www.jsonschemavalidator.net/>'
* open the downloaded JSONSchema, copy and paste the content of 'components/schemas' in the validator, in the boiler template (A).
* save the boiler template, you can re-use it for all your input-descriptions.
* for each input (operation request) you can make a copy, and create a validation JSONSchema for it by modifying the copy:
  * replace the tag 'B' (the reference to the input to validate) with your input subclass, adjust

```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Template input JSONSchema",
    "description": "JSON Schema for the request body of input schema",
    "$ref": "#/components/requestBodies/processRequestBody",
    "$comment": "Replace the `inputs` reference in the processRequestBody to create a valid JSONSchema to validate",
    "components": {
        "schemas": {
            "<A: THIS IS WHERE YOU MUST PAST THE 'schemas' PART OF THE DOWNLOADED JSONSchema FILE>"
        },
        "requestBodies": {
            "processRequestBody": {
                "type": "object",
                "properties": {
                    "inputs": {
                        "description": "this body can be replaced by a subtype of defaultInput",
                        "$comment": "This is the place to place your input (must be a subclass of defaultInput)",
                        "$ref": "#/components/schemas/<B: THIS IS WHERE YOU SHOULD PUT YOUR SUBCLASS OF DefaultInput, like searchOfferInput>"
                    },
                    "response": {
                        "type": "string",
                        "enum": [
                            "document"
                        ]
                    },
                    "subscriber": {
                        "type": "object",
                        "required": [
                            "successUrl"
                        ],
                        "properties": {
                            "successUri": {
                                "type": "string",
                                "format": "uri"
                            },
                            "inProgressUri": {
                                "type": "string",
                                "format": "uri"
                            },
                            "failedUri": {
                                "type": "string",
                                "format": "uri"
                            }
                        }
                    }
                },
                "required": [
                    "inputs"
                ]
            }
        }
    }
}
```