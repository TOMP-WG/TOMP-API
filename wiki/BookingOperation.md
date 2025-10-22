[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [BookingOperation](BookingOperation.md)

The booking operation must be used until the trip is started.

| field | required | description |
| ----- | -------- | ----------- | 
| operation | *	| The operation |
| origin | | from 1.2.0,  This operation can be done on behalf of another party. The MP can act on behalf of the END_USER (cancel this booking for me); to override the default origin. In case this field is obsolete, it must be assumed that the events the MP is sending, this field should contain "MP". And in case the TO is sending, "TO". |