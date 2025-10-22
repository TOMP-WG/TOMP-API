[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [process steps](process-steps.md)   

# Process steps  
Since 1.5.0, process steps have been added to describe how you should go through the different phases. Each phase has its own steps, and the order of the steps is important. A reseller (MP) should consider this order when implementing its app.

## Planning
During the planning phase, a TO can request a MP to show some information, attached to their offers. It is indicated with this process step: `RESULT_SHOWN`.

```json
{ "type": "URL", 
  "url": "http://example.to/steps/?plan",
  "goal": "SALES",
  "action": "RESULT_SHOWN"
}
```
 
This URL could contain some advertisements.

## Booking
It is convenient for the end user to inform the status, and explain things, and what's happening during the booking phase. Therefore this booking step construct is provided. You can show a series of steps.  
An example:
```json
[ { "type": "TEXT", "goal": "INSTRUCTIONS", "text": "Waiting for response", "action": "PENDING" },
  { "type": "TEXT", "goal": "INSTRUCTIONS", "text": "Booking is final", "action": "CONFIRMED" },
  { "type": "TEXT", "goal": "INSTRUCTIONS", "text": "You will be notified when everything is ready", "action": "CONDITIONAL_CONFIRMED" },
  { "type": "TEXT", "goal": "INSTRUCTIONS", "text": "The booking wasn't finished in time", "action": "EXPIRED" } ]
```

## On-boarding
Before the leg is actually started, instructions are often required in micromobility. These actions are foreseen right now:  
* `SEND_PREPARE` - indicate the leg is going to start
* `UNLOCK_LOCKER` - manual user action - when done by the TO, it should be triggered by the PREPARE event
* `DISCONNECT_CHARGER` - requested user action 
* `UNLOCK_ASSET` - requested user action, when done by the TO it should be triggered by SET_IN_USE event 
* `START_ASSET` - requested user action 
* `SEND_OPEN_TRUNK` - request TO to open trunk/helmet case remotely
* `UNLOCK_TRUNK` - requested user action  
* `TAKE_HELMET` - requested user action 
* `SEND_SET_IN_USE` - request to start leg
* `SEND_ASSIGN_ASSET` - request to assign the specified asset to the leg
* `LOCK_LOCKER` - requested user action 

## Off-boarding
During the off-boarding process, additional instructions can be needed as well:
* `SEND_START_FINISHING` - the TO needs to be informed the leg is about to finish
* `PARK_ASSIST` - user action to park (stop) using the asset
* `UNLOCK_LOCKER` - user action, when done by the TO, should be triggered by the START_FINISH event
* `CONNECT_CHARGER` - user action
* `LOCK_ASSET` - user action, when done by the TO, should be triggered by the FINISH event
* `SEND_OPEN_TRUNK` - the TO opens the trunk remotely 
* `UNLOCK_TRUNK` - user action 
* `STOW_HELMET` - user action 
* `LOCK_TRUNK` - user action 
* `LOCK_LOCKER` - user action 
* `SEND_FINISH` - the TO wants to be informed about the end of the leg
* `SEND_EVIDENCE_PARKED` - the TO requires parking evidence. Send it using the POST /legs/{id}/events - FINISH endpoint
* `SEND_EVIDENCE_HELMET` - the TO requires evidence of storing the helmet. Send it using the POST /legs/{id}/events - FINISH endpoint
* `SEND_EVIDENCE_CHARGER` - the TO requires evidence of correct charger usage. Send it using the POST /legs/{id}/events - FINISH endpoint

## Pausing the leg
If the traveler(s) want to pause the leg for a while, instruction or sales information can be sent to them, using the onPausingSteps with these actions:
* `SEND_PAUSE` - send leg event PAUSE to inform the TO
* `PARK_ASSIST` - user action, the end user can be informed how and where to park
* `LOCK_ASSET` - user action, when done by the TO, should be triggered by the PAUSE event
* `SEND_OPEN_TRUNK` - request TO to open the trunk remotely
* `UNLOCK_TRUNK` - user action
* `STOW_HELMET` - user action
* `LOCK_TRUNK` - user action

## Resuming the leg
And, when following the happy flow, after a pause, the trip will be resumed. The actions allow the TO to communicate with the traveler(s) before they hit the road again:
* `UNLOCK_ASSET` - user action, when done by the TO, should be triggered by SET_IN_USE event
* `SEND_OPEN_TRUNK` - request TO to open trunk remotely
* `UNLOCK_TRUNK` - user action
* `TAKE_HELMET` - user action
* `LOCK_TRUNK` - user action
* `START_ASSET` - user action
* `SEND_SET_IN_USE` - the TO wants to be informed that the leg is resumed. Optionally triggers the unlock of the vehicle