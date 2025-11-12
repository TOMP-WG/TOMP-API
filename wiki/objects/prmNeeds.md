# prmNeeds

**Type:** `object`

semantics [{'transmodel': 'TYPE OF USER NEEDS'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `encumbranceNeed` | enum (`pushchair`, `baggage_trolley`, `oversized_baggage`, `luggage_encumbrance`, `guide_dog`, ...) |  |  |
| `medicalNeed` | enum (`heart_condition`, `other`) |  |  |
| `mobilityNeed` | enum (`wheelchair`, `assisted_wheelchair`, `motorized_wheelchair`, `mobility_scooter`, `road_mobility_scooter`, ...) |  |  |
| `psychoSensoryNeed` | enum (`visual_impaired`, `auditory_impaired`, `cognitive_impaired`, `averse_to_lifts`, `averse_to_escalators`, ...) |  |  |

## Detailed Properties

- **`encumbranceNeed`**  *(enum (`pushchair`, `baggage_trolley`, `oversized_baggage`, `luggage_encumbrance`, `guide_dog`, ...))* - optional  

- **`medicalNeed`**  *(enum (`heart_condition`, `other`))* - optional  

- **`mobilityNeed`**  *(enum (`wheelchair`, `assisted_wheelchair`, `motorized_wheelchair`, `mobility_scooter`, `road_mobility_scooter`, ...))* - optional  

- **`psychoSensoryNeed`**  *(enum (`visual_impaired`, `auditory_impaired`, `cognitive_impaired`, `averse_to_lifts`, `averse_to_escalators`, ...))* - optional  

## Example

```json
{
  "encumbranceNeed": "pushchair",
  "medicalNeed": "heart_condition",
  "mobilityNeed": "wheelchair"
}
```