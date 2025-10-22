[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Asset class](Asset-class.md)  

These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.  
In the future 'HOTEL' and 'MEETING' can be added. 

| Allowed values | Note | 
| --- | --- |
| AIR | | 
| BUS| | 
| TROLLEYBUS| | 
| TRAM| | 
| COACH| | 
| RAIL| | 
| INTERCITYRAIL| | 
| URBANRAIL| | 
| METRO | | 
| WATER | Mainly for ferry | 
| CABLEWAY | | 
| FUNICULAR| | 
| TAXI | | 
| SELFDRIVE | | 
| FOOT | | 
| BICYCLE | | 
| MOTORCYCLE | | 
| CAR | | 
| SHUTTLE | | 
| OTHER | | 
| PARKING | No difference between on-street and off-street | 
| MOPED | | 
| STEP | | 

If you want to specify the modality more accurate, use the field `assetSubClass` in the assetType.
