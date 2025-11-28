# bankAccount

bank account

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | [shortString](shortString.md) | ✓ | account name |
| `number` | [shortString](shortString.md) | ✓ | account number |
| `country` | [country](country.md) |  | two-letter country codes according to ISO 3166-1 |
| `bankIdentification` | [shortString](shortString.md) |  | bank identification, like BIC code |

## Detailed Properties

- **`name`**  *([shortString](shortString.md))* - **required**  
  account name

- **`number`**  *([shortString](shortString.md))* - **required**  
  account number

- **`country`**  *([country](country.md))* - optional  
  value: "[A-Z]{2}"
  two-letter country codes according to ISO 3166-1

- **`bankIdentification`**  *([shortString](shortString.md))* - optional  
  bank identification, like BIC code

## Additional Properties

❌ No additional properties are allowed.

## Example

```json
{
  "name": "example-string",
  "number": "example-string",
  "country": "[A-Z]{2}",
  "bankIdentification": "example-string"
}
```

