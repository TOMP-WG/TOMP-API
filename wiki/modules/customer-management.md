<span style="display: inline-block; white-space: nowrap;"><a href="../home.md">home</a><details style="display: inline;"><summary><a href="../modules.md">modules</a></summary>
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

</details></span>

# customer management module

the <u>CUSTOMER MANAGEMENT MODULE</u> contains the functionality to explicitly manage the customer account on the TO side .

<h3>POST /collections/customers/items <a href="../objects/customer.md">customer</a> -> <a href="../objects/customerAccount.md">customerAccount</a> -> <a href="../objects/customerAccount.md">customerAccount</a></h3><div style="margin-left:20px"><i>Create a TO CUSTOMER ACCOUNT for the customer</i><br>creates a CUSTOMER ACCOUNT that can be later used for purchase of a trip

<details><summary><i>Request Body</i></summary>

```json
{
  "id": "f84d777c-9260-48cd-b634-b11174caf74a",
  "initials": "H.",
  "firstName": "Hank",
  "lastName": "Wolters"
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [customerAccount](../objects/customerAccount.md) | this IS NOT THE DEFAULT response. Only to return if the customer already existed on the TO side, based on email address, phone number or other supplied details.| 201 | application/json | [customerAccount](../objects/customerAccount.md) | a new customer is created.
</details>
<br></div>
</details>
<h3>DELETE /collections/customers/items/{customerId}</h3><div style="margin-left:20px"><i>Delete the CUSTOMER ACCOUNT from the TO system.</i><br>The timeline of deletion of the customer account depends on the TO processes, it could be instant, weeks or months.

<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
<h3>GET /collections/customers/items/{customerId} -> <a href="../objects/customerAccount.md">customerAccount</a></h3><div style="margin-left:20px"><i>Get the customer account from the TO system</i><br><details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [customerAccount](../objects/customerAccount.md) | Customer Account
</details>
<br></div>
</details>
<h3>PATCH /collections/customers/items/{customerId} -> <a href="../objects/customerAccount.md">customerAccount</a></h3><div style="margin-left:20px"><i>Update the CUSTOMER ACCOUNT on the TO system</i><br>updates the defined fields of the CUSTOMER ACCOUNT.<br>

<details><summary><i>Request Body</i></summary>


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [customerAccount](../objects/customerAccount.md) | Customer Account
</details>
<br></div>
</details>
