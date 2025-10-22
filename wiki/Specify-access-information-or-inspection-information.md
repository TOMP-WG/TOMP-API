[home](https://github.com/TOMP-WG/TOMP-API/wiki)  

Replaced in version 1.2.0 by [Access-Methods](Access-Methods.md)

## Token types ##
Each leg does have 2 attributes of the type 'Token': **assetAccessData** and **ticket**.  

The assetAccessData should be filled with data to get access to an asset/open it, the ticket attribute is for inspection. If the ticket attribute is missing and inspection is required, the assetAccessData object should be shown. The ticket attribute is only needed when those 2 are different.  

## TokenType ##
The token type is an enumeration, that is not yet solidified. Possible candidates for this enumeration are: 
* QR_CODE
* AZTEC
* BARCODE
* DEEPLINK
* PDF
* HTML

In case of the deeplink the tokenData field should contain an URI, otherwise it should contain a representation of the access information.

```
ticket	{
  description: The MaaS user's proof of their right to travel on this leg
  validFrom*	string($date-time)
  validUntil*	string($date-time)
  tokenType*	string
  tokenData*	{...}
},
assetAccessData	{
  description: Data to open a specific asset (e.g. QR code, image base64)
  validFrom*	string($date-time)
  validUntil*	string($date-time)
  tokenType*	string
  tokenData*	{...}
}
```

## Distribution of access information ##
These attributes of the Leg object can be filled in by the TO, at 3 different moments in the process. This depends on the TO's process.  
* The first moment is directly after committing the booking. In the returned booking/leg this information can be provided.  
* The second possibility is returning this information in the /legs/{id}/events - PREPARE event. In the returned booking/leg this information can be completed.  
* The third possibility is when assigning a specific asset to the leg. In some scenarios, the asset is assigned not at booking time, but at starting time of the leg. In that case, the assets access information is only transferable in the result of the /legs/{id}/events - ASSIGN_ASSET event.

How does the MP know at which moment you'll be delivering the access information? This is specified by the [ProcessIdentifiers](ProcessIdentifiers.md). 

* ACCESS_CODE_IN_BOOKING: The QR, PDF, etc can be found in the booking result -- not recommended; without commit providing access information.  
* ACCESS_CODE_IN_COMMIT_EVENT: The QR, PDF, etc can be found in the commit result  
* ACCESS_CODE_IN_PREPARE_EVENT: The QR, PDF, etc can be found in the trip execution - prepare result  
* ACCESS_CODE_IN_ASSIGN_ASSET_EVENT: The QR, PDF, etc can be found in the result. Assigning an asset directly delivers the access information (e.g. for opening lockers).