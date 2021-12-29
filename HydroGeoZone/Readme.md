## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python
Keywords: `arcpy` `env` `arcpy.env.workspace` `arcpy.env.overwriteOutput` `datetime` `time` `Kc` `Gravelius` `Dd` `Dc` `arcpy.GetCount_management()` `arcpy.Describe()` `shapeType` `arcpy.ListFields()` `matplotlib` `arcpy.Statistics_analysis` `arcpy.SearchCursor()` `getValue()` `arcpy.Dissolve_management()` `arcpy.JoinField_management` `arcpy.AddField_management()` `arcpy.CalculateGeometryAttributes_management()` `arcpy.Intersect_analysis()` `arcpy.Statistics_analysis()` `arcpy.JoinField_management()` `arcpy.TableToExcel_conversion()` `open()` `.write()` `close()` 

![HydroGeoZone.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/HydroGeoZone.png)

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p.ej, el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico.[^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.[^2]

| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales.[^2]

![SZHSubzonaHidrografica2013.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrografica2013.png)

| AH  | Área Hidrográfica | ZH  | Zona Hidrográfica                  |
|-----|-------------------|-----|------------------------------------|
| 1   | Caribe            | 11  | Atrato - Darién                    |
| 1   | Caribe            | 12  | Caribe - Litoral                   |
| 1   | Caribe            | 13  | Sinú                               |
| 1   | Caribe            | 15  | Caribe - La Guajira                |
| 1   | Caribe            | 16  | Catatumbo                          |
| 1   | Caribe            | 17  | Islas del Caribe                   |
| 2   | Magdalena - Cauca | 21  | Alto Magdalena                     |
| 2   | Magdalena - Cauca | 22  | Saldaña                            |
| 2   | Magdalena - Cauca | 23  | Medio Magdalena                    |
| 2   | Magdalena - Cauca | 24  | Sogamoso                           |
| 2   | Magdalena - Cauca | 25  | Bajo Magdalena - Cauca - San Jorge |
| 2   | Magdalena - Cauca | 26  | Cauca                              |
| 2   | Magdalena - Cauca | 27  | Nechí                              |
| 2   | Magdalena - Cauca | 28  | Cesar                              |
| 2   | Magdalena - Cauca | 29  | Bajo Magdalena                     |
| 3   | Orinoco           | 31  | Inírida                            |
| 3   | Orinoco           | 32  | Guaviare                           |
| 3   | Orinoco           | 33  | Vichada                            |
| 3   | Orinoco           | 34  | Tomo                               |
| 3   | Orinoco           | 35  | Meta                               |
| 3   | Orinoco           | 36  | Casanare                           |
| 3   | Orinoco           | 37  | Arauca                             |
| 3   | Orinoco           | 38  | Orinoco Directos                   |
| 3   | Orinoco           | 39  | Apure                              |
| 4   | Amazonas          | 41  | Guainía                            |
| 4   | Amazonas          | 42  | Vaupés                             |
| 4   | Amazonas          | 43  | Apaporis                           |
| 4   | Amazonas          | 44  | Caquetá                            |
| 4   | Amazonas          | 45  | Yarí                               |
| 4   | Amazonas          | 46  | Caguán                             |
| 4   | Amazonas          | 47  | Putumayo                           |
| 4   | Amazonas          | 48  | Amazonas - Directos                |
| 4   | Amazonas          | 49  | Napo                               |
| 5   | Pacífico          | 51  | Mira                               |
| 5   | Pacífico          | 52  | Patía                              |
| 5   | Pacífico          | 53  | Tapaje - Dagua - Directos          |
| 5   | Pacífico          | 54  | San Juan                           |
| 5   | Pacífico          | 55  | Baudó - Directos Pacífico          |
| 5   | Pacífico          | 56  | Pacífico - Directos                |
| 5   | Pacífico          | 57  | Islas del Pacífico                 |

> En el presente análisis no se han incluido resultados para la ZH - zona hidrográfica 57 correspondiente a las Islas del Pacífico, debido a que la capa geográfica SZH - subzonas hidrográficas no contiene el polígono de delimitación. 


### Caso de estudio

Estudiar la forma y densidad de las áreas, zonas y subzonas hidrográficas de Colombia a partir de la delimitación geográfica realizada por el [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/) y la red de drenajes sencillos digitalizada a escala 1:100k por el [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/).

Análisis de forma y densidad

| Parámetro | Descripción                    | Fórmula                                                               | 
|-----------|--------------------------------|-----------------------------------------------------------------------|
| Kc        | Índice de compacidad Gravelius | Kc = P / (2π ( A / π ) ^ 0.5 )<br>Kc = 0.28209479179826 * P / A ^ 0.5 |
| Dd        | Densidad de drenajes, km/km²   | Dd = Σ LCi / A                                                        |
| Dc        | Densidad de corrientes, 1/km²  | Dd = n / A                                                            |

Donde,
* P, perímetro de la zona hidrográfica en kilómetros.
* A, área de la zona hidrográfica hen km².
* LCi, longitud de cada cauce o corriente de agua.
* n, número de cauces o corrientes de agua.

Para la marcación complementaria del coeficiente de compacidad Kc, se utilizará la clasificación de la [Autoridad Nacional de Licencias Ambientales de Colombia - ANLA](https://www.anla.gov.co/), cuya clasificación en el modelo nacional de datos geográficos establecido en el dominio `Dom_Forma_IndComp` relacionado con la capa geográfica `CuencaHidrografica` del componente `HIDROLOGIA`, indica que se subclasifican en los siguientes 3 tipos: [^6] 

| Código | Descripción                        | Valor de referencia [^7] | 
|--------|------------------------------------|--------------------------|
| 1001   | Casi redonda a oval redonda        | 1 a 1.25                 |
| 1002   | Oval-redonda a oval oblonga        | 1.25 a 1.5               |
| 1003   | Oval-oblonga a rectangular-oblonga | > 1.5                    |


### Objetivos

* Identificar las AH - áreas hidrográficas, ZH - zonas hidrográficas y SZH - subzonas hidrográficas de Colombia - Suramérica.
* Mediante intersección espacial, determinar el número y longitud de drenajes en cada zonificación.
* Estimar los coeficientes de forma y densidad en cada zonificación.
* Ejecutar varias de las funciones de geoprocesamiento disponibles en ArcPy de ArcGIS.  


### Requerimientos

* [Python 2.7+ de ArcGIS for Desktop 10.6+](https://www.esri.com/en-us/home)
* [ArcGIS Pro 2.9+](https://www.esri.com/en-us/home)
* [PyCharm 2021.3+ Commmunity](https://www.jetbrains.com/pycharm/download/#section=windows) 
* [Sistema operativo Microsoft Windows](https://www.microsoft.com/en-us/windows?r=1)
* [matplotlib](https://matplotlib.org/)

> Para la ejecución del script principal, no es necesaria la instalación de librerías adicionales en ArcGIS, sin embargo, para la versión Desktop es requerida como mínimo la versión 10.6 para el cálculo directo de los parámetros geométricos de las entidades a través de la función `CalculateGeometryAttributes_management()`.


### Funcionalidades

* Creación automática de log de resultados en formato Markdown con impresión de versión en archivo de salida.
* Parametrización general con definición de rutas, nombres de campos de entrada y activación o desactivación de subprocesos intermedios principales. El usuario puede modificar el arreglo de datos para la sub-clasificación de las zonificaciones por rango de área y los clasificadores del índice de compacidad.
* Impresión de propiedades y entidades encontradas para las capas de entrada.
* Estadísticos generales de drenajes por subtipo.
* Evaluación a partir de todos los subtipos de drenajes disponibles (sin subtipo, permanentes, intermitentes) o solo para drenajes permanentes. Los archivos de registro de resultados contienen la etiqueta `All` y `Per` que identifica el tipo de drenajes utilizados.
* Reproyección automática de la capa original SZH - subzonas hidrográficas al sistema de coordenadas `9377 MAGNA-SIRGAS / Origen-Nacional`. La capa original de drenajes no se reproyecta debido a que se encuentra en este sistema.
* Disolución espacial de SZH - subzonas hidrográficas para obtención de entidades multiparte.
* A partir de la capa de subzonas se generan las capas de orden superior ZH - Zona hidrográfica y AH - Área hidrográfica.
* Inclusión de campos y cálculo automático de propiedades geométricas de área, perímetro y longitud de cada drenaje en sistema internacional de unidades.
* Intersección espacial de SZH - subzonas hidrográficas con drenajes.
* Estadísticos de conteo y sumatoria de longitudes de drenaje para cada zonificación (AH, ZH, SZH).
* Unión de resultados estadísticos a capas geográficas.
* Análisis de distribución de áreas por rangos para niveles superiores de zonificación (AH, ZH).
* Análisis de forma y densidad para Kc - Coeficiente de compacidad, Dd - Densidad de drenajes y Dc - Densidad de corrientes.
* Etiqueta de marcado para Kc - Coeficiente de compacidad indicando la forma.
* Visualización detallada en pantalla de los resultados obtenidos.
* Exportación de resultados a formato de Microsoft Excel.

> La capa de drenajes utiliza el sistema de proyección `9377 MAGNA-SIRGAS / Origen-Nacional` que contiene sistema proyectado con unidades en metros y para el cálculo de las longitudes requeridas por este script, no es necesaria su reproyección. La capa de subzonas hidrográficas requiere ser proyectada al origen nacional debido a que se encuentra referenciada en `4686 MAGNA` solo en sistema geográfico.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\HydroGeoZone\`. 

Para la correcta ejecución de los scripts se recomienda utilizar la siguiente estructura de directorios.

| Directorio                                                                                 | Descripción                                                                                |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [/Datos](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Data)             | Directorio de datos de entrada.                                                            |
| [/Graph](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Graph)            | Directorio con gráficas e ilustraciones.                                                   |
| [/Map](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Map)                | Directorio con mapas para visualización de resultados en ArcGIS for Desktop y ArcGIS Pro.  |
| [/Output](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Output)          | Directorio de salida de capas generadas y archivos de resultados estadísticos.             |
| [/Reference](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Reference)    | Referencias bibliográficas.                                                                |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone/Screenshot)  | Capturas de pantalla con resultados de ejecución.                                          |


### Capas requeridas


#### Subzonas hidrográficas de Colombia - Escala 1:500k

Este mapa representa las unidades de análisis para el ordenamiento ambiental de territorio definidas por el Ideam en convenio con el Instituto Geográfico Agustín Codazzi (IGAC), a escala 1:500.000 llamadas zonificación hidrográfica de Colombia. [^3]

Procedimiento:

1. Ingrese al portal http://www.ideam.gov.co/en/capas-geo y en el cuadro de búsqueda escriba _Zonificación Hidrográfica_, observará que a 2021.12.23 existen dos versiones de la capa de zonificación correspondientes al año 2010 y 2013.

2. Para las dos capas, realice la descarga del archivo de formas Shapefile y consulte sus metadatos y el catálogo de objetos disponible.

3. Descomprima solo los datos contenidos en las carpetas `/shape` en la carpeta `/Data` dentro de D:\R.GISPython\HydroGeoZone.

Catálogo de objetos en Subzonas [^4]
| Nombre       | Alias          | Definición                                                                   | Tipo de dato |
|--------------|----------------|------------------------------------------------------------------------------|--------------|
| OBJECTID     | OBJECTID       | Identificador de objeto geográfico.                                          | Texto        |
| Shape        | Shape          | Tipo de geometría.                                                           | Geometría    |
| COD_AH       | Código Area    | Código del Area hidrográfica a la que corresponde.                           | Entero       |
| COD_ZH       | Código Zona    | Código de la Zona hidrográfica a la que corresponde.                         | Entero       |
| COD_SZH      | Código Subzona | Código de Subzona hidrográfica a la que corresponde.                         | Entero       |
| NOM_AH       | Nombre Área    | Nombre del área hidrográfica a la que corresponde. Dominio Área Hidográfica. | Texto        |
| NOM_ZH       | Nombre Zona    | Nombre de la zona hidrográfica a la que corresponde.                         | Texto        |
| NOM_SZH      | Nombre Subzona | Nombre de la Subzona hidrográfica a la que corresponde.                      | Texto        |
| Shape_Length | Shape_Length   | Perímetro en las unidades del sistema de referencia espacial.                | Entero       |
| Shape_Area   | Shape_Area     | Área en las unidades del sistema de referencia espacial.                     | Entero       |
| RULEID       | RULEID         | Id único asignado por el sistema a la representación gráfica.                | Entero       |
| Override     | Override       | Representación gráfica.                                                      | Blob         |

![IDEAMZonificacionHidrograficaDescarga.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/IDEAMZonificacionHidrograficaDescarga.png)


#### Drenajes de Colombia: tomados de datos abiertos IGAC - Escala 1:100k

Flujo de agua superficial que depende de la precipitación pluvial y/o afloramiento de aguas subterráneas y va a desembocar en otra corriente, en una laguna o en el mar. Los drenajes dispersos son aquellos que no desembocan en otro cuerpo de agua, o desaparecen al ser no fotointerpretables, por ejemplo en corrientes subterráneas.[^5]

Procedimiento:

1. Ingrese al portal https://www.colombiaenmapas.gov.co/, en temática seleccione _Cartografía Básica_ y busque `Base de datos vectorial básica. Colombia. Escala 1:100.000. Año 2019`. En la parte inferior del _Detalle del Servicio_ seleccione en _Formato de descarga_ `Geodatabase` y de clic en _Descargar_, automáticamente iniciará la descarga a través de una orden de servicio. La GDB comprimida tiene un tamaño apoximado de 661 MB.

![IGACGDB100k.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/IGACGDB100k.png)

2. Descomprima la base de datos geográfica en la carpeta de descargas, cree un mapa nuevo en blanco en ArcGIS for Desktop o en ArcGIS Pro, agregue el mapa base _World Light Gray Canvas Base_ y desde el dataset `Superficies_Agua`, agregue la capa `Drenaje_Sencillo`.

![IGACDrenajeSencillo100k.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/IGACDrenajeSencillo100k.png)

3. Exporte la clase de entidad _Drenaje_Sencillo_ a un archivo de formas en formato Shapefile dentro de la carpeta `/Data` en D:\R.GISPython\HydroGeoZone. La versión descargada contiene 426719 entidades.

![IGACDrenajeSencillo100kExport.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/IGACDrenajeSencillo100kExport.png)

> Para el desarrollo del análisis no se ha utilizado la digitalización de la Base de datos vectorial básica - Colombia a Escala 1:25.000 del Año 2018 debido a que aún no se encuentran todas las planchas del país digitalizadas y almacenadas en la GDB disponible para descarga como se muestra en la siguiente imagen.

Información disponible a escala 1:25k
![IGACGDB25k.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/IGACGDB25k.png)

Catálogo de objetos en Drenaje_Sencillo para capa en formato Shapefile

| Nombre     | Alias      | Definición                                                                                         | Tipo de dato          |
|------------|------------|----------------------------------------------------------------------------------------------------|-----------------------|
| OBJECTID   | OBJECTID   | Identificador único de objeto.                                                                     | Numérico              |
| Shape      | Shape      | Tipo de geometría.                                                                                 | Geometría             |
| ESTADO_DRE | TEDD       | Indica si el drenaje es permanente o intermitente. Subtipo.                                        | Texto                 |
| SYMBOL     | Symbol     | En este campo se especifica la geometría como se representará el objeto (punto, línea o polígono). | Numérico y texto, 255 |
| PROYECTO   | PROYECTO   | Proyecto en el cual se desarrollaron los datos.                                                    | Numérico y texto, 255 |
| FECHA      | FECHA      | Fecha de realización de los datos.                                                                 | Dato                  |
| DISPERSION | Dispersión | Indica si el drenaje es disperso no no.                                                            | Dato                  |
| NOMBRE_GEO | NMG        | Nombre de la entidad geográfica.                                                                   | Numérico y texto, 255 |
| PK_CUE     | PK_CUE     | Identificador único global de cada elemento.                                                       | Numérico              |
| RULEID     | RuleID     | Identificador único de la representación.                                                          | Texto                 |
| GLOBALID   | GLOBALID   | Identificador global en la base de datos espacial.                                                 | Texto                 |
| SHAPE_Leng | SHAPE_Leng | Longitud del elemento.                                                                             | Numérico              |

Estado de drenajes - Subtipos

| Code               | Description  |
|--------------------|--------------|
| 5101               | Permanente   | 
| 5102               | Intermitente |


### Ejecución y resultados del análisis

#### Consideraciones generales

* Para la ejecución completa del análisis para drenajes permanentes, intermitentes y no clasificados, establecer las variables `intersectActive = True` para volver a realizar la intersección espacial y calcular las longitudes de los drenajes intersecados y `statisticActive = True` para volver a generar estadísticos en DBF y convertirlos a Excel.
* Para analizar solo a partir de drenajes permanentes, establecer en `True` las variables anteriores y establecer adicionalmente la variable `onlyPermanentDrainActive = True`.
* Para realizar modificaciones en el Script e incluir nuevas funcionalidades y ejecutar pruebas de funcionamiento, se recomienda ejecutar todos los procesos incluyendo todos los drenajes (permanentes e intermitentes) y luego de obtener las capas principales del análisis espacial `DrenajeSencilloFiltro.shp` y `DrenajeSencilloIntersect.shp`. Luego desactivar la ejecución de drenajes intersecados y recálculo de estadísticos detallados, de esta forma no tendrá que esperar (aproximadamente 10 minutos para 500k drenajes) a la creación completa de las capas principales resultantes del análisis.

#### Reportes detallados de resultados

El detalle de los resultados obtenidos del análisis, ha sido generado automáticamente por el script en Python y puede ser consultado o descargado en formato Markdown a través de los enlaces presentados en la siguiente tabla. 

| Reporte                                                                                                                            | Descripción                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [HydroGeoZoneDrainAll20211229.md](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/HydroGeoZoneDrainAll20211229.md) | Análisis para SZH - Subzonas hidrográficas IDEAM 2013 y Drenajes Sencillos IGAC 2019 - Drenajes de todos los subtipos. |
| [HydroGeoZoneDrainPerm20211229.md]()                                                                                               | Análisis para SZH - Subzonas hidrográficas IDEAM 2013 y Drenajes Sencillos IGAC 2019 - Drenajes solo permanentes.      |

A continuación se observan los resultados obtenidos a partir de la intersección espacial entre las SZH - Subzonas hidrográficas IDEAM del año 2013 con los drenajes permanentes e intermitentes IGAC a 2019.  

#### Total nacional de SZH - subzonas hidrográficas por rango de área

> Debido a que existen algunas subzonas hidrográficas con el mismo código y como polígonos independientes, y debido a que el script principal realiza el proceso de unificación en entidades multiparte para garantizar que el conteo y estadísticos de análisis a partir de drenajes sea consistente en el proceso de intersección espacial, el número de polígonos de la capa original (316) corresponde a un total de 314 subzonas únicas como se muestra en los siguientes resultados. 

![SZHSubzonaHidrograficaRangoArea2013.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaRangoArea2013.png)


#### SZH - subzonas hidrográficas por rango de área para cada AH - Área hidrográfica

Los resultados detallados de las sub-clasificaciones de área espacial para cada AH - Área hidrográfica se encuentran en los reportes detallados. 


#### Forma y densidad por zonificación hidrográfica 

AH - Áreas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.zip](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/AreaHidrograficaEstadistica.zip).

![AHAreaHidrograficaFormaDensidad2013All.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/AHAreaHidrograficaFormaDensidad2013All.png)

AH - Áreas hidrográficas año 2013 solo drenajes permanentes a 2019. [.zip](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/AreaHidrograficaEstadisticaSoloPermanente.zip)

ZH - Zonas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.zip](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/ZonaHidrograficaEstadistica.zip).

Mapa de áreas por ZH - Zona hidrográfica
![ZHZonaHidrograficaArea.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaArea.png)

Mapa de número de drenajes por ZH - Zona hidrográfica
![ZHZonaHidrograficaNumDrenajesAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaNumDrenajesAll.png)

Mapa de sumatoria de longitud de drenajes por ZH - Zona hidrográfica
![ZHZonaHidrograficaSumLDrenajesAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaSumLDrenajesAll.png)

Mapa de Kc - Coeficiente de Compacidad por ZH - Zona hidrográfica

> Debido a que algunas ZH - Zonas Hidrográficas están compuestas por entidades multiparte, se pueden presentar valores altos en el cálculo del índice de compacidad, p.ej, la zona `38 - Orinoco Directos` se compone de 5 entidades polígonos.   

![ZHZonaHidrograficaKcAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaKcAll.png)

Mapa de Dd - Densidad de Drenajes por ZH - Zona hidrográfica
![ZHZonaHidrograficaDdAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaDdAll.png)

Mapa de Dc - Densidad de Corrientes por ZH - Zona hidrográfica
![ZHZonaHidrograficaDcAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/ZHZonaHidrograficaDcAll.png)

ZH - Zonas hidrográficas año 2013 con solo drenajes permanentes 2019. [.zip](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/ZonaHidrograficaEstadisticaSoloPermanente.zip)

SZH - Subzonas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.zip](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.zip).

Mapa de áreas por SZH - Zona hidrográfica
![SZHSubzonaHidrograficaArea.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaArea.png)

Mapa de número de drenajes por SZH - Subzona hidrográfica
![SZHSubzonaHidrograficaNumDrenajesAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaNumDrenajesAll.png)

Mapa de sumatoria de longitud de drenajes por SZH - Subzona hidrográfica
![SZHSubzonaHidrograficaSumLDrenajesAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaSumLDrenajesAll.png)

Mapa de Kc - Coeficiente de Compacidad por SZH - Subzona hidrográfica

![SZHSubzonaHidrograficaKcAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaKcAll.png)

Mapa de Dd - Densidad de Drenajes por SZH - Subzona hidrográfica
![SZHSubzonaHidrograficaDdAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaDdAll.png)

Mapa de Dc - Densidad de Corrientes por SZH - Subzona hidrográfica
![SZHSubzonaHidrograficaDcAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/SZHSubzonaHidrograficaDcAll.png)


### Matrices de dispersión en SZH - Subzonas hidrográficas

![PlotAreaVsFREQUENCYDrainAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/PlotAreaVsFREQUENCYDrainAll.png)
![PlotAreaVsSUM_LDreDrainAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/PlotAreaVsSUM_LDreDrainAll.png)
![PlotAreaVsKcDrainAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/PlotAreaVsKcDrainAll.png)
![PlotAreaVsDdDrainAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/PlotAreaVsDdDrainAll.png)
![PlotAreaVsDcDrainAll.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Graph/PlotAreaVsDcDrainAll.png)


### Ejecución en ArcGIS Pro

![Python3.7.11ArcGISPro2.9.0.png](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Screenshot/Python3.7.11ArcGISPro2.9.0.png)


### Referencias

* http://www.ideam.gov.co/capas-geo
* http://www.siac.gov.co/catalogo-de-mapas
* http://visor.ideam.gov.co/geovisor/#!/profiles/3
* https://desktop.arcgis.com/en/arcmap/10.6/tools/data-management-toolbox/calculate-geometry-attributes.htm
* [Hidrografía Colombiana - IDEAM y SiGaia (versión no oficial de zonificación a 2018)](https://www.arcgis.com/home/item.html?id=89f6818e093f4b0faa99b456ad98018d)
* [ESRI - Versiones de Python según la versión de ArcGIS](https://support.esri.com/en/technical-article/000013224)
* [ESRI - Python, NumPy, and MatPlotlib en ArcGIS 10.6](https://desktop.arcgis.com/en/arcmap/10.6/get-started/installation-guide/python-requirement.htm)

### Autores

* Creado por [r.cfdtools](r.cfdtools@gmail.com) (40h).


### Compatibilidad

* Compatible con ArcGIS for Desktop 10.6 o superior.
* Compatible con ArcGIS Pro.


### Control de versiones

| Versión     | Descripción      |
|-------------|------------------|
| v.20211228  | Versión inicial. |


### Licencia, cláusulas y condiciones de uso

R.GISPython es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.GISPython/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.GISPython/wiki) | [Actividad siguiente]()     |
|------------------------|---------------------------------------------------------|-----------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

Notas a pie
[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6
[^5]: https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf
[^6]: http://portal.anla.gov.co/sistema-informacion-geografica
[^7]: https://www.cvc.gov.co/sites/default/files/Planes_y_Programas/Planes_de_Ordenacion_y_Manejo_de_Cuencas_Hidrografica/La%20Vieja%20-%20POMCA%20en%20Ajuste/Fase%20Diagnostico/7_CapituloI_Diagnostico_Morfometria.pdf
