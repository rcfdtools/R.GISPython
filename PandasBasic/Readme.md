## Introducción a pandas

[Pandas](https://pandas.pydata.org/) es una librería complementaria del lenguaje de programación Python que permite leer, representar y manipular datos almacenados en diferentes formatos, p.ej, en archivos de texto separados por comas _.csv_ [(CSV - Comma separated values)](https://en.wikipedia.org/wiki/Comma-separated_values) y archivos en formatos de libro de cálculo electrónico como [Microsoft Excel](https://es.wikipedia.org/wiki/Microsoft_Excel) en formato _.xls_ y _.xlsx_.


### Caso de estudio

Clasificar, representar y analizar la división geopolítica de los Municipios de Colombia a través de diferentes métodos de representación en función de su área espacial utilizando los datos abiertos del [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/).  


### Objetivos

* Utilizando ArcGIS for Desktop y ArcGIS Pro, simbolizar y representar en 5 clases, la capa geográfica de Municipios de Colombia utilizando los métodos de Cortes Naturales, Intervalo de Igualdad, Cuantil, Intervalo Geométrico y Desviación Típica.
* A partir de los valores de corte obtenidos y número de entidades (municipios) obtenidas en cada clase y método, crear archivos CSV y un libro de cálculo con diferentes hojas.
* Leer y visualizar los archivos CSV y las hojas del libro de Microsoft Excel en Python usando pandas a través de dataframes.
* Representar gráficamente los valores obtenidos utilizando la librería matplotlib y también a través de las funciones de graficación embebidas en pandas. 


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* Python 3.10.0+ como instalación independiente o standalone.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7 de Python.


### Procedimiento para la creación de las tablas requeridas 


#### Descarga de capa de municipios

1. En el portal del [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/) de clic en la opción de [Datos Abiertos]().



#### En ArcGIS for Desktop 10.2.2

1. 


### Referencias

* [Pandas - Oficial](https://pandas.pydata.org/)
* [Pandas - Read Excel files](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
* [Pandas - Read CSV files](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
* [Pandas - Plotting](https://pandas.pydata.org/pandas-docs/stable/reference/plotting.html)
* [Pandas - Dataframe Plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
* [Wikipedia - Pandas (software)](https://es.wikipedia.org/wiki/Pandas_(software))
