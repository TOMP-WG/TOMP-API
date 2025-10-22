[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [Cope with 'Required data'](Cope-with-'Required-data'.md)

If the TO requires personal data (using the conditionRequireBookingData), it must be supplied by the MP. The result should also contain the requested fields.

```http
POST https://exampleTO.com/bookings/
{
  "id": "746ac-48792bb-746dac3", ** this is the ID provided in the planning phase **
  "customer": {
    "id": 123456,
    "firstName": "John",
    "lastName": "Doe",
    "phone": "tring"
  }
}
```
The result must repeat the personal data. If data is missing, the TO should return an error state (400). see [Error handling in TOMP](Error-handling-in-TOMP.md).  

If everything is correct, a booking has to be returned in state 'PENDING'. The rest of the process is described in the [Booking phase](Booking-phase#Default-booking-workflow.md).
```
{
  "id": "746ac-48792bb-746dac3",
  "customer": {
    "id": 123456,
    "firstName": "John",
    "lastName": "Doe",
    "phone": "string"
  },
  "state": "PENDING", ** this is a new booking in state pending **
  ...
}
```
