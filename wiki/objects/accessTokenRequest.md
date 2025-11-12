# accessTokenRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `grant_type` | string | ✓ |  |
| `scope` | string | ✓ |  |
| `client_id` | string | ✓ |  |
| `client_assertion_type` | string | ✓ |  |
| `client_assertion` | string | ✓ |  |

## Detailed Properties

- **`grant_type`**  *(string)* - **required**  

- **`scope`**  *(string)* - **required**  

- **`client_id`**  *(string)* - **required**  

- **`client_assertion_type`**  *(string)* - **required**  

- **`client_assertion`**  *(string)* - **required**  

## Example

```json
{
  "grant_type": "example-string",
  "scope": "example-string",
  "client_id": "example-string",
  "client_assertion_type": "example-string",
  "client_assertion": "example-string"
}
```