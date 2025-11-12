# binaryTicket

Binary information, like a image or certificate

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contentType` | string | ✓ | the media type (IANA) |
| `base64` | [longString](longString.md) | ✓ | base 64 binary data |

## Detailed Properties

- **`contentType`**  *(string)* - **required**  
  the media type (IANA)

- **`base64`**  *([longString](longString.md))* - **required**  
  base 64 binary data

## Example

```json
{
  "contentType": "example-string",
  "base64": "example-string"
}
```

