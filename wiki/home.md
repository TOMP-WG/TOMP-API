# TOMP-API

Welcome to the TOMP-API wiki pages. In this wiki you will find all detailed information about all the modules, endpoints and concepts used in the TOMP-API, but be aware of the fact that you'll probably only need a small selection of it.

To help you selecting the right part(s), we have described the functionality in the blueprints per mode, you can find them in the 'documents' section of this GitHub.

Secondly, we have created some tooling to cherrypick your required functionality into a single specification file. And, since it conforms to the OGC API specifications, you can extend it with the `discovery` module, to make it discoverable and reusable, showing what you have implemented.

## Quick start guide

> a. read the 'intro' blueprint  
> b. read the blueprint of your mode  
> c. get a copy of this wiki on your machine (zip or clone)  
> d. run the 'merge-API.ps1' file (powershell, windows) and follow the instructions. When you have read the blueprints, it will become clear which modules you need to select.  
> e. the result will be a TOMP-API.yaml file, but it contains all endpoints of the selected modules. You need to run a python script ( in /tools/filter_endpoints) to only select the appropriate endpoints for your way of doing business. The result will be a TOMP-API-filtered.yaml. This yaml file is tailor made for your needs.

## Quick start Discovery & Reuse

> a. In the generic quick start guide, you should have selected 'discovery module: y'. Otherwise, redo the process.  
> b. The discovery module complies to the OGC API Core, displaying meta data, but this meta-data can be derived from the specification.  
> c. To do so, use the python tool that can be found in /tools/create_meta_data. It will create the necessary output (machine readable only) for the required discovery endpoints.  
> d. Be aware of the fact that you still need to create the human readable variant (.html).

## General structure

In general, we have only a few structures in the TOMP-API, fully OGC API compliant. We have:  
### __Collections__  
These type of endpoints always deliver GeoJSON, although there are a few in there without geometries. But it always has this structure:
```json
{ 
  "type": "FeatureCollection", 
  "features": [ { "type": "Feature", 
                  "geometry": { ... }, 
                  "properties": {
                     "type": "real type of the feature, like a leg, zone, etc", 
                     ...
                  } 
                } ],
  "properties": { "type": "real type of the collection, like offers",
                  ... },
  "links": [ ... ]
}
```
Sometimes there are a few more attributes on the root level, indicating the number of features available and returned (to support paging).

The URL of the collections is always /collections/[collection name]/items, and it can be retrieved with an HTTP GET. In most cases, query parameters are applicable, like a package-reference.

The meta-data (when activate the discovery module) can be found when calling GET /collections/[collection name].

Example collections:
```http 
-- retrieve assets (like seats or bikes) available for a package
GET /collections/assets/items?package=34d531e2-05fc-4c25-9bcc-eef60156a860

-- retrieve a single package, including all details
GET /collections/packages/items?package=34d531e2-05fc-4c25-9bcc-eef60156a860
```

### __Processes__  
These endpoints always have the same output structure: a [package](./objects/package.md). The only exception is when searching for offers, in that case, you'll get a list of offers. But in all cases, the output is a (implementation of) GeoJSON. An example of a package can be found at the package-page.

The URL is formatted like this: /processes/[process name]/execution, and  the meta-data (when using the discovery module) must be available when calling GET /processes/[process name]. A [process name] normally consists out of a verb and a noun, like 'search-offers', or 'start-leg'.

Example process call:
```http 
POST /processes/start-leg/execution 
body: { "package": "2026a8ff-d4af-4e09-bb6d-1394628ae217"
      , "leg": "7c8f2603-f87f-487d-8f36-7a4c3cd81852" }
```

It returns a package:
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "type": "leg"
      },
      "id": "5d260584-9f78-4204-884b-3dd899a68f57",
      "geometry": { "type": "LineString", "coordinates": [ ... ] },
      "links": []
    }
  ],
  "properties": {
    "type": "offer",
    "id": "aff11b01-c888-44ff-b6f5-d0aed162f605",
    "status": "OFFERED",
    "summary": {
      "id": "aff11b01-c888-44ff-b6f5-d0aed162f605",
      "specification": { "type": "travelSpecification", "from": "GPS:52.342392,41.43i4234" },
      "price": { "amount": 5.54, "currencyCode": "EUR" }
    },
    "price": {
      "amount": 5.54,
      "taxPercentageUsed": 21,
      "currencyCode": "EUR",
      "elements": [
        { "amount": 3.14, "type": "FIXED" },
        { "amount": 2.40, "type": "FLEX", "units": "HRS", "amountOfUnits": 0.5 } ],
      "description": "Estimated price for half an hour of usage"
    }
  }
}
```

## Modules

A brief summary of the modules can be found here: [modules](modules.md), but also in the intro blueprint. It must be clear that not all modules need to be implemented, only use what's appropriate for you. For instance, if you only want to use it in a peer-2-peer solution, you probably won't implement the discovery module.