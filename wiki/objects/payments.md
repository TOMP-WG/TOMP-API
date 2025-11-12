# payments

a list of offers.

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `features` | array[object] |  |  |
| `properties` | object |  | this object contains the filter parameters |
| `numberMatched` | number |  |  |
| `numberReturned` | number |  |  |
| `links` | array[[link](link.md)] |  | actions that can be performed on this package, but also alternative (rel=alte... |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "FeatureCollection"

- **`features`**  *(array[object])* - optional  
  **Array item properties:**
  - **`type`**  *(string)* - optional  
    value: "Feature"
  - **`id`**  *([uuid](uuid.md))* - optional  
    https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)
  - **`properties`**  *([financialDetail](financialDetail.md))* - optional  
  - **`links`**  *(array[[link](link.md)])* - optional  
    **Array item properties:**
    - **`rel`**  *(string)* - **required**  
      the action that can be performed OR part of the URI allowed values include the 'processId's, prefixes for the referenced data sources, prefixes for deeplinks ('apple' and 'android'), OGC compliant ones (alternative, next, etc)
    - **`href`**  *(string (uri))* - **required**  
      valid URL
    - **`type`**  *(string)* - optional  
      allowed values are described by IANA, ("application/geo+json")
    - **`method`**  *(enum (`POST`, `GET`, `DELETE`, `PATCH`))* - optional  
      to indicate the http method.
default: `GET`
    - **`description`**  *(string)* - optional  
      the description of the external data source
    - **`body`**  *(object)* - optional  
      the (prefilled) body for the request
    - **`headers`**  *(object)* - optional  
    - **`mandatory`**  *(boolean)* - optional  
      is this link informative, or must it be used?
    - **`hash`**  *(string)* - optional  
      to validate that the content of the link hasn`t been changed.
    - **`expires`**  *(string (date-time))* - optional  
      https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
    - **`availableFrom`**  *(string (date-time))* - optional  
      https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

- **`properties`**  *(object)* - optional  
  this object contains the filter parameters
  - **`type`**  *(string)* - optional  
    value: "paymentCollection"
  - **`limit`**  *(integer)* - optional  
  - **`offset`**  *(integer)* - optional  
  - **`startTime`**  *([dateTime](dateTime.md))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`endTime`**  *([dateTime](dateTime.md))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`invoiceState`**  *([paymentState](paymentState.md))* - optional  
    the state of the payment detail
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`category`**  *([paymentCategory](paymentCategory.md))* - optional  
    The category of the journalled item <br> _ALL_ - for filtering purposes only<br>
<h2>TO initiated payments </h2> To request these payments, use the notifications, send a notification containing the payment confirmation.<br> _DEPOSIT_ - a deposit, to refund, use _REFUND_<br> _DAMAGE_ - extra costs that must be paid by the MP due to damage to the asset or ancillaries<br> _LOSS_ - extra costs that must be paid by the MP due to loss of asset or ancillaries<br> _STOLEN_ - the asset (and ancillaries) are stolen and should be paid for<br> _EXTRA_USAGE_ - the asset is paid for in advance, additional usage must be paid for (can also be a refund when used less! The amount should be negative in that case)<br> _FINE_ - a fine that arrived later on<br> _OTHER_ASSET_USED_ - additional costs for a replaced asset<br> _FARE_ - the normal costs of the purchased and executiond leg(s)<br> _OTHER_ - unspecified<br>
_CREDIT_ - generic CREDIT, e.g. for kick-backs <br> _VOUCHER_ - part of the fare that is covered by a voucher (no need to pay)<br> _REFUND_ - refund of the deposit or upfront paid fare<br> _REBATE_ - (partial) rebate of the fare<br> _REIMBURSEMENT_ - reimbursement of the fare<br>

- **`numberMatched`**  *(number)* - optional  

- **`numberReturned`**  *(number)* - optional  

- **`links`**  *(array[[link](link.md)])* - optional  
  actions that can be performed on this package, but also alternative (rel=alternative+1, alternative+2) offers or references to other resources In case it is an alternative, specify clearly in the description what the financial consequences are.
  **Array item properties:**
  - **`rel`**  *(string)* - **required**  
    the action that can be performed OR part of the URI allowed values include the 'processId's, prefixes for the referenced data sources, prefixes for deeplinks ('apple' and 'android'), OGC compliant ones (alternative, next, etc)
  - **`href`**  *(string (uri))* - **required**  
    valid URL
  - **`type`**  *(string)* - optional  
    allowed values are described by IANA, ("application/geo+json")
  - **`method`**  *(enum (`POST`, `GET`, `DELETE`, `PATCH`))* - optional  
    to indicate the http method.
default: `GET`
  - **`description`**  *(string)* - optional  
    the description of the external data source
  - **`body`**  *(object)* - optional  
    the (prefilled) body for the request
  - **`headers`**  *(object)* - optional  
  - **`mandatory`**  *(boolean)* - optional  
    is this link informative, or must it be used?
  - **`hash`**  *(string)* - optional  
    to validate that the content of the link hasn`t been changed.
  - **`expires`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`availableFrom`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

## Example

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "identifier",
      "properties": {
        "amount": 3.14,
        "taxPercentageUsed": 0,
        "currencyCode": "[a-zA-Z]{3}",
        "vatCountryCode": "[A-Z]{2}",
        "id": "identifier",
        "category": "ALL",
        "state": "TO_INVOICE"
      }
    },
    {
      "type": "Feature",
      "id": "identifier",
      "properties": {
        "amount": 3.14,
        "taxPercentageUsed": 0,
        "currencyCode": "[a-zA-Z]{3}",
        "vatCountryCode": "[A-Z]{2}",
        "id": "identifier",
        "category": "ALL",
        "state": "TO_INVOICE"
      }
    }
  ],
  "properties": {
    "type": "paymentCollection",
    "limit": 42,
    "offset": 42
  }
}
```

