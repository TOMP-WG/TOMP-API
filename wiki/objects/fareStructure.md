# fareStructure

**Type:** `object`

semantics [{'transmodel': 'TARIFF'}]

---

## Composition (allOf)

This schema is composed of **all** of the following schemas:

1. [amountOfMoney](amountOfMoney.md)
   - an amount of money, usable in fares, fare calculations or in extra costs.
   - Properties: `amount`, `taxPercentageUsed`, `currencyCode`, `vatCountryCode`
2. object
   - the total fare is the sum of all parts, except for the 'MAX' fareStructureElement. This one descripes the maximum price for the complete leg.
   - Properties: `id`, `estimated`, `description`, `userProfiles`, `temporalValidity`, `yieldPriceUrl`, `elements`

## Example

```json
{
  "amount": 3.14,
  "taxPercentageUsed": 21,
  "currencyCode": "EUR",
  "elements": [
    {
      "amount": 3.14,
      "type": "FIXED"
    },
    {
      "amount": 0.21,
      "type": "FLEX",
      "units": "KM",
      "amountOfUnits": 1
    }
  ],
  "estimated": true,
  "description": "Simple fare (21cts/km), with start tariff"
}
```