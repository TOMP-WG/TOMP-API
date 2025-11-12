# fareStructureElement

this describes a part of the fare (or discount). It contains a for instance the startup costs (fixed) or the flex part (e.g. 1.25 EUR per 2.0 MILES). The amount is tax included. In case of discounts, the values are negative. With 'MAX' you can specify e.g. a maximum of 15 euro per day. Percentage is mainly added for discounts. The `scale` properties create the ability to communicate scales (e.g. the first 4 kilometers you've to pay EUR 0.35 per kilometer, the kilometers 4 until 8 EUR 0.50 and above it EUR 0.80 per kilometer).

**Type:** `object`

semantics [{'transmodel': 'TIME INTERVAL PRICE, TIME UNIT PRICE, GEOGRAPHICAL UNIT PRICE, GEOGRAPHICAL INTERVAL PRICE, LIMITING RULE'}]

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [amountOfMoney](amountOfMoney.md)
   - an amount of money, usable in fares, fare calculations or in extra costs.
   - Properties: `amount`, `taxPercentageUsed`, `currencyCode`, `vatCountryCode`
2. object
   - Properties: `type`, `priceCondition`, `units`, `amountOfUnits`, `scale`, `priceInterval`, `name`, `appliesTo`, `assetCondition`, `customFields`

## Example

```json
{
  "amount": 3.14,
  "taxPercentageUsed": 0,
  "currencyCode": "[a-zA-Z]{3}",
  "vatCountryCode": "[A-Z]{2}",
  "type": "FIXED",
  "priceCondition": "DEFAULT",
  "units": "KM",
  "amountOfUnits": 0
}
```

