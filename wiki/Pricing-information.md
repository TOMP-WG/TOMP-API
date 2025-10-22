[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Pricing information](Pricing-information.md) 

The endpoint '/operator/pricing-plans' should return general information about the pricing options. TOs and MPs can of course agree on other prices. It is not mandatory that this endpoint returns the prices for the calling MP. The 'fare' object is described [here](Fare-construction.md).

| field | required | description | 
| ----- | -------- | ----------- |
| planId | * | A unique identifier for this plan in the system |
| url | | a fully qualified URL where the customer can learn more about this particular scheme |
| name | * | name of this pricing scheme, matches Content-Language (see [Information](Information.md)) |
| fare | * | the fare object |
| isTaxable | * | false indicates that no additional tax will be added (either because tax is not charged, or because it is included) true indicates that tax will be added to the base price
| description | * | Text field describing the particular pricing plan in human readable terms. This should include the duration, price, conditions, etc. that the publisher would like users to see. This is intended to be a human-readable description and should not be used for automatic calculations, matches Content-Language |
| regionId |  | price plan applicable for this region (see [Regions](Regions.md)), introduced in 1.1. |
| stationId |  | price plan applicable for this station (see [Stations](Stations.md)), introduced in 1.1. |
| assetTypeId |  | price plan applicable for this assetType (see [Available assets](Available-assets.md)), introduced in 1.1. |
