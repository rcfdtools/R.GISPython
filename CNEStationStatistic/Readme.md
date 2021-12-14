## Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia, descarga y análisis usando Python

<div  align="center">
    <img align="center"  alt="StationScatterPlotMap20211213.png" src="https://github.com/rcfdtools/R.GISPython/blob/main/CNEStationStatistic/Graph/StationScatterPlotMap20211213.png" width="800px"/>
</div>

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

El presente repositorio y el código desarrollado en Python por r.cfdtools@gmail.com, permite descargar de forma automática el archivo del catálogo nacional de estaciones y realizar un análisis estadístico detallado a través de los diferentes clasificadores registrados.

### Funcionalidades

* Descarga automática del archivo del catálogo nacional de estaciones
* 

### Atributos que componen el catálogo nacional de estaciones

Atributos tomados directamente del archivo [CNE_IDEAM.xls](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls).

| Atributo | Tipo | Descripción                                                                                                                                                                                                                                     |
|----------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID | int64 | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                   |
| CODIGO | int64 | Código de la estación.                                                                                                                                                                                                                          |
| nombre | object | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                        |
| CATEGORIA | object | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria.  |
| TECNOLOGIA | object | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                            |
| ESTADO | object | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                 |
| FECHA_INSTALACION | datetime64[ns] | Fecha de instalación.                                                                                                                                                                                                                           |
| altitud | int64 | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                                |
| latitud | float64 | Latitud en grados decimales.                                                                                                                                                                                                                    |
| longitud | float64 | Longitud en grados decimales.                                                                                                                                                                                                                   |
| DEPARTAMENTO | object | Departamento o zonificación política. Equivalente a estados en otros países.                                                                                                                                                                    |
| MUNICIPIO | object | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                    |
| AREA_OPERATIVA | object | Área operativa que administra la estación.                                                                                                                                                                                                      |
| AREA_HIDROGRAFICA | object | Área hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| ZONA_HIDROGRAFICA | object | Zona hidrográfica a la cual pertenece.                                                                                                                                                                                                          |
| observacion | object | Observaciones generales.                                                                                                                                                                                                                        |
| CORRIENTE | object | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                     |
| FECHA_SUSPENSION | datetime64[ns] | Fecha de suspensión.                                                                                                                                                                                                                            |
| SUBZONA_HIDROGRAFICA | object | Subzona hidrográfica a la cual pertenece.                                                                                                                                                                                                       |
| ENTIDAD | object | Entidad encargada.                                                                                                                                                                                                                              |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres.

### Definiciones generales del catálogo nacional de estaciones

Tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.

#### Categorías de las estaciones

| Categoría                        | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo)                                                                                     |
| Estación Climatológica Ordinaria | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                               |
| Estación Climatológica Principal | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores                                                                                                                                                           |
| Estación Limnigráfica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                      |
| Estación Limnimétrica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                      |
| Estación Mareográfica            | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Estación meteorológica especial  | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                            |
| Estación Radio Sonda             | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                           |
| Estación Sinóptica Principal     | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos |
| Estación Sinóptica Secundaria    | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento                                                                                                                                                                                                        |

#### Estado de la estación

| Estado | Descripción                                                                                                                                                                                |
|  --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activa | Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.                                                                                           |
| En mantenimiento | Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.  |
| Suspendida | Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones |

####  Tecnología de la estación

| Estado | Descripción                                                                                                                                                                                                                                                                                                                                 |
|  --- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Convencional | Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.                                                                                                                                                                        |
| Automática con telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)                                                                                     |
| Automática sin telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos. |

> De acuerdo a la nota del Anexo 2: Se debe tener en cuenta que la red es de tipo dinámico; es decir, a través de su operación se han instalado y suspendido estaciones a lo largo del territorio nacional, conservando en todo caso los datos históricos registrados. Esto significa que la sumatoria de las estaciones del Catálogo corresponde al número total de estaciones que han hecho parte de la red a través de su historia de operación y registro de información.




Data sample with Pandas from https://www.codegrepper.com/
```
df['date'] = pd.to_datetime(df['date'],format='%Y%m%d')
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month

#Exctract month and create a dedicated column df["Month"] from a 
#column in datetime format df["Date"]
df['Month'] = pd.DatetimeIndex(df['Date']).month
```


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
* [IDEAM Colombia - Clasificación de los climas (clima-text.pdf)](http://atlas.ideam.gov.co/basefiles/clima-text.pdf)
* [IDEAM Colombia - Clasificación climática de Caldas](http://www.ideam.gov.co/documents/10182/599272/Clasificacion+Climatica+de+Caldas+2014.pdf/d4ffa383-e60b-4ec5-8aa2-1b553d23b44f?version=1.0)
* [Pisos térmicos en Costa Rica](https://www.mep.go.cr/sites/default/files/recursos/recursos-interactivos/clima_tiempo/pdf/pisos_termicos.pdf)
