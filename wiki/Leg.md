[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) | [Booking phase](Booking-phase.md) | [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [Leg](Leg.md)

The leg represents a part of a trip, made using one asset. A transfer from one train to another will result in 2 legs. It doesn't need to be for one traveler, it can also be for a group.

| field | required | description | 
| --- | --- | --- |
| id | mandatory after the planning phase  | The unique identifier (TO) of this leg |
| from| * | [Place](Place.md) |
| to | | [Place](Place.md) |
| departureTime	|| format: ISO 8601 The departure time of this leg |
| arrivalTime || format: ISO 8601 The intended arrival time at the to place |
| travelerReferenceNumbers | | This leg is intended to be for a (set of) referred travels (from the planning-request) |
| assetType| * | The asset type used in this leg as determined during booking, See [AssetType](AssetType.md) |
| legSequenceNumber || The order of the leg in the booking. There can be multiple legs with the same sequence (different user or parallel usage (eg. parking lot and a bike)). |
| asset	|| reference to a specific asset (if assigned) |
| pricing || pricing for this part of the trip (only to specify if detailed pricing needs to be published. Otherwise use the pricing in the booking) |
| suboperator || Delegated Transport Operator, needed in brooker/aggregator scenarios |
| conditions || [Conditions](Conditions.md) for this leg |
| state	|| status of a leg. Enum: NOT_STARTED, PREPARING, IN_USE, PAUSED, FINISHING, FINISHED, ISSUE_REPORTED (in 1.2.0: + CANCELLED) |
| departureDelay || A duration of some time (relative to a time) in milliseconds |
| arrivalDelay || A duration of some time (relative to a time) in milliseconds |
| distance || The estimated distance traveled in the leg (in meters) |
| progressGeometry || geometry of the leg |
| ticket || travel right proof |
| assetAccessData || data to access assets (Deeplink, QR code, etc). See [Access-Methods](Access-Methods.md) |