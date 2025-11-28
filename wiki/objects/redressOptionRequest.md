# redressOptionRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`package`**  *([packageReference](packageReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`offer`**  *([offerReference](offerReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`guarantee`**  *([uuid](uuid.md))* - **required**  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)
  - **`option`**  *([uuid](uuid.md))* - **required**  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "guarantee": "example-string",
    "option": "example-string",
    "offer": "example-string"
  }
}
```

