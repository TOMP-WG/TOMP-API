[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) | [Booking phase](Booking-phase.md) | [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [AssetType](AssetType.md)

The assetType is a group of assets, that can be grouped on any subset of properties. Can be used to group them (runtime) on station level, or on certain aspects ('small cars', 'electric bikes', etc).

AssetType is used in the /operator/available-asset endpoint to report the number of available assets, and in the case of ASSET_BASED (See [processIdentifiers](processIdentifiers.md)), the real assets could be published here as well, but please take notice of the rotating asset-id (GDPR).

AssetType is also used in the /plannings/ endpoint, to report -if possible- the real asset that can be booked. If it is only an assetType, there is no problem at all; in most scenarios, the physical asset doesn't need to be known/communicated. If an asset must be assigned later on, please use the /legs/{id}/events - ASSIGN_ASSET event.

| field | required | description | 
| --- | --- | --- | 
| id | *	| Unique identifier of an asset type |
| stationId | | |
| nrAvailable | | If stationId is present, the nrAvailable is expected to find the availableity at that particular station. This is only used in the /operator/available-assets, not in the planning request |
| assets | | the available assets (in /operator/available-assets) or the applicable assets for the planning request |
| assetClass| * | See [Asset Class](Asset-Class.md) |
| assetSubClass| | a more precise classification of the asset, like 'cargo bike', 'public bus', 'coach bus', 'office bus', 'water taxi', 'segway'. This is mandatory when using 'OTHER' as class.
| sharedProperties | * | the properties that are shared over all the assets in this assetType |

## Example
```
        "assetType": {
            "id": "electric-bikes-ams-01",
            "stationId": "ams-01",
            "nrAvailable": 18,
            "assetClass": "BIKE",
            "assetSubClass": "electric bikes < 25km/h",
            "sharedProperties": {
              "fuel": "NONE",
              "energyLabel": "A",
              "image": "https://files.fietsersbond.nl/app/uploads/2014/10/30151126/ST2_Men_Side_CityKit-Stromer.jpg",
              "persons": 1,
              "propulsion": "MUSCLE"
            }
       }
```
This could be part of the response of the /operator/available-assets.  

```
         "assetType": {
            "assets": [
              {
                "id": "ams-bike-02341",
                "overriddenProperties": {
                  "location": {
                    "stationId": "ams-01",
                    "coordinates": {
                      "lng": 6.169639,
                      "lat": 52.253279
                    },
                  },
                  "fuel": "NONE",
                  "energyLabel": "A",
                  "co2PerKm": 0,
                  "brand": "Stromer",
                  "model": "ST-2",
                  "buildingYear": 2018,
                  "colour": "white",
                  "gears": 21,
                  "gearbox": "MANUAL",
                  "image": "https://files.fietsersbond.nl/app/uploads/2014/10/30151126/ST2_Men_Side_CityKit-Stromer.jpg",
                  "persons": 1,
                  "propulsion": "MUSCLE",
                  "stateOfCharge": 85,
                }
              }
            ],
            "assetClass": "BIKE",
            "assetSubClass": "electric bike 45km/h",
          },
```
This could be part of the response of the /planning/ request.  