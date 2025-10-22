[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) | [Booking phase](Booking-phase.md) | [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [Customer object](Customer-object.md)

Please use this construct as little as possible (GDPR). The customer is the 'owner' of the app. She/he requests the planning, using hers/his account in the app. Could be the same as the traveler, but doesn't have to be the same one. Traveling in groups always means there is one customer, and this customer can be part of the group.

Contains all fields of [Traveler](Traveler.md), extended with these fields:
| field | required | description |
| --- | --- | --- |
| id | * | The identifier MaaS uses to identify the customer, can be MP or TO specific |
| travelerReference | | optional reference field to the travelers, from the planning request |
| initials | | Initials of the customer |
| firstName | | First name of the customer |
| lastName | | Last name of the customer |
| middleName | | Middle name of the customer |
| prefix | | prefix of the customer, like titles |
| postfix | | postfix of the customer, like titles | 
| phones | | phone numbers of the customer |
| email | | the email address of the customer |
| birthDate | | birth date of the customer |
| address | | registered address of the customer |
| photo	| | base64 encoded image of the customer |
| cards	| | [card](card.md)s of the customer |
| licenses | | [license](license.md)s of the customer |
