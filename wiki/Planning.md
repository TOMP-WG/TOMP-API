
# Planning

Planning forms the exploration phase of a trip, where options are explored by the User through the MP. The MP has an archive of (semi-)static general information which is periodically retrieved from the TO. Thus, the MP can check real-time availability of assets to give different travel options to the User. Table 2 presents the functions between the MP and TOs within the planning process, which relate to the user stories presented earlier in §4 and to available API calls from similar API specifications.

|Function|User Story; see Appendix A.4 |Reference|
|---|---|---|
|Update static operator information > provide static operator information|1.2; 1.6; 2.1; 2.2; 2.3; 2.4; 3.4|General Information [from GBFS]|
|Check availability of trips > Verify availability and temporarily reserve asset|1.1; 1.2; 2.1; 2.2; 2.3; 3.2|Asset availability and competences [from GBFS and amended]|

_Table 2. Functions between the MaaS Provider and Transport Operator within the planning process_


![Registration and Planning Modules](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki_F5b_planning.jpg?raw=true)  
_Fig. 5b: Operational view of the Registration & Planning modules_


## Calls ##

The planning phase is quite simple with respect to the API: the Transport Operators (TOs) can be asked what assets they have available. This can be done using a request with fields like: from location to location, timestamp to start, timestamp to end, the number of travellers and their (dis)abilities.

The TO should return the available asset types and per asset type the physical assets (if applicable).
Some examples:
- you (TO) have 3 bikes. There is a request for 8 persons in the area you're serving. You can or deliver 3 results (if they are all available) or deliver none. That's up to you.
- you (TO) have an awful lot of cars. There is a request for 5 persons to travel. You can decide to deliver per available car, even if they don't have the capacity to transport 5 persons. You let the MP (MaaS Provider) create the best possible solution for the customer. The only thing you've got to take into account is the (dis)ability list.

The planning comes in 2 flavours: with or without booking intent. If you (MP) are just investigating the options the TO can deliver, use the 'without booking intent' way. When you (MP) have constructed a trip (consisting out of multiple legs), you have to "prereserve" the legs by calling the 'planning with booking intent'. The TO has to respond with a leg they can fulfil (otherwise none), including an ID that can be used throughout the process.

<br/><br/>
### Routing ###
The MP (MaaS Provider) can (optional!) call this endpoint on the TO's side to ask for the available assets during the routing phase:
```http
POST https://exampleTO.com​/plannings/?booking-intent=false
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "travellers": 1,
  "users": [ ... ]
}
```
'Users' contains information about specific travellers:
```
"users": [
    {
      "age": 22,
      "licenses": [
        {
          "cardType": "DRIVING LICENSE",
          "country": "NL",
          "assetType": "B"
        }
      ],
      "cards": [
        {
          "cardType": "NS",
          "country": "NL",
          "assetType": "TRAIN"
        }
      ],
      "requirements": []
    }
```
This information can be used to a) give more accurate prices (age), b) return only the assets that are appropriate for the travellers (license-check or (discount) cards). The requirements can be provided per user.

On the other hand, if a TO requires personal information (like driver license) and it's not provided in the planning call, the TO can put in the result a condition: 'conditionRequireBookingData'. The MP should provide the requested data with the booking, otherwise the TO can reject the booking.

The 'planning-options' call can be made to all known TOs. They should respond very quickly on this request.  
Therefore it's advisable to implement this with simple conditions (like operating area, opening times).  
This is an example response. It says that there is one bike available for the requested leg:
```http
{
  "conditions": [ ... ],
  "legOptions": [
    {
      "startTime": "2020-06-28T14:55:00+02:00",
      "endTime": "2020-06-28T14:25:00+02:00",
      "from": {
        "coordinates": {
          "lng": 6.169639,
          "lat": 52.253279 }
      },
      "to": {
        "coordinates": {
          "lng": 6.169639,
          "lat": 52.253279 }
      },
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
If the TO is offering specific assets, the physical asset should be returned. Or if the startTime (or endTime) is in the near future, in that case it would also be wise to give physical assets directly (if applicable, it's not usual to return scheduled assets like busses or trains).  
In case for an 'upfront planning' the result normally will be containing 'asset types'. The physical asset can be attached (if needed/wanted) later on in the process.
  
#### Conditions
In the response are 'conditions'. These are conditions the TO is requesting. These conditions can like be 'conditionReturnArea', 'conditionPostponedCommit', 'conditionDeposit', ... In the results there can be references to these conditions (so they don't need to be repeated).  
#### Fare
We've chosen to add a Fare construction. Instead of just supplying an exact or estimated amount of money, we supply the 'calculation rules'. This can be a fixed price, but also scaled prices.

### Just before giving options to the end-user ###
After the MP has constructed a route, possibly containing multiple legs, the MP must call the TOs once again to provide id's per option. These IDs can be used to communicate between MP and TO:
```http
POST https://exampleTO.com​/plannings/?bookingIntent=true
{
  "from": { "coordinates": { "lng": 6.169639,"lat": 52.253279} },
  "radius": 100,
  "to": { "coordinates": {"lng": 6.169639,"lat": 52.253279} },
  "startTime": "2020-06-24T07:12:03.000Z",
  "endTime": "2020-06-24T07:20:03.000Z",
  "travellers": 1,
  "users": [ ... ]
}
```
The result will contain id's now:
```http
{
  "legOptions": [
    {
      **"id": "746ac-48792bb-746dac3",** 
      ...
    }
  ]
}
```
The MP can now give the routes to the end-user. The end-user can simply select a route and the MP can book the legs in the route for the end-user, just by booking a provided trip using it's provided id, but that's in the next phase.
