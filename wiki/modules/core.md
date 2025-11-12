# core module

Core functions, used in multiple modules

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

</details><h3>GET /collections/datasources/items -> <a href="../objects/link.md">link</a></h3><div style="margin-left:20px"><i>Retrieves all (external) datasources, used in requests and responses</i><br>Retrieves all datasources

<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
Used object: [link](../objects/link.md)

```json
[
  {
    "href": "https://example.com",
    "rel": "string",
    "type": "string",
    "method": "POST",
    "description": "string"
  }
]
```


</details>
<br></div>
</details>
<h3>GET /collections/packages/items?packageId=... -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Get package details</i><br>Retrieves package details

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `packageId` | query | string | ✓ | the identifier of a package |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
