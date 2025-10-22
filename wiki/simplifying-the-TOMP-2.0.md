# Context
We have found out in the past few years that there are quite a few other standards out there in the (Mobility) world that are more or less related to the working field of the TOMP-API. And since our mission contains alignment as one of the key aspects, we will move towards a new version, **taking other standards into account**, not redoing/reinventing functionality that they have as well. This **[decreases the number of endpoints](https://github.com/TOMP-WG/TOMP-API/wiki/simplifying-the-TOMP-2.0#endpoints.md)** we have nowadays.  

Secondly, we have introduced in the past versions **functionality that is hardly or not used**. Therefore, we want to use this page as well: we will describe here endpoints we want to drop, resulting also in a **[decrease of endpoints](https://github.com/TOMP-WG/TOMP-API/wiki/simplifying-the-TOMP-2.0#endpoints.md)**, to make it easier to understand and implement the TOMP-API.  
This also applies to the **postponed-commit scenario**, it can be dropped.

Thirdly, some concepts are needlessly complex. We'll propose **[a more simple solution](https://github.com/TOMP-WG/TOMP-API/wiki/simplifying-the-TOMP-2.0#simplifying-concepts.md)** for them.  

If you're interested, you can find the latest specification [here](https://github.com/TOMP-WG/TOMP-API/blob/transmodel-v1/TOMP-API.yaml.md).

# Endpoints 
On this page we'll enlist all the known endpoints of the TOMP v1.5.0. We'll write our ideas on what should happen with these endpoints in version 2.0. If you have other considerations, please [report](https://github.com/TOMP-WG/TOMP-API/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=%5BSIMPLIFY+REQUEST%5D+.md) them!

### Planning/booking
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|POST /planning/inquiries|Drop it||
|POST /planning/offers|Make it Transmodel compliant<br>_POST /offers_||
|POST /bookings/one-stop|Make it Transmodel compliant<br>_POST /bookings/one-stop_||
|POST /bookings|Make it Transmodel compliant<br>_POST /bookings/{id}_||
|POST /bookings/{id}/events|Make it Transmodel compliant<br>_POST /bookings/{id}/operations/{operation}_||
|GET /bookings/{id}|* Make it Transmodel compliant<br>* Add reporting functionality (event log, progress, notifications, ...)<br>_GET /bookings/{id}_ ||

### Trip execution
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|All trip execution endpoints|Add /bookings/{id}/ in front of them to refer to a leg in a booking||
|GET /legs/{id}/available-assets|* Make it Transmodel compliant<br>* make it also usable for seat reservation<br>_GET /bookings/{id}/legs/{lid}/available-assets_||
|GET /legs/{id}|Incorporate it in /bookings/{id}/ OR<br>maybe not. It contains possible HATEOAS links for each leg. In the booking it doesn't||
|PUT /legs/{id}|Drop it. Altering a leg should be done using the /legs/{id}/events endpoint<br> - ||
|POST /legs/{id}/ancillaries/{category}/{number}|* Make it Transmodel compliant OR<br> * migrate it to the /legs/{id}/events endpoint<br>_POST /bookings/{id}/legs/{lid}/operations/ADD_ANCILLARY_||
|DELETE /legs/{id}/ancillaries/{category}/{number}|* Make it Transmodel compliant OR<br> * migrate it to the /legs/{id}/events endpoint<br>_POST /bookings/{id}/legs/{lid}/operations/REMOVE_ANCILLARY_||
|POST /legs/{id}/events|Make it Transmodel compliant<br>_POST /bookings/{id}/legs/{lid}/operations/{operation}_||
|GET /legs/{id}/progress|Integrate it into the GET /bookings/{id}<br>-||
|POST /legs/{id}/progress|Drop it<br>-||
|POST /legs/{id}/confirmation|* Drop it OR<br> * migrate it to the /legs/{id}/events endpoint<br>_POST /bookings/{id}/legs/{lid}/operations/CONFIRM_REPLACE_ASSET_<br>_POST /bookings/{id}/legs/{lid}/operations/CONFIRM_START_LEG_||

### Operator information
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|Almost every operator information endpoints should be dropped, start using external standards||
|GET /operator/ping|Maintain as is<br>_GET /discovery_||
|GET /operator/meta|Make it Transmodel compliant<br>_GET /ping_||
|others|drop||

### support
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|POST /support|Make it Transmodel compliant<br>_POST /bookings/{id}/legs/{lid}/support_||
|GET /support/{id}/status|Make it Transmodel compliant<br>_GET /bookings/{id}/legs/{lid}/support_||

### payment
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|GET /payment/journal-entry|Make it Transmodel compliant<br>_GET /journal-entries_||
|POST /payment/{id}/claim-extra-costs|migrate it to /legs/{id}/events<br>_POST /bookings/{id}/legs/{id}/operations/CLAIM_COSTS_||

### general
|Endpoint|Ideas|Decision|
|-----------|-----------|-----|
|GET /bookings/{id}/notifications|merge it into the GET /bookings/{id}<br>-||
|POST /bookings/{id}/notifications|merge it into the POST /legs/{id}/events<br>_POST /bookings/{id}/legs/{id}/operations/NOTIFY_||

# Simplifying Concepts
We should consider renaming all concepts to Transmodel equivalents. If there are multiple candidates, we must make change proposals for Transmodel (to adopt our concept).  

## In general
In general, we should consider adding HATEOAS links, that will allow us to see in a response what the possible next steps are. For instance, when you call POST /bookings/, the result will be a booking and a set of operations (COMMIT, CANCEL) and how to call them.  

|Concept|Ideas|Decision|
|-----------|-----------|-----|
|Booking|Represents in most cases only 1 leg. Merge LEG and BOOKING, with an option for additional LEGs.||
|Booking|Drop the functionality of multiple legs in one booking, it will simplify the endpoints a lot!! ||
|AssetProperties+Asset|Merging both concepts, so you don't have an additional field 'sharedProperties'.||
|Conditions|Additional conditions will be replacing some fields from the assetProperties||
|BookingRequest|Allow multiple 'previousLegs' instead of just the previous one||
|Error|Allow multiple errors in the results||
|AssetType|will be a reference to an external data source||
|Station|will be a reference to an external data source (it already was, made it explicit)||
|Stop|will be a reference to an external data source (it already was, made it explicit)||
|Region|will be a reference to an external data source||
|Requirement|will be a reference to an external data source (it already was, made it explicit)||
|Asset|will remain as a concept, but can be supported/extended using an external data source||
