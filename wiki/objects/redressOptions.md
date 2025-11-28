# redressOptions

**Type:** `object`

semantics [{'transmodel': 'TRAVEL REDRESSes'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `features` | array[object] |  |  |
| `properties` | object |  |  |
| `numberMatched` | number |  |  |
| `numberReturned` | number |  |  |
| `links` | array[[link](link.md)] |  | actions that can be performed on this package, but also alternative (rel=alte... |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "FeatureCollection"

- **`features`**  *(array[object])* - optional  
  **Array item properties:**
  - **`id`**  *([uuid](uuid.md))* - optional  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)
  - **`type`**  *(string)* - optional  
    value: "Feature"
  - **`properties`**  *([redressOption](redressOption.md))* - optional  
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

- **`properties`**  *(object)* - optional  
  - **`type`**  *(string)* - optional  
    value: "redressOptions"
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`offer`**  *([offerReference](offerReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`guarantee`**  *([uuid](uuid.md))* - optional  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)

- **`numberMatched`**  *(number)* - optional  

- **`numberReturned`**  *(number)* - optional  

- **`links`**  *(array[[link](link.md)])* - optional  
  actions that can be performed on this package, but also alternative (rel=alternative+1, alternative+2) offers or references to other resources In case it is an alternative, specify clearly in the description what the financial consequences are.
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
  "type": "FeatureCollection",
  "features": [
    {
      "id": "identifier",
      "type": "Feature",
      "properties": {
        "type": null,
        "id": null,
        "packageState": null
      }
    },
    {
      "id": "identifier",
      "type": "Feature",
      "properties": {
        "type": null,
        "id": null,
        "packageState": null
      }
    }
  ],
  "properties": {
    "type": "redressOptions",
    "package": "example-string",
    "offer": "example-string"
  },
  "numberMatched": 3.14
}
```

