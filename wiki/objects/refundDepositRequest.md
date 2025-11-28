# refundDepositRequest

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
  - **`leg`**  *([legReference](legReference.md))* - optional  
    default string, full names etc (length 0-200)

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "leg": "example-string"
  }
}
```

