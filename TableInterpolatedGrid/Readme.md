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
* Conversión de grillas principales a grillas de representación por simbología única. 

> Actualmente el script no dispone de representación segmentada (slices) para de una serie diaria elegir el juliano inicial y final. 
 
> El usuario puede incluir manualmente en el módulo `TableInterpolatedGridModule.py` dentro del arreglo `coordSystem`, nuevos o diferentes sistemas a los predeterminados.

> Tenga en cuenta que la resolución espacial definida para la interpolación de grillas se define a partir del sistema de unidades, p.ej, para los sistemas MAGNA que contienen sistema proyectado, el valor de entrada se define en metros y para el CRS WGS84 el valor de entrada se define en grados decimales. 

> Las rampas de colores en formato .clr incluidas en la carpeta `ColorMapStyle` han sido creadas por r.cfdtools.

 
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


#### Ejecución en ArcGIS for Desktop

![Python3.7.11ArcGISPro2.9.0.png]()


#### Ejecución en ArcGIS Pro

![Python3.7.11ArcGISPro2.9.0.png]()

### Scripts

#### Script [TableInterpolatedGrid.py]()

'''

'''

#### Script [TableInterpolatedGridModule.py]()

'''

'''


### Referencias

* https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-functions/checkoutextension.htm
* https://stackoverflow.com/questions/7852855/in-python-how-do-you-convert-a-datetime-object-to-seconds
* https://stackoverflow.com/questions/34165941/how-to-display-tiff-file-in-color



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
