### Examples:

To assign a seat to a leg:
```json
{
  "inputs": {
    "package": "64c247f5-97ac-4bc5-b904-515beac004e8",
    "leg": "26c45426-a9ee-45ce-b93f-515eb747e1b8",
    "asset": "Seat 35A"
  }
}
```

To assign a bike to a leg:
```json
{
  "inputs": {
    "package": "64c247f5-97ac-4bc5-b904-515beac004e8",
    "leg": "26c45426-a9ee-45ce-b93f-515eb747e1b8",
    "asset": "NDB:GBFS:vehicle:Bike93"
  }
}
```

To replace a bike:
```json
{
  "inputs": {
    "package": "64c247f5-97ac-4bc5-b904-515beac004e8",
    "leg": "26c45426-a9ee-45ce-b93f-515eb747e1b8",
    "asset": "Bike 001",
    "replacesAsset": "Bike 002"
  }
}
```
