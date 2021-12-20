## Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos

En actividad contiene script en Python que permite listar todas las capas geográficas (en formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm)) disponibles en el directorio de datos local de un proyecto de ArcGIS o en las capas cargadas en un mapa de QGIS, consultar los atributos disponibles en cada capa, sus tipos, filtrar a partir de un campo específico y graficar los valores encontrados a partir de la definición de dos campos específicos.

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3Layer.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/GISListLayerField.png)

### Objetivos

* Utilizar el núcleo y las funciones [ArcPy](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/what-is-arcpy-.htm) de ESRI ArcGIS for Desktop y ArcGIS Pro.
* Utilizar el núcleo y las funciones [PyQGIS](https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html) de QGIS.
* Listar las capas y atributos contenidos en el directorio de datos de un proyecto geográfico.
* Representar gráficamente los datos contenidos en la tabla de atributos de las capas geográficas.


### ¿Qué es ArcPy y PyQGIS?

ArcPy y PyQGIS son paquete de Python para ArcGIS y QGIS que contiene gran variedad de funciones para análisis  espacial, conversión de datos, administración y automatización de tareas geográficas. En un script o en un Notebook de ArcGIS Pro o en QGIS, ingresando `arcpy.` o `qgis.` más una letra o palabra clave, el usuario obtendrá una lista desplegable con las propiedades y métodos disponibles y podrá de forma rápida seleccionar alguna de ellas para ser insertada en el código o para conocer sus parámetros. 


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM](http://www.ideam.gov.co/) - Colombia localizadas sobre varios Departamentos de la zona central del país.


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* QGIS 3.22.1+.
* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.
* Paquete [Datos.zip](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Datos/Datos.zip) con archivos de formas [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm).


### Paquete de datos

En el directorio `/Datos`, se encuentran las siguientes capas geográficas en formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm) que han sido utilizadas para el desarrollo de esta actividad.

| Shapefile         | Descripción                                                                                                                                                                                                                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Departamentos.shp | Capa de Departamentos de Colombia - Suramérica. Construida a partir de la capa [IGAC](https://www.igac.gov.co/) de Municipios de Colombia - Suramérica.                                                                                                                                          |
| Estaciones.shp    | Estaciones hidrometeorológicas del [IDEAM](http://www.ideam.gov.co/) - Colombia localizadas sobre varios Departamentos de la zona central del país. Más información en la actividad Catálogo nacional de estaciones hidrometeorológicas del IDEAM - Colombia, descarga y análisis usando Python. |
| Precipitacion.shp | Estaciones con estadísticos mensuales multianuales de _Precipitación Mensual Total_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                   |
| Evaporacion.shp   | Estaciones con estadísticos mensuales multianuales de _Evaporación Mensual Total_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                                                               |
| Temperatura.shp   | Estaciones con estadísticos mensuales multianuales de _Temperatura del Aire Mensual Media_ a partir de registros discretos del [IDEAM](http://www.ideam.gov.co/).                                                                                                                                                                                                      |

> Tenga en cuenta que los datos utilizados pueden estar desactualizados y solamente se utilizan como recurso para ejemplificar esta actividad.  


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

Ejecución usando Python 2.7.5 de ArcGIS for Desktop para todas las capas.
![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3All.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3All.png)

Ejecución usando Python 2.7.5 de ArcGIS for Desktop para una capa específica.
![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3Layer.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3Layer.png)

Ejecución usando Python 3.7.11 de ArcGIS Pro para todas las capas.
![Python3.7.11ArcGISPro2.9.0PyCharm2021.3All.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3All.png)

Ejecución usando Python 3.7.11 de ArcGIS Pro para una capa específica.
![Python3.7.11ArcGISPro2.9.0PyCharm2021.3Layer.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3Layer.png)

> Debido a que ArcGIS For Desktop utiliza Python 2, es necesario ingresar los nombres de los campos solicitados por consola entre comillas.


### Ejecución en Notebook de ArcGIS Pro

En un Notebook ejecutar `%run -i D:\R.GISPython\GISListLayerField\GISListLayerFieldArcGIS.py`

![Python3.7.11ArcGISPro2.9.0Run.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python3.7.11ArcGISPro2.9.0Run.png)
![Python3.7.11ArcGISPro2.9.0Layer.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python3.7.11ArcGISPro2.9.0Layer.png)

> Debido a que ArcGIS Pro utiliza Python 3, no es necesario ingresar los nombres de los campos solicitados por consola entre comillas.


### Ejecución en QGIS


### Referencias

* https://pro.arcgis.com/es/pro-app/arcpy/functions/listfields.htm
* https://pro.arcgis.com/es/pro-app/arcpy/classes/field.htm
* https://pro.arcgis.com/es/pro-app/tool-reference/data-management/get-count.htm
* https://community.esri.com/thread/36300
* https://pro.arcgis.com/es/pro-app/arcpy/functions/searchcursor.htm
* [Fix Python Error – UnicodeEncodeError: ‘ascii’ codec can’t encode character’](https://gankrin.org/fix-unicodeencodeerror-ascii-codec-cant-encode-character/)


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

