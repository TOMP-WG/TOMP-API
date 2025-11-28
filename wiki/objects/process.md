# process

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [processSummary](processSummary.md)
2. object
   - Properties: `inputs`, `outputs`, `subscriber`

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
  ],
  "inputs": {},
  "outputs": {},
  "subscriber": {
    "successUri": "https://example.com",
    "inProgressUri": "https://example.com",
    "failedUri": "https://example.com"
  }
}
```

