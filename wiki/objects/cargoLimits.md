# cargoLimits

applicable properties to specify cargo space/loads

**Type:** `object`

semantics [{'transmodel': 'LUGGAGE ALLOWANCE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | [longString](longString.md) |  | describes options to carry cargo, should match Content-Language |
| `volume` | [normalInt](normalInt.md) |  | the volume in liters of the cargo |
| `weight` | [normalInt](normalInt.md) |  | the weight in kilograms of the cargo |

## Detailed Properties

- **`description`**  *([longString](longString.md))* - optional  
  describes options to carry cargo, should match Content-Language

- **`volume`**  *([normalInt](normalInt.md))* - optional  
  the volume in liters of the cargo
default: `0`

- **`weight`**  *([normalInt](normalInt.md))* - optional  
  the weight in kilograms of the cargo
default: `0`

## Example

```json
{
  "description": "example-string",
  "volume": 0,
  "weight": 0
}
```