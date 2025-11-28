## Link details

* The 'href' should always countain the complete URL, including path and query parameters. These URLs can also contain deeplinks!
* the 'rel' normally contains the collection name or the process name. If you want to publish more information, like a link to a policy zone in MDS, you must use an intuitive relation name. These names are free to choose, but be aware of the fact that they might be shown in the user facing application.
* headers should be specified only if it is necessary to have them (e.g. for authorization, if you haven't agreed on any other method to settle this)

```json
{
  "href": "https://example.com/tomp/v2/collections/travel-documents/items?packageId=342",
  "rel": "travel-documents",
  "type": "application/pdf",
  "method": "GET",
  "description": "get your ticket",
  "headers": { "Authorization": "Bearer 238492384983242" },
  "availableFrom": "2025-10-12T11:15:00"
}
```