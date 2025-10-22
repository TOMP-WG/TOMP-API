[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [On route](Trip-execution-phase---on-route.md)

After the asset is in use, the end user can travel. In some scenarios it is requested that the end user can pause and resume the trip.
This can also be done by using the same end point for starting the leg.

__Step 1:__ pausing the asset  
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events
{
  "operation": "PAUSE",
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
__Step 2:__ Resuming can be done by using again the 'SET_IN_USE' operation:  
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

From version 1.1 there is also a facility to use the operations 'TIME_EXTEND' and 'TIME_POSTPONE'. The first one asks the TO to extend the rental period a bit, until the timestamp in the `time` field.
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "TIME_EXTEND",
  "time": "2017-07-21T17:32:28Z"
}
```
Or, to ask if the asset can be picked up a bit later:
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "TIME_POSTPONE",
  "time": "2017-07-21T17:32:28Z"
}
```

## Objects ##
[LegEvent](LegEvent.md)  
[Leg](Leg.md)

## Next ##
[End](Trip-execution-phase---end.md)