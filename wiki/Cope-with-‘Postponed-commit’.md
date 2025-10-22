[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [Cope with ‘Postponed commit’](Cope-with-‘Postponed-commit’.md)

<img align="right" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/postponed-commit-booking-process.png">

__Step 1:__ The MP wants to book the selected leg from the planning phase, but sends it to a TO with a 'postponed commit' scenario.
```http
POST https://exampleTO.com/bookings/
{
  "id": "746ac-48792bb-746dac3", // provided in planning phase
}
```
The result must be a booking in PENDING state, unless it is rejected by the TO for some reason.
```
{
  "id": "746ac-48792bb-746dac3",
  "state": "PENDING", 
  ...
}
```
  
__Step 2:__ After sending the request to all needed TO's - and they all responded positively, the MP will have to send a POST request with the operation `COMMIT` in it to change the booking-option into a real booking.

```http
POST https://exampleTO.com/bookings/746ac-48792bb-746dac3/events/
{
  "operation": "COMMIT"
}
```
The result will be a booking object, in state `CONDITIONAL_COMFIRMED`. The MP has now to wait for the message from the TO that tells him it is committed or denied. 
```
{
  "id": "746ac-48792bb-746dac3",
  "state": "CONDITIONAL_CONFIRMED",
  ...
}
```

__Step 3:__ Wait for the TO to respond.  
The TO will call the MPs endpoint. If the TO accepts the leg, it will send a commit:
```http
POST https://exampleMP.com/bookings/746ac-48792bb-746dac3/events/
{
  "operation": "COMMIT"
}
```
But it is also possible that the TO denies the leg: 
```http
POST https://exampleMP.com/bookings/746ac-48792bb-746dac3/events/
{
  "operation": "DENY"
}
```
Or, there is no message before the 'expires' in the header of the result. The assumption is that it should be treated as a 'deny'.