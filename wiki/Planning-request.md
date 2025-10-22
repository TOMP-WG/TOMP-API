[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Planning request](Planning-request.md)

# Description
The planning request contains all information to create a planning.

| field | required | description | 
| --- | --- | --- | 
| from | * | The starting location. See [Place](Place.md), this contains at least a lon/lat combination (WGS84), but can contain also additional (required) information |
| previousLegInfo | | (Proposal 2.0.0): information about the previous leg, to facilitate combination vouchers, communicate flight numbers, etc. See [connectedLegInfo](connectedLegInfo.md) |
| radius | | Maximum distance in <b>meters</b> a user wants to travel to reach the travel option. Mandatory in case of MANDATORY_RADIUS (see [processIdentifiers](processIdentifiers.md)) |
| to | | The end location. See [Place](Place.md). Is optional in case of the scenario 'I want to use this asset'. In most (planned) cases it should contain the end location. Is mandatory in case of MANDATORY_TO_STATION_ID, MANDATORY_TO_STOP_REFERENCE or MANDATORY_TO_ADDRESS (see [processIdentifiers](processIdentifiers.md)) |
| departureTime	| | The intended departure time. If left out and no arrivalTime is set, the current time should be assumed. If only the arrival time is specified, this is an implicit request for a guaranteed arrival at that time.<ul><li> format: [ISO 8601](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#rfc.section.5.6). <li>Mandatory in case of MANDATORY_DEPARTURE_TIME, see [processIdentifiers](processIdentifiers.md). </ul>|
| arrivalTime | | The intended arrival time, at the `to place`. If not set, the time the user intends to stop using the asset (implicit request for arrival guarantee). <ul><li> format [ISO 8601](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#rfc.section.5.6). <li> Mandatory in case of MANDATORY_ARRIVAL_TIME, see [processIdentifiers](processIdentifiers.md). <li>If both departure and arrival time are specified, the results should start at/after the departure time and end at/before the arrival time.</ul> |
| nrOfTravelers | | The number of people that intend to travel, including the customer. Since 1.3.0 not mandatory (issue #389). When it is not provided, it should be assumed it is 1. <ul><li>minimum: 1 <li>Mandatory in case of MANDATORY_NR_OF_TRAVELERS (see [processIdentifiers](processIdentifiers.md))</ul> |
| travelers | | Specification per [Traveler](Traveler.md). |
| useAssets | | A list of assetIds, referring to /operator/available-assets or to external sources (GBFS, GTFS, NeTEx), .... Also used in case of map-oriented planning/booking | 
| userGroups | | A list of user groups, that might be used to expose extra assets for members-only. Contains group identifiers that can be agreed on in a peer-2-peer setup. |
| useAssetTypes	| | comparable with `useAssets`, but now referring to assetTypes from /operator/available-assets |
| estimatedDistance | | the estimated distance for the request. Used instead of 'via'-points; this requires routing on TO side. (#378). If the TO needs this information, the Process Identifier (see [processIdentifiers](processIdentifiers.md)) 'USE_ESTIMATED_DISTANCE' should be included in the meta-endpoint.

## Example
```
{
  "from": {
    "name": "Dam, Amsterdam",
    "coordinates": { 
      "lng": 4.892318810863422,
      "lat": 52.3730401756074
    }
  },
  "radius": 1000,
  "to": {
    "name": "Stationsplein 17-21, 1012 AB Amsterdam",
    "coordinates": {
      "lng": 4.900180469413146
      "lat": 52.379696933756556
    },
    "physicalAddress": {
      "streetAddress": "Stationsplein 17-21",
      "areaReference": "Amsterdam",
      "postalCode": "1012 AB",
      "country": "NL"
    }
  },
  "departureTime": "2021-04-02T08:35:04.327Z",
  "nrOfTravelers": 1,
  "travelers": [
    {
...
    }
  ],
  "useAssets": [],
  "userGroups": [],
  "useAssetTypes": ["NORMAL-BIKE"]
}
```
In this example, someone requests a bike from the Dam in Amsterdam to the Central station in Amsterdam.