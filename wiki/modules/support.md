# support module

This part of the API facilitates in handling exceptions, like delays, flat tires, accidents or broken equipment reports.

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

</details><h3>GET /collections/support-tickets/items?packageId=...&legId=...</h3><div style="margin-left:20px"><i>Get for support tickets of a package/leg</i><br>returns support tickets in their current state, based on the parameters

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `packageId` | query | string | ✓ | the identifier of a package |
| `legId` | query | string | ✓ | leg identifier |
| `supportTicketStatus` | query | string |  |  |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
<h3>POST /processes/request-support/execution <a href="../objects/supportRequest.md">supportRequest</a> -> <a href="../objects/supportTicket.md">supportTicket</a></h3><div style="margin-left:20px"><i>Create a support ticket</i><br>creates a request for SUPPORT from end user via MP

<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "supportType": "BROKEN_DOWN",
    "type": "supportTicket",
    "location": "GPS:52.3342433,41.4322234",
    "timestamp": "2024-01-15T10:30:00Z",
    "id": "0f52e3c9-b6f3-440c-956f-65da0c1c5710",
    "status": "ISSUE_REQUESTED",
    "context": {
      "asset": "TI:AMS:342",
      "leg": "8f703032-e244-42ee-9342-d3af25dd68b0",
      "package": "7136dae5-cbb9-4b7d-8dc5-52d3faeb7ad2"
    }
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [supportTicket](../objects/supportTicket.md) | support request acknowledged, the response contains a support ticket with a unique ID. Multiple support tickets can be created on one single leg.
</details>
<br></div>
</details>
