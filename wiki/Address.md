[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [Customer](Customer.md) > [Address](Address.md)

| field | required | description |
| --- | --- | --- | 
| streetAddress	| * | example: example street 18, 2nd floor, 18-B33 <br> Street address, including number OR PO box number, eventually extended with internal reference like room number, could match Content-Language |
| street | | street, consistent with streetAddress [v1.2.0] |
| houseNumber || house number, consistent with streetAddress [v1.2.0] |
| houseNumberAddition || the additional part of the house number (f.x. 13bis, where 'bis' is the additional part), consistent with streetAddress [v.1.2.0] |
| addressAdditionalInfo | | additional information to find the address (f.x. just around the corner) [v1.2.0] |
| areaReference	| * | example: Smallcity, Pinetree county <br>city or town, principal subdivision such as province, state or county, could match Content-Language |
| city || specified city or town, consistent with areaReference [v1.2.0] |
| province || province or region, consistent with areaReference [v1.2.0] |
| state || state, consistent with areaReference [v1.2.0] |
| postalCode | | |
| country | | example: NL<br>two-letter country codes according to [ISO 3166-1](https://nl.wikipedia.org/wiki/ISO_3166-1) |

```
{ 
  "streetAddress" : "example street 18, 2nd floor, 18-B33"
, "areaReference" : "Smallcity, Pinetree county"
, "postalCode": "3478GG"
, "country": "NL"
}
```

Since version 1.2.0, there is also the possibility to specify the street parts and area reference more specific:
```
       {
            "streetAddress": "example street 18, 2nd floor, 18-B33",
            "street": "example street",
            "houseNumber": 18,
            "houseNumberAddition": "B33",
            "addressAdditionalInfo": "2nd floor",
            "areaReference": "Smallcity, Pinetree county",
            "city": "Smallcity",
            "state": "Pinetree county",
            "postalCode": "3478GG",
            "country": "NL"
        }
```
Note that the 'streetAddress' and 'areaReference' fields are mandatory. The other fields are there to specify fields more clearly.

