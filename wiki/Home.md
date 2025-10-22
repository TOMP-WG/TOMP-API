# Introduction
Welcome to the TOMP-API WIKI pages. This page contains the information for implementing the TOMP-API. The [Blueprint](Introduction.md) describes in free format the idea of how the TOMP API was set up.  
  
The latest released version is Dragonfly - 1.6.0. The OpenApi (former: swagger) file can be found [here](https://github.com/TOMP-WG/TOMP-API/blob/master/TOMP-API.yaml.md).

### What functionality does the TOMP-API cover? 
Look at our [Use cases](Use-cases.md).  

### Work in progress
We've started with version 2.0.0, and we have described a few guidelines:
* TRANSMODEL compliant ([TRANSMODEL mapping 2.0](TRANSMODEL-mapping-2.0.md))
* Use OGC API as meta-standard ([https://ogcapi.ogc.org/](https://ogcapi.ogc.org/.md))
* Maximize alignment with GBFS, GTFS, NeTEx, SIRI, IXSI5, APDS, OCPI, etc.

<table style="border:none"><tr style="border:none"><td style="border:none;min-width:50%">
<h2>General</h2>
<ul>
<li> [Roadmap](Roadmap.md) - the roadmap items for upcoming period
<li> [Website](https://tomp-wg.org/.md), [Blog](https://tomp-wg.org/?page_id=9.md) and [LinkedIn page](https://www.linkedin.com/company/37216817.md)
</ul>
<h2>Versions</h2>
<ul><li> [Changes per version](Changes.md) - change record
<li> [Semantic versioning](Semantic-versioning-in-the-TOMP-API.md) - the TOMP-API uses semantic versioning. What does this mean?
</ul></td><td valign=top style="border-width:0px">
<h2> Contribution / implementations </h2>
<ul><li> [Contribution](Contribution.md)
<li> [Participants](https://tomp-wg.org/?page_id=186.md) ([short descriptions per organisation](Participants.md))
<li> [Reference implementation](https://github.com/TOMP-WG/TOMP-REF.md) - an example Github project with implementations
<li> [Example implementation](https://tomp.dat.nl.md) - the running environment, just to experiment with a web client as MP. Due to Log4J issues temporarily out of order. 
<li> [Quickstart Operator Information](Quickstart-Operator-Information.md) - A docker-based quick start, the Operator Information can be implemented by only supplying some JSON files.</ul>
</td></tr></table>

# Workflow
The actual workflow of the TOMP-API is simple. The scenario for a __planned trip__: gather information about the known TOs, create the best routes, propose them to the end user, book and go! Payment as dessert.  

If the end user __doesn't want to plan__ ("pick up and go"), the actual activity diagram stays the same, the only thing that changes is that the planning doesn't need to look for availability, but can directly request an offer for an asset, providing the asset it wants to use. This approach is also supported in (version 1.4.0 and above) the 'one-stop-booking' (a.k.a. simplified booking process).

<img align="right" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/planned%20trip%201.4.0.png" width="550">

## Operator information
> Information about the operator. Where does it operate, and what are its opening hours? Most of these endpoints contain static data, except for the available-assets. [more...](Operator-information.md)  

## Planning phase
> The planning phase actually consists of 1 endpoint but has 2 modes: one for the routing (returns options, without registering anything) and one for getting offers (creates offers that can be booked, with a generated id for the complete life cycle). Completely controlled by one query parameter: booking-intent. 
* In version 1.3 this is split into the endpoints 'inquiry' and 'offer'. 
* In version 1.4 the planning phase can be skipped when all booking information is already provided in 'static' information (using Operator Information Module or external data source, like GBFS, NeTEx or like)
[more...](Planning-phase.md) 

## Booking phase
> The booking is a transactional process. The booking scenarios are:
* up to version 1.3: one of the offers of the planning phase is booked (using the generated id). 
* after 1.3.0: the 'one-stop-booking' endpoint can be used as well, if offers are not needed (e.g. 'I want bike no. 18').

After all the TOs have responded positively to the bookings, each TO has to be confirmed by a commit. (Even this can be bypassed using the [process identifiers](ProcessIdentifiers.md)). [more...](Booking-phase.md)  

## Trip execution phase 
### Prepare
> Before a leg can be started, access data can be needed. In this event, the MP requests access information or just informs the TO that the leg is going to start. This can also be used to open lockers. [more...](Trip-execution-phase---prepare.md)  

### Start
> Starting a booked 'leg' is dependent on the type of transport ('modality'). A taxi company will send start information indirectly to the end user, while opening a bike will be initiated by the end user. [more...](Trip-execution-phase---start.md)  

### En route
> While using the asset, there are all kinds of events possible. E.g. the end-user can pause the asset. [more...](Trip-execution-phase---on-route.md)  

### End
> The leg ends, the asset has to be returned, closed, etc. [more...](Trip-execution-phase---end.md)  

## Support
> During the trip execution, incidents or accidents may happen. To handle this kind of situation, the support module is added. [more...](Support.md)

## Payment
> To get an overview of the payments, this module offers an endpoint, but also to report the non-fare-based payments (like fines). [more...](Payment.md)

# Points of attention
## Per modality
* [Bike](How-do-I-implement-a-bike-operator.md) - a generic scenario description for (shared) bike operators
* [Taxi](How-do-I-implement-a-taxi-operator.md) - a generic scenario description for taxi operators 
* [Moped](How-do-I-implement-a-micromobility-operator.md) - a generic scenario description for (shared) micro-mobility operators 
* [Train](How-do-I-implement-a-public-transport-operator.md) - a generic scenario description for PT operators
* [Metro](How-do-I-implement-a-public-transport-operator.md) - a generic scenario description for PT operators
* [Bus](How-do-I-implement-a-public-transport-operator.md) - a generic scenario description for PT operators
* [Parking facility](How-do-I-implement-a-parking-facility-(offstreet).md) - a generic scenario description for Parking facilities
* [Shared car](How-do-I-implement-a-shared-car-operator.md) - a generic scenario description for shared car operators

## Other
* [Process identifiers](ProcessIdentifiers.md) - the 'care labels', describing the specific process requirements of the TO
* [Specifying locations](Specify-pick-up-or-drop-off-locations.md) - how to specify a pick-up or drop-off location
* [GDPR](GDPR-compliant.md) - GDPR aspects
* [Specify Deeplink](Specify-Deeplink.md) - how to use deep links in combination with the TOMP-API
* [Specify access information or inspection information](Specify-access-information-or-inspection-information.md) - how to communicate tickets or access information
* [Offboarding process](Offboarding-process.md) - how to request off-boarding proof
* [Generating code using OpenAPI editor](Generating-code-using-OpenAPI-editor.md) - how to generate code (tips & tricks) 
* [Cooperation with other standards](Cooperation-with-other-standards.md) - like GBFS, GTFS, NeTEx, APDS, ...
