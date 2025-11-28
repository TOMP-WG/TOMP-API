[home](home.md) > [Error handling in TOMP](errors.md)

# Introduction
The TOMP API uses a lot of endpoints that have to be used in a specific order. In order to facilitate the unhappy flows of calling those endpoints, error codes have been specified. At any moment in time and at any endpoint, errors can be returned. From both the transport operator to the maas provider and vice versa.

Error codes are forever active as per TOMP version 1.0 and are not version specific. Error codes and their meaning will always stay the same. However, the summary and description in the error code table may change to better explain what the error means.

# Format
Error codes will be returned within the body of an API response, along with the regular HTTP error code. The syntax of the error object can be found in [the latest Swagger file](https://app.swaggerhub.com/apis/TOMP-API-WG/transport-operator_maas_provider_api). The errorCode-field is required, the other fields are not. For instance, the title can be deducted from the error code table below using the errorCode, but may be included to make an error more human readable when working with the API.

```json
{ "errorCode": 3202,
  "title": "Availability expired.",
```

Additional fields may be returned, as long as the errorCode-field is provided. For instance, a transport operator may want to fill the detail field to include some more context regarding the error or return a unique identifier (in the instance field). This identifier may be used by developers of both parties to track down errors and look for the identifier in their logging. An example:

```json
{ "errorCode": 3202,
  "type": "Expired",
  "title": "Availability expired.",
  "detail": "The Nissan Leaf you want to confirm has been freed up. Please make a new booking.",
  "instance": "889bf030-8963-11ea-b110-63982e64cb91" }
```
# Error codes
Every error comes with an error code in the error code table. An error code is specified as x001. The x stands for a number in the _Module number table_ below. This reduces redundancy. For instance, when error x001 can happen in both the planning and booking phase, it can be returned both as 2001 and 3001.

**When an error is not present in the table below but you do want to return an error code to your clients, please use the error codes x500 and onwards and create an issue on our GitHub page.** We will then look at the error to see if we can incorporate it into this table. **DO NOT use the reserved range from x100 to x499!**

## Module number table

| # | Module |
| - | ------ |
| 1 | Operator information |
| 2 | Planning |
| 3 | Booking |
| 4 | Trip execution |
| 5 | Support |
| 6 | Payment |
| 7 | General |
| 8 | Customer Management |

## Error code table
The second digit of the error code stands for the type of error:
*  x000 to x199 are for technical errors that shouldn't happen in the normal usage of the TOMP API.
*  x200 to x499 are for functional errors that are to be expected in the normal usage of the TOMP API.
*  x500 and onwards are not yet defined.

### Technical errors

| Error code | Type | Title | Description of the error |
| ---------- | ---- | ------ | ------------|
| x001 | Missing | Field: {}, Reason: {} | |
| x002 | Invalid | Field: {}, Reason: {} | |
| x004 | Illegal operation | Operation {} is illegal in current status. | |
| x005 | Technical issue | Internal technical problem, contact support. | |
| x006 | Technical issue | No access to endpoint  | Using the authentication provided, this endpoint cannot be used. |
| x007 | Technical issue | Request limit | You've reached the maximum amount of requests per time period. |
| x008 | Illegal operation | Unsupported API-version | The version of the API you're trying to use is not supported. |
| x009 | Illegal operation | Page size too big | The request's page size is too big. Please have a look at the meta endpoint. |
| x100 - x199 | Placeholder for technical errors |  |  |

### Functional errors

| Error code | Type | Example detail | Description |
| ---------- | ---- | ------ | ------------|
| x201 | Maximum bookings per period reached | Your contract allows you to book {} assets per {time period}. | When you can only book a limited amount of assets per time period and you want to make another. |
| x202 | Expired | Availability of booking {} expired. | When the pending timer is finished and a new booking must be made in order to book this asset. |
| x203 | In use | Booking {} has started. | It is no longer possible to edit the details of this booking since the asset is already in use. |
| x204 | Not found | Booking {} not found. | The specified booking, leg, customer etc. cannot be found. |
| x209 | Booking | User blocked | Booking not possible because the user is blocked by the TO. This error is provided alongside a HTTP 428 error code |
| x210 | Customer Management | Duplicated customer | Customer with given data already exists and cannot be registered twice |
| x211 | Read-only | Data field {} is read-only | Data field cannot be changed |
| x200 - x499 | Placeholder for functional errors |  |

