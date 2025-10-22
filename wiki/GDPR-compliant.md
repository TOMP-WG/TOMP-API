[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [GDPR](GDPR-compliant.md)  

In the endpoint /operator/available-assets it's possible to list collections of assets (e.g. per type or per station). It's not necessary to add the real assets in these collections, in most cases reporting the number of available assets per collection will do for most scenarios, except for the map-oriented apps.

```
[
  {
    "id": "id_x",
    "nrAvailable": 29,
    "sharedProperties": {"name": "yellow bikes", "colour": "yellow"}
  }
  , 
  {
    "id": "id_7",
    "nrAvailable": 3,
    "sharedProperties": {"name": "brown bikes", "colour": "brown"}
  }
]
```
But, if you want to facilitate displaying your assets on a map, you must of course should list assets and their locations. This is non-GDPR compliant if you use every time the same id or name for the same asset.

The solution of GBFS 2.0 is also embraced by the TOMP-API: rotating asset ids. As soon a trip is ended, the asset should get a new id. This way it becomes harder to trace the bikes.