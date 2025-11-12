# after sales module

This part of the API describes how the financial settlement should be done. All kinds of fares, fees, debits, and credits are described.

<details><summary><a>modules</a></summary>  

*  [module overview](../modules.md)  
*  [core](core.md)  
*  [offer](offer.md)  
*  [pre-sales](pre-sales.md)  
*  [purchase](purchase.md)  
*  [execution](execution.md)  
*  [support](support.md)  
*  [after-sales](after-sales.md)  
*  [travel-information](travel-information.md)  
*  [customer management](customer-management.md)  
*  [discovery](discovery.md)  
*  [tech](tech.md)  

</details><h3>GET /collections/payments/items -> <a href="../objects/payments.md">payments</a></h3><div style="margin-left:20px"><i>Retrieve financial details</i><br>Returns all the JOURNAL ENTRIES that should be paid

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `startTime` | query | string (date-time) |  | start of the selection |
| `endTime` | query | string (date-time) |  | end of the selection |
| `invoiceState` | query | string |  |  |
| `package` | query | string |  |  |
| `category` | query | string |  | type of PAYMENT DETAIL (e.g. fare, addition costs, fines, ...) |
| `onBehalveOf` | header | string |  | the identity of the reseller. Only to be used in a PSP (externalized payments) setup. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [payments](../objects/payments.md) | journal entries
</details>
<br></div>
</details>
<h3>GET /collections/redress-options/items?packageId=... -> <a href="../objects/redressOptions.md">redressOptions</a></h3><div style="margin-left:20px"><i>Retrieve redress options for a guarantee</i><br>Returns possible refund or replacement options for a guarantee

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `packageId` | query | string | ✓ | the id of the package that contains a purchased product |
| `offerId` | query | string |  | the offer with a guarantee |
| `legId` | query | string |  | the offer with a guarantee |
| `guaranteeId` | query | string |  | the unfulfilled guarantee |
| `travellerId` | query | string |  | to request redresses for a single traveller |
| `ancillaryId` | query | string |  | to request redresses for a not-used ancillary or ancillary to remove |
| `supportTicket` | query | string |  | reference to support ticket(s) to claim redress options |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [redressOptions](../objects/redressOptions.md) | a list of redress options
</details>
<br></div>
</details>
<h3>POST /processes/cancel-package/execution <a href="../objects/packageRequest.md">packageRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Cancel a package in confirmed state for (technical issues).</i><br>Cancel this package. This endpoint is only there to correct (technical) issues.<br> Normally, after purchase, you have to request redress options, claim it and confirm the claim.<br> <br> Before purchase you release a package.<br> During the purchase you rollback a package.<br>

<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
  }
}
```
Cancellation of a package. Only to use for technical purposes. Normally, use the request of redress options.

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/claim-redress-option/execution <a href="../objects/redressOptionRequest.md">redressOptionRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px">redress options must be claimed & confirmed

<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "75d0dc0b-6dfb-4c27-8799-0052591b918b",
    "guarantee": "Reimburse"
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/confirm-payment/execution <a href="../objects/confirmPaymentRequest.md">confirmPaymentRequest</a></h3><div style="margin-left:20px"><i>Confirm a financial transaction</i><br>The MP (reseller) confirms a payment

<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "paymentId": "string"
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
<h3>POST /processes/confirm-redress-option/execution <a href="../objects/redressOptionRequest.md">redressOptionRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px">confirm the claimed redress option

<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "offer": "4e547ecc-9758-4b62-8083-382f8009a3f2"
  }
}
```
Request to remove an offer from a package (request refund)

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/refund-deposit/execution <a href="../objects/refundDepositRequest.md">refundDepositRequest</a></h3><div style="margin-left:20px"><i>Request to refund a deposit</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "f00680b3-6f72-46de-bf2c-f51331abae6d",
    "leg": "66737d50-6d65-4462-b2ae-1be8827ac3e6"
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
