# legRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`timestamp`**  *([dateTime](dateTime.md))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`assetLocation`**  *([placeReference](placeReference.md))* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
  - **`userLocation`**  *([placeReference](placeReference.md))* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    This field might lead to GDPR issues. Be aware, use it with caution.
  - **`currentCharge`**  *(integer)* - optional  
    percentage of charge available
  - **`time`**  *([duration](duration.md))* - optional  
    value: "/-?P?=\d|T\d?:\d+Y??:\d+M??:\d+[DW]??:T?:\d+H??:\d+M??:\d+?:\.\d+?S??/"
    time to extend or postpone
  - **`comment`**  *(string)* - optional  
    free text, should match Content-Language
  - **`evidence`**  *(array[[link](link.md)])* - optional  
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
  - **`class`**  *([classOfUse](classOfUse.md))* - optional  
    A classification of fare and other service classes by category of user entitled to use them.

## Example

```json
{
  "inputs": {
    "leg": "example-string",
    "timestamp": "2024-01-15T10:30:00Z",
    "package": "example-string",
    "assetLocation": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+"
  }
}
```

