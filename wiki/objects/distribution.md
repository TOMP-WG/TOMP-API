# distribution

**Type:** `object`

semantics [{'transmodel': 'DISTRIBUTION VALIDITY PARAMETERS'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accessType` | [typeOfTravelDocument](typeOfTravelDocument.md) |  | A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ ... |
| `distributionChannel` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |

## Detailed Properties

- **`accessType`**  *([typeOfTravelDocument](typeOfTravelDocument.md))* - optional  
  A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ a barcode can be retrieved from the links and used to access the purchased service<br> _QRCODE_ a QR code can be retrieved from the links<br> _AZTECCODE_ an Aztec code can be retrieved from the links<br> _REMOTE_ the /processes/start-leg/execution must be used to open the asset<br> _DEEP_LINK_ a deep link into a proprietary app is provided in the links to open the asset (NFC, Bluetooth)<br> _KEY_ a physical key must be obtained (see instructions) to open the asset<br>

- **`distributionChannel`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

## Example

```json
{
  "accessType": "BARCODE",
  "distributionChannel": "example-string"
}
```