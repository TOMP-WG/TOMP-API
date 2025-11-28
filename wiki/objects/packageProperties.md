# packageProperties

a purchased package is a registration of an agreement between end user and TO, to execute a package (=set of legs) according a specification, including all conditions (labels)

**Type:** `object`

semantics [{'transmodel[type!=offer]': 'TRAVEL PACKAGE / CUSTOMER PURCHASE PACKAGE'}, {'transmodel[type==offer]': 'SALES OFFER PACKAGE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [packageReference](packageReference.md) | ✓ | default string, full names etc (length 0-200) |
| `status` | [packageStatus](packageStatus.md) | ✓ | The life-cycle state of the package<br> _OFFERED_ the package is offered (pre... |
| `summary` | [summary](summary.md) |  |  |
| `price` | [fareStructure](fareStructure.md) |  |  |
| `guarantees` | array[[guarantee](guarantee.md)] |  |  |
| `legs` | array[[legProperties](legProperties.md)] |  |  |
| `offers` | array[[summary](summary.md)] |  | contains offered packages, so it is only applicable when the type is package.... |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "offer|package"

- **`id`**  *([packageReference](packageReference.md))* - **required**  
  default string, full names etc (length 0-200)

- **`status`**  *([packageStatus](packageStatus.md))* - **required**  
  The life-cycle state of the package<br> _OFFERED_ the package is offered (pre-sales) <br> _PENDING_ the purchase of the package is not confirmed (the end user has shown intentions to purchase this offer), must be finalized with the package-confirm operation (purchase)<br> _CONFIRMED_ a purchased package. Both parties agreed to deliver services in return of payment<br> _CANCELLED_ the package is cancelled before it is executed. The agreement will specify whether there is a refund, or under which conditions<br> _ROLLBACK_ the package is purchased, but before the Rollback-Expires timestamp has passed, therefore no financial consequences<br> _EXPIRED_ the MP didn't respond on time, the package offer has been expired<br> _STARTED_ the package is started, the <u>trip execution</u> module is needed now to manage the execution of the package<br> _ENDED_ the package has ended, the trip has been executed<br> _RELEASED_ for internal archiving, the package has not been purchased.<br> _SETTLED_ final exit state, services delivered & financial settlement succeeded.

- **`summary`**  *([summary](summary.md))* - optional  
  - **`id`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`specification`**  *(object)* - optional  
  - **`price`**  *(object)* - optional  
    an amount of money, usable in fares, fare calculations or in extra costs.
  - **`estimatedPrice`**  *(boolean)* - optional  
    is this an estimated price; the final price is not known yet. Use the 'fare' link (ref /collections/fares/) in the links section get calculation details.
  - **`products`**  *(array[string])* - optional  
    product names
  - **`legs`**  *(array[object])* - optional  
    **Array item properties:**
    - **`mode`**  *(enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...))* - **required**  
      These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.
    - **`name`**  *(string)* - **required**  
    - **`icon`**  *(string (uri))* - optional  
      valid URL
    - **`destination`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`travellers`**  *(array[string])* - optional  
    - **`equipment`**  *(array[string])* - optional  
    - **`boarding`**  *(object)* - optional  
    - **`accomodation`**  *(object)* - optional  
  - **`labels`**  *(array[enum (`MOST_FLEXIBLE`, `NON_FLEXIBLE`, `MOST_ECO_FRIENDLY`)])* - optional  
  - **`distribution`**  *(object)* - optional  
  - **`cancellation`**  *(object)* - optional  
  - **`exchangeable`**  *(boolean)* - optional  
default: `True`
  - **`exchanging`**  *(object)* - optional  
  - **`refundable`**  *(boolean)* - optional  
default: `True`
  - **`transferrable`**  *(boolean)* - optional  
default: `True`
  - **`transfer`**  *(object)* - optional  
  - **`paymentMethod`**  *(object)* - optional  

- **`price`**  *([fareStructure](fareStructure.md))* - optional  

- **`guarantees`**  *(array[[guarantee](guarantee.md)])* - optional  
  **Array item properties:**
  - **`id`**  *(string)* - optional  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)
  - **`name`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`organisation`**  *(string)* - optional  
    guaranteeing organisation
  - **`type`**  *(enum (`ALTERNATIVE_JOURNEY`, `HOME_LEG`, `RETURN_TO_ORIGIN`, `ON_TIME_TRAVEL`, `TRIP_ON_TIME`, ...))* - optional  
    _ALTERNATIVE_JOURNEY_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY is not available then alternative SERVICE JOURNEY will be provided. -| (EASEMENT_REDRESS, PRODUCT EXCHANGE REDRESS) _HOME_LEG_ - A TRIP REPAIR GUARANTEE that if a the passenger is unable to reach their destination by public transport because of a delay in services, a taxi to their destination will be provided. -| (TAXI HOME REDRESS) _RETURN_TO_ORIGIN_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY cannot be completed, then the passenger will be returned to their origin stop. -| (RETURN TO ORIGIN REDRESS)
_ON_TIME_TRAVEL_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if repeated travel within a certain TIME INTERVAL fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _TRIP_ON_TIME_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a trip fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _FACILITIES_AVAILABLE_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a facility or service (e.g. WIFI, Meal, seat reservation, etc) is not available or fails to meet a specified quality. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ACCOMODATION_ - A TRAVEL QUALITY GUARANTEE that special accommodation will be provided in the event of severe disruption. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ASSISTANCE_ - A TRAVEL QUALITY GUARANTEE that mobility assistance will be provided. -| (ALL REDRESSES, needs SERVICE PARAMETER) _PASSENGER_SUPPORT_ - A TRAVEL QUALITY GUARANTEE that assistance will be provided, for example, if a disruption occurs or a that stations are staffed. (ALL REDRESSES)
_DISRUPTION_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on disruptions will be made available. (ALL REDRESSES) _REDRESS_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on available compensation or other statutory and discretionary redress options will be made available to the passenger. (ALL REDRESSES) _BEST_FARE_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on the best value fares will be made available (ALL REDRESSES)
_GENERAL_TRAVEL_ - An arbitrary OTHER TRAVEL GUARANTEE describing some special guarantee not covered by the normal categories (ALL REDRESSES) _MEDIA_REPLACEMENT_ - An OTHER GUARANTEE that a replacement media will be provided if the original becomes unusable. _REFUND_UNUSED_ANCILLARIES_ - unused ancillaries will be refunded _REFUND_WHEN_CANCELLED_ - when cancelled before start, a refund will be scheduled

- **`legs`**  *(array[[legProperties](legProperties.md)])* - optional  
  **Array item properties:**
  - **`type`**  *(string)* - **required**  
    value: "leg"
  - **`id`**  *(string)* - **required**  
    The unique identifier (TO) of this leg. Must always the same as applied in the request URL. And when there are not additional legs in the offered or purchased package, the same **id** as the package id.
  - **`specification`**  *(object)* - **required**  
  - **`sequenceNumber`**  *(integer)* - optional  
    The order of the leg within the package. Mandatory, if there are multiple legs in the package. If there are parallel legs (eg. using parking lot and a renting a bike), it can be the same within one package.
default: `0`
  - **`mode`**  *(enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...))* - optional  
    These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.
  - **`status`**  *(enum (`NOT_STARTED`, `PREPARING`, `READY_TO_USE`, `IN_USE`, `PAUSED`, ...))* - optional  
    status of a leg<br> _NOT_STARTED_ the leg is not started, initial state<br> _PREPARING_ the _PREPARE_ operation has been received<br> _READY_TO_USE_ the leg is ready to use<br> _IN_USE_ the travellers are on their way<br> _PAUSED_ the asset is paused<br> _ENDING_ the end-leg request is received, the offboarding process has is started<br> _ENDED_ the travellers have arrived at their destination, leg is final<br> _ISSUE_REPORTED_ due to an issue, there is (temporarily) no progress to report, when the issue isn't solved, this is a final state<br> _CANCELLED_ the leg has been cancelled, before execution<br> _ABENDED_ the leg is abnormally ended (e.g. due to an issue)
  - **`travellers`**  *(array[string])* - optional  
  - **`products`**  *(array[string])* - optional  
    The main product (v1.x 'asset type') used to execute this leg
  - **`ancillaries`**  *(array[string])* - optional  
    additional products that can be assigned to this leg
  - **`assets`**  *(array[string])* - optional  
    The physical asset(s) used for the execution of the leg
  - **`operatorId`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`operatorName`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`labels`**  *(array[enum (`REFUNDABLE`, `EXCHANGABLE`, `CANCELLABLE`, `TRANSFERABLE`, `DEPOSIT_REQUIRED`, ...)])* - optional  
  - **`returnLocations`**  *(array[string])* - optional  

- **`offers`**  *(array[[summary](summary.md)])* - optional  
  contains offered packages, so it is only applicable when the type is package. When a package only contains one offer, this property should be neglected. All references in the offers refer to the products the packageProperties. Optional - the offers can be retrieved using the /collections/offers/items?offerId={reference} endpoint.
  **Array item properties:**
  - **`id`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`specification`**  *(object)* - optional  
  - **`price`**  *(object)* - optional  
    an amount of money, usable in fares, fare calculations or in extra costs.
  - **`estimatedPrice`**  *(boolean)* - optional  
    is this an estimated price; the final price is not known yet. Use the 'fare' link (ref /collections/fares/) in the links section get calculation details.
  - **`products`**  *(array[string])* - optional  
    product names
  - **`legs`**  *(array[object])* - optional  
    **Array item properties:**
    - **`mode`**  *(enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...))* - **required**  
      These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.
    - **`name`**  *(string)* - **required**  
    - **`icon`**  *(string (uri))* - optional  
      valid URL
    - **`destination`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`travellers`**  *(array[string])* - optional  
    - **`equipment`**  *(array[string])* - optional  
    - **`boarding`**  *(object)* - optional  
    - **`accomodation`**  *(object)* - optional  
  - **`labels`**  *(array[enum (`MOST_FLEXIBLE`, `NON_FLEXIBLE`, `MOST_ECO_FRIENDLY`)])* - optional  
  - **`distribution`**  *(object)* - optional  
  - **`cancellation`**  *(object)* - optional  
  - **`exchangeable`**  *(boolean)* - optional  
default: `True`
  - **`exchanging`**  *(object)* - optional  
  - **`refundable`**  *(boolean)* - optional  
default: `True`
  - **`transferrable`**  *(boolean)* - optional  
default: `True`
  - **`transfer`**  *(object)* - optional  
  - **`paymentMethod`**  *(object)* - optional  

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "type": "offer|package",
  "id": "identifier",
  "status": "OFFERED",
  "summary": {
    "id": "identifier",
    "specification": {
      "type": "travelSpecification",
      "from": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
      "via": []
    },
    "price": {
      "amount": 3.14,
      "taxPercentageUsed": 0,
      "currencyCode": "[a-zA-Z]{3}",
      "vatCountryCode": "[A-Z]{2}"
    }
  },
  "price": {
    "amount": 3.14,
    "taxPercentageUsed": 0,
    "currencyCode": "[a-zA-Z]{3}",
    "vatCountryCode": "[A-Z]{2}",
    "elements": [
      {
        "amount": 3.14,
        "taxPercentageUsed": 0,
        "currencyCode": "[a-zA-Z]{3}",
        "vatCountryCode": "[A-Z]{2}",
        "type": "FIXED",
        "priceCondition": "DEFAULT",
        "units": "KM",
        "amountOfUnits": 0
      },
      {
        "amount": 3.14,
        "taxPercentageUsed": 0,
        "currencyCode": "[a-zA-Z]{3}",
        "vatCountryCode": "[A-Z]{2}",
        "type": "FIXED",
        "priceCondition": "DEFAULT",
        "units": "KM",
        "amountOfUnits": 0
      }
    ],
    "id": "identifier",
    "estimated": true,
    "description": "example-string"
  },
  "guarantees": [
    {
      "id": "identifier",
      "name": "example-string",
      "organisation": "example-string"
    },
    {
      "id": "identifier",
      "name": "example-string",
      "organisation": "example-string"
    }
  ]
}
```