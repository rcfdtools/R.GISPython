## Estadísticos de una capa geográfica
Topics: 

A partir de una capa geográfica en formato shapefile o feature class dentro de una Geodatabase, obtener los estadísticos de un campo de atributos determinado y por comparación por filtrado en ArcGIS y QGIS.

### Objetivos

* 


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9+.
* QGIS 3.22.1+.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda. 
* Sistema operativo Microsoft Windows.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en `D:\R.GISPython\LayerStatistic\`. 


### Caso de estudio

Para el desar


### Estadísticos en capas geográficas [^1]

| Estadístico | Descripción                                                                                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUM         | Adds the total value for the specified field.                                                                                                                 |
| MEAN        | Calculates the average for the specified field.                                                                                                               |
| MIN         | Finds the smallest value for all records of the specified field.                                                                                              |
| MAX         | Finds the largest value for all records of the specified field.                                                                                               |
| RANGE       | Finds the range of values (MAX minus MIN) for the specified field.                                                                                            |
| STD         | Finds the standard deviation on values in the specified field.                                                                                                |
| COUNT       | Finds the number of values included in statistical calculations. This counts each value except null values. To determine the number of null values in a field |
| FIRST       | Finds the first record in the Input Table and uses its specified field value.                                                                                 |
| LAST        | Finds the last record in the Input Table and uses its specified field value.                                                                                  |





### Referencias




[^1]: https://pro.arcgis.com/en/pro-app/2.8/tool-reference/analysis/summary-statistics.htm