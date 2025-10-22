[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > ( [Booking phase](Booking-phase.md) OR [Trip Execution phase](Trip-execution-phase---start.md) ) > [Providing access data](Providing-access-data.md)  

V1.2.0: See also [Access Methods](Access-Methods.md).

Whenever the TO responds to POST /bookings/{id}/events or /legs/{id}/events, it can provide access information or ticket.  

This can be done on various moments:
* in the response of /bookings/{id}/events - `COMMIT` operation (step two in the booking process)
* in the response of /legs/{id}/events - `PREPARE` operation (just before starting the leg)
* in the response of /legs/{id}/events - `ASSIGN_ASSET` operation (before starting the leg)

In the trip execution the /legs/{id}/events - `SET_IN_USE` must be regarded as the official start of the usage of the asset. It must be a confirmation that the asset is used.

The access data must be placed in the assetAccessData of the leg(s).

| field | required | description |
| ----- | -------- | ----------- | 
| validFrom | * | The start moment from the validity of the access data | 
| validUntil | * | The end moment from the validity of the access data | 
| tokenType | * | type of access data: QR, PDF, TOKEN, LINK, BASE64. This enum for this type is not yet complete. These are already available, but this has to be standardized later on. |
| tokenData | * | free format object containing access information as specified in tokenType |
