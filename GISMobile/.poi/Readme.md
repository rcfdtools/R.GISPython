## Puntos de interés - POI

Localización de puntos de interés en GISMobile.


### GIF sample

![GISMobile](7/PXL_20230503_184310359.TS.gif)


### Point sample

```geojson
{
  "type": "Feature",
  "geometry": {
    "type": "Point", 
    "coordinates": [-73.72825833333333, 4.537927777777778]
  }, 
  "properties": {
    "Name:": "Tunel derivador Río Guatiquía a Embalse Chuza",
    "Localización:": "Chingaza" 
  }
}
```

```topojson
{
  "type": "Topology",
  "transform": {
    "scale": [0.0005000500050005, 0.00010001000100010001],
    "translate": [100, 0]
  },
  "objects": {
    "example": {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "properties": {"prop0": "value0"},
          "coordinates": [4000, 5000]
        },
        {
          "type": "LineString",
          "properties": {"prop0": "value0", "prop1": 0},
          "arcs": [0]
        },
        {
          "type": "Polygon",
          "properties": {"prop0": "value0",
            "prop1": {"this": "that"}
          },
          "arcs": [[1]]
        }
      ]
    }
  },
  "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]
}
```


### Polygon sample

```
longitud 96W, 25W
latitud 16N, 58S
```

```geojson
{
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-96, 16],
                [-96, -58],
                [-25, -58],
                [-25, 16]
            ]
        ]
    }
}
```

### Referencias

* https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams