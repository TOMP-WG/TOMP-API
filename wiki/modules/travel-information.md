# travel information module

Traveller information that is not (yet) (completely) available in other standards

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

</details><h3>GET /collections/card-types/items -> <a href="../objects/cardTypeCollection.md">cardTypeCollection</a></h3><div style="margin-left:20px"><i>Retrieves all accepted card types</i><br><details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [cardTypeCollection](../objects/cardTypeCollection.md) | a list of accepted card types
</details>
<br></div>
</details>
<h3>GET /collections/entitlements/items -> <a href="../objects/entitlementCollection.md">entitlementCollection</a></h3><div style="margin-left:20px"><i>Retrieves all accepted entitlements</i><br><details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [entitlementCollection](../objects/entitlementCollection.md) | a list of accepted entitlements
</details>
<br></div>
</details>
<h3>GET /collections/fares/items?productId=... -> <a href="../objects/fareCollection.md">fareCollection</a></h3><div style="margin-left:20px"><i>Retrieve fare information for a product, user profile, entitlement, and card type. The reseller should identify itself with an authorization token (to get specific prices)</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `productId` | query | string | ✓ | Product identifier |
| `user-profile` | query | string |  | user profile name, as specified in the user profiles |
| `entitlement` | query | string |  | entitlement id |
| `card-type` | query | string |  | card type |
| `bbox` | query | array |  | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional)  If the value consists of four numbers, the coordinate reference system is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  If the value consists of six numbers, the coordinate reference system is WGS 84 longitude/latitude/ellipsoidal height (http://www.opengis.net/def/crs/OGC/0/CRS84h) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  The query parameter `bbox-crs` is specified in OGC API - Features - Part 2: Coordinate Reference Systems by Reference.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [fareCollection](../objects/fareCollection.md) | fares per user profile / entitlement / card type
</details>
<br></div>
</details>
<h3>GET /collections/license-types/items -> <a href="../objects/licenseTypeCollection.md">licenseTypeCollection</a></h3><div style="margin-left:20px"><i>Retrieves all accepted license types</i><br><details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [licenseTypeCollection](../objects/licenseTypeCollection.md) | a list of accepted license types
</details>
<br></div>
</details>
<h3>GET /collections/user-profiles/items -> <a href="../objects/userProfileCollection.md">userProfileCollection</a></h3><div style="margin-left:20px"><i>Retrieves all user profile definitions</i><br><details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [userProfileCollection](../objects/userProfileCollection.md) | a list of user profiles
</details>
<br></div>
</details>
