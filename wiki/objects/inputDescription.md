# inputDescription

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [descriptionType](descriptionType.md)
   - Properties: `title`, `description`, `keywords`, `metadata`, `additionalParameters`
2. object
   - Properties: `minOccurs`, `maxOccurs`, `schema`

## Example

```json
{
  "title": "example-string",
  "description": "example-string",
  "keywords": [
    "example-string",
    "example-string"
  ],
  "schema": {},
  "minOccurs": 1,
  "maxOccurs": "example-string"
}
```

