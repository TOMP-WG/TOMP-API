# processIdentifier

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `module` | enum (`offers`, `pre-sales`, `purchase`, `execute`, `support`, ...) | ✓ |  |
| `identifiers` | array[[shortString](shortString.md)] | ✓ |  |

## Detailed Properties

- **`module`**  *(enum (`offers`, `pre-sales`, `purchase`, `execute`, `support`, ...))* - **required**  

- **`identifiers`**  *(array[[shortString](shortString.md)])* - **required**  

## Example

```json
{
  "module": "offers",
  "identifiers": [
    "example-string",
    "example-string"
  ]
}
```