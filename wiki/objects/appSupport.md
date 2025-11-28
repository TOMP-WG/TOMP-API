# appSupport

attributes to display/use in an external app.

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `displayName` | [shortString](shortString.md) |  | displayable name for this asset |
| `description` | [longString](longString.md) |  | the description of the asset |
| `image` | [url](url.md) |  | Link to an image of the asset |
| `icon` | [url](url.md) |  | Link to an icon of the asset |
| `accessMethods` | array[[typeOfTravelDocument](typeOfTravelDocument.md)] |  | how this asset can be opened |

## Detailed Properties

- **`displayName`**  *([shortString](shortString.md))* - optional  
  displayable name for this asset

- **`description`**  *([longString](longString.md))* - optional  
  the description of the asset

- **`image`**  *([url](url.md))* - optional  
  Link to an image of the asset

- **`icon`**  *([url](url.md))* - optional  
  Link to an icon of the asset

- **`accessMethods`**  *(array[[typeOfTravelDocument](typeOfTravelDocument.md)])* - optional  
  how this asset can be opened

## Example

```json
{
  "displayName": "Blizz Jumper (Normal bike)",
  "description": "A simple uni-sex bike",
  "image": "https://images.com/transport/simple_bike.jpg"
}
```