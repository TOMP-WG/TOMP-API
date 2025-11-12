# pre sales module

Module that can be used 'pre-sales'; in the pre-purchase state. Calling one of these endpoints, will put the package in a pre-purchased state (might reserve resources). The package must be released (when the intention of purchasing it is removed) or it expires. The result of each of these endpoints (except for the release) must contain an expiry date in the header.

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

</details><h3>GET /collections/ancillaries/items?packageId=...&legId=... -> <a href="../objects/ancillaryCollection.md">ancillaryCollection</a></h3><div style="margin-left:20px"><i>Request available ancillaries for a leg</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `bbox` | query | array |  | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional)  If the value consists of four numbers, the coordinate reference system is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  If the value consists of six numbers, the coordinate reference system is WGS 84 longitude/latitude/ellipsoidal height (http://www.opengis.net/def/crs/OGC/0/CRS84h) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  The query parameter `bbox-crs` is specified in OGC API - Features - Part 2: Coordinate Reference Systems by Reference.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. |
| `packageId` | query | string | ✓ | the identifier of a package |
| `legId` | query | string | ✓ | leg identifier |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [ancillaryCollection](../objects/ancillaryCollection.md) | a list of ancillaries
</details>
<br></div>
</details>
<h3>GET /collections/assets/items?packageId=...&legId=... -> <a href="../objects/assetCollection.md">assetCollection</a></h3><div style="margin-left:20px"><i>Request available assets for a leg</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `bbox` | query | array |  | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional)  If the value consists of four numbers, the coordinate reference system is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  If the value consists of six numbers, the coordinate reference system is WGS 84 longitude/latitude/ellipsoidal height (http://www.opengis.net/def/crs/OGC/0/CRS84h) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  The query parameter `bbox-crs` is specified in OGC API - Features - Part 2: Coordinate Reference Systems by Reference.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. |
| `packageId` | query | string | ✓ | the identifier of a package |
| `legId` | query | string | ✓ | leg identifier |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [assetCollection](../objects/assetCollection.md) | a list of assets
</details>
<br></div>
</details>
<h3>POST /processes/assign-ancillary/execution <a href="../objects/assignAncillaryRequest.md">assignAncillaryRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Assign an ancillary to a package (and a leg). It could also replace another ancillary or remove one</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "ancillary": "Free coffee"
  }
}
```
This example adds an ancillary (product) to a package. It is also possible to refer to a leg. The referenced ancillary should be findable in /collections/ancillaries/items (no prefix) OR in /collections/datasources/items, where you have to look for the 'rel' that contains the prefix.   

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "leg": "caf451c0-a1b9-498f-be8f-aacdae365d07",
    "ancillary": "DKR:Medium helmet",
    "replacesAncillary": "DKR:Small helmet"
  }
}
```
This example shows how a medium helmet can be replaced with a small one.
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/assign-asset/execution <a href="../objects/assignAssetRequest.md">assignAssetRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Assign an asset to a package (and a leg). It could also replace another asset or remove one</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "leg": "caf451c0-a1b9-498f-be8f-aacdae365d07",
    "asset": "DKR:GBFS_Vehicles:AMS-3w2ui"
  }
}
```
Assign a bike to a leg, the asset should be findable in /collections/assets/items (without prefix) or in /collections/datasources/items with the 'rel' equal to the prefix.

```json
{
  "inputs": {
    "package": "b0b7316d-6587-476e-bd12-ea946bd52ca7",
    "leg": "caf451c0-a1b9-498f-be8f-aacdae365d07",
    "asset": null,
    "replacesAsset": "DKR:GBFS_Vehicles:AMS-3w2ui"
  }
}
```
Remove a bike from a leg.
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/release-package/execution <a href="../objects/packageRequest.md">packageRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Release the complete package</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "769d940a-a457-41d1-ae13-814fbbbf04be"
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
<h3>POST /processes/remove-offer/execution <a href="../objects/removeOfferRequest.md">removeOfferRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Remove an offer from the package</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "45ca7f0c-dbaf-4ad1-9fae-ab9ad6db558b",
    "offer": "09d47a2e-da7e-46ce-bbe7-c31d5574b085"
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
<h3>POST /processes/select-offers/execution <a href="../objects/selectOffersRequest.md">selectOffersRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Select offer(s) into a package</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "offers": [
      "f890aadb-9490-4003-b1b6-87b15284a112",
      "6185460f-3f6b-4fdf-bbca-8c262b75650e"
    ]
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
<h3>POST /processes/update-travel-specification/execution <a href="../objects/updateTravelSpecificationRequest.md">updateTravelSpecificationRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>update start/end location or start/end time</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "package": "d947eef7-ae70-49f8-b623-2bf6e7ec5549",
    "leg": "1f30eadf-40df-4ba1-a5e9-461fe84d401a",
    "startTime": "2024-01-15T10:30:00Z",
    "endTime": "2024-01-15T13:33:00Z"
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
<h3>POST /processes/update-traveller/execution <a href="../objects/updateTravellerRequest.md">updateTravellerRequest</a> -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>update details of a traveller</i><br><details><summary><i>Request Body</i></summary>

```json
{
  "inputs": {
    "traveller": "ACT:342",
    "package": "8606aa98-775e-4f87-bd2c-490e016b2a37",
    "fullName": "H. Bakking"
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
