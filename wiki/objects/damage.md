# damage

A damage of the asset.

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetComponent` | enum (`FRONT`, `REAR`, `LEFT`, `RIGHT`, `TOP`, ...) | ✓ | Part/Component of the asset affected. If OTHER is specified the description n... |
| `description` | [longString](longString.md) | ✓ | Description of the damage. |
| `pictures` | array[[url](url.md)] |  | URL where pictures of the damage can be accessed. Any special characters in t... |

## Detailed Properties

- **`assetComponent`**  *(enum (`FRONT`, `REAR`, `LEFT`, `RIGHT`, `TOP`, ...))* - **required**  
  Part/Component of the asset affected. If OTHER is specified the description needs to provide more detail as to what part/component is affected.<br>

- **`description`**  *([longString](longString.md))* - **required**  
  Description of the damage.

- **`pictures`**  *(array[[url](url.md)])* - optional  
  URL where pictures of the damage can be accessed. Any special characters in the URL must be correctly escaped.

## Additional Properties

❌ No additional properties are allowed.

## Example

```json
{
  "assetComponent": "FRONT",
  "description": "example-string",
  "pictures": [
    "https://example.com",
    "https://example.com"
  ]
}
```