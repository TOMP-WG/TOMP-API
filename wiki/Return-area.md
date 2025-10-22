[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Return area](Return-area.md)  

Another condition in the legs of the option ([booking object](Planning-based#response.md)) is the conditionReturnArea. Per leg (actually per asset) the return station or area can be described. 

| field | description | 
| ----- | ----------- |
| stationId | station to which the asset should be returned, see GET /Operator/stations)
| coordinates | coordinates of the station |
| returnHours | opening hours |
| returnArea | geojson polygon, first and last node must be the same (https://geojson.org/geojson-spec.html#polygon) |

> If the asset needs to be returned at a specific station, fill in the stationId, coordinates and return hours. If the TO uses a free floating set up, respond with the returnArea.