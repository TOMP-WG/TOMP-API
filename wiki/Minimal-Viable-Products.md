Each modality requires specific functionality, and these functions relate to the described [use cases](use-cases.md).  

On this page, we will try to describe the relevant use cases per modality, so you can start implementing the TOMP-API with a head start: what is the minimal viable product for a TO, and what's less relevant or even not applicable at all? Using the MoSCoW principle, we describe what use cases you MUST implement (the MVP), what you SHOULD implement (relevant, but not necessary), what you COULD implement (nice to haves) and what you WOULD implement (if you want to have a complete solution).

_But, on the other hand, in a peer-2-peer solution, EVERY ENDPOINT can be used out of context (e.g. only Operator information parts)._

# What do I have to implement on TO side?
As said before, the endpoints to implement are depending on your modality and the [use cases](use-cases.md) you want to support. To help you out, we've enlisted -per module- for each modality the use cases and classified them. To implement a MVP on TO side, you have to implement the MUST use cases at first.

* [Plan & book](#plan--book) Required, unless agreed differently in a peer-2-peer solution
* [Trip execution](#Trip-execution) Required, except when using deeplink solutions or in case of PT with static tickets
* [Operator information](#operator-information) Optional, can be exchanged with other standards
* [Technical](#technical) Required in an ecosystem/dataspace
* [Payment](#payment) Required in an ecosystem/dataspace
* [Support](#support) Optional

## Some examples
How should you read these tables? Go over the modules, look at your modality, and pick the 'MUST' use cases as first as your minimal viable product. Two examples:

### Bus
For instance, if you're a bus operator, you'll find out you can use PB1 (one-stop-booking, providing a static digital ticket). And if that's the only thing you want (you have arranged payment differently), that's the only endpoint you MUST implement in a peer-2-peer solution with a reseller.

If you do have dynamic tickets, you SHOULD add T15 (fetch a digital ticket at inspection time).

Summarized, you have to implement PB1 only in this case. This results in implementing **1 endpoint**: `POST /bookings/one-stop`.

### Free floating bikes
Suppose you already have implemented a GBFS feed for other purposes, and you're going to expose your services into a dataspace. In that case, you MUST implement TE1, SHOULD implement TE3 to connect properly to the dataspace. The planning & booking part can be done by PB1 and PB13. The trip execution can be done by using T1 (icm T5) and T4.  

And because you have to expose your costs (to get the fares), you MUST implement the payment module (P1).

Summarized, you have to implement TE1, PB1 and PB13, T1 and T4. This will end up in these endpoints to implement & configuration in the meta-endpoint:  
* TE1: `POST /operator/meta`
* PB1: `POST /bookings/one-stop` (using GBFS identifiers)
* PB13: add the process identifier planning.ASSET_BASED in the meta-endpoint
* T1: `POST /legs/{id}/events` - SET_IN_USE & add the process identifier planning.LOCK_UNLOCK_REMOTELY in the meta-endpoint
* T4: `POST /legs/{id}/events` - FINISH

## Plan & Book
This module is required unless agreed on in a peer-2-peer solution. If you look at the 'MUST' column, you'll find out that an MVP can be arranged with 2 use cases to implement. This will result in 1, 2, or sometimes 3 endpoints to implement.

|Modality|Must|Should|Could|Would|
|---|---|---|---|---|
|Bike|PB1, PB13 *or* PB14|PB3, PB16|PB4, PB15|PB8|
|Scooter|PB1, PB13 *or* PB14|PB3, PB16|PB, PB154|PB8|
|Taxi|PB1, PB2, PB12|PB3, PB6, PB17|PB4, PB7, PB9, PB10, PB11|PB8|
|Train|PB1, PB2, PB12|PB3, PB5, PB6, PB7, PB17|PB4|PB8|
|Bus|PB1|PB3, PB5, PB6, PB12, PB17|PB4, PB7|PB8|
|Parking|PB1|PB3, PB13, PB17|PB4, PB5|PB8|
|Shared-car|PB1, PB2|PB3|PB4, PB6, PB15|PB7, PB8, PB16|
|On-demand service|PB1|PB3|PB4, PB6|PB7, PB8|

## Trip execution
This module is required, except when using deeplink solutions or in case of PT with static tickets. An MVP must contain one or two use cases, depending on the modality. It will result in one or two endpoints.

|Modality|Must|Should|Could|Would|
|---|---|---|---|---|
|Bike|T1 OR T2, T4|T3, T12, T13, T14, T17, T18, T19|T5, T7, T8, T10, T11, T20|T9|
|Scooter|T1 OR T2, T4|T3, T12, T13, T14, T17, T18, T19|T5, T7, T8, T10, T11, T20|T9|
|Taxi|T18|T6, T7|T10, T12, T13, T16, T20|T9|
|Train||T4, T12, T13, T15|T19, T20||
|Bus||T4, T15|T19, T20||
|Parking|T4|T8, T19|T7, T20|T9|
|Shared-car|T4|T8, T12, T13, T19|T5, T7, T10, T17, T20|T9, T11|
|On-demand service|T18|T4, T6, T7, T12, T13, T16, T19|T5, T10, T17, T20|T9|

## Operator information
This module is required when cooperating in an ecosystem/dataspace, or can be used in a peer-2-peer solution. An MVP on this module, contains at least the `available-assets` endpoint.

* use an external standard (NeTEx, GBFS, ..)  
* OR you implement everything, with this priority:
  * available-assets
  * pricing-plans
  * stations (if you do have stations or hubs)
  * regions
  * information
  * operating-calendar & hours

Possible external standards
|Modality|Standards|
|---|---|
|Bike|GBFS, NeTEx|
|Scooter|GBFS, NeTEx|
|Taxi| GTFS-GOFS? |
|Train| NeTEx, GTFS |
|Bus| NeTEx, GTFS |
|Parking| APDS, SPDP |
|Shared-car| GBFS, GTFS-GOFS, IXSI5 |
|On-demand services| GBFS, GTFS-GOFS, IXSI5 |

## Techical
This one is quite simple and independent of the modality. When acting in an ecosystem/dataspace, you MUST implement the 'meta' endpoint (MVP) and SHOULD implement the 'ping'.

## Payment
Only applicable when cooperating in an ecosystem/data space or when you have agreed on it in a peer-2-peer solution.
* journal-entry: MUST (MVP)
* claim-extra-costs: SHOULD

## Support
Only applicable when cooperating in an ecosystem/data space or when you have agreed on it in a peer-2-peer solution.
* support: MUST (MVP)
* support/{id}/status: SHOULD
