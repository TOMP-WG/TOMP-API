# supportRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | [supportTicket](supportTicket.md) | ✓ |  |

## Detailed Properties

- **`inputs`**  *([supportTicket](supportTicket.md))* - **required**  
  - **`id`**  *(string)* - optional  
    ticketID, to be provided when created. Mandatory when status != REQUESTED
  - **`type`**  *(string)* - **required**  
    value: "supportTicket"
  - **`status`**  *(enum (`ISSUE_REQUESTED`, `ISSUE_OPEN`, `ISSUE_UPDATE_REQUESTED`, `ISSUE_RESOLVED`, `ISSUE_REVOKED`))* - optional  
    _ISSUE_REQUESTED_ the ticket is new, to be processed by the TO<br> _ISSUE_OPEN_ the ticket is open, we're on our way<br> _ISSUE_UPDATE_REQUESTED_ we're waiting on a response of the traveller(s)<br> _ISSUE_RESOLVED_ Issue succesfully closed<br> _ISSUE_REVOKED_ Issue revoked<br>
  - **`supportType`**  *(enum (`BROKEN_DOWN`, `NOT_AT_LOCATION`, `MISSING_AFTER_PAUSE`, `NOT_CLEAN`, `NOT_AVAILABLE`, ...))* - **required**  
    these are the currently enlisted support requests<br> _BROKEN_DOWN_ The asset doesn't work anymore<br> _NOT_AT_LOCATION_ The asset isn't available at the specified time/location<br> _MISSING_AFTER_PAUSE_ The asset is missing (stolen?)<br> _NOT_CLEAN_ The asset is not clean<br> _NOT_AVAILABLE_ The asset is at the location, but unreachable<br> _UNABLE_TO_OPEN_ The asset cannot be unlocked (malfunctioning)<br> _UNABLE_TO_CLOSE_ The asset cannot be closed (malfunctioning)<br> _ACCIDENT_ Accident occurred<br> _OTHER_ unspecified<br> _REPORT_DAMAGE_ Oeps. Photo sent with slight damage<br> _REQUEST_ASSISTANCE_ request personal assistance, e.g. to get into the train<br> _EVIDENCE_ Send evidence to the TO for redress functions<br>
  - **`context`**  *(object)* - optional  
  - **`location`**  *(string)* - **required**  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
  - **`timestamp`**  *(string (date-time))* - **required**  
    the reporting timestamp of the support request
  - **`priority`**  *(enum (`ERROR_CANNOT_CONTINUE`, `ERROR_CAN_CONTINUE`, `DISTURBING_ISSUE`, `QUESTION`, `OTHER`))* - optional  
    the priority of the support request.
  - **`contactInformationEndUser`**  *(string)* - optional  
    contact information of the end user in case of direct response requests, like phone number
  - **`comment`**  *(string)* - optional  
    long string, memos etc (length 0-10.000)
  - **`urls`**  *(array[string (uri)])* - optional  
    urls to clarify the support request e.g. pictures showing damage or digital scans with evidence documents
  - **`requestedResponseTime`**  *(integer)* - optional  
    time to respond in minutes.
default: `0`
  - **`timeToResolution`**  *(integer)* - optional  
    time in minutes to the expected resolution of support request
default: `0`
  - **`damage`**  *(object)* - optional  
    A damage of the asset.
  - **`sequence`**  *(integer)* - optional  
    the sequence number of the status of tickets on this issue
default: `0`
  - **`links`**  *(object)* - optional  

## Example

```json
{
  "inputs": {
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
}
```

