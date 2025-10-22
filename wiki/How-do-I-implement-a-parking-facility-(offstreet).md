[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) > [Parking](How-do-I-implement-a-parking-facility-(offstreet).md)  

**Q**: How to implement a Parking facility?<br>
_A_: I'll list them per module:<br>
Planning module<br>

* You WILL RECEIVE a lot of calls on the POST /plannings/ endpoint. Most of them will contain 'booking-intent=false'. Those are request for availability during the planning phase of the MPs. Just give a fast answer if you think you're able to fullfil the request. The location of the start and endpoint should be nearby your parking facility. (openstanding issue for stationId in the planning-option request #140).<br>
* You WILL RECEIVE calls on the POST /plannings/ endpoint with 'booking-intent=true'. You MUST persist the results you return, because the IDs you have to generate (or take from your internal system) are a reference during the whole process. The information you offer won't be supplied back to you. Be as precise as possible in your results.<br>
* You CAN put entrance information in the result (token field), like QR or BAR codes. (alternative: provide it on trip execution). You also CAN sent back a specific location, for instance a specific slot (e.g. B593) in the 'meta'-field. The key for this entry should be 'slot'. (e.g. _meta: [ {"slot":"B593" } ]_ ).
* YOU SHOULD add a toAddress containing the entrance gate.

Booking module<br>

* You WILL RECEIVE bookings POST /bookings/, in the body an ID you provided. Reserve a parking spot for the requested period and respond a 'PENDING' result.
* You WILL RECEIVE a POST /bookings/{id}/events within seconds. If it contains a COMMIT, commit the booking, otherwise release it again. Don't forget to mark the provided access information as invalid.

Trip execution module<br>

* If you didn't provide access information in the booking process, you WILL RECEIVE a /executions/{id}/events with the type 'PREPARE'. This means the end user is requesting access to the facility. You can OR provide access information on this moment, or open the gate remotely.
* As soon the gate is opened and closed correctly, you MUST send a /executions/{id}/events with 'SET_IN_USE' to the requesting MP.
* As long the asset is parked, you CAN receive post /executions/{id}/events with the type 'PREPARE'. The location object contains a long/lat, the nearest door should be opened to provide entrance to the end user. (needed #179).
* When the asset request to exit the facility, you probably WILL receive a 'FINISH' event on the /executions/{id}/events. 
* If you don't receive a 'FINISH', but a 'START_FINISHING', it is also a request to open the exit gate. After successful opening and closing the exit gate you HAVE to send a 'FINISH' to the MP as confirmation that the process has been finished. 
