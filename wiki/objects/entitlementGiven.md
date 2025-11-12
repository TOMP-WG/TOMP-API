# entitlementGiven

**Type:** `object`

semantics [{'transmodel': 'ENTITLEMENT GIVEN, COMMERCIAL_PROFILE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [entitlementReference](entitlementReference.md) | ✓ | an ID for this entitlement or commercial profile. |
| `type` | string | ✓ |  |
| `description` | [normalString](normalString.md) | ✓ | default string, full names etc (length 0-200) |

## Detailed Properties

- **`id`**  *([entitlementReference](entitlementReference.md))* - **required**  
  an ID for this entitlement or commercial profile.

- **`type`**  *(string)* - **required**  
  value: "entitlement|commercialProfile"

- **`description`**  *([normalString](normalString.md))* - **required**  
  default string, full names etc (length 0-200)

## Example

```json
{
  "id": "identifier",
  "type": "entitlement|commercialProfile",
  "description": "example-string"
}
```