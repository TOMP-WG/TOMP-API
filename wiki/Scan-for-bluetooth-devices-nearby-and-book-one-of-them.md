__DRAFT__

This scenario is not yet completely in the API, but for now we can do it like this:
1. Do a bluetooth scan to find nearby assets.
2. call /planning/ with booking-intent=true and fill the field 'assetIds'. It should contain an array of scanned bluetooth (or other technique) devices. 
3. let the user decide which asset to use (or select on yourself, based on their profile)
4. book it using ​/bookings​/. It should result in a PENDING booking.
5. whenever the call is successful, call the /bookings/{provided id}/events { "operation": "COMMIT" } This way you have 2 points in time to verify that the asset is still available.
6. Now it's time to unlock the asset. Request information to open the lock ( using /executions/{id}/events { "operation": "PREPARE" } ). The result contains a field 'assetAccessData'. As far we know now, every (bike) operator has his own way of unlocking. This is unfortunally not yet standardised. **The MP should only show assets in their app they know how to open these!**
7. After a successful unlock, the start of the trip should be registered: using /executions/{id}/events { "operation": "SET_IN_USE" }.