# geojsonGeometry

geoJSON geometry

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "Point|LineString|Polygon|MultiPolygon"

## Composition (oneOf)

This schema must match **exactly one** of the following schemas:

1. [geojsonPoint](geojsonPoint.md)
   - Geojson Coordinate
   - Properties: `coordinates`
2. [geojsonLine](geojsonLine.md)
   - An array of WGS84 coordinate pairs
   - Properties: `coordinates`
3. [geojsonPolygon](geojsonPolygon.md)
   - geojson representation of a polygon. First and last point must be equal. See also https://geojson.org/geojson-spec.html#polygon and example https://geojson.org/geojson-spec.html#id4. The order should be lon, lat [[[lon1, lat1], [lon2,lat2], [lon3,lat3], [lon1,lat1]]], the first point should match the last point.
   - Properties: `coordinates`
4. [geojsonMultiPolygon](geojsonMultiPolygon.md)
   - geojson representation of a multi polygon. See also https://geojson.org/geojson-spec.html#multipolygon
   - Properties: `coordinates`

## Example

```json
{
  "type": "Point|LineString|Polygon|MultiPolygon"
}
```