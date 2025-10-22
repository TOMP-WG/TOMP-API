[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md)

The __Operator information module__ provides more or less static data about the operator, its regions, stations, opening hours, pricing and 'terms and conditions' (since version 1.1). The most important endpoints are described here.

[Meta Information](Meta-Information.md)
> Meta information contains per version the implemented endpoints, the supported scenarios, the [process identifiers](processIdentifiers.md), and [process steps](process-steps.md). This endpoint is introduced for discovery reasons.

[Information](Information.md)
> This endpoint contains generic information about the TO. 

[Regions](Regions.md)
> Regions contains named polygons. These regions can be used to filter other items in the operator module.

[Stations](Stations.md)
> The public stations the TO publishes.

[Pricing information](Pricing-information.md)
> Published pricing plans.

[Available assets](Available-assets.md)
> The only 'realtime' endpoint in this module. Provides information about classes of assets (like 'Men\'s bike' or 'e-bike')

[Operating hours and calendar](Operating-hours-and-calendar.md)
> Describes the default opening hours per day of the week. Is GBFS compliant, an extension for 'specific days' is on the roadmap.

[Alerts](Alerts.md)
> For compliancy reasons with GBFS. Public notifications/alerts can be done using this endpoint, but peer-to-peer notifications (f.x. communication about support or ETAs) should be done using the /bookings/{id}/notification endpoint.