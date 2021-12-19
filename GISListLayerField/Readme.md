## Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos

En actividad contiene script en Python que permite listar todas las capas geográficas (en formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm)) disponibles en el directorio de datos local de un proyecto de ArcGIS o en las capas cargadas en un mapa de QGIS, consultar los atributos disponibles en cada capa, sus tipos, filtrar a partir de un campo específico y graficar los valores encontrados a partir de la definición de dos campos específicos.


### Objetivos

* Utilizar el núcleo y las funciones [ArcPy](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/what-is-arcpy-.htm) de ESRI ArcGIS for Desktop y ArcGIS Pro.
* Utilizar el núcleo y las funciones `PyQGIS` de QGIS.
* Listar las capas y atributos contenidos en el directorio de datos de un proyecto geográfico.
* Representar gráficamente los datos contenidos en la tabla de atributos de las capas geográficas.


### ¿Qué es ArcPy y PyQGIS?

ArcPy y PyQGIS son paquete de Python para ArcGIS y QGIS que contiene gran variedad de funciones para análisis  espacial, conversión de datos, administración y automatización de tareas geográficas. En un script o en un Notebook de ArcGIS Pro o en QGIS, ingresando `arcpy.` o `qgis.` más una letra o palabra clave, el usuario obtendrá una lista desplegable con las propiedades y métodos disponibles y podrá de forma rápida seleccionar alguna de ellas para ser insertada en el código o para conocer sus parámetros. [ArcPy + información. ](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/what-is-arcpy-.htm). [PyQGIS + información. ](https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html)


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM](http://www.ideam.gov.co/) - Colombia localizadas sobre varios Departamentos de la zona central del país.


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* QGIS 3.22.1+.
* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.
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

> Tenga en cuenca que los datos utilizados pueden estar desactualizados y solamente se utilizan como recurso para ejemplificar esta actividad.  


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se almacenen en D:\R.GISPython\GISListLayerField\


### Scripts

* Script GISListLayerFieldArcGIS.py
* Script GISListLayerFieldArcGIS.py


### Descripción instrucciones y comandos empleados

| Instrucción | Explicación                |
|-------------|----------------------------|
| #           | Comentario de una línea.   |


### Ejecución en Pycharm


### Ejecución en ArcGIS for Desktop


### Ejecución en ArcGIS Pro


# Ejecución en QGIS


### Referencias

* https://pro.arcgis.com/es/pro-app/arcpy/functions/listfields.htm
* https://pro.arcgis.com/es/pro-app/arcpy/classes/field.htm
* https://pro.arcgis.com/es/pro-app/tool-reference/data-management/get-count.htm
* https://community.esri.com/thread/36300
* https://pro.arcgis.com/es/pro-app/arcpy/functions/searchcursor.htm


### Autores

* Creado por r.cfdtools@gmail.com


### Compatibilidad

* Compatible con cualquier versión de Python.


### Tags
`Hydrology` `Stations` `Prepipitation` `Evaporation` `Temperature` `arcpy` `pyqgis` 'Metadata'


### Control de versiones

| Versión    | Descripción      |
|------------|------------------|
| v.20211219 | Versión inicial. |



### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]() |
|------------------------|------------|-------------------------|

