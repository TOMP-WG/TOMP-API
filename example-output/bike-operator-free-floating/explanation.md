# Free floating bike operator

## Meta endpoint

We're going to address the items that are specific for the free floating operators in the `meta-endpoint`:

##### Endpoints:

```json
"endpoints": [
    { "method": "GET", "path": "/operator/meta/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/information/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/regions/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/operating-hours/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/pricing-plans/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/stations/", "status": "NOT_IMPLEMENTED" },
    { "method": "GET", "path": "/operator/available-assets/", "status": "IMPLEMENTED" },
    { "method": "GET", "path": "/operator/alerts/", "status": "NOT_IMPLEMENTED" },
    { "method": "POST", "path": "/plannings/", "status": "IMPLEMENTED" },
    { "method": "POST", "path": "/bookings/", "status": "IMPLEMENTED" },
    { "method": "POST", "path": "/bookings/{id}/events", "status": "IMPLEMENTED", "eventType": "COMMIT" },
    { "method": "POST", "path": "/bookings/{id}/events", "status": "IMPLEMENTED", "eventType": "DENY" },
    { "method": "POST", "path": "/legs/{id}/events", "status": "NOT_IMPLEMENTED", "eventType": "SET_IN_USE" },
    { "method": "POST", "path": "/legs/{id}/events", "status": "IMPLEMENTED", "eventType": "FINISH" },
    { "method": "POST", "path": "/payment/journal-entry?id={id}", "status": "IMPLEMENTED" }
],

```

Note that 'stations' isn't implemented. 'set_in_use' isn't implemented eighter, because of the following part of the meta-endpoint, the process identifiers.

##### Process identifiers - remotely unlockable

```json
"processIdentifiers":  {
    "operatorInformation": ["DEFAULT"],
    "planning": ["ASSET_BASED", "QR_SCAN"],
    "booking": ["ATOMIC_BOOKING_UNLOCKING"],
    "tripExecution": ["LOCK_UNLOCK_REMOTELY", "OFF_BOARDING_REQUIRED"],
    "payment": []
}
```

One common thing for all these examples, is that the bike can be opened directly after the booking. If you want the end user to have control over the unlocking, don't provide the 'ATOMIC_BOOKING_UNLOCKING' process identifier.

This booking-identifier 'ATOMIC_BOOKING_UNLOCKING' requires the next implementation: as soon the booking is committed, the bike should be 'set_in_use' (the leg must be started) and the lock should be opened remotely. In this example, the bike's ID can be found using a QR code scan.

##### Process identifiers - Bluetooth operated (SDK)

```json
"processIdentifiers":  {
    "operatorInformation": ["DEFAULT"],
    "planning": ["ASSET_BASED", "BLUETOOTH_SCAN"],
    "booking": ["ACCESS_CODE_IN_COMMIT_EVENT"],
    "tripExecution": ["OFF_BOARDING_REQUIRED"],
    "payment": []
}
```

This setup requires the MP app to have the Bluetooth process integrated (SDK). In the response of the commit event the information to open up the lock, should be provided. The bike's ID can be retrieved using a Bluetooth-scan.

##### Process identifiers - Bluetooth operated (Deeplink)

```json
"processIdentifiers":  {
    "operatorInformation": ["DEFAULT"],
    "planning": ["ASSET_BASED", "BARCODE_SCAN"],
    "booking": ["ACCESS_CODE_IN_COMMIT_EVENT", "ACCESS_CODE_DEEPLINK"],
    "tripExecution": ["OFF_BOARDING_REQUIRED"],
    "payment": []
}
```

Again, the booking can be done using the TOMP-API, but there is a deeplink into the bike operators app to control the opening and closing of the bike (Bluetooth).

##### Process identifiers - Map based (book by click on map)

```json
"processIdentifiers":  {
    "operatorInformation": ["DEFAULT"],
    "planning": ["ASSET_BASED", "EXACT_ID"],
    "booking": ["AUTO_COMMIT", "ATOMIC_BOOKING_UNLOCKING"],
    "tripExecution": ["LOCK_UNLOCK_REMOTELY"],
    "payment": []
}
```

In this example, users can look up assets on a map (provided by the available-assets), book it (when booked, it directly returns a committed booking) and opened directly.

## Information

This endpoint gives high-level information about the operator:

```json
{
    "systemId": "XXTO0001",
    "language": ["eng-GB"],
    "name": "FreeBike",
    "timezone": "CET",
    "typeOfSystem": "FREE_FLOATING"
}
```

The systemId should be provided by the scheme owner. In a blockchain solution, it could be a DID. All languages that are usable in the API, should be enlisted here, so in the requests one of these must be used in the header.

##### Regions

The regions endpoint delivers different areas, and there should be at least one area of type 'OPERATING', to describe the boundaries where vehicles are allowed to operate.

There are other regions that can be served, for instance for implementing dynamic policies. Regions like 'PARKING', 'NO_ACCESS' and 'NO_PARKING' must be communicated to the end user to avoid fines.

```json
{
    "regionId": "PC_001",
    "name": "City Center",
    "type": "PARKING",
    "areaStartTime": "2022-11-16T10:00:00.840Z",
    "areaEndTime": "2022-11-16T18:00:00.840Z",
    "serviceArea": [ ... ]
}
```

This example describes a temporary PARKING area, where it is allowed to park the bike between 10 and 18, on the 16th of November 2022.

In the area below, there is a permanent speed limit of 10 kilometers per hour.

```json
{
    "regionId": "SL_34829",
    "name": "Speed limit around city mall",
    "type": "SPEED_LIMIT",
    "unitType": "KMPH",
    "unitValue": 10,
    "serviceArea": [ ... ]
}
```

##### Pricing plans

This is one of the most complex parts of the operator information. It can cope with start up prices, flexible prices per timespan or per kilometer, scales (for the first hour, 3th-5th kilometer) and max prices.

```json
{
    "planId": "P0001",
    "name": "default price",
    "fare": {
        "estimated": false,
        "class": "FARE",
        "parts": [
            { 
                "amount": 3.0,
                "currencyCode": "EUR",
                "type": "FIXED"
            },
            { 
                "amount": 0.2,
                "currencyCode": "EUR",
                "type": "FLEX",
                "unitType": "KM",
                "units": 1
            }
        ]
    },
    "isTaxable": false,
    "description": "the default price for our bikes"
}
```

This simple example shows that you have to pay 3 Euro as a start-up price, and after that 20 cents per kilometer.

We'll zoom in on the 'parts' field, to show a few other examples:

```json
"parts": [
            { 
                "amount": 3.0,
                "currencyCode": "EUR",
                "type": "FIXED"
            },
            { 
                "amount": 0,
                "currencyCode": "EUR",
                "type": "FLEX",
                "unitType": "KM",
                "units": 1,
                "scaleFrom": 0,
                "scaleTo": 3,
                "scaleType": "KM"
            },
            { 
                "amount": 0.2,
                "currencyCode": "EUR",
                "type": "FLEX",
                "unitType": "KM",
                "units": 1,
                "scaleFrom": 3,
                "scaleTo": 10,
                "scaleType": "KM"
            },
            { 
                "amount": 0.15,
                "currencyCode": "EUR",
                "type": "FLEX",
                "unitType": "KM",
                "units": 1,
                "scaleFrom": 10,
                "scaleType": "KM"
            },
            { 
                "amount": 30,
                "currencyCode": "EUR",
                "type": "MAX"
            }
        ]
```

This example starts with 3 euros, and after that the first 3 kilometers are for free. The kilometers 3-10 are billed for 0.20 euro, and from the 10th kilometer, you have to pay 0.15 euro per kilometer, but you never have to pay more than 30 euros for a trip.

You can also put helmets etc on the bill (and you have to pay 50 cents per 15 minutes):

```json
"parts": [
            { 
                "amount": 0.50,
                "currencyCode": "EUR",
                "type": "FLEX",
                "unitType": "HOUR",
                "units": 0.25
            },
            { 
                "amount": 3.2,
                "currencyCode": "EUR",
                "type": "FIXED",
                "name": "Rental of helmet",
                "class": "ANCILLARY"
            }
        ]
```

##### Available assets

In most cases, this endpoint returns only the available asset types. Not the specific assets. Unless you have a map-oriented solution, where the specific assets have to be displayed on a map.

You can create your own 'asset types'. You can specify them per station, or by a physical asset type, like an e-bike.

```json
[
  {
    "id": "e-bike-class-01",
    "nrAvailable": 10,
    "assetClass": "BICYCLE",
    "sharedProperties": {
        "name": "Standard e-bike, 15 km/h",
        "maxSpeed": 15,
        "regionId": "LU-01",
        "infantSeat": true,
        "helmetRequired": true,
        "ancillaries": [ 
            { "category": "BA", "number": "09" } 
            { "category": "BA", "number": "11" } 
            ]
    }
```

This example shows 10 available e-bikes, with an infant seat on the back (see https://github.com/TOMP-WG/TOMP-API/blob/master/documents/CROW%20passenger%20characteristics%20V2.0.xlsx) and a phone holder, in the region LU-01.
