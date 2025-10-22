[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) > [Bike](How-do-I-implement-a-bike-operator.md)  

**Q**: How to implement a Bike operator?<br>
_A_: There are several specific scenarios in the TOMP API for bike operators. I'll list them per module:
* There are several ways to plan a bike. The most common one is "I've got a map, click on a bike and book it" (Click and travel). 
* Another one is a 'bluetooth swipe', where you can find bikes in the area and book one of them (Bluetooth swipe). 
* A thirth option is the booking of a bike in the future (part of a longer trip). (Future usage)

_Click and travel_<br>
Operator information<br>
* Use the /operator/available-assets to retrieve all assets per operator and show them on a map. Whenever an user clicks on a bike, you can show the properties of that bike. 

Planning<br>
* If the user wants to book it, he can click on it, this fires a /planning-options/, fill in the planning-check the property "useAssets" with the id of the asset from the bluetooth device. Don't forget to set the property "provideIds" to true.
* the TO has to return only this asset as planning option (of course, it might be several times in the results, for several reasons, like with/without insurance etc).

Booking<br>
* normal way, no specific items

Trip execution<br>
* Firing /legs/{id}/event with "event": "PREPARE" can result in a leg object with in the field "assetAccessData" necessary data to open a bluetooth lock.
* After the lock is openend, the /legs/{id}/events with "event": "SET_IN_USE" should be fired.
* During the usage of the bike, a sequence of events like "PAUSE", "SET_IN_USE", "PAUSE", "SET_IN_USE" can be executed.
* At the end a /legs/{id}/event {"event": "FINISH", "time": 3423423423, "asset": { ... , "place": { "coordinate": { "lng": ..., "lat": ... } } } } can be fired after locking the bike.

_Bluetooth swipe_<br>
Planning<br>
* This scenario looks a lot like the 'Click and travel', only the operator information isn't needed for this one. After a bluetooth swipe all found bluetooth devices can be put in the planning-check, in the property 'useAssets'.
* The TO can deliver all assets that are his (bluetooth id check). Of course only the assets that are available.
The rest of the booking/trip execution is similar to the Click and travel

_Bike in the future_<br>
Planning<br>
* You can book a bike like a normal asset, but it's very likely you'll have a lot of similar bikes. In that case you can offer assetTypes in the planning phase. 
* In case a request comes in for multiple persons, you'll have to return every asset type for each person (with different ids), so the MP can book a specific assetType for each person.<br>

Trip execution<br>
* Before starting the trip you can assign a specific asset to a leg (assign_asset). This counts like a reservation of the bike.
* This assignment should automatically be done when preparing a bike (request of token) or set_in_use.

**Recap**<br>
You have to implement these endpoints:
* GET /operator/meta
* GET /operator/available-assets (click and travel: provide assets, the other ones: provide only assetTypes)
* GET /operator/stations
* GET /operator/alerts
* GET /operator/operating-calendar
* GET /operator/operating-hours
* GET /operator/information
* GET /operator/pricing-plans
* GET /operator/regions
* POST /plannings
* POST /bookings
* GET /payment/journal-entry

Process identifiers to use in the meta endpoint:
* Planning: ASSET_BASED (with one of the accompanied process identifiers), ATOMIC_PLANNING_AND_BOOKING (click and travel)
* Booking: NORMAL, ACCESS_CODE_DEEPLINK OR ACCESS_CODE_TOKEN (not likely), ACCESS_CODE_IN_[BOOKING|COMMIT_EVENT|PREPARE_EVENT]
* Trip execution: LOCK_UNLOCK_REMOTELY (online operated locks) or LOCK_UNLOCK_APP (with one of the accompanied process identifiers)
