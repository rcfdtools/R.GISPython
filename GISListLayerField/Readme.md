## Consulta de metadatos, propiedades y atributos en capas vectoriales de proyectos geográficos

Esta actividad contiene scripts en Python que permiten listar todas las capas geográficas (en formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm)) disponibles en el directorio de datos local de un proyecto de ArcGIS o en las capas cargadas en un mapa de QGIS, consultar los atributos disponibles en cada capa, sus tipos, filtrar a partir de un campo específico y graficar los valores encontrados a partir de dos campos específicos definidos por el usuario.

![GISListLayerField.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/GISListLayerField.png)


### Objetivos

* Utilizar el núcleo y las funciones [ArcPy](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/what-is-arcpy-.htm) de ESRI ArcGIS for Desktop y ArcGIS Pro.
* Utilizar el núcleo y las funciones [PyQGIS](https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html) de QGIS.
* Listar las capas y atributos contenidos en el directorio de datos de un proyecto geográfico de ArcMap o en un mapa de QGIS.
* Representar gráficamente los datos contenidos en las tablas de atributos de las capas geográficas.


### ¿Qué es ArcPy y PyQGIS?

ArcPy y PyQGIS son paquetes de Python para ArcGIS y QGIS que contiene gran variedad de funciones para análisis espacial, conversión de datos, administración y automatización de tareas geográficas. En un script o en un Notebook de ArcGIS Pro o en QGIS, ingresando `arcpy.` o `qgis.` más una letra o palabra clave, el usuario obtiene una lista desplegable con las propiedades y métodos disponibles y podrá de forma rápida seleccionar alguna de ellas para ser insertada en el código o para conocer sus parámetros. 


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM - Colombia](http://www.ideam.gov.co/) localizadas sobre varios Departamentos de la zona central del país.


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* QGIS 2.18.28+
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
| Estaciones.shp    | Estaciones hidrometeorológicas del [IDEAM - Colombia](http://www.ideam.gov.co/) localizadas sobre varios Departamentos de la zona central del país. Más información en la actividad Catálogo nacional de estaciones hidrometeorológicas del IDEAM - Colombia, descarga y análisis usando Python. |
| Precipitacion.shp | Estaciones con estadísticos mensuales multianuales de _Precipitación Mensual Total_ a partir de registros discretos del [IDEAM - Colombia](http://www.ideam.gov.co/).                                                                                                                            |
| Evaporacion.shp   | Estaciones con estadísticos mensuales multianuales de _Evaporación Mensual Total_ a partir de registros discretos del [IDEAM - Colombia](http://www.ideam.gov.co/).                                                                                                                              |
| Temperatura.shp   | Estaciones con estadísticos mensuales multianuales de _Temperatura del Aire Mensual Media_ a partir de registros discretos del [IDEAM - Colombia](http://www.ideam.gov.co/).                                                                                                                     |

> Tenga en cuenta que los datos utilizados pueden estar desactualizados y solamente se utilizan como recurso para ejemplificar esta actividad.  


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se almacenen en D:\R.GISPython\GISListLayerField\


### Script para Esri ArcGIS for Desktop y ArcGIS Pro

Descripción instrucciones y comandos empleados en [GISListLayerFieldArcGIS.py](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/GISListLayerFieldArcGIS.py)

| Instrucción                                                      | Explicación                                                                                                                                                                                      |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| import arcpy                                                     | Importación de la librería acrpy de ArcGIS.                                                                                                                                                      |
| def CapaPropiedades(i):                                          | Función que permite consultar las propiedades generales de una capa geográfica (nombre, geometría) los atributos disponibles y sus tipos. En los parámetros, i corresponde al nombre de la capa. |
| totalEntidades = arcpy.GetCount_management(i)                    | Total de entidades encontradas en la capa.                                                                                                                                                       |
| descGeometria = arcpy.Describe(i)                                | Descripción general de la capa.                                                                                                                                                     |
| tipoGeometria = DescGeometria.shapeType                          | shapeType permite conocer el tipo de geometría nativa de la capa (puntos, líneas o polígonos).                                                                                                   |
| campos = arcpy.ListFields(i)                                     | Lista los campos disponibles en la capa y los almacena en la variable Campos. Las propiedades más comunes son el nombre (name) y tipo (type).                                                    |
| absolutePath = r'D:/R.GISPython/GISListLayerField'               | Definición de ruta absoluta para compaibilidad de ejecución en ArcGIS Pro Notebook y Jupyter. Usar `r'.'` para retornar a ruta relativa.                                                         |
| arcpy.env.workspace = absolutePath+'/Datos'                      | Definición del espacio de trabajo.                                                                                                                                                               |
| featureList = arcpy.ListFeatureClasses()                         | Lista las capas disponibles en el espacio de trabajo y las almacena en la variable FeatureList.                                                                                                  |
| cursor = arcpy.SearchCursor(FeatureList[NumCapaEntrada-1])       | Mediante cursores es posible almacenar en una variable toda la información de la tabla de atributos de una capa.                                                                                 |
| fila.getValue(campoEvaluar)                                      | Permite obtener el valor de un campo específico desde el registro activo.                                                                                                                        |
| plt.bar(listaCampoRotulo, listaCampoEvaluar, color = 'darkGray') | Graficar mediante barras de color gris oscuro a partir de dos campos numéricos.                                                                                                                  |
| except NameError as e:                                           | Excepción para error en nombre de variable o variable no encontrada.                                                                                                                             |
| except ValueError as e:                                          | Excepción para error en valor definido en una variable al ejecutar una operación o cuando una función recibe el valor como un argumento.                                                         |
| except SyntaxError as e:                                         | Excepción para error en sintaxis.                                                                                                                                                                |
| except IndexError as e:                                          | Excepción para error en índices o valores fuera de rango.                                                                                                                                        |
| except RuntimeError as e:                                        | Excepción para error general de ejecución cuando no puede ser evaluada por otro tipo de excepcion.                                                                                               |


### Script para QGIS 3

Descripción instrucciones y comandos empleados en [GISListLayerFieldArcGIS.py](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/GISListLayerFieldQGIS.py)

| Instrucción                                                                          | Explicación                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| from qgis.core import *                                                              | Importación del núcleo de QGIS.                                                                                                                                                                          |
| import qgis.utils                                                                    | Importación de paquete de utilidades generales.                                                                                                                                                          |
| from qgis.core import QgsProject                                                     | Importación de paquete para administración del proyecto en el GUI de la aplicación.                                                                                                                      |
| featureList = [layer.name() for layer in QgsProject.instance().mapLayers().values()] | Creación de lista con las capas disponibles en el proyecto actual. No incluye las extensiones de las capas. El For aninado dentro de los corchetes es un tipo de sintaxis compacta utilizada por Python. |
| for layer in QgsProject.instance().mapLayers().values():                             | for principal para la visualización de capas, sus atributos y tipos.                                                                                                                                     |
| totalEntidades = layer.featureCount()                                                | Conteo de entidades dentro de la capa actual.                                                                                                                                                            |
| if layer.wkbType() == QgsWkbTypes.Point:                                             | Evaluación de geometría de capa para tipo punto.                                                                                                                                                         |
| elif layer.wkbType() == QgsWkbTypes.LineString:                                      | Evaluación de geometría de capa para tipo línea.                                                                                                                                                         |
| elif layer.wkbType() == QgsWkbTypes.Polygon:                                         | Evaluación de geometría de capa para tipo polígono.                                                                                                                                                      |
| elif layer.wkbType() == QgsWkbTypes.MultiPolygon:                                    | Evaluación de geometría de capa para tipo multi-polígono.                                                                                                                                                |
| for field in layer.fields():                                                         | for para evaluar cada atributo en cada registro de la capa actual.                                                                                                                                       |
| field.name()                                                                         | Nombre del campo de atributo.                                                                                                                                                                            |
| field.typeName()                                                                     | Tipo de atributo.                                                                                                                                                                                        |
| #layerInput = iface.addVectorLayer(gisFileInput,'','ogr')                            | Cargar una capa al mapa actual.                                                                                                                                                                          |
| layerInput = QgsVectorLayer(gisFileInput,'','ogr')                                   | Cargar una capa solo en memoria.                                                                                                                                                                         |
| fCount = layerInput.featureCount()                                                   | Conteo de entidades en la capa cargada en el mapa o en memoria.                                                                                                                                          |
| plt.style.use('fast')                                                                | Estilo de ploteo de gráficas en la versión 3.1.1+ de matplotlib.                                                                                                                                         |

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

![Python3.9.5QGIS3.22.1.png](https://github.com/rcfdtools/R.GISPython/blob/main/GISListLayerField/Screenshot/Python3.9.5QGIS3.22.1.png)


### Referencias

* https://pro.arcgis.com/es/pro-app/arcpy/functions/listfields.htm
* https://pro.arcgis.com/es/pro-app/arcpy/classes/field.htm
* https://pro.arcgis.com/es/pro-app/tool-reference/data-management/get-count.htm
* https://community.esri.com/thread/36300
* https://pro.arcgis.com/es/pro-app/arcpy/functions/searchcursor.htm
* https://gankrin.org/fix-unicodeencodeerror-ascii-codec-cant-encode-character/
* https://gis.stackexchange.com/questions/118862/getting-list-of-layer-names-using-pyqgis
* https://gis.stackexchange.com/questions/312153/how-to-test-the-geometry-type-from-a-list-of-layers-and-then-join-it-with-pyqgis
* https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/geometry.html 


### Autores

* Creado por [r.cfdtools](r.cfdtools@gmail.com) (24h)


### Compatibilidad

* Compatible con ArcGIS for Desktop, ArcGIS Pro y QGIS 3+.


### Tags

`Hydrology` `Stations` `Prepipitation` `Evaporation` `Temperature` `arcpy` `pyqgis` `Metadata`


### Control de versiones

| Versión    | Descripción                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------|
| v.20211219 | Versión inicial.                                                                                          |
| v.20211220 | Versión con incorporación de gráficas tipo pastel, validación de codificación según la versión de Python. |


### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]() |
|------------------------|------------|-------------------------|

