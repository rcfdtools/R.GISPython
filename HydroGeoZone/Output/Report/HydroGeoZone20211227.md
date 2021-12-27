## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python

* Compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro
* Python versión: 3.7.11 [MSC v.1927 64 bit (AMD64)]
* Python rutas: ['D:\\R.GISPython\\HydroGeoZone', 'C:\\Program Files\\ArcGIS\\Pro\\Resources\\ArcPy', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python37.zip']
* matplotlib versión: 3.4.2
* Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License
* Créditos: r.cfdtools@gmail.com

Fecha y hora de inicio de ejecución: 2021-12-27 16:00:01.301841

### Propiedades y entidades encontradas para las capas de entrada

#### Campos en D:/R.GISPython/HydroGeoZone/Data/Zonificacion_hidrografica_2013.shp (Polygons 316)

| # | Campo | Tipo |
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


#### Campos en D:/R.GISPython/HydroGeoZone/Data/Drenaje_Sencillo.shp (Polylines 426719)

| # | Campo | Tipo |
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

#### Evaluación de drenajes por subtipo
> (0 - Sin asignación, 5101 - Permanente, 5102 - Intermitente)

| Código | # Drenajes |
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
