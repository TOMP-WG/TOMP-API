[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Booking phase](Booking-phase.md) > [Customer](Customer.md)

The [Customer](Customer.md) is (technically derived from) a [Traveler](Traveler.md). He/she has a contract with the MP.

Only the additional fields are enlisted here.

| field | required | description |
| --- | --- | --- |
| id | * | The identifier MaaS uses to identify the customer |
| travelerReference | | optional reference field to the travelers in the planning request. |
| initials | | |
| firstName | | First name of the customer |
| lastName | | Last name of the customer |
| middleName | | Middle name of the customer |
| prefix | | prefix of the customer, like titles |
| postfix | | postfix of the customer, like titles |
| phones | | array of [Phone](Phone.md)s, only one phone in this array can have a true in the property 'preferred' |
| email | | the email address of the customer |
| birthDate | | ISO 6801 |
| address | | [Address](Address.md)es | 
| photo	 | | base64 encoded |
| cards	 | | Cards, containing specific information, should be the 'instances' of the card types of the traveler |
| licenses | | Licenses, containing specific information, should be the 'instances' of the licenses types of the traveler |
