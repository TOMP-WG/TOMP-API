[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) 

The booking phase is more complex: in a transactional way the MP has to book all the legs/assets at (different) TOs.

## Default workflow
> First, the default workflow for booking is described. This is generic for every booking. Book the offer from the [Planning phase](Planning-phase.md), for each leg in the trip, and after that, commit all the legs. [more...](Booking-phase#Default-booking-workflow.md)  

## One-stop booking
> The one-stop booking was introduced in version 1.4, to optimize the booking flow for many operators, who don't work with offers. The 'offer' can be constructed from external sources (like GBFS, GTFS, NeTEx or many others), and in the booking request you can request a bike of a specific type or a specific asset. [more...](Booking-phase#One-stop-workflow.md)

## Personal data for validation
> The TO can request personal information for validation or to check its terms and conditions. This can be done by returning a specific condition in the planning phase, this information has to be delivered in the booking. [more...](Cope-with-'Required-data'.md)  
See also [Require data in planning phase](Requiring-specific-data.md).  

## Provide tickets or access data
> Some TOs provide tickets or access data directly in the booking process. Others might postpone this until the trip starts. But for those who want to provide it immediately, [this](Providing-access-data.md) information is needed.  

## Expiry time
Since version 1.5.0, you can request to extend the expiry time of a to commit a booking. In the result of the POST /bookings, there is a header field 'expires', indicating the validity of the offer. If this is too short, the MP can request additional time using the POST /bookings/{id}/event - EXTEND_EXPIRY_TIME.

```http
POST https://exampleTO.com/bookings/746ac-48792bb-746dac3/events  
{ "operation": "EXTEND_EXPIRY_TIME" }
```

<img align="right" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/default-booking-process.png">

### Default booking workflow
__Step 1:__ The MP wants to book the selected leg from the planning phase. 
```http
POST https://exampleTO.com/bookings/
{ "id": "746ac-48792bb-746dac3", <= this is the ID provided in the planning phase
  ...  
}
```
The result must be a booking in `PENDING` state, unless it is rejected by the TO for some reason.
```
{ "id": "746ac-48792bb-746dac3",
  "state": "PENDING", 
  ...
}
```
Remark: the state could also become CONFIRMED (or IN_USE) when using the process identifier `AUTO_COMMIT` (or `ATOMIC_BOOKING_SET_IN_USE`). See [processIdentifiers](processIdentifiers.md)

__Step 2:__ After sending the request to all needed TO's - and they all responded positively, the MP will have to send a POST request with the operation `COMMIT` in it to change the booking-option into a real booking.

```http
POST https://exampleTO.com/bookings/746ac-48792bb-746dac3/events/  
{ "operation": "COMMIT" }
```
The result will be a booking object, in state `COMFIRMED`. The leg is now committed (guaranteed) by the TO.   
```
{ "id": "746ac-48792bb-746dac3",
  "state": "CONFIRMED",
  ...
}
```
If any of the TOs responds negative (state: `REJECTED`), the other TOs have to be informed that the complete trip is cancelled. This must be done using the same endpoint again, only now with a `CANCEL` operation: 
```http
POST https://exampleTO.com/bookings/746ac-48792bb-746dac3/events/  
{ "operation": "CANCEL" }
```
### One-stop workflow
The one-stop workflow uses another endpoint to book: POST /bookings/one-stop, instead of POST /bookings/. The request looks quite similar to the planning request, but additional information is required:
- OR useAsset (to indicate which asset you want to book, like a license plate or external visible reference) OR useAssetType (derived from a routeplanner or external data sets, like GBFS' asset-types).
- required booking information, like a driver's license or discount cards. This information is the same as normally supplied in the booking process.

## No immediate confirmation
> The generic flow will be changed a little to cope with TOs that cannot directly guarantee the leg ("Postponed commit scenario"). Instead of ending a booking in a `CONFIRMED` state, the state be `CONDITIONAL_CONFIRMED`. The MP has to wait for a `COMMIT` or a `DENY` from the TO side. [more...](Cope-with-‘Postponed-commit’.md)  
See also [Postponed commit in planning phase](Postponed-commit.md).  

## Objects
The main objects in this phase are the [BookingRequest](BookingRequest.md), the [Booking object](Booking-object.md) and the [BookingOperation](BookingOperation.md).