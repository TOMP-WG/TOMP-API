# collection

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | ✓ | identifier of the collection used, for example, in URIs |
| `title` | string |  | human readable title of the collection |
| `description` | string |  | a description of the features in the collection |
| `links` | array[[link](link.md)] | ✓ |  |
| `extent` | [extent](extent.md) |  | The extent of the features in the collection. In the Core only spatial and te... |
| `crs` | array[string] |  | the list of coordinate reference systems supported by the service |

## Detailed Properties

- **`id`**  *(string)* - **required**  
  identifier of the collection used, for example, in URIs

- **`title`**  *(string)* - optional  
  human readable title of the collection

- **`description`**  *(string)* - optional  
  a description of the features in the collection

- **`links`**  *(array[[link](link.md)])* - **required**  
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

- **`extent`**  *([extent](extent.md))* - optional  
  The extent of the features in the collection. In the Core only spatial and temporal
extents are specified. Extensions may add additional members to represent other
extents, for example, thermal or pressure ranges.
  - **`spatial`**  *(object)* - optional  
    The spatial extent of the features in the collection.
  - **`temporal`**  *(object)* - optional  
    The temporal extent of the features in the collection.

- **`crs`**  *(array[string])* - optional  
  the list of coordinate reference systems supported by the service
default: `['http://www.opengis.net/def/crs/OGC/1.3/CRS84']`

## Example

```json
{
  "id": "identifier",
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
  "title": "example-string",
  "description": "example-string",
  "extent": {
    "spatial": {
      "bbox": [],
      "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    },
    "temporal": {
      "interval": [],
      "trs": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
    }
  }
}
```