# summary

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [packageReference](packageReference.md) |  | default string, full names etc (length 0-200) |
| `specification` | [travelSpecification](travelSpecification.md) |  |  |
| `price` | [amountOfMoney](amountOfMoney.md) |  | an amount of money, usable in fares, fare calculations or in extra costs. |
| `estimatedPrice` | boolean |  | is this an estimated price; the final price is not known yet. Use the 'fare' ... |
| `products` | array[[productReference](productReference.md)] |  | product names |
| `legs` | array[[legSummary](legSummary.md)] |  |  |
| `labels` | array[enum (`MOST_FLEXIBLE`, `NON_FLEXIBLE`, `MOST_ECO_FRIENDLY`)] |  |  |
| `distribution` | [distribution](distribution.md) |  |  |
| `cancellation` | object |  |  |
| `exchangeable` | boolean |  |  |
| `exchanging` | object |  |  |
| `refundable` | boolean |  |  |
| `transferrable` | boolean |  |  |
| `transfer` | object |  |  |
| `paymentMethod` | object |  |  |

## Detailed Properties

- **`id`**  *([packageReference](packageReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`specification`**  *([travelSpecification](travelSpecification.md))* - optional  
  - **`type`**  *(string)* - optional  
    value: "travelSpecification"
  - **`from`**  *(string)* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'
  - **`via`**  *(array[string])* - optional  
    use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'
  - **`to`**  *(string)* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'
  - **`startTime`**  *(string (date-time))* - optional  
    The intended departure time. If left out and no endTime is set, the current time should be assumed. If only the arrival time is specified, this is an implicit request for a guaranteed arrival at that time.
  - **`endTime`**  *(string (date-time))* - optional  
    The intended arrival time, at the `to place`. When the **startTime** is not set, and **endTime** is set, it is an implicit request for an arrival time guarantee.

- **`price`**  *([amountOfMoney](amountOfMoney.md))* - optional  
  an amount of money, usable in fares, fare calculations or in extra costs.
  - **`amount`**  *(number (float))* - **required**  
    This should be in the base unit as defined by the ISO 4217 currency code with the appropriate number of decimal places and omitting the currency symbol. e.g. if the price is in US Dollars the price would be 9.95. This is inclusive VAT
  - **`taxPercentageUsed`**  *(number (float))* - optional  
    value added tax rate (percentage of amount)
  - **`currencyCode`**  *(string)* - optional  
    value: "[a-zA-Z]{3}"
    ISO 4217 currency code
  - **`vatCountryCode`**  *(string)* - optional  
    value: "[A-Z]{2}"
    two-letter country codes according to ISO 3166-1

- **`estimatedPrice`**  *(boolean)* - optional  
  is this an estimated price; the final price is not known yet. Use the 'fare' link (ref /collections/fares/) in the links section get calculation details.

- **`products`**  *(array[[productReference](productReference.md)])* - optional  
  product names

- **`legs`**  *(array[[legSummary](legSummary.md)])* - optional  
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

- **`distribution`**  *([distribution](distribution.md))* - optional  
  - **`accessType`**  *(enum (`BARCODE`, `QRCODE`, `AZTECCODE`, `REMOTE`, `DEEP_LINK`, ...))* - optional  
    A way to open/access the asset OR a proof of travel rights<br><br> _BARCODE_ a barcode can be retrieved from the links and used to access the purchased service<br> _QRCODE_ a QR code can be retrieved from the links<br> _AZTECCODE_ an Aztec code can be retrieved from the links<br> _REMOTE_ the /processes/start-leg/execution must be used to open the asset<br> _DEEP_LINK_ a deep link into a proprietary app is provided in the links to open the asset (NFC, Bluetooth)<br> _KEY_ a physical key must be obtained (see instructions) to open the asset<br>
  - **`distributionChannel`**  *(string)* - optional  
    default string, full names etc (length 0-200)

- **`cancellation`**  *(object)* - optional  
  - **`cancellable`**  *(boolean)* - optional  
    is it possible to cancel this package?
  - **`fee`**  *([amountOfMoney](amountOfMoney.md))* - optional  
    amount of money you have to pay when you cancel this purchased package
  - **`feePercentage`**  *(number)* - optional  
    percentage of the offered price you have to pay when you cancel this purchased package

- **`exchangeable`**  *(boolean)* - optional  
default: `True`

- **`exchanging`**  *(object)* - optional  
  - **`numberOfExchangesAllowed`**  *(integer)* - optional  

- **`refundable`**  *(boolean)* - optional  
default: `True`

- **`transferrable`**  *(boolean)* - optional  
default: `True`

- **`transfer`**  *(object)* - optional  
  - **`fee`**  *([amountOfMoney](amountOfMoney.md))* - optional  
    an amount of money, usable in fares, fare calculations or in extra costs.
  - **`feePercentage`**  *(number)* - optional  
  - **`maximumNumberOfNamedUsers`**  *(integer)* - optional  

- **`paymentMethod`**  *(object)* - optional  
  - **`paymentType`**  *([typeOfPaymentMethod](typeOfPaymentMethod.md))* - optional  
  - **`deposit`**  *([amountOfMoney](amountOfMoney.md))* - optional  
    the amount of money to pay as a deposit.

## Example

```json
{
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
}
```