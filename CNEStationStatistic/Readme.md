## Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia, descarga y análisis

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

El presente repositorio y el código desarrollado en Python, permite descargar de forma automática el archivo del catálogo nacional de estaciones y realizar un análisis estadístico detallado a través de los diferentes clasificadores registrados.

### Funcionalidades

* Descarga automática del archivo del catálogo nacional de estaciones
* 

### Atributos que componen el catálogo nacional de estaciones

| Atributo | Tipo | Descripción                                                                                                                                                                                                                                    |
|----------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID | int64 | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                  |
| CODIGO | int64 | Código de la estación.                                                                                                                                                                                                                         |
| nombre | object | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                       |
| CATEGORIA | object | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria. |
| TECNOLOGIA | object | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                           |
| ESTADO | object | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                |
| FECHA_INSTALACION | datetime64[ns] | Fecha de instalación.                                                                                                                                                                                                                          |
| altitud | int64 | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                               |
| latitud | float64 | Latitud en grados decimales.                                                                                                                                                                                                                   |
| longitud | float64 | Longitud en grados decimales.                                                                                                                                                                                                                  |
| DEPARTAMENTO | object | Departamento o zonificación política. Equivalente a estados en otros países.                                                                                                                                                                   |
| MUNICIPIO | object | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                   |
| AREA_OPERATIVA | object | Área operativa que administra la estación.                                                                                                                                                                                                     |
| AREA_HIDROGRAFICA | object | Área hidrográfica a la cual pertenece.                                                                                                                                                                                                         |
| ZONA_HIDROGRAFICA | object | Zona hidrográfica a la cual pertenece.                                                                                                                                                                                                         |
| observacion | object | Observaciones generales.                                                                                                                                                                                                                       |
| CORRIENTE | object | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                    |
| FECHA_SUSPENSION | datetime64[ns] | Fecha de suspensión.                                                                                                                                                                                                                           |
| SUBZONA_HIDROGRAFICA | object | Subzona hidrográfica a la cual pertenece.                                                                                                                                                                                                      |
| ENTIDAD | object | Entidad encargada.                                                                                                                                                                                                                             |



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
