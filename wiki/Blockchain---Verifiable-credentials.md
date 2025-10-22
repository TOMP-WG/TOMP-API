The TOMP-API facilitates in communicating the DID and in the claims that can be verified. 

# How to know personal information will be verified using the blockchain?
In the result of the planning (v1.3: inquiry or offer), the claims that are going to be verified can be found in the condition field of the leg:
```
{
  "validUntil": "2021-11-19T13:37:36.113Z",
  "options": [
    {
      "id": "string",
	  ...
      "legs": [
        {
          "id": "string",
		  ...
          "conditions": [
            {
              "requiredFields": [
                "BLOCKCHAIN_CLAIMS"
              ],
              "claims": [
                "ABOVE_18", "DRIVER_LICENSE_CAR"
              ],
              "conditionType": "conditionRequireBookingData",
              "id": "claims"
            }
          ],
	  ...
       }
      ]
    }
  ]
}
```

## Known claims
The claims so far are:
* ABOVE_12
* ABOVE_18
* ABOVE_21
* DRIVER_LICENSE_CAR
* DRIVER_LICENSE_TRUCK
* DRIVER_LICENSE_MOPED
This list can be extended on request. Please add an issue to the Github to request one.

## Location of the DID
The DID is provided in the field `knownIdentifierProvider` in the booking request:

```
{
  "id": "34920hg3903",
  "customer": {
    {
      "knownIdentifierProvider": "did:example:123456789abcdefghi"
    }
  }
}
```
The TO can use this DID to verify the requested claims.
