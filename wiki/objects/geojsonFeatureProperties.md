# geojsonFeatureProperties

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [shortString](shortString.md) | ✓ | short string, display names (length 0-75) |

## Detailed Properties

- **`type`**  *(string)* - **required**  

- **`id`**  *([shortString](shortString.md))* - **required**  
  short string, display names (length 0-75)

## Additional Properties

✅ Additional properties of any type are allowed.

```json
{
    "type": "the real type of the feature, like a zone, a bike, a seat, etc",
    ...
}
```

## Example

```json
{
  "type": "example-string",
  "id": "identifier"
}
```