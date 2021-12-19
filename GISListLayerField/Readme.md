## Consulta de capas vectoriales, propiedades y atributos en proyectos geográficos

En esta actividad aprenderá a crear un script en Python que permita listar todas las capas disponibles en el directorio de datos local o en las capas cargadas en un proyecto de QGIS, consultar los atributos disponibles en cada capa y sus tipos, filtrar a partir de un campo específico y graficar los valores encontrados a partir de la definición de un campo específico.


### Objetivos

* Utilizar el núcleo de Python `arcpy` de ESRI ArcGIS for Desktop y ArcGIS Pro.
* Utilizar el núcleo de Python `pyqgis` de QGIS.
* Listar las capas y atributos contenidos en el directorio de datos de un proyecto geográfico.
* Representar gráficamente los datos contenidos en la tabla de atributos de las capas geográficas.


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM](http://www.ideam.gov.co/) - Colombia localizadas sobre varios Departamentos de la zona central del país.


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* QGIS 3.22.1+.
* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.
* Capa geográfica de Municipios de Colombia.
* Paquete de datos con archivos de formas [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm).


### Paquete de datos

En el directorio `/Datos`, se encuentran las siguientes capas geográficas en formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm) que han sido utilizadas para el desarrollo de esta actividad.

| Shapefile         | Descripción                                                                                                                                                                                                                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Departamentos.shp | Capa de Departamentos de Colombia - Suramérica. Construida a partir de la capa [IGAC](https://www.igac.gov.co/) de Municipios de Colombia - Suramérica.                                                                                                                                          |
| Estaciones.shp    | Estaciones hidrometeorológicas del [IDEAM](http://www.ideam.gov.co/) - Colombia localizadas sobre varios Departamentos de la zona central del país. Más información en la actividad Catálogo nacional de estaciones hidrometeorológicas del IDEAM - Colombia, descarga y análisis usando Python. |
| Precipitacion.shp | Estaciones con estadísticos mensuales multianuales de _Precipitación Mensual Total_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                   |
| Evaporacion.shp   | Estaciones con estadísticos mensuales multianuales de _Evaporación Mensual Total_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                                                               |
| Temperatura.shp   | Estaciones con estadísticos mensuales multianuales de _Temperatura del Aire Mensual Media_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                                                      |


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\GISListLayerField\


### Scripts en Python

* Script GISListLayerFieldArcGIS.py
* Script GISListLayerFieldArcGIS.py



