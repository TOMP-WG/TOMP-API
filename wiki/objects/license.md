# license

driver or usage license for a specific user. Contains the number and the assetType you're allowed to operate (e.g. driver license for CAR)

**Type:** `object`

semantics [{'transmodel': 'ACCEPTED DRIVER PERMIT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `licenseType` | [licenseType](licenseType.md) |  | the type of license, like a driver license, or a license to operate a |
| `licenseNumber` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `endValidity` | [date](date.md) |  | https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12) |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "license"

- **`licenseType`**  *([licenseType](licenseType.md))* - optional  
  the type of license, like a driver license, or a license to operate a
  - **`type`**  *(string)* - optional  
    value: "licenseType"
    required when delivered in /collections/license-types/items.
  - **`modes`**  *(array[enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...)])* - **required**  
  - **`licenseCategory`**  *(enum (`DRIVER_LICENSE`, `OPERATOR_LICENSE`, `OTHER`))* - optional  
  - **`licenseCode`**  *(string)* - optional  
    in most countries a driver license has also a code. As TO you can exactly verify, based on this code if the license allows to operate it's assets, if the assetType too generic.
  - **`issuingCountry`**  *(string)* - optional  
    value: "[A-Z]{2}"
    two-letter country codes according to ISO 3166-1
  - **`customFields`**  *(object)* - optional  
    dictionary for extra fields (bilatural agreements)

- **`licenseNumber`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`endValidity`**  *([date](date.md))* - optional  
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12)

## Example

```json
{
  "type": "license",
  "licenseType": {
    "modes": [
      "AIR",
      "AIR"
    ],
    "type": "licenseType",
    "licenseCategory": "DRIVER_LICENSE",
    "licenseCode": "example-string"
  },
  "licenseNumber": "example-string"
}
```