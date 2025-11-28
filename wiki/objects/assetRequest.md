# assetRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |
| `subscriber` | object |  |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`timestamp`**  *([dateTime](dateTime.md))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`asset`**  *([assetReference](assetReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`location`**  *([placeReference](placeReference.md))* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.

- **`subscriber`**  *(object)* - optional  
  - **`successUri`**  *(string (uri))* - optional  
  - **`inProgressUri`**  *(string (uri))* - optional  
  - **`failedUri`**  *(string (uri))* - optional  

## Example

```json
{
  "inputs": {
    "asset": "example-string",
    "timestamp": "2024-01-15T10:30:00Z",
    "package": "example-string",
    "leg": "example-string"
  },
  "subscriber": {
    "successUri": "https://example.com",
    "inProgressUri": "https://example.com",
    "failedUri": "https://example.com"
  }
}
```

