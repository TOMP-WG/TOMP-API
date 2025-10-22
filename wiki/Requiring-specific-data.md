[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Requiring specific data](Requiring-specific-data.md)  

If the TO needs personal data to validate or to contact the traveler, it can be requested in the result of the planning. Therefore the 'conditions' are introduced.  

In each leg conditions can be added in the 'conditions' field. The condition needed for this purpose is the 'conditionRequireBookingData', with an array of required fields. Each field corresponds with a field in the request of the POST /bookings/. If the TO demands a specific field, the MP __must__ supply this field in the booking request, otherwise the TO must deny the booking.  

| required field label | field in /bookings/ request |
| -------------------- | --------------------------- |
| FROM_ADDRESS | from.physicalAddress |
| TO_ADDRESS | to.physicalAddress | 
| BIRTHDATE | customer.birthDate |
| EMAIL | customer.email |
| PERSONAL_ADDRESS | customer.address |
| PHONE_NUMBERS | customer.phones, with at least one phone number |
| LICENSES | customer.licenses |
| BANK_CARDS | customer.cards, with at least one card of type BANK |
| DISCOUNT_CARDS | customer.cards, with at least one card of type DISCOUNT |
| TRAVEL_CARDS | customer.cards, with at least one card of type TRAVEL |
| ID_CARDS | customer.cards, with at least one card of type ID or PASSPORT |
| CREDIT_CARDS | customer.cards, with at least one card of type CREDIT |
| NAME | customer.firstName AND customer.lastName |
| AGE | customer.age |
