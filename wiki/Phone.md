[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [Customer](Customer.md) > [Phone](Phone.md)

| field | required | description | 
| --- | --- | --- | 
| preferred | | true or false. Is this the preferred phone number to use |
| number | | Phone number, pattern: ^[+]\*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.0-9]\*$ <br>example: +31-48934758 or +(0075)-834923384 or 020 1234 1234.<br> In case of international usage, always provide the country code. |
| kind| | LANDLINE or MOBILE |
| type | | PRIVATE, BUSINESS or OTHER |