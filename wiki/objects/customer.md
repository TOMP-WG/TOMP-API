# customer

A user that wishes to purchase a package

**Type:** `object`

semantics [{'transmodel': 'TRANSPORT CUSTOMER'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [customerReference](customerReference.md) | ✓ | The identifier the MP uses to identify the customer. Could be an external ref... |
| `initials` | [tinyString](tinyString.md) |  | Initials of the customer |
| `firstName` | [shortString](shortString.md) |  | First name of the customer |
| `lastName` | [shortString](shortString.md) |  | Last name of the customer |
| `middleName` | [tinyString](tinyString.md) |  | Middle name of the customer |
| `prefix` | [tinyString](tinyString.md) |  | prefix of the customer, like titles |
| `postfix` | [tinyString](tinyString.md) |  | postfix of the customer, like titles |
| `phoneNumber` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |
| `email` | [normalString](normalString.md) |  | the email address of the customer |
| `dateOfBirth` | [date](date.md) |  | https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12) |
| `placeOfBirth` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `countryOfBirth` | [shortString](shortString.md) |  | short string, display names (length 0-75) |
| `address` | [place](place.md) |  | address parts, where addressLine1 and 2 should contain the complete address, ... |
| `photo` | string |  |  |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |

## Detailed Properties

- **`id`**  *([customerReference](customerReference.md))* - **required**  
  The identifier the MP uses to identify the customer. Could be an external referenced ID, like a ABT account number

- **`initials`**  *([tinyString](tinyString.md))* - optional  
  Initials of the customer

- **`firstName`**  *([shortString](shortString.md))* - optional  
  First name of the customer

- **`lastName`**  *([shortString](shortString.md))* - optional  
  Last name of the customer

- **`middleName`**  *([tinyString](tinyString.md))* - optional  
  Middle name of the customer

- **`prefix`**  *([tinyString](tinyString.md))* - optional  
  prefix of the customer, like titles

- **`postfix`**  *([tinyString](tinyString.md))* - optional  
  postfix of the customer, like titles

- **`phoneNumber`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

- **`email`**  *([normalString](normalString.md))* - optional  
  the email address of the customer

- **`dateOfBirth`**  *([date](date.md))* - optional  
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12)

- **`placeOfBirth`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`countryOfBirth`**  *([shortString](shortString.md))* - optional  
  short string, display names (length 0-75)

- **`address`**  *([place](place.md))* - optional  
  address parts, where addressLine1 and 2 should contain the complete address, matches Content-Language
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

- **`photo`**  *(string)* - optional  

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "id": "identifier",
  "initials": "example-string",
  "firstName": "example-string",
  "lastName": "example-string"
}
```