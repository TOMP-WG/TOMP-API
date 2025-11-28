# geojsonCollectionProperties

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `id` | [shortString](shortString.md) | ✓ | short string, display names (length 0-75) |
| `definitions` | [definitions](definitions.md) |  | object containing all necessary collections for a package and a offerCollecti... |

## Detailed Properties

- **`type`**  *(string)* - **required**  

- **`id`**  *([shortString](shortString.md))* - **required**  
  short string, display names (length 0-75)

- **`definitions`**  *([definitions](definitions.md))* - optional  
  object containing all necessary collections for a package and a offerCollection Both refer to objects in these collections.
  - **`products`**  *(array[object])* - optional  
    **Array item properties:**
    - **`type`**  *(string)* - **required**  
      value: "product"
    - **`id`**  *(string)* - **required**  
      default string, full names etc (length 0-200)
    - **`name`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`description`**  *(string)* - optional  
      long string, memos etc (length 0-10.000)
    - **`parts`**  *(array[string])* - optional  
      to be used for composed products.
    - **`fare`**  *(object)* - optional  
    - **`conditions`**  *(array[enum (`REFUNDABLE`, `EXCHANGABLE`, `CANCELLABLE`, `TRANSFERABLE`, `DEPOSIT_REQUIRED`, ...)])* - optional  
    - **`guarantees`**  *(array[object])* - optional  
      **Array item properties:**
      - **`id`**  *(string)* - optional  
        https://en.wikipedia.org/wiki/Universally_unique_identifier see also https://www.ietf.org/rfc/rfc4122.txt (ae76f51c-a1a6-46af-b9ab-8233564adcae)
      - **`name`**  *(string)* - optional  
        default string, full names etc (length 0-200)
      - **`organisation`**  *(string)* - optional  
        guaranteeing organisation
      - **`type`**  *(enum (`ALTERNATIVE_JOURNEY`, `HOME_LEG`, `RETURN_TO_ORIGIN`, `ON_TIME_TRAVEL`, `TRIP_ON_TIME`, ...))* - optional  
        _ALTERNATIVE_JOURNEY_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY is not available then alternative SERVICE JOURNEY will be provided. -| (EASEMENT_REDRESS, PRODUCT EXCHANGE REDRESS) _HOME_LEG_ - A TRIP REPAIR GUARANTEE that if a the passenger is unable to reach their destination by public transport because of a delay in services, a taxi to their destination will be provided. -| (TAXI HOME REDRESS) _RETURN_TO_ORIGIN_ - A TRIP REPAIR GUARANTEE that if a designated SERVICE JOURNEY cannot be completed, then the passenger will be returned to their origin stop. -| (RETURN TO ORIGIN REDRESS)
_ON_TIME_TRAVEL_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if repeated travel within a certain TIME INTERVAL fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _TRIP_ON_TIME_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a trip fails to meet certain performance targets as to arrival times. -| (ALL REDRESSES, needs TEMPORAL PARAMETER) _FACILITIES_AVAILABLE_ - A TRAVEL QUALITY GUARANTEE that compensation will be offered if a facility or service (e.g. WIFI, Meal, seat reservation, etc) is not available or fails to meet a specified quality. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ACCOMODATION_ - A TRAVEL QUALITY GUARANTEE that special accommodation will be provided in the event of severe disruption. -| (ALL REDRESSES, needs SERVICE PARAMETER) _MOBILITY_ASSISTANCE_ - A TRAVEL QUALITY GUARANTEE that mobility assistance will be provided. -| (ALL REDRESSES, needs SERVICE PARAMETER) _PASSENGER_SUPPORT_ - A TRAVEL QUALITY GUARANTEE that assistance will be provided, for example, if a disruption occurs or a that stations are staffed. (ALL REDRESSES)
_DISRUPTION_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on disruptions will be made available. (ALL REDRESSES) _REDRESS_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on available compensation or other statutory and discretionary redress options will be made available to the passenger. (ALL REDRESSES) _BEST_FARE_INFORMATION_ - An INFORMATION QUALITY GUARANTEE that information on the best value fares will be made available (ALL REDRESSES)
_GENERAL_TRAVEL_ - An arbitrary OTHER TRAVEL GUARANTEE describing some special guarantee not covered by the normal categories (ALL REDRESSES) _MEDIA_REPLACEMENT_ - An OTHER GUARANTEE that a replacement media will be provided if the original becomes unusable. _REFUND_UNUSED_ANCILLARIES_ - unused ancillaries will be refunded _REFUND_WHEN_CANCELLED_ - when cancelled before start, a refund will be scheduled
  - **`places`**  *(array[object])* - optional  
    Places that are not specified in an external data source (like a home address)
    **Array item properties:**
    - **`id`**  *(string)* - **required**  
      value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
      this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
    - **`type`**  *(string)* - optional  
      value: "place"
    - **`addressLine1`**  *(string)* - **required**  
      contains street, housenumber & additions example street 18, 2nd floor, 18-B33
    - **`addressLine2`**  *(string)* - optional  
      city or town, principal subdivision such as province, state or county Smallcity, Pinetree county
    - **`street`**  *(string)* - optional  
      street, consistent with addressLine1
    - **`houseNumber`**  *(integer)* - optional  
      house number, consistent with addressLine1
default: `0`
    - **`houseNumberAddition`**  *(string)* - optional  
      the additional part of the house number (f.x. 13bis, where 'bis' is the additional part), consistent with addressLine1
    - **`postalCode`**  *(string)* - optional  
      the postal code, whenever available
    - **`city`**  *(string)* - optional  
      specified city or town, consistent with addressLine2
    - **`province`**  *(string)* - optional  
      province or region, consistent with addressLine2
    - **`state`**  *(string)* - optional  
      state, consistent with addressLine2
    - **`country`**  *(string)* - optional  
      value: "[A-Z]{2}"
      two-letter country codes according to ISO 3166-1
    - **`additionalInfo`**  *(string)* - optional  
      additional information to find the address (f.x. just around the corner)
  - **`ancillaries`**  *(array[object])* - optional  
    **Array item properties:**
    - **`type`**  *(string)* - optional  
      value: "ancillary"
    - **`id`**  *(string)* - **required**  
      default string, full names etc (length 0-200)
    - **`name`**  *(string)* - optional  
      short string, display names (length 0-75)
    - **`description`**  *(string)* - optional  
      long string, memos etc (length 0-10.000)
    - **`product`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`image`**  *(string (uri))* - optional  
      Link to an image of the ancillary
    - **`fee`**  *(object)* - optional  
  - **`assets`**  *(array[object])* - optional  
    **Array item properties:**
    - **`type`**  *(string)* - optional  
      value: "asset"
    - **`id`**  *(string)* - **required**  
      Identifier of an asset. Can be an external reference, but also a (internal) ID
    - **`visualId`**  *(string)* - optional  
      for instance, a license plate or seat number.
    - **`product`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`mode`**  *(enum (`AIR`, `BUS`, `TROLLEYBUS`, `TRAM`, `COACH`, ...))* - optional  
      These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.
    - **`subMode`**  *(string)* - optional  
      a more precise classification of the asset, like 'cargo bike', 'public bus', 'coach bus', 'office bus', 'water taxi',  'segway'. This is mandatory when using 'OTHER' as class.
    - **`damages`**  *(array[object])* - optional  
      list of damages that are reported for this asset
      **Array item properties:**
      - **`assetComponent`**  *(enum (`FRONT`, `REAR`, `LEFT`, `RIGHT`, `TOP`, ...))* - **required**  
        Part/Component of the asset affected. If OTHER is specified the description needs to provide more detail as to what part/component is affected.<br>
      - **`description`**  *(string)* - **required**  
        Description of the damage.
      - **`pictures`**  *(array[string (uri)])* - optional  
        URL where pictures of the damage can be accessed. Any special characters in the URL must be correctly escaped.
    - **`cargo`**  *(object)* - optional  
      applicable properties to specify cargo space/loads
    - **`appSupport`**  *(object)* - optional  
      attributes to display/use in an external app.
    - **`equipment`**  *(array[string])* - optional  
      list of external references
    - **`customFields`**  *(object)* - optional  
      dictionary for extra fields (bilatural agreements)
    - **`fee`**  *(object)* - optional  
  - **`travellers`**  *(array[object])* - optional  
    **Array item properties:**
    - **`type`**  *(string)* - **required**  
      value: "traveller"
    - **`id`**  *(string)* - **required**  
      default string, full names etc (length 0-200)
    - **`characteristics`**  *(object)* - optional  
    - **`requirements`**  *(object)* - optional  
    - **`profile`**  *(string)* - optional  
      default string, full names etc (length 0-200)
    - **`groupSize`**  *(number)* - optional  
      in case of a travelling party, specify the (sub)group size with equivalent attributes

## Additional Properties

✅ Additional properties of any type are allowed.

## Example

```json
{
  "type": "example-string",
  "id": "identifier",
  "definitions": {
    "products": [
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null,
        "parts": null
      },
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null,
        "parts": null
      }
    ],
    "places": [],
    "ancillaries": [
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null
      },
      {
        "id": null,
        "type": null,
        "name": null,
        "description": null
      }
    ]
  }
}
```