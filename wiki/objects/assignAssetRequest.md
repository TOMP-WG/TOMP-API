# assignAssetRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ | this can be used to assign an asset (/seat) to a leg, by using the field `ass... |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  this can be used to assign an asset (/seat) to a leg, by using the field `asset`. If you want to replace an asset, fill the field `replacesAsset` with the asset to replace and `asset` with the new one. If you want to remove an assigned asset from a leg, fill `asset` with 'null' and fill `replacesAsset` with the asset to remove.
  - **`package`**  *([packageReference](packageReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`leg`**  *([legReference](legReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`asset`**  *([assetReference](assetReference.md))* - **required**  
    default string, full names etc (length 0-200)
  - **`replacesAsset`**  *([assetReference](assetReference.md))* - optional  
    default string, full names etc (length 0-200)

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
## Example

```json
{
  "inputs": {
    "package": "64c247f5-97ac-4bc5-b904-515beac004e8",
    "leg": "26c45426-a9ee-45ce-b93f-515eb747e1b8",
    "asset": "Seat 35A"
  }
}
```