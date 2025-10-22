[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Meta Information](Meta-Information.md)

# Meta Information

The TOMP-API contains a self-describing endpoint (/operator/meta). This endpoint contains information about the endpoints that are implemented and a series of ‘process identifiers’, describing how the process flow around these endpoints should be. Alternatives like HATEOAS don’t cover the required functionality. These Process Identifiers are described in the wiki on Github ([ProcessIdentifiers](ProcessIdentifiers.md)).

For example, in the planning module, there is the process identifier ‘ASSET_BASED’, telling that the TO provides nearby assets to end-users in the near future. It supports the pick-up-and-go scenario. The MP cannot reserve assets from this TO as long they don’t provide ‘PLANNING_BASED’ as well.

But in combination with ‘ASSET_BASED’, the MP must supply a reference to the asset. When the TO requires the identifier ‘QR_SCAN’, the reference to the asset can be gained by the MP using a QR scan.
There are quite a few process identifiers, making it possible to describe the process of the TO. The list of process identifiers on Github is leading, but new identifiers will be introduced in the future, together with new releases of the swagger file. 

This is an example response:
```
[
  {
    "version": "1.0.0",
    "baseUrl": "https://dummy-bikes.org/",
    "endpoints": [
      {"method": "POST","path": "/planning-options/","status": "IMPLEMENTED"},
      {"method": "POST","path": "/bookings/","status": "IMPLEMENTED"},
      {"method": "POST","path": "/bookings/{id}/events","status": "IMPLEMENTED"},
      {"method": "GET","path": "/bookings/{id}","status": "NOT_IMPLEMENTED"},
      {"method": "PUT","path": "/bookings/{id}","status": "NOT_IMPLEMENTED"},
      {"method": "GET","path": "/bookings/?state=","status": "NOT_IMPLEMENTED"},
       .....
     ],
    "scenarios": [
      "POSTPONED_COMMIT"
    ],
    "processIdentifiers": {
      "planning": [ "ASSET_BASED", "QR_SCAN" ],
      "booking": [ "ACCESS_CODE_DEEPLINK", "ACCESS_CODE_IN_COMMIT_EVENT"],
      .....
     ]
   }
  }
]
```

# Steps
Since version 1.5.0, we included the [process steps](process-steps.md) in the meta endpoint:
```json
  "steps": {
      "planning": [ { ... } ],
      "booking": [ { ... } ],
      "onboarding": [ { ... } ],
      "offboarding": [ { ... } ],
      "pausing": [ { ... } ],
      "resuming": [ { ... } ]
    }
```