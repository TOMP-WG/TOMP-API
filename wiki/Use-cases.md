[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Use cases](Use-cases.md)  

In this page, we will describe use cases and how they **MUST** be implemented, to avoid creating new dialects.

_[Note: Obviously we should try to eliminate the creation of of TOMP (semantic) dialects as much as possible. At the same time we should carefully verify if by standardizing certain scenarios with mandatory flow implementations, we do not exclude too many parties who's business models for some reason do not seem to fit the standard semantics. In a recent WT2 discussion we considered several options:_
_- treating the standardization strictness different for anonymous vs peer-to-peer connections_
_- allow for operator side versioning of customized semantics]_

We will address each module, and in each module, we will enlist the known use cases. Each use case will have a detailed explanation of what to implement.

# Modules
* [Planning & Booking](#Planning--Booking)
* [Trip execution](#trip-execution)
* [Operator Information](#operator-information)
* [Payment](#payment)
* [Support](#support)
* [Technical](#Technical)

# Planning & Booking  
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|[PB1](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb1)|TO|enable external parties to book a specific asset|provide the asset|
|[PB2](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb2)|TO|give multiple trip offers for a single 'leg'|serve the traveler|
|[PB3](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb3)|TO|facilitate 2-phase booking (default, preferred)|let the user (or reseller/MP) combine other legs into a chained trip|
|[PB4](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb4)|TO|allow to cancel a booking|release a claimed asset (and optionally refund something)|
|[PB5](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb5)|TO|provide a digital ticket, together with the committed booking|provide proof (for inspection or entrance/exit) of travel rights|
|[PB6](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb6)|MP|be able to communicate that the traveler is less abled|request a smooth ride, with assistance if needed|
|[PB7](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb7)|MP|indicate that the traveler brings along personal item(s), like a bike|facilitate that the items are transported as well|
|[PB8](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb8)|MP|get a price indication for a personalized leg|inform the customer how much it will take to get there|
|[PB8A](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb8a)|MP|Inform the TO in my booking request about the precise details of my trip plan (from a trip planner), including leg details and personal “extras” (half-price card, etc.)|enable the TO to compute an offer for the given trip plan, including an accurate price matching my personal extras.|
|[PB9](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb9)|TO|react on a booking, although I'm not completely convinced  I can guarantee it (the so-called `postponed commit scenario`)|get some time to arrange everything needed to deliver the service|
|[PB10](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb10)|TO|inform that the booking is confirmed|make the customer happy (related to PB9)|
|[PB11](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb11)|TO|inform that the booking is NOT confirmed|give the MP/reseller time to arrange something else (related to PB9)|
|[PB12](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb12)|TO|inform that you can book my assets in the future|use my services in the right way|
|[PB13](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb13)|TO|inform that you can find my assets on a map for direct usage (free-floating)|use my services in the right way|
|[PB14](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb14)|TO|inform that you can find my assets in specific locations (stations, hubs)|use my services in the right way|
|[PB15](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb15)|TO|instruct that you have to supply an estimated distance you want to travel|serve assets with enough fuel, battery power|
|[PB16](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb16)|TO|inform you how you can discover the asset's identifying name/id|use it directly in the booking process|
|[PB17](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb17)|TO|get information about the previous leg|pick you up at the right location OR to give discounts|
|[PB18](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb18)|TO|request neglectable time between the offer I serve and the booking request (no user interaction in between)|integrate with my existing back end|
|[PB19](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb19)|TO|request the age or other personal aspects|give legal ground to the booking|
|[PB20](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb20)|TO|request specific location information  (like station or stop references, exact street address, ..)|avoid problems at the pick up or drop off locations|
|[PB21](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb21)|TO|request an arrival time, the departure time is less relevant|get the traveler on time on the destination|
|[PB22](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb22)|TO|request a first departure time|be able to create schedules|
|[PB23](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb23)|TO|request a time window where the complete trip has to be completed in|be able to create schedules|
|[PB24](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb24)|TO|tell the MP that assets are opened up directly after booking it|reduce actions (see T5)|
|[PB25](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb25)|TO|inform where to find the ticket or access information|make it possible to inspect it| 
|[PB26](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb26)|TO|inform about the format of the tickets/access codes|to make it possible to open gates, assets, etc.|
|[PB27](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb27)|TO|offer a trip with a fixed price|to sell the leg|
|[PB28](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb28)|TO|offer a trip with a flexible price related to the distance|to sell the leg|
|[PB29](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb29)|TO|offer a trip with a flexible price related to the usage time|to sell the leg|
|[PB30](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb30)|TO|offer a trip with a scaled price|to sell the leg|
|[PB31](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb31)|TO|offer a trip with a capped price|to sell the leg|
|[PB32](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb32)|TO|offer a trip with an estimated price|to sell the leg|
|[PB33](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb33)|Customer|pick a bike without having to first book it|use it|
|[PB34](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb34)|Customer|be able to rent an asset even though I don't know when I want to return it |use it|
|[PB35](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb35)|MP|want to be able to book parking spaces via TOMP|use it|
|[PB36](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb36)|Customer|book a bike in a storage facility (with charging capability)|use it|
|[PB37](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb37)|Customer|return the bike of PB36 to another storage facility|finish it|
|[PB38](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb38)|Customer|to pay a parking session with a MaaS app|make use easier|
|[PB39](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb39)|Customer|to redirect the payment to the MaaS provider for the usage of an asset|make use easier|
|[PB40](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-PB#pb40)|Customer|travel, although I'm in a wheelchair|go from A to B|
|PB41|MP|extend the expiry time of a booking|request more time to handle operations like end-user payment|
|PB42|TO|need the stationId or regionId when planning|have exact location(s) to use in the planning|

# Trip execution
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|[T1](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t1)|MP|open a internet controlled asset|let the traveler us it|
|[T2](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t2)|MP|open a bike with Bluetooth lock|let the traveler us it|
|[T3](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t3)|MP|close an asset without ending the leg|let the user pause|
|[T4](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t4)|MP|close an asset with ending the leg|let the user end the leg|
|[T5](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t5)|MP|open an asset directly after booking|reduce actions|
|[T6](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t6)|TO|indicate that the on-demand asset is heading to the pickup location|inform the user to prepare|
|[T7](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t7)|MP|inform the TO the traveler is delayed|take the delay into account|
|[T8](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t8)|MP|inform the TO the traveler wants to use the asset a bit longer|take this into account (planning?)|
|[T9](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t9)|TO|inform the MP that a specific asset has been assigned to the trip|give the MP the ability to control it|
|[T10](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t10)|TO|inform the MP the progress of the trip|to show it on the end users map|
|[T11](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t11)|TO|ask confirmation of the MP to switch to another asset|alter the leg (financial consequences)|
|[T12](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t12)|TO|add ancillaries to a leg (like a helmet)|to add them to the bill|
|[T13](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t13)|TO|remove ancillaries to a leg|make it possible to change ancillaries (exchanging helmets)|
|[T14](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t14)|MP|indicate that the leg is near to ending|execute end-of-ride actions, like opening a fence|
|[T15](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t15)|MP|fetch a digital ticket at inspection time|make inspection possible|
|[T16](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t16)|TO|inform the end user that the on-demand assets will arrive shortly by phone|perform a good user experience|
|[T17](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t17)|TO|request proof of a correct off-boarding process|have proof of corrrect usage|
|[T18](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t18)|TO|inform the MP of the events during the trip|control the process on TO side (likely taxi/on-demand scenario)|
|[T19](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t19)|TO|give instructions to the end user|instruct how to operate the asset|
|[T20](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-T#t19)|TO|supply sales information to the end user|inform e.g. upcoming reductions|
|T21|TO|give an overview to the end user of registered damage of the asset|check before using the asset (see also S4)|
|T22|TO|specify the steps (onboarding, offboarding, pausing etc) the MP has to take to operate with me|guarantee a seamless travel|
|T23|TO|use another fare when pausing|make the use of the asset more attractive|
|T24|TO|pause the asset, without locking it||
|T25|TO|make the location in the events required|know where my asset is when events occur|
|T26|TO/MP|report e.g. the battery charge during the ride|inform the end-user when to return|

# Operator Information  
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|[O1](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o1)|TO|publish where you can find my assets (stations or free-floating)|make them rentable|
|[O2](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o2)|TO|publish the times when you can use my assets|make them rentable|
|[O3](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o3)|TO|give general information about my operation|provide contact details|
|[O4](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o4)|TO|inform about event|inform end users|
|[O5](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o5)|TO|give policy information, like parking areas or operational areas|instruct the end user|
|[O6](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o6)|TO|give general information about prices|make it possible choose for my assets|
|[O7](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-O#o7)|TO|specify that I'm publishing my information using an external standard, like NeTEx, GBFS, GTFS and so on|inform the outer world (users, planning apps)|

# Payment
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|[P1](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p1)|TO|communicate the payment details to the MP|get paid, with a clear substantiation of the costs|
|[P2](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p2)|MP|request the final costs of a single leg at the end of the trip|report it to the end user|
|[P3](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p3)|TO|be able to claim extra costs related to a leg, like fines or additional usage|report later on, not on the trip end|
|[P4](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p4)|TO|request a deposit up forehand|have a financial backup for the trip|
|[P5](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p5)|TO|request direct payment after finishing the trip|get paid instantly|
|[P6](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-P#p6)|TO|request upfront payment|get paid without risks|
|P7|TO|have my invoice claim (payment details) for a given service registered by the Clearing House (CH) and the due amount paid into my clearing account|get paid ultimately for my services.|
|P8|MP|approve an invoice claim of the TO for a given service (on behalf of one of my customers), resulting in a debit on my clearing account|pay for the service of the TO and pave the way for trip execution.|
|P9|TO|get my credit (balance) in my clearing account transferred daily/weekly onto my bank account|ultimately have my money.|
|P10|MP|transfer money daily/weekly into my clearing account so that the balance does not go below a prescribed minimum|pay for the services on behalf of my customers.|

# Support
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|S1|MP|report a broken asset during usage|inform the TO to contact the end user|
|S2|TO|ask permission to exchange the asset for another one|let the MP agree to make e.g. additional costs|
|S3|MP|request the status of a reported issue|inform the end user|
|S4|End user|report damage at the asset before the leg starts|avoid becoming fined|

# Technical
[back to top](#modules)
|ID| As a | I would like to | In order to |
|--|------|-----------------|-------------|
|[TE1](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-TE#te1)|TO|Describe my implementation|facilitate external parties to use my implementation|
|[TE2](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-TE#te2)|Broker/router/platform|request the addressee in the request ('addresssed-to' field)|deliver the request at the correct TO|
|[TE3](https://github.com/TOMP-WG/TOMP-API/wiki/Use-cases-TE#te3)|TO|inform the outer world that my backend is properly running|facilitate a trustable connection|
