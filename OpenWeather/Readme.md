## Obtención y análisis de datos climatológicos utilizando la API de openweathermap.org y el  Catálogo nacional de estaciones hidrometeorológicas - CNE del IDEAM - Colombia
Keywords: `openweathermap` `forecast` `historical` `pandas` `matplotlib` `API`

A partir de la localización geográfica de estaciones hidrometeorológicas y utilizando la interfaz de programación de aplicaciones - API del portal openweathermap.org, obtener datos históricos o datos de pronóstico para las variables climatológicas: temperatura, sensación térmica, punto de rocío, nubosidad, humedad, presión atmosférica, dirección del viento, velocidad del viento, velocidad de ráfagas de viento, precipitación, visibilidad e índice ultravioleta - UVI.

### Caso de estudio

Análisis de datos climatológicos históricos en la ciudad de Bogotá - Colombia para todos los tipos y estados de estaciones registradas en el Catálogo Nacional del [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/). 

> La ventana de tiempo para consulta de datos históricos mediante la API de OWM es de hasta 5 días anteriores incluida la fecha actual.

> El script de descarga y procesamiento también permite la realización de descarga de datos pronóstico a partir de la fecha y hora actual de ejecución más una ventana de tiempo que puede estar al rededor de 1 semana dependiendo de la localización consultada y los datos disponibles.  


### Funcionalidades incorporadas

* Descarga directa del archivo del catálogo nacional de estaciones. Si en la fecha actual ya ha sido descargado el archivo, el script realizará únicamente su procesamiento.
* Configuración inicial modificable por el usuario para definir ruta de descarga `urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls` y los nombre de los atributos del modelo de datos del catálogo.
* Definición de filtros de procesamiento de estaciones por: código de estación, categoría, tecnología, estado, departamento, municipio, corriente, área operativa, área hidrográfica, zona hidrográfica y subzona hidrográfica. 
* Para datos históricos (máximo 5 días incluida la fecha de ejecución actual), el usuario puede definir el número de días previos a la fecha actual sobre el cual se realizará la obtención y análisis de los datos climatológicos disponibles en OWM.
* Procesamiento automático de diccionario JSON obtenido mediante la API de OWM a formato de texto separado por comas - CSV. Todos los datos discretos obtenidos para las localizaciones definidas a partir de las estaciones son procesados a escala horaria y volcados a un archivo único en `/Output`.
* Generación automática de archivos de reporte detallados en formato Markdown para cada estación procesada de acuerdo a los filtros definidos.
* Impresión detallada de datos y metadatos de cada estación procesada.
* Impresión detallada de tabla de datos climáticos por estación con iconografía oficial de OWM.
* Hipervinculación activa en reporte para visualización de localización de estación en Google Maps y OpenStreet Map.
* Definición del sistema de unidades para la obtención de datos de OWM e impresión de tabla detallada de referencia del sistema de unidades utilizado.
* Impresión detallada del catálogo de objetos del archivo CSV generado.
* Generación masiva de gráficas de análisis para las estaciones procesadas y para cada tipo de dato climatológicos obtenido. Gráficas embebidas dentro del documento principal de cada estación.
 
> En caso de que requiera analizar una versión antigua del archivo del catálogo nacional de estaciones, podrá cargar el archivo en cualquier repositorio de uso personal, redireccionar el script a la url del archivo y ejecutar el script. Tener en cuenta que las fechas presentadas en los análisis, corresponderán a la fecha del sistema operativo. Opcionalmente podrá crear una copia del archivo a analizar y modificar la fecha incluida en el nombre del archivo a la fecha actual en formato aaaammdd.

> En el evento de que por reestructuración del modelo de datos IDEAM, desaparezca alguno de los campos utilizados para el análisis general y la creación de las tablas dinámicas, el usuario deberá crear manualmente en el archivo .xls fuente, las columnas requeridas para la ejecución correcta del script.

> Mediante la inclusión del parámetro 'All' al inicio del arreglo de filtrado para cada uno de los filtros disponibles, el script identifica que se requiere de todos los datos disponibles, por lo que no es necesario eliminar las demás entradas ya definidas. 

> Para localizaciones diferentes a las obtenidas a través del CNE, puede crear un archivo .xls con diferentes estaciones virtuales y con la misma estructura de datos. El archivo deberá identificarse con el mismo nombre del catálogo agregando al final la fecha de procesamiento. 

### Requerimientos

* API key de [OWM](https://openweathermap.org)
* Python 3.10.0+ como instalación independiente o standalone.
* Matplotlib 3.5.0
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.

> La API Key requerida puede ser libre o comercial. Para cuentas de usuario por descarga libre, el número de consultas únicas por día no debe exceder de 1000.  


### Parámetros y sistema de unidades disponibles

| Parameter | Unit metric system | Unit imperial system | openweathermap name |
|---|---|---|---|
| Temperature | °C | °F | temp |
| Dew Point | °C | °F | dew_point |
| Feels like | °C | °F | feels_like |
| Clouds | % | % | clouds |
| Humidity | % | % | humidity |
| Pressure | hPa | hPa | pressure |
| Wind Direction | ° | ° | wind_deg |
| Wind Speed | m/s | mi/h | wind_speed |
| Wind Gust | m/s | mi/h | wind_gust |
| Rain | mm | mm | rain |
| Visibility | m | m | visibility |
| UV Index | DN | DN | uvi |

> mi: Miles unit for imperial system

> DN: Dimensionless numbers


### Catálogo de objetos del archivo CSV generado

| r.cfdtools | CNE IDEAM | OpenWeather | Description |
|---|---|---|---|
| Station | CODIGO | N/A | Station code |
| Statname | nombre | N/A | Station name |
| Latitude | latitud | lat | Geolocalization latitude degrees |
| Longitude | longitud | lon | Geolocalization longitude degrees |
| Elevation | altitud | N/A | Elevation over the sea level |
| Category | CATEGORIA | N/A | Station category: pluviometric, limnimetric, pluviograph, limnigraph, ordinary climatology, principal climatology, special meteorologic, soil meteorological, main synoptic, secundary synotic, radiosonde, mareographic |
| Technology | TECNOLOGIA | N/A | Main technology: conventional, automatic assisted with telemetry, automatic not assisted with telemetry |
| Status | ESTADO | N/A | Functional status: active, suspended, under maintenance |
| InstDate | FECHA_INSTALACION | N/A | Installation date |
| SuspDate | FECHA_SUSPENSION | N/A | Suspension date |
| State | DEPARTAMENTO | N/A | Geopolitical location state |
| County | MUNICIPIO | N/A | Geopolitical location county |
| Stream | CORRIENTE | N/A | Stream point or near stream |
| Operator | AREA_OPERATIVA | N/A | Gouvernament operator |
| AHName | AREA_HIDROGRAFICA | N/A | AH - Hydrographic area. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZName | ZONA_HIDROGRAFICA | N/A | ZH - Hydrographic zone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZHName | SUBZONA_HIDROGRAFICA | N/A | SZH - Hydrographic subzone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| Timezone | N/A | timezone | Global time zone |
| Datetime | N/A | N/A | Date and time of the weather values |
| Clouds | N/A | clouds | Cloudiness |
| Dewpoint | N/A | dew_point | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. |
| Feelslike | N/A | feels_like | Temperature. This temperature parameter accounts for the human perception of weather |
| Humidity | N/A | humidity | Humidity |
| Pressure | N/A | pressure | Atmospheric pressure on the sea level |
| Rain | N/A | rain | Rain volume for last hour |
| Temp | N/A | temp | Temperature |
| UVI | N/A | uvi | Current UV index |
| Visibility | N/A | visibility | Average visibility |
| Winddeg | N/A | wind_deg | Wind direction, degrees (meteorological) |
| Windgust | N/A | wind_gust | Wind gust |
| Windspeed | N/A | wind_speed | Wind speed |
| OWMid | N/A | id | Weather identification over OWM |
| OWMmain | N/A | main | Group of weather parameters (Rain, Snow, Extreme etc.) |
| OWMdesc | N/A | description | Weather condition within the group. [More info.](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2) |
| OWMicon | N/A | icon | Weather icon id. [More info.](https://openweathermap.org/weather-conditions#How-to-get-icon-URL) |
| Hour | N/A | N/A | Hour can be used like a Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API


### Estructura de directorios

Para la ejecución correcta del script, es necesario clonar, descargar o crear la estructura de directorios definida en la siguiente tabla en el directorio `D:\R.GISPython\OpenWeather`.

| Directorio                                                                               | Descripción                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [/Data](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather/Data)             | Directorio de descarga del archivo CNE_IDEAM.xls con registro de versiones.                                                                                                                                                                           |
| [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather/Graph)           | Directorio para volcado de gráficas en formato [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphic) .png. Para cada ejecución por fecha y estación se crea un nuevo grupo de imágenes con registro de versiones. |
| [/Old](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather/Old)               | Directorio con versiones antiguas de los script.                                                                                                                                                                                                      |
| [/Output](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather/Output)         | Directorio de volcado de archivos detallados por estación en formato Markdown y archivo único CSV.                                                                                                                                                    |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather/Screenshot) | Capturas de pantalla de ejecución y configuración.                                                                                                                                                                                                    |

> Para los archivos generados u obtenidos a través de la ejecución del script, se conserva el registro de versiones a partir de la fecha de ejecución utilizando el formato aaaammdd.


### Ejecución en PyCharm usando Python 3.10.0


#### Ejecución script principal

![PyCharm2021.3OpenWeather1.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeather1.png)
![PyCharm2021.3OpenWeather2.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeather2.png)
![PyCharm2021.3OpenWeather3.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeather3.png)
![PyCharm2021.3OpenWeather4.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeather4.png)
![PyCharm2021.3OpenWeather5.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeather5.png)


#### Ejecución script generación masiva de gráficas de análisis

![PyCharm2021.3OpenWeatherPlot1.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeatherPlot1.png)
![PyCharm2021.3OpenWeatherPlot2.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/PyCharm2021.3OpenWeatherPlot2.png)


#### Resultados

![GitHubMarkdownOutputSample1.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/GitHubMarkdownOutputSample1.png)
![GitHubMarkdownOutputSample2.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/GitHubMarkdownOutputSample2.png)
![GitHubMarkdownOutputSample3.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/GitHubMarkdownOutputSample3.png)
![NotepadMarkdownOutputSample.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/NotepadMarkdownOutputSample.png)
![WindowsExplorerGraph.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/WindowsExplorerGraph.png)
![WindowsExplorerOutput.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Screenshot/WindowsExplorerOutput.png)




### Scripts

#### Script principal [OpenWeather.py](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/OpenWeather.py)

```

```

#### Script para generación masiva de gráficas de análisis OpenWeatherPlot.py](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/OpenWeatherPlot.py) 

```

```


### Referencias

* https://openweathermap.org
* https://towardsdatascience.com/develop-your-weather-application-with-python-in-less-than-10-lines-6d092c6dcbc9
* https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timeStamp
* https://www.youtube.com/watch?v=9N6a-VLBa2I
* https://realpython.com/python-json/
* https://knasmueller.net/using-the-open-weather-map-api-with-python
* https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
* https://stackoverflow.com/questions/3327946/how-can-i-get-the-current-time-now-in-utc
* https://pynative.com/python-check-if-key-exists-in-json-and-iterate-the-json-array/
* https://www.epa.gov/sites/default/files/documents/uviguide.pdf
* https://stackoverflow.com/questions/44177417/how-to-display-openweathermap-weather-icon
* https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte
* https://stackoverflow.com/questions/48668580/filter-csv-with-pandas
* https://www.pythonprogramming.in/customize-grid-color-and-style.html
* https://gitanswer.com/pixmap-error-python-pytorch-forecasting-909130815


### Autores

* Creado por r.cfdtools@gmail.com (40 horas)


### Compatibilidad

* Compatible con Python 3, librerías requeridas indicadas en la cabecera del archivo .py. 


### Control de versiones

| Versión    | Descripción                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------|
| v.20220112 | Versión inicial con volcado de datos obtenidos en archivo CSV y generación masiva de gráficas de análisis. |


### Licencia, cláusulas y condiciones de uso

R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]()  |
|------------------------|---------------------------------------------------------|--------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_