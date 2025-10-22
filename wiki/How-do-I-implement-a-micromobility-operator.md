[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) >> [Micro mobility](How-do-I-implement-a-micromobility-operator.md)  

**Q**: How to implement a Micro mobility operator?<br>
_A_: There are several scenarios. At first you'll have the 'map-centric' scenario (click on available assets on the map), but there is also a 'i-want-an-asset-here-and-now' scenario and the 'i-m-in-front-of-an-asset' scenario. But you can also implement the 'upfront-booking' scenario. I'll describe them all.

# Map centric #
<br>Operator module
* You WILL receive a lot of requests on the /operator/available-assets. This information can be shown by any MP to show the location of your assets.

Planning module<br>
* Whenever an end user clicks on an asset, it's information is shown. When the end user wants to use the asset, he'll click on a button to reserve. You WILL receive a POST /plannings/ with the asset id in the field 'assetIds'. You can return a result with only that asset. It should be a planning request with 'booking-intent=true'.

Booking module<br>
* Directly after this, the MP will send a POST /booking/.
* Directly after the booking, the POST /booking/{id}/events with a COMMIT WILL follow.

Trip execution<br>
* The end user can walk to the booked asset and request to open it. Therefore you WILL receive a 'PREPARE' event (POST /executions/{id}/events). The result will contain information about how to open it (QR, bar code, remote controlled, bluetooth controlled, ...).
* After a succesfull unlock, the MP WILL send you a SET_IN_USE event (POST /executions/{id}/events).
* During the ride the bike can multiple times be paused. (PAUSE event POST /executions/{id}/events).
* Before closing the asset again, you WILL receive a 'START_FINISHING' event (POST /executions/{id}/events), wherein you MUST supply the information how to close the asset again.
* After a successfull close operation, the 'FINISH' event WILL be send to you.

# I want an asset now (or in the near future) #
Planning module<br>
* Actually, this is the 'normal' way of using the TOMP API. You WILL receive a planning-options request with a startTime and location. You can return likely options. It might be the case that the MP will directly request with 'booking-intent=true'.
* After this one the end user can select one of the options.

Booking module & Trip execution<br>
* see the Map-centric scenario above.

# I'm in front of an asset #
Planning Module<br>
* The app of the MP can do a bluetooth swipe to find all assets nearby. The found bluetooth IDs can be used in the planning-options request (field: assetIds). You WILL receive these planning options and return only the assets that you recognise as being yours. The request should be 'booking-intent=true'. The end user can select a specific asset; in the result there must be information that can be used by the end user to identify the asset. 

Booking module & Trip execution<br>
* see the Map-centric scenario above.

# upfront-booking #
Operator information<br>
* You WILL receive /operators/available-assets requests; you CAN return results that contain only asset-types (e.g. 'large bikes'). 

Planning module<br>
* Whenever you get a /plannings/, you can return a list of asset-types. You don't know yet which asset you're going to serve.
* Rest: normal way of planning with 'booking-intent=false', 'booking-intent=true'. 

Booking module<br>
* normal way

Trip execution<br>
* A fixed amount of time before the trip starts, the TO can assign an asset to a trip. You MUST send an ASSIGN ASSET event to the MP (POST /executions/{id}/events).
* An alternative: the end user can request all available assets nearby that are fulfilling his initial request. Therefore you WILL receive a GET /executions/{id}/available-assets. You MUST return asset-types containing assets. After his, the end user can claim the asset by using the /executions/{id}/events with ASSIGN_ASSET.