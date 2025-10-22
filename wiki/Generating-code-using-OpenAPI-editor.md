## How to generate code ##
Past the content of the TOMP-API.yaml in https://editor.swagger.io/. The easiest way to do this is to copy the content from https://raw.githubusercontent.com/TOMP-WG/TOMP-API/dragonfly/TOMP-API.yaml, where 'dragonfly' is the branche name. In the editor you can select the language and which part you want to generate: the server side (TO and MP, select only the appropriate endpoints) and the client side (to call the server, most of these are for the MP. The TO should only use the code parts for calling the MP, so notifications and events concerning booking and trip execution).

Choose the language you prefer, generate the code, and do a comparison (e.g. using [WinMerge](https://winmerge.org/)) with the last version you've generated. Take only the changed parts, so your code will be impacted in a minimal way.

## Tip: how to create compact code ##
When you generate code from the OpenAPI specification, you can do these steps to make the code more compact and usable:
* remove the 'allOf' operators, containing only 1 referenced object and a description. These are added to add a description. Without these 'allOf' operators, there is no ability to add a description to a referenced object.  
F.x.:
```
            pricing:
              description: The pricing information of the overall booking, in addition to any leg pricing, 
                if not all legs have pricing the booking should have the fare
              allOf:
                - $ref: "#/components/schemas/fare"
```
should become:
```
            pricing:
              $ref: "#/components/schemas/fare"
```

Known locations [1.2.0]: 
* booking.pricing
* bookingRequest.from
* bookingRequest.to
* bookingRequest.customer
* conditionReturnArea.returnArea
* leg.from
* leg.to
* leg.assetType
* leg.asset
* leg.pricing
* leg.progressGeometry
* leg.ticket
