# purchase module

This part of the API facilitates purchasing offer(s), a package, a product or start the usage of an asset.

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

</details>

[flow](purchase-flow.md)

<h3>GET /collections/travel-documents/items?packageId=... -> <a href="../objects/travelDocuments.md">travelDocuments</a></h3><div style="margin-left:20px"><i>Retrieve travel documents</i><br>Returns travel documents for a package or leg

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `packageId` | query | string | ✓ | the identifier of a package |
| `legId` | query | string |  | leg identifier |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [travelDocuments](../objects/travelDocuments.md) | a response to obtain travel document (references)
</details>
<br></div>
</details>
<h3>POST /processes/confirm-purchase/execution <a href="../objects/packageRequest.md">packageRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Confirm the purchase, before the rollbackExpiryTime has ended</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | A package was succesfully purchased (PURCHASED), or pending (PENDING, to be confirmed using the package operation CONFIRM).
</details>
<br></div>
</details>
<h3>POST /processes/extend-expiry-time/execution <a href="../objects/extendExpiryTimeRequest.md">extendExpiryTimeRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Request additional time to complete the purchase</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "reason": "PURCHASE_PENDING",
  }
}
```
Request additional time due to no response.

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/purchase-offers/execution <a href="../objects/purchaseOfferRequest.md">purchaseOfferRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an purchase of offer(s)</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `digest` | header | string |  | the hash of the body, SHA-256 ("SHA-256=3q2+7w==:") |
| `publicKey` | header | string |  | the public key of the sending party, can be used to validate the signed digest (it should deliver the digest) |
| `signedDigest` | header | string |  | the signed hash of complete response, using the private key, SHA-256 base64 encoded |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
    "inputs": {
      "customer": "EDK:39424",
      "products": [
        "GBFS:Vehicle_types:NormalBike"
      ],
      "travellers": [
        {
          "type": "traveller",
          "id": "Traveller 1",
          "entitlements": [
            {
              "type": "license",
              "modes": [
                "CAR"
              ],
              "licenseCode": "A",
              "issuingCountry": "NL",
              "licenseNumber": "someNumber",
              "endValidity": "tomorrow"
            }
          ],
          "isValidated": true,
          "age": 20,
          "userProfile": "ADULT"
        }
      ]
    }
  }
```

</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | A package was succesfully purchased (PURCHASED), or pending (PENDING, to be confirmed using the package operation CONFIRM).
</details>
<br></div>
</details>
<h3>POST /processes/purchase-package/execution <a href="../objects/packageRequest.md">packageRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an purchase of a package</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `digest` | header | string |  | the hash of the body, SHA-256 ("SHA-256=3q2+7w==:") |
| `publicKey` | header | string |  | the public key of the sending party, can be used to validate the signed digest (it should deliver the digest) |
| `signedDigest` | header | string |  | the signed hash of complete response, using the private key, SHA-256 base64 encoded |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "eb108a85-ff43-4d4e-a6c1-1b3dbd7f2772"
  }
}
```

The package id is referring to the package delivered by the pre-sales module. If you want to
purchase an offer, you have to use the purchase-offers endpoint. This endpoint allows you to
purchase packages, that contain (modified or completed) offers.
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | A package was succesfully purchased (PURCHASED), or pending (PENDING, to be confirmed using the package operation CONFIRM).
</details>
<br></div>
</details>
<h3>POST /processes/purchase-product/execution <a href="../objects/purchaseProductRequest.md">purchaseProductRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Perform an purchase of a product</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "products": [
      "Daycard"
    ],
    "customer": {
      "id": "0495de43-32d2-4668-ac25-7a81563ccce0",
      "initials": "H.",
      "lastName": "Bartels"
    }
  }
}
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | A package was succesfully purchased (PURCHASED), or pending (PENDING, to be confirmed using the package operation CONFIRM).
</details>
<br></div>
</details>
<h3>POST /processes/rollback-purchase/execution <a href="../objects/packageRequest.md">packageRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Rollback a purchase, before the rollbackExpiryTime has ended</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "de329fae-e854-4b92-b599-815c1d888563"
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
<h3>POST /processes/use-asset/execution <a href="../objects/useAssetRequest.md">useAssetRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Request to use an asset</i><br><details><summary><i>Request Body</i></summary>

```json
{
    "inputs": {
      "customer": "EDK:39424",
      "assets": [
        "GBFS:available_vehicles:SharedCar3492"
      ],
      "travellers": [
        {
          "type": "traveller",
          "id": "Traveller 1",
          "licenses": [
            {
              "licenseNumber": "someNumber",
              "endValidity": "31-12-2027",
              "licenseType" {
                "modes": [ "CAR" ],
                "licenseCategory": "DRIVER_LICENSE",
                "licenseCode": "A",
                "issuingCountry": "NL"
              }
            }
          ],
          "isValidated": true,
          "age": 20,
          "userProfile": "ADULT"
        }
      ]
    }
  }
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | A package was succesfully purchased (PURCHASED), or pending (PENDING, to be confirmed using the package operation CONFIRM).
</details>
<br></div>
</details>
