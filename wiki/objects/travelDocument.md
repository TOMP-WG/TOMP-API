# travelDocument

**Type:** `object`

semantics [{'transmodel': 'TRAVEL DOCUMENT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string |  |  |
| `type` | string | ✓ |  |
| `validity` | [dateTimeRange](dateTimeRange.md) | ✓ |  |
| `package` | [packageReference](packageReference.md) |  | default string, full names etc (length 0-200) |
| `leg` | [legReference](legReference.md) |  | default string, full names etc (length 0-200) |
| `asset` | [assetReference](assetReference.md) |  | default string, full names etc (length 0-200) |
| `traveller` | [travellerReference](travellerReference.md) |  | default string, full names etc (length 0-200) |
| `travelDocumentType` | [typeOfTravelDocument](typeOfTravelDocument.md) | ✓ | A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ ... |

## Detailed Properties

- **`id`**  *(string)* - optional  

- **`type`**  *(string)* - **required**  
  value: "travelDocument"

- **`validity`**  *([dateTimeRange](dateTimeRange.md))* - **required**  

- **`package`**  *([packageReference](packageReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`leg`**  *([legReference](legReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`asset`**  *([assetReference](assetReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`traveller`**  *([travellerReference](travellerReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`travelDocumentType`**  *([typeOfTravelDocument](typeOfTravelDocument.md))* - **required**  
  A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ a barcode can be retrieved from the links and used to access the purchased service<br> _QRCODE_ a QR code can be retrieved from the links<br> _AZTECCODE_ an Aztec code can be retrieved from the links<br> _REMOTE_ the /processes/start-leg/execution must be used to open the asset<br> _DEEP_LINK_ a deep link into a proprietary app is provided in the links to open the asset (NFC, Bluetooth)<br> _KEY_ a physical key must be obtained (see instructions) to open the asset<br>

## Composition (oneOf)

This schema must match **exactly one** of the following schemas:

1. [externalDigitalTicket](externalDigitalTicket.md)
   - External ticket, can be accessed using the links collection, with rel=ticket the mediatype tells what it refers to.
   - Properties: `customFields`
2. [binaryTicket](binaryTicket.md)
   - Binary information, like a image or certificate
   - Properties: `contentType`, `base64`
3. [eKey](eKey.md)
   - Axa EKey information
   - Properties: `ekey`, `lock`
4. [customProperties](customProperties.md)
   - dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "validity": [
    "2024-01-15T10:30:00Z",
    "2024-01-15T10:30:00Z"
  ],
  "travelDocumentType": "BARCODE",
  "type": "travelDocument",
  "id": "identifier",
  "package": "example-string",
  "leg": "example-string"
}
```

