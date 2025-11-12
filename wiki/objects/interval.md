# interval

**Type:** `object`

semantics [{'transmodel': 'TIME INTERVAL (in case UNITS = minutes or hours)'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `from` | [float](float.md) | ✓ | in case of scaling, this is the bottom value (f.x. in the first hour 3 CAD, t... |
| `to` | [float](float.md) | ✓ | the upper value of the scale (f.x. 3 CAD in the first hour, this field should... |
| `units` | enum (`KM`, `MILE`, `HOUR`, `MINUTE`, `ZONE`, ...) | ✓ | the units is normally the same as the **interval.units**, but it doesn't have... |

## Detailed Properties

- **`from`**  *([float](float.md))* - **required**  
  in case of scaling, this is the bottom value (f.x. in the first hour 3 CAD, the `interval.from` should contain 0 and the `interval.units` HOUR). When `to` is used, but this field is missing, it should be assumed it is a 0.

- **`to`**  *([float](float.md))* - **required**  
  the upper value of the scale (f.x. 3 CAD in the first hour, this field should contain 1, `interval.from` 0 and `interval.units` HOUR)

- **`units`**  *(enum (`KM`, `MILE`, `HOUR`, `MINUTE`, `ZONE`, ...))* - **required**  
  the units is normally the same as the **interval.units**, but it doesn't have to be. For instance, you could pay 1 EUR per kilometer for the first hour.

## Example

```json
{
  "from": 0,
  "to": 0,
  "units": "KM"
}
```

