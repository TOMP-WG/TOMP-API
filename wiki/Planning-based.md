[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Planning based](Planning-based.md)  

Planning based TOMP usage is the original scenario. The plannings endpoint can be called during the routing, to find out if it's likely that the TO has assets to move people from A to B at a specific time. Extra information of the end user can be provided (if requested, see [ProcessIdentifiers](ProcessIdentifiers.md)).
```
(v1.0) POST https://exampleTO.com​/plannings/?booking-intent=false
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "nrOfTravelers": 1,
  "travelers": [ ... ]
}

(v1.3 and above)
POST https://exampleTO.com​/planning/inquiry
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "nrOfTravelers": 1,
  "travelers": [ ... ]
}
```
When using ?booking-intent=true or /planning/offers, the IDs in the result of the booking and its legs are required! If you return only one leg per booking, use the same ID for the booking and the leg. This makes things a lot more easy in production.

## Request
| field | required | description |
| ----- | -------- | ----------- | 
| from  | * | place, containing at least a lon/lat, but can contain a lot more information |
| radius | | Maximum distance in meters a user wants to travel to reach the travel option |
| to | | place, see from |
| departureTime	| | The intended departure time. If left out and no arrivalTime is set, the current time should be assumed. |
| arrivalTime | | The intended arrival time, at the to place if set otherwise the time the user intends to stop using the asset. |
| nrOfTravelers	| | The number of people that intend to travel, including the customer. Minimum is 1 |
| travelers | | more information about the travelers. see [Traveler](Traveler.md) |
| useAssets | | array of IDs of the assets that are already gathered by the MP, to filter the options |
| userGroups | | array of IDs of user groups. These IDs are not public and only known to the MP and the specific TO |
| useAssetTypes	| | array of IDs of the asset types. see [Available assets](Available-assets.md). Assets that can be assigned later on in the trip execution (ASSIGN_ASSET) |

## Response
| field | required | description | 
| ----- | -------- | ----------- | 
| validUntil | * | The time until which the presented options are (likely) available |
| options | * | An array of options. Every option is a Booking object. The booking objects do have a unique ID when booking-intent = true |


__Booking object__
| field | required | description | 
| ----- | -------- | ----------- | 
| id | | Mandatory with booking-intent=true (or offer endpoint); A unique identifier for the TO to identify this booking |
| from | | Departure location, can be slightly different from the requested 'from'. It is the exact location where the leg will start. |
| to | | Arrival location, can be slightly different from the requested 'to'. It is the exact location where the leg will end. |
| customer | | The customer, doesn't need to travel. Most likely the customer will be (one of) the traveler(s). |
| state | | The life-cycle state of the booking (from NEW to FINISHED). NEW, PENDING, REJECTED, RELEASED, EXPIRED, CONDITIONAL_CONFIRMED, CONFIRMED, CANCELLED, STARTED, FINISHED. When returned from a planning call, the state should be NEW. When booked (result of POST /bookings/{id}), it should be PENDING, when committed (result of /bookings/{id}/events COMMIT) the status should be CONFIRMED or CONDITIONAL_CONFIRMED (see [Postponed commit](Postponed-commit.md) |
| legs | * | an array of legs (=part of a trip by one asset). A booking can contain multiple legs (with a transfer between the legs). The first leg should have the same ID as the booking, for convenience. |
pricing	| | The price of the trip. Can be a fixed one, but can also consist of multiple parts (partly fixed, partly price per km, minute etc.). For each traveler in the request, there should be at least one fare part (see [Fare construction](Fare-construction.md)). |
| extraData | |  free format object, for specific communication between MP and TO |
