[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Use cases](Use-cases.md) > Use cases Technical

## TE1
### Description
As a TO I want to describe my implementation of the TOMP-API, to facilitate external parties to discover the interface and have a clear overview of what I do have and how I want to be treated.

**Implementation**
| Type | object | remarks |
|---|---|---|
|Endpoint| `POST /operator/meta`||

**Applies to**  
All modalities, and is especially applicable when acting in a data space or ecosystem.

## TE2
### Description
As a routing structure, I request information where to deliver the messages. The ID of the TO must be in the header field 'addressed-to', so I can deliver it to the right address.

**Implementation**
| Type | object | remarks |
|---|---|---|
|[Process identifier](Process-identifier.md) | TO_OPERATOR_REQUIRED | |
|Endpoint| ALL | all endpoint calls must be accomodated with the addressee |

**Applies to**  
All modalities.