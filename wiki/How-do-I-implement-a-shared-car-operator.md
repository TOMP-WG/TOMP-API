[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) > [Shared car](How-do-I-implement-a-shared-car-operator.md)  

**Q**: How to implement a Shared-car operator?  
_A_: I'll list them per module:  
### Planning module  
The planning module is pretty similar to the other modalities. A planning is posted, and - dependent on the time to depart, it can return OR specific assets (when it's in the near future) OR assetTypes.  
![](https://github.com/TOMP-WG/website/blob/master/wiki/images/Shared-car-process-planning.png)

### Booking module
The booking can be done for the asset or asset type, using the normal process in the TOMP-API: posting a booking (which returns a booking in PENDING state) and committing it.  
![](https://github.com/TOMP-WG/website/blob/master/wiki/images/Shared-car-process-booking.png)

### Trip execution module
Whenever an asset type is booked, the asset will be assigned after the booking process, but before the trip starts. (/legs/{id}/events – ASSIGN_ASSET)  
![](https://github.com/TOMP-WG/website/blob/master/wiki/images/Shared-car-process-trip-assign.png)

The car can be opened using Bluetooth or over the internet (/legs/{id}/events – SET_IN_USE).   
Locking the car at a location that’s not a valid end location (e.g. not at a hub (=station) or area), will pause the usage. (/legs/{id}/events – FINISH returns error => /legs/{id}/events – PAUSE called). When the car is opened again, the /legs/{id}/events – SET_IN_USE is called again. 
![](https://github.com/TOMP-WG/website/blob/master/wiki/images/Shared-car-process-trip-pause.png)

Locked at a valid end location (/legs/{id}/events – FINISH) will end the leg.
![](https://github.com/TOMP-WG/website/blob/master/wiki/images/Shared-car-process-trip-finish.png)

