# cardType

A generic description of a CARD

**Type:** `object`

semantics [{'transmodel': 'TYPE OF PAYMENT METHOD, MEDIUM ACCESS DEVICE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [cardTypeReference](cardTypeReference.md) | ✓ | external reference to address the card used. |
| `type` | string | ✓ |  |
| `cardCategory` | enum (`DISCOUNT`, `TRAVEL`, `BANK`, `CREDIT`, `ID`, ...) |  | The broad category of card<br> DISCOUNT - discount card, can be applied in th... |
| `subType` | [shortString](shortString.md) |  | For use in case of OTHER. Can be used in bilateral agreements. |
| `modes` | array[[mode](mode.md)] |  | modes for which this card can be used, when empty, all modes are allowed |
| `relatedProduct` | [productReference](productReference.md) |  | default string, full names etc (length 0-200) |
| `transportOrganisations` | array[[organisationReference](organisationReference.md)] |  | references to accepting parties, only if applicable |
| `customFields` | [customProperties](customProperties.md) |  | dictionary for extra fields (bilatural agreements) |

## Detailed Properties

- **`id`**  *([cardTypeReference](cardTypeReference.md))* - **required**  
  external reference to address the card used.

- **`type`**  *(string)* - **required**  
  value: "cardType"

- **`cardCategory`**  *(enum (`DISCOUNT`, `TRAVEL`, `BANK`, `CREDIT`, `ID`, ...))* - optional  
  The broad category of card<br> DISCOUNT - discount card, can be applied in the purchase process to get rebate<br> TRAVEL - (external) travel card, possibly paid for in other context, but also monthly, weekly or day-cards<br> BANK - bank card<br> CREDIT - credit card<br> ID - identification card, like an ID card<br> PASSPORT - passport to identify yourself<br> OTHER - unspecified

- **`subType`**  *([shortString](shortString.md))* - optional  
  For use in case of OTHER. Can be used in bilateral agreements.

- **`modes`**  *(array[[mode](mode.md)])* - optional  
  modes for which this card can be used, when empty, all modes are allowed

- **`relatedProduct`**  *([productReference](productReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`transportOrganisations`**  *(array[[organisationReference](organisationReference.md)])* - optional  
  references to accepting parties, only if applicable

- **`customFields`**  *([customProperties](customProperties.md))* - optional  
  dictionary for extra fields (bilatural agreements)

## Example

```json
{
  "type": "cardType",
  "id": "identifier",
  "cardCategory": "DISCOUNT",
  "subType": "example-string",
  "modes": [
    "AIR",
    "AIR"
  ]
}
```