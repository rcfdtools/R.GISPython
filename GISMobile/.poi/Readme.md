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
          "coordinates": [-96, 16]
        },
		{
          "type": "Point",
          "properties": {"prop0": "value0"},
          "coordinates": [-96, -58]
        }		
      ]
    }
  }
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