# travellerCharacteristics

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isValidated` | boolean |  | Whether this traveller's identity and properties have been verified by the Ma... |
| `name` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |
| `age` | [shortInt](shortInt.md) |  | Age of the traveller, may be approximate |
| `fullName` | [normalString](normalString.md) |  | the name of the traveller, can be used to validate against ID cards |
| `customerReference` | [customerReference](customerReference.md) |  | default string, full names etc (length 0-200) |
| `entitlements` | array[[entitlementGiven](entitlementGiven.md)] |  | entitlements or commercial profiles that are applicable to this traveller |
| `cardTypes` | array[[cardType](cardType.md)] |  | card types that are applicable to this traveller |
| `cards` | array[[card](card.md)] |  | cards that are applicable to this traveller |
| `licenseTypes` | array[[licenseType](licenseType.md)] |  | license types that are applicable to this traveller |
| `licenses` | array[[license](license.md)] |  | licenses that are applicable to this traveller |
| `assets` | array[[assetReference](assetReference.md)] |  |  |

## Detailed Properties

- **`isValidated`**  *(boolean)* - optional  
  Whether this traveller's identity and properties have been verified by the MaaS provider

- **`name`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

- **`age`**  *([shortInt](shortInt.md))* - optional  
  Age of the traveller, may be approximate
default: `0`

- **`fullName`**  *([normalString](normalString.md))* - optional  
  the name of the traveller, can be used to validate against ID cards

- **`customerReference`**  *([customerReference](customerReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`entitlements`**  *(array[[entitlementGiven](entitlementGiven.md)])* - optional  
  entitlements or commercial profiles that are applicable to this traveller
  **Array item properties:**
  - **`id`**  *(string)* - **required**  
    an ID for this entitlement or commercial profile.
  - **`type`**  *(string)* - **required**  
    value: "entitlement|commercialProfile"
  - **`description`**  *(string)* - **required**  
    default string, full names etc (length 0-200)

- **`cardTypes`**  *(array[[cardType](cardType.md)])* - optional  
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

- **`cards`**  *(array[[card](card.md)])* - optional  
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

- **`licenseTypes`**  *(array[[licenseType](licenseType.md)])* - optional  
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

- **`licenses`**  *(array[[license](license.md)])* - optional  
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

- **`assets`**  *(array[[assetReference](assetReference.md)])* - optional  

## Example

```json
{
  "isValidated": true,
  "name": "example-string",
  "age": 0
}
```