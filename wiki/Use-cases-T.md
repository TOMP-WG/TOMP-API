# Use cases Trip execution
[Use cases](Use-cases.md) > Use cases Trip execution

## T1
[back to top](#Use-cases-T)
### Description
As an MP I want to request the TO to open an asset, like a bike, so the end user can start using it. Instructions can be shown in advance. (See T16)

**Implementation**  
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: SET_IN_USE|
|[Process Identifier](Process-Identifier.md)| `tripExecution.LOCK_UNLOCK_REMOTELY` | to indicate that it must be opened remotely by the TO |

**Applies to**  
Bike, scooters, shared-cars, PT gates, kick-scooter

## T2 
[back to top](#Use-cases-T)  
### Description
As an MP I would like to open a bike with Bluetooth lock in order to let the traveler us it. Bluetooth operations are nowadays done using SDK or external app solutions.

**Implementation**  
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: SET_IN_USE|
|[Process Identifier](Process-Identifier.md)| `tripExecution.LOCK_UNLOCK_APP` | to indicate that it must be opened by an app |
|[Process Identifier](Process-Identifier.md)| `tripExecution.LOCK_UNLOCK_BLUETOOTH` | in case the Bluetooth operations are known by the MP |
|[Process Identifier](Process-Identifier.md)| `tripExecution.LOCK_UNLOCK_OWN_SDK` | requires that the MP app has the SDK incorporated |
|[Process Identifier](Process-Identifier.md)| `tripExecution.LOCK_UNLOCK_DEEPLINK` | requires that the end user installs (automatically) the app of the TO to unlock/lock the asset |

**Applies to**  
Bike, scooter, shared-car, kick-scooter

## T3 
[back to top](#Use-cases-T)  
### Description
As an end user I want close an asset without ending the leg, I want to pause it for a while.

**Implementation**  
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: PAUSE|

**Applies to**  
Bike, scooter, shared-car, kick-scooter

## T4 
[back to top](#Use-cases-T)  
### Description
As an end user I want close an asset and end the leg. I don't want to use it anymore.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: FINISH|

**Applies to**
Bike, scooter, shared-car, kick-scooter

## T5 
[back to top](#Use-cases-T)  
### Description
As an MP I want to open an asset directly after booking. It depends on the TO's implementation how to cope with this.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process Identifier](Process-Identifier.md)| `booking.ATOMIC_BOOKING_UNLOCKING` | request from TO side to do the POST bookings & POST /legs/{id}/events - SET_IN_USE in one atomic process, depricated |
|[Process Identifier](Process-Identifier.md)| `booking.ATOMIC_BOOKING_SET_IN_USE` | same as ATOMIC_BOOKING_UNLOCKING, preferred |
|Endpoint| POST /legs/{id}/events | Operation: SET_IN_USE, required unless using 'tripExecution.AUTO_UNLOCK' |
|[Process Identifier](Process-Identifier.md)| `tripExecution.AUTO_UNLOCK` | TO unlocks the asset after the booking is completed |

**Applies to**  
Bike, scooter, shared-car, kick-scooter

## T6 
[back to top](#Use-cases-T)  
### Description
As a taxi operator, I want to inform the end user (delegated to the MP) that the taxi is heading towards the pick up location. 

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: SET_IN_USE, !note! This is from the TO towards the MP side|

**Applies to**  
Taxi, on-demand

## T7 
[back to top](#Use-cases-T)  
### Description
As an end user I want to inform the TO I'm late.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: TIME_POSTPONE |

**Applies to**  
All modalities

## T8 
[back to top](#Use-cases-T)  
### Description
As an end user I want to ask the TO to extend my requested usage time.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: TIME_EXTEND |

**Applies to**  
All 

## T9 
[back to top](#Use-cases-T)  
### Description
As a TO I want to inform the MP that a specific asset has been assigned to the trip. So the ID can be used for instance to open the specific bike. Typically used when offered & booked in advance, and an asset type is booked, not a specific asset.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: ASSIGN_ASSET |

**Applies to**  
Bike, scooter, shared-car, kick-scooter

## T10 
[back to top](#Use-cases-T)  
### Description
As a TO I want to inform the MP the progress of the trip, to show it on the end user's map.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint|POST or GET /legs/{id}/progress| |

**Applies to**  
All

## T11 
[back to top](#Use-cases-T)  
### Description
As a TO I want to ask confirmation of the MP to switch to another asset, in order to alter the leg, with possible financial consequences.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint|POST /legs/{id}/confirmation| |

**Applies to**  
All

## T12 
[back to top](#Use-cases-T)  
### Description
As a TO I want to add ancillaries to a leg (like a helmet).

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/ancillaries/{category}/{number} | the category & number are referring to the [traveler's dictionary](https://github.com/TOMP-WG/TOMP-API/blob/master/documents/CROW%20passenger%20characteristics%20V2.0.xlsx)

**Applies to**  
Bikes, scooters, kick-scooters

## T13 
[back to top](#Use-cases-T)  
### Description
As a TO I want to remove ancillaries to a leg in order to make it possible to change ancillaries (exchanging helmets)

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| DELETE /legs/{id}/ancillaries/{category}/{number} | the category & number are referring to the [traveler's dictionary](https://github.com/TOMP-WG/TOMP-API/blob/master/documents/CROW%20passenger%20characteristics%20V2.0.xlsx)|

**Applies to**   
Bikes, scooters, kick-scooters

## T14 
[back to top](#Use-cases-T)  
### Description
As an MP I want to communicate to the TO that a leg is ending, in order to execute end-of-ride actions, like opening a fence / charging pole
**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| POST /legs/{id}/events | Operation: START_FINISHING |

**Applies to**  
All

## T15 
[back to top](#Use-cases-T)  
### Description
As an MP I want to fetch a digital ticket at inspection time.
**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_BOOKING`||
|Endpoint| POST /bookings/ | `booking.ACCESS_CODE_IN_BOOKING`: already supplied in the resulting booking, not preferred |
|||
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_COMMIT_EVENT`||
|Endpoint| POST /bookings/{id}/events - COMMIT | `booking.ACCESS_CODE_IN_COMMIT_EVENT`: already supplieding in the result booking, preferred in case of a static digital ticket |
|||
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_PREPARE_EVENT`||
|Endpoint| POST /legs/{id}/events - PREPARE | `booking.ACCESS_CODE_IN_PREPARE_EVENT`: already supplied in the result booking, not preferred |
|||
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_ASSIGN_ASSET_EVENT`||
|Endpoint| POST /legs/{id}/events - ASSIGN_ASSET | `booking.ACCESS_CODE_IN_ASSIGN_ASSET_EVENT`: already supplied in the result booking, not preferred |
|||
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_GET_LEG`||
|Endpoint| GET /legs/{id} | Can be used to provide dynamic tickets |
|||
|[Process identifier](Process-identifier.md)|`booking.ACCESS_CODE_IN_GET_BOOKING`||
|Endpoint| GET /bookings/{id} | not preferred, you still have to look up the leg |

**Applies to**
Public transport

## TODO ##

## T16 
[back to top](#Use-cases-T)  
### Description
As a TO I want to inform the end user that the on-demand assets will arrive shortly by phone

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md) | `SUPPLIES_CALL_SERVICE`| used in combination with requiredBookingData - phone_numbers |

**Applies to**
