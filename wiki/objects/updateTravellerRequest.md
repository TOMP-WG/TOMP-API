# updateTravellerRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`traveller`**  *([travellerReference](travellerReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`age`**  *([shortInt](shortInt.md))* - optional  
    Age of the traveller, may be approximate
default: `0`
  - **`fullName`**  *([normalString](normalString.md))* - optional  
    the name of the traveller, can be used to validate against ID cards
  - **`characteristics`**  *([travellerCharacteristics](travellerCharacteristics.md))* - optional  
    the COMPLETE set of entitlements, replaces the previous set of entitlements of this traveller

## Example

```json
{
  "inputs": {
    "traveller": "example-string",
    "package": "example-string",
    "age": 0,
    "fullName": "example-string"
  }
}
```

