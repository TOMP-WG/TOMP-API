# extent

The extent of the features in the collection. In the Core only spatial and temporal
extents are specified. Extensions may add additional members to represent other
extents, for example, thermal or pressure ranges.

**Type:** `object`

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `spatial` | object |  | The spatial extent of the features in the collection. |
| `temporal` | object |  | The temporal extent of the features in the collection. |

## Detailed Properties

- **`spatial`**  *(object)* - optional  
  The spatial extent of the features in the collection.
  - **`bbox`**  *(array[array[number]])* - optional  
    One or more bounding boxes that describe the spatial extent of the dataset.
In the Core only a single bounding box is supported. Extensions may support
additional areas. If multiple areas are provided, the union of the bounding
boxes describes the spatial extent.
  - **`crs`**  *(enum (`http://www.opengis.net/def/crs/OGC/1.3/CRS84`))* - optional  
    Coordinate reference system of the coordinates in the spatial extent
(property `bbox`). The default reference system is WGS 84 longitude/latitude.
In the Core this is the only supported coordinate reference system.
Extensions may support additional coordinate reference systems and add
additional enum values.
default: `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

- **`temporal`**  *(object)* - optional  
  The temporal extent of the features in the collection.
  - **`interval`**  *(array[array[string (date-time)]])* - optional  
    One or more time intervals that describe the temporal extent of the dataset.
The value `null` is supported and indicates an unbounded interval end.
In the Core only a single time interval is supported. Extensions may support
multiple intervals. If multiple intervals are provided, the union of the
intervals describes the temporal extent.
  - **`trs`**  *(enum (`http://www.opengis.net/def/uom/ISO-8601/0/Gregorian`))* - optional  
    Coordinate reference system of the coordinates in the temporal extent
(property `interval`). The default reference system is the Gregorian calendar.
In the Core this is the only supported temporal coordinate reference system.
Extensions may support additional temporal coordinate reference systems and add
additional enum values.
default: `http://www.opengis.net/def/uom/ISO-8601/0/Gregorian`

## Example

```json
{
  "spatial": {
    "bbox": [
      []
    ],
    "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
  },
  "temporal": {
    "interval": [
      []
    ],
    "trs": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
  }
}
```