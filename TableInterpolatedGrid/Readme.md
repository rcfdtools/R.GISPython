## Interpolación y representación espacial de datos meteorológicos con simbología de rampa única
Keywords: `ArcGIS for Desktop` `ArcGIS Pro`

A partir de series de datos diarias o mensuales contenidas en registros discretos dentro de archivos de texto separados por comas o CSV, interpolar y representar espacialmente datos hidrometeorológicos usando re-escalamiento a rampa única de color.


### Antecedentes

En el desarrollo de estudios hidrológicos, comúnmente se realiza la espacialización de variables meteorológicas en series temporales a través de procesos de interpolación, que luego son visualizadas desde interfases gráficas o GUI dentro de sistemas de información geográfica - SIG. Si bien este sistema facilita los procesos de análisis, existe un problema en su representación relacionado con el estilo de visualización, que para una rampa de color específica representa los valores de las celdas o pixeles desde el valor mínimo hasta el valor máximo encontrado, sin embargo, cuando se requiere analizar visualmente multiples grillas de una misma serie temporal (p.ej, una serie mensual precipitación media con 12 grillas), los colores utilizados en la representación para una misma rampa de referencia, no corresponden con los valores obtenidos en las demás grillas debido a que los valores mínimos y máximos pueden ser diferentes en cada una.

Para representar correctamente la serie temporal de la variable en estudio y poder visualizar bidimensional o tridimensionalmente las grillas de resultados, es necesario re-escalar los valores de todas las grillas a mapas de colores únicos a partir del mínimo y máximo encontrado en toda la serie de datos de entrada; de esta forma, en la representación, un valor discreto (p.ej, 100 milímetros de lluvia) existente en múltiples grillas será representado con el mismo color en la visualización.


### Caso de estudio

Estudio de variables hidrometeorológicos (precipitación, evaporación y brillo solar a nivel diario medio y mensual) en diferentes zonas de Colombia - Suramérica a partir de datos escalados utilizando las series de datos del IDEAM.  


### Requerimientos

* [Python 2.7+ de ArcGIS for Desktop 10.6+](https://www.esri.com/en-us/home)
* [ArcGIS Pro 2.9+](https://www.esri.com/en-us/home)
* [PyCharm 2021.3+ Commmunity](https://www.jetbrains.com/pycharm/download/#section=windows) 
* [Sistema operativo Microsoft Windows](https://www.microsoft.com/en-us/windows?r=1)
* [matplotlib](https://matplotlib.org/)

> Para la actualización de librerías existentes o la instalación de librerías adicionales, se recomienda la creación y uso de ambientes virtuales para no modificar las versiones originales de Python sobre ArcMAP y QGIS.


### Funcionalidades

* Evaluación preliminar del archivo de entrada identificando el número de atributos y registros de datos.
* Previsualización de datos de entrada a partir del número de registros indicado por el usuario.
* Selección de variable numérico a representar. 
* Representación en grafica de texto mediante barras horizontales con % de referencia de cada valor discreto respecto al valor máximo encontrado.
* Estadísticos generales (conteo, no nulos, nulos, máximo, mínimo, sumatoria, promedio) de la variable seleccionada para el análisis.
* Evaluación de tamaño espacial del dominio a representar.
* Selección del tipo de frecuencia (diaria o mensual) a analizar. Diarios se evalúan en julianos de 1 a 366 y mensuales de 1 a 12. El usuario puede decidir si genera toda la serie temporal o una fracción (p.ej, para una serie de datos diarios, el usuario puede elegir solo generar los datos del primer trimestre correspondiente a los julianos entre el día 1 y 90 para años)
* Selección del sistema de proyección de coordenadas - CRS. Se han incorporado en el módulo `TableInterpolatedGridModule.py` dentro del arreglo `coordSystem`, diferentes sistemas predeterminados.
* Definición de la resolución de salida de los mapas a interpolar. El valor se ingresa en función de las unidades del CRS seleccionado. El script hace una recomendación del tamaño de pixel para la interpolación.
* Selección de la rampa de colores (128, 256, 512, 1024 valores discretos únicos de color) a utilizar en la representación.
* Interpolación espacial masiva de grillas a partir de la escala temporal definida teniendo en cuenta los parámetros definidos previamente.
* Remuestreo de grillas principales a grillas de representación por simbología única utilizando algebra de mapas. 

> Actualmente el script no dispone de representación segmentada (slices) para de una serie diaria elegir el juliano inicial y final. 
 
> Tenga en cuenta que la resolución espacial definida para la interpolación de grillas se define a partir del sistema de unidades, p.ej, para los sistemas MAGNA que contienen sistema proyectado, el valor de entrada se define en metros y para el CRS WGS84 el valor de entrada se define en grados decimales. 

 
### Ruta de ejecución

Para el desarrollo de este microcontenido se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\HydroGeoZone\` utilizando la siguiente estructura de directorios. 

| Directorio                                                                                         | Descripción                                                                                                              |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [/Data](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/Data)             | Directorio de datos de entrada.                                                                                          |
| [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/Graph)           | Directorio con gráficas e ilustraciones.                                                                                 |
| [/Map](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/Map)               | Directorio con mapas para visualización de resultados en ArcGIS for Desktop y ArcGIS Pro.                                |
| [/Old](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/Old)               | Directorio con versiones antiguas del script y módulos.                                                                  |
| /OutputColorMap                                                                                    | Directorio de salida de grillas remuestreadas con rampa única de color.                                                  |
| /OutputGrid                                                                                        | Directorio de salida de grillas generadas.                                                                               |
| [/PDF](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/PDF)               | Directorio con registros de ejecución en formado Adobe Acrobat.                                                          |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid/Screenshot) | Capturas de pantalla con resultados de ejecución.                                                                        |
| /Temp                                                                                              | Directorio donde se localizan los archivos de forma temporales generados para la creación de las grillas interpoladas.   |

> Los directorios `/OutputColorMap`, `/OutputGrid`, `/Temp` se crea automáticamente en la unidad local y no visibles en el repositorio de GitHub debido al tamaño de los archivos generados. 


### Estructura de datos de entrada

Para la correcta ejecución del script se requiere que los archivos de texto separados por comas utilicen la siguiente estructura:

| Campo  | Descripción                      | Aplica diarios | Aplica mensuales |
|--------|----------------------------------|----------------|------------------|
| Julian | Número de día del año de 1 a 366 | ✅              | ⛔               |
| Month  | Mes del año de 1 a 12            | ⛔              | ✅               |
| CX     | Coordenada en x o este           | ✅              | ✅               |
| CY     | Coordenada en y o noerte         | ✅              | ✅               |
| Var    | Variable númerica a representar  | ✅              | ✅               |


> En un mismo archivo de entrada pueden existir múltiples columnas `Var` registrando diferentes variables meteorológicas, para lo cual el usuario podrá elegir la variable de entrada a analizar a partir de la lista de atributos encontrados.

> En representaciones diarias, el juliano 366 corresponde al día 29 de febrero para años bisiestos. 


### Ejecuciones

#### Ejecución en ArcGIS for Desktop sobre PyCharm

![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png]()


#### Ejecución en ArcGIS Pro sobre PyCharm

![Python3.7.11ArcGISPro2.9.0PyCharm2021.3.png]()


#### Carpetas de resultados

![OutputGrid.png]()
![OutputColorMap.png]()


### Scripts

#### Script [TableInterpolatedGrid.py](https://github.com/rcfdtools/R.GISPython/blob/main/TableInterpolatedGrid/TableInterpolatedGrid.py)

'''

'''

#### Script [TableInterpolatedGridModule.py](https://github.com/rcfdtools/R.GISPython/blob/main/TableInterpolatedGrid/TableInterpolatedGridModule.py)

'''

'''

#### Funciones asociadas al módulo 

| Función                | Descripción                                                                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| systemprompt()         | Prompt para identificación de líneas de consola que requieren acción de usuario, se identifica como {R}.                                                                                |
| printtitle()           | Impresión de títulos con estilo de líneas superior, inferior o ambos. Permite impresión tabulada.                                                                                       |
| optionrange()          | Validación de opción de entrada de usuario para valores enteros dentro de un rango específico de valores.                                                                               |
| optionrangefloat()     | Validación de opción de entrada de usuario para valores flotantes dentro de un rango específico de valores.                                                                             |
| optionyesno()          | Validación de opción de entrada de usuario para valores respuestas con Sí (Y) o Nó (N).                                                                                                 |
| csvtotalfieldfound(()  | A partir de la ruta de localización del archivo .csv, cuenta el número de atributos o columnas disponibles.                                                                             |
| csvtotalrecordfound(() | A partir de la ruta de localización del archivo .csv, cuenta el número de registros incluida la cabecera de columna.                                                                    |
| csvspacialdomain()     | A partir de los registros contenidos en el archivo de entrada, evalúa el tamaño del dominio espacial de los datos.                                                                      |
| csvsamplerecord()      | A partir de los registros contenidos en el archivo de entrada y un número de registros indicado por el usuario, imprime una muestra de los datos de entrada incluida la cabecera.       |
| datafrecuency()        | Frecuencias disponibles para análisis para selección de usuario: Diaria o Mensual. El usuario puede elegir el número de grillas a generar a partir del tipo de frecuencia seleccionada. |
| crscoordsystem()       | Sistemas de referencia de coordenadas predeterminados para la referenciación espacial de los archivos de forma temporales y las grillas interpoladas.                                   |
| crscoordsystem()       | Sistemas de referencia de coordenadas predeterminados para la referenciación espacial de los archivos de forma temporales y las grillas interpoladas.                                   |
| csvheader()            | Lista los nombres de los atributos disponibles en el archivo de entrada y solicita al usuario el atributo a utilizar en el análisis correspondiente a la variable a interpolar.         |
| csvstatistic()         | Para la variable especificada en `csvheader()` calcula los siguientes estadísticos: Registros, Conteo no nulos, Conteo nulos, Máximo, Mínimo, Suma y Promedio.                          |
| colormapstyle()        | Lista de estilos de rampa de color seleccionables por el usuario para la representación de las grillas re-escaladas.                                                                    |
| graphtxt()             | Grafica e imprime como texto en la consola de ejecución, todos los valores discretos encontrados de la variable a analizar.                                                             |
| graphtxtonevalue(()    | Grafica e imprime como texto en la consola de ejecución, un valor definido respecto a un valor máximo establecido.                                                                      |

> La función `optionrange()` valida la entrada numérica y en caso de contener valores decimales, válida la parte entera como entrada de usuario. 

> Para las funciones `optionrange()`, `optionrangefloat()` y `optionyesno()`, en caso de que la opción ingresada no pueda ser validada o esté fuera de rango, se solicita nuevamente el valor hasta que se ingrese un valor válido.
 
> La función `optionyesno()` válida que la entrada sea una cadena de texto y evalúa si se ingresa en mayúsculas o minúsculas la opción solicitada. En Python 2 sobre ArcGIS for Desktop 10+, es necesario ingresar la respuesta entre comillas, p.ej, 'Y', 'y', 'N' o 'n'.

> La función `csvspacialdomain()` identifica el número de columna donde se encuentran los valores CX o longitudes y CY o latitudes; calcula el tamaño horizontal y vertical del dominio espacial y divide la menor dimensión entre 150 celdas o pixeles para sugerir el tamaño de pixel a utilizar en las interpolaciones espaciales.

> El script no presenta en la función `datafrecuency()` una opción específica para series de datos anuales, sin embargo, utilizando la frecuencia `Díaria` a partir de Julianos, se pueden generar interpolaciones hasta 366 años. Los valores de la columna `Var` o la columna numérica a representar, deberán corresponder a datos escalados a nivel anual.   

> En caso de que el usuario requiera un CRS diferente a los predeterminados en `crscoordsystem()`, en el arreglo `coordSystem` se pueden agregar nuevos sistemas o modificar los existentes. Los parámetros de entrada del CRS pueden ser obtenidos a través de un archivo .prj asociado a un archivo de formas shapefile previamente georeferenciado.

> La función `csvstatistic()` además de calcular los estadísticos generales, almacena en listas, el número de registro y los valores discretos de la variable seleccionada para su posterior graficación con `matplotlib`. 

> Las rampas de colores en formato .clr incluidas en la carpeta `ColorMapStyle` han sido creadas por r.cfdtools.


### Referencias

* https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-functions/checkoutextension.htm
* https://stackoverflow.com/questions/7852855/in-python-how-do-you-convert-a-datetime-object-to-seconds
* https://stackoverflow.com/questions/34165941/how-to-display-tiff-file-in-color
* https://www.codegrepper.com/code-examples/python/python+2.7+datetime+to+timestamp


### Autores

* Creado por [r.cfdtools](r.cfdtools@gmail.com) (60h).


### Compatibilidad

* Compatible con ArcGIS for Desktop 10 o superior.
* Compatible con ArcGIS Pro.


### Control de versiones

| Versión    | Descripción                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------|
| v.20171123 | Versión inicial sobre Python 2 solo compatible con ArcGIS for Desktop.                                |
| v.20180124 | Versión con módulo y funciones.                                                                       |
| v.20211231 | Actualización para compatibilidad con Python 3 y ArcGIS Pro. Optimización de script. Log de registro. |


### Licencia, cláusulas y condiciones de uso

R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]()     |
|------------------------|---------------------------------------------------------|-----------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_
