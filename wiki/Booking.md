
# Booking States
In addition, Table 1 describes the transition states that take place during the Booking process. All these states are helpful to understand the steps and actions within the process of making a reservation. The Booking states are also indicated in the operational flow presented in Fig. 6.

|Phase|State||
|---|---|---|
|Planning|Availability check|In the planning phase, an MP can check the real-time **availability of assets** from a TO. In this way, an MP can offer their Users an overview of which assets and options are currently available following the User's request (for a specific mode, a specific location or other User conditions). A time-to-live can optionally be added to the response to show the User how long the information will be valid. Just before presenting the results to the user add `booking-intent = true` to get booking IDs.|
|Booking|Pending|Once the User has narrowed down their selection, the MP can send a booking request to the TO for a specific asset (or asset type) selection, using the id provided in the previous step. This creates a booking with the state **PENDING** and temporarily 'freezes' an asset while the User is finalizing the selection (i.e., while the User is having to choose multiple options for multiple legs of a journey). A time-to-live in the availability confirmation response is mandatory. This phase is also known as 'Prereserving'.|
|	|Released|If a User decides to go for other options than the one(s) narrowed down, the PENDING state can be cancelled by the MP. The Booking State is changed to **RELEASED**. This frees up the asset for other Users.|
|	|Expired|	If the expiry time for the PENDING state is reached (as defined in the time-to-live in the availability confirmation), because the User has not (yet) made a selection, the booking state changes to **EXPIRED** and the corresponding asset(s) are no longer 'frozen' for the specific request and the asset is released for other Users.|
|	|Confirmed|	If a User confirms the selection of a given option, the asset (or asset type) is requested from the MP to the TO and the Booking State changes to either CONFIRMED (in case the “authentication” and payment conditions are met) or to REJECTED (in case the “authentication” and/or “payment” conditions haven’t been met). In case of 'POSTPONED-COMMIT' scenarios the TO cannot confirm immediately and the 'Conditional-confirmed' can be replied instead of 'confirmed'. |
|	|Rejected|The conditions for a booking have not been met and the TO rejects the booking that has been conditional-confirmed state. This is the result of a deny-event.|
|Trip Execution|Started|Once the confirmed asset is in use, the Booking State is changed to **STARTED**.|
|	|Finished|Once the asset is returned, the leg is considered completed and the booking state is changed to **FINISHED**.|
|Additional States|Cancelled|	If the asset confirmation is cancelled by the MP (which could also happen upon request from the User), the Booking State changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply. If the asset confirmation is cancelled by the TO (in case of a broken-down vehicle, late return etc.), the booking state changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply.|
|	|Conditional_Confirmed|Booking state for TOs that cannot immediately confirm a booking (due to e.g. planning issues). The **CONDITIONAL-CONFIRMED** state can be set by the TO to inform that a reservation is not yet completely confirmed. Whenever the subcontractor confirms, the booking state will change to CONFIRMED. The **CONDITIONAL_CONFIRMED** state is also limited by a time-to-postponed-commitment, if the time has expired, the booking state will become EXPIRED.|

_Table 1. Transition states of the Booking process_

# Booking operations

![STD Booking](https://github.com/TOMP-WG/website/blob/master/wiki/images/bookingphase-states.png?raw=true)

The first step in making a booking is for the MP to post a call to the _​/bookings-options_ end point to let the TO's know that he's intending to book this asset for the requested leg.

If the TO requested extra data (using the conditionRequireBookingData), this data should also be included in the posted fields, like the customer data in the example below.

```http
POST https://exampleTO.com/bookings/
{
  "id": "746ac-48792bb-746dac3", ** this is the ID provided in the planning phase **
  "customer": {
    "id": 123456,
    "firstName": "John",
    "lastName": "Doe",
    "phone": "string"
  }
}
```
The example result below is a booking object in the state PENDING:
```
{
  "id": "746ac-48792bb-746dac3",
  "customer": {
    "id": 123456,
    "firstName": "John",
    "lastName": "Doe",
    "phone": "string"
  },
  "state": "PENDING", ** this is a new booking in state pending **
  "terms": "some text",
  "token": {
    "validityDuration": {
      "from": 1546336800,
      "to": 1546336800,
      "meta": []
    }
  },
  "meta": []
}
```
After sending the request to all required TOs - and they all responded with a confirmation, the MP will have to send a POST request with the operation 'COMMIT' in it to change the booking-option into a real booking.

```http
POST https://exampleTO.com/booking/{id}/events/
{
  "operation": "COMMIT"
}
```
The result will be a booking object, in the state COMFIRMED. The web hook in the booking object can be used to communicate from TO to MP about the asset or booked leg.

```
{
  "id": "746ac-48792bb-746dac3",
  "customer": {
    "id": 123456,
    "firstName": "John",
    "lastName": "Doe",
    "phone": "string"
  },
  "state": "CONFIRMED", ** this is a confirmed booking **
  "terms": "some text",
  "token": {
    "validityDuration": {
      "from": 1546336800,
      "to": 1546336800,
      "meta": []
    }
  },
  "meta": []
}
```
In case of assets that will be opened offline, the 'token' should provide the information to open the asset. 

So, the route is booked, and the user can be informed everything is OK. The trip can be made. Look at the next section: trip execution.

In case the user changes her/his mind, the booking can be cancelled by sending a cancel-event to https://exampleTO.com/bookings/{id}/events/. 

## Postponed commit
During the planning phase, the TO can send a 'conditionPostponedCommit'. The MP should keep this in mind as the process flow of these legs is quite different. The returned booked leg is in state 'CONDITIONAL_CONFIRMED' and will later on be committed or denied, using the /booking/{id}/events endpoint, when the conditions for the leg have either been met or are rejected.

![With postponed commit](https://github.com/TOMP-WG/website/blob/master/wiki/images/bookingphase-postponed.png?raw=true)


### Booking module overview 
For reference only
![Operational view of booking module](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki%20_F6_Booking_module.jpg?raw=true)  
_Fig. 6: Operational view of the Booking module_
