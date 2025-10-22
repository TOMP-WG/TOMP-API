# Description
Cargoroo is a back-to-one TO that provides cargo bikes for immediate hire. Due to the type of vehicle we offer, we have defined the back-to-one model as being the most appropriate for our business model and use cases.

# Station Type & Info
All our stations are virtual in nature and may be represented as geoshape (a circle or a polygon). Currently only one asset is assigned to a single station for use.

<p>Stations can and may be moved. This may be at the request of the City or location manager that the station is located. It could also be in order to maximise fleet usage internally. There is no set duration or time that this will occur.

<p>There are currently no posts or visual identifiers defining a station except for the bike being in position. This may change in future.

# Asset Type & Info
All our assets are cargo bikes. They have a standard configuration with a hot swappable battery. Additional configurations to this bike that we currently have is if the cargo bike has Maxi-Cosi (child car seat) adaptors available for use in the bike.

<p>A user can currently filter our assets based on: Availability; Distance from a users current location; SOC on the batter; If the bike has the car seat adaptors.

# Shared Mobility Model
We operate a back-to-one model which means a user must pick up and return a hired asset to the same location.

<p>This means our concept of end location will always be the same as the start location. We do not have a defined end time (see below).

# Bookings
We do not currently allow advanced bookings within our system. This means we do not have an end time relating to a trip. A user must immediately reserve a bike to enable it to be held for usage. They are then free to use the bike within a 24 hour period for a duration up to 24 hours (to comply with our T&Cs).

<p>When a user reserves a bike they get a 20 minute window in which to be positioned next to the bike and to have opened the lock. Before the lock is opened and during the 20 minute window the booking is in the state of CLAIMED.

<p>Once the lock is opened the booking is REDEEMED.

<p>If the lock is closed outside of the station geofence that the bike belongs to the booking/trip is in a REDEEMED state.

<p>If the bike is within the station geofence to which it belongs and the lock is closed then the booking is ENDED and cost calculations for the booking are carried out.

<p>If a user fails to open the bike during the reservation period then the booking goes in to the state of EXPIRED.

# Trips
<p>A trip occurs when a user is in the state of REDEEMED within a booking. The trip has six key states:

TRIP_START (when a bike starts moving for the first time)<br>
MOTION_TO_REST (when a bike comes to a stop)<br>
REST_TO_MOTION (when a bike starts moving again from a stop)<br>
UNLOCKED_TO_LOCKED (when the lock is closed outside of the station geofence)<br>
LOCKED_TO_UNLOCKED (when the lock is opened)<br>
TRIP_END (when the bike has been returned to the geofence for the station and the lock is closed)<br>

# Limitations

<p>We do not offer multi legs.
<p>We do not allow a user to book in advance