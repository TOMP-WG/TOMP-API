**Q**: How do I start implementing a TO?<br>
**A**: That's actually a good question. The API is not the smallest one and consists actually out of 2 API's: one that has to be implemented as TO and one for the MP. Every endpoint is marked with TO, MP or both.<br>

# Transport operator API
The TO has to implement only a few 'endpoints' to play along. The most essential ones can be found in the planning, booking and trip execution modules.<br>
## Planning
### Minimal
Have a look at the [Simple planning &amp; booking phase](Simple-planning-and-booking-phase.md).<br>
In the planning module we have the endpoint /plannings/. You cannot do without this one. The plannings request contains at least: one of the start and endpoint and corresponding time. As a TO you have to deliver all the options you can create. The options can be in 2 formats: or you deliver physical assets (e.g. specific cars) or an asset-type (e.g. men's bike) and an available amount.<br>Remember that the fare isn't a final one.
One important thing is that these planning options can be created, returned and forgotten, but when the property 'provide-ids' with value 'true' is send, you have to provide an id per option and store the option. In this case the fare should be accurate.<br>
_Example_ 
<pre>POST https://exampleTO.com​/plannings/?booking-intent=false
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "travellers": 1,
  "users": [ ... ]
}</pre>
could produce: 
<pre>{
  "conditions": [],
  "legOptions": [
    {
      "id": "leg 1",
      "startTime": "2020-06-28T14:55:00+02:00",
      "endTime": "2020-06-28T14:25:00+02:00",
      "from": {
        "coordinates": {
          "lng": 6.169639,
          "lat": 52.253279 }
      },
      "to": {
        "coordinates": {
          "lng": 6.169639,
          "lat": 52.253279 }
      },
      "assetType": {
        "typeId": "mens bike",
        "brand": "BATAVUS",
        "model": "FONK",
        "buildingYear": 2019,
        "meta": []
      },
      "pricing": {
        "parts": [
          {
            "amount": 3.50,
            "currencyCode": "EUR",
            "taxRate": 21,
            "type": "FLEX",
            "unit-type": "HOUR",
            "units": 1
          }
        ]
      },
      "conditions": []
    }
  ]
}</pre>

### Extra
You can extend this, you can add more users, with ages, licenses, cards or other requirements like disabilities in the request and of course you can add conditions you demand of the MP or end user (like requesting deposits, return of the asset to certain area's). In case of multiple legs (like a train ride with overlay), you should use the "parts" field of the leg, where per 'subleg' an entry should be added.

## Booking
### Minimal
The booking phase exists contains at least 2 calls: after the planning phase is ended with a 'booking-intent', you can book a trip using POST /bookings/ with in the body the provided id from the planning phase.<br>
The result will be a booking object in the state 'PENDING'. For each asset you will book, you have to call this endpoint. In case you will travel with 3 adult women you can request a planning with travellers: 3, but you have to call 3 times this endpoint to actually book 3 assets (e.g. bikes).<br>
The MP has to confirm all pending 'legs' (=booked asset for a trip part). It will call POST /bookings/{id}/events with in the body { "operation" : "COMMIT" }. This way a kind of transaction can be created. You have to respond with a booking with state 'CONFIRMED'.

### Extra
a) Whenever the booking is too long in PENDING state, you can send a POST /bookings/{id}/events with an 'EXPIRE' event to the MP. <br>
b) You can implement the 'POSTPONED-COMMIT' scenario: as TO you cannot always directly respond with 'OK, I can book this asset for you'. In that case you should respond to the 'COMMIT' event with an object in state 'CONDITIONAL_CONFIRMED'.<br> After a while, when you have found out that you can supply the asset, you can send the 'COMMIT' event to the MP. If you cannot deliver the asset, send the 'DENY' event to the MP.<br>
c) You can implement the 'CANCEL' event. There can be multiple reasons for cancelling a booked asset.<br>

## Trip execution
### Minimal
The trip execution endpoint that has to be implemented is the POST /executions/{id}/events. The start and end of a trip should be registered for payment reasons. The corresponding events are 'SET_IN_USE' and 'FINISH'. <br>
In case the initiator is the TO to open/close an asset (e.g. bike), the TO has to inform the MP. Or, in case an app should open/close an asset, the MP has to inform the TO.

### Extra
1) Not all events are applicable for each modality, PREPARE, RESERVE, PAUSE, START_FINISHING should only be implemented when needed/applicable<br>
2) /executions/{id}/available-assets will return the available assets in the surroundings. This endpoint should be used to find the nearest asset. After this /executions/{id}/events ASSIGN_ASSET can be used to assign a specific asset to the trip.
3) POST of /executions/{id}/progress

All other endpoints can be implemented later on. The Operator Information should be doable; it not complex. After this payment and support can be done, but these can also be handled in other ways. But the more you've implemented, the better the integration with the MP's.<br>It's also possible that certain MP's will require parts of the API that are not in the 'mimimal viable product'. 