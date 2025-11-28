# asset

the asset that can by applied to execute a leg.

**Type:** `object`

semantics [{'transmodel': 'VEHICLE, PARKING BAY, CYCLE STORAGE EQUIPMENT, VEHICLE CHARGING EQUIPMENT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string |  |  |
| `id` | [assetReference](assetReference.md) | ✓ | Identifier of an asset. Can be an external reference, but also a (internal) ID |
| `visualId` | [shortString](shortString.md) |  | for instance, a license plate or seat number. |
| `product` | [productReference](productReference.md) |  | default string, full names etc (length 0-200) |
| `mode` | [mode](mode.md) |  | These classes are taken from the NeTeX standard, but ALL and UNKNOWN are remo... |
| `subMode` | [normalString](normalString.md) |  | a more precise classification of the asset, like 'cargo bike', 'public bus', ... |
| `damages` | array[[damage](damage.md)] |  | list of damages that are reported for this asset |
| `cargo` | [cargoLimits](cargoLimits.md) |  | applicable properties to specify cargo space/loads |
| `appSupport` | [appSupport](appSupport.md) |  | attributes to display/use in an external app. |
| `equipment` | array[[equipmentReference](equipmentReference.md)] |  | list of external references |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |
| `fee` | [fareStructure](fareStructure.md) |  |  |

## Detailed Properties

- **`type`**  *(string)* - optional  
  value: "asset"

- **`id`**  *([assetReference](assetReference.md))* - **required**  
  Identifier of an asset. Can be an external reference, but also a (internal) ID

- **`visualId`**  *([shortString](shortString.md))* - optional  
  for instance, a license plate or seat number.

- **`product`**  *([productReference](productReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`mode`**  *([mode](mode.md))* - optional  
  These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.

- **`subMode`**  *([normalString](normalString.md))* - optional  
  a more precise classification of the asset, like 'cargo bike', 'public bus', 'coach bus', 'office bus', 'water taxi',  'segway'. This is mandatory when using 'OTHER' as class.

- **`damages`**  *(array[[damage](damage.md)])* - optional  
  list of damages that are reported for this asset
  **Array item properties:**
  - **`assetComponent`**  *(enum (`FRONT`, `REAR`, `LEFT`, `RIGHT`, `TOP`, ...))* - **required**  
    Part/Component of the asset affected. If OTHER is specified the description needs to provide more detail as to what part/component is affected.<br>
  - **`description`**  *(string)* - **required**  
    Description of the damage.
  - **`pictures`**  *(array[string (uri)])* - optional  
    URL where pictures of the damage can be accessed. Any special characters in the URL must be correctly escaped.

- **`cargo`**  *([cargoLimits](cargoLimits.md))* - optional  
  applicable properties to specify cargo space/loads
  - **`description`**  *(string)* - optional  
    describes options to carry cargo, should match Content-Language
  - **`volume`**  *(integer)* - optional  
    the volume in liters of the cargo
default: `0`
  - **`weight`**  *(integer)* - optional  
    the weight in kilograms of the cargo
default: `0`

- **`appSupport`**  *([appSupport](appSupport.md))* - optional  
  attributes to display/use in an external app.
  - **`displayName`**  *(string)* - optional  
    displayable name for this asset
  - **`description`**  *(string)* - optional  
    the description of the asset
  - **`image`**  *(string (uri))* - optional  
    Link to an image of the asset
  - **`icon`**  *(string (uri))* - optional  
    Link to an icon of the asset
  - **`accessMethods`**  *(array[enum (`BARCODE`, `QRCODE`, `AZTECCODE`, `REMOTE`, `DEEP_LINK`, ...)])* - optional  
    how this asset can be opened

- **`equipment`**  *(array[[equipmentReference](equipmentReference.md)])* - optional  
  list of external references

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

- **`fee`**  *([fareStructure](fareStructure.md))* - optional  

### Asset statusses

The asset statusses are not pre-defined. The operations are also free to create, but they have to be compliant with OGC API processes.  
The returned object must be a geojson, containing the package, just like all the other endpoints deliver.

Example json (list of links), to unlock (seperated from the 'start-leg') a bike
```json
[ 
    { "rel": "unlock-asset", 
      "href": "https://bike.org/tomp/v2/processes/unlock-asset/execution", 
      "body": { "inputs": { "asset": "GDR:GBFS_vehicle:2581dd23-460d-4df0-b8cf-fb2c97e17a40" } },
      "method": "POST",
      "type": "application/geo+json"
    }
]
```
The 'GDR:GBFS_vehicle' prefix must be available in the GET /collections/datasources/items endpoint, as a 'rel', referring to the source file where this asset can be found.

This approach can also be used to unlock lockers (the word 'asset' in the url is not mandatory, it can also be 'unlock-locker', or 'connect-charger').## Example

```json
{
  "id": "identifier",
  "type": "asset",
  "visualId": "example-string",
  "product": "example-string"
}
```