# paymentCategory

The category of the journalled item <br> _ALL_ - for filtering purposes only<br>
<h2>TO initiated payments </h2> To request these payments, use the notifications, send a notification containing the payment confirmation.<br> _DEPOSIT_ - a deposit, to refund, use _REFUND_<br> _DAMAGE_ - extra costs that must be paid by the MP due to damage to the asset or ancillaries<br> _LOSS_ - extra costs that must be paid by the MP due to loss of asset or ancillaries<br> _STOLEN_ - the asset (and ancillaries) are stolen and should be paid for<br> _EXTRA_USAGE_ - the asset is paid for in advance, additional usage must be paid for (can also be a refund when used less! The amount should be negative in that case)<br> _FINE_ - a fine that arrived later on<br> _OTHER_ASSET_USED_ - additional costs for a replaced asset<br> _FARE_ - the normal costs of the purchased and executiond leg(s)<br> _OTHER_ - unspecified<br>
_CREDIT_ - generic CREDIT, e.g. for kick-backs <br> _VOUCHER_ - part of the fare that is covered by a voucher (no need to pay)<br> _REFUND_ - refund of the deposit or upfront paid fare<br> _REBATE_ - (partial) rebate of the fare<br> _REIMBURSEMENT_ - reimbursement of the fare<br>

**Type:** `string`

semantics [{'transmodel': 'none'}]

---

## Example

```json
"ALL"
```

