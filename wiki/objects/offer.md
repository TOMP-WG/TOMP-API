# offer

**Type:** `object`

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [geojsonFeature](geojsonFeature.md)
   - Properties: `type`, `id`, `geometry`, `properties`, `links`
2. object
   - an offer for a package to execute a trip
   - Properties: `properties`

## Example

```json
{
  "type": "Feature",
  "properties": {
    "type": "offer|package",
    "id": "identifier",
    "status": "OFFERED",
    "summary": {
      "id": "identifier",
      "specification": {
        "type": null,
        "from": null,
        "via": null
      },
      "price": {
        "amount": null,
        "taxPercentageUsed": null,
        "currencyCode": null,
        "vatCountryCode": null
      }
    },
    "price": {
      "amount": 3.14,
      "taxPercentageUsed": 0,
      "currencyCode": "[a-zA-Z]{3}",
      "vatCountryCode": "[A-Z]{2}",
      "elements": [
        {
          "amount": 3.14,
          "taxPercentageUsed": 0,
          "currencyCode": "[a-zA-Z]{3}",
          "vatCountryCode": "[A-Z]{2}",
          "type": "FIXED",
          "priceCondition": "DEFAULT",
          "units": "KM",
          "amountOfUnits": 0
        },
        {
          "amount": 3.14,
          "taxPercentageUsed": 0,
          "currencyCode": "[a-zA-Z]{3}",
          "vatCountryCode": "[A-Z]{2}",
          "type": "FIXED",
          "priceCondition": "DEFAULT",
          "units": "KM",
          "amountOfUnits": 0
        }
      ],
      "id": "identifier",
      "estimated": true,
      "description": "example-string"
    },
    "guarantees": [
      {
        "id": null,
        "name": null,
        "organisation": null
      },
      {
        "id": null,
        "name": null,
        "organisation": null
      }
    ]
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

