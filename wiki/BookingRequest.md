[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [BookingRequest](BookingRequest.md)

The booking request object is relying on the outcome of the [Planning result](Planning-result.md). One of the offered [Bookings](Booking-object.md) in the result can be booked. The id of the choosen booking should be in the booking request, along with extra information that is needed for the booking/trip execution, f.x. personal information (that's not needed for planning/routing) or information to create access data.

| field | required | description | 
| --- | --- | --- | 
| id | * | A unique identifier for the TO to know this booking by. In this phase of the booking process, the id is mandatory |
| from | | [Place](Place.md), contains the starting place. If provided, it should be the same as the starting place from the selected offer (=booking) |
| to | | [Place](Place.md), contains the end place. If provided, it should be the same as the end place from the selected offer (=booking) |
| customer | | [Customer](Customer.md), information about the end user, who has the contract with the MP. Can be one of the [Traveler](Traveler.md)s |
| callbackUrl | | The callback URL of the Maas Provider, to use as base url for callback, f.x. the POST legs/{id}/events and POST /bookings/{id}/events. Only to be provided when this deviates from standard or agreed URL. [v1.2.0] |
