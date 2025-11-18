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

# offer module

This part of the API facilitates in supplying offers.

<h3>GET /collections/offers/items?offerId=... -> <a href="../objects/package.md">package</a></h3><div style="margin-left:20px"><i>Get offer details</i><br><details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `offerId` | query | string | ✓ | the identifier of an offer |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [package](../objects/package.md) | a single instance of a package
</details>
<br></div>
</details>
<h3>POST /processes/search-offers/execution <a href="../objects/searchOfferRequest.md">searchOfferRequest</a> -> <a href="../objects/offerCollection.md">offerCollection</a></h3><div style="margin-left:20px"><i>Search for offers</i><br>Returns offers based on travel specification, trip pattern, location, asset, product and user preferences. In case of a shallow integration, can even be offered as an endpoint without authentication.

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `bbox` | query | array |  | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional)  If the value consists of four numbers, the coordinate reference system is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  If the value consists of six numbers, the coordinate reference system is WGS 84 longitude/latitude/ellipsoidal height (http://www.opengis.net/def/crs/OGC/0/CRS84h) unless a different coordinate reference system is specified in the parameter `bbox-crs`.  The query parameter `bbox-crs` is specified in OGC API - Features - Part 2: Coordinate Reference Systems by Reference.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.  If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. |
</details>
<details><summary><i>Request Body</i></summary>

```json
{
    "inputs": {
      "type": "search_offer",
      "specification": {
        "from": "GPS:6.169639,52.253279",
        "to": "local:p2",
        "startTime": "2025-04-24T08:39:01.160Z",
        "endTime": "2025-04-25T08:39:01.160Z"
      },
      "travellers": [
        {
          "type": "traveller",
          "id": "traveller1",
          "entitlements": [
            {
              "id": "string",
              "type": "card_type",
              "cardType": "DISCOUNT",
              "subType": "NL daluren",
            },
          ],
          "requirements": {
            "mode": "TRAIN",
            "class": "FIRST_CLASS",
          }
        }
      ],
      "places": [
        {
          "placeId": "local:p2",
          "addressLine1": "Startline 1",
          "addressLine2": "Discountcity",
        }
      ]
    }
  }
```


</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/geo+json | [offerCollection](../objects/offerCollection.md) | a list of offers
</details>
<br></div>
</details>
