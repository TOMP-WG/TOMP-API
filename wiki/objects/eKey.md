# eKey

Axa EKey information

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ekey` | object | ✓ |  |
| `lock` | object | ✓ |  |

## Detailed Properties

- **`ekey`**  *(object)* - **required**  
  - **`key`**  *([longString](longString.md))* - optional  
    certificate
  - **`passkey`**  *([longString](longString.md))* - optional  
    one time pass key

- **`lock`**  *(object)* - **required**  
  - **`bdAddress`**  *([longString](longString.md))* - optional  
    physical address
  - **`deviceName`**  *([normalString](normalString.md))* - optional  
    how it advertises itself

## Example

```json
{
  "ekey": {
    "key": "example-string",
    "passkey": "example-string"
  },
  "lock": {
    "bdAddress": "example-string",
    "deviceName": "example-string"
  }
}
```

