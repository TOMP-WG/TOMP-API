# ancillaryCollection

a list of available ancillaries.

**Type:** `object`

semantics [{'transmodel': 'ANCILLARY PRODUCTs'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `features` | array[object] |  |  |
| `properties` | object |  |  |
| `numberMatched` | number |  |  |
| `numberReturned` | number |  |  |
| `links` | array[[link](link.md)] |  | actions that can be performed on this package, but also alternative (rel=alte... |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "FeatureCollection"

- **`features`**  *(array[object])* - optional  

- **`properties`**  *(object)* - optional  
  - **`type`**  *(string)* - **required**  
    value: "ancillaryCollection"

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
      "type": "Feature",
      "properties": {
        "type": "ancillary",
        "name": "Simple child seat",
        "description": "can carry a child up to 12 kilo"
      },
      "id": "a08e8360-a070-41cf-801f-c66ca69c32cc",
      "links": [
        {
          "href": "https://example.com/tomp/v2/processes/assign-ancillary/execution",
          "rel": "assign-ancillary",
          "body": { "inputs": { "ancillary": "a08e8360-a070-41cf-801f-c66ca69c32cc",
                                "package": "2b35e746-1a0b-4826-bb41-d733ca025e31" } },
          "type": "application/geo+json",
          "method": "POST"
        }
      ] 
    }
  ],
  "properties": {
    "type": "ancillaryCollection"
  }
}
```