applies to: [v2.0](v2.0.md) and beyond

# External references
In requests and responses external references can be used, like to a NeTEx bus stop, a GBFS bike or station, or in any other format.  
This can be done using a strict, prescribed _**format**_ and a _**link**_, a clear reference to the source.

# Identifier format
The external references can be applied anywhere in fields named 'id', ending with 'id', or 'reference'. The format itself is like this (example):
`DKR:station:3942`. Without any context, it is not clear what this means.  

The format itself should comply to [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). The regex format is `^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?`

Semantically seen: 
- the first part references to an organisation (if applicable),
- the second part to the concept,
- and the last part is a unique identifier within the referenced data source

A few examples to make it easier to understand:
- _MYW:vehicle:349-34289_ - a vehicle from an organisation (using the abbreviation MYW), identified by 349-34289.
- _ARR:ScheduledStopPoint:10000032#OAN:P799_ - a scheduled stop point from an organisation (using the abbreviation ARR), identified by 10000032#OAN:P799.

# Link
The context of these identifiers will be clarified by 'link objects'. These can be found in the 'landing page' (OGC complient, accessible with a GET on the root `GET /`), but we extended it with some additional properties. One of these properties is 'dataSources', containing the context of these identifiers.
 
The dataSources field is an array of external links, derived from [JSON API linked objects](https://jsonapi.org/format/#auto-id--link-objects). 

> A “link object” is an object that represents a [web link](https://tools.ietf.org/html/rfc8288).  
>
> A link object MUST contain the following member:  
> **href**: a string whose value is a URI-reference [[RFC3986 Section 4.1](https://tools.ietf.org/html/rfc3986#section-4.1)] pointing to the link’s target.   
> **rel**: a string indicating the link’s relation type. The string MUST be a [valid link relation type](https://tools.ietf.org/html/rfc8288#section-2.1). This includes [RFC 8228 section 2.1.2](https://httpwg.org/specs/rfc8288.html#rfc.section.2.1.2), which allows to have 'custom' semantical labels.    
> **type**: a string indicating the media type of the link’s target. These types are preferably registered at IANA.  

_**OPTIONAL**_
> A link object MAY also contain any of the following members:  
>   **title**: a string which serves as a label for the destination of a link such that it can be used as a human-readable identifier (e.g., a menu entry).  
>   **describedby**: a [link](https://jsonapi.org/format/#document-links-link) to a description document (e.g. OpenAPI or JSON Schema) for the link target.  
>   **hreflang**: a string or an array of strings indicating the language(s) of the link’s target. An array of strings indicates that the link’s target is available in multiple languages. Each string MUST be a valid language tag [[RFC5646](https://tools.ietf.org/html/rfc5646)].  
>   **meta**: a meta object containing non-standard meta-information about the link.

A few examples of referenced data sets:
- { "rel": "NB:vehicle_types": "href": "https://www.nextbike.ba/bs/vehicle_types.json", "type": "application/gbfs+json" }
- { "rel": "ARR:NeTEx": "href": "https://data.ndovloket.nl/netex/arr/NeTEx_ARR_NL_20240903_20240904_1420.xml.gz", "type": "application/netex+gzip" }

# Using links in results
This approach is pretty straight forward, but we had the idea to use these links not only as references to data, but also to use it to formalise the 'possible operations' on each offer, package, leg or purchased product.

Therefore we looked at several solutions, but none of them suits our needs [RFC 9264](https://www.rfc-editor.org/rfc/rfc9264), [HAL](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-00), [JSON-LD](https://www.w3.org/TR/json-ld11/) nor [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS).

Finally, we took the liberty to modify this 'linked objects' approach, but added some additional fields to cope with operations:
> **method**: required, a HTTP method, like POST, GET, PATCH [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-method-definitions)   
> **description**: a free format text, containing a description of the data source or operation  
> **body**: a template request body (JSON) to supply with the POST/PUT/PATCH and so on  
> **headers**: a list of key-value pairs to be used in the request  
> **parameters**: a list of key-value pairs to be used in the request, but these can be added in the href as well, when not templated  
> **required**: list of attributes in the body and header that must be completed before sending it [JSON path](https://en.wikipedia.org/wiki/JSONPath).

A few examples of operations:  
- { "rel": "details", "href": "https://some.url/product_details.html", "method": "GET", "type": "text/html" } - just provide a human readable URL with details
- { "rel": "getTicketOffers", "href": "[https://some.url/tomp/v2/collections/offers/items?validity={'type':'PRODUCT', 'product': 'ARR:Product:BRABANTLINER'}](https://test.html)", "method": "GET", "type": "application/geo+json" } - a 'bootstrap' link, could be provided in the 'links' set of the landing page.
- { "rel": "purchase", "href": "https://some.url/tomp/v2/collections/offers/items?operation=purchase&packageId=42934", "method", "POST", "type": "application/geo+json", "body": { "customerId": "" }, "required": [ "$.customerId" ] } - a link that is supplied in the offers, on offer 42934. Only the customerId is required to be filled in, and the body can be send to the specified URL.

