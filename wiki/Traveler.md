[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Traveler](Traveler.md)

A generic description of a traveler, not including any identifying information. It is anonymously.

| field | required | description | 
| ----- | -------- | ----------- | 
| isValidated | | Whether this traveler's identity and properties have been verified by the MaaS provider |
| age | | Age of the traveler, may be approximate. Mandatory in case of MANDATORY_TRAVELER_AGE (see [processIdentifiers](processIdentifiers.md)) |
| referenceNumber | | reference number of the traveler. This number could be used to refer to in the planning result.  ([Planning Request](Planning-Request.md).[traveler](traveler.md)s.referenceNumber])|
| cardTypes | | array of cards the end user has, without any end user information (like card number). See [Card types](Card-types.md) |
| licenseTypes | | array of licenses the end user has, without any end user information (like license number). See [License types](License-types.md) |
| requirements | | array of requirements the end user has, not formalized yet, but the [Reizigerswoordenboek (CROW)](https://github.com/TOMP-WG/TOMP-API/blob/master/documents/Woordenboek%20Reizigerskenmerken%20CROW.pdf) can be used in here. [Requirement](Requirement.md)  |