## Introducción a pandas - Representación 

[Pandas](https://pandas.pydata.org/) es una librería complementaria al lenguaje de programación Python que permite leer, representar y manipular datos almacenados en diferentes formatos, p.ej, en archivos de texto separados por comas _.csv_ [(CSV - Comma separated values)](https://en.wikipedia.org/wiki/Comma-separated_values) y archivos en formatos de libro de cálculo electrónico como [Microsoft Excel](https://es.wikipedia.org/wiki/Microsoft_Excel) en formato _.xls_ y _.xlsx_.


### Caso de estudio

Clasificar, representar y analizar la división geopolítica de los Municipios de Colombia a través de diferentes métodos de representación disponibles en ArcGIS, en función de su área espacial utilizando los datos abiertos del [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/).  


### Objetivos

* Utilizando ArcGIS for Desktop y ArcGIS Pro, simbolizar y representar en 5 clases, la capa geográfica de Municipios de Colombia utilizando los métodos de Cortes Naturales, Intervalo de Igualdad, Cuantil, Intervalo Geométrico y Desviación Típica.
* A partir de los valores de corte obtenidos y número de entidades (municipios) obtenidas en cada clase y método, crear archivos CSV y un libro de cálculo con diferentes hojas.
* Leer y visualizar los archivos CSV y las hojas del libro de Microsoft Excel en Python usando pandas a través de dataframes.
* Representar gráficamente los valores obtenidos utilizando la librería matplotlib y también a través de las funciones de graficación embebidas en pandas. 


### Requerimientos

* ArcGIS for Desktop 10.2.2+.
* ArcGIS Pro 2.9.0+.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.
* Capa geográfica de Municipio de Colombia.
* Archivos CSV y libro de Microsoft Excel con el resultado de los valores de corte y conteo de elementos.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7 de Python.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\PandasBasic\ 


### Descarga de capa de municipios

> Tenga en cuenta que el procedimiento de descarga puede no estar actualizado debido a las actualizaciones permanentes que se realizan en el portal del IGAC, sin embargo, podrá utilizar los archivos descargados y utilizados para ejemplificar el caso de estudio que se encuentran en este repositorio. Descarga realizada en 2021.12.16.

1. En el portal del [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/) de clic en la opción de [Datos Abiertos]().

![IGACDatosAbiertos.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/IGACDatosAbiertos.png)

2. En Datos Abiertos, seleccione la opción [Cartografía y Geografía](https://geoportal.igac.gov.co/contenido/datos-abiertos-cartografia-y-geografia) y luego seleccione la opción [Cartografía Base Escala 1:25000](https://www.colombiaenmapas.gov.co/?e=-82.43784778320864,-0.17644239911865092,-71.23179309571162,9.90326984502256,4686&b=igac&u=0&t=23&servicio=206) contenida en la sección Descarga de Información Integrada. Automáticamente será redirigido al portal [colombiaenmapas.gov.co](https://www.colombiaenmapas.gov.co/).

![IGACCartografiaGeografia.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/IGACCartografiaGeografia.png)
![IGACCartografiaBaseEscala1a25000.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/IGACCartografiaBaseEscala1a25000.png)

3. En el portal de Colombia en Mapas, filtre por Municipios, de clic en la opción _Municipios, Distritos y Áreas no municipalizadas de Colombia_, seleccione formato [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm) y luego en el botón Descargar. Automáticamente se creará una orden de servicio y se iniciará la descarga (p.ej, Servicio-610.zip).

![IGACColombiaMapasDescarga.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/IGACColombiaMapasDescarga.png)

4. En la carpeta `/Datos`, descomprima el archivo de Municipios, observará que el [shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm) se compone de diferentes archivos (p.ej, .shp, .shx, .dbf y .prj). 

![DatosShapefileMunicipios.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/DatosShapefileMunicipios.png)


### Procedimiento para la creación de tablas requeridas 


#### En ArcGIS for Desktop 10.2.2

1. En ArcMap, cree un mapa en blanco y agregue la capa descargada municipios202110.

![ArcGISDesktopAddLayer.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopAddLayer.png)

2. Abra la tabla de atributos de la capa (clic derecho en la capa, _Open Attribute Table_), acóplela a la derecha de la ventana y desde las propiedades de la tabla, cree un nuevo campo de atributos tipo numérico doble usando la opción `Add Field...` y nombrelo como `Areakm2`.

![ArcGISDesktopAddField.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopAddField.png)

3. Utilizando el calculador de geometría, calcule el valor del área espacial en km² de todos los polígonos de la capa. Clic derecho en la cabecera del campo `Areakm2` y `Calculate Geometry...`.

> Podrá observar que la capa contiene un campo denominado `MpArea` que ya contiene el cálculo en km², sin embargo, se recomienda que sea creado el campo `Areakm2` para actualizar los valores a partir del sistema de proyección _MARNA-SIRGAS / Origen Nacional_ embebido en la capa.

![ArcGISDesktopCalculateGeometry.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopCalculateGeometry.png)

4. Desde las propiedades de la capa, realice la simbolización por Cantidades y por colores graduados en 5 clases a partir del campo `Areakm2` para los métodos de clasificación Cortes Naturales - Jenks, Intervalo de Igualdad, Cuantil, Intervalo Geométrico y Desviación Típica. Para las representaciones, utilice paleta de verdes a naranjas y transparencia del 50%.

![ArcGISDesktopEqualInterval.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopEqualInterval.png)
![ArcGISDesktopGeometricalInterval.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopGeometricalInterval.png)
![ArcGISDesktopNaturalBreaksJenks.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopNaturalBreaksJenks.png)
![ArcGISDesktopQuantile.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopQuantile.png)
![ArcGISDesktopStandardDeviation.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/ArcGISDesktopStandardDeviation.png)

5. En Microsoft Excel, cree en la carpeta `/Datos` un libro en formato .xlsx y guárdelo como [GISClassificationMethodValue.xlsx](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Datos/GISClassificationMethodValue.xlsx). Dentro del libro cree las siguientes hojas y registre los valores, porcentajes y conteos de elementos obtenidos en las diferentes clasificaciones:

| Hoja             | Descripción                                       |
|------------------|---------------------------------------------------|
| ArcMapValor      | Registro de valores de corte para cada clase.     |
| ArcMapPercentage | Registro de porcentajes de corte para cada clase. |
| ArcMapCount      | Registro de conteo de elementos para cada corte.  |

![MicrosoftExcelArcMapValor.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/MicrosoftExcelArcMapValor.png)
![MicrosoftExcelArcMapPercentage.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/MicrosoftExcelArcMapPercentage.png)
![MicrosoftExcelArcMapCount.png](https://github.com/rcfdtools/R.GISPython/blob/main/PandasBasic/Screenshot/MicrosoftExcelArcMapCount.png)






### Referencias

* [Pandas - Oficial](https://pandas.pydata.org/)
* [Pandas - Read Excel files](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
* [Pandas - Read CSV files](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
* [Pandas - Plotting](https://pandas.pydata.org/pandas-docs/stable/reference/plotting.html)
* [Pandas - Dataframe Plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
* [Wikipedia - Pandas (software)](https://es.wikipedia.org/wiki/Pandas_(software))
