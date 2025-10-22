[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Use cases](Use-cases.md) > Use cases Planning & Booking

## PB1
### Description
The end-user has found a specific asset on the street (like a free parking spot, a bike, or shared car) or a route planner has returned all needed information to book an asset (like a tram line, bus, or train seat). This information is enough to book the asset directly.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop`| result.status = CONFIRMED (in case of AUTO_COMMIT) or PENDING (otherwise) |
|[Process identifier](Process-identifier.md)| booking.ONE_STOP ||
|[Process identifier](Process-identifier.md)| booking.AUTO_COMMIT | don't use this one in case you want to provide a 2-phase booking, see [PB3](#pb3) |

**Applies to**
Mostly public transport & free-floating/zone-floating shared mobility providers (e.g. bikes, scooters, cars). But also parking operators. Actually, everything I can book 'here-and-now'.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB2
### Description
As a TO, you want to be able to serve multiple options for a trip request. Like (PT case) serving a first-class or second-class ticket (or even day, week, or month tickets), (shared-car case) different types of cars, with or without insurance, etc.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| provides the bookable options |
|Endpoint| `POST /bookings`| book one of the options,  result.status = CONFIRMED (in case of AUTO_COMMIT) or PENDING (otherwise)  |
|[Process identifier](Process-identifier.md)| booking.NORMAL ||
|[Process identifier](Process-identifier.md)| booking.AUTO_COMMIT | don't use this one in case you want to provide a 2-phase booking, see [PB3](#pb3) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB3
### Description
An MP or reseller often combines multiple legs together to establish one trip. Each part (legs) must be found and booked separately. In case one of the suppliers of the legs offers something, but during the booking process the offer is retracted, it cannot be confirmed. In that case, it might also be needed to roll back the other bookings. Therefore the default TOMP process provides a 2-phase booking. When you're not complying with it (and use 'AUTO_COMMIT'), the MP needs to CANCEL the booking, with possible financial consequences.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/{id}/events` | operation: COMMIT |

**Applies to**  
All TOs that want to integrate into MaaS, whilst keeping fines when cancelling a leg.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB4 
### Description
As a TO I would like to allow canceling a booking in order to release a claimed asset (and optionally refund something).

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/{id}/events` | operation: CANCEL |

**Applies to**  
All TOs that will refund cancelled trips before the trip is started

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB5 
### Description
As a TO I would like to provide a digital ticket, together with the committed booking in order to provide proof (for inspection or entrance/exit) of travel rights. 

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/{id}/events` | operation: COMMIT, provide the digital ticket in legs[0].ticket |

**Applies to**  
PTO

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB6 
### Description
As an MP I would like to be able to communicate that the traveler is less abled in order to request a smooth ride, with assistance if needed.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers` | In the request, the traveler's aspects can be specified, in the `requirements.abilities` (referring to the CROW traveler's dictionary). |

**Applies to**  
PTO, taxi, shared-cars, flight, ...

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB7 
### Description
As an MP I would like to indicate that the traveler brings along personal item(s), like a bike in order to facilitate that the items are transported as well.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers` | In the request, the traveler's aspects can be specified, in the `requirements.bringalong` (referring to the CROW traveler's dictionary). |

**Applies to**  
PTO, taxi, flight

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB8 
### Description
As an MP I would like get a price indication for a personalized leg in order to inform the customer how much it will take to get there.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/inquiry` | This endpoint can be called without any consequences to the caller. It must mainly be fast, which might be more important than 100% accurate. |

**Applies to**  
Every operator using dynamic pricing.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB8A
### Description  
As an MP I would like to inform the TO in my booking request about the precise details of my trip plan (from a trip planner), including leg details and personal “extras” (half-price card, etc.) in order to enable the TO to compute an offer for the given trip plan, including an accurate price matching my personal extras.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offer` | In the offer request the cards can be supplied in the travelers > cardTypes (you don't supply the card numbers, that's something you have to do in the booking request). |
|Endpoint| `POST /bookings` | In the booking request you can supply the required information in the customer object (cards). **Remark** there is a problem until v1.4, you cannot supply cards for accompanying travelers. |


## PB9 
### Description
As a TO I would like to respond to a booking request, although I'm not completely convinced I can guarantee it (the so-called postponed commit scenario) in order to get some time to arrange everything needed to deliver the service.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offer` | returns options |
|Endpoint| `POST /bookings/` | result: the status of the booked option is 'CONDITIONAL_CONFIRMED' |
|[Process identifier](Process-identifier.md)| booking.POSTPONED_COMMIT | to indicate this process flow |

**Applies to**  
Taxi

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB10 
### Description
As a TO I would like to confirm that the booking is confirmed in order to make the customer happy (related to PB9)

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/{id}/events` | operation: COMMIT, `SENT BY THE TO TO THE MP!`, the status of the booking will be 'CONFIRMED' |
|[Process identifier](Process-identifier.md)| booking.POSTPONED_COMMIT | to indicate this process flow |

**Applies to**  
MP that wants to use taxis

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB11 
### Description
As a TO I would like to tell that the booking is NOT confirmed in order to give the MP/reseller time to arrange something else (related to PB9)

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/{id}/events` | operation: DENY, `SENT BY THE TO TO THE MP!`, the status of the booking will be 'RELEASED' |
|[Process identifier](Process-identifier.md)| booking.POSTPONED_COMMIT | to indicate this process flow |

**Applies to**  
MP that wants to use taxis

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB12 
### Description
As a TO I would like to inform that you can book my assets in the future in order to use my services in the right way.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.PLANNING_BASED | 'departureTime' can be 'now', it doesn't require to be in the far future. |

**Applies to**  
Shared cars, trains, buses, bikes, ..

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB13 
### Description
As a TO I would like to inform you that you can find my assets on a map for direct usage (free-floating) in order to use my services in the right way.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.ASSET_BASED | |

**Applies to**  
Bike, scooter operators, street parking

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB14 
### Description
As a TO I would like to inform you that you can find my assets in specific locations (stations, hubs) in order to use my services in the right way.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.LOCATION_BASED | |

**Applies to**  
Station-based operators, trains, buses, (taxis), off-street parking, ..

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB15 
### Description
As a TO I would like instruct that you have to supply an estimated distance you want to travel in order to serve assets with enough fuel, battery power.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.USE_ESTIMATED_DISTANCE | |

**Applies to**  
Shared cars, e-bikes

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB16 
### Description
As a TO I would like to inform you how you can discover the asset's identifying name/id in order to use it directly in the booking process.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.BLUETOOTH_SCAN | using a Bluetooth scan, you can find nearby assets and their IDs. Supply these in the field 'use_assets'.  |
|[Process identifier](Process-identifier.md)| planning.QR_SCAN | The ID of the asset can be found in a QR code on the asset. Supply the QR code content in the field 'use_assets'.|
|[Process identifier](Process-identifier.md)| planning.NFC_SCAN | The ID of the asset can be found using NFC. Supply the NFC content in the field 'use_assets'.|
|[Process identifier](Process-identifier.md)| planning.BARCODE_SCAN | The ID of the asset can be found in the barcode on the asset. Supply the barcode content in the field 'use_assets'.|
|[Process identifier](Process-identifier.md)| planning.MANUAL_ENTRY | The ID of the asset can be found somewhere on the asset, to be entered manually in the app. Supply the entered code in the field 'use_assets'.|
|[Process identifier](Process-identifier.md)| planning.EXACT_ID | The ID of the asset can be found in the data that is supplied for the map (/available-assets). Supply the ID in the field 'use_assets'.|

**Applies to**  
Scooters, bikes, buses, parking

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB17 
### Description
As a TO I would like to get information about the previous leg in order to pick you up at the right location OR give discounts. In case you want to use it for discounts, you still have an agreement between the two organizations about the format.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/one-stop` | in the request there is `previousLegInfo`. |
|Endpoint| `POST /planning/offers` | in the request there is `previousLegInfo`. |

**Applies to**  
Taxi, bus, parking

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB18 
### Description
As a TO I would like to request neglectable time between the offer I serve and the booking request (no user interaction in between) in order to integrate with my existing back end.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.ATOMIC_PLANNING_AND_BOOKING | |

**Applies to**  
Mostly bikes

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB19 
### Description
As a TO I would like to  request the age or other personal aspects in order to give legal ground to the booking.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers` | in the resultset the booking.legs.conditions a requiredBookingData object must be specified **OR** |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_TRAVELER_AGE | when this is specified, this applies to all offers | 
|Endpoint| `POST /bookings/` | in the request 'customer.age' (or other required field) must be supplied | 

**Applies to**  
e.g Age restricted mobility: Car, E-bike, scooter.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB20 
### Description
As a TO I would like to request specific location information (like station or stop references, exact street address, ..) in order to avoid problems at the pickup or drop off locations

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/ ` | In the booking request specific location information with the `bookingRequest.from` and `bookingRequest.to` that contain `place` objects. (`stopReference`, `stationId` or a `physicalAddress`). |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_FROM_STATION_ID | require mandatory from station id. |
| [Process identifier](Process-identifier.md) | planning .MANDATORY_TO_STATION_ID | require mandatory to station id. |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_FROM_STOP_REFERENCE | require mandatory from stop reference (e.g `stopReference`: NL:S:13121110 or stopReference: BE:S:79640040). |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_TO_STOP_REFERENCE | require mandatory to stop reference (e.g `stopReference`: NL:S:13121110 or `stopReference`: BE:S:79640040).
| [Process identifier](Process-identifier.md) | planning.MANDATORY_FROM_ADDRESS | require mandatory from address (e.g a taxi service might want to implement this).
| [Process identifier](Process-identifier.md) | planning.MANDATORY_TO_ADDRESS | require mandatory to address (e.g a taxi service might want to implement this).

**Applies to**  
Station based operators, trains, buses. Taxi.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB21 
### Description
As a TO I would like to  request an arrival time, the departure time is less relevant in order to get the traveler on time on the destination.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers ` | In the planning request give a `arrivalTime`. If only the arrival time is specified, this is an implicit request for a guaranteed arrival at that time. |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_ARRIVAL_TIME | when this is specified this applies to alle offers. |

**Applies to**  
All mobility not operated by the customer.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB22 
### Description
As a TO I would like to  request a first departure time in order to be able to create schedules.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers ` | In the planning request give a `departureTime` |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_DEPARTURE_TIME | when this is specified this applies to alle offers. |

**Applies to**  
All mobility not operated by the customer.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB23 
### Description
As a TO I would like to  request a time window where the complete trip has to be completed in in order to be able to create schedules.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers` | In planning request give a `departureTime` and `arrivalTime`. |
| [Process identifier](Process-identifier.md) | planning.MANDATORY_DEPARTURE_TIME | together with planning.MANDATORY_ARRIVAL_TIME require a time window on all offers.
| [Process identifier](Process-identifier.md) | planning.MANDATORY_ARRIVAL_TIME | together with planning.MANDATORY_DEPARTURE_TIME require a time window on all offers.

**Applies to**  
All mobility not operated by the customer.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB24
### Description
As a TO I would like to tell the MP that assets are opened up directly after booking it in order to reduce actions (see T5).

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| planning.ATOMIC_PLANNING_AND_BOOKING | The final planning and booking should be done without user intervention. |

**Applies to**  
Locked share mobility (e.g shared bike that needs to be unlocked)

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB25
### Description
As a TO I would like to inform where to find the ticket or access information in order to make it possible to inspect it.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| booking.ACCESS_TICKETSTOCK | The digital ticket can be fetched from a ticket stock (like Ximedes) |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_BOOKING | In the result of the booking (preferred if used in combination with the AUTO_COMMIT) |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_COMMIT_EVENT | In the result of the COMMIT-event (preferred for static tickets) |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_PREPARE_EVENT | In the result of the PREPARE-event (sometimes used to deliver the ticket at the gate) |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_ASSIGN_ASSET_EVENT | In the result of the ASSIGN_ASSET-event |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_GET_LEG | In the result of the GET /legs/{id} (preferred for dynamic tickets) |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_IN_GET_BOOKING | In the result of the GET /bookings/{id} |

**Applies to**  
Mainly to public transport, but also used to exchange access information to open a door, or bike.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB26
### Description
As a TO I would like to inform about the format of the tickets/access codes in order to to make it possible to open gates, assets, etc.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_QR | the tokenData contains a `tokenQR` object, with a base64 representation of the QR code |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_PDF | the tokenData contains a `tokenDefault` object, with a URL to the PDF document, containing the ticket |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_DEEPLINK | the tokenData contains a `tokenDeeplink` object, with a base deep URL into the app, and a list of parameters that can be used to extend the URL (like longitude, latitude, userID etc). With this deeplink the external app can be started and can navigate to the appropriate location |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_AZTEC | tokenData contains a 'tokenQR' object, similar to QR |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_AXA_EKEY_OTP | tokenData contains a `tokenEKey` object, for the AXA E-Key locks |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_PHYSICAL_KEY | tokenData contains a `tokenDefault` object, containing the location in plain text |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_BARCODE | tokenData contains a 'tokenQR' object, similar to QR |
|[Process identifier](Process-identifier.md)| booking.ACCESS_CODE_HTML | the tokenData contains a `tokenDefault` object, with a URL to the HTML document, containing the ticket |

**Applies to**  

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB27
### Description
As a TO I would like to  offer a trip with a fixed price in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described using one fixed fare-part [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB28
### Description
As a TO I would like to  offer a trip with a flexible price related to the distance in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described using one flex fare-part. Unit and unit-type (containing km, mile, etc) are mandatory fields [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB29
### Description
As a TO I would like to offer a trip with a flexible price related to the usage time in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described using one flex fare-part. Unit and unit-type (containing hour, minute, etc) are mandatory fields [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB30
### Description
As a TO I would like to offer a trip with a scaled price in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described using multiple fare-parts, for each scale there is a price. Scale-from, to and scale-type are also mandatory in this case. [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB31
### Description
As a TO I would like to offer a trip with a capped price in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described using multiple fare-parts, one of them has the type 'MAX', containing the max price. Can be combined with the scale (e.g. 24 Euro's per day) [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB32
### Description
As a TO I would like to offer a trip with an estimated price in order to sell the leg

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /planning/offers`| In the leg object, the fare is described, and it contains also the 'estimated' field [Fare construction](Fare-construction.md) |

**Applies to**  
All

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB33
### Description
As a customer, I would like to pick a bike without having to first book it in order to use it.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop` | This is actually the normal one-stop booking. The concept 'booking' relates as well to direct sales (being able to use it directly) as to reservation (that, in some cases is called 'booked'). Booking is not the same as reservation in our ontology. A booking can start now, but also in the future. |

**Applies to**  
Bike

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

**TODO**

## PB34
### Description
As a customer, I would like to be able to rent an asset even though I don't know when I want to return it in order to use it.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop` | The concept 'booking' relates as well to direct sales (being able to use it directly) as to reservation. If no arrivalTime is given the time the user intends to stop using the asset (implicit request for arrival guarantee) |

**Applies to**
Shared mobilities

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB35
### Description
As an MP, I want to be able to book parking spaces via TOMP to use it.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `GET /operator/information` | Check if the TO provides parking spaces you can book and read the systeminformation -> productType. If it has parking you can book parking space with this TO through the `POST /bookings` endpoint and the ID the TO provided.|
|Endpoint| `POST /bookings` | Use this API to book the parking space you found with the API above. |

**Applies to**
Parking

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB36
### Description
As a customer, I would like to book a bike in a storage facility (with charging capability) in order to use it.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `/oparator/stations` | Get the station information of the operator. In this case you will be looking for systeminformation -> isChargingStation to be true.|
|Endpoint| `POST /bookings` | Use this API to make a booking for the station that contains a charging station you found in the API above.|

**Applies to**
Electric vehicles

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB37
### Description
As a customer, I would like to return the bike of PB36 to another storage facility in order to finish the trip.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `/legs/{id}/events` | In the legEvent -> asset give a different station than the home station id. |

**Applies to**  
Bike

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB38
### Description
As a customer, I would like to pay for a parking session with a MaaS app in order to make use easier

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop` | In the booking request a valid (and registered) license plate must be supplied |
|[Process identifier](Process-identifier.md)| booking.PICK_UP_THE_BILL | The user payment will be handled by the MP, the MP will pay for the parking session to the TO |

**Applies to**  
Parking

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB39
### Description
As a customer, I would like to redirect the payment to the MaaS provider for the usage of an asset in order to make use easier

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop` | In the booking request a valid customer payment card & asset ID (in the 'useAssets' field) must be supplied |
|[Process identifier](Process-identifier.md)| booking.PICK_UP_THE_BILL | The user payment will be handled by the MP, the MP will pay for the parking session to the TO |

**Applies to**  
All, where external access methods are available to use assets (like bank cards, NFC cards, ..)

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)

## PB40
### Description
As a customer, I would like to travel, although I'm in a wheelchair in order to go from A to B

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /bookings/one-stop` OR `POST /planning/offer` and `POST /bookings/` | In the booking request there must be an indication in the traveller's 'requirements' field, referring to the traveller's dictionary. In this case, HR-01. |

**Applies to**  
All, TOs should take these travel requirements into account.

[back to top](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)