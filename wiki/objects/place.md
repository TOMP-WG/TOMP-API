# place

address parts, where addressLine1 and 2 should contain the complete address, matches Content-Language

**Type:** `object`

semantics [{'transmodel': 'POSTAL ADDRESS'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [placeReference](placeReference.md) | ✓ | this string references to information that can be found in the `data sources`... |
| `type` | string |  |  |
| `addressLine1` | [longString](longString.md) | ✓ | contains street, housenumber & additions example street 18, 2nd floor, 18-B33 |
| `addressLine2` | [longString](longString.md) |  | city or town, principal subdivision such as province, state or county Smallci... |
| `street` | [normalString](normalString.md) |  | street, consistent with addressLine1 |
| `houseNumber` | [normalInt](normalInt.md) |  | house number, consistent with addressLine1 |
| `houseNumberAddition` | [tinyString](tinyString.md) |  | the additional part of the house number (f.x. 13bis, where 'bis' is the addit... |
| `postalCode` | [shortString](shortString.md) |  | the postal code, whenever available |
| `city` | [shortString](shortString.md) |  | specified city or town, consistent with addressLine2 |
| `province` | [shortString](shortString.md) |  | province or region, consistent with addressLine2 |
| `state` | [shortString](shortString.md) |  | state, consistent with addressLine2 |
| `country` | [country](country.md) |  | two-letter country codes according to ISO 3166-1 |
| `additionalInfo` | [longString](longString.md) |  | additional information to find the address (f.x. just around the corner) |

## Detailed Properties

- **`id`**  *([placeReference](placeReference.md))* - **required**  
  value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
  this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.

- **`type`**  *(string)* - optional  
  value: "place"

- **`addressLine1`**  *([longString](longString.md))* - **required**  
  contains street, housenumber & additions example street 18, 2nd floor, 18-B33

- **`addressLine2`**  *([longString](longString.md))* - optional  
  city or town, principal subdivision such as province, state or county Smallcity, Pinetree county

- **`street`**  *([normalString](normalString.md))* - optional  
  street, consistent with addressLine1

- **`houseNumber`**  *([normalInt](normalInt.md))* - optional  
  house number, consistent with addressLine1
default: `0`

- **`houseNumberAddition`**  *([tinyString](tinyString.md))* - optional  
  the additional part of the house number (f.x. 13bis, where 'bis' is the additional part), consistent with addressLine1

- **`postalCode`**  *([shortString](shortString.md))* - optional  
  the postal code, whenever available

- **`city`**  *([shortString](shortString.md))* - optional  
  specified city or town, consistent with addressLine2

- **`province`**  *([shortString](shortString.md))* - optional  
  province or region, consistent with addressLine2

- **`state`**  *([shortString](shortString.md))* - optional  
  state, consistent with addressLine2

- **`country`**  *([country](country.md))* - optional  
  value: "[A-Z]{2}"
  two-letter country codes according to ISO 3166-1

- **`additionalInfo`**  *([longString](longString.md))* - optional  
  additional information to find the address (f.x. just around the corner)

## Additional Properties

❌ No additional properties are allowed.

## Example

```json
{
  "id": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
  "addressLine1": "example-string",
  "type": "place",
  "addressLine2": "example-string",
  "street": "example-string"
}
```