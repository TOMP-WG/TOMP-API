# processList

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `processes` | array[[processSummary](processSummary.md)] | ✓ |  |
| `links` | array[[link](link.md)] | ✓ |  |

## Detailed Properties

- **`processes`**  *(array[[processSummary](processSummary.md)])* - **required**  

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

## Example

```json
{
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
  "processes": [
    {
      "title": "example-string",
      "description": "example-string",
      "keywords": [
        "example-string",
        "example-string"
      ],
      "id": "identifier",
      "version": "example-string",
      "jobControlOptions": [
        "sync-execute",
        "sync-execute"
      ],
      "outputTransmission": [
        "value",
        "value"
      ],
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
      ]
    },
    {
      "title": "example-string",
      "description": "example-string",
      "keywords": [
        "example-string",
        "example-string"
      ],
      "id": "identifier",
      "version": "example-string",
      "jobControlOptions": [
        "sync-execute",
        "sync-execute"
      ],
      "outputTransmission": [
        "value",
        "value"
      ],
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
      ]
    }
  ]
}
```

