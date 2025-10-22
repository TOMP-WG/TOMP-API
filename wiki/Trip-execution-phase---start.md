[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [Start](Trip-execution-phase---start.md)

The trip execution phase can be started in several ways:
1) The end-user opens the first asset, the required access information has been delivered by the TO in the [Prepare](Trip-execution-phase---prepare.md) event or in the [Commit](Booking-phase.md) of the booking phase
2) The TO is starting the leg (e.g. rides the taxi to the end-user)
3) The MP will start searching for a physical asset near the end-user

## 1 Opening the asset ##
### Online scenario ###
The end-user is near the booked asset, requests to open the asset (online). The app signals the MP, and the MP calls the TO:
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "SET_IN_USE",
  "asset": {
    "assetId": "bike1",
    "place": {
      "coordinates": {
        "lng": 6.169639,
        "lat": 52.253279
      }
    }
  }
}
```
The bike should be opened now by the TO. In case there is not yet assigned a specific bike to the booking, it should be assigned now.

![](https://user-images.githubusercontent.com/10400054/65756974-73cf3400-e116-11e9-91aa-84c25151ffbd.png)

### Offline scenario ###
The app has to send the information to open the bike (e.g. using Bluetooth). The app has to inform the MP that the asset is in use, only after the bike is opened.
```https
POST https://exampleTO.com/leg/746ac-48792bb-746dac3/events
{
  "operation": "SET_IN_USE",
  "asset": {
    "assetId": "bike1",
    "place": {
      "coordinates": {
        "lng": 6.169639,
        "lat": 52.253279
      }
    }
  }
}
```
![](https://user-images.githubusercontent.com/10400054/65756949-6154fa80-e116-11e9-934f-93278b0c87aa.png)

## The TO is starting the leg ##
The TO can have assets that have to be prepared before they can be used by the end-user. For instance a taxi operator or a bike parked in a carousel. Let's say we're a taxi operator. We've scheduled the leg and our taxi driver is leaving the garage. <br>
We have to inform the MP (and thereby also the end-user):
```https
POST https://exampleMP.com/legs/746ac-48792bb-746dac3/events
{
  "operation": "PREPARE",
  "asset": {
    "assetId": "taxi3428",
    "place": {
      "coordinates": {
        "lng": 6.169639,
        "lat": 52.253279
      }
    }
  }
}
```
After starting the leg with the end-user on board, we have to send 
```https
POST https://exampleMP.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "SET_IN_USE",
  "asset": {
    "assetId": "taxi3428",
    "place": {
      "coordinates": {
        "lng": 6.169639,
        "lat": 52.253279
      }
    }
  }
}
```

## 3 The MP will search for an available asset ##
The last scenario is that an upfront booked asset type has to be searched for. The MP will search for an available asset nearby the end-user, let's say about 15 minutes before start time. 
```https
GET https://exampleTO.com/746ac-48792bb-746dac3/available-assets
```
This one will give all available assets nearby. The MP (or end-user) can select one, the asset can be assigned to the leg:
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events
{
  "operation": "ASSIGN_ASSET",
  "asset": {
    "assetId": "bike18",
    "place": {
      "coordinates": {
        "lng": 6.169639,
        "lat": 52.253279
      }
    }
  }
}
```
After this, scenario 1 can be followed.

# Objects #
The [LegEvent](LegEvent.md) object reflects an operation on the leg, like requesting access information, opening a lock / informing about an opened lock, pausing, closing a lock / informing about a closed lock, assigning assets, extend the leg, or postponing the leg.  
[Leg](Leg.md)

## Next ##
[On route](Trip-execution-phase---on-route.md)