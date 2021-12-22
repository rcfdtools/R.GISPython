## Estadísticos de una capa geográfica
Topics: `arcpy` `env` `arcpy.env.overwriteOutput`  `arcpy.GetCount_management()` `arcpy.Describe` `arcpy.ListFields()` `arcpy.env.workspace` `arcpy.Statistics_analysis()` `arcpy.TableToExcel_conversion()`

A partir de una capa geográfica en formato shapefile o feature class dentro de una Geodatabase, obtener los estadísticos de un campo de atributos determinado y estadísticos por filtrado a partir de un valor de corte en ArcGIS y QGIS.

![LayerStatistic.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/LayerStatistic.png)


### Objetivos

* Estudiar las propiedades y metadatos de una capa geográfica
* Definir un atributo y el valor de corte a evaluar.
* Obtener los estadísticos generales de la capa seleccionada con y sin filtrado a partir del atributo definido.
* Mostrar los valores discretos de la tabla de atributos con y sin filtrado.
* Analizar con gráficas de barras, los valores discretos evaluados a partir del campo de atributos definido y el valor de corte.  


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9+.
* QGIS 3.22.1+.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda. 
* Sistema operativo Microsoft Windows.
* matplotlib

> Para la instalación o actualización de librerías en ArcGIS for Desktop o en ArcGIS Pro se recomienda crear entornos virtuales, de esta forma no se modificarán las versiones originales del paquete requeridas para su correcta ejecución.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\LayerStatistic\`. 


### Caso de estudio

Estudio de localización y valores de precipitación, evaporación y temperatura de las estaciones hidrometeorológicas del [IDEAM - Colombia](http://www.ideam.gov.co/) localizadas sobre varios Departamentos de la zona central del país.


### Estadísticos en capas geográficas vectoriales sobre ArcGIS [^1]

| Estadístico | Descripción                                                                                                                                                    | Desktop | Pro  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|------|
| SUM         | Adds the total value for the specified field.                                                                                                                  | ✅       | ✅    |
| MEAN        | Calculates the average for the specified field.                                                                                                                | ✅       | ✅    |
| MIN         | Finds the smallest value for all records of the specified field.                                                                                               | ✅       | ✅    |
| MAX         | Finds the largest value for all records of the specified field.                                                                                                | ✅       | ✅    |
| RANGE       | Finds the range of values (MAX minus MIN) for the specified field.                                                                                             | ✅       | ✅    |
| STD         | Finds the standard deviation on values in the specified field.                                                                                                 | ✅       | ✅    |
| COUNT       | Finds the number of values included in statistical calculations. This counts each value except null values. To determine the number of null values in a field  | ✅       | ✅    |
| FIRST       | Finds the first record in the Input Table and uses its specified field value.                                                                                  | ✅       | ✅    |
| LAST        | Finds the last record in the Input Table and uses its specified field value.                                                                                   | ✅       | ✅    |
| MEDIAN      | The median for all records of the specified field will be calculated.                                                                                          | ⛔       | ✅    |
| VARIANCE    | The variance for all records of the specified field will be calculated.                                                                                        | ⛔       | ✅    |
| UNIQUE      | The number of unique values of the specified field will be counted.                                                                                            | ⛔       | ✅    |

> Atención: para la ejecución correcta de los sripts se recomienda cerrar sus aplicativos GIS. Para garantizar la compatibilidad con la versión Desktop de ArcGIS, no se han incluido los estadísticos `MEDIAN`, `VARIANCE` y `UNIQUE`.

### Estadísticos generales de una capa geográfica en ArcGIS for Desktop

#### Script [LayerStatisticArcGIS.py](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/LayerStatisticArcGIS.py)

```
# -*- coding: UTF-8 -*-
# Nombre: LayerStatisticArcGIS.py
# Descripción: Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro
# Requerimiento: PyCharm 2021.3+, ArcGIS 10.2.2, ArcGIS Pro 2.9.0

# Librerías
import arcpy                        # Importación de arcpy de ArcGIS.
from arcpy import env               # Importación de librería para manejo del entorno de trabajo.
arcpy.env.overwriteOutput = True    # Permitir sobreescribir archivos en directorio del entorno de trabajo.
import sys

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Función para consultar los campos de atributos disponibles
def CapaPropiedades(i):
    cont = 1
    totalEntidades = arcpy.GetCount_management(i)
    descGeometria = arcpy.Describe(i)
    tipoGeometria = descGeometria.shapeType
    tituloCapa = 'Campos en ' + i + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')'
    Separador(len(tituloCapa))
    print(tituloCapa)
    Separador(len(tituloCapa))
    print('  #, Campo, Tipo')
    campos = arcpy.ListFields(i)
    for campo in campos:
        print('  ' + str(cont) + ', ' + campo.name + ', ' + campo.type)  # Print field properties
        cont += 1

# Variables
absolutePath = r'D:/R.GISPython/LayerStatistic' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Datos/'
outputPath = absolutePath+'/Output/'
layerInput = 'Precipitacion.shp'
layerSelect = outputPath+'LayerSelect.shp'
layerStatistic = outputPath+'LayerStat.dbf'
layerStatisticXLS = outputPath+'LayerStat.xls'
layerStatisticFilter = outputPath+'LayerStatFilter.dbf'
layerStatisticFilterXLS = outputPath+'LayerStatFilter.xls'

# Cabecera
Separador(67)
print ('Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro')
Separador(67)
print ( 'Compatible con: ArcGIS for Desktop y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Ejecución
print(  'Capa de entrada: '+layerInput+'\n'
        'Capa de filtrado: '+layerSelect+'\n'
        'Estadísticos capa entrada:  '+layerStatistic+'\n'
        'Estadísticos capa filtrada:  '+layerStatisticFilter+'\n')
CapaPropiedades(layerInput)
print('\n  Antes de continuar, cierre ArcGIS...')
fieldEval = input('  >>> Nombre del campo a evaluar (usar comillas): ')
fieldValue = input('  >>> Mostrar valores >= a: ')
print('\nEjecutando estadística para ' + outputPath + layerInput + '...')
# Estadísticos compatibles con ArcGIS for Desktop
statisticsType = [[fieldEval,'SUM'],[fieldEval,'MEAN'],[fieldEval,'MIN'],[fieldEval,'MAX'],[fieldEval,'RANGE'],[fieldEval,'STD'],[fieldEval,'COUNT'],[fieldEval,'FIRST'],[fieldEval,'LAST']]
arcpy.Statistics_analysis(layerInput,layerStatistic,statisticsType)
print('Ejecutando estadística para ' + layerSelect + ' con '+ fieldEval + ' >= ' + str(fieldValue) + '...')
arcpy.Select_analysis(layerInput, layerSelect, fieldEval+'>='+str(fieldValue))
arcpy.Statistics_analysis(layerSelect,layerStatisticFilter,statisticsType)
# Conversión a libro de Microsoft Excel
print ('Conversión de estadísticos a XLS file...')
arcpy.TableToExcel_conversion(layerStatistic,layerStatisticXLS)
arcpy.TableToExcel_conversion(layerStatisticFilter,layerStatisticFilterXLS)
print('Proceso completado, visualice la capa filtrada y las tablas de resultados estadísticos en ArcGIS o en Microsoft Excel.')
```

#### Explicación de instrucciones empleadas

| Instrucción                                                                                                                                                                                  | Descripción                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| import arcpy                                                                                                                                                                                 | Importación de arcpy de ArcGIS for Desktop y ArcGIS Pro.                                                                                                         |
| from arcpy import env                                                                                                                                                                        | Importación de librería para manejo del entorno de trabajo.                                                                                                      |
| arcpy.env.overwriteOutput = True                                                                                                                                                             | Permitir sobreescribir archivos en directorio del entorno de trabajo.                                                                                            |
| import sys                                                                                                                                                                                   | Importación de librería nativa de sistema en Python.                                                                                                             |
| def Separador(n=24)                                                                                                                                                                          | Función para creación de líneas de separación                                                                                                                    |
| def CapaPropiedades(i)                                                                                                                                                                       | Función para consultar los campos de atributos disponibles en una capa geográfica.                                                                               |
| arcpy.GetCount_management()                                                                                                                                                                  | Cuenta el número de entidades en una capa.                                                                                                                       |
| arcpy.Describe                                                                                                                                                                               | Descripción de la geometría de la capa.                                                                                                                          |
| descGeometria.shapeType                                                                                                                                                                      | Descripción del tipo de geometría vectorial de la capa.                                                                                                          |
| arcpy.ListFields()                                                                                                                                                                           | Lista los campos de atributos de una capa. Liego de la asignación a una variable local, los parámetros nombre y tipo pueden ser obtenidos con `.name` y `.type`. |
| arcpy.env.workspace = 'mypath'                                                                                                                                                               | Definición de la ruta de localización del espacio de trabajo.                                                                                                    |
| sys.version                                                                                                                                                                                  | Muestra la versión de Python sobre la que se ejecuta el script.                                                                                                  |
| sys.path[0:5]                                                                                                                                                                                | Muestra las rutas asociadas a la versión de Python utilizada entre las posiciones 0 a 5.                                                                         |
| input()                                                                                                                                                                                      | Entrada de usuario por consola.                                                                                                                                  |
| statisticsType = [[fieldEval,'SUM'],[fieldEval,'MEAN'],[fieldEval,'MIN'],[fieldEval,'MAX'],[fieldEval,'RANGE'],[fieldEval,'STD'],[fieldEval,'COUNT'],[fieldEval,'FIRST'],[fieldEval,'LAST']] | Estadísticos a obtener a través de arcpy.Statistics_analysis.                                                                                                    |
| arcpy.Statistics_analysis(layerInput,layerOutpu,statisticsType)                                                                                                                              | Obtención de estadísticos de la capa.                                                                                                                            |
| arcpy.TableToExcel_conversion(layerStatistic,layerStatisticXLS)                                                                                                                              | Conversión de tabla a libro de Microsoft Excel.                                                                                                                  |

#### Resultados de ejecución

Desde PyCharm 2021.3. usando Python 2.7.5 de ArcGIS for Desktop 10.2.2.
![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png)

> En ArcGIS for Desktop es necesario ingresar las entradas `input()` para cadenas de texto entre comillas debido a que utiliza la versión 2 de Python.

Visualización de resultados en ArcGIS for Desktop.
![Python2.7.5ArcGISDesktop10.2.2.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python2.7.5ArcGISDesktop10.2.2.png)

Desde PyCharm 2021.3. usando Python 3.7. de ArcGIS Prop 2.9.0.
![Python3.7.11ArcGISPro2.9.0PyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python3.7.11ArcGISPro2.9.0PyCharm2021.3.png)

Ejecución desde Notebook en ArcGIS Pro con `%run -i D:\R.GISPython\LayerStatistic\LayerStatisticArcGIS.py`.
![Python3.7.11ArcGISPro2.9.0Notebook.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python3.7.11ArcGISPro2.9.0Notebook.png)

> La ejecución desde un Notebook utiliza el entorno gráfico o GUI de ArcGIS Pro y sobreescribe automáticamente los resultados de la capa de filtrado y tablas de estadísticos obtenidos sin que la aplicación deba ser cerrada.

> En ArcGIS Pro no es necesario ingresar las entradas `input()` para cadenas de texto entre comillas debido a que utiliza la versión 3 de Python.  

Visualización de resultados en ArcGIS Pro.
![Python3.7.11ArcGISPro2.9.0.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python3.7.11ArcGISPro2.9.0.png)


### Estadísticos generales de una capa geográfica en QGIS 3

#### Script [LayerStatisticQGIS3.py](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/LayerStatisticQGIS3.py)

```
# -*- coding: UTF-8 -*-
# Nombre: LayerStatisticQGIS3.py
# Descripción: Estadísticos de capas geográficas - QGIS 3
# Requerimiento: PyCharm 2021.3+, QGIS 3.22.1

# Librerías
from qgis.core import *
import qgis.utils
import matplotlib
import matplotlib.pyplot as plt

# Función para creación de líneas de separación
def Separador(n = 24): # Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Variables
#qgs = QgsApplication([], False)
absolutePath = r'D:/R.GISPython/LayerStatistic/Datos/' # Usar r'.' para retornar a ruta relativa
layerInput = absolutePath+'Precipitacion.shp'
fieldEval = 'TotalAnno' # Variable para filtrado
fieldTag = 'ESTACION' # Campo para etiquetado
fieldValue = 1200 # Variable de corte para selección
recordSample = 10 # Número de registros de ejemplo a mostrar en pantalla

# Cabecera
Separador(40)
print ('Estadísticos de capas geográficas - QGIS')
Separador(40)
print ( 'Compatible con: QGIS 3'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__) +
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Ejecución de procesos geográficos
print('Capa de entrada: '+layerInput)
#layerMAPProject = iface.addVectorLayer(layerInput,'','ogr') # Cargar en mapa QGIS
layerMAPProject = QgsVectorLayer(layerInput,'','ogr') # Sin cargar en mapa QGIS
print('Layer ID:', layerMAPProject.id(),'\n')
Separador(29)
print('Campos disponibles en la capa')
Separador(29)
for field in layerMAPProject.fields():
    print(field.name(), end = ', ')
entityCount = layerMAPProject.featureCount()
print('\n')
tagShow = 'Muestra de ' + str(recordSample) + ' datos'
Separador(len(tagShow))
print('Muestra de '+str(recordSample)+' datos')
Separador(len(tagShow))
print(fieldTag+', '+fieldEval)
averageValue = 0
averageValueSelect = 0
cont = 0
contAux = 0
listaCampoEtiqueta, listaCampoEvaluar, listaCampoEvaluarFiltro = [], [], []
for i in range(0, entityCount):
    listaCampoEtiqueta.append(contAux)
    featureValue = layerMAPProject.getFeature(i)
    listaCampoEvaluar.append(featureValue[fieldEval])
    #print(featureValue[0])
    if i < recordSample:
        print(featureValue[fieldTag]+', '+str(round(featureValue[fieldEval],3)))
    averageValue = averageValue + featureValue['TotalAnno']
    if featureValue['TotalAnno'] > fieldValue:
        cont += 1
        averageValueSelect = averageValueSelect + featureValue[fieldEval]
        listaCampoEvaluarFiltro.append(-featureValue[fieldEval])
    else:
        listaCampoEvaluarFiltro.append(0)
    contAux+=1
print('\n')
Separador(23)
print('Ejecutando estadísticas')
Separador(23)
print('# Entidades sin filtro:', entityCount)
print('# Entidades con filtro:',cont)
print('Promedio sin filtro:',averageValue / entityCount)
print('Promedio con filtro >'+str(fieldValue)+':'+str(averageValueSelect / cont))
print('Generando gráfica de barras para datos no filtrados....')
plt.figure(figsize=(8, 8), dpi=100)
plt.bar(listaCampoEtiqueta, listaCampoEvaluar, color = 'darkGray', label='Sin filtro')
plt.bar(listaCampoEtiqueta, listaCampoEvaluarFiltro, color = 'red', label='Con filtro')
plt.title('Valores encontrados con y sin filtro')
plt.xlabel('Index')
plt.ylabel(fieldEval)
plt.legend(loc='best', shadow=False, fontsize=11)
plt.grid()
plt.show()

#Visualizar las propiedades de una capa seleccionada en el proyecto actual requiere una capa cargada y seleccionada en QGIS
'''
layer = qgis.utils.iface.activeLayer()
print(layer.id())
print(layer.featureCount())
'''
```

Explicación de instrucciones empleadas



![Python3.9.5QGIS3.22.1.png](https://github.com/rcfdtools/R.GISPython/blob/main/LayerStatistic/Screenshot/Python3.9.5QGIS3.22.1.png)

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