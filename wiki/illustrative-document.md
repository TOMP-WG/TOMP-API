# TOMP API v 0.9.0
## Planning phase – travel now – happy flow

Planning a trip consists out of a few steps, where the MP (MaaS Provider) should support.

The MP should (dependent on their business case) create a route (trip planning) for one or more persons. The MP could use the availability of assets (all kinds of transport) during the planning phase, but it’s not a must. This availability-check could be a heavily used web service, just responding whether the TO has assets to let. The result of the check could be physical assets (for instance a very nice Ferrari) or a asset type (for instance ‘a bike’).

When the trips are constructed, the alternatives should be presented to the user. He/she can choose one. This is the trip that will enter the ‘Booking phase’.

_Example:_

John wants to travel to his sister, just 6km away in an urban area. He just enters the address of his sister.

The MP creates a few routes and looks for TO’s that can serve assets on (parts of) the route (=leg). On every leg the MP checks the availability of assets, requesting also to provide ID’s to refer to in the communication between the TO and MP. 

In our example the MP creates 3 routes, one by bike (there is a bike 120m from his house), one by bike in combination with a metro and one by rented car. He checks the availability and finds out that there are no rented cars available. 

![](https://user-images.githubusercontent.com/10400054/65756732-f3a8ce80-e115-11e9-9a89-8051a03fc682.png)

The 2 routes that are left over, are checked again, but now the TO should add ID’s per served leg/asset combination. After this the routes are presented to John, including prices, travel times etc.
The requests between MP and TO send are listed below:

**MP -> TO1:**
POST /plannings/?booking-intent=false
```
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "requirements": [{"driver-licence-type": "A,B,AM"}]
}
```
Response:
```
{
  "conditions": [ ... ],
  "legOptions": [
    {
      "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
      "radius": 100,
      "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
      "startTime": "2020-06-24T07:12:03.000Z",
      "endTime": "2020-06-24T07:20:03.000Z",
      "assetType": {
        "typeId": "bike",
        "name": "bike",
        "travelAbroad": true,
        "assetClass": "bike",
        "brand": "MyBike",
        "cabrio": false,
        "gears": 3,
        "gearbox": "MANUAL",
        "infantSeat": false,
        "persons": 1,
        "propulsion": "MUSCLE",
        "meta": [
          {
            "rating": "4.5"
          }
        ]
      },
      "pricing": {
        "parts": [
          {
            "amount": 9.96,
            "currencyCode": "EUR",
            "taxRate": 21,
            "type": "FLEX",
            "unitType": "HOUR",
            "units": 1
          }
        ]
      },
      "conditions": []
    }
  ]
}
```
**MP -> TO3:**
POST /plannings/?booking-intent=false
```
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "requirements": [{"driver-licence-type": "A,B,AM"}]
}
```
}

Response:
```
[]
```

Just before showing the available trips to John, the same request is done, except the 'booking-intent' is set to true:

**MP -> TO3:**
POST /plannings/?booking-intent=true
```
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "requirements": [{"driver-licence-type": "A,B,AM"}]
}
```

The response will be the same, except there will be an ID in the response. This ID will be the reference for this leg/asset combination during the complete live time (booking, trip execution, issues, payment, etc.).
```
{
  "conditions": [ ... ],
  "legOptions": [
    {
      "id": "f8a9fda93e90231-38247",
      ...
```
 
## Booking phase – travel now – happy flow
John chooses a route to travel, let’s say the combination: bike and metro. Now we’ve got to reserve both assets. Therefore the MP sends an availability-request to the bike rental and to the metro organization. Both respond positive to the request, the bike rental will put the specific bike in status ‘PENDING’ and the metro organization assumes his assets are unlimited in space (ahum). 

The MP receives both acknowledgements and sends the asset-request (=commit) to both the operators. After acknowledgement of both TO’s, the booking status is ‘CONFIRMED’. The bike rental should reserve the bike, so it cannot be used for anyone else.

![](https://user-images.githubusercontent.com/10400054/65756837-2652c700-e116-11e9-9938-cbb23ab182eb.png)

Now the trip can be made!
 
## Trip execution phase – travel now – happy flow
John leaves his house, walks to the bike and uses the app to open the bike. Let’s say in the acknowledgement of the CONFIRMED information is send to the user which can be used to open the bike (Bluetooth) (in-use-request or in-use-confirmed). 

![](https://user-images.githubusercontent.com/10400054/65756949-6154fa80-e116-11e9-934f-93278b0c87aa.png)

Another option is that the app communicates with the TO, that can open the bike remotely. 
 
![](https://user-images.githubusercontent.com/10400054/65756974-73cf3400-e116-11e9-91aa-84c25151ffbd.png)

Nevertheless, the bike is ready to use. The MP and TO should be signaled so the status of the bike/booking can be changed. 

During his ride John will be informed about his route. Let’s say it’s a sunny day, no traffic problems, no flat tires etc. John arrives at time at the metro station. He lock the bike with the app (finish-request or finish-confirmed, see also below) and steps into the metro. 

The metro will provide him access by using the app. The digital ticket is provided to the app on the during the booking phase.

Finally John arrives at the metro station, just outside his sister’s house. The leg should be finished. This can be done by the check out at the metro station (TO -> MP, finish-confirmed).

![](https://user-images.githubusercontent.com/10400054/65757020-89dcf480-e116-11e9-83b2-fe84cdff94aa.png)
 
For modalities like bikes/cars with Bluetooth the MP should call the finish-request (initiated by the app).

![](https://user-images.githubusercontent.com/10400054/65757045-9b260100-e116-11e9-906d-97803639c134.png)
 
## Trip execution phase
The trip execution phase can be entered in several ways. The most common one is that the traveler is starting to travel by opening an asset (as described in the example of John). Another way is that the asset has to be prepared. There is also an option that there is not yet assigned a specific asset to the trip, the MP or TO assigns an asset and optionally guides the traveler to the assigned asset. 
 
## Travel later (or assets later on in the trip)
Another example: when Marie wants to travel later (e.g. tomorrow) to a business meeting, she will see 3 options: a) a single bus ride, b) a combination of bike, train and bus and c) a single car ride. The latter one is the most expensive on, she hates riding busses, so she chooses option b. The booking process is already described. She sees she has to start travelling at 9:30am, the train will be leaving at 9:50 and will arrive at 10:08 at it’s destination. From there on she can use a bus to travel about 10 minutes to her meeting.

The TO delivering the first bike can of course try to arrange a bike near her starting point at 9:30, as agreed. But let’s say, it’s a densely populated area she’s living in, he is sure he can deliver a bike without explicitly moving a bike in Marie’s surroundings. The MP can look for available assets nearby Marie at, let’s say 9:15am. 

The MSP can assign the nearest bike to the leg, thereby reserving it with the TO. The MSP can calculate the walking distance and time, so the MP warns Marie to start walking to at 9:22. He guides her to the reserved bike. Marie unlocks the bike, travels to the station, locks the bike and starts her second leg in time.

![image](https://user-images.githubusercontent.com/10400054/65757071-abd67700-e116-11e9-9f41-a681e0c36e1c.png)

The train is unfortunately delayed, Marie is going to miss the bus. The MP should look for alternatives. Let’s say, there is an option to take a bus later (15minutes, but she’ll arrive too late) and an option to take a bike. Hey, it’s beautiful weather, let’s take that one! Marie selects the bike option, the original bus leg is cancelled and the process of booking can be executed (request-availability, request-asset).

**Assumptions**

1)	A very important assumption is that – since this is the API initiative between MP and TO – when we’re talking about a ‘booking’ this is a booking for 1 asset for 1 leg. It might be logical that multiple persons can be travelling with one asset. 
2)	The MP is responsible for handling a booking an decomposing it to legs and assets to use.
3)	The TO can help selecting suitable assets, using information provided by the MP (for instance the disability codes, the number of travelers, etcetera).

_Some extra thoughts_

**Planning phase – travel later**

The planning phase is somewhat different when you’ll travel later. The availability is mostly returning asset types instead of specific assets (or you are a TO that rents specific cars). The request should now have at least a start time (or none, if you want to travel on arrival time) or end time (later than now+travel time).

**Booking phase – travel later**

In the booking phase John has to do the same things as he did in the ‘travel now’ scenario. The TO’s and MP also, but the TO should be aware of the fact that he can provide an asset somewhere in the future at a specific place (or area). This means he has a logistic challenge.

**Taxi**

The taxi is an example of one using the prepared phase. The taxi operator starts the trip, riding to the traveler. In this case the booking enters the execution phase in ‘PREPARING’. As soon the traveler is in the taxi, the trip is entering ‘IN_USE’. This can be done by the app or by the taxi driver. 

**Bike**

Bookings for bikes can also have a ‘PREPARING’ state. For instance, when a carrousel is spinning to deliver the requested bike. Bikes can be paused (short visit), but the usage of this should be monitored. Otherwise users can pause the travel and ride on… 

### Attachments
Sequence diagram 1:
App->+MSP: get-alternatives (from, to, start time, end time)
note over MP: do some routing and find suitable TO'state
MSP<->TO1: check-availability
MSP<->TO2: check-availability
MSP<->TO3: check-availability: no assets available
note over MSP: found some suitable trips
MSP<->TO1: check-availability-with-id
MSP<->TO2: check-availability-with-id
MSP->-App: results

Sequence diagram 2:
App->+MSP: selected trip
MSP<->TO1: request-availability (with ack)
MSP<->TO2: request-availability (with ack)
MSP<->TO1: asset-request (with ack)
MSP<->TO2: asset-request (with ack)
MSP->-App: booked!

Title bluetooth opened bike
App<->Bike: open bike
App->+MSP: in-use-confirmed
MSP->+TO: in-use-confirmed
Title remotely opened bike
App->+MSP: in-use-request
MSP->+TO: in-use-request
TO<->Bike: open
TO->MSP: ok, bike open
MSP->App: ok

Title finish TO initiated
TO->MSP: finish-confirmed

Title finish App initiated
App->Bike: lock
App->+MSP: finish-request
MSP->TO: finish-request
MSP->-App: ok

Title Available assets
MSP->+TO: available-assets
TO->-MSP: assets[]
MSP<->TO: reserve
