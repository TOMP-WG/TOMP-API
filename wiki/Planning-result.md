[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Planning result](Planning-result.md)

| field | required | description | 
| --- | --- | --- | 
| validUntil | * | format: <ul><li> format [ISO 8601](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#rfc.section.5.6) <li>The time until which the presented options are (likely) available</ul> |
| options | * | the list of possible options (of object `booking`) this TO can deliver. It is dependent on the query-parameter `booking-intent` how accurate the result can be. In case of `true`, the results must contain an ID, to refer to in the [booking phase](booking-phase.md) and contains trustable information, with an accurate price (to be paid by the MP to the TO). |

# Bookings
Each result in the 'options' array is a complete [booking](booking-object.md) object. 