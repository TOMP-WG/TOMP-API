# Plant UML descriptions of known flows
The flows are grouped per modality, so have a look at them before implementing them, which flow suits you best. But when you have a different flow, please contact us: support@tomp-wg.org.

You can click on the scenario names to open a plantuml sequence diagram. You can use https://planttext.com or http://plantuml.com to view it. Visual Studio Code also provides plantuml preview extensions.

# Building blocks
In the first part, we describe all the 'building blocks', per module. After this we zoom in on specific operator types and describe there flows per operator type.
The names in _italics_ are [processIdentifiers](https://github.com/TOMP-WG/TOMP-API/wiki/ProcessIdentifiers). They describe the way the TO wants to be threated ('care labels').

## Operator information
The operator information actually contains no flow. All endpoints here can be called to get data. If you want to operate with all kinds of MPs, you must implement at least these endpoints, /operator/alerts is the only one that can be marked as optional.

This information can also be used by 'lookups'; central locations where MPs can look up information about the TOs.

The sequence diagram can be found here: [operator information](/Planning/default.plantuml).

## Planning
We have a few types of planning:
* [planned-trip](/Planning/planned-trip.plantuml): person(s) who want to travel from A to B on a certain time (departure or arrival): _PLANNING_BASED_. 
* [book-and-go](/Planning/book-and-go.plantuml): person(s) who want to book an asset really nearby and go instantly: _ASSET_BASED_ OR _SPECIFIC_LOCATION_BASED_.
* [book-from-map](/Planning/book-from-map.plantuml): person(s) who want to book an asset in the near future, go there and use it: _ASSET_BASED_ OR _SPECIFIC_LOCATION_BASED_.

## Booking
The booking has only two scenarios:
* [default](/Booking/default.plantuml): the booking is done by the MP, the TO can directly guarantee that the leg can be made: _NORMAL_.
* [postponed-commit](/Booking/postponed-commit.plantuml): the TO **cannot** guarantee directly the leg. There have to be taken some (manual) actions or acknowledgments from third parties (e.g. drivers): _POSTPONED_COMMIT_.

## Trip execution
In the trip execution there are quite a few endpoints. We've described here the flow for a few types of usage (the opening, closing and pausing assets by TO (internet controlled) or by app (bluetooth, etc)).

### Micro mobility - by app
These flows are marked by _LOCK_UNLOCK_APP_, accompanied by any of the other _LOCK_UNLOCK_ process identifiers:
* [opening](/TripExecution/open-asset-by-app.plantuml)
* [closing](/TripExecution/finish-asset-by-app.plantuml)
* [pausing](/TripExecution/pause-asset-by-app.plantuml)

In these scenarios there might be some extra information needed to open / close the lock. This information can be posted to the MP in the booking (_ACCESS_CODE_IN_BOOKING_), in the commit event (_ACCESS_CODE_IN_COMMIT_EVENT_) or in the prepare event (_ACCESS_CODE_IN_PREPARE_EVENT_).

### Micro mobility - internet controlled
These flows are marked by _LOCK_UNLOCK_REMOTELY_:
* [opening](/TripExecution/open-asset-by-TO.plantuml)
* [closing](/TripExecution/finish-asset-by-TO.plantuml)
* [pausing](/TripExecution/pause-asset-by-TO.plantuml)

There are also a few endpoint regarding the progess (reporting) and changing a leg: [progress](/TripExecution/progress.plantuml) and [changes](/TripExecution/change-leg.plantuml).

### TO controlled trip execution (e.g. taxi)
The flow for taxis is a bit different: [TO controlled](/TripExecution/to-controlled.plantuml).

## Support
The support part is pretty straight forward: issues can be reported by the MP and monitored by the MP: [support](/Support/default.plantuml).

## Payment
The payment module facilitates in enlisting the costs of all the executed legs. This can be called by the MP. On the other hand, there are facilities to report extra costs on both sides: [payment](/Payment/default.plantuml).

# Operator type flow files
The flow files per operator type can be constructed the scenario flow files as described above.

## Car rental
* Planning: the Car rental operators might support all planning scenarios, but the book-from-map is not very likely.
* Booking: implementing the NORMAL scenario where possible, but if you have to wait for (external) approval, implement the POSTPONED_COMMIT scenario. Therefore you have to return the postponed commit condition in the planning result.
* Trip execution: if the car itself communicates with the TO directly using the internet about start/stop, the `TO controlled trip execution` must be used. If the car must be controlled by the app, have a look at the `Micro mobility - by app` scenario. Otherwise, look at the `Micro mobility - internet controlled`.
* Support: normal
* Payment: normal

## Bike operator
* Planning: all 3 scenarios are applicable here. In addition the process identifier `ATOMIC_PLANNING_AND_BOOKING` can be used to plan and book in an atomic way: request a planning with useAssets filled with the found asset. If it's available, the booking should be made directly without user interaction.
* Booking: If `ATOMIC_BOOKING_UNLOCKING` is used, the postponed commit scenario cannot be implemented. Right after booking, the bike must be opened. 
* Trip exection: dependent on the `LOCK_UNLOCK` process identifier that has been specified, the trip can be executed (internet controlled, by app). The access codes are already provided in the booking module or can be requested using the PREPARE event.
* Support: normal
* Payment: normal

## Train
* Planning: normally the planned trip is the case, but the other 2 scenarios might be implemented as well.
* Booking: normal, no postponed commit. Add the approrpiate process identifiers like `ACCESS_CODE_QR` or `ACCESS_CODE_PDF`.
* Trip execution: validation of a token / ticket can be done, because it has been provided in the booking module or can be requested using the PREPARE event. In that case, you have to add the `ACCESS_CODE_IN_PREPARE_EVENT` in the <b>booking</b>. In case of opening gates, the `LOCK_UNLOCK_SHOW_ACCESS_CODE` can be used, in combination with e.g. `ACCESS_CODE_QR` (can be aztek) or `ACCESS_CODE_PDF`. The MP app should show the PDF or QR code on screen to open the gate.
* Support: normal
* Payment: normal

## Parking facilities
* Planning: all three scenarios might be valid, but the booking-from-map is not very likely.
* Booking: normal, no postponed commit
* Trip execution: The prepare event can be used to get the access token. The SET_IN_USE must be used to open the entrance gate (open-asset-by-TO). The FINISH event must be used to open the exit gate (close-asset-by-TO).
* Support: normal
* Payment: normal

## Charging facilites
* Planning: all three scenarios might be valid, but the booking-from-map is not very likely.
* Booking: normal, no postponed commit
* Trip execution: The prepare event can be used to get the access token. The SET_IN_USE must be used to start charging (open-asset-by-TO). The FINISH event must be used to stop charging (close-asset-by-TO).
* Support: normal
* Payment: normal
