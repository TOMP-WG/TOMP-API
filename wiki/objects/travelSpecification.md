# travelSpecification

**Type:** `object`

semantics [{'transmodel': 'TRAVEL SPECIFICATION'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `from` | [placeReference](placeReference.md) |  | use an ID contained in the **places** field, or from an external source, when... |
| `via` | array[[placeReference](placeReference.md)] |  | use an ID contained in the **places** field, or from an external source, when... |
| `to` | [placeReference](placeReference.md) |  | use an ID contained in the **places** field, or from an external source, when... |
| `startTime` | [dateTime](dateTime.md) |  | The intended departure time. If left out and no endTime is set, the current t... |
| `endTime` | [dateTime](dateTime.md) |  | The intended arrival time, at the `to place`. When the **startTime** is not s... |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "travelSpecification"

- **`from`**  *([placeReference](placeReference.md))* - optional  
  value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
  use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'

- **`via`**  *(array[[placeReference](placeReference.md)])* - optional  
  use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'

- **`to`**  *([placeReference](placeReference.md))* - optional  
  value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
  use an ID contained in the **places** field, or from an external source, when using coordinates, please use the prefix 'gps:'

- **`startTime`**  *([dateTime](dateTime.md))* - optional  
  The intended departure time. If left out and no endTime is set, the current time should be assumed. If only the arrival time is specified, this is an implicit request for a guaranteed arrival at that time.

- **`endTime`**  *([dateTime](dateTime.md))* - optional  
  The intended arrival time, at the `to place`. When the **startTime** is not set, and **endTime** is set, it is an implicit request for an arrival time guarantee.

## Example

```json
{
  "type": "travelSpecification",
  "from": "GPS:52.342392,41.431234",
  "to": "NSR:StopPoint:108842"
}
```