# searchOfferRequest

A package planning request, resulting in offers

**Type:** `object`

semantics [{'transmodel': 'TRIP REQUEST'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `specification` | object | ✓ |  |
| `requirements` | [travellerRequirements](travellerRequirements.md) |  |  |
| `travellers` | array[[traveller](traveller.md)] |  |  |
| `places` | array[[place](place.md)] |  | Places that are not specified in an external data source (like a home address) |
| `packageToExchange` | [packageReference](packageReference.md) |  | default string, full names etc (length 0-200) |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "searchOffer"

- **`specification`**  *(object)* - **required**  

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

- **`travellers`**  *(array[[traveller](traveller.md)])* - optional  
  **Array item properties:**
  - **`type`**  *(string)* - **required**  
    value: "traveller"
  - **`id`**  *(string)* - **required**  
    default string, full names etc (length 0-200)
  - **`characteristics`**  *(object)* - optional  
  - **`requirements`**  *(object)* - optional  
  - **`profile`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`groupSize`**  *(number)* - optional  
    in case of a travelling party, specify the (sub)group size with equivalent attributes

- **`places`**  *(array[[place](place.md)])* - optional  
  Places that are not specified in an external data source (like a home address)
  **Array item properties:**
  - **`id`**  *(string)* - **required**  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
  - **`type`**  *(string)* - optional  
    value: "place"
  - **`addressLine1`**  *(string)* - **required**  
    contains street, housenumber & additions example street 18, 2nd floor, 18-B33
  - **`addressLine2`**  *(string)* - optional  
    city or town, principal subdivision such as province, state or county Smallcity, Pinetree county
  - **`street`**  *(string)* - optional  
    street, consistent with addressLine1
  - **`houseNumber`**  *(integer)* - optional  
    house number, consistent with addressLine1
default: `0`
  - **`houseNumberAddition`**  *(string)* - optional  
    the additional part of the house number (f.x. 13bis, where 'bis' is the additional part), consistent with addressLine1
  - **`postalCode`**  *(string)* - optional  
    the postal code, whenever available
  - **`city`**  *(string)* - optional  
    specified city or town, consistent with addressLine2
  - **`province`**  *(string)* - optional  
    province or region, consistent with addressLine2
  - **`state`**  *(string)* - optional  
    state, consistent with addressLine2
  - **`country`**  *(string)* - optional  
    value: "[A-Z]{2}"
    two-letter country codes according to ISO 3166-1
  - **`additionalInfo`**  *(string)* - optional  
    additional information to find the address (f.x. just around the corner)

- **`packageToExchange`**  *([packageReference](packageReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "type": "searchOffer",
  "specification": "example-string",
  "requirements": {
    "mode": "AIR",
    "subMode": "example-string",
    "class": "FIRST_CLASS"
  },
  "travellers": [
    {
      "type": "traveller",
      "id": "identifier",
      "characteristics": {
        "isValidated": null,
        "name": null,
        "age": null
      },
      "requirements": {
        "mode": null,
        "subMode": null,
        "class": null
      },
      "profile": "example-string"
    },
    {
      "type": "traveller",
      "id": "identifier",
      "characteristics": {
        "isValidated": null,
        "name": null,
        "age": null
      },
      "requirements": {
        "mode": null,
        "subMode": null,
        "class": null
      },
      "profile": "example-string"
    }
  ],
  "places": []
}
```