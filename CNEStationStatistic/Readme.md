## Catálogo nacional de estaciones hidrometeorológicas del IDEAM - Colombia, descarga y análisis usando Python

<div  align="center">
    <img align="center"  alt="StationScatterPlotMap20211213.png" src="https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/StationScatterPlotMap20211213.png" width="800px"/>
</div>


### Caso de estudio

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

El presente repositorio y el código desarrollado en Python por r.cfdtools@gmail.com, descarga de forma directa el archivo del catálogo nacional de estaciones y realiza un análisis estadístico detallado a través de los diferentes clasificadores registrados.

### Funcionalidades incorporadas

* Descarga directa del archivo del catálogo nacional de estaciones. Si en la fecha actual ya ha sido descargado el archivo, el script realizará únicamente su procesamiento.
* Configuración inicial modificable por el usuario para definir ruta de descarga `urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls`, presentación de resumen corto de estaciones encontradas`sampleRecord = 12`, listado completo de estaciones con geo-localizadores `showAllRecords = False`.
* Despliegue de gráficas de análisis en ventanas emergentes a petición del usuario `showGraphScreen = False`, volcado automático de gráficas a formato PNG `plt.savefig()` y generación e impresión en consola de enlaces de consulta.
* Definición del método de análisis para la clasificación por pisos térmicos `thermalLevelCaldas = True`: convencional o Caldas 1802. Los arreglos de datos `thermalLevelRefConv` y `thermalLevelRefCaldas` utilizados para la clasificación pueden ser actualizados por el usuario.
* Definición de nombres de campos de atributos de análisis. En el evento de que el modelo de datos de estaciones IDEAM sea actualizado, reestructurado o normalizado, el usuario podrá evaluar el nombre de los nuevos campos y realizar la actualización de los nuevos nombres. Aplica para: nombre, latitud, longitud, altitud, CATEGORIA, TECNOLOGIA, ESTADO, FECHA_INSTALACION, DEPARTAMENTO, AREA_OPERATIVA, AREA_HIDROGRAFICA, ZONA_HIDROGRAFICA y SUBZONA_HIDROGRAFICA.
* Definición de nivel de transparencia en gráficas para ahorro en consumo de insumos de impresión.
* Identificación y resumen de atributos encontrados en el catálogo.
* Estadísticos generales sobre campos numéricos del catálogo.
* Estadístico de conteo y con normalización de estaciones por categoría, tecnología, estado, departamento, área operativa, área hidrográfica, zona hidrográfica, subzona hidrográfica y año de instalación.
* Generación automática de tablas y gráficas dinámicas por estado de actividad con análisis para categoría, tecnología, departamento, área operativa, área hidrográfica, zona hidrográfica, sub-zona hidrográfica y año de instalación.
* Análisis y graficación de estaciones por piso térmico para el método definido.
* Mapa de matriz de dispersión con localización de toda la red de estaciones subclasificada por elevación.
* Mapa de matriz de dispersión con localización de la red de estaciones subclasificada por elevación y por departamento.
* Diccionario de definiciones generales impreso como apéndice en la ventana de ejecución.
 
> En caso de que requiera analizar una versión antigua del archivo del catálogo nacional de estaciones, podrá cargar el archivo en cualquier repositorio de uso personal, redireccionar el script a la url del archivo y ejecutar el script. Tener en cuenta que las fechas presentadas en los análisis, corresponderán a la fecha del sistema operativo. Opcionalmente podrá crear una copia del archivo a analizar y modificar la fecha incluida en el nombre del archivo a la fecha actual en formato aaaammdd.

> En el evento de que por reestructuración del modelo de datos IDEAM, desaparezca alguno de los campos utilizados para el análisis general y la creación de las tablas dinámicas, el usuario deberá crear manualmente en el archivo .xls fuente, las columnas requeridas para la ejecución correcta del script.   


### Requerimientos

* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.


### Atributos que componen el catálogo nacional de estaciones

Atributos tomados directamente del archivo [CNE_IDEAM.xls](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls).

| Atributo             | Tipo           | Descripción                                                                                                                                                                                                                                     |
|----------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID             | int64          | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                   |
| CODIGO               | int64          | Código de la estación.                                                                                                                                                                                                                          |
| nombre               | object         | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                        |
| CATEGORIA            | object         | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria.  |
| TECNOLOGIA           | object         | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                            |
| ESTADO               | object         | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                 |
| FECHA_INSTALACION    | datetime64[ns] | Fecha de instalación.                                                                                                                                                                                                                           |
| altitud              | int64          | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                                |
| latitud              | float64        | Latitud en grados decimales.                                                                                                                                                                                                                    |
| longitud             | float64        | Longitud en grados decimales.                                                                                                                                                                                                                   |
| DEPARTAMENTO         | object         | Departamento o zonificación política. Equivalente a estados en otros países.                                                                                                                                                                    |
| MUNICIPIO            | object         | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                    |
| AREA_OPERATIVA       | object         | Área operativa que administra la estación.                                                                                                                                                                                                      |
| AREA_HIDROGRAFICA    | object         | Área hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| ZONA_HIDROGRAFICA    | object         | Zona hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| observacion          | object         | Observaciones generales.                                                                                                                                                                                                                        |
| CORRIENTE            | object         | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                     |
| FECHA_SUSPENSION     | datetime64[ns] | Fecha de suspensión.                                                                                                                                                                                                                            |
| SUBZONA_HIDROGRAFICA | object         | Subzona hidrográfica a la cual pertenece.                                                                                                                                                                                                       |
| ENTIDAD              | object         | Entidad encargada.                                                                                                                                                                                                                              |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres.


### Definiciones generales del catálogo nacional de estaciones

Tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.


#### Categorías de las estaciones

| Categoría                        | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).                                                                                     |
| Estación Climatológica Ordinaria | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                                |
| Estación Climatológica Principal | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.                                                                                                                                                           |
| Estación Limnigráfica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                       |
| Estación Limnimétrica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                       |
| Estación Mareográfica            | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación meteorológica especial  | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                             |
| Estación Radio Sonda             | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                            |
| Estación Sinóptica Principal     | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos. |
| Estación Sinóptica Secundaria    | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.                                                                                                                                                                                                        |

#### Estado de la estación

| Estado           | Descripción                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activa           | Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.                                                                                            |
| En mantenimiento | Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.   |
| Suspendida       | Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones. |

####  Tecnología de la estación

| Estado                    | Descripción                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Convencional              | Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.                                                                                                                                                                        |
| Automática con telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)                                                                                     |
| Automática sin telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos. |

> De acuerdo a la nota del Anexo 2 del IDEAM: se debe tener en cuenta que la red es de tipo dinámico; es decir, a través de su operación se han instalado y suspendido estaciones a lo largo del territorio nacional, conservando en todo caso los datos históricos registrados. Esto significa que la sumatoria de las estaciones del Catálogo corresponde al número total de estaciones que han hecho parte de la red a través de su historia de operación y registro de información.


### Estructura de directorios

Para la ejecución correcta del script, es necesario clonar, descargar o crear la estructura de directorios definida en la siguiente tabla.

| Directorio                                                                                              | Descripción                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/BasicTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable)        | Directorio para volcado de tablas de estadísticos básicos y normalizados en formato de valores separados por comas [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).                                                                                                                                                                                               |
| [/Data](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Data)                    | Directorio de descarga del archivo CNE_IDEAM.xls con registro de versiones.                                                                                                                                                                                                                                                                                                   |
| [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph)                  | Directorio para volcado de gráficas en formato [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphic) .png. Para cada ejecución se crea un nuevo grupo de imágenes con registro de versiones.                                                                                                                                              |
| [/Graph/PlotMap](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph/PlotMap)  | Directorio para volcado de gráficas por departamento en formato [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphic) .png. Para cada ejecución se crea un nuevo grupo de imágenes con registro de versiones.                                                                                                                             |
| [/Old](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Old)                      | Directorio con versiones antiguas del script.                                                                                                                                                                                                                                                                                                                                 |
| [/PDF](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PDF)                      | Directorio de impresión de la ventana de ejecución del script. Directamente no se realiza la escritura en un archivo .log de resultados por lo que su impresión se realiza de forma manual. En este directorio pueden existir versiones para clasificación de pisos térmicos con rangos convencionales o con los rangos definidos por Francisco José de Caldas en el año 1802. |
| [/PivotTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable)        | Directorio para volcado de las tablas dinámicas producidas por el script en formato de valores separados por comas [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).  Para cada ejecución se crea un nuevo grupo de archivos .csv con registro de versiones.                                                                                                       |
| [/Reference](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Reference)          | Documentos de referencias bibliográficas recopiladas.                                                                                                                                                                                                                                                                                                                         |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Screenshot)        | Capturas de pantalla de ejecución y configuración.                                                                                                                                                                                                                                                                                                                            |

> Para los archivos generados u obtenidos a través de la ejecución del script, se conserva el registro de versiones a partir de la fecha de ejecución utilizando el formato aaaammdd.


### Script 

* Script principal [CNEStationStatistic.py](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationStatistic.py)
* Script diccionario [CNEStationDictionary.py](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationDictionary.py)


### Arreglos de datos para clasificación de estaciones por pisos térmicos


#### Cortes convencionales

| Valor de corte | Etiqueta                        |
|----------------|---------------------------------|
| 1000           | Cálido, 24°C+, <= 1000 meters   |
| 2000           | Templado, 18°C+, <= 2000 meters |
| 3000           | Frío, 12°C+, <= 3000 meters     |
| 4000           | Páramo, 0°C, <= 4000 meters     |
| 99999          | Glacial, 0°C-, > 4000 meters    |


#### Cortes Francisco José de Caldas, año 1802

| Valor de corte | Etiqueta                                    |
|----------------|---------------------------------------------|
| 800            | Cálido, T>=24°C, <=800meter                 |
| 1800           | Templado, 24°C>T>18°C, <=1800meter          |
| 2800           | Frío, 18°C>T>12°C, <=2800meter              |
| 3700           | Muy Frío, 12°C>T>6°C, <=3700meter           |
| 4700           | Extremadamente Frio, 6°C>T>0°C, <=4700meter |
| 99999          | Nival, T<0°C, >4700meter                    |


### Resumen general de datos analizados y publicados

Para cada ejecución del script principal, se analizan y publican en este repositorio diferentes [gráficas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph), [tablas básicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable) y [tablas dinámicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable) que son ordenadas cronológicamente y a partir de las cuales se presenta el siguiente resumen general. 

| Fecha       | Activa | Suspendida | En Mantenimiento  |
|-------------|--------|------------|-------------------|
| 2021.12.13  | 2643   | 1832       | 17                |
| 2021.12.14  | 2643   | 1832       | 17                |
| 2021.12.15  | 2643   | 1832       | 17                |


### Ejecución en PyCharm usando Python 3.10.0

> PyCharm requiere de configuración previa del intérprete de Python a utilizar en la ejecución del script. Oprima `Ctrl+Alt+S` para acceder a la ventana de configuración y en la pestaña _Project: R.GISPython_ configurar los intérpretes disponibles en su equipo.

![PyCharm2021.3SetupPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/PyCharm2021.3SetupPythonInterpreter.png)

Ventana de ejecución con atributos obtenidos. 
![Python3.10.0StandalonePyCharm2021.3Attributes.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3Attributes.png)

Ventana de ejecución con atributos estadísticas generales. 
![Python3.10.0StandalonePyCharm2021.3GeneralStatistic.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3GeneralStatistic.png)

Ventana de ejecución con tablas dinámicas. 
![Python3.10.0StandalonePyCharm2021.3PivotTable.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3PivotTable.png)

Ventana de ejecución con clasificación por piso térmico. 
![Python3.10.0StandalonePyCharm2021.3ThermalLevel.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Python3.10.0StandalonePyCharm2021.3ThermalLevel.png)


### Configuración para impresión de log de ejecución en PyCharm 2021.3

Configuración general de impresión.

![Pycharm2021.3RunSetupPrintSettings.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintSettings.png)

Configuración de cabecera y pie de página.

![Pycharm2021.3RunSetupPrintHeaderFooter.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintHeaderFooter.png)

Configuración avanzada.

![Pycharm2021.3RunSetupPrintAdvanced.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Screenshot/Pycharm2021.3RunSetupPrintAdvanced.png)


### Ejemplo de gráficas obtenidas

![CategoryPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/CategoryPivot20211214.png)
![GeoHydroAreaPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroAreaPivot20211214.png)
![GeoHydroSubzonePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroSubzonePivot20211214.png)
![GeoHydroZonePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoHydroZonePivot20211214.png)
![GeoOperativeAreaPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoOperativeAreaPivot20211214.png)
![GeoStatePivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/GeoStatePivot20211214.png)
![InstallationYearPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/InstallationYearPivot20211214.png)
![TechnologyPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/TechnologyPivot20211214.png)
![TechnologyPivotPie20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/TechnologyPivotPie20211214.png)
![ThermalLevelPivot20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/ThermalLevelPivot20211214.png)
![ThermalLevelPivotPie20211214.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/ThermalLevelPivotPie20211214.png)
![StationScatterPlotMapCundinamarca20211215.png](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/PlotMap/StationScatterPlotMapCundinamarca20211215.png)


### Referencias

* [Data Analysis with Python for Excel Users - Full Course](https://www.youtube.com/watch?v=WcDaZ67TVRo&t=84s)
* [Python program to print current year, month and day](https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/)
* [How to extract year from date in pandas](https://www.codegrepper.com/code-examples/python/how+to+extract+year+from+date+in+pandas)
* [How to display all rows from data frame using pandas](https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha)
* [How to rotate x-axis tick labels in Pandas barplot](https://stackoverflow.com/questions/32244019/how-to-rotate-x-axis-tick-labels-in-pandas-barplot)
* [Pandas dataFrame plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot)
* [Pandas dataframe plot bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
* [Pandas DataFrame Plot - Pie Chart](https://kontext.tech/column/code-snippets/402/pandas-dataframe-plot-pie-chart)
* [Make Better Bar Charts in Python using Pandas Plot](https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/)
* [Annotate bars with values on Pandas bar plots](https://stackoverflow.com/questions/25447700/annotate-bars-with-values-on-pandas-bar-plots)
* [Pandas pie plot actual values for multiple graphs](https://stackoverflow.com/questions/48299254/pandas-pie-plot-actual-values-for-multiple-graphs)
* [How to print an entire Pandas DataFrame in Python?](https://www.geeksforgeeks.org/how-to-print-an-entire-pandas-dataframe-in-python/)
* [How to filter rows containing a string pattern from a Pandas dataframe](https://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe)
* [Pandas: How to Find Unique Values in a Column](https://www.statology.org/pandas-unique-values-in-column/)
* [matplotlib get rid of max_open_warning output](https://stackoverflow.com/questions/27476642/matplotlib-get-rid-of-max-open-warning-output)
* [IDEAM Colombia - Clasificación de los climas (clima-text.pdf)](http://atlas.ideam.gov.co/basefiles/clima-text.pdf)
* [IDEAM Colombia - Clasificación climática de Caldas](http://www.ideam.gov.co/documents/10182/599272/Clasificacion+Climatica+de+Caldas+2014.pdf/d4ffa383-e60b-4ec5-8aa2-1b553d23b44f?version=1.0)
* [Pisos térmicos en Costa Rica](https://www.mep.go.cr/sites/default/files/recursos/recursos-interactivos/clima_tiempo/pdf/pisos_termicos.pdf)


### Autores

* Creado por r.cfdtools@gmail.com (32 horas)


### Compatibilidad

* Compatible con Python 3, librerías requeridas indicadas en la cabecera del archivo .py. 


### Tags
`IDEAM` `Stations` `Weather` `Plot` `matplotlib` `Pandas` `os` `Meteorological` `Automatic` `Pivot Table` `Graph` `Catalog`


### Control de versiones

| Versión     | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v.20211213  | Versión inicial con estadísticos básicos y clasificación de pisos térmicos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| v.20211214  | Incorporación de [gráficas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph) y [tablas dinámicas](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/PivotTable), inclusión de clasificación Caldas.                                                                                                                                                                                                                                                                                                                                                     |
| v.20211215 | Impresión de hiperenlaces en ventana de ejecución para cada gráfica y tabla dinámica generada. Generación de tablas con estadísticos básicos y normalizados en carpeta [/BasicTable](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/BasicTable). Creación de [diccionario](https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/CNEStationDictionary.py) general con impresión en consola. Gráfica de localización de estaciones por departamento en [/Graph/PlotMap](https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic/Graph/PlotMap) |


### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License


| [Actividad anterior](https://github.com/rcfdtools/R.GISPython/tree/main/LogScript) | [Actividad siguiente]() |
|------------------------------------------------------------------------------------|-------------------------|
