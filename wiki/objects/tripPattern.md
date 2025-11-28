# tripPattern

**Type:** `object`

semantics [{'transmodel': 'TRIP PATTERN'}]

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [travelSpecification](travelSpecification.md)
   - Properties: `type`, `from`, `via`, `to`, `startTime`, `endTime`
2. object
   - Properties: `type`, `serviceJourneys`, `travelDate`

## Example

```json
{
  "type": "tripPattern",
  "from": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
  "via": [],
  "serviceJourneys": [
    "example-string",
    "example-string"
  ],
  "travelDate": "full-date"
}
```

