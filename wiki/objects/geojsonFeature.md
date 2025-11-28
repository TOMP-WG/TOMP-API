# geojsonFeature

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `geometry` | [geojsonGeometry](geojsonGeometry.md) |  | geoJSON geometry |
| `properties` | [geojsonFeatureProperties](geojsonFeatureProperties.md) | ✓ |  |
| `links` | array[[link](link.md)] |  |  |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "Feature"

- **`id`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`geometry`**  *([geojsonGeometry](geojsonGeometry.md))* - optional  
  geoJSON geometry
  - **`type`**  *(string)* - **required**  
    value: "Point|LineString|Polygon|MultiPolygon"

- **`properties`**  *([geojsonFeatureProperties](geojsonFeatureProperties.md))* - **required**  
  - **`type`**  *(string)* - **required**  
  - **`id`**  *(string)* - **required**  
    short string, display names (length 0-75)

- **`links`**  *(array[[link](link.md)])* - optional  
  **Array item properties:**
  - **`rel`**  *(string)* - **required**  
    the action that can be performed OR part of the URI allowed values include the 'processId's, prefixes for the referenced data sources, prefixes for deeplinks ('apple' and 'android'), OGC compliant ones (alternative, next, etc)
  - **`href`**  *(string (uri))* - **required**  
    valid URL
  - **`type`**  *(string)* - optional  
    allowed values are described by IANA, ("application/geo+json")
  - **`method`**  *(enum (`POST`, `GET`, `DELETE`, `PATCH`))* - optional  
    to indicate the http method.
default: `GET`
  - **`description`**  *(string)* - optional  
    the description of the external data source
  - **`body`**  *(object)* - optional  
    the (prefilled) body for the request
  - **`headers`**  *(object)* - optional  
  - **`mandatory`**  *(boolean)* - optional  
    is this link informative, or must it be used?
  - **`hash`**  *(string)* - optional  
    to validate that the content of the link hasn`t been changed.
  - **`expires`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`availableFrom`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

```json
{
  "type": "Feature",
  "properties": {
    "type": "leg",
    "id": "DBC:Leg:432903:1",
    "specification": { "from": "GPS:52.342,37.342", "startTime": "2025-08-30T10:15:00Z" }
  },
  "id": "432903:1",
  "geometry": {
    "type": "LineString", "geometry": [[]]
  },
  "links": [
    {
      "href": "https://example.com/v1/tomp/processes/start-leg/execution",
      "rel": "start-leg",
      "type": "application/geo+json",
      "method": "POST",
      "description": "start the leg",
      "body": { "inputs": { "package": "DBC:432903", "leg": "1" } }
    },
    {
      "href": "https://example.com/v1/tomp/processes/assign-ancillary/execution",
      "rel": "assign-ancillary",
      "type": "application/geo+json",
      "method": "POST",
      "description": "Add a helmet",
      "body": { "inputs": { "package": "DBC:432903", "leg": "1", "ancillary": "DBC:anc:default-helmet" } }
    }
  ]
}
```
Note: the reference "DBC:anc" should be available in the 'datasources' endpoint, which references machine and/or human readable resources with details about the ancillary products of DBC.

## Example

```json
{
  "type": "Feature",
  "properties": {
    "type": "example-string",
    "id": "identifier"
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