# processSummary

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [descriptionType](descriptionType.md)
   - Properties: `title`, `description`, `keywords`, `metadata`, `additionalParameters`
2. object
   - Properties: `id`, `version`, `jobControlOptions`, `outputTransmission`, `links`

## Example

```json
{
  "title": "example-string",
  "description": "example-string",
  "keywords": [
    "example-string",
    "example-string"
  ],
  "id": "identifier",
  "version": "example-string",
  "jobControlOptions": [
    "sync-execute",
    "sync-execute"
  ],
  "outputTransmission": [
    "value",
    "value"
  ],
  "links": [
    {
      "href": "https://example.com",
      "rel": "example-string",
      "type": "example-string",
      "method": "POST",
      "description": "example-string"
    },
    {
      "href": "https://example.com",
      "rel": "example-string",
      "type": "example-string",
      "method": "POST",
      "description": "example-string"
    }
  ]
}
```