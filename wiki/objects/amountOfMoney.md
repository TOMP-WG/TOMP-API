# amountOfMoney

an amount of money, usable in fares, fare calculations or in extra costs.

**Type:** `object`

semantics [{'transmodel': 'FARE PRICE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | number (float) | ✓ | This should be in the base unit as defined by the ISO 4217 currency code with... |
| `taxPercentageUsed` | [float](float.md) |  | value added tax rate (percentage of amount) |
| `currencyCode` | [currencyCode](currencyCode.md) |  | ISO 4217 currency code |
| `vatCountryCode` | [country](country.md) |  | two-letter country codes according to ISO 3166-1 |

## Detailed Properties

- **`amount`**  *(number (float))* - **required**  
  This should be in the base unit as defined by the ISO 4217 currency code with the appropriate number of decimal places and omitting the currency symbol. e.g. if the price is in US Dollars the price would be 9.95. This is inclusive VAT

- **`taxPercentageUsed`**  *([float](float.md))* - optional  
  value added tax rate (percentage of amount)

- **`currencyCode`**  *([currencyCode](currencyCode.md))* - optional  
  value: "[a-zA-Z]{3}"
  ISO 4217 currency code

- **`vatCountryCode`**  *([country](country.md))* - optional  
  value: "[A-Z]{2}"
  two-letter country codes according to ISO 3166-1

## Example

```json
{
  "amount": 3.14,
  "taxPercentageUsed": 19,
  "currencyCode": "EUR",
  "vatCountryCode": "BE"
}
```