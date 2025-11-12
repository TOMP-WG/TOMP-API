# offerFeature

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [geojsonFeature](geojsonFeature.md)
   - Properties: `type`, `id`, `geometry`, `properties`, `links`
2. object
   - a single offer, the 'package' in a single feature
   - Properties: `type`, `properties`

## Example

```json
{
  "type": "offer",
  "properties": {
    "id": "identifier",
    "specification": {
      "type": "travelSpecification",
      "from": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
      "via": []
    },
    "price": {
      "amount": 3.14,
      "taxPercentageUsed": 0,
      "currencyCode": "[a-zA-Z]{3}",
      "vatCountryCode": "[A-Z]{2}"
    }
  },
  "id": "identifier",
  "geometry": {
    "type": "Point|LineString|Polygon|MultiPolygon"
  },
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

