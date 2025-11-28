### Asset statusses

The asset statusses are not pre-defined. The operations are also free to create, but they have to be compliant with OGC API processes.  
The returned object must be a geojson, containing the package, just like all the other endpoints deliver.

Example json (list of links), to unlock (seperated from the 'start-leg') a bike
```json
[ 
    { "rel": "unlock-asset", 
      "href": "https://bike.org/tomp/v2/processes/unlock-asset/execution", 
      "body": { "inputs": { "asset": "GDR:GBFS_vehicle:2581dd23-460d-4df0-b8cf-fb2c97e17a40" } },
      "method": "POST",
      "type": "application/geo+json"
    }
]
```
The 'GDR:GBFS_vehicle' prefix must be available in the GET /collections/datasources/items endpoint, as a 'rel', referring to the source file where this asset can be found.

This approach can also be used to unlock lockers (the word 'asset' in the url is not mandatory, it can also be 'unlock-locker', or 'connect-charger').