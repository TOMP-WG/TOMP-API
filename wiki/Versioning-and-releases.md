# Versioning and releases
Changes in the API are inevitable since we are exploring a new field and knowledge and experience improves. These changes are controlled using milestones and semantic versioning. First, the WG defines functional milestones for the API. The milestones refer to new capabilities of the API at a point in time. The most recent version is TOMP Dragonfly and contains all functional aspects of a MaaS journey, (operator information, planning, booking, travel, payment, support). Milestones have animal names, in alphabetic order. Secondly, for developers and implementors of TOMP, semantic versioning is used. Semantic versioning means that by looking at our version number, you can quickly identify what has changed and how much work goes into changing your own implementation. Table 1 below shows the different TOMP versions and the major updates - (https://github.com/TOMP-WG/TOMP-API/wiki/Changes).

|Version|Release date|API content|
|---|---|---|
|TOMP 0.0.3|November 2018|User stories defined and first description of planning module, based on GBFS|
|TOMP 0.0.7|	January 2019|	Modules for planning and booking added|
|TOMP 0.1.1|	October 2019|	Trip execution added and API was adjusted to a consistent and uniform REST format|
|TOMP 0.1.2|	March 2020|	Added license and first description of payment module|
|TOMP 0.5.0|	May 2020|	All modules for a complete MaaS journey including support and payment|
|TOMP 0.9.0 <br/> (prerelease Dragonfly)| July 2020|	Added simplified object model in planning phase and a self-describing endpoint|
|TOMP 1.0.0 <br/>(Dragonfly)	|September 2020|	Minor changes and feedback from first full implementations|
|TOMP 1.1.0 <br/>(Dragonfly)	|December 2020|	        No breaking changes and added paging|
|TOMP 1.2.0 <br/>(Dragonfly)    |May 2021|Handling Personal information, deeplink processes & non-happy flows|
|TOMP 1.2.1 <br/>(Dragonfly)    |May 2021|Hotfix for a missing discriminator field for tokenData|
|TOMP 1.3.0 <br/>(Dragonfly)    |January 2022|Alignment with GTFS-GOFS / blockchain, added ancillaries, extended regions|
|TOMP 1.4.0 <br/>(Dragonfly)    |December 2022|One-stop booking process, integration with other standards, added context to bookings|

_Table 1. Overview of all TOMP-API releases_
