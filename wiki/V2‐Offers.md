# Searching for Offers using the TOMP-API

Welcome to the guide on how to search for offers using the TOMP-API. This guide is tailored for developers and integrators looking to utilize the API to retrieve offers based on specific travel specifications, patterns, and preferences. The TOMP-API can be a powerful tool for integrating transport options into your Mobility as a Service (MaaS) platform.

## Overview

The TOMP-API provides an endpoint to search for offers based on various travel criteria, including travel specifications, trip patterns, locations, assets, products, and user preferences. This functionality is central to facilitating communication between Transport Operators (TO) and MaaS Providers (MP) to deliver a seamless user experience.

The primary endpoint for this operation is:

```
POST /processes/search-offers/execute
```

## Endpoint Details

- **Path**: `/processes/search-offers/execute`
- **Method**: POST
- **Operation ID**: `searchOffers`
- **Security**: BearerAuth, OAuth, OAuthPKI

### Description

This endpoint returns offers that match the specified travel criteria supplied in the request body. The responses are configured to provide a list of viable travel options with associated details and pricing. Each result must have an expiry date included in the header.

### Security

To access the offers search functionality, authentication is required. You can authenticate using:

- **Bearer Authentication**: Providing a JWT token obtained from the platform.
- **OAuth**: Obtaining tokens via username/password.
- **OAuthPKI**: OAuth 2.0 flow with PKI and mutual TLS for client authentication.

### Request Parameters

- **Headers**:
  - `Accept-Language` (required): Specifies the language preference for user-facing content. Must be a BCP 47 language tag.
  - `Authorization` (required): A JWT token for authentication.

- **Query Parameters**:
  - `limit` (optional): Limits the number of items presented in the response (default = 100, min = 1, max = 10000).
  - `offset` (optional): The starting index of the returned collection (default = 0).
  - `bbox` (optional): Bounding box for geospatial queries.

### Request Body Structure

The request body is designed to include travel specifications and other relevant details to obtain offers matching those criteria. Here is a detailed breakdown:

- **Root Object**:
  - `type`: This is a constant field set to "searchOffer", which indicates the nature of the request.
  - `specification`: This object contains details about the travel request. It can be a travelSpecification or a tripPattern.
  - `requirements`: (Optional) Specifies any additional requirements or constraints for the travelers.
  - `travellers`: (Optional) An array of traveler objects with details about each traveler.
  - `places`: (Optional) An array specifying custom places that are not available from an external data source.
  - `packageToExchange`: (Optional) Contains references to packages that might be exchanged.
  - `customFields`: (Optional) Allows for any additional custom data fields as per bilateral agreements between parties.

### Travel Specifications (`specification`)

The specification can include details from either travelSpecification or tripPattern as defined below:

- **Travel Specification**:
  - `type`: This should be set to "travelSpecification".
  - `from`: A place reference indicating the starting location (e.g., GPS:52.379189,4.899431).
  - `to`: A place reference indicating the destination location (e.g., GPS:51.924419,4.477733).
  - `via`: (Optional) An array of place references for intermediate stops.
  - `startTime`: (Optional) Intended departure time in ISO 8601 format.
  - `endTime`: (Optional) Intended arrival time.
- **Trip Pattern** (Extends travelSpecification):
  - `type`: This should be set to "tripPattern".
  - `serviceJourneys`: An array of service journey references related to the pattern.
  - `travelDate`: The specific date of travel.

### Successful Response

- **Status Code**: 200
- **Content-Type**: `application/geo+json`
- **Schema**: A list of offers, wrapped in a GeoJSON feature collection.
- **Headers**:
  - `Version`: API version used.
  - `Content-Language`: Language of the content.
  - `Expires`: Expiry date of the offer(s).

### Error Handling

- **Default Error Response**:
  - **Status Code**: An appropriate HTTP error status.
  - **Content-Type**: `application/json`
  - **Schema**: Provides details of the error encountered.
  - **Headers**:
    - `Version`: API version used.
    - `Content-Language`: Language of the error message.

## Example Request

```http
POST /processes/search-offers/execute HTTP/1.1
Host: example.to.eu
Authorization: Bearer your_jwt_token_here
Accept-Language: en-US
Content-Type: application/json

{
  "inputs": {
    "type": "searchOffer",
    "specification": {
      "type": "travelSpecification",
      "from": "P:start",
      "to": "gps:51.924419,4.477733",
      "startTime": "2023-10-15T09:00:00Z"
    },
    "requirements": {
      "mode": "BUS",
      "class": "ECONOMY_CLASS"
    },
    "travellers": [
      {
        "type": "traveller",
        "id": "traveler1",
		"profile": "ADULT",
        "characteristics": {
          "cards": [ { "type": "card", "cardType": "NS-Business", "cardNumber": "342342" } ]
        }
      },
	  {
        "type": "traveller",
        "id": "traveler2",
		"profile": "CHILD",
        "characteristics": {
          "age": 3
        }
      }
    ],
    "places": [
      {
        "id": "P:start",
        "type": "place",
        "addressLine1": "Leidseplein 3",
        "city": "Amsterdam",
        "country": "NL"
      }
    ]
  }
}
```

## Example Response

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "type": "offer",
        "summary": {
          "id": "offer123",
          "specification": {
            // Travel specification details
          },
          "price": {
            "amount": 25.50,
            "currencyCode": "EUR"
          },
          "products": [
            // Product references
          ]
        }
      },
      "geometry": {
        // GeoJSON geometry for offer
      }
    }
  ],
  "properties": {
    "id": "OfferCollection123",
    "type": "OfferCollection"
  }
}
```

## Conclusion

The TOMP-API offers a robust solution for searching transport offers, simplifying the integration between Transport Operators and MaaS providers. By engaging with this API, you can potentially offer users more tailored and efficient journey planning options as part of your mobility service.

For further information or to participate in developing the TOMP-API, consider becoming a member of the House Of TOMP, and help establish a uniform language between transport operators and resellers/MaaS providers for a more sustainable world.