# geojsonPolygon

geojson representation of a polygon. First and last point must be equal. See also https://geojson.org/geojson-spec.html#polygon and example https://geojson.org/geojson-spec.html#id4. The order should be lon, lat [[[lon1, lat1], [lon2,lat2], [lon3,lat3], [lon1,lat1]]], the first point should match the last point.

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `coordinates` | array[array[array[number (float)]]] | ✓ |  |

## Detailed Properties

- **`coordinates`**  *(array[array[array[number (float)]]])* - **required**  

## Example

```json
{
  "coordinates": [
    [
      [],
      []
    ],
    [
      [],
      []
    ]
  ]
}
```

