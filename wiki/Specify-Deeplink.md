[home](https://github.com/TOMP-WG/TOMP-API/wiki)  

The deeplink can be provided in the returned leg. This leg can be returned in the options (from the planning). This is even possible when you only have implemented the plannings endpoint (with booking-intent=false). You can open up your own app with this url and do the complete process of booking & trip execution in your own app.

```
"assetAccessData": {
            "validFrom": "2020-12-01T07:33:59.619Z",
            "validUntil": "2020-12-01T09:33:59.619Z",
            "tokenType": "DEEPLINK",
            "tokenData": {
              "web": “some web URI”,
              “android” : “some other deeplink URI directly into the app (android)”,
              “ios” : “some other deeplink URI directly into the app (ios)”
            }
          }
```

Moments in the process where you can supply the deeplink:  
a) /plannings/?booking-intent=false. This one you should only use if you use the TOMP-API for planning only   
b) /plannings/?booking-intent=true. No known scenario. Ignore this possibility  
c) POST /bookings/. You could supply the deeplink, but the booking isn't yet final. Ignore this possibility  
d) ​/bookings​/{id}​/events with eventtype COMMIT. This one you could use when the booking is ready and the deeplink cannot change anymore. Disadvantage of this one is of course when the booking is cancelled later on, you've supplied the deeplink and have to register this one as an invalid one.  
e) /legs/{id}/events PREPARE. Just before starting the leg, you can force the MP with the Process Identifier 'ACCESS_CODE_IN_PREPARE_EVENT' to request access data at this specific moment in time. Precondition is of course that you have booked a specific asset already in the booking (or using the /legs/{id}/available-assets).   
f) /legs/{id}/events ASSIGN_ASSET. As soon you have assigned a specific asset to the leg, you can also supply the access data.  
g) ​/legs​/{id}. This one can be used anytime, after the leg is started. Disadvantage of this one is that in order to start the leg, the asset should have been opened.... Ignore this possibility.  