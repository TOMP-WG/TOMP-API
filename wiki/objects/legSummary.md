# legSummary

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mode` | [mode](mode.md) | ✓ | These classes are taken from the NeTeX standard, but ALL and UNKNOWN are remo... |
| `name` | string | ✓ |  |
| `icon` | [url](url.md) |  | valid URL |
| `destination` | [normalString](normalString.md) |  | default string, full names etc (length 0-200) |
| `travellers` | array[[travellerReference](travellerReference.md)] |  |  |
| `equipment` | array[[equipmentReference](equipmentReference.md)] |  |  |
| `boarding` | object |  |  |
| `accomodation` | object |  |  |

## Detailed Properties

- **`mode`**  *([mode](mode.md))* - **required**  
  These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand OTHER and PARKING are added.

- **`name`**  *(string)* - **required**  

- **`icon`**  *([url](url.md))* - optional  
  valid URL

- **`destination`**  *([normalString](normalString.md))* - optional  
  default string, full names etc (length 0-200)

- **`travellers`**  *(array[[travellerReference](travellerReference.md)])* - optional  

- **`equipment`**  *(array[[equipmentReference](equipmentReference.md)])* - optional  

- **`boarding`**  *(object)* - optional  
  - **`onboardStayDuration`**  *([duration](duration.md))* - optional  
    value: "/-?P?=\d|T\d?:\d+Y??:\d+M??:\d+[DW]??:T?:\d+H??:\d+M??:\d+?:\.\d+?S??/"
    duration, ISO 8601 compliant
  - **`delayedAlightingAllowed`**  *(boolean)* - optional  
  - **`overnightStayAllowed`**  *(boolean)* - optional  
  - **`earlyBoardingAllowed`**  *(boolean)* - optional  

- **`accomodation`**  *(object)* - optional  
  - **`name`**  *([shortString](shortString.md))* - optional  
    short string, display names (length 0-75)
  - **`accomodationClass`**  *([classOfUse](classOfUse.md))* - optional  
    A classification of fare and other service classes by category of user entitled to use them.
  - **`accomodationGender`**  *(enum (`M`, `F`, `X`, `U`))* - optional  
  - **`sleeper`**  *(boolean)* - optional  
  - **`nuisances`**  *(array[enum (`no_smoking`, `smoking`, `mobile_phone_use_zone`, `mobile_phone_free_zone`, `family_area`, ...)])* - optional  

## Example

```json
{
  "mode": "AIR",
  "name": "example-string",
  "icon": "https://example.com",
  "destination": "example-string",
  "travellers": [
    "example-string",
    "example-string"
  ]
}
```