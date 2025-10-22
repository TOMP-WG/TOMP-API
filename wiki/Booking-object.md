[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) | [Booking phase](Booking-phase.md) > [booking object](booking-object.md)

The booking object is used in most modules: in the planning (where bookable objects are returned) and in the booking (where the booked object is returned and committed). In the trip execution module, the separate [leg](leg.md)s are used.

| field | required | description | 
| --- | --- | --- | 
| id | < 1.3.0 not in booking-intent=false, >= 1.3.0 everywhere except in the inquiry result | A unique identifier for the TO to know this booking by |
| from | | [Place](Place.md), could be slightly different than requested |
| to | | [Place](Place.md), could be slightly different than requested |
| customer | | [Customer object](Customer-object.md), not filled in the planning phase. Use this part as little as possible (GDPR) |
| state	| | The life-cycle state of the booking (from NEW to FINISHED), enum: [ NEW, PENDING, REJECTED, RELEASED, EXPIRED, CONDITIONAL_CONFIRMED, CONFIRMED, CANCELLED, STARTED, FINISHED ] |
| legs | < 1.3.0 | The [Leg](Leg.md)s of this booking. Mostly contains 1 leg, but for brokers/aggregators or TOs with transfers between assets (mostly public transit), it might contain multiple legs. For convenience reasons, the first leg should contain the same id as the booking-id.  In case this object is omitted, the first leg must be constructible using the mainAssetType, id, pricing, departureTime, and arrivalTime from the booking itself|
| pricing | | The overall pricing of the complete booking. See [Fare construction](Fare-construction.md) |
| extraData | | Data for mutually agreed information (peer-2-peer solutions). Please create an issue in Github to inform the usage of extra information in this field, providing the ability to standardize this in a future release |
| mainAssetType | when `legs` is omitted | the main asset type for this booking |
| departureTime | | the overall departure time for this booking. When `legs` is omitted, it should contain the departure time of the leg (if available) |
| arrivalTime | | the overall arrival time for this booking. When `legs` is omitted, it should contain the arrival time of the leg (if available) |
