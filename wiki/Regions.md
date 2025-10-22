[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Regions](Regions.md) 

The region endpoint returns a list of regions. Each region is described by an id (self generated or descriptive), a name and a polygon. __The polygon MUST be closed__. This means the last and the first point in the polygon must be the same.

| field | required | description |
| ----- | -------- | ----------- | 
| regionId | * | Unique identifier for this region. |
| name | * | Public name for this region, matches Content-Language (see [Information](Information.md)) |
| serviceArea | * | geojsonPolygon: geojson representation of a polygon. The first and the last point must be equal. See also https://geojson.org/geojson-spec.html#polygon and example https://geojson.org/geojson-spec.html#id4 |
| type |  | Since 1.3.0. See [#384](https://github.com/TOMP-WG/TOMP-API/issues/384). the type of area. Default this is 'OPERATING', but other areas can be published here as well. Before 1.3.0, it was only allowed to communicate OPERATING areas. Therefore, when it is omitted, it should be assumed it is 'OPERATING'  |