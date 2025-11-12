# supportTicket

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [uuid](uuid.md) |  | ticketID, to be provided when created. Mandatory when status != REQUESTED |
| `type` | string | ✓ |  |
| `status` | [supportTicketStatus](supportTicketStatus.md) |  | _ISSUE_REQUESTED_ the ticket is new, to be processed by the TO<br> _ISSUE_OPE... |
| `supportType` | enum (`BROKEN_DOWN`, `NOT_AT_LOCATION`, `MISSING_AFTER_PAUSE`, `NOT_CLEAN`, `NOT_AVAILABLE`, ...) | ✓ | these are the currently enlisted support requests<br> _BROKEN_DOWN_ The asset... |
| `context` | object |  |  |
| `location` | [placeReference](placeReference.md) | ✓ | this string references to information that can be found in the `data sources`... |
| `timestamp` | [dateTime](dateTime.md) | ✓ | the reporting timestamp of the support request |
| `priority` | enum (`ERROR_CANNOT_CONTINUE`, `ERROR_CAN_CONTINUE`, `DISTURBING_ISSUE`, `QUESTION`, `OTHER`) |  | the priority of the support request. |
| `contactInformationEndUser` | [normalString](normalString.md) |  | contact information of the end user in case of direct response requests, like... |
| `comment` | [longString](longString.md) |  | long string, memos etc (length 0-10.000) |
| `urls` | array[[url](url.md)] |  | urls to clarify the support request e.g. pictures showing damage or digital s... |
| `requestedResponseTime` | [shortInt](shortInt.md) |  | time to respond in minutes. |
| `timeToResolution` | [shortInt](shortInt.md) |  | time in minutes to the expected resolution of support request |
| `damage` | [damage](damage.md) |  | A damage of the asset. |
| `sequence` | [tinyInt](tinyInt.md) |  | the sequence number of the status of tickets on this issue |
| `links` | [links](links.md) |  |  |

## Detailed Properties

- **`id`**  *([uuid](uuid.md))* - optional  
  ticketID, to be provided when created. Mandatory when status != REQUESTED

- **`type`**  *(string)* - **required**  
  value: "supportTicket"

- **`status`**  *([supportTicketStatus](supportTicketStatus.md))* - optional  
  _ISSUE_REQUESTED_ the ticket is new, to be processed by the TO<br> _ISSUE_OPEN_ the ticket is open, we're on our way<br> _ISSUE_UPDATE_REQUESTED_ we're waiting on a response of the traveller(s)<br> _ISSUE_RESOLVED_ Issue succesfully closed<br> _ISSUE_REVOKED_ Issue revoked<br>

- **`supportType`**  *(enum (`BROKEN_DOWN`, `NOT_AT_LOCATION`, `MISSING_AFTER_PAUSE`, `NOT_CLEAN`, `NOT_AVAILABLE`, ...))* - **required**  
  these are the currently enlisted support requests<br> _BROKEN_DOWN_ The asset doesn't work anymore<br> _NOT_AT_LOCATION_ The asset isn't available at the specified time/location<br> _MISSING_AFTER_PAUSE_ The asset is missing (stolen?)<br> _NOT_CLEAN_ The asset is not clean<br> _NOT_AVAILABLE_ The asset is at the location, but unreachable<br> _UNABLE_TO_OPEN_ The asset cannot be unlocked (malfunctioning)<br> _UNABLE_TO_CLOSE_ The asset cannot be closed (malfunctioning)<br> _ACCIDENT_ Accident occurred<br> _OTHER_ unspecified<br> _REPORT_DAMAGE_ Oeps. Photo sent with slight damage<br> _REQUEST_ASSISTANCE_ request personal assistance, e.g. to get into the train<br> _EVIDENCE_ Send evidence to the TO for redress functions<br>

- **`context`**  *(object)* - optional  
  - **`asset`**  *([assetReference](assetReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`product`**  *([productReference](productReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)

- **`location`**  *([placeReference](placeReference.md))* - **required**  
  value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
  this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.

- **`timestamp`**  *([dateTime](dateTime.md))* - **required**  
  the reporting timestamp of the support request

- **`priority`**  *(enum (`ERROR_CANNOT_CONTINUE`, `ERROR_CAN_CONTINUE`, `DISTURBING_ISSUE`, `QUESTION`, `OTHER`))* - optional  
  the priority of the support request.

- **`contactInformationEndUser`**  *([normalString](normalString.md))* - optional  
  contact information of the end user in case of direct response requests, like phone number

- **`comment`**  *([longString](longString.md))* - optional  
  long string, memos etc (length 0-10.000)

- **`urls`**  *(array[[url](url.md)])* - optional  
  urls to clarify the support request e.g. pictures showing damage or digital scans with evidence documents

- **`requestedResponseTime`**  *([shortInt](shortInt.md))* - optional  
  time to respond in minutes.
default: `0`

- **`timeToResolution`**  *([shortInt](shortInt.md))* - optional  
  time in minutes to the expected resolution of support request
default: `0`

- **`damage`**  *([damage](damage.md))* - optional  
  A damage of the asset.
  - **`assetComponent`**  *(enum (`FRONT`, `REAR`, `LEFT`, `RIGHT`, `TOP`, ...))* - **required**  
    Part/Component of the asset affected. If OTHER is specified the description needs to provide more detail as to what part/component is affected.<br>
  - **`description`**  *(string)* - **required**  
    Description of the damage.
  - **`pictures`**  *(array[string (uri)])* - optional  
    URL where pictures of the damage can be accessed. Any special characters in the URL must be correctly escaped.

- **`sequence`**  *([tinyInt](tinyInt.md))* - optional  
  the sequence number of the status of tickets on this issue
default: `0`

- **`links`**  *([links](links.md))* - optional  
  - **`links`**  *(array[object])* - optional  
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
  "supportType": "BROKEN_DOWN",
  "type": "supportTicket",
  "location": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "identifier",
  "status": "ISSUE_REQUESTED",
  "context": {
    "asset": "example-string",
    "leg": "example-string",
    "product": "example-string"
  }
}
```

