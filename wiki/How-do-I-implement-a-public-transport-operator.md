[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Modalities](https://github.com/TOMP-WG/TOMP-API/wiki#Per-modality.md) > [Public transport](How-do-I-implement-a-public-transport-operator.md)  

**Q**: How to implement a Public transport operator?<br>
_A_: There are a few specific items to take into account implementing a train TO. Per module:<br>
Planning phase<br>
* you have to use composite-legs when planning overlaps.<br>
* scenario: reserve chairs is not yet implemented
* whenever you have to provide tokens, you probably have to request birthday, name etc. Therefore add the condition require-booking-data-condition: birthday to the response of your planning options.

Booking phase<br>
* In case you can deliver an access token (QR code or other), you can put it into the booking response in 
<pre>
  "token": {
    "startTime": "2020-06-28T14:55:00+02:00",
    "endTime": "2020-06-29T00:00:00+02:00",
    "meta": [
      {
        "QR": "base64 string containing the image"
      }
    ]
  },
</pre> Of course it can be an azztec image.
<br>
<br>
Trip execution<br>
* when you cannot create an access token at the time of booking, it should be retrieved before starting the leg using /executions/{id}/events, requesting a PREPARE. In the response there is 
<pre>
   "assetAccessData": {
      "startTime": "2020-06-28T14:55:00+02:00",
    "endTime": "2020-06-29T00:00:00+02:00",
      "meta": [
        {
          "QR": "base64 string containing the image"
        }
      ]
    },</pre>
In both cases the start and end time are used to specify the time window of validity.
* In case of required birthday etc, the MP must supply the required fields.