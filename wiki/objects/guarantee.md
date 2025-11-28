# guarantee

**Type:** `object`

semantics [{'transmodel': 'TRAVEL GUARANTEE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [uuid](uuid.md) |  | https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://... |
| `name` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |
| `organisation` | [organisationReference](organisationReference.md) |  | guaranteeing organisation |
| `type` | enum (`ALTERNATIVE_JOURNEY`, `HOME_LEG`, `RETURN_TO_ORIGIN`, `ON_TIME_TRAVEL`, `TRIP_ON_TIME`, ...) |  | _ALTERNATIVE_JOURNEY_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE ... |

## Detailed Properties

- **`id`**  *([uuid](uuid.md))* - optional  
  https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)

- **`name`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

- **`organisation`**  *([organisationReference](organisationReference.md))* - optional  
  guaranteeing organisation

- **`type`**  *(enum (`ALTERNATIVE_JOURNEY`, `HOME_LEG`, `RETURN_TO_ORIGIN`, `ON_TIME_TRAVEL`, `TRIP_ON_TIME`, ...))* - optional  
  _ALTERNATIVE_JOURNEY_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY is not available then alternative SERVICE JOURNEY will be provided. -| (EASEMENT_REDRESS, PRODUCT EXCHANGE REDRESS) _HOME_LEG_ - A TRIP REPAIR GUARANTEE that if a the passenger is unable to reach their destination by public transport because of a delay in services, a taxi to their destination will be provided. -| (TAXI HOME REDRESS) _RETURN_TO_ORIGIN_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY cannot be completed, then the passenger will be returned to their origin stop. -| (RETURN TO ORIGIN REDRESS)
_ON_TIME_TRAVEL_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if repeated travel within a certain TIME INTERVAL fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _TRIP_ON_TIME_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a trip fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _FACILITIES_AVAILABLE_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a facility or service (e.g. WIFI, Meal, seat reservation, etc) is not available or fails to meet a specified quality. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ACCOMODATION_ - A TRAVEL QUALITY GUARANTEE that special accommodation will be provided in the event of severe disruption. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ASSISTANCE_ - A TRAVEL QUALITY GUARANTEE that mobility assistance will be provided. -| (ALL REDRESSES, needs SERVICE PARAMETER) _PASSENGER_SUPPORT_ - A TRAVEL QUALITY GUARANTEE that assistance will be provided, for example, if a disruption occurs or a that stations are staffed. (ALL REDRESSES)
_DISRUPTION_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on disruptions will be made available. (ALL REDRESSES) _REDRESS_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on available compensation or other statutory and discretionary redress options will be made available to the passenger. (ALL REDRESSES) _BEST_FARE_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on the best value fares will be made available (ALL REDRESSES)
_GENERAL_TRAVEL_ - An arbitrary OTHER TRAVEL GUARANTEE describing some special guarantee not covered by the normal categories (ALL REDRESSES) _MEDIA_REPLACEMENT_ - An OTHER GUARANTEE that a replacement media will be provided if the original becomes unusable. _REFUND_UNUSED_ANCILLARIES_ - unused ancillaries will be refunded _REFUND_WHEN_CANCELLED_ - when cancelled before start, a refund will be scheduled

## Example

```json
{
  "id": "identifier",
  "name": "example-string",
  "organisation": "example-string"
}
```