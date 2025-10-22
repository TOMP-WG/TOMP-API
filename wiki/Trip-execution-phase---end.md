[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [End](Trip-execution-phase---end.md)

Whenever the leg is ended, the asset can be locked again by using the app. The app has to inform the MP that the trip is finished (offline scenario). The MP has to send it to the TO.
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "FINISH",
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
In case of an online scenario the same message has to be send to the MP, this one send it to the TO and the TO should lock the bike.
```https
POST https://exampleTO.com/legs/746ac-48792bb-746dac3/events/
{
  "operation": "FINISH",
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
In some cases, the asset or TO will send the finish message to the MP (train, metro, ...). In that case, the MP shouldn't pass on the message to the TO of course.

It could be needed to have a 'FINISHING' state, where the asset is ending up the leg. Therefore this operation is also in the API.

## Objects ##
[LegEvent](LegEvent.md)  
[Leg](Leg.md)