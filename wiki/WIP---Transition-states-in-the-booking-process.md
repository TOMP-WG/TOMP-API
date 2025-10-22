_Table 3 : Transition states of the booking process_

| Phase    | # |  State             | Description |
|:--------:|:-:|:------------------:|:------------|
| Planning | 1 | Availability check | In the planning phase, a MP can check the real-time **availability of assets** from a TO. In this way, a MP can offer their Users an overview of which assets and options are currently available following the User's request (for a specific mode, a specific location or other User conditions). A time-to-live can optionally be added to the response to show the User how long the information will be valid for. Just before presenting the results to the user add `provideIds = true` to get booking ids. |
| Booking  | 2 |   Pending |   Once the User has narrowed down their selection, the MP can send a booking request to the TO for a specific asset (or asset type) selection, using the ids provided in the previous step. This creates a booking with the state **PENDING** and temporarily 'freezes' an asset while the User is finalizing the selection (i.e., while the User is having to choose multiple options for multiple legs of a journey). A time-to-live in the availability confirmation response is mandatory. |
|          | 3 | Released  |    If a User decides to go for other options than the one(s) narrowed down, the PENDING state can be cancelled by the MP. The Booking State is changed to **RELEASED**. This frees up the asset for other Users. |
|          | 4 | Expired   |    If the expiry time for the PENDING state is reached (as defined in the time-to-live in the availability confirmation), because the User has not (yet) made a selection, the booking state changes to **EXPIRED** and the corresponding asset(s) are no longer 'frozen' for the specific request and the asset is released for other Users. |
|          | 5 & 6 | Confirmed & Rejected | If a User confirms the selection of a given option, the asset (or asset type) is requested from the MP to the TO and the Booking State changes to either **CONFIRMED** (in case the “authentication” and payment conditions are met) or to **REJECTED** (in case the “authentication” and/or “payment” conditions haven’t been met). |
| Trip Execution | 7 | Started | Once the confirmed asset is in use, the Booking State is changed to **STARTED**. |
|                | 8 | Paused  | If a User wants to pause a ride (fe. park a bike) the Booking Stage can be changed to **PAUSED**. |
|                | 9 | Finished | Once the asset is returned, the leg is considered completed and the booking state is changed to **FINISHED**. |
| Exception states | C | Cancelled | If the asset confirmation is cancelled by the MP (which could also happen upon request from the User), the Booking State changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply. If the asset confirmation is cancelled by the TO (in case of a broken-down vehicle, late return etc.), the booking state changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply. |
|  | CC | Conditional-Confirmed (Optional) | Optional booking state for parties acting as a _“broker”_ between TOs and MPs. This state supports a postponed commitment by the broker (which would act as a TO) and originated by its sub-TOs. The **CONDITIONAL-CONFIRMED** state can be set by the TO to inform that a reservation it’s not yet completely confirmed. Whenever the subcontractor confirms, the booking state will change to CONFIRMED. The **CONDITIONAL-CONFIRMED** stated is also limited by a time-to-postponed-commitment, if the time has expired, the booking state will become EXPIRED. |


Planning 
========
Availability check - 1
------------------
> In the planning phase, a MP can check the real-time **availability of assets** from a TO. In this way, a MP can offer their Users an overview of which assets and options are currently available following the User's request (for a specific mode, a specific location or other User conditions). A time-to-live can optionally be added to the response to show the User how long the information will be valid for. Just before presenting the results to the user add `provideIds = true` to get booking ids.

Booking
========
Pending -  2 
-------------------------------------
> Once the User has narrowed down their selection, the MP can send a booking request to the TO for a specific asset (or asset type) selection, using the ids provided in the previous step. 
This creates a booking with the state **PENDING** and temporarily 'freezes' an asset while the User is finalizing the selection (i.e., while the User is having to choose multiple options for multiple legs of a journey). A time-to-live in the availability confirmation response is mandatory.

Released - 3
------------
> If a User decides to go for other options than the one(s) narrowed down, the PENDING state can be cancelled by the MP. The Booking State is changed to **RELEASED**. This frees up the asset for other Users.

Expired - 4
-----------
> If the expiry time for the PENDING state is reached (as defined in the time-to-live in the availability confirmation), because the User has not (yet) made a selection, the booking state changes to **EXPIRED** and the corresponding asset(s) are no longer 'frozen' for the specific request and the asset is released for other Users.

Confirmed & Rejected - 5 & 6
---------------------------
> If a User confirms the selection of a given option, the asset (or asset type) is requested from the MP to the TO and the Booking State changes to either **CONFIRMED** (in case the “authentication” and payment conditions are met) or to **REJECTED** (in case the “authentication” and/or “payment” conditions haven’t been met).

Trip Execution
==============
Started - 7
----------
> Once the confirmed asset is in use, the Booking State is changed to **STARTED**.

Paused- 8
----------
> If a User wants to pause a ride (fe. park a bike) the Booking Stage can be changed to **PAUSED**.

Finished - 9
----------
> Once the asset is returned, the leg is considered completed and the booking state is changed to **FINISHED**.

Exception states
================

Cancelled - C
-------------
> If the asset confirmation is cancelled by the MP (which could also happen upon request from the User), the Booking State changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply. If the asset confirmation is cancelled by the TO (in case of a broken-down vehicle, late return etc.), the booking state changes to **CANCELLED**, and the corresponding terms and conditions for cancellations between TOs and MPs apply.

Conditional-Confirmed - CC (Optional)
-------------------------------------
> Optional booking state for parties acting as a _“broker”_ between TOs and MPs.
This state supports a postponed commitment by the broker (which would act as a TO) and originated by its sub-TOs. The **CONDITIONAL-CONFIRMED** state can be set by the TO to inform that a reservation it’s not yet completely confirmed. Whenever the subcontractor confirms, the booking state will change to CONFIRMED. The **CONDITIONAL-CONFIRMED** stated is also limited by a time-to-postponed-commitment, if the time has expired, the booking state will become EXPIRED.