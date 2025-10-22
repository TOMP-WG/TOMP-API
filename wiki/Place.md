[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Place](Place.md)  

| field | required | description | 
| --- | --- | --- | 
| name | | Human readable name of the place, could match Content-Language |
| stopReference | | Reference to the (PT) stop, mandatory in case of MANDATORY_FROM_STOP_REFERENCE or MANDATORY_TO_STOP_REFERENCE. See [processIdentifiers](processIdentifiers.md) |
| stationId | | reference to /operator/stations, mandatory in case of MANDATORY_FROM_STATION_ID or MANDATORY_TO_STATION_ID. See [processIdentifiers](processIdentifiers.md) |
| coordinates | * | object containing lon/lat information about the exact location |
| physicalAddress | | Address object, mandatory in case of MANDATORY_FROM_ADDRESS or MANDATORY_TO_ADDRESS. See [processIdentifiers](processIdentifiers.md) |
| extraInfo | | Extra object, not standardized. Only to use in a peer-2-peer solution. If you use this field, please create also an issue in github, might be interesting to standardize | 