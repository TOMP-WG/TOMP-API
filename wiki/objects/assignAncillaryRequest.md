# assignAncillaryRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ | this can be used to assign an ancillary to a leg, by using the field `ancilla... |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  this can be used to assign an ancillary to a leg, by using the field `ancillary`. If you want to replace an ancillary, fill the field `replacesAncillary` with the ancillary to replace and `ancillary` with the new one. If you want to remove an assigned ancillary from a leg, fill `ancillary` with 'null' and fill `replacesAncillary` with the ancillary to remove.
  - **`package`**  *([packageReference](packageReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`ancillary`**  *([ancillaryReference](ancillaryReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`replacesAncillary`**  *([ancillaryReference](ancillaryReference.md))* - optional  
    default string, full names etc (length 0-200)

## Example

```json
{
  "inputs": {
    "package": "432d4a65-9d94-4519-876d-dc5389a2671c",
    "leg": "304f2e8e-50e7-4aeb-b4f2-6f528df4c676",
    "ancillary": "simple bike 01"
  }
}
```