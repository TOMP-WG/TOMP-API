# links

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `links` | array[[link](link.md)] |  |  |

## Detailed Properties

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

## Example

```json
{
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