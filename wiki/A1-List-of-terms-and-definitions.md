
# A.1 List of terms and definitions

This appendix presents the terms and definitions that served as a reference for the development of the functionalities covered by the TOMP-API.

|TERM|DEFINITION|SOURCE|
| --- | ------- | ---- |
|Availability|The ability of an asset to perform a required function under given conditions at a given instant in time, or over a given time interval, assuming that the required external resources are provided.| Adapted from UNISIG (2016)|
|Booking|The process of making a reservation for space on a means of transport for the movement of people or goods.| Adapted from EC 1305/2014|
|Booking Process|The process involving those steps necessary to make a reservation, possibly including: <br/>- Query of  route <br/> - Select preferred option <br/> - Request reservation <br/>  - Accept terms and conditions (incl. payment) <br/> - Get reservation confirmation| TOMP WG (2019) |
|Booking State|The situation at a particular time during the booking process.	|TOMP WG (2019)|
|	| **Started**: User requested the usage or reservation of an asset(s) or a seat(s). 	|TOMP WG (2019)|
|	| **Pending**: The requested seat(s) or asset(s) is/are temporary reserved for the user. Reservation is pending for payment.|TOMP WG (2019)|	
|	| **Released**: If a User decides to go for other options than the one(s) narrowed down, the PENDING state can be cancelled by the MP. Then the booking state is changed to RELEASED.|TOMP WG (2019)|	
|| **Confirmed**: Reservation has been paid and the seat(s) or vehicle(s) has/have been granted for the user |TOMP WG (2019)|	
|	| **Cancelled**: The reservations have been cancelled by one of the parties involved	|TOMP WG (2019)|
| | **Changed**: If a reservation needs to be changed after it has been CONFIRMED by the User or TO (e.g., a different asset has been assigned, different starting time), the MP will indicate it to the other party and the booking state will change to CHANGED.|TOMP WG (2019)|	
| | **Finished**: Reservation period has ended and the utilization of the asset or seat is no longer valid.|TOMP WG (2019)|	
|(passenger) Journey|	A collection of segments which satisfies transportation of a passenger for a given origin and destination.|IATA (2018)|
|Mass transit|	Large-scale public transportation with high carrying capacities, such as buses, subways, and trains.	|Byars, M., Wei, A., & Handy, S. (2017)|
|Motor vehicle|	A road vehicle propelled by an engine or motor (internal combustion engine, or electric motor, or some combination of the two) and used for the transportation of passengers, property, or freight	||
|Multi-modal travel|	Travel using more than one travel mode.	||
|Multimodal access|	A system that meets the needs of bicyclists, pedestrians, transit users, passenger vehicles, and other motor vehicle users. A system providing multimodal access integrates different transportation modes to allow co-existence and easy switching between modes	|California State Bicycle and Pedestrian Plan in Byars et al. (2017)|
|Multimodal connectivity|The ease with which people can switch between modes on the same trip. For example, pedestrian and bicycling access to transit stops and stations|Byars et. al (2017)|
|OSLO| Open Standards of Linking Organisations, a Flanders' initiative to enhance the exchange and traceability of data. | Blumauer, A. (2012)|
|Passenger vehicle|A motor vehicle with at least four wheels, used for the transport of passengers, and comprising no more than eight seats in addition to the driver's seat.	|Organisation Internationale des Constructeurs d'Automobiles (OICA)|
|Private transportation	|Transport services owned and operated by private entities, such as privately-owned shuttles	|Adapted from Byars, M., Wei, A., & Handy, S. (2017)|
|Public transportation|	Transport services owned and operated by state, regional, or local public agencies.	|
|Rebooking	|A change of reservation and/or other changes which do not require ticket issuance or exchange	|IATA (2018)|
|Reservation	|The allotment in advance of seating or sleeping accommodation for a passenger or of space or weight capacity for baggage, cargo or mail. This term is also applied to hotel, car and other types of travel services.	|IATA (2018)|
|Rideshare|When a driver, or a passenger, shares an open seat(s) in a vehicle with one or more passengers that have similar travel paths and schedules. Traditional forms of ridesharing include carpooling and vanpooling and current use includes sharing space in a ride sourced vehicle.	|Byars et. al (2017)|
|Ride sourcing|	A rideshare service that connects passengers to drivers, typically through a digital application and typically for a fee. Drivers and companies work for-profit and typically offer rides that are not incidental to their own trips.||	
|Shared Mobility|When a transportation mode, such as an automobile or bicycle, is used by more than one person either for moving a person or personal goods. Mode-usage typically occurs at the same time, but may also refer to sequential use, i.e. a leasing a shared bicycle. Although it can reduce miles travelled per person, it may or may not be efficient in terms of the mode used or emissions per person. This includes public transit options, car sharing; personal vehicle sharing (peer-to-peer car-sharing and fractional ownership); car-pooling; van-pooling; ride-splitting, bike-sharing; scooter sharing; shuttle services; micro-transit; ridesharing; e-Hail (taxis); shuttle services; neighbourhood jitneys; ride-sourcing; transportation network companies; ride-hailing; paratransit; and more. It can also include courier network services or flexible goods delivery, which provide for-hire delivery services using an online application or platform (such as a website or smartphone app) to connect couriers using their personal vehicles, bicycles, or scooters with freight (e.g., packages, food), and commercial delivery vehicles providing flexible goods movement.||
|Station|Location or facility where air or surface transportation originates, stops and/or terminates, and where passengers and/or cargo can be taken on or off.||
|Traffic|The vehicles, pedestrians, ships, or planes moving through an area or along a route.	||
|Transport|Take or carry (people or goods) from one place to another by means of a vehicle, aircraft, or ship.	|Oxford Dictionary|
|Transportation	|The action of transporting someone or something or the process of being transported||	
|Transit|Public or private transportation service that moves passengers in mass and usually has fixed routes, stops, and fares. Operates within cities or regions rather than between cities or regions.	|Byars et. al (2017)|
|Travel	|The action of going from one location to the other, from origin to destination. ||	
|Travel mode|	The means by which travel is done. Common travel modes for people include passenger car (driving alone or shared ride), public transit (bus, subway, or train), walking, and bicycling. Common travel modes for freight include land (road, rail, and pipelines), maritime, and air transportation.	||
|Vehicle sharing|	Provides short-term, on-demand access to a transportation mode without sole, direct ownership, thus reducing the overall number of vehicles including automobiles, bicycles, and scooters.||


### References
|Reference| Description|Source |
|---|---|---|
|Blumauer, A (2012) | Linked Open Data: The Essentials – A quick start guide for decision-makers | Retrieved from https://semantic-web.com/2012/01/20/linked-open-data-the-essentials-a-quick-start-guide-for-decision-makers/ | 
|Byars, M., Wei, A., & Handy, S. (2017)	|Sustainable Transportation Terms: A Glossary | Retrieved from https://itspubs.ucdavis.edu/wp-content/themes/ucdavis/pubs/download_pdf.php?id=2759|
|EC 1305/2014|COMMISSION REGULATION (EU) No 1305/2014 – Annex II, Glossary|Retrieved from https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32014R1305&from=EN|
|EC 62/2006|COMMISSION REGULATION (EU) No 1305/2014 – Annex B, Glossary	|Retrieved from https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32006R0062&from=EN|
|IATA (2007)|International Air Transport Association (IATA) — Ticketing Handbook 39th Ed.| Retrieved from https://www.travelready.org/PDF%20Files/IATA%20-%20Ticketing%20Handbook.pdf|
|IATA (2018)|International Air Transport Association (IATA) — Passenger Glossary of Terms|Retrieved from https://www.iata.org/whatwedo/passenger/Documents/IATA-Passenger-Glossary-of-Terms.xlsx|
|OICA|	OICA statistics web page	|Retrieved from http://oica.net/wp-content/uploads/stats-definition1.pdf|
|Oxford Dictionary |	Online	|https://www.lexico.com. Accessed on 30 July 2019|
|TOMP WG|Dutch working group for a Transport Operator to MaaS Provider	|https://www.linkedin.com/company/tomp-wg|
|UNISIG (2016)	|Glossary of Terms and Definitions - SUBSET-023 v.3.3.0	|Retrieved from https://www.era.europa.eu/filebrowser/download/1091982_en |
