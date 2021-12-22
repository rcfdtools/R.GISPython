## Estadísticos de capas geográficas
Topics: 

A partir de una capa geográfica en formato shapefile o feature class dentro de una Geodatabase, obtener los estadísticos de un campo de atributos determinado y por comparación por filtrado en ArcGIS y QGIS.


### Objetivos

* Seleccionar una capa, definir el atributo y valor de corte a analizar.
* Obtener los estadísticos generales de la capa seleccionada sin y con filtrado.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9+.
* QGIS 3.22.1+.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda. 
* Sistema operativo Microsoft Windows.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\LayerStatistic\`. 


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM - Colombia](http://www.ideam.gov.co/) localizadas sobre varios Departamentos de la zona central del país.


### Estadísticos en capas geográficas vectoriales sobre ArcGIS [^1]

| Estadístico | Descripción                                                                                                                                                   | Desktop | Pro |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----|
| SUM         | Adds the total value for the specified field.                                                                                                                 | [ X ]   | Yes |
| MEAN        | Calculates the average for the specified field.                                                                                                               | Yes     | Yes |
| MIN         | Finds the smallest value for all records of the specified field.                                                                                              | Yes     | Yes |
| MAX         | Finds the largest value for all records of the specified field.                                                                                               | Yes     | Yes |
| RANGE       | Finds the range of values (MAX minus MIN) for the specified field.                                                                                            | Yes     | Yes |
| STD         | Finds the standard deviation on values in the specified field.                                                                                                | Yes     | Yes |
| COUNT       | Finds the number of values included in statistical calculations. This counts each value except null values. To determine the number of null values in a field | Yes     | Yes |
| FIRST       | Finds the first record in the Input Table and uses its specified field value.                                                                                 | Yes     | Yes |
| LAST        | Finds the last record in the Input Table and uses its specified field value.                                                                                  | Yes     | Yes |
| MEDIAN      | The median for all records of the specified field will be calculated.                                                                                         | No      | Yes |
| VARIANCE    | The variance for all records of the specified field will be calculated.                                                                                       | No      | Yes |
| UNIQUE      | The number of unique values of the specified field will be counted.                                                                                           | No      | Yes |

> Atención: para la ejecución correcta de los sripts se recomienda cerrar sus aplicativos GIS. Para garantizar la compatibilidad con la versión Desktop de ArcGIS, no se han incluido los estadísticos `MEDIAN`, `VARIANCE` y `UNIQUE`.

### Estadísticos generales de una capa geográfica en ArcGIS for Desktop

script [LayerStatisticArcGIS.py](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/LayerStatisticArcGIS.py)

Explicación de instrucciones empleadas

![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png)
![Python2.7.5ArcGISDesktop10.2.2.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python2.7.5ArcGISDesktop10.2.2.png)




### Estadísticos de una capa geográfica con comparación por filtrado en ArcGIS

script LayerStatisticCompareArcGIS.py

Explicación de instrucciones empleadas


### Estadísticos de una capa geográfica con comparación por filtrado en QGIS

script LayerStatisticCompareQGIS3.py

Explicación de instrucciones empleadas


### Referencias



### Autores

* Creado por [r.cfdtools](r.cfdtools@gmail.com) (16h).


### Compatibilidad

* Compatible con ArcGIS for Desktop, ArcGIS Pro y QGIS 3+.


### Control de versiones

| Versión    | Descripción                                                                                                                           |
|------------|---------------------------------------------------------------------------------------------------------------------------------------|
| v.20211220 | Versión inicial.                                                                                                                      |
| v.20211221 | Documentación y pruebas funcionales en ArcGIS Pro. Inclusión de rutas absolutas para compatiblidad con Jupyter y ArcGIS Pro Notebook. |


### Licencia, cláusulas y condiciones de uso

R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]()     |
|------------------------|---------------------------------------------------------|-----------------------------|


[^1]: https://pro.arcgis.com/en/pro-app/2.8/tool-reference/analysis/summary-statistics.htm