# purchaseProductRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |
| `subscriber` | object |  |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`customer`**  *([customer](customer.md))* - optional  
    A user that wishes to purchase a package
  - **`location`**  *([placeReference](placeReference.md))* - optional  
    value: "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\-_.]+"
    this string references to information that can be found in the `data sources`. Enlist all prefixes (=rel) from the /collections/datasources/items that apply to a place/location. Default it matches already with 'GPS' (no entry required in the datasources). In case of a custom place (like home address), you can use the 'P:' prefix and add the address to the **places** list of the request/offer/package.
  - **`products`**  *(array[[productReference](productReference.md)])* - **required**  
  - **`distribution`**  *([distribution](distribution.md))* - optional  
  - **`traveller`**  *(array[[traveller](traveller.md)])* - optional  
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

- **`subscriber`**  *(object)* - optional  
  - **`successUri`**  *(string (uri))* - optional  
  - **`inProgressUri`**  *(string (uri))* - optional  
  - **`failedUri`**  *(string (uri))* - optional  

## Example

```json
{
  "inputs": {
    "products": [
      "example-string"
    ],
    "customer": {
      "id": "identifier",
      "initials": "example-string",
      "firstName": "example-string",
      "lastName": "example-string"
    },
    "location": "GPS|gps|{datasource-prefix}|P:[a-zA-Z0-9\\-_.]+",
    "distribution": {
      "accessType": "BARCODE",
      "distributionChannel": "example-string"
    }
  },
  "subscriber": {
    "successUri": "https://example.com",
    "inProgressUri": "https://example.com",
    "failedUri": "https://example.com"
  }
}
```

