# extendExpiryTimeRequest

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputs` | object | ✓ |  |
| `subscriber` | object |  |  |

## Detailed Properties

- **`inputs`**  *(object)* - **required**  
  - **`package`**  *([packageReference](packageReference.md))* - optional  
    default string, full names etc (length 0-200)
  - **`reason`**  *(enum (`PURCHASE_PENDING`, `PAYMENT_PENDING`, `OTHER`))* - optional  
    in case operation is EXTEND_EXPIRY_TIME, the reason for extension must be supplied here.<br> _PURCHASE_PENDING_ - The internal purchase process on the MP side is not yet finished<br> _PAYMENT_PENDING_ - The customer is in the payment process<br> _OTHER_ - unspecified
  - **`origin`**  *(enum (`TO`, `MP`, `END_USER`, `OTHER`))* - optional  
    This operation can be done on behalf of another party. The MP can act on behalf of the END_USER (cancel this booking for me); to override the default origin. In case this field is missing, it must be assumed that the events the MP is sending, this field should contain "MP". And in case the TO is sending, "TO".

- **`subscriber`**  *(object)* - optional  
  - **`successUri`**  *(string (uri))* - optional  
  - **`inProgressUri`**  *(string (uri))* - optional  
  - **`failedUri`**  *(string (uri))* - optional  

## Example

```json
{
  "inputs": {
    "package": "example-string",
    "reason": "PURCHASE_PENDING",
    "origin": "TO"
  },
  "subscriber": {
    "successUri": "https://example.com",
    "inProgressUri": "https://example.com",
    "failedUri": "https://example.com"
  }
}
```

