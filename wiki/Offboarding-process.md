[home](https://github.com/TOMP-WG/TOMP-API/wiki)  

The offboarding process is facilitated in TOMP-API 1.1.0 and above.  

To request this, the TO should specify the OFF_BOARDING_REQUIRED process identifier in the meta endpoint. The MP must supply at least one URI to a photo. This functionality is only allowed using the FINISH and START_FINISH event types.  
```
{
  "time": "2020-12-01T08:15:05.634Z",
  "event": "FINISH",
  "url": [
    "https://url to available image",
    "another one",
  ],
...
```