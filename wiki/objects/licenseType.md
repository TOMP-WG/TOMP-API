# licenseType

A category of license to use a certain asset class.

**Type:** `object`

semantics [{'transmodel': 'TYPE OF DRIVER PERMIT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  | required when delivered in /collections/license-types/items. |
| `modes` | array[[mode](mode.md)] | ✓ |  |
| `licenseCategory` | enum (`DRIVER_LICENSE`, `OPERATOR_LICENSE`, `OTHER`) |  |  |
| `licenseCode` | [shortString](shortString.md) |  | in most countries a driver license has also a code. As TO you can exactly ver... |
| `issuingCountry` | [country](country.md) |  | two-letter country codes according to ISO 3166-1 |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "licenseType"
  required when delivered in /collections/license-types/items.

- **`modes`**  *(array[[mode](mode.md)])* - **required**  

- **`licenseCategory`**  *(enum (`DRIVER_LICENSE`, `OPERATOR_LICENSE`, `OTHER`))* - optional  

- **`licenseCode`**  *([shortString](shortString.md))* - optional  
  in most countries a driver license has also a code. As TO you can exactly verify, based on this code if the license allows to operate it's assets, if the assetType too generic.

- **`issuingCountry`**  *([country](country.md))* - optional  
  value: "[A-Z]{2}"
  two-letter country codes according to ISO 3166-1

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "modes": [
    "AIR",
    "AIR"
  ],
  "type": "licenseType",
  "licenseCategory": "DRIVER_LICENSE",
  "licenseCode": "example-string"
}
```