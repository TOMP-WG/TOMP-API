# legStatus

status of a leg<br> _NOT_STARTED_ the leg is not started, initial state<br> _PREPARING_ the _PREPARE_ operation has been received<br> _READY_TO_USE_ the leg is ready to use<br> _IN_USE_ the travellers are on their way<br> _PAUSED_ the asset is paused<br> _ENDING_ the end-leg request is received, the offboarding process has is started<br> _ENDED_ the travellers have arrived at their destination, leg is final<br> _ISSUE_REPORTED_ due to an issue, there is (temporarily) no progress to report, when the issue isn't solved, this is a final state<br> _CANCELLED_ the leg has been cancelled, before execution<br> _ABENDED_ the leg is abnormally ended (e.g. due to an issue)

**Type:** `string`

semantics [{'transmodel': 'none'}]

---

## Example

```json
"NOT_STARTED"
```