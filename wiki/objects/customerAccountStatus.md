# customerAccountStatus

status of a CUSTOMER ACCOUNT<br> _CREATED_ the customer account has been created but is not ready to create a purchase yet<br> _TO_PENDING_VALIDATION_ the customer account is pending a verification of identity and properties by the TO. No purchases can be made in this step<br> _OTP_REQUIRED_ the TO has sent an OTP to the customer's phone or email address and is expecting it to activate the account. No purchases can be made in this step<br> _ACTIVE_ the customer account is active and can continue to purchase offers<br> _BLOCKED_ the customer account has been blocked by the TO and can no longer use this TO<br>

**Type:** `string`

semantics [{'transmodel': 'CUSTOMER ACCOUNT . status'}]

---

## Example

```json
"CREATED"
```