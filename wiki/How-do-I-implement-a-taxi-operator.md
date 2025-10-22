[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) >> [Taxi](How-do-I-implement-a-taxi-operator.md)  

**Q**: How to implement a Taxi operator?<br>
_A_: There are several specific items in the TOMP API for taxi operators. I'll list them per module:
<br>Planning module
* take abilities in scope. Please have a close look at the abilities that are in the planning request. Please make sure you can actually can transport people with the requested abilities. These (dis)abilities can be found in the POST /plannings body. "travelers">"requirements".
* add in the response the condition 'requireBookinData' with at least ["FROM-ADDRESS", "TO-ADDRESS"] in order to get physical addresses beside lon/lat combinations (eg. { "type": "conditionRequireBookingData", "requiredFields": ["FROM-ADDRESS", "TO-ADDRESS"] }).
* the fare object should reflect how your price is calculated. The property 'estimated' should contain 'true'

<br>Booking module
* use the postponed-commit scenario. Whenever you're not able to directly commit a planned trip (for instance if you must plan the trip), you should respond with a booking object with the status 'PENDING'. After the 'COMMIT' request from the MP, you can respond with a 'CONDITIONAL_CONFIRMED'. Whenever you've planned a taxi with a driver, you can send a /bookings/{id}/event with a 'COMMIT' to the MP. If you're not able to plan the trip, send a 'DENY'.

<br>Trip execution
* You'll have to send an event to the MP when the taxi starts riding to the pickup address, using the /executions/{id}/event with "event": "PREPARE". This can be used to communicate to the end-user. 
* You'll have to send ETA's using the /bookings/{id}/notifications { "type": "ETA", "comment": "We'll arrive at 12:23 PM", "minutes": 3 }. 
* You should also send this notification when you've arrived at the pickup location with type: ETA and comment: "Arrived" and minutes is zero. Alternative (proposal 1.4.0): 'ARRIVED' is a new notification type and (proposal 2.0.0) 'READY_TO_USE' is a new leg status.
* When the actual ride is starting for the passenger(s), the leg has to start /legs/{id}/event {"event": "SET_IN_USE", "time": 3423423423, "asset": { ... , "place": { "coordinate": { "lng": ..., "lat": ... } } } }
* When a user isn't at the pickup point, a /bookings/{id}/notification should be sent, using the type 'USER_NO_SHOW'.
* Whenever the leg ends, send again a simular message:  /legs/{id}/event {"event": "FINISH", ..., "asset": { ... , "place": { "coordinate": { "lng": ..., "lat": ... } } } }
* Based on the start and end event the actual price can be calculated. It must be in the result of /payment/journal-entry, with a fixed price.
* Manual adjustments on the price should be communicated with a claim-extra-costs.
* on the end of the trip, you can send the difference between the offered price and the actual price in an extra claim-extra-costs

<br>Operator information
* All endpoints of the OI should be implemented, without the stations endpoint (except when you operate from taxi hubs).
* The available-assets should be implemented returning an assetClass (per region), telling the amount of available taxis.
* Pricing plans should return the normal way you're charging the end user. Probably partly fixed prices (startup costs) and partly flexible (price per minute/km/mile).

<br>**Recap**<br>
Endpoints to implement:
* GET /operator/meta
* GET /operator/available-assets (return only assetTypes)
* GET /operator/alerts
* GET /operator/operating-calendar
* GET /operator/operating-hours
* GET /operator/information
* GET /operator/pricing-plans
* GET /operator/regions
* POST /plannings
* POST /bookings
* GET /payment/journal-entry

Process identifiers to use in the meta endpoint:
* Planning: PLANNING_BASED
* Booking: POSTPONED_COMMIT
* Trip execution: TO_CONTROLLED, ETA_NOTIFICATION, USE_PREPARE_TO_INDICATE_START
* Payment: CORRECTION_BY_EXTRA_COSTS (if applicable)

The endpoint the MP will need to interact with you (you'll have to call the MP at these endpoints!):
* POST /bookings/{id}/events
* POST /bookings/{id}/notifications
* PATCH /payment/{id}/claim-extra-costs

