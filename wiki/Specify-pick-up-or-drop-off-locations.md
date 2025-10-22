[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Specifying locations](Specify-pick-up-or-drop-off-locations.md)  

**Q**: How do I specify a pick up or drop off location? A simple lon/lat is not enough (taxi scenario)<br>
**A**: During the planning phase you have to use the lon/lat for the starting and end location. As TO you should add the condition REQUIRE-BOOKING-DATA to your planning conditions: <br>
{ "name": "physical_locations", "conditionType": "conditionRequireBookingData", "requiredFields": ["FROM-ADDRESS", "TO-ADDRESS"] }<br>
And you have to add this to every result:<br>
{ .... conditions: ["physical_locations"] }<br>
This means you request the from and to address when booking. The MP should provide these fields when booking, otherwise you (TO) can reject it directly.<br>
/bookings/
<pre>
{
  "id": "the id you provided as TO",
  "customer": {
    "id": "A0-123456",
    "firstName": "John",
    "lastName": "Doe",
    "phone": "string",
    "email": "string"
  },
  "fromAddress": {
    "streetAddress": "example street 18, 2nd floor, 18B-33",
    "areaReference": "Smallcity, Pinetree county",
    "postalCode": "string",
    "country": "NL"
  },
  "toAddress": {
    "streetAddress": "example street 18, 2nd floor, 18B-33",
    "areaReference": "Smallcity, Pinetree county",
    "postalCode": "string",
    "country": "NL"
  }
}
</pre>