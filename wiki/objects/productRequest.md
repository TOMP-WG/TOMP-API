# productRequest

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
  - **`location`**  *([placeReference](placeReference.md))* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
  - **`package`**  *([packageReference](packageReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`product`**  *([productReference](productReference.md))* - **required**  
    default string, full names etc (length 0-200)

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "product": "example-string",
    "timestamp": "2024-01-15T10:30:00Z",
    "location": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+"
  }
}
```

