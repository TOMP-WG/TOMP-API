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