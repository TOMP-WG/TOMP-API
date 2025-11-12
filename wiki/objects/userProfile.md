# userProfile

**Type:** `object`

semantics [{'transmodel': 'USER PROFILE'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | ✓ |  |
| `name` | [userProfileReference](userProfileReference.md) | ✓ | default string, full names etc (length 0-200) |
| `ageGroup` | enum (`ANYONE`, `INFANT`, `CHILD`, `YOUTH`, `ADULT`, ...) |  | The age group of the user profile, used to determine applicable fares and dis... |
| `age` | [range](range.md) |  |  |
| `length` | [range](range.md) |  |  |
| `weight` | [range](range.md) |  |  |
| `monthDayOnWhichAgeApplies` | [shortInt](shortInt.md) |  | a bit short integer (0-100) |
| `localResident` | boolean |  |  |
| `genderLimitation` | enum (`SAME_SEX`, `FEMALE_ONLY`, `MALE_ONLY`, `BOTH`) |  |  |
| `discountBasis` | enum (`DISCOUNT`, `FREE`, `FULL_RATE`) |  |  |

## Detailed Properties

- **`type`**  *(string)* - **required**  
  value: "userProfile"

- **`name`**  *([userProfileReference](userProfileReference.md))* - **required**  
  default string, full names etc (length 0-200)

- **`ageGroup`**  *(enum (`ANYONE`, `INFANT`, `CHILD`, `YOUTH`, `ADULT`, ...))* - optional  
  The age group of the user profile, used to determine applicable fares and discounts.

- **`age`**  *([range](range.md))* - optional  

- **`length`**  *([range](range.md))* - optional  

- **`weight`**  *([range](range.md))* - optional  

- **`monthDayOnWhichAgeApplies`**  *([shortInt](shortInt.md))* - optional  
  a bit short integer (0-100)
default: `0`

- **`localResident`**  *(boolean)* - optional  

- **`genderLimitation`**  *(enum (`SAME_SEX`, `FEMALE_ONLY`, `MALE_ONLY`, `BOTH`))* - optional  

- **`discountBasis`**  *(enum (`DISCOUNT`, `FREE`, `FULL_RATE`))* - optional  

## Example

```json
{
  "name": "example-string",
  "type": "userProfile",
  "ageGroup": "ANYONE",
  "age": [
    3.14,
    3.14
  ],
  "length": [
    3.14,
    3.14
  ]
}
```

