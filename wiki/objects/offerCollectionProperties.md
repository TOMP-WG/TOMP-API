# offerCollectionProperties

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. object
   - Properties: `type`
2. [geojsonCollectionProperties](geojsonCollectionProperties.md)
   - Properties: `type`, `id`, `definitions`

## Example

```json
{
  "type": "example-string",
  "id": "identifier",
  "definitions": {
    "products": [
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null,
        "parts": null
      },
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null,
        "parts": null
      }
    ],
    "places": [],
    "ancillaries": [
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null
      },
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null
      }
    ]
  }
}
```

