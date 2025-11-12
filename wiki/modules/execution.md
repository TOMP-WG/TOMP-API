# execution module

This part of the API facilitates changing operational parts of the trip, like starting, stopping legs or initiate new legs from a product. For modifications of the package (travellers, assignment of assets (seats), ancillaries), use the endpoint specified in the pre-sales module.

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

</details><h3>POST /processes/{assetOperation}-asset/execution?assetOperation=... <a href="../objects/assetRequest.md">assetRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an operation on a asset</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `assetOperation` | path | string | ✓ | OPERATION on a specified asset |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "asset": "DKR:CPN:GBFS:ffb6e2f3-b4a5-46b1-9132-39d00b92de69",
    "timestamp": "2024-01-15T10:30:00Z",
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "leg": "caf451c0-a1b9-498f-be8f-aacdae365d07"
  }
}
```
Note: asset is described in the datasource that can be found in /collections/datasources/items, with 
the 'rel' DKR:CPN:GBFS. In the datasource there should be an asset defined with the key 'ffb6e2f3-b4a5-46b1-9132-39d00b92de69' or 'DKR:CPN:GBFS:ffb6e2f3-b4a5-46b1-9132-39d00b92de69'. 

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/{legOperation}-leg/execution?legOperation=... <a href="../objects/legRequest.md">legRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an operation on a leg</i><br>This endpoint must be used to alter the state of a LEG, using OPERATION requests.

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `legOperation` | path | string | ✓ | OPERATION on a specified leg |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "leg": "caf451c0-a1b9-498f-be8f-aacdae365d07",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```
Note: this could be a start or an end request of an leg. Optionally, you can add the location (GPS).

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/{productOperation}-product/execution?productOperation=... <a href="../objects/productRequest.md">productRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an operation on a product</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `productOperation` | path | string | ✓ | OPERATION on a specified product |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "product": "DVC Businesscard",
    "timestamp": "2024-01-15T10:30:00Z",
    "location": "GPS:52.34249,31.43933043"
  }
}
```
Note: this could be an swipe-on operation, to initate a leg.

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
