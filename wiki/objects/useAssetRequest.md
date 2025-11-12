# useAssetRequest

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
  - **`assets`**  *(array[[assetReference](assetReference.md)])* - **required**  
  - **`distribution`**  *([distribution](distribution.md))* - optional  
  - **`paymentMethod`**  *([typeOfPaymentMethod](typeOfPaymentMethod.md))* - optional  
  - **`travellers`**  *(array[[traveller](traveller.md)])* - optional  
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
    "assets": [
      "example-string"
    ],
    "customer": {
      "id": "identifier",
      "initials": "example-string",
      "firstName": "example-string",
      "lastName": "example-string"
    },
    "distribution": {
      "accessType": "BARCODE",
      "distributionChannel": "example-string"
    },
    "paymentMethod": "PREPAID"
  },
  "subscriber": {
    "successUri": "https://example.com",
    "inProgressUri": "https://example.com",
    "failedUri": "https://example.com"
  }
}
```

