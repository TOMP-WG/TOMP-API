
# Trip Execution

The Trip Execution module offers all functionalities for the User during the trip. This includes breakdown into different legs, access to the asset, ending a leg and monitoring a trip. When all legs are concluded, summaries of the specific legs are exchanged to offer the User a complete overview of the executed trip. Table 5 presents the functions between the MPs and TOs within this process, which relate to the User stories presented earlier in §4.

|Function|User Story  (See Appendix A.4)|Reference|
|---|---|---|
|Forward location request > provide location|	1.1; 2.1|Asset availability and competences >  GET /legs/{id}/available-assets|
|Forward access request > grant / reject access 	|2.6; 3.6|PUT /legs/{id}/events - PREPARE and SET_IN_USE|
|Monitor trip <> monitor use of asset|2.7|POST /legs/{id}/progress|
|Forward exit request > grant / reject exit|2.6|PUT /legs/{id}/events - FINISH|
|Generate Trip Summary > Provide Leg Summary|1.3|GET /legs/{id}|
|Manage Review / Feedback <> Review / Feedback with respect to user|1.4; 2.8; 3.5|POST /bookings/{id}/notifications (TO can post this) or GET /payment/journal-entry (not realtime)|
|Trip support (optional)	|2.8; 3.7	|POST /support|

_Table 5. Functions between the MaaS Provider and Transport Operators within the Trip Execution process_

In addition, Table 6 describes the transition states that take place during the Trip Execution process. All these states are helpful to understand the steps and actions within the process of executing a trip. The Trip Execution states are also indicated in the operational flow presented in **Fig. 7.**

Trip Execution states
|#|State|Description|
|---|---|---|
|1|Preparing|	When an asset is not being used yet by the user, but is being prepared (e.g., a taxi is coming towards the user, or a rental car is being cleaned before start of the rental). Also used to request access information.|
|2|In use|The user has started to use the asset. This can be acknowledged or confirmed either by the TO or MP, depending on the type of asset.|
|3|Paused|	If possible, an asset that is in use can be paused in order to apply a lower rate (e.g., when parked). |
|4|Finishing|	When the asset is no longer being used by the user, but the Trip execution is not yet finished (e.g., during verification of damages, cleaning of asset, payment check). At this time the user could have continued with another leg of their trip.|
|5|Finished|The asset has been returned and the trip/leg is confirmed to be finished.|
|U|Issue|An issue has arisen during the trip execution, reported by the user through the MP to the TO.|

_Table 6. Transition states of the Trip Execution process_

![Trip Execution](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki_F7_Trip%20Execution.png?raw=true)  
_Fig. 7: Operational view of the Trip Execution module_
