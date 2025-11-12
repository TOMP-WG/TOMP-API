# removeOfferRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    reference to the package to remove the offer of
  - **`offer`**  *([offerReference](offerReference.md))* - optional  
    reference to the offer to remove from the specified package

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "offer": "example-string"
  }
}
```

