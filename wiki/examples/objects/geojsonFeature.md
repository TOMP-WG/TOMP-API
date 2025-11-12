```json
{
  "type": "Feature",
  "properties": {
    "type": "leg",
    "id": "DBC:Leg:432903:1",
    "specification": { "from": "GPS:52.342,37.342", "startTime": "2025-08-30T10:15:00Z" }
  },
  "id": "432903:1",
  "geometry": {
    "type": "LineString", "geometry": [[]]
  },
  "links": [
    {
      "href": "https://example.com/v1/tomp/processes/start-leg/execution",
      "rel": "start-leg",
      "type": "application/geo+json",
      "method": "POST",
      "description": "start the leg",
      "body": { "inputs": { "package": "DBC:432903", "leg": "1" } }
    },
    {
      "href": "https://example.com/v1/tomp/processes/assign-ancillary/execution",
      "rel": "assign-ancillary",
      "type": "application/geo+json",
      "method": "POST",
      "description": "Add a helmet",
      "body": { "inputs": { "package": "DBC:432903", "leg": "1", "ancillary": "DBC:anc:default-helmet" } }
    }
  ]
}
```
Note: the reference "DBC:anc" should be available in the 'datasources' endpoint, which references machine and/or human readable resources with details about the ancillary products of DBC.

