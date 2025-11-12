# card

Any kind of card that isn't a license, only provide the cards that are required

**Type:** `object`

semantics [{'transmodel': 'CUSTOMER PAYMENT MEANS, MEDIUM APPLICATION INSTANCE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `cardType` | [cardTypeReference](cardTypeReference.md) | ✓ | the type of card, like a credit card, ID card, etc. |
| `cardNumber` | [shortString](shortString.md) | ✓ | number of the card, like ID number, credit card or bank account number |
| `description` | [shortString](shortString.md) |  | description of the card |
| `additionalNumber` | [shortString](shortString.md) |  | additional number, like CVC code or IBAN code |
| `endValidity` | [date](date.md) |  | this card is valid until this date |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "card"

- **`cardType`**  *([cardTypeReference](cardTypeReference.md))* - **required**  
  the type of card, like a credit card, ID card, etc.

- **`cardNumber`**  *([shortString](shortString.md))* - **required**  
  number of the card, like ID number, credit card or bank account number

- **`description`**  *([shortString](shortString.md))* - optional  
  description of the card

- **`additionalNumber`**  *([shortString](shortString.md))* - optional  
  additional number, like CVC code or IBAN code

- **`endValidity`**  *([date](date.md))* - optional  
  this card is valid until this date

## Example

```json
{
  "type": "card",
  "cardType": "example-string",
  "cardNumber": "example-string",
  "description": "example-string",
  "additionalNumber": "example-string",
  "endValidity": "full-date"
}
```