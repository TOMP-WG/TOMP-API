[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Asset based](Asset-based.md)  

Asset based planning will need an identifier to distinguish the asset you're looking at (or at least should be nearby). This identifier can be found in several ways, using Bluetooth or another identifying method. It will be very likely that you can directly send a planning request with booking intent; you don't have to plan a trip. By using the booking-intent=true the TO will generate offer(s) for the asset directly.  

For a description of the endpoint itself, see [Planning based](Planning-based#request.md).

> Whenever you want to require the MP to do planning and booking in __one go__, you should add 'ATOMIC_PLANNING_AND_BOOKING'. It will force the MP to request a planning with booking intent and directly book the returned asset, without user interaction.  

## Bluetooth
For Bluetooth we need to do a Bluetooth swipe before we can plan/book the asset, adding all found Bluetooth devices in the planning request: 
```
(v1.0) POST https://exampleTO.com​/plannings/?booking-intent=true
{
  ...
  "useAssets": [ "2058f89b-9aec-4515-9ee1-f453fccd71fe", "61d4a23a-248d-497f-ab7b-9b36dfec2568", ... ],
  ...
}

(v1.3 and above) POST https://exampleTO.com​/planning/offers
{
  ...
  "useAssets": [ "2058f89b-9aec-4515-9ee1-f453fccd71fe", "61d4a23a-248d-497f-ab7b-9b36dfec2568", ... ],
  ...
}
```
The TO can look into his known bluetooth operated assets and respond with a planning option for each matching asset. To request the MP to add Bluetooth IDs in the request, you should add 'ASSET_BASED' and 'BLUETOOTH_SCAN' in your process identifiers (GET /operator/meta) [more...](ProcessIdentifiers.md).  

## Station oriented
It is also possible to request assets for a specific station. Adding 'SPECIFIC_LOCATION_BASED' to the [process identifiers](ProcessIdentifiers.md) will force the MP to add at least a stationId in the 'from' field (or a stopReference in case of a public transport operator):
```
{
  "from": {
    ...
    "stationId": "string",
    ...
  }
} 
```

## Other identifying methods
Other identifying methods, like QR code, NFC, Barcode or manual entry of an identifier, work similar. Instead of sending the Bluetooth IDs, the QR code, NFC ID, barcode number or manually entered ID should be sent in the 'useAssets' array. Of course, the appropriate process identifier should be added in the meta endpoint (GET /operator/meta) [more...](ProcessIdentifiers.md). 

 