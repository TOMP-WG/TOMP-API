# travellerRequirements

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mode` | [mode](mode.md) |  | These classes are taken from the NeTeX standard, but ALL and UNKNOWN are remo... |
| `subMode` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `class` | [classOfUse](classOfUse.md) |  | A classification of fare and other service classes by category of user entitl... |
| `operators` | array[[operatorReference](operatorReference.md)] |  |  |
| `products` | array[[productReference](productReference.md)] |  |  |
| `assets` | array[[assetReference](assetReference.md)] |  |  |
| `zones` | array[[zoneReference](zoneReference.md)] |  |  |
| `distribution` | array[[distribution](distribution.md)] |  |  |
| `avoid` | object |  |  |
| `previousLeg` | object |  | when this leg is part of a sequence, refer to the previous (external) leg |
| `estimatedUsage` | object |  |  |
| `prmNeeds` | array[[prmNeeds](prmNeeds.md)] |  |  |

## Detailed Properties

- **`mode`**  *([mode](mode.md))* - optional  
  These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.

- **`subMode`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`class`**  *([classOfUse](classOfUse.md))* - optional  
  A classification of fare and other service classes by category of user entitled to use them.

- **`operators`**  *(array[[operatorReference](operatorReference.md)])* - optional  

- **`products`**  *(array[[productReference](productReference.md)])* - optional  

- **`assets`**  *(array[[assetReference](assetReference.md)])* - optional  

- **`zones`**  *(array[[zoneReference](zoneReference.md)])* - optional  

- **`distribution`**  *(array[[distribution](distribution.md)])* - optional  
  **Array item properties:**
  - **`accessType`**  *(enum (`BARCODE`, `QRCODE`, `AZTECCODE`, `REMOTE`, `DEEP_LINK`, ...))* - optional  
    A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ a barcode can be retrieved from the links and used to access the purchased service<br> _QRCODE_ a QR code can be retrieved from the links<br> _AZTECCODE_ an Aztec code can be retrieved from the links<br> _REMOTE_ the /processes/start-leg/execution must be used to open the asset<br> _DEEP_LINK_ a deep link into a proprietary app is provided in the links to open the asset (NFC, Bluetooth)<br> _KEY_ a physical key must be obtained (see instructions) to open the asset<br>
  - **`distributionChannel`**  *(string)* - optional  
    default string, full names etc (length 0-200)

- **`avoid`**  *(object)* - optional  
  - **`places`**  *(array[[placeReference](placeReference.md)])* - optional  
  - **`zones`**  *(array[[zoneReference](zoneReference.md)])* - optional  
  - **`lines`**  *(array[[lineReference](lineReference.md)])* - optional  

- **`previousLeg`**  *(object)* - optional  
  when this leg is part of a sequence, refer to the previous (external) leg
  - **`operator`**  *([operatorReference](operatorReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`product`**  *([productReference](productReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`asset`**  *([assetReference](assetReference.md))* - optional  
    default string, full names etc (length 0-200)

- **`estimatedUsage`**  *(object)* - optional  
  - **`time`**  *([duration](duration.md))* - optional  
    value: "/-?P?=\d|T\d?:\d+Y??:\d+M??:\d+[DW]??:T?:\d+H??:\d+M??:\d+?:\.\d+?S??/"
    duration, ISO 8601 compliant
  - **`distanceType`**  *(enum (`KM`, `MILE`))* - optional  
  - **`distance`**  *([float](float.md))* - optional  
    the travelled distance. Only if applicable.

- **`prmNeeds`**  *(array[[prmNeeds](prmNeeds.md)])* - optional  
  **Array item properties:**
  - **`encumbranceNeed`**  *(enum (`pushchair`, `baggage_trolley`, `oversized_baggage`, `luggage_encumbrance`, `guide_dog`, ...))* - optional  
  - **`medicalNeed`**  *(enum (`heart_condition`, `other`))* - optional  
  - **`mobilityNeed`**  *(enum (`wheelchair`, `assisted_wheelchair`, `motorized_wheelchair`, `mobility_scooter`, `road_mobility_scooter`, ...))* - optional  
  - **`psychoSensoryNeed`**  *(enum (`visual_impaired`, `auditory_impaired`, `cognitive_impaired`, `averse_to_lifts`, `averse_to_escalators`, ...))* - optional  

## Example

```json
{
  "mode": "AIR",
  "subMode": "example-string",
  "class": "FIRST_CLASS"
}
```