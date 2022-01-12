## Obtención de datos climatológicos utilizando la API de openweathermap.org y el  Catálogo nacional de estaciones hidrometeorológicas - CNE del IDEAM - Colombia
keywords: `openweathermap` `forecast` `historical` `pandas` `matplotlib` `API`

A partir de la localización geográfica de estaciones hidrometeorológicas y utilizando la interfaz de programación de aplicaciones - API del portal openweathermap.org, obtener datos históricos o datos de pronóstico para las variables climatológicas: temperatura, sensación térmica, punto de rocío, nubosidad, humedad, presión atmosférica, dirección del viento, velocidad del viento, velocidad de ráfagas de viento, precipitación, visibilidad e índice ultravioleta - UVI.

### Caso de estudio

Análisis de datos climatológicos históricos en la ciudad de Bogotá - Colombia para todos los tipos y estados de estaciones registradas en el Catálogo Nacional del [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/). 

> La ventana de tiempo para consulta de datos históricos mediante la API de OWM es de 5 días antes, incluida la fecha actual.

> El script de descarga y procesamiento también permite la realización de descarga de datos tipo pronóstico para datos a partir de la fecha y hora actual de ejecución más una ventana de tiempo que puede estar al rededor de 1 semana dependiendo de la localización consultada y los datos disponibles.  


### Funcionalidades incorporadas

* Descarga directa del archivo del catálogo nacional de estaciones. Si en la fecha actual ya ha sido descargado el archivo, el script realizará únicamente su procesamiento.
* Configuración inicial modificable por el usuario para definir ruta de descarga `urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls`
* 
 
> En caso de que requiera analizar una versión antigua del archivo del catálogo nacional de estaciones, podrá cargar el archivo en cualquier repositorio de uso personal, redireccionar el script a la url del archivo y ejecutar el script. Tener en cuenta que las fechas presentadas en los análisis, corresponderán a la fecha del sistema operativo. Opcionalmente podrá crear una copia del archivo a analizar y modificar la fecha incluida en el nombre del archivo a la fecha actual en formato aaaammdd.

> En el evento de que por reestructuración del modelo de datos IDEAM, desaparezca alguno de los campos utilizados para el análisis general y la creación de las tablas dinámicas, el usuario deberá crear manualmente en el archivo .xls fuente, las columnas requeridas para la ejecución correcta del script.   


### Requerimientos

* API Key de https://openweathermap.org
* Python 3.10.0+ como instalación independiente o standalone.
* Matplotlib 3.5.0
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.

> La API Key requerida puede ser libre o comercial. Para cuentas de usuario por descarga libre, el número de consultas únicas por día no debe exceder de 1000.  


### References
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