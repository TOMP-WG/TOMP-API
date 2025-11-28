# financialDetail

**Type:** `object`

semantics [{'transmodel': 'none'}]

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [amountOfMoney](amountOfMoney.md)
   - an amount of money, usable in fares, fare calculations or in extra costs.
   - Properties: `amount`, `taxPercentageUsed`, `currencyCode`, `vatCountryCode`
2. object
   - Properties: `id`, `category`, `state`, `expirationDate`, `sequenceId`, `invoiceId`, `invoiceDate`, `comment`, `units`, `vatNumber`, `bankAccount`, `customFields`

## Example

```json
{
  "amount": 3.14,
  "taxPercentageUsed": 0,
  "currencyCode": "[a-zA-Z]{3}",
  "vatCountryCode": "[A-Z]{2}",
  "id": "identifier",
  "category": "ALL",
  "state": "TO_INVOICE"
}
```