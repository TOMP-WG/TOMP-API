In the TOMP-API, we allow to book assets and asset types that are specified in other data standards, like GBFS, GTFS or NeTEx. This page tells you how you have to configure things (in the endpoint specification, the discovery) to 'plug' the external data in the TOMP booking process.

# Learning by example
**Example 1**: a free-floating bike operator has its own GBFS files, specifying the assets in the vehicle-status file (or JSON endpoint). In the discovery part of the TOMP, you should specify in that case:

```json
"endpoints": [
{ "method": "GET", "externalType": "GBFS", "path": "https://some-external.url/GBFS/vehicle_status.json",
  "useAssets": ["vehicle_status.vehicle_id" "visualID"], "status": "IMPLEMENTED" },
{ "method": "POST", "path": "https://some-external.url/TOMP/v1/bookings", "status": "IMPLEMENTED" }
]
```
You indicate that the field 'useAssets' in the offer request or the one-stop booking request can contain IDs from your GBFS file 'vehicle_status', from the field 'vehicle_id'. OR you can supply a visual ID on the bike. 

**Example 2**: a scheduled ferry, using NeTEx to publish their operations.

```json
"endpoints": [
{ "method": "GET", "externalType": "NeTEx", "path": "https://data.ndovloket.nl/netex/wsf/NeTEx_WSF_WSF_20231206_20231206.xml.gz",
  "useAssetTypes": [ "Route.id", "RouteLink.id" ], "status": "IMPLEMENTED" },
{ "method": "POST", "path": "https://some-external.url/TOMP/v1/bookings", "status": "IMPLEMENTED" }
]
```
The ferry operator allows you to book using the IDs of the route or routelink, when you supply and ID one of these in the field 'useAssetTypes'.

## Allowed values  
for useAssetTypes:
```
              # GBFS
              "vehicle_types.vehicle_type_id",
              # GTFS
              "routes.route_id",
              "trips.trip_id",
              # NeTEx
              "Route.id",
              "RouteLink.id",
              "Line.id",
              "TimingLink.id",
              "TimingPattern.id",
              "ServicePattern.id",
              "JourneyPattern.id",
              # OSDM Online
              "CoachLayout.layoutId::Compartment.number::PlacePosition.number"  
```

for useAssets:
```
              # common, identifying codes/names on assets, QR codes
              "visualId",
              # GBFS
              "free_bike_status.bike_id",
              "vehicle_status.vehicle_id"
              # GTFS
              # NeTEx -> spot IDs?
```