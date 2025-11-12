# ancillary

**Type:** `object`

semantics [{'transmodel': 'ANCILLARY PRODUCT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `id` | [ancillaryReference](ancillaryReference.md) | ✓ | default string, full names etc (length 0-200) |
| `name` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `description` | [longString](longString.md) |  | long string, memos etc (length 0-10.000) |
| `product` | [productReference](productReference.md) |  | default string, full names etc (length 0-200) |
| `image` | [url](url.md) |  | Link to an image of the ancillary |
| `fee` | [fareStructure](fareStructure.md) |  |  |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "ancillary"

- **`id`**  *([ancillaryReference](ancillaryReference.md))* - **required**  
  default string, full names etc (length 0-200)

- **`name`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`description`**  *([longString](longString.md))* - optional  
  long string, memos etc (length 0-10.000)

- **`product`**  *([productReference](productReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`image`**  *([url](url.md))* - optional  
  Link to an image of the ancillary

- **`fee`**  *([fareStructure](fareStructure.md))* - optional  

## Example

```json
{
  "type": "ancillary",
  "id": "b6e03978-699e-4b57-82e1-31653afcb359",
  "name": "Simple bike"
}
```