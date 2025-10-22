The TOMP-API can be used together with other standards. The main focus of the TOMP-API is facilitating the planning, booking, and trip execution, where standards like NeTEx, GBFS, GTFS, and APDS are mainly focussing on providing accurate information about the current situation.

## How should the standards work together?
Information about the bus line, bike type, taxis, car spots, etcetera are mentioned in these standards and each does have a unique identifier. For example, each bus line itself has a unique identifier. This identifier can be used to start the planning and/or booking process.  
This example does allow you to request planning for a GBFS vehicle type:
```
POST https://tomp.some-bike-operator/plannings?booking-intent=false
{
  "from": { "coordinates": { "lng": 6.169639, "lat": 52.253279 } },
  "to": { "coordinates": { "lng": 6.164383, "lat": 52.243224 } },
  "departureTime": "2021-08-23T12:39:10.123Z"
  "nrOfTravelers": 1
  "useAssetTypes": [
    "basic-bike"
  ]
}
```
This 'basic-bike' comes from the file 'vehicle_types.json' in the GBFS section of the some-bike-operator.  
This approach can also be taken using GTFS's routes or NeTEx's vehicle services.

## The response
The content of the response is up to the transport operator. But this could be a minimal response:
```
{
  "validUntil": "2021-08-23T12:39:10.142Z",
  "options": [
    {
      "from": { "coordinates": { "lng": 6.169651, "lat": 52.253272 }, "stationId": "HOWDY-STREET-01" },
      "to": { "coordinates": { "lng": 6.164383, "lat": 52.243224 } },
      "state": "NEW",
      "legs": [
        {
          "from": { "coordinates": { "lng": 6.169651, "lat": 52.253272 }, "stationId": "HOWDY-STREET-01" },
          "to": { "coordinates": { "lng": 6.164383, "lat": 52.243224 } },
          "departureTime": "2021-08-23T12:39:10.143Z",
          "arrivalTime": "2021-08-23T12:39:10.143Z",
          "assetType": {
            "id": "basic-bike",
            "stationId": "HOWDY-STREET-01",
            "nrAvailable": 38,
		"assetClass": "BICYCLE",
	  }          
        }
      ],
      "pricing": {
	"type": "default",
	"estimated": true,
	"description": "Estimated price",
	"class": "FARE",
	"parts": [ { "amount": 3.58, "currencyCode": "CAD", "vatRate": 15, "type": "FIXED" } ]
      }
    }
  ]
}
``` 
thereby offering a bike from a nearby station (HOWDY-STREET-01, also findable in the GBFS/NeTEx files), for an estimated price of CAD 3.58 (including tax of 15%). In the meantime also providing also some extra information about the current availability. Of course, it is up to the transport operator to offer multiple offers (other nearby stations, other times etcetera).

The response can contain a lot more information, but with this request/response, basic information can be provided.

## What's next?
After requesting/proposing a transport asset, the next step is of course **booking** it! And this step is on interface level not complex in this case:
* call the planning endpoint again, but use 'true' instead of 'false' for the booking-intent parameter. The offer _must contain a unique, generated ID_, which can be used in the next endpoint: /bookings.
* call the /bookings endpoint, with the offer ID in the body (that's the minimum)
```
POST /bookings { "id": "1e637eab-0d98-4594-beb6-db613351bd7c" }
```
* the response can be the same as in the planning stage (of course, the operator must guarantee this time there is an ability to deliver transport), but the state should contain 'PENDING'. This is for transactional reasons (a trip can be a chained one, and all of the transport services should be able to deny an offer). 
* after a response containing a booking in PENDING state, a single call to POST /bookings/{provided unique id}/events with body { "operation": "COMMIT" } will commit the booking.
```
POST /bookings/1e637eab-0d98-4594-beb6-db613351bd7c/events { "operation": "COMMIT" }
```