[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Alerts](Alerts.md)

This endpoint returns all the alerts known to the TO that should be communicated to support public operations. This doesn't mean you have to publish flat bike tires etc. in here.

| field | required | description |
| --- | --- | --- | 
| alertId | * | a unique identifier for this alert
| alertType | * | Type of alert. Nowadays limited to SYSTEM_CLOSURE, STATION_CLOSURE, STATION_MOVE, OTHER
| startAndEndTimes | | Array of hashes with the keys "start" and "end" indicating when the alert is in effect (e.g. when the system or station is actually closed, or when it is scheduled to be moved). If this array is omitted then the alert should be displayed as long as it is in the feed.
| stationIds | | Array of strings - If this is an alert that affects one or more stations, include their ids, otherwise omit this field. If both stationIDs and regionIDs are omitted, assume this alert affects the entire system. Items reference /operator/stations/ |
| regionId | |  If this system has regions, and if this alert only affects certain regions, include their ids, otherwise, omit this field. If both stationIDs and regionIDs are omitted, assume this alert affects the entire system. Items reference /operator/regions/ |
| URL | | string($hostname) URL where the customer can learn more information about this alert, if there is one | 
| summary| * | A short summary of this alert to be displayed to the customer, should match Content-Language |
| description| | Detailed text description of the alert, should match Content-Language |
| lastUpdated| | Last update of this message. Format [ISO 8601](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#rfc.section.5.6) |

## Example
```
[
  {
    "alertId": "69215fe2-5066-4400-8ebe-9b464ee82713",
    "alertType": "STATION_CLOSURE",
    "startAndEndTimes": [
      [ "2021-04-01T00:00:00.000Z", "2021-04-02T00:00:00.000Z" ]
    ],
    "stationIds": "BRUX_01",
    "url": "http://myfirstbike.org/brussels/",
    "summary": "station closed",
    "description": "station closed due to vandalism",
    "lastUpdated": "2021-04-02T06:40:43.930Z"
  },
  {
    "alertId": "bf1d1a3f-bf23-47de-bf35-0a9dc159165c",
    "alertType": "STATION_CLOSURE",
    "startAndEndTimes": [
      [ "2021-04-03T00:00:00.000Z", "2021-04-04T00:00:00.000Z" ]
     ,[ "2021-04-07T00:00:00.000Z", "2021-04-08T00:00:00.000Z" ]
    ],
    "stationIds": "BRUX_01",
    "url": "http://myfirstbike.org/brussels/",
    "summary": "station closed",
    "description": "repair & maintenance",
    "lastUpdated": "2021-04-02T06:40:43.930Z"
  }
]
```
The station in Brussels is closed on the 1st of April, due to vandalism and it needs repairs. The operation combines it with a maintenance session on the 3th and 7th of April.