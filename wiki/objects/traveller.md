# traveller

**Type:** `object`

semantics [{'transmodel': 'INDIVIDUAL TRAVELLER'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [travellerReference](travellerReference.md) | ✓ | default string, full names etc (length 0-200) |
| `characteristics` | [travellerCharacteristics](travellerCharacteristics.md) |  |  |
| `requirements` | [travellerRequirements](travellerRequirements.md) |  |  |
| `profile` | [userProfileReference](userProfileReference.md) |  | default string, full names etc (length 0-200) |
| `groupSize` | number |  | in case of a travelling party, specify the (sub)group size with equivalent at... |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "traveller"

- **`id`**  *([travellerReference](travellerReference.md))* - **required**  
  default string, full names etc (length 0-200)

- **`characteristics`**  *([travellerCharacteristics](travellerCharacteristics.md))* - optional  
  - **`isValidated`**  *(boolean)* - optional  
    Whether this traveller's identity and properties have been verified by the MaaS provider
  - **`name`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`age`**  *(integer)* - optional  
    Age of the traveller, may be approximate
default: `0`
  - **`fullName`**  *(string)* - optional  
    the name of the traveller, can be used to validate against ID cards
  - **`customerReference`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`entitlements`**  *(array[object])* - optional  
    entitlements or commercial profiles that are applicable to this traveller
    **Array item properties:**
    - **`id`**  *(string)* - **required**  
      an ID for this entitlement or commercial profile.
    - **`type`**  *(string)* - **required**  
      value: "entitlement|commercialProfile"
    - **`description`**  *(string)* - **required**  
      default string, full names etc (length 0-200)
  - **`cardTypes`**  *(array[object])* - optional  
    card types that are applicable to this traveller
    **Array item properties:**
    - **`id`**  *(string)* - **required**  
      external reference to address the card used.
    - **`type`**  *(string)* - **required**  
      value: "cardType"
    - **`cardCategory`**  *(enum (`DISCOUNT`, `TRAVEL`, `BANK`, `CREDIT`, `ID`, ...))* - optional  
      The broad category of card<br> DISCOUNT - discount card, can be applied in the purchase process to get rebate<br> TRAVEL - (external) travel card, possibly paid for in other context, but also monthly, weekly or day-cards<br> BANK - bank card<br> CREDIT - credit card<br> ID - identification card, like an ID card<br> PASSPORT - passport to identify yourself<br> OTHER - unspecified
    - **`subType`**  *(string)* - optional  
      For use in case of OTHER. Can be used in bilateral agreements.
    - **`modes`**  *(array[enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...)])* - optional  
      modes for which this card can be used, when empty, all modes are allowed
    - **`relatedProduct`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`transportOrganisations`**  *(array[string])* - optional  
      references to accepting parties, only if applicable
    - **`customFields`**  *(object)* - optional  
      dictionary for extra fields (bilatural agreements)
  - **`cards`**  *(array[object])* - optional  
    cards that are applicable to this traveller
    **Array item properties:**
    - **`type`**  *(string)* - **required**  
      value: "card"
    - **`cardType`**  *(string)* - **required**  
      the type of card, like a credit card, ID card, etc.
    - **`cardNumber`**  *(string)* - **required**  
      number of the card, like ID number, credit card or bank account number
    - **`description`**  *(string)* - optional  
      description of the card
    - **`additionalNumber`**  *(string)* - optional  
      additional number, like CVC code or IBAN code
    - **`endValidity`**  *(string (full-date))* - optional  
      this card is valid until this date
  - **`licenseTypes`**  *(array[object])* - optional  
    license types that are applicable to this traveller
    **Array item properties:**
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
  - **`licenses`**  *(array[object])* - optional  
    licenses that are applicable to this traveller
    **Array item properties:**
    - **`type`**  *(string)* - optional  
      value: "license"
    - **`licenseType`**  *(object)* - optional  
      the type of license, like a driver license, or a license to operate a
    - **`licenseNumber`**  *(string)* - optional  
      short string, display names (length 0-75)
    - **`endValidity`**  *(string (full-date))* - optional  
      https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12)
  - **`assets`**  *(array[string])* - optional  

- **`requirements`**  *([travellerRequirements](travellerRequirements.md))* - optional  
  - **`mode`**  *(enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...))* - optional  
    These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.
  - **`subMode`**  *(string)* - optional  
    short string, display names (length 0-75)
  - **`class`**  *(enum (`FIRST_CLASS`, `SECOND_CLASS`, `THIRD_CLASS`, `ECONOMY_CLASS`, `BUSINESS_CLASS`, ...))* - optional  
    A classification of fare and other service classes by category of user entitled to use them.
  - **`operators`**  *(array[string])* - optional  
  - **`products`**  *(array[string])* - optional  
  - **`assets`**  *(array[string])* - optional  
  - **`zones`**  *(array[string])* - optional  
  - **`distribution`**  *(array[object])* - optional  
    **Array item properties:**
    - **`accessType`**  *(enum (`BARCODE`, `QRCODE`, `AZTECCODE`, `REMOTE`, `DEEP_LINK`, ...))* - optional  
      A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ a barcode can be retrieved from the links and used to access the purchased service<br> _QRCODE_ a QR code can be retrieved from the links<br> _AZTECCODE_ an Aztec code can be retrieved from the links<br> _REMOTE_ the /processes/start-leg/execution must be used to open the asset<br> _DEEP_LINK_ a deep link into a proprietary app is provided in the links to open the asset (NFC, Bluetooth)<br> _KEY_ a physical key must be obtained (see instructions) to open the asset<br>
    - **`distributionChannel`**  *(string)* - optional  
      default string, full names etc (length 0-200)
  - **`avoid`**  *(object)* - optional  
  - **`previousLeg`**  *(object)* - optional  
    when this leg is part of a sequence, refer to the previous (external) leg
  - **`estimatedUsage`**  *(object)* - optional  
  - **`prmNeeds`**  *(array[object])* - optional  
    **Array item properties:**
    - **`encumbranceNeed`**  *(enum (`pushchair`, `baggage_trolley`, `oversized_baggage`, `luggage_encumbrance`, `guide_dog`, ...))* - optional  
    - **`medicalNeed`**  *(enum (`heart_condition`, `other`))* - optional  
    - **`mobilityNeed`**  *(enum (`wheelchair`, `assisted_wheelchair`, `motorized_wheelchair`, `mobility_scooter`, `road_mobility_scooter`, ...))* - optional  
    - **`psychoSensoryNeed`**  *(enum (`visual_impaired`, `auditory_impaired`, `cognitive_impaired`, `averse_to_lifts`, `averse_to_escalators`, ...))* - optional  

- **`profile`**  *([userProfileReference](userProfileReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`groupSize`**  *(number)* - optional  
  in case of a travelling party, specify the (sub)group size with equivalent attributes

## Example

```json
{
  "type": "traveller",
  "id": "identifier",
  "characteristics": {
    "isValidated": true,
    "name": "example-string",
    "age": 0
  },
  "requirements": {
    "mode": "AIR",
    "subMode": "example-string",
    "class": "FIRST_CLASS"
  },
  "profile": "example-string"
}
```