# licenseTypeCollection

a list of accepted license types.

**Type:** `object`

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
  **Array item properties:**
  - **`type`**  *(string)* - optional  
    value: "Feature"
  - **`properties`**  *([licenseType](licenseType.md))* - optional  
    A category of license to use a certain asset class.

- **`properties`**  *(object)* - optional  
  - **`type`**  *(enum (`license_types`))* - optional  

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
        "modes": null,
        "type": null,
        "licenseCategory": null,
        "licenseCode": null
      }
    },
    {
      "type": "Feature",
      "properties": {
        "modes": null,
        "type": null,
        "licenseCategory": null,
        "licenseCode": null
      }
    }
  ],
  "properties": {
    "type": "license_types"
  }
}
```

