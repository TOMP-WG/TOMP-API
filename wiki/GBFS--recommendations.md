The following additions to GBFS have been proposed by the TOMP-WG to the GBFS community. The acceptance of these suggestions and future phasing is still to be defined. A national **GBFS+** standard can be implemented to speed up developments in the Netherlands.

**1. Deep links, Add rental_url to free bikes and stations**<br>
There is already a change-requests (from others) for an extension of the standard, covering exactly our wishes. So we include request #25 in GBFS+, which enables deep links.

**2. Type_of_system**<br>
We will add type_of_system in the “system info” file. Allowed values are [free_floating, station_based, virtual_station_based]

**3. Type_of_bike**<br>
We add a file “Types_of_bikes” which describes the different bike types (type_id, name, gears, electric, description, img_url). In free-bike-status file we add the field type_of_bike (our first proposal on OpenBikeShare Github)  

**4. TTL**<br>
The time to live (TTL) for real-time data feeds will be at most 30s, so that traveller has always the most actual information about the availability of bicycles.

There are some other topics to cover to make an awesome bike standard in the future, but more research has to be done. Possible topics are:

* Which fields should be compulsory?
* Operation area: For a free-floating system we would like to indicate where you can return your bike (for example you are only allowed to return the bike within the city). In this https://github.com/NABSA/gbfs/issues/65 thread there is already a discussion about this idea.
* Virtual stations: We would like to introduce virtual stations (a virtual location where you allowed to park your bike) within GBFS so operators comparable with Donkey Republic are supported as well. We created a proposal. The exact location of a virtual zone should be presented as GeoJSON polygon in station_information.json.
* Option to define a radius around a bike or bikesharing station for location-specific API-calls.
* Option to OPEN/CLOSE/PAUSE an asset.
