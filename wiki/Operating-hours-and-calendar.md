[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) >> [Operating hours and calendar](Operating-hours-and-calendar.md)

# Operating hours
The operating hours are compliant with GBFS 2.0, but extended to specify operating hours per station or region.
| field | required | description |
| --- | --- | --- |
| startTime | * | The start of the opening hours on each day. Format HH:MM, local time |
| endTime | * | The end of the opening hours on each day. Format HH:MM, local time |
| days | * | Array of days where these hours are applied to, enum [MON - SUN] |
| userType | | This indicates that this set of rental hours applies to either members or non-members only. |
| stationId | | Id of the station where these hours apply to, reference to /operator/stations/ |
| regionId | | Id of the region where these hours apply to, reference to /operator/regions/ |

The result of this endpoint contains an object for all stations/regions, with the default opening hours and for each station or region that doesn't comply with these opening hours, a specific object for that station/region.

## Example
```
[
  {
    "userType": "MEMBER",
    "stationId": "BRUX_01",
    "startTime": "08:00",
    "endTime": "19:00",
    "days": [
      "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"
    ]
  },
  {
    "stationId": "BAST_01",
    "startTime": "08:00",
    "endTime": "19:00",
    "days": [
      "MON", "TUE", "WED", "THU", "FRI"
    ]
  },
  {
    "stationId": "BAST_01",
    "startTime": "10:00",
    "endTime": "15:00",
    "days": [
      "SAT", "SUN"
    ]
  }
]
```
The station in Brussels is open from 8AM until 7PM, 7 days in the week and The station in Bastenaken is open from 8 until 19 during the weekdays and in the weekend from 10AM until 3PM.

# Operating calendar
| field | required | description |
| --- | --- | --- |
| startYear | | Starting year for the system operations. If not specified, it is 'this year' |
| startMonth | * | Starting month for the system operations (1-12) |
| startDay | * | Starting day for the system operations (1-31) |
| endYear | | Ending year for the system operations. If not specified, it is 'this year' |
| endMonth | * | Ending month for the system operations (1-12) |
| endDay | * | Ending day for the system operations (1-31) |
| stationId | | Id of the station where this calendar apply to, reference to /operator/stations/ |
| regionId | | Id of the region where this calendar apply to, reference to /operator/regions/ |

Here is the same remark about stations/regions as in Operating hours.

## Example
```
[
  {
    "stationId": "BRUX_01",
    "startDay": 1,
    "startMonth": 1,
    "startYear": 2019,
    "endDay": 31,
    "endMonth": 12,
    "endYear": 2019
  },
    {
    "stationId": "BAST_01",
    "startDay": 1,
    "startMonth": 4,
    "startYear": 2019,
    "endDay": 31,
    "endMonth": 09,
    "endYear": 2019
  }
]
```
Station 01 in Brussels is open all days in 2019, in Bastenaken only from the first of April until the last day of September.