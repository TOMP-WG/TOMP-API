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