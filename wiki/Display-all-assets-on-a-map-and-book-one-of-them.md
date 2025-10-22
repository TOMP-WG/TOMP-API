1. You have to use the endpoint /operator/available-assets (Operator Information). In the result all physical assets are reported, including there (near) real-time locations. 
2. The user can select one of them on the map (you can show the information provided by the available-assets call). 
3. When the user decides to book it, call the endpoint ​/plannings​/ with in the field 'use-asset' the corresponding asset-id and booking-intent=true
4. There should be a result (normally one, just showing the required asset. It might be that the same asset has some different fare options, be aware of this!). Or, in case the asset has been booked just between your 2 calls, it's an empty result.
5. Use the provided id in the result to book (/bookings/). 
6. A successful booking has to be followed with a commit of the booking, because it's still in the 'PENDING' state: /bookings/{provided id}/events { "operation": "COMMIT" }
7. Now the unlocking can be done. The normal way to do this, is requesting a way to open the bluetooth device. This can be done using the /executions/{provided id}/events { "operation": "PREPARE" }. In the result there is a field 'asset-access-data', containing information to unlock the device.
8. After a successful unlock, the /executions/{provided id}/events { "operation": "SET_IN_USE" } should be called, so the starting point of the leg is registrated.