# tech module

technical functions of the API, also used in dataspaces

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

</details><h3>GET /capabilities -> <a href="../objects/capabilitiesResponse.md">capabilitiesResponse</a></h3><div style="margin-left:20px"><i>data spaces capabilities check</i><br>data space compliancy

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `date_time` | query | string |  | Date time for which the information is requested. If provided the result becomes final and therefore MUST be cacheable. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [capabilitiesResponse](../objects/capabilitiesResponse.md) | the capabilities of an API, see also https://dev.ishare.eu/ishare-satellite-role/capabilities
</details>
<br></div>
</details>
<h3>POST /connect/token <a href="../objects/accessTokenRequest.md">accessTokenRequest</a> -> <a href="../objects/accessTokenResponse.md">accessTokenResponse</a></h3><div style="margin-left:20px"><i>Request an access token</i><br>request an JWT token to use in a dataspace context

<details><summary><i>Request Body</i></summary>

```json
{
  "grant_type": "string",
  "scope": "string",
  "client_id": "string",
  "client_assertion_type": "string",
  "client_assertion": "string"
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [accessTokenResponse](../objects/accessTokenResponse.md) | in case of a valid request, a accessTokenResponse
</details>
<br></div>
</details>
<h3>GET /health</h3><div style="margin-left:20px"><i>is the API up and running?</i><br>This is a healthcheck ENDPOINT

<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
<h3>POST /oauth/token</h3><div style="margin-left:20px"><i>Token Endpoint</i><br>This endpoint is used to obtain an access token and optionally an ID token through different OAuth 2.0 grant types, including Client Credentials Flow. Whenever the mTLS flow is taken, the properties will be ignored, and the access token will be generated based on the credentials in the certificate (O or CN).

<details><summary><i>Request Body</i></summary>


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
