# Style guide #
This document contains the style guide for the TOMP-API, in order to maintain the uniformity, comprehensibility and usability of the API.

## Common ##
Every seperate file should be ended with 2 carriage returns, just to let it work with the tooling.

### Clear description ###
What does a clear description say?

	* The meaning of the object/property
	* What purpose does it have
	* What it ISN'T (do)
	* The name of the object must match the description

E.g.

	booking:
	  type: object
	  description: A booking formalizes the leg to take, by which user, to make or made by a transport operator. It's not a proposal booking, but an actual booked asset to be payed for.

## Objects ##
Every seperate file contains 1 object. The object has a name, a type 'object' and a clear description of what it means. This information is followed by the required properties and the properties themselves.

E.g.

    booking:  
      type: object
      description: The booking information describing the state and details of the
        transaction
      required:
        - id
        - state
        - leg
        - customer
        - token
      properties:
        id:
          type: string

## Names ##
Every name consists of one or more words, seperated by dashes. E.g. support-status. NO CAMEL CASING, NO UNDERSCORES!

## Properties ##
The properties should always have a type and - if it's a flat type - a clear description. If it's an object, use ALWAYS a $ref, referencing to another object, **DON'T nest objects**.

Other keywords for properties (example, format, etc) are not mandatory. But when it makes sence, please add them. For references to websites/uri's, DO use format: URL. 

Property names are with lowercase, optionally use dashes.

E.g. 

      (the proper way)
      properties:
        id:
          description: The identifier MaaS will be using to referring to the booking
          type: string
        state:
          $ref: '#/components/schemas/booking-state'

      (INVALID!)
      properties:
        asset:
          type: object
          properties:
            passengers:
              type: integer
	
## Enumerations ##
Whenever it's possible, use enumerations to limitate the possibilities and interpretations.

E.g.

          type-of-system:
            description: Describes the type of system
            type: string
            enum: [FREE_FLOATING, STATION_BASED, VIRTUAL_STATION_BASED]
            example: FREE_FLOATING

The enumeration values are ALWAYS in capitals. The meaning of the values should be in the description of the property. Use underscores instead of dash.

## Arrays ##
The arrays should be handled the same way as properties, but in the 'items' there should be flat types OR $ref's. **No embedded objects**.
