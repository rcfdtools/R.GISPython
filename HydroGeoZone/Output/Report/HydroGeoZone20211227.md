# Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python

* Compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro
* Python versión: 3.7.11 [MSC v.1927 64 bit (AMD64)]
* Python rutas: ['D:\\R.GISPython\\HydroGeoZone', 'C:\\Program Files\\ArcGIS\\Pro\\Resources\\ArcPy', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python37.zip']
* matplotlib versión: 3.4.2
* Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License
* Créditos: r.cfdtools@gmail.com

Fecha y hora de inicio de ejecución: 2021-12-27 16:22:26.739463

Sistema de coordenadas: PROJCS['MAGNA-SIRGAS / Origen-Nacional',GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',5000000.0],PARAMETER['False_Northing',2000000.0],PARAMETER['Central_Meridian',-73.0],PARAMETER['Scale_Factor',0.9992],PARAMETER['Latitude_Of_Origin',4.0],UNIT['Meter',1.0]] # GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]

## Propiedades y entidades encontradas para las capas de entrada

### Campos en D:/R.GISPython/HydroGeoZone/Data/Zonificacion_hidrografica_2013.shp (Polygons 316)

| # | Campo | Tipo |
|---|---|---|
| 1 | FID | OID |
| 2 | Shape | Geometry |
| 3 | OBJECTID_1 | Integer |
| 4 | COD_AH | SmallInteger |
| 5 | COD_ZH | SmallInteger |
| 6 | COD_SZH | SmallInteger |
| 7 | NOM_AH | String |
| 8 | NOM_ZH | String |
| 9 | NOM_SZH | String |
| 10 | Shape_Leng | Double |
| 11 | Shape_Area | Double |
| 12 | RULEID | Integer |


### Campos en D:/R.GISPython/HydroGeoZone/Data/Drenaje_Sencillo.shp (Polylines 426719)

| # | Campo | Tipo |
|---|---|---|
| 1 | FID | OID |
| 2 | Shape | Geometry |
| 3 | OBJECTID | Integer |
| 4 | NOMBRE_GEO | String |
| 5 | ESTADO_DRE | Integer |
| 6 | PROYECTO | String |
| 7 | SYMBOL | String |
| 8 | FECHA | Date |
| 9 | DISPERSION | String |
| 10 | RULEID | Integer |
| 11 | PK_CUE | Double |
| 12 | GLOBALID | String |
| 13 | SHAPE_Leng | Double |
| 14 | LDre | Double |

### Evaluación de drenajes por subtipo

> (0 - Sin asignación, 5101 - Permanente, 5102 - Intermitente)

| Código | # Drenajes |
|---|---|---|
| 0 | 140 |
| 5101 | 421909 |
| 5102 | 4670 |

### Total nacional de SZH - subzonas hidrográficas por rango de área

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 9 | 9 |
| 300-700 | 19 | 28 |
| 700-900 | 16 | 44 |
| 900-1100 | 18 | 62 |
| 1100-1300 | 18 | 80 |
| 1300-1500 | 11 | 91 |
| 1500-2000 | 34 | 125 |
| 2000-2500 | 29 | 154 |
| 2500-3500 | 40 | 194 |
| 3500-5000 | 45 | 239 |
| 5000-10000 | 60 | 299 |
| 10000-20000 | 14 | 313 |
| 20000-999999 | 1 | 314 |

### SZH - subzonas hidrográficas por rango de área para cada AH - área hidrográfica


#### AH - Área hidrográfica 1 - Caribe

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 3 | 3 |
| 300-700 | 3 | 6 |
| 700-900 | 2 | 8 |
| 900-1100 | 4 | 12 |
| 1100-1300 | 3 | 15 |
| 1300-1500 | 3 | 18 |
| 1500-2000 | 9 | 27 |
| 2000-2500 | 3 | 30 |
| 2500-3500 | 8 | 38 |
| 3500-5000 | 3 | 41 |
| 5000-10000 | 5 | 46 |
| 10000-20000 | 0 | 46 |
| 20000-999999 | 0 | 46 |

#### AH - Área hidrográfica 2 - Magdalena Cauca

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 4 | 4 |
| 300-700 | 13 | 17 |
| 700-900 | 7 | 24 |
| 900-1100 | 9 | 33 |
| 1100-1300 | 10 | 43 |
| 1300-1500 | 7 | 50 |
| 1500-2000 | 10 | 60 |
| 2000-2500 | 7 | 67 |
| 2500-3500 | 14 | 81 |
| 3500-5000 | 9 | 90 |
| 5000-10000 | 14 | 104 |
| 10000-20000 | 1 | 105 |
| 20000-999999 | 0 | 105 |

#### AH - Área hidrográfica 3 - Orinoco

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 2 | 2 |
| 300-700 | 0 | 2 |
| 700-900 | 2 | 4 |
| 900-1100 | 2 | 6 |
| 1100-1300 | 3 | 9 |
| 1300-1500 | 1 | 10 |
| 1500-2000 | 8 | 18 |
| 2000-2500 | 7 | 25 |
| 2500-3500 | 5 | 30 |
| 3500-5000 | 16 | 46 |
| 5000-10000 | 21 | 67 |
| 10000-20000 | 6 | 73 |
| 20000-999999 | 0 | 73 |

#### AH - Área hidrográfica 4 - Amazonas

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 0 | 0 |
| 300-700 | 1 | 1 |
| 700-900 | 0 | 1 |
| 900-1100 | 1 | 2 |
| 1100-1300 | 1 | 3 |
| 1300-1500 | 0 | 3 |
| 1500-2000 | 4 | 7 |
| 2000-2500 | 6 | 13 |
| 2500-3500 | 7 | 20 |
| 3500-5000 | 9 | 29 |
| 5000-10000 | 20 | 49 |
| 10000-20000 | 7 | 56 |
| 20000-999999 | 1 | 57 |

#### AH - Área hidrográfica 5 - Pacifico

| Rango km² | # Subzonas | Acumulado |
|---|---|---|
| 0-300 | 0 | 0 |
| 300-700 | 2 | 2 |
| 700-900 | 5 | 7 |
| 900-1100 | 2 | 9 |
| 1100-1300 | 1 | 10 |
| 1300-1500 | 0 | 10 |
| 1500-2000 | 3 | 13 |
| 2000-2500 | 6 | 19 |
| 2500-3500 | 6 | 25 |
| 3500-5000 | 8 | 33 |
| 5000-10000 | 0 | 33 |
| 10000-20000 | 0 | 33 |
| 20000-999999 | 0 | 33 |
