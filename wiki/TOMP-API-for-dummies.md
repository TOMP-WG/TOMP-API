# Introduction
Welcome to the TOMP-API WIKI pages. This page contains the information for implementing the TOMP-API. The [Blueprint](Introduction.md) describes in free format the idea how the TOMP API was set up.  
  
The latest released version is Dragonfly - 1.0.0. The OpenApi (former: swagger) file can be found [here](https://app.swaggerhub.com/apis/TOMP-API-WG/transport-operator_maas_provider_api/.md).
* [Roadmap](Roadmap.md)
* [Semantic versioning](Semantic-versioning-in-the-TOMP-API.md)
* [Changes per version](Changes.md)
* [Contribution](Contribution.md)
* [Participants](A6-Adoption-and-Implementation-of-the-TOMP-API.md) ([short descriptions per organisation](Participants.md))

# Workflow
The actual workflow of the TOMP-API is simple. The scenario for a __planned trip__: gather information about the known TOs, create best routes, propose them to the end user, book and go! Payment as dessert.  

If the end user __doesn't want to plan__ ("pick up and go"), the actual activity diagram stays the same, the only thing that changes is that the planning doesn't need to look for availability, but can directly request an asset with booking-intent, providing the asset it wants to use.  

<img align="right" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/planned%20trip.png">

## Operator information
> Information about the operator. Where does it operate, what are its opening hours. Most of these endpoints contain static data, except for the available-assets. [more...](Operator-information.md)  

## Planning phase
> The planning phase actually consists out of 1 endpoint, but has 2 modi: one for the routing (returns options, without registrating anything) and one for getting offers (creates offers that can be booked, with a generated id for the complete life cycle). Completely controlled by one query parameter: booking-intent. [more...](Planning-phase.md)  

## Booking phase
> The booking is a transactional process. One of the offers of the planning phase is booked (using the generated id). After all the TOs have responded positively to the bookings, each TO has to be confirmed by a commit. [more...](Booking-phase.md)  

## Trip execution phase 
### Start
> Starting a booked 'leg' is dependant of the type of transport ('modality'). A taxi company will send start information indirectly to the end user, while opening a bike will be initiated by the end user. [more...](Trip-execution-phase---start.md)  

### En route
> While using the asset, there are all kinds of events possible. E.g. the end user can pause the asset. [more...](Trip-execution-phase---on-route.md)  

### End
> The leg ends, the asset has to be returned, closed etc. [more...](Trip-execution-phase---end.md)  

## Support
> During the trip execution, incidents or accidents may happen. To handle these kind of situations, the support module is added. [more...](Support.md)

## Payment
> To get an overview of the payments, this module offers an endpoint, but also to report the non-fare based payments (like fines). [more...](Payment.md)

# Points of attention
## Per modality
* [Bike](How-do-I-implement-a-bike-operator.md)
* [Taxi](How-do-I-implement-a-taxi-operator.md)
* [Moped](How-do-I-implement-a-micromobility-operator.md)
* [Train](How-do-I-implement-a-public-transport-operator.md)
* [Metro](How-do-I-implement-a-public-transport-operator.md)
* [Bus](How-do-I-implement-a-public-transport-operator.md)
* [Parking facility](How-do-I-implement-a-parking-facility-(offstreet).md)

## Other
* [Specifying locations](Specify-pick-up-or-drop-off-locations.md)
* [GDPR](GDPR-compliant.md)

## Eco system relations
* [Discovery service](Discovery-service.md)
* [Clearing house](Clearing-house.md)
* [Personal data store](Personal-data-store.md)
* [Authentication/Authorization](Authentication/Authorization.md)
* [Digital contracts](Digital-contracts.md)