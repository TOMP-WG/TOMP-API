# legProperties

A (planned) consumption of a product within a package

**Type:** `object`

semantics [{'transmodel': 'LEG'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [legReference](legReference.md) | ✓ | The unique identifier (TO) of this leg. Must always the same as applied in th... |
| `specification` | [travelSpecification](travelSpecification.md) | ✓ |  |
| `sequenceNumber` | [shortInt](shortInt.md) |  | The order of the leg within the package. Mandatory, if there are multiple leg... |
| `mode` | [mode](mode.md) |  | These classes are taken from the NeTeX standard, but ALL and UNKNOWN are remo... |
| `status` | [legStatus](legStatus.md) |  | status of a leg<br> _NOT_STARTED_ the leg is not started, initial state<br> _... |
| `travellers` | array[[travellerReference](travellerReference.md)] |  |  |
| `products` | array[[productReference](productReference.md)] |  | The main product (v1.x 'asset type') used to execute this leg |
| `ancillaries` | array[[ancillaryReference](ancillaryReference.md)] |  | additional products that can be assigned to this leg |
| `assets` | array[[assetReference](assetReference.md)] |  | The physical asset(s) used for the execution of the leg |
| `operatorId` | [organisationReference](organisationReference.md) |  | default string, full names etc (length 0-200) |
| `operatorName` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |
| `labels` | array[[label](label.md)] |  |  |
| `returnLocations` | array[[placeReference](placeReference.md)] |  |  |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "leg"

- **`id`**  *([legReference](legReference.md))* - **required**  
  The unique identifier (TO) of this leg. Must always the same as applied in the request URL. And when there are not additional legs in the offered or purchased package, the same **id** as the package id.

- **`specification`**  *([travelSpecification](travelSpecification.md))* - **required**  
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

- **`sequenceNumber`**  *([shortInt](shortInt.md))* - optional  
  The order of the leg within the package. Mandatory, if there are multiple legs in the package. If there are parallel legs (eg. using parking lot and a renting a bike), it can be the same within one package.
default: `0`

- **`mode`**  *([mode](mode.md))* - optional  
  These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.

- **`status`**  *([legStatus](legStatus.md))* - optional  
  status of a leg<br> _NOT_STARTED_ the leg is not started, initial state<br> _PREPARING_ the _PREPARE_ operation has been received<br> _READY_TO_USE_ the leg is ready to use<br> _IN_USE_ the travellers are on their way<br> _PAUSED_ the asset is paused<br> _ENDING_ the end-leg request is received, the offboarding process has is started<br> _ENDED_ the travellers have arrived at their destination, leg is final<br> _ISSUE_REPORTED_ due to an issue, there is (temporarily) no progress to report, when the issue isn't solved, this is a final state<br> _CANCELLED_ the leg has been cancelled, before execution<br> _ABENDED_ the leg is abnormally ended (e.g. due to an issue)

- **`travellers`**  *(array[[travellerReference](travellerReference.md)])* - optional  

- **`products`**  *(array[[productReference](productReference.md)])* - optional  
  The main product (v1.x 'asset type') used to execute this leg

- **`ancillaries`**  *(array[[ancillaryReference](ancillaryReference.md)])* - optional  
  additional products that can be assigned to this leg

- **`assets`**  *(array[[assetReference](assetReference.md)])* - optional  
  The physical asset(s) used for the execution of the leg

- **`operatorId`**  *([organisationReference](organisationReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`operatorName`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

- **`labels`**  *(array[[label](label.md)])* - optional  

- **`returnLocations`**  *(array[[placeReference](placeReference.md)])* - optional  

## Example

```json
{
  "id": "identifier",
  "type": "leg",
  "specification": {
    "type": "travelSpecification",
    "from": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
    "via": []
  },
  "sequenceNumber": 0,
  "mode": "AIR",
  "status": "NOT_STARTED"
}
```