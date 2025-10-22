[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md)  

The planning phase is quite simple with respect to the API: the Transport Operators (TOs) can be asked what assets they have available. This can be done using a request with fields like: from location to location, timestamp to start, timestamp to end, the number of travelers, and their (dis)abilities.  

> The planning endpoint has 2 flavors: one for quick searches (booking-intent=false) and one for creating offers (booking-intent=true). The first one is optional, but the TO should take into account that this flavor can be used a lot. Therefore it is not needed to be very accurate; the booking-intent=true should be accurate.  
>
> From version 1.3.0 these two flavors are split into 2 separate endpoints: /planning/inquiry and /planning/offer (see [#402](https://github.com/TOMP-WG/TOMP-API/issues/402)).

Within the planning phase we distinguish 3 'scenarios': 
* [Asset based](Asset-based.md): without long term reservation, book and open asset to use (e.g. using Bluetooth)
* [Planning based](Planning-based.md): long term reservation, assign physical asset later on
* [Map based](Map-based.md): using a map to depict all the available assets to book one

There are also a few specific requirements you can possibly have to deal with:
* [Requiring specific data](Requiring-specific-data.md) (like addresses, licenses, phone numbers) for booking
* [Return area](Return-area.md)
* [Postponed commit](Postponed-commit.md)

To integrate access methods (like deeplink, QR codes, etc.), look at [this page](Access-Methods.md).  
From version 1.3.0 it is also possible to enlist things you bring along (like luggage or a bike) and ancillaries you need. [Look here](Personal-requirements.md).

## Objects
* [Planning request](Planning-request.md): this request requires the information needed for planning. How the content should be filled, is described here and partially mandatory, dependent on the [processIdentifiers](processIdentifiers.md).
* [Planning result](Planning-result.md): the results are bookable objects, each containing a (sequence of) legs. If you're implementing and return max of 1 leg per booking, use the same ID for the booking as for the leg, for convenience reasons.
