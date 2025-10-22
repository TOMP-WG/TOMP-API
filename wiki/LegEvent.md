[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [LegEvent](LegEvent.md)

The leg event is an operation on a leg:  
_PREPARE_ the TO can send a message telling the MP that he is preparing the booked leg [To be implemented by the MP] (see (7.2) in the process flow - trip execution). In the result the leg can contain the access information, like deeplinks, QR codes etc.  
_ASSIGN\_ASSET_ can assign an asset to a leg. Can be to assign an asset in case there is still an asset type assigned [Optionally implementable by the MP]. See (4.7) in the process flow - trip execution  
_SET\_IN\_USE_ will activate the leg or resume the leg [TO and MP] (see (4.6) in process flow),  
_TIME\_EXTEND_ will be used to request an extension in time; the end user wants to use the asset longer, the time field contains the new end time,  
_TIME\_POSTPONE_ will be used to request a delay in the departure time, the end user wants to depart later, the time field contains the new departure time,  
_PAUSE_ will pause the leg [TO and MP] (see (4.6) in process flow),  
_START\_FINISHING_ will start the end-of-leg [Optionally implementable by TO and MP],  
_FINISH_ will end this leg (see (4.6) in process flow) [TO and MP]  

| field | required | description |
| --- | --- | --- | 
| time | * | Time of the event (local date), ISO 8601 |
| event | * | The 'event type', see above | 
| comment| | free text, should match Content-Language |
| url | | this field is only used to provide URI's containing proof for leaving the asset behind in an appropriate way, START\_FINISHING or FINISH. |
| asset	| | the asset related to the event. Is optional, only mandatory in case of ASSIGN_ASSET or when one of the process Identifiers starting with `LEG_EVENT_LOCATION_REQUIRED_` is used.  |

```
POST /legs/{id}/events  
{ "time": "2021-04-14T15:54:58.324Z", "event": "PREPARE" }
```
This event could be used to indicate to the TO that the end-user is preparing to start the leg. The result can contain the needed information to open an asset.

__Details__  
See [Process Identifiers](ProcessIdentifiers.md)