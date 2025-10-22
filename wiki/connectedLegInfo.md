This object contains information about the previous leg.

## connectedLegInfo

| field | required | description | 
| --- | --- | --- | 
| provider | | the provider of the previous leg (usually a Transport Operator reference) |
| assetReference | C* | the identification of the previous asset, like a flight number. This field (in case of a specific asset) or assetTypeReference must be filled. |
| assetTypeReference | C* | the identification of the previous asset type, like a discount combi. This field (in case of a specific asset type) or asset reference must be filled. |

C* = Conditionally required. One of both is required.
