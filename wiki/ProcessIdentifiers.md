[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Meta Information](Meta-Information.md) > [Process Identifiers](ProcessIdentifiers.md)   

These identifiers describe the possible process flows per module (some are module transcending) or is adding more detailed information that will be needed to make TO and MP operate with each other. Each identifier is described here briefly and more information is needed, you can navigate from there to a precise description, optionally with a sequence diagram. (In progress)

# Operator Information
The availability endpoint has some parameters, that can be conditionally required. Therefore these process identifiers have been introduced:
* AVAILABILITY_REGION_MANDATORY: the parameter regionId is required when calling the availability endpoint
* AVAILABILITY_STATION_MANDATORY: the parameter stationId is required when calling the availability endpoint
* AVAILABILITY_ASSET_TYPE_MANDATORY: the parameter assetTypeId is required when calling the availability endpoint
* AVAILABILITY_ON_SPOT: the parameters lon, lat & radius are required when calling the availability endpoint  

When combining these labels, only ONE of them is required. For example, when you specified that the region is mandatory and the ON_SPOT is applicable as well, it doesn't mean you have to provide regionId AND the lon, lat and radius. You only have to comply with one of these requirements (but you of course may supply them all).

# Planning
The described process identifiers below actually don't describe a process flow, but the requested usage of the endpoints /planning/inquiries and /planning/offers.
In the planning we see a few options: 
* PLANNING_BASED: the planning is made to go from A to B. The 'from' is mandatory, the 'to' is optional. Either departureTime or arrivalTime should be present. If you specify arrivalTime you should also specify 'to'.
* ASSET_BASED: the planning is made based on an asset(s) ('I want to use this bike'). The planning request's useAssets array contains an asset id from the operator information module. This one should be accompanied by one (or multiple) of those:
   * BLUETOOTH_SCAN: the planning is made based on a series of assets, that are found with a Bluetooth scan. The information found during a Bluetooth scan is provided in the useAssets array. The TO must use this information to filter the possible results. This can also be a beacon scan.
   * QR_SCAN: same as BLUETOOTH_SCAN, except the input, is a scanned QR code.
   * NFC_SCAN: same as BLUETOOTH_SCAN, but now with NFC.
   * BARCODE_SCAN: same as BLUETOOTH_SCAN, but now with a barcode.
   * MANUAL_ENTRY: in case the other possibilities are not applicable, a manual code can be requested by the app.
   * OTHER_ID: this can be used in specific situations. MP-TO should contact each other if and how this specific implementation can be arranged.
   * EXACT_ID: this must be used in the 'book-from-map' scenario. An exact identifier (found in the /available-assets/ endpoint) is used.
* SPECIFIC_LOCATION_BASED: the planning is made, like asset-based, but with extra info about the location, e.g. like station id from the Operator Information module.
* ATOMIC_PLANNING_AND_BOOKING: the final planning (booking-intent=true) and booking should be done without user intervention. This is typically used to allow a user to select an asset and directly book it. Like, Pick and Go. This Process Identifier became obsolete when the POST /bookings/one-stop (v1.3) was introduced.

* USE_ESTIMATED_DISTANCE: Use estimated distance to create an offer, instead of using the 'from' and 'to' fields, this TO needs a 'from' and 'estimatedDistance' [version 1.3]

* Mandatory labels:
   * MANDATORY_TRAVELER_AGE: there must be at least one traveler in the request, containing an age.
   * MANDATORY_RADIUS
   * MANDATORY_FROM_STATION_ID
   * MANDATORY_TO_STATION_ID
   * MANDATORY_FROM_STOP_REFERENCE
   * MANDATORY_TO_STOP_REFERENCE
   * MANDATORY_DEPARTURE_TIME
   * MANDATORY_ARRIVAL_TIME
   * MANDATORY_NR_OF_TRAVELERS
   * MANDATORY_FROM_ADDRESS
   * MANDATORY_TO_ADDRESS

# Booking
The booking process itself can be described using these process identifiers:
* POSTPONED_COMMIT: the booking is created, but has no full commitment. The status of the booking (directly after creation) is 'CONDITIONAL_CONFIRMED'. The TO has to confirm using the POST /bookings/{id}/events - COMMIT or to deny it, using the POST /bookings/{id}/events - DENY. This is applicable when the TO has to arrange the required resources to fulfill the trip. [version 2.0]  
* ONE_STOP: a booking can be made directly, without requesting offers. This requires external information (from GBFS, GTFS, NeTEx and so on); identifiers found in these sources can be applied in the booking process. [version 1.4]
* NORMAL: the default booking process is supported. Request offers, book one of them and finally commit it. [version 1.4]  
  
When all of these process identifiers are not in the `booking` process identifiers, the `NORMAL` should be considered.

These can be combined with other booking process identifiers (see also [Access Methods](Access-Methods.md)):<br>
* These identifiers tell you about what is the access code:<br>
  * ACCESS_CODE_QR: a QR code is provided to use during the execution in "token"
  * ACCESS_CODE_PDF: a PDF is provided to use during the execution in "token"
  * ACCESS_CODE_TOKEN: a token is provided to use during the execution in "token"
  * ACCESS_CODE_DEEPLINK: a deep link is provided to use during the execution in "token"
  * ACCESS_CODE_AZTEC: an Aztec code is provided to use during the execution in "token"
  * ACCESS_CODE_AXA_EKEY_OTP: an EKey token is provided to use during the execution in "token"
  * ACCESS_CODE_PHYSICAL_KEY: a description of where to pick up the physical key is provided to use during the execution in "token"
  * ACCESS_CODE_BARCODE: a barcode is provided to use during the execution in "token"
  * ACCESS_CODE_HTML: an HTML page is provided to use during the execution in "token"
* These identifiers tell you about the source of the access code:<br>
  * ACCESS_TICKETSTOCK: a ticket is created in the ticket stock by the TO
  * ACCESS_CODE_BY_TO: the access code is created by the TO. This is the default (not necessary to add).
  * ACCESS_CODE_BY_MP: the access code is created by the MP. (not yet supported).
* These identifiers tell you how to obtain the access code:<br>
  * ACCESS_CODE_IN_BOOKING: The QR, PDF, etc can be found in the booking result 
  * ACCESS_CODE_IN_COMMIT_EVENT: The QR, PDF, etc can be found in the commit result
  * ACCESS_CODE_IN_PREPARE_EVENT: The QR, PDF, etc can be found in the trip execution - prepare the result
  * ACCESS_CODE_IN_ASSIGN_ASSET_EVENT: The QR, PDF, etc can be found in the result. Assigning an asset directly delivers the access information (e.g. for   
opening lockers).
  * ACCESS_CODE_IN_GET_LEG: the access code can be found in the result of GET /legs/{id}
  * ACCESS_CODE_IN_GET_BOOKING: the access code can be found in the result of GET /bookings/{id}

* ALLOW_EXTEND_BOOKING_EXPIRY_TIME: this TO allows an extension of the expiry time of the booking. In the header of the booking response, there is an expiry time (required). Whenever it is near this expiry time, the MP can request a new expiry time. When it is done too often, the TO can decide not to grant the request. [version 1.5]  
* PICK_UP_THE_BILL: this TO takes care of all functionality, except for the payment part. When booking, there must be a valid license plate of a parked car in the 'useAssets' field. It is also possible to supply a payment method using the customer->cards. The returned booking is usually FINISHED [proposed in v1.5]. 

* ATOMIC_BOOKING_SET_IN_USE: the booking, commit & /legs/events/ set-in-use should be done in one strike. This identifier cannot be combined with the 'POSTPONED_COMMIT' scenario. The returned booking is STARTED.
* AUTO_COMMIT: the booking will result in a committed booking, not expecting any /bookings/{id}/events - COMMIT message. This implies that -when cancelling a chain of legs- this leg requires to CANCEL the leg.  


* **Deprecated** ATOMIC_BOOKING_UNLOCKING: the booking, commit & unlock (from the trip execution module) should be done in one strike. This identifier cannot be combined with the 'POSTPONED_COMMIT' scenario. The returned booking is STARTED.

These identifiers can be used in combination (therefore there is an array of processIdentifiers in the API):
```
{ ...,
  "processIdentifiers": { "booking": ["NORMAL", "ACCESS_CODE_BY_TO", "ACCESS_CODE_PDF", "ACCESS_CODE_IN_COMMIT_EVENT"], ... },
...
}
```
# Trip Execution
The trip execution is the most complex one here. 
* LOCK_UNLOCK_REMOTELY: the asset is locked/unlocked remotely
* LOCK_UNLOCK_APP: the asset must be opened using the app. For now, you have to use the deep link solution.
  * LOCK_UNLOCK_BLUETOOTH
  * LOCK_UNLOCK_DEEPLINK
  * LOCK_UNLOCK_WIFI
  * LOCK_UNLOCK_NFC
  * LOCK_UNLOCK_RFID (cannot be supported by the app, unless a button "It's open"/"It's closed").
  * LOCK_UNLOCK_SHOW_ACCESS_CODE
  * LOCK_UNLOCK_OWN_SDK
  * LOCK_UNLOCK_OTHER
* USE_PREPARE_TO_INDICATE_START: the TO (taxi) will send a prepare event to the MP to indicate it started moving towards the pickup address.
* ETA_NOTIFICATION: the TO will send ETA notifications to the MP. Whenever 'Arrived' is sent as an ETA message, the asset is at the pickup location. This ETA is up forehand of the trip, e.g. the taxi is coming to you and sends information about the time of arrival at YOUR pickup location. To send ETAs during the trip, use PROGRESS_NOTIFICATION.
* PROGRESS_NOTIFICATION: the TO will send the progress of the trip using POST /bookings/{id}/progress
* GENERAL_NOTIFICATION: the TO can send additional information (e.g. to the end user) using POST /bookings/{id}/progress
* TO_CONTROLLED: the TO (e.g. taxi) will send the SET_IN_USE and FINISH events to the MP.
* OFF_BOARDING_REQUIRED: The TO requires off-boarding evidence in the FINISH event. __DEPRECATED__ Use the offBoarding steps [process steps](process-steps.md).
* SUPPLIES_CALL_SERVICE: when a telephone number is supplied at booking time, this number will be (automatically) called a few minutes in advance, before the asset arrives at the `to` location.
* AUTO_UNLOCK: after the booking process has ended (by /bookings/{id}/events - COMMIT OR by the AUTO_COMMIT), the assets is UNLOCKED directly by the TO. __DEPRECATED__ Use the ATOMIC_BOOKING_SET_IN_USE process identifier.
* in some cases the location is required in the leg events. We have added these process identifiers to cope with it:
  * LEG_EVENT_LOCATION_REQUIRED_SET_IN_USE: the location must be supplied when starting the leg
  * LEG_EVENT_LOCATION_REQUIRED_PAUSE: the location must be supplied when pausing the leg
  * LEG_EVENT_LOCATION_REQUIRED_OPEN_TRUNK: the location must be supplied when the trunk (/helmet box) is opened
  * LEG_EVENT_LOCATION_REQUIRED_FINISH: the location must be supplied when the leg is ended
  * LEG_EVENT_LOCATION_REQUIRED_TIME_EXTEND: the location must be supplied when the leg is extended in time (whenever possible of the asset)
  * LEG_EVENT_LOCATION_REQUIRED_ASSIGN_ASSET: the location must be supplied when assigning an asset  
  * LEG_EVENT_LOCATION_IS_USER_LOCATION: the location of the user must be supplied in the asset.overriddenproperties.place. Please remind this is a GDPR related issue! Don't apply it without additional security actions (v2.0).  
  _There is no generic LEG_EVENT_LOCATION_REQUIRED process identifier: you have to be aware of what you are requesting. Sharing this information requires a need to share it (GDPR)._

# Support
Support is straightforward and doesn't need any process identifiers (yet).

# Payment
Deposit and refunding issues must be communicated in the conditions because it can depend on who (MP) booked the leg. The only identifier we added is 
* CORRECTION_BY_EXTRA_COSTS: the estimated costs in the booking can directly be committed, and the difference between the actual costs (calculated after the trip execution) will be communicated to the MP with a POST /payments/{id}/claim-extra-costs.
* DEPOSIT: the TO requires a deposit before the trip can be executed. The process of how to get it is externally handled (NON-TOMP) [version 2.0]
* PAY_WHEN_FINISHED: the TO requires a direct payment after the trip is finished [version 2.0]
* UPFRONT_PAYMENT: the TO requires the payment before the trip starts. [version 2.0]

# General
General has - for now - one process identifier, but it is an important one since it impacts all endpoints.
* TO_OPERATOR_REQUIRED: in ALL the requests, the header 'addressed-to' field is mandatory (if this header field is specified). This is applicable when the TO is 'behind walls', like in a platform or in a broker/routing structure.