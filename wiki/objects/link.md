# link

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `rel` | string | ✓ | the action that can be performed OR part of the URI allowed values include th... |
| `href` | [url](url.md) | ✓ | valid URL |
| `type` | [shortString](shortString.md) |  | allowed values are described by IANA, ("application/geo+json") |
| `method` | enum (`POST`, `GET`, `DELETE`, `PATCH`) |  | to indicate the http method. |
| `description` | string |  | the description of the external data source |
| `body` | object |  | the (prefilled) body for the request |
| `headers` | object |  |  |
| `mandatory` | boolean |  | is this link informative, or must it be used? |
| `hash` | string |  | to validate that the content of the link hasn`t been changed. |
| `expires` | [dateTime](dateTime.md) |  | https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:... |
| `availableFrom` | [dateTime](dateTime.md) |  | https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:... |

## Detailed Properties

- **`rel`**  *(string)* - **required**  
  the action that can be performed OR part of the URI allowed values include the 'processId's, prefixes for the referenced data sources, prefixes for deeplinks ('apple' and 'android'), OGC compliant ones (alternative, next, etc)

- **`href`**  *([url](url.md))* - **required**  
  valid URL

- **`type`**  *([shortString](shortString.md))* - optional  
  allowed values are described by IANA, ("application/geo+json")

- **`method`**  *(enum (`POST`, `GET`, `DELETE`, `PATCH`))* - optional  
  to indicate the http method.
default: `GET`

- **`description`**  *(string)* - optional  
  the description of the external data source

- **`body`**  *(object)* - optional  
  the (prefilled) body for the request

- **`headers`**  *(object)* - optional  

- **`mandatory`**  *(boolean)* - optional  
  is this link informative, or must it be used?

- **`hash`**  *(string)* - optional  
  to validate that the content of the link hasn`t been changed.

- **`expires`**  *([dateTime](dateTime.md))* - optional  
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

- **`availableFrom`**  *([dateTime](dateTime.md))* - optional  
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

## Additional Properties

❌ No additional properties are allowed.

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
```## Example

```json
{
  "href": "https://example.com/tomp/v2/end-leg/execution",
  "rel": "end-leg",
  "type": "application/geo+json",
  "method": "POST",
  "body": { "inputs": { "package": "7645e96a-efce-4e87-b665-2a96b93f013b", "leg": "c25f3f81-acdc-4427-9982-fa23e6971aca" } }
}
```