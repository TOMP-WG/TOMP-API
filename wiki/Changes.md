[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Changes](Changes.md)

### 1.6.0 - Dragonfly (likely release date: 2025/01/23)
*Contracts, conditions*  
Extended functionality to specify pre-conditions, and how to handle these  

*Communication*   
Extended the "information object" to give more detailed informed to the MP.

**Feature requests**
- #540 Precondition Required
  - added error code 428 (Precondition required)
  - added additional steps
  - extended the information object (+ PLAIN_TEXT & HTML)
  - added conditions on mandatory steps
- #526 Terms & conditions
  - extended the information object
- #103 Add 'Code of conduct'
- #532 Added a bounding box for available assets
- #528 Refer to asset in support request
- #553 Transmit user location on events. Requires GDPR mitigating actions.

**Change requests**
- #533 ValidUntil on card object optional
- #519 Required Personal data in the booking process
- #530 Remove obsolete ATOMIC_PLANNING_AND_BOOKING process identifier
- #557 Cancel a pending booking

### 1.5.0 - Dragonfly (release date: 2023/12/20)
*Use cases described*  
In the section [Use cases](Use-cases.md) we enlisted quite a few use cases, each of them with a clarification and how to implement it.

*Improved trip execution*  
In this version, some extensions have been made to support the trip execution & payment even better. An exact description of the steps to be taken (like opening lockers, connecting to chargers, which event to send, etc) is added. Also, a distinction is made between fares during pauses and when travelling.  

*Improved communication*  
Additional fields have been added to communicate additional information between TO and MP, or to get access to information on each other's side.

Major extensions:
- You can specify the atomic steps to take during OnBoarding, OffBoarding, Pausing and Resuming a trip (#480)
- Pausing a leg without locking the asset (#498)
- Handle a different fare when paused (#501)

**Feature requests**
- #480 Self-describing actions (added conditions & added 'steps' in meta-endpoint)
- #481 Extend booking expiry time (added new event type)
- #482 Required location in events (added process identifier)
- #484 Asset replacement and early asset return (added actual times)
- #498 Pause without locking
- #499 Add assets in progress events
- #500 Add filters in GET /bookings/ endpoint
- #501 Payment in paused state
- #516 Damages (see also [Damage](Damage.md))

**Change requests**
- #478 stationId or regionId required in available assets (added process identifiers)
- #489 Support additional leg event

**Bugs**
- #472 /payment/journal-entry in version 1.3.0 has incomplete category enum in query parameter (textual)
- #492 The /bookings/one-stop request body is missing the callbackUrl field. 
- #502 Journal entries category in Swagger file is not updated (textual)

### 1.4.0 - Dragonfly (release date: 2022/12/01)
Major extensions:
- The one-stop booking process for public transport and map-oriented assets (#462)
- Added context to a booking, allowing reduction (#422)
- Better support taxi process (#421, 420, 422)
- Better support scooters/bikes in the support module (#436, 380, 452, 351)
- Integration with other standards (#440)

**Feature requests**
- #357 Helmet specification (Bikes)
- #451 Region ID in asset object (Bikes, scooters, shared cars)
- #450 Notifications on leg level (All)
- #421 Call service (Taxi)
- #439 Missing error codes (all)
- #436 Upload images to support module (bikes, scooters)
- #438 Add ‘Ferry’ to vehicle types (Ferry)
- #380 Add ‘User out of limits’ (bikes, scooters)
- #420 Arrival guarantee (taxi)
- #422 Flight number (=add context, all)
- #426 make overriddenProperties not required (all)
- #346 Add ‘extraInfo’ to planningRequest (all)
- #351 become compliant with GBFS 2.1 (bikes, scooters)
- #441 Show additional user information at booking or starting (all)
- #452 Indicate which off-boarding evidence is required (bikes, scooters, shared-cars)
- #459 Add memo to booking / legs (all)
- #440 Specify how to use other standards
- #461 Add VAT Identification number to journal-entry (all)
- #462 Add one-stop-booking (public transport, bikes, scooters)

**Change requests**
- #448 Add IDEAL as payment method (all)

**Bugs**
- #429 Documentation error code x203 is used twice
- #460 Invalid reference to older version

### 1.3.0 - Dragonfly
We tried to keep the API backwards compatible and succeeded. Major extensions are for:
- alignment with GOFS (402, 399, 398, 395, 396)
- added ancillaries (357)
- alignment with blockchain solutions (390, 391)
- an extension of the regions (384)

**Feature requests**
- #402 split the planning endpoint into inquiry ('booking-intent=false') and offer (='booking-intent=true')
- #384 extend areas. Now also available: NO_PARKING, NO_ACCESS, SPEEDLIMIT, ...

**Change requests**
- #399 add main asset type in booking, to facilitate simplifying the booking object (no legs)
- #398 add overall start and end time in booking, to facilitate simplifying the booking object (no legs)
- #395 make 'assetClass' conditional required
- #397, #396 make 'type' and 'vatrate' conditional mandatory in farepart (simplifying the fare structure)
- #393 add mileage to journalEntry
- #392, #368, #358 extend asset with mileage, number of doors, max speed, and license plate (GDPR warning)
- #391, #390 extend assetType with references to pricing and conditions (f.x. for this bike you need to be 12)
- #389 make nrOfTravelers optional, when it's not there, it's one.
- #378 add 'via' in planning request
- #362 add a category to journalEntry
- #273 ability to share ETA with location
- #414, #415 price ranges & indication 'normal price' and additions (or discount).

**Bugs**
- #400 specify number formats
- #382 remove circular dependencies

### 1.2.0 - Dragonfly
Again, no breaking changes. Even requests from a 0.9.0 version are processable in this version since we're backward compatible for over a year now! If you need one of the enlisted issues, you can implement this version. 
The biggest changes are:
- related to the communication of personal information while planning/booking (#336, #347)
- better integration of the deeplink process (when returning into the MaaS app, error handling) (#348)
- better support for 'non-happy' flows: cancelation of bookings/legs and extension of support (stolen/lost scenario) (#314, #337)

**Feature requests**
- #336 the CROW woordenboek ('travelers dictionary') has been formalized & integrated
- #314 extended enumeration of supportType & created a new endpoint to request confirmation from TO side (to be implemented by MP)
- #348 added fields to support deeplink integration (return URL when finishing the trip)
- #325 extended enumeration of legStates with 'cancelled' & events with 'CANCEL'
- #328 the TO can directly book a leg, without planning.

**Change requests**
- #312 request stations within a specific radius
- #337 added a field to determine who canceled the leg: the MP or the end-user
- #347 added fields to support an external source for user information
- #349 divergent base URL (the MP has a different URL to reply)
- #352 add a health check endpoint
- #353 specified address fields

**Bugs**
- #338 journalEntry.invoiceId had no type
- #335 Headerfields for MaaS id of the sender and receiver, was in the API, but not applied on the endpoints
- #334 POST /bookings description mentions leg, but should be booking

### 1.1.0 - Dragonfly  
There are no breaking changes from 1.0.0 to 1.1.0. Everything is backward compatible, but MPs will have to take #177 (Paging) into account when contacting TOs that have implemented 1.1 or above.  

The biggest functional changes between 1.0.0 and 1.1.0  are: 
- adoption of new features of GBFS 2.0  
- support of the offboarding process
- support of multiple region TOs
- support of user groups
- better support of multi leg offers (reference to users & leg sequence)

**Feature requests**  
* #289 Add vehicle_docks_available (GBFS 2.0)
* #237 Adding deeplinks (GBFS 2.0)
* #305 support offboarding process
* #265 support multi-region TOs / #244 regional aspects
* #282 User reference in booking
* #283 Leg sequences
* #248 Simple endpoint for extending legs
* #247 User group support

**Change requests**
* #177 Added paging
* #164 consistency in respond codes 401/403
* #301 Allow POST /booking to respond with 410 - Gone
* #266 RESERVE and ISSUE in leg event
* #277 numbers should be used in geojsonpolygon example
* #264 Idempotency for booking return 409 - Conflict when booking same id twice
* #242 add useAssetType (conform useAsset) in planning
* #245 Add extra notification type: MESSAGE_TO_DRIVER
* #224 Add minutes field to notification

**Bugs**
* #299 Bookingid should not be required
* #179 missing location in legs/{id}/events => solved in explanation in Wiki
* #305 obsolete trailing slashes
* #304 unitType in Farepart should not be required
* #271 inconsistent vatRate / taxRate
* #275 syntax `description` should not used next to `$ref`
* #276 Invalid regex used in phone number
* #277 inconsistent nrAvailable/amountAvailabe in description
* #252 fixed a typo in comment
* #242 assets in available-assets not mandatory
* #243 type field in FarePart should be mandatory

### 1.0.0 - Dragonfly  
**Feature requests**
* #200 Added product description  
* #209 Being able to request a payment/journal-entry on a booking basis 
* #221 Add availability at a particular station/hub and calendar per station/hub
* #222 Extended endpoint legs-event with 503-retry after for temporary malfunctioning.
* #234 GDPR aspect: Rotation of asset ID after rental
* #218 Added sequence diagrams

**Change requests**
* #215 subscription endpoint doesn't need complex request body
* #231 rename field "properties" in Asset; it is a keyword

**Bugs**
* #219 claim extra cost shouldn't be a PATCH
* #228 too many fields in booking object
* #239 Reintroduce REJECTED state as booking state  

### 0.9.0 - Release Candidate Dragonfly<br>
We've taken the lessons learned so far and applied them in the API. Also used reviews to make it better. Major changes: support module has been reviewed (#146), some simplification (#176) and a new endpoint to facilitate a self describing API (#180).  
**Feature requests**
* #147 Using a single url for multiple organizations
* #167 conditionRequireBookingData lacks name  
* #159 Use ISO 8601 (RFC3339) timestamps in JSON body
* #180 Self describing facilities   

**Change requests**
* #176 PlanningOptions has duplicate items and in general could use a cleanup
* #144 renaming "provide-ids" in /planning-options
* #146 Support endpoint refactoring
* #134 Restructure error object duplicate / #163 [FEATURE REQUEST] Specify errors WT1  

**Bugs**
* #186 Example timestamp is in seconds, not in milliseconds
* #165 mandatory fields  

### 0.5.0 _Breaking changes_<br>
* #136 Standardized API error breaking change request
* #133 kebab-case to camelCase breaking change request
* #120 composit-leg should be named composite-leg breaking bug
* #114 Remove items from asset and asset-type (#110) breaking change request
* #111 Consistency in the Operator Information breaking
* #126 Coordinates instead of coordinate

0.4.0<br>
* #93 Trip Execution: ETA is missing change request question
* #115 Add GBFS attributes to station information change request
* #119 Adding personal info change request
* #105 Multiple fields in "type-of-asset" in /planning-options response should not be on type level bug change request
* #112/#116 Missing geometries in Operator Information change request

0.3.1: bugfix<br>
* #131 key-value only contains key.... (bug)

0.3.0: semantic versioning adopted<br>
* #102 Add semantic versioning

1.2: confirmed 1.1.2. No real changes, except for removing server, contact etc.<br>
<br>
1.1.2: more payment phase, but also include the first implementation impacts<br>
Includes:
* Operator information: 
  1. missing available assets in operator information (#83, #96)
* Planning options: 
  1. overlays can now be handled in a composit-leg (#59)
  2. fare scales (#89)
  3. amount of available assets added (in case of type-of-asset results) (#91)
* Payment: 
  1. extra condititions for payment (upfront-payment and pay-when-finished) and optional bank account (#85)
  2. distance or time based scales (#87)
  3. in journal entries time and distance are reported (#87)
  4. composit leg is supported (88)
* some small adjustments:
  1. missing MP/TO id (#86)
  2. geojson to communicate the leg (reducing the message length) (#63)
  3. when booking some extra information could be required (physical pick-up/drop-off addresses, e-mail addresses, date of birth). (#94, #97)
  4. extra modalities (moped, step)

1.1.1: goal: first set up for the payment phase (batch payment).
Includes:
* payment phase
* 'Postponed commit' scenario
* Transport types clarified
* More precise description of travellers for more accurate planning
* return conditions
* some smaller issues:
   1. corrected example values
   2. merge 'mode' and 'type-of-asset'

1.1.0: major changes, not compatible with 1.0.0. <br>
Includes now:
* planning phase
* booking phase
* trip execution phase
* REST implementation
* first setup webhooks
* first setup authentication
* one swaggerfile to maintain
* first setup TOMP API for dummies (WIKI)
* all kinds of smaller issues:
   1. adjustments on the availability check (timestamp, number of passangers, request of ID's, 'woordenboek reizigers'
   2. longitude/latitude is now everywhere in an object instead of array
   3. generic message header
   4. uniformity