# landingPage

a complete endpoint description, containing all endpoints, their status, but also the served scenarios and implemented process flows. The identifiers for the process flows can be found at https://github.com/TOMP-WG/TOMP-API/wiki/ProcessIdentifiers<br>

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | ✓ |  |
| `description` | string | ✓ |  |
| `links` | array[[link](link.md)] | ✓ |  |
| `processIdentifiers` | array[[processIdentifier](processIdentifier.md)] |  | an array with 'care labels', indiacting how this implementation wants to be t... |

## Detailed Properties

- **`title`**  *(string)* - **required**  

- **`description`**  *(string)* - **required**  

- **`links`**  *(array[[link](link.md)])* - **required**  
  **Array item properties:**
  - **`rel`**  *(string)* - **required**  
    the action that can be performed OR part of the URI allowed values include the 'processId's, prefixes for the referenced data sources, prefixes for deeplinks ('apple' and 'android'), OGC compliant ones (alternative, next, etc)
  - **`href`**  *(string (uri))* - **required**  
    valid URL
  - **`type`**  *(string)* - optional  
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
  - **`expires`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)
  - **`availableFrom`**  *(string (date-time))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, date-time (2019-10-12T07:20:50.52Z)

- **`processIdentifiers`**  *(array[[processIdentifier](processIdentifier.md)])* - optional  
  an array with 'care labels', indiacting how this implementation wants to be treated.
  **Array item properties:**
  - **`module`**  *(enum (`offers`, `pre-sales`, `purchase`, `execute`, `support`, ...))* - **required**  
  - **`identifiers`**  *(array[string])* - **required**  

## Additional Properties

❌ No additional properties are allowed.

## Example

```json
{
  "title": "example-string",
  "description": "example-string",
  "links": [
    {
      "href": "https://example.com",
      "rel": "example-string",
      "type": "example-string",
      "method": "POST",
      "description": "example-string"
    },
    {
      "href": "https://example.com",
      "rel": "example-string",
      "type": "example-string",
      "method": "POST",
      "description": "example-string"
    }
  ],
  "processIdentifiers": [
    {
      "module": "offers",
      "identifiers": []
    },
    {
      "module": "offers",
      "identifiers": []
    }
  ]
}
```

