[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [Damage](Damage.md)

The damage object holds information regarding a damage of an asset, typically a vehicle. 

## Existing Damage
When renting a shared car the user is responsible for any damages of the vehicle caused by carelessness. Such a damage might happen when the door is opened too wide so that it hits the wall next to the car and e.g. the paint chips of at some place.

In order to be not accountable for damages already existent the user needs to check the condition of the vehicle before starting his trip. This is done based on the list of already known damages. Therefore the TO has to expose the list of damages when the vehicle is SET_IN_USE.

## Example
```
"damages": [ {
            "vehicleComponent": "FRONT",
            "description": "front bumper lower grill loose",
            "pictures": [ "https://car.sharing.com/files/X16072016Z.png", "https://car.sharing.com/files/X16072016Z.png" ]
        } ]
```
