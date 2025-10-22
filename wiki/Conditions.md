[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) | [Booking phase](Booking-phase.md) | [Trip execution phase](https://github.com/TOMP-WG/TOMP-API/wiki/#Trip-execution-phase.md) > [Conditions](Conditions.md)

Nowadays we distinguish a few conditions. These can be extended in the future. If conditions are for each asset, they should be enlisted in the [processIdentifiers](processIdentifiers.md). If they are for some asset, but not for all, the conditions can be added by the TO in the planning phase.

## Postponed commit
conditionPostponedCommit contains only one property: ultimateResponseTime. This condition only tells that the booking is not yet finally committed. In the booking phase, the TO will respond a booking with the state `CONDITIONAL_CONFIRMED`. Later on, the TO will respond on the MPs endpoint /bookings/{id}/event with a COMMIT or with a DENY. This has to be done before the ultimateResponseTime, otherwise is will be a DENY.

## Bookingdata required
conditionRequireBookingData: The TO can demand required data before it can commit a booking. This data is enlisted in the field requiredFields.
FROM_ADDRESS, TO_ADDRESS, BIRTHDATE, EMAIL, PERSONAL_ADDRESS, PHONE_NUMBERS, LICENSES, BANK_CARDS, DISCOUNT_CARDS, TRAVEL_CARDS, ID_CARDS, CREDIT_CARDS, NAME, AGE can be demanded and should be supplied in the booking request.

## Return area
conditionReturnArea: the asset has to be returned at a specific station or in a return area. The hours of return can also be changed (regarding the /operator/opening-hours).

## Deposit conditions
conditionDeposit: future use, is depending on how the Clearing Houses are developing

## Pay-as-you-go conditions
conditionPayWhenFinished: future use, is depending on how the Clearing Houses are developing

## Upfront payment
conditionUpfrontPayment: future use, is depending on how the Clearing Houses are developing