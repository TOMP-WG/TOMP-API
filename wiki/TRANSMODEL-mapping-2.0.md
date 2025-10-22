|TOMP concept|TRANSMODEL candidate|Remarks|Description|
|---|---|---|---|
|address|POSTAL ADDRESS|pretty good match, most attributes are there|street address, including number OR PO box number, eventually extended with internal reference like room number|
|amountOfMoney|-|It seems the TOMP has a separate concept, where TM has incorporated it||
|asset|VEHICLE|for things on wheels or boats||
||PARKING BAY|for parking||
||CYCLE STORAGE EQUIPMENT||A specialisation of PLACE EQUIPMENT describing cycle parking equipment: e.g. bike lockers|
||VEHICLE CHARGING EQUIPMENT|for charging poles||
||PASSENGER SPOT|for a seat||
|assetClass|MODE|Any means of transport|These classes are taken from the NeTeX standard, but ALL and UNKNOWN are removed. On the other hand, OTHER and PARKING are added.|
|assetType|VEHICLE TYPE|for things on wheels or boats||
||SITE ELEMENT|for everything geographical groupable||
||DECK (PLAN)?|seats||
|assetProperties|VEHICLE EQUIPMENT PROFILE|some overlap, a lot of details don't match|Aspects of an asset or assetType. Most aspects are optional and should only be used when applicable.|
|assetAccessMethods|TYPE OF TRAVEL DOCUMENT|should be something like a fulfilment||
|bankAccount|?|||
|booking|TRAVEL SPECIFICATION||The booking information describing the state and details of an agreed-upon trip|
||CUSTOMER PURCHASE PACKAGE||The booking information describing the state and details of an agreed-upon trip|
||SALES OFFER PACKAGE||The booking information describing the state and details of an agreed-upon trip|
|bookingOperation|?||operation on the booking|
|bookingRequest|TRIP REQUEST|Is not correct, it is a creation of a booking|A booking requested by the MP|
|bookingState|?||The life-cycle state of the booking|
|bookingStep|?||
|card|?|payment cards, discount cards, voucher numbers, ID|Any kind of card that isn't a license, only provide the cards that are required|
|cardType|?||A generic description of a card|
|condition|?||superclass for all conditions|
|conditionDeposit|?|deposit required|in case the TO demands a deposit before usage|
|conditionPayWhenFinished|?|pay-as-you-go|in case the TO demands a direct payment after usage|
|conditionPostponedCommit|?|(deprecated)Non-binding booking||
|conditionRequireBookingData|?|Very important|What information is required to supply when booking|
|conditionRequireEvidence|?|(deprecated)|use this condition to specify the evidence you require as TO in the off-boarding process|
|conditionRequireOnboardingSteps|?||steps to be taken in the onboarding process|
|conditionRequireOffboardingSteps|?||steps to be taken in the offboarding process|
|conditionRequirePausingSteps|?||steps to be taken when pausing|
|conditionRequireResumingSteps|?||steps to be taken when resuming the trip|
|conditionReturnArea|?||the asset has to be returned to this location|
|conditionUpfrontPayment|?||in case the TO demands a upfront payment before usage. The payment should be made in the booking phase.|
|confirmationRequest|?||the TO can ask permission to do something to the MP, as the MP is financially responsible|
|connectedLegInfo|?||this object describes the previous leg. It can contain f.x. a flight number, a used parking to get a discount, etc.|
|coordinates|LOCATION||location|
|country|COUNTRY||country code ISO 3166-1|
|customer|TRAVEL CUSTOMER||A MaaS user that wishes to make or has made a booking|
|damage|?||A damage of the vehicle|
|day|DAY OF WEEK|||
|distance|?||The estimated distance traveled in the leg (in meters)|
|duration|?||A duration of some time (relative to a time) in milliseconds|
|endpoint|?||A formal description of an endpoint|
|endpointImplementation|?||a complete endpoint description, containing all endpoints, their status, but also the served scenarios and implemented process flows|
|error|?||An error that the service may send|
|extraCosts|?||Costs that the TO is charging the MP; credits are negative|
|fare|TARIFF (Fare structure)|| The total fare is the sum of all parts|
|farePart|FARE STRUCTURE ELEMENT|| This describes a part of the fare (or discount)|
|geojsonLine|?||An array  of WGS84 coordinate pairs|
|geojsonPoint|?||Geojson Coordinate|
|geojsonPolygon|?||Geojson representation of a polygon|
|geojsonMultiPolygon|?||Geojson representation of a multi polygon|
|geojsonGeometry|?|||
|information|?||Information provided to or by end users|
|journalEntry|?|||
|journalState|?|||
|journalCategory|?|||
|leg|LEG||A planned (segment of) a booked trip using one asset type|
|legEvent|?||event during the execution|
|legProgress|?||provides current asset location & duration and distance of the current leg|
|legState|?||status of a leg|
|license|?||driver or usage license for a specific user. Contains the number and the assetType you're allowed to operate (e.g. driver's license for CAR)|
|licenseType|?||A category of license to use a certain asset class|
|notification|?NOTICE?||notifies the MaaS operator of issues with a booking|
|offBoardingStep|?||required steps during offboarding|
|onBoardingStep|?||required steps during onboarding|
|oneStopBookingRequest|?||a booking request using external information directly|
|pausingStep|?||required steps when starting to pause|
|phone|?|||
|place|PLACE||a origin or destination of a leg, 3D. lon/lat in WGS84|
|planningRequest|TRIP REQUEST||A travel planning, bookable options are requested|
|planningStep|?||this action allows to publish advertisements together with the proposed leg|
|planning|TRIP DELIVERY||A travel planning with bookable options that fulfill the constraints of the planning|
|processIdentifiers|?||describes the process and how to operate the API|
|requirement|MOBILITY NEED||In case of a disability|
|requirement|ENCUMBRANCE NEED||In case of traveler equipment (bring alongs)|
|requirement|VEHICLE EQUIPMENT||In case of an ancillary or asset equipment|
|requirements|?||array of requirements|
|resumingStep|?||actions to take when resuming|
|scenario|?|(deprecated)|scenario|
|stationInformation|?|GBFS concept||
|stopReference|STOP PLACE||reference to a STOP PLACE|
|suboperator|TRANSPORT ORGANISATION||The operator of a leg or asset, in case this is not the TO itself but should be shown to the user|
|supportRequest|?||request for support|
|supportStatus|?||the current status of support|
|systemAlert|?|GBFS concept||
|systemCalendar|?|GBFS concept||
|systemHours|?|GBFS concept||
|systemInformation|?|GBFS concept||
|systemPricingPlan|?|GBFS concept||
|systemRegion|?|GBFS concept||
|token|TRAVEL DOCUMENT||The validity token (such as booking ID, travel ticket etc.) that MaaS clients will display to show their right to travel, or use to access an asset|
|tokenArray|?|||
|tokenData|TRAVEL DOCUMENT|||
|tokenDefault|TRAVEL DOCUMENT||Arbitrary data the TO may pass along the ticket to the client|
|tokenDeeplink|TRAVEL DOCUMENT||deeplink info|
|tokenEKey|TRAVEL DOCUMENT||Axa EKey information|
|tokenQR|TRAVEL DOCUMENT||QR information|
|chamberOfCommerceInfo|?|(used in GBFS part)||
|traveler|INDIVIDUAL TRAVELER||A generic description of a traveler, not including any identifying information|

