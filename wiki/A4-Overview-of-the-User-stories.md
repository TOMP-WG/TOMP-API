
# A.4 – Overview of the User stories used as parameters for the MaaS functionalities applicable to the TOMP-API

To facilitate the definition of parameters and values that are required for full interoperability in MaaS, user stories have been defined from three different perspectives: the User, Transport Operator (TO) and MaaS Provider (MP).  

By using these three perspectives, the chances are increased that all necessary functionalities for MaaS are taken into account. These functionalities can then be related to the necessary interface specifications between the TO and MP. This document does not set up any requirements for the human-machine-interface (HMI) between Users and MPs.


## Definitions within the User Stories

| **Definition** | **Meaning** |
| --- | --- |
| API | Application Programming Interface, using REST-APIs as architectural style |
| User | Customer wanting to make a journey |
| Maas Provider | Provider of travel advice, information, booking and invoicing |
| Transport Operator | Owner of (any) transport assets. This can be a bike-sharing or car-sharing platform, public transport operators, taxi companies, ferry operators etc. |
| Required for MaaS | Yes = mandatory Conditional = mandatory for some operators Optional = mandatory for no operators |
| Existing API description | Shows which API was used as the basis for implementing this user story. Which are mentioned in the A.3 – APIs available on the transportation ecosystem |
| User | Competence = is the user able Conditions = is the user compliant Authentication = confirmation of identity/profile/token |

## Part 1: From a USER perspective

| **Definition** | **Meaning** |
| --- | --- |
| Item | 1.1 |
| Who | As a USER |
| What | I want to depart from STARTLOCATION and arrive at DESTINATION |
| Why | To define from where to where I need mobility services for my trip |
| Required for MaaS | STARTLOCATION = yes, DESTINATION = conditional |
| Existing API description | GBFSMaaS-API |
| Comments | Some transport operators require the asset to be brought back to a specific station or zone. This requires knowledge about the desired destination or trip (single, return, multi-leg). |
| | |
| Item | 1.2 |
| Who | As a USER |
| What | I want to know the PRICING of my trip |
| Why | To determine how expensive my trip will be |
| Required for MaaS | PRICING = yes |
| Existing API description | GBFS |
| Comments ||
| | |
| Item | 1.3 |
| Who | As a USER |
| What | I want to receive a single INVOICE for my entire trip |
| Why | To simplify my cost overview |
| Required for MaaS | INVOICE = yes |
| Existing API description | |
| Comments | |
| | |
| Item | 1.4 |
| Who | As a USER |
| What | I want to give a RATING and see other ratings of a transport operator |
| Why | To leave my feedback or determine if I want to use a certain transport operator |
| Required for MaaS | RATING = optional |
| Existing API description | |
| Comments | |
| | |
| Item | 1.5 |
| Who | As a USER |
| What | I want to be able to REPORT an issue |
| Why | In case the asset I want to use has a problem/damage/issue |
| Required for MaaS | REPORT = yes |
| Existing API-description | |
| Comments | Maybe this doesn't have to be available in an API but needs to be covered by B2B arrangements.<br/> A User wants the MaaS Provider to solve any issues, as this is their travel interface.<br/> A booking should only be made if an asset has no known technical issues, a transport operator should facilitate this. |
| | |
| Item | 1.6 |
| Who | As a USER |
| What | I want to be able to select an asset-based on COMPETENCES of the vehicle |
| Why | To fit with the criteria for my trip |
| Required for MaaS | COMPETENCES = yes |
| Existing API description | GBFS+ |
| Comments | E.g., selection of the number of seats, type of vehicle, range, fuel type etc. |
| | |
| Item | 1.7 |
| Who | As a USER |
| What | I want to receive SUPPORT during my trip |
| Why | In case I want to be guided along with my travel, get additional suggestions or need any kind of support. |
| Required for MaaS | SUPPORT = yes |
| Existing API description ||
| Comments | Added in v0.9 |

&nbsp;

| Proposals for 1.6 |  |
| --- | --- |
| No of passengers   | Propulsion (e.g., hydrogen)    |
| Vehicle class    |  Exclusive yes/no (in case of ridesharing) |
| Brand   | Type of access/key  |
| Type  | Towing hook  |
| Bicycle type (men, women, tandem)  | Steering wheel on left or right  |
| Colour  | Airconditioning  |
| State of charge (%)  |  Cabrio |
| Child's seat   | Allowed to travel abroad   | 
|  Winter tires | Pets allowed  | 
|  Smoking allowed |  Underground parking allowed | 
| Easy accessibility to the location (lift, escalator) | |

## Part 2: From a MaaS Provider perspective

| **Definition** | **Meaning** |
| --- | --- |
| Item | 2.1 |
| Who | As a MAAS PROVIDER |
| What | I want to know which travel means are available around STARTLOCATION which allow reaching DESTINATION |
| Why | To give travel advice to the USER |
| RequiredForMaaS | STARTLOCATION = yes, DESTINATION = conditional |
| Existing API description | GBFS, MaaS-API |
| Comments | The destination is not always relevant, but some assets need to be brought back to their specific station or zone or even if a one way trip is possible, to a specific zone or station at destination location |
| | |
| Item | 2.2 |
| Who | As a MAAS PROVIDER |
| What | I want to know if the trip starts at STARTLOCATION and ends at DESTINATIONOr will end at the STARTLOCATION |
| Why | To define my travel options to the USER |
| Required for MaaS | STARTLOCATION = yes, DESTINATION = conditional |
| Existing API description | GBFS, MaaS-API |
| Comments | Covered by user story 2.1The destination is not always relevant, but some shared bikes need to be brought back to their specific station or zone or even if a one way trip is possible, to a specific zone or station at destination location |
| | |
| Item | 2.3 |
| Who | As a MAAS PROVIDER |
| What | I want to know the ACCEPTABLE DISTANCE for the USER from LOCATION X to STARTLOCATION |
| Why | To define the travel options to the USER |
| Required for MaaS | ACCEPTABLE DISTANCE = optional, LOCATION X = optional |
| Existing API description | GBFS+ |
| Comments | A user can have a preference for the maximum distance he/she wants to walk to reach a bicycle. Proposed standard value = 500 meters|
| | |
| Item | 2.4 |
| Who | As a MAAS PROVIDER |
| What | I want to know the CONDITIONS of a transport operator |
| Why | To define the travel options to the USER |
| Required for MaaS | CONDITIONS = yes (but can be periodical) |
| Existing API description | GBFS, MaaS-API |
| Comments | E.g., business conditions, user conditions for the rental of the asset etc. These can be updated every week or month (t.b.d.), and do not necessarily have to be requested with each query |
| | |
| Item | 2.5 |
| Who | As a MAAS PROVIDER |
| What | I want to be able to place a BOOKING with a TRANSPORT OPERATOR |
| Why | To book an asset beforehand |
| Required for MaaS | BOOKING=conditional |
| Existing API description | MaaS-API |
| Comments | This could also be done without a USER requesting a booking. In this case, the booking risk lies with the MAAS PROVIDER instead of the TRANSPORT OPERATOR. In this case, the TO's own clients might not have access to the assets if the MP books everything in advance.|
| | |
| Item | 2.6 |
| Who | As a MAAS PROVIDER |
| What | I want the USER to be able to OPEN/CLOSE/PAUSE the asset through my interface |
| Why | To make the use of the asset as easy as possible |
| Required for MaaS | OPEN = conditional, CLOSE = conditional, PAUSE = optional |
| Existing API description | GBFS+ |
| Comments | Requires information on the locking systems of operators. Pausing is an optional function to allow different pricing models when the asset is temporarily parked by user |
| | |
| Item | 2.7 |
| Who | As a MAAS PROVIDER |
| What | I want to give my USER on-the-fly USAGE INFORMATION about the asset usage and the booking from the TRANSPORT OPERATOR |
| Why | To avoid having to keep and update all the information myself |
| Required for MaaS | USAGE INFORMATION = conditional |
| Existing API description ||
| Comments | A transport operator could like to send real-time usage instructions (e.g., _'please unlock the bike now using the QR-code'_) to the User through the MaaS-provider interface. |
| | |
| Item | 2.8 |
| Who | As a MAAS PROVIDER |
| What | I want to patch my USER through to the HELPDESK of the TRANSPORT OPERATOR in case of issues |
| Why | To deliver the best support possible |
| Required for MaaS | HELPDESK = yes |
| Existing API description ||
| Comments | A Transport Operator can give specific support about the asset in case of issues. A direct link between User and Transport Operator is required, the MaaS Provider can facilitate this link through their service. As a reference, insurance companies offer similar assistance, where a neutral helpdesk can take on the role of the insurance provider that manages the specific contract of the User. |
| | |
| Item | 2.9 |
| Who | As a MAAS PROVIDER |
| What | I want to be able to CANCEL/MODIFY a transaction or booking |
| Why | To inform the TRANSPORT OPERATOR about any changes |
| Required for MaaS | CANCEL = yes, MODIFY = yes |
| Existing API description | MaaS-API |
| Comments | MaaS providers need to be able to cancel or modify transactions or bookings on behalf of their users. |
| | |
| Item | 2.10 |
| Who | As a MAAS PROVIDER |
| What | I want to know if my USER can share a journey or booking with a USER from another MAAS PROVIDER |
| Why | To efficiently make use of available transportation through carpooling or ridesharing |
| Required for MaaS | No |
| Existing API description ||
| Comments | This allows higher occupancy of available assets through ridesharing and carpooling |
| | |
| Item | 2.11 |
| Who | As a MAAS PROVIDER |
| What | I want to receive information on public transport USERstops and line information |
| Why | To plan an efficient route for my USER and give the necessary SUPPORT along the journey |
| RequiredForMaaS  | No |
| Existing API description ||
| Comments | For planning purposes, e.g., information on kerbs, ramps, lights, displays, line type and transport operator |

## Part 3: From a Transport Operator perspective

| **Definition** | **Meaning** |
| --- | --- |
| Item | 3.1 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to know from when to when (TIME T1 to TIME T2) the USER wants to use my assets |
| Why | To define if this fits my offer of assets |
| Required for MaaS | TIME T1(START TIME/DAY) = conditional, TIME T2(END TIME/DAY) = conditional |
| Existing API description | GBFS, MaaS-API |
| Comments | This is optional, only required in case of usage restrictions of the Transport Operator or to implement the option to book an asset beforehand (long-term). |
| | |
| Item | 3.2 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to know the DESTINATION of the USER |
| Why | To determine if my assets are suitable or available |
| Required for MaaS | DESTINATION = conditional |
| Existing API description | GBFS, MaaS-API |
| Comments | The destination is not always relevant, but some shared bikes need to be brought back to their specific station or zone or even if a one way trip is possible, to a specific zone or station at destination location |
| | |
| Item | 3.3 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to know if the USER has the right USER COMPETENCE |
| Why | To determine if the USER is allowed to use my assets |
| Required for MaaS | USER COMPETENCE = yes |
| Existing API description | Not available/necessary in GBFS, use other MaaS-API specs. |
| Comments | E.g., the user should have a driving license, correct contact details, a membership etc. This could be a liability issue that needs to be covered with insurance providers. |
| | |
| Item | 3.4 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to know if the USER complies with my USER CONDITIONS before starting a trip |
| Why | To determine if the USER is allowed to use my assets |
| Required for MaaS | USER CONDITIONS = yes |
| Existing API description ||
| Comments | E.g., the user is not on a blacklist, registered member |
| | |
| Item | 3.5 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to give a RATING and see other ratings of a USER |
| Why | To leave my feedback about and determine if USER can use my asset |
| Required for MaaS | RATING = optional |
| Existing API description ||
| Comments | A transport operator might want to rate a user or determine if a user is allowed to use an asset-based on their rating |
| | |
| Item | 3.6 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to be able to receive USER AUTHENTICATION |
| Why | To confirm the identity of the USER using my asset |
| Required for MaaS | USER AUTHENTICATION = yes |
| Existing API description | MaaS-API |
| Comments | Authentication provides the transport operator with a confirmation of a user&#39;s identity, profile or token. |
| | |
| Item | 3.7 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to be able to notify the MaaS provider to CONTACT the USER |
| Why | In case of problems, emergencies or other issues |
| Required for MaaS | CONTACT = yes |
| Existing API description ||
| Comments | A transport operator can give specific support about the asset in case of issues.  A direct link between user and transport operator is required, the MaaS Provider can facilitate this link through their service (see also item 2.8). |
| | |
| Item | 3.8 |
| Who | As a TRANSPORT OPERATOR |
| What | I want to be able to CANCEL/MODIFY a transaction or booking |
| Why | To inform the MAAS PROVIDER about any changes |
| RequiredForMaaS  | CANCEL = yes, MODIFY = yes |
| Existing API description | MaaS-API |
| Comments | Transport operators need to be able to cancel or modify transactions or bookings in case an asset is unavailable or delayed. |
