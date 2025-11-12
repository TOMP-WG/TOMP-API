# packageStatus

The life-cycle state of the package<br> _OFFERED_ the package is offered (pre-sales) <br> _PENDING_ the purchase of the package is not confirmed (the end user has shown intentions to purchase this offer), must be finalized with the package-confirm operation (purchase)<br> _CONFIRMED_ a purchased package. Both parties agreed to deliver services in return of payment<br> _CANCELLED_ the package is cancelled before it is executed. The agreement will specify whether there is a refund, or under which conditions<br> _ROLLBACK_ the package is purchased, but before the Rollback-Expires timestamp has passed, therefore no financial consequences<br> _EXPIRED_ the MP didn't respond on time, the package offer has been expired<br> _STARTED_ the package is started, the <u>trip execution</u> module is needed now to manage the execution of the package<br> _ENDED_ the package has ended, the trip has been executed<br> _RELEASED_ for internal archiving, the package has not been purchased.<br> _SETTLED_ final exit state, services delivered & financial settlement succeeded.

**Type:** `string`

semantics [{'transmodel': 'CUSTOMER PURCHASE STATUS'}]

---

## Example

```json
"OFFERED"
```