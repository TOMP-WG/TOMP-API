[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md)  > [Card types](Card-types.md)

| field | required | description | 
| --- | --- | --- | 
| type | * | Card type ID, DISCOUNT, TRAVEL, BANK, CREDIT, PASSPORT, OTHER |
| subType | | For use in case of OTHER. Can be used in bilateral agreements. |
| assetClass | | Applicable for these [Asset class](Asset-class.md)es |
| acceptors || An array with accepting parties (MaaS Id of the accepting TO) |
