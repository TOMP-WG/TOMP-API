# updateTravelSpecificationRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`package`**  *([packageReference](packageReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`startTime`**  *([dateTime](dateTime.md))* - optional  
    The intended departure time. If left out and no endTime is set, the current time should be assumed. If only the arrival time is specified, this is an implicit request for a guaranteed arrival at that time.
  - **`endTime`**  *([dateTime](dateTime.md))* - optional  
    The intended arrival time, at the `to place`. When the **startTime** is not set, and **endTime** is set, it is an implicit request for an arrival time guarantee.

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "leg": "example-string",
    "startTime": "2024-01-15T10:30:00Z",
    "endTime": "2024-01-15T10:30:00Z"
  }
}
```

