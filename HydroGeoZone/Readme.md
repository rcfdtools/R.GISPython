## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python

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


### Caso de estudio

Estudiar la forma y densidad de las áreas, zonas y subzonas hidrográficas de Colombia a partir de la delimitación geográfica realizada por el [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/) y la red de drenajes sencillos digitalizada a escala 1:25k por el [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/).

Análisis de forma y densidad

| Parámetro | Descripción                   | Fórmula                 | 
|-----------|-------------------------------|-------------------------|
| Kc        | Coeficiente de compacidad     | Kc = 0.25 * P / A ^ 0.5 |
| Dd        | Densidad de drenajes, km/km²  | Dd = Σ LCi / A          |
| Dc        | Densidad de corrientes, 1/km² | Dd = n / A              |

Donde,
* P, perímetro de la zona hidrográfica en kilómetros.
* A, área de la zona hidrográfica hen km².
* LCi, longitud de cada cauce o corriente de agua.
* n, número de cauces o corrientes de agua.


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




### Resultados del análisis

#### AH - Áreas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.dbf](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/AreaHidrograficaEstadistica.dbf), [.xls](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/AreaHidrograficaEstadistica.xls).

| AH | Nombre AH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 102803.08 | 4814.69 | 39119 | 108190.65 | 3.75 | 1.05 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 270888.94 | 3763.38 | 134281 | 314458.56 | 1.81 | 1.16 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 346081.36 | 3736.08 | 122458 | 301766.4 | 1.59 | 0.87 | 0.35 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 341164.55 | 6122.88 | 101572 | 298438.97 | 2.62 | 0.87 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 77372.03 | 3360.07 | 35124 | 81609.93 | 3.02 | 1.05 | 0.45 | Oval-oblonga a rectangular-oblonga |

#### ZH - Zonas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.dbf](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/ZonaHidrograficaEstadistica.dbf), [.xls](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/ZonaHidrograficaEstadistica.xls).

| AH | Nombre AH | ZH | Nombre ZH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 11 | Atrato - Darién | 37837.02 | 1568.38 | 13615 | 39050.93 | 2.02 | 1.03 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 12975.9 | 1336.35 | 4344 | 13865.35 | 2.93 | 1.07 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 14101.53 | 890.79 | 3166 | 10845.28 | 1.88 | 0.77 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 21371.89 | 1252.31 | 8310 | 23469.98 | 2.14 | 1.1 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 16439.46 | 789.96 | 9679 | 20948.14 | 1.54 | 1.27 | 0.59 | Oval-redonda a oval oblonga |
| 1 | Caribe | 17 | Islas Caribe | 77.29 | 109.87 | 5 | 10.96 | 3.12 | 0.14 | 0.06 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 44503.94 | 1891.31 | 23992 | 55857.48 | 2.24 | 1.26 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 9961.0 | 603.0 | 7774 | 14866.61 | 1.51 | 1.49 | 0.78 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 59628.27 | 2005.81 | 32194 | 71567.76 | 2.05 | 1.2 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 23206.44 | 1046.29 | 12392 | 28066.87 | 1.72 | 1.21 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 21142.21 | 1045.18 | 5496 | 17827.1 | 1.8 | 0.84 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 45739.61 | 2627.71 | 25193 | 57307.42 | 3.07 | 1.25 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 14603.72 | 872.53 | 9015 | 17024.62 | 1.81 | 1.17 | 0.62 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 22892.03 | 849.58 | 9155 | 25441.49 | 1.4 | 1.11 | 0.4 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 29211.73 | 1309.22 | 9070 | 26499.23 | 1.92 | 0.91 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 53591.77 | 1926.75 | 20940 | 50386.44 | 2.08 | 0.94 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 84348.26 | 2733.95 | 29348 | 75165.5 | 2.35 | 0.89 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 26118.92 | 1469.25 | 15943 | 28040.12 | 2.27 | 1.07 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 20213.3 | 1189.87 | 7857 | 15978.9 | 2.09 | 0.79 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 82506.03 | 2504.65 | 26097 | 73274.44 | 2.18 | 0.89 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 24176.66 | 791.28 | 2903 | 14808.37 | 1.27 | 0.61 | 0.12 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 11348.72 | 999.15 | 2944 | 9176.94 | 2.34 | 0.81 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 43514.08 | 3424.61 | 16336 | 34695.0 | 4.1 | 0.8 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 39 | Apure | 263.63 | 106.78 | 90 | 240.7 | 1.64 | 0.91 | 0.34 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 41 | Guanía | 31130.32 | 1561.0 | 12852 | 29879.38 | 2.21 | 0.96 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 37570.93 | 1820.01 | 7763 | 25828.86 | 2.35 | 0.69 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 53359.39 | 2615.79 | 12581 | 42687.56 | 2.83 | 0.8 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 99768.59 | 3755.68 | 32157 | 93819.82 | 2.97 | 0.94 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 36591.94 | 1621.95 | 10793 | 33205.62 | 2.12 | 0.91 | 0.29 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 21207.97 | 1279.19 | 8737 | 21303.05 | 2.2 | 1.0 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 57822.73 | 3855.06 | 15800 | 48839.68 | 4.01 | 0.84 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 48 | Amazonas - Directos | 3256.52 | 375.27 | 698 | 2444.36 | 1.64 | 0.75 | 0.21 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 49 | Napo | 456.15 | 159.57 | 191 | 430.64 | 1.87 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5874.67 | 679.52 | 2357 | 4443.78 | 2.22 | 0.76 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 24029.6 | 1236.12 | 10183 | 23227.29 | 1.99 | 0.97 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 20848.95 | 1088.56 | 8732 | 20179.07 | 1.88 | 0.97 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 16393.56 | 946.72 | 8156 | 20697.74 | 1.85 | 1.26 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5968.79 | 719.69 | 3277 | 7614.21 | 2.33 | 1.28 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 56 | Pacífico - Directos | 4256.46 | 1031.69 | 2419 | 5447.84 | 3.95 | 1.28 | 0.57 | Oval-oblonga a rectangular-oblonga |

#### SZH - Subzonas hidrográficas año 2013 con drenajes permanentes e intermitentes a 2019. [.dbf](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.dbf), [.xls](https://github.com/rcfdtools/R.GISPython/blob/main/HydroGeoZone/Output/SubZonaHidrograficaEstadistica.xls).

| AH | Nombre AH | ZH | Nombre ZH | SZH | Nombre SZH | Área, km² | Perm, km | n Drenajes | Σ LCi, km | Kc | Dd | Dc | Kc Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 11 | Atrato - Darién | 1101 | Río Andágueda | 901.97 | 214.5 | 410 | 1020.98 | 1.79 | 1.13 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1102 | Alto Atrato | 1668.11 | 242.54 | 583 | 1732.97 | 1.48 | 1.04 | 0.35 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1103 | Río Quito | 1817.46 | 310.67 | 862 | 2161.13 | 1.82 | 1.19 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1104 | Río Bebaramá y otros Directos Atrato (md) | 2599.28 | 259.65 | 830 | 2715.14 | 1.27 | 1.04 | 0.32 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1105 | Directos Atrato entre ríos Quito y Bojayá (mi) | 3095.85 | 376.54 | 1633 | 4031.18 | 1.69 | 1.3 | 0.53 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1106 | Directos Atrato entre ríos Bebaramá y Murrí (md) | 1605.86 | 277.03 | 549 | 1820.55 | 1.73 | 1.13 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1107 | Río Murrí | 3472.61 | 401.88 | 1327 | 3741.37 | 1.7 | 1.08 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1108 | Río Bojayá | 1821.28 | 280.75 | 982 | 2375.23 | 1.64 | 1.3 | 0.54 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1109 | Río Napipí - Río Opogadó | 1120.47 | 205.04 | 485 | 1361.28 | 1.53 | 1.21 | 0.43 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1110 | Río Murindó - Directos al Atrato | 2656.99 | 292.61 | 569 | 2038.36 | 1.42 | 0.77 | 0.21 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1111 | Río Sucio | 5377.12 | 577.2 | 1705 | 5185.55 | 1.97 | 0.96 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1112 | Río Salaquí  y otros directos Bajo Atrato | 5849.07 | 489.76 | 1970 | 5921.61 | 1.6 | 1.01 | 0.34 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1113 | Río Cacarica | 1158.56 | 164.07 | 254 | 960.9 | 1.21 | 0.83 | 0.22 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1114 | Directos Bajo Atrato entre río Sucio y desembocadura | 2057.02 | 392.81 | 283 | 972.1 | 2.17 | 0.47 | 0.14 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1115 | Río Tanela y otros Directos al Caribe | 1452.44 | 247.87 | 528 | 1541.37 | 1.63 | 1.06 | 0.36 | Oval-redonda a oval oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1116 | Río Tolo y otros Directos al Caribe | 714.92 | 194.43 | 378 | 868.47 | 1.82 | 1.21 | 0.53 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 11 | Atrato - Darién | 1117 | Río Cabi y otros Directos Atrato (md) | 467.99 | 122.05 | 267 | 602.73 | 1.41 | 1.29 | 0.57 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1201 | Río León | 2279.19 | 252.78 | 735 | 2475.74 | 1.32 | 1.09 | 0.32 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1202 | Río Mulatos y otros directos al Caribe | 2981.99 | 341.32 | 1001 | 3450.35 | 1.56 | 1.16 | 0.34 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1203 | Río San Juan | 1444.54 | 258.03 | 305 | 1172.48 | 1.7 | 0.81 | 0.21 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1204 | Rio Canalete y otros Arroyos Directos al Caribe | 1898.25 | 285.98 | 578 | 1797.0 | 1.64 | 0.95 | 0.3 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1205 | Directos Caribe Golfo de Morrosquillo | 2504.61 | 316.25 | 821 | 2614.71 | 1.58 | 1.04 | 0.33 | Oval-redonda a oval oblonga |
| 1 | Caribe | 12 | Caribe - Litoral | 1206 | Arroyos Directos al Caribe | 1867.32 | 326.99 | 904 | 2355.08 | 1.89 | 1.26 | 0.48 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 13 | Sinú | 1301 | Alto Sinú - Urrá | 4596.16 | 382.36 | 1260 | 3849.95 | 1.41 | 0.84 | 0.27 | Oval-redonda a oval oblonga |
| 1 | Caribe | 13 | Sinú | 1302 | Medio Sinú | 3926.58 | 365.31 | 705 | 2850.67 | 1.46 | 0.73 | 0.18 | Oval-redonda a oval oblonga |
| 1 | Caribe | 13 | Sinú | 1303 | Bajo Sinú | 5578.79 | 507.07 | 1201 | 4144.65 | 1.7 | 0.74 | 0.22 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1501 | Río  Piedras - Río Manzanares | 928.48 | 187.87 | 588 | 1222.89 | 1.54 | 1.32 | 0.63 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1502 | Río Don Diego | 541.15 | 135.0 | 356 | 785.61 | 1.45 | 1.45 | 0.66 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1503 | Río Ancho y Otros Directos al caribe | 1952.39 | 206.67 | 1208 | 2614.82 | 1.17 | 1.34 | 0.62 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1504 | Río Tapias | 1076.53 | 162.59 | 571 | 1377.39 | 1.24 | 1.28 | 0.53 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1505 | Río Camarones y otros directos Caribe | 892.74 | 183.4 | 275 | 871.43 | 1.53 | 0.98 | 0.31 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1506 | Río Ranchería | 4276.8 | 427.77 | 1558 | 4590.35 | 1.64 | 1.07 | 0.36 | Oval-redonda a oval oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1507 | Directos Caribe - Ay.Sharimahana Alta Guajira | 5374.02 | 634.64 | 1695 | 5514.55 | 2.16 | 1.03 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1508 | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | 5646.16 | 607.86 | 1577 | 5559.94 | 2.02 | 0.98 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 15 | Caribe - Guajira | 1509 | Rio Guachaca - Mendiguaca y Buritaca | 683.63 | 124.89 | 482 | 933.0 | 1.19 | 1.36 | 0.71 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1601 | Río Pamplonita | 1402.87 | 372.15 | 812 | 1781.65 | 2.48 | 1.27 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1602 | Río Zulia | 3420.53 | 421.91 | 2031 | 4487.43 | 1.8 | 1.31 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1603 | Río Nuevo Presidente - Tres Bocas (Sardinata, Tibu) | 3434.34 | 334.15 | 2506 | 4898.81 | 1.43 | 1.43 | 0.73 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1604 | Río Tarra | 1760.13 | 278.18 | 1373 | 2583.08 | 1.66 | 1.47 | 0.78 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1605 | Río Algodonal (Alto Catatumbo) | 2336.05 | 340.94 | 1647 | 3476.41 | 1.76 | 1.49 | 0.71 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1606 | Río Socuavo del Norte y Río Socuavo Sur | 964.18 | 159.61 | 119 | 603.65 | 1.29 | 0.63 | 0.12 | Oval-redonda a oval oblonga |
| 1 | Caribe | 16 | Catatumbo | 1607 | Bajo Catatumbo | 1247.6 | 252.46 | 401 | 1145.79 | 1.79 | 0.92 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 16 | Catatumbo | 1608 | Río del Suroeste y directos Río de Oro | 1873.75 | 312.68 | 790 | 1971.33 | 1.81 | 1.05 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1701 | San Andres | 27.4 | 39.75 | 1 | 0.78 | 1.9 | 0.03 | 0.04 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1702 | Providencia | 22.49 | 32.55 | 4 | 10.18 | 1.72 | 0.45 | 0.18 | Oval-oblonga a rectangular-oblonga |
| 1 | Caribe | 17 | Islas Caribe | 1703 | Roncador y Quitasueño | 27.41 | 37.57 | 0 | 0.0 | 1.79 | 0.0 | 0.0 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2101 | Alto Magdalena | 2507.03 | 319.8 | 1352 | 3429.09 | 1.6 | 1.37 | 0.54 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2102 | Río Timaná y otros directos al Magdalena | 382.26 | 146.1 | 144 | 385.24 | 1.87 | 1.01 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2103 | Río Suaza | 1422.26 | 238.82 | 728 | 1757.18 | 1.58 | 1.24 | 0.51 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2104 | Ríos Directos al Magdalena (mi) | 1543.87 | 320.1 | 497 | 1464.96 | 2.04 | 0.95 | 0.32 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2105 | Río Páez | 5203.62 | 434.89 | 2825 | 6288.3 | 1.51 | 1.21 | 0.54 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2106 | Ríos directos Magdalena (md) | 1149.7 | 246.05 | 872 | 1608.12 | 1.81 | 1.4 | 0.76 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2108 | Río Yaguará y Río Iquira | 937.19 | 160.0 | 503 | 1083.71 | 1.31 | 1.16 | 0.54 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2109 | Juncal y otros Rios directos al Magdalena | 451.67 | 150.62 | 387 | 650.45 | 1.77 | 1.44 | 0.86 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2110 | Rio Neiva | 1070.3 | 176.09 | 1064 | 1936.87 | 1.35 | 1.81 | 0.99 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2111 | Rio Fortalecillas y otros | 2158.1 | 268.06 | 1858 | 3276.7 | 1.44 | 1.52 | 0.86 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2112 | Río Baché | 1168.15 | 205.31 | 744 | 1496.39 | 1.5 | 1.28 | 0.64 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2113 | Río Aipe, Río Chenche y otros directos al Magdalena | 2605.73 | 399.1 | 1322 | 2923.0 | 1.95 | 1.12 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2114 | Río Cabrera | 2804.02 | 355.14 | 1788 | 3707.31 | 1.68 | 1.32 | 0.64 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2115 | Directos Magdalena entre ríos Cabrera y Sumapaz | 1035.29 | 294.4 | 593 | 1282.62 | 2.29 | 1.24 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2116 | Río Prado | 1674.75 | 207.0 | 862 | 2134.97 | 1.26 | 1.27 | 0.51 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2118 | Río Luisa y otros directos al Magdalena | 1075.5 | 227.81 | 509 | 1380.92 | 1.74 | 1.28 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2119 | Río Sumapaz | 3045.26 | 352.88 | 1206 | 3411.17 | 1.6 | 1.12 | 0.4 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2120 | Río Bogotá | 5925.89 | 581.65 | 2396 | 6362.44 | 1.89 | 1.07 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2121 | Río Coello | 1831.15 | 285.94 | 1390 | 2970.78 | 1.67 | 1.62 | 0.76 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2122 | Río Opía | 552.76 | 153.34 | 108 | 529.95 | 1.63 | 0.96 | 0.2 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2123 | Río Seco y otros Directos al Magdalena | 1771.39 | 346.21 | 829 | 2134.23 | 2.06 | 1.2 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2124 | Río Totare | 1436.31 | 203.79 | 633 | 1735.02 | 1.34 | 1.21 | 0.44 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 21 | Alto Magdalena | 2125 | Río Lagunilla y Otros Directos al Magdalena | 2751.75 | 272.46 | 1382 | 3908.06 | 1.3 | 1.42 | 0.5 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2201 | Alto Saldaña | 2583.74 | 267.84 | 1660 | 3503.69 | 1.32 | 1.36 | 0.64 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2202 | Río Atá | 1534.98 | 247.22 | 870 | 1954.49 | 1.58 | 1.27 | 0.57 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2203 | Medio Saldaña | 604.01 | 161.92 | 458 | 869.99 | 1.65 | 1.44 | 0.76 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2204 | Río Amoyá | 1462.36 | 233.18 | 1081 | 2148.82 | 1.52 | 1.47 | 0.74 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2206 | Río Tetuán, Río Ortega | 1204.44 | 183.87 | 1357 | 2182.59 | 1.32 | 1.81 | 1.13 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2207 | Rïo Cucuana | 1865.74 | 261.08 | 1901 | 3276.16 | 1.51 | 1.76 | 1.02 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 22 | Saldaña | 2208 | Bajo Saldaña | 705.73 | 232.02 | 447 | 930.87 | 2.18 | 1.32 | 0.63 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2301 | Río Gualí | 875.8 | 219.88 | 531 | 1302.38 | 1.86 | 1.49 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2302 | Río Guarinó | 843.39 | 234.13 | 545 | 1248.2 | 2.02 | 1.48 | 0.65 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2303 | Directos al Magdalena entre Ríos Seco y Negro (md) | 434.39 | 153.13 | 272 | 570.36 | 1.84 | 1.31 | 0.63 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2304 | Directos Magdalena entre Ríos Guarinó y La Miel | 965.1 | 169.23 | 767 | 1771.98 | 1.36 | 1.84 | 0.79 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2305 | Río La Miel (Samaná) | 2398.89 | 264.82 | 1842 | 3829.8 | 1.35 | 1.6 | 0.77 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2306 | Río Negro | 4567.37 | 438.65 | 3027 | 5631.62 | 1.62 | 1.23 | 0.66 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2307 | Directos Magdalena Medio entre ríos La Miel y Nare | 1483.27 | 244.57 | 415 | 1446.11 | 1.59 | 0.97 | 0.28 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2308 | Río Nare | 5596.74 | 458.68 | 4432 | 7589.83 | 1.53 | 1.36 | 0.79 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2310 | Rió San Bartolo y otros directos al Magdalena Medio | 3592.46 | 350.67 | 1912 | 4083.5 | 1.46 | 1.14 | 0.53 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2311 | Directos al Magdalena Medio entre ríos Negro | 2681.99 | 359.54 | 1162 | 3070.69 | 1.74 | 1.14 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2312 | Río Carare (Minero) | 7273.39 | 544.29 | 3474 | 8252.58 | 1.6 | 1.13 | 0.48 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2314 | Río Opón | 4312.06 | 424.24 | 1536 | 4101.77 | 1.62 | 0.95 | 0.36 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2317 | Río Cimitarra y otros directos al Magdalena | 4966.83 | 433.82 | 1220 | 3214.65 | 1.54 | 0.65 | 0.25 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2319 | Río Lebrija y otros directos al Magdalena | 9575.1 | 560.16 | 5088 | 12458.3 | 1.43 | 1.3 | 0.53 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2320 | Directos al Magdalena (Brazo Morales) | 7092.22 | 482.2 | 4106 | 8563.25 | 1.43 | 1.21 | 0.58 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 23 | Medio Magdalena | 2321 | Quebrada El Carmen y Otros Directos al Magdalena | 2969.27 | 282.24 | 1865 | 4432.76 | 1.29 | 1.49 | 0.63 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2401 | Río Suárez | 7843.08 | 599.68 | 4078 | 9802.22 | 1.69 | 1.25 | 0.52 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2402 | Río Fonce | 2406.2 | 273.42 | 1342 | 2953.96 | 1.39 | 1.23 | 0.56 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2403 | Río Chicamocha | 9554.3 | 719.31 | 5425 | 11654.85 | 1.84 | 1.22 | 0.57 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 24 | Sogamoso | 2405 | Río Sogamoso | 3402.85 | 367.12 | 1547 | 3655.83 | 1.57 | 1.07 | 0.45 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 2501 | Alto San Jorge | 3960.43 | 396.1 | 1218 | 3572.98 | 1.57 | 0.9 | 0.31 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 25 | Bajo Magdalena- Cauca -San Jorge | 2502 | Bajo San Jorge - La Mojana | 17181.78 | 779.56 | 4278 | 14254.12 | 1.49 | 0.83 | 0.25 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2601 | Alto Río Cauca | 854.62 | 187.35 | 261 | 839.96 | 1.6 | 0.98 | 0.31 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2602 | Río Palacé | 934.6 | 189.91 | 545 | 1292.61 | 1.55 | 1.38 | 0.58 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2603 | Rio Salado y otros directos Cauca | 1247.99 | 261.83 | 883 | 1562.85 | 1.85 | 1.25 | 0.71 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2604 | Río Palo | 1651.31 | 234.67 | 1327 | 2425.1 | 1.44 | 1.47 | 0.8 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2605 | Río Timba | 485.14 | 125.66 | 323 | 681.04 | 1.43 | 1.4 | 0.67 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2606 | Río Ovejas | 924.28 | 155.18 | 637 | 1493.31 | 1.28 | 1.62 | 0.69 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2607 | Río Guachal (Bolo - Fraile y Párraga) | 1186.31 | 185.58 | 358 | 1094.17 | 1.35 | 0.92 | 0.3 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2608 | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | 1288.7 | 313.98 | 516 | 1375.36 | 2.19 | 1.07 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2609 | Ríos Amaime y Cerrito | 1124.62 | 189.54 | 432 | 1269.5 | 1.41 | 1.13 | 0.38 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2610 | Ríos Tulua y Morales | 1078.41 | 179.44 | 562 | 1377.42 | 1.37 | 1.28 | 0.52 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2611 | Río Frío | 476.3 | 124.47 | 162 | 491.39 | 1.43 | 1.03 | 0.34 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2612 | Río La Vieja | 2836.45 | 303.82 | 1672 | 4590.07 | 1.43 | 1.62 | 0.59 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2613 | Río Otún y otros directos al Cauca | 1220.72 | 226.26 | 585 | 1648.57 | 1.62 | 1.35 | 0.48 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2614 | Río Risaralda | 1259.39 | 231.16 | 697 | 1889.28 | 1.63 | 1.5 | 0.55 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2615 | Río Chinchiná | 1054.24 | 177.36 | 551 | 1466.09 | 1.37 | 1.39 | 0.52 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2616 | Rio Tapias y otros directos al Cauca | 1404.02 | 226.68 | 1417 | 2503.89 | 1.51 | 1.78 | 1.01 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2617 | Río Frío y Otros Directos al Cauca | 1638.21 | 338.8 | 799 | 2150.88 | 2.09 | 1.31 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2618 | Río Arma | 1860.27 | 261.43 | 1367 | 2797.17 | 1.52 | 1.5 | 0.73 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2619 | Río San Juan | 1416.12 | 217.9 | 724 | 1843.55 | 1.45 | 1.3 | 0.51 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2620 | Directos Río Cauca  entre Río San Juan y  Pto Valdivia | 3552.96 | 503.22 | 2404 | 4602.56 | 2.11 | 1.3 | 0.68 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2621 | Directos Río Cauca entre Río San Juan y Pto Valdia | 3413.51 | 524.35 | 2217 | 4404.63 | 2.24 | 1.29 | 0.65 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2622 | Río Desbaratado | 191.48 | 113.15 | 70 | 197.4 | 2.04 | 1.03 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2624 | Río Taraza - Río Man | 2578.59 | 346.4 | 885 | 2346.37 | 1.71 | 0.91 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2625 | Directos al Cauca entre Pto Valdivia y Río Nechí | 1436.42 | 405.47 | 846 | 1569.53 | 2.67 | 1.09 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2626 | Directos Bajo Cauca - Cga La Raya entre río Nechí | 4343.67 | 459.57 | 2163 | 4180.79 | 1.74 | 0.96 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2627 | Río Piendamo | 601.69 | 208.32 | 467 | 917.32 | 2.12 | 1.52 | 0.78 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2628 | Río Quinamayo y otros directos al Cauca | 810.98 | 174.12 | 472 | 1353.56 | 1.53 | 1.67 | 0.58 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2629 | Ríos Claro y Jamundí | 668.82 | 152.62 | 169 | 553.02 | 1.48 | 0.83 | 0.25 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2630 | Ríos Lilí, Melendez y Canaveralejo | 193.06 | 70.25 | 32 | 93.69 | 1.26 | 0.49 | 0.17 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2631 | Rios Arroyohondo - Yumbo - Mulalo - Vijes - Yotoco | 631.27 | 234.4 | 265 | 658.2 | 2.33 | 1.04 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2632 | Ríos Guabas,Sabaletas y Sonso | 556.67 | 114.0 | 179 | 604.49 | 1.21 | 1.09 | 0.32 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2633 | Ríos Guadalajara y San Pedro | 463.3 | 148.76 | 125 | 404.88 | 1.73 | 0.87 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2634 | Ríos Cali | 212.46 | 81.26 | 45 | 147.69 | 1.39 | 0.7 | 0.21 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2635 | Río Bugalagrande | 834.94 | 210.88 | 536 | 1135.96 | 1.82 | 1.36 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2636 | Río Paila | 525.76 | 109.02 | 239 | 645.88 | 1.19 | 1.23 | 0.45 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 26 | Cauca | 2637 | Rios Las Cañas - Los Micos y Obando | 782.38 | 187.43 | 261 | 699.22 | 1.68 | 0.89 | 0.33 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2701 | Río Porce | 5228.39 | 639.38 | 4206 | 7586.11 | 2.21 | 1.45 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2702 | Alto Nechí | 2936.92 | 340.29 | 2771 | 3997.73 | 1.57 | 1.36 | 0.94 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2703 | Bajo Nechí (md) | 4487.76 | 409.48 | 1432 | 3744.25 | 1.53 | 0.83 | 0.32 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 27 | Nechí | 2704 | Directos al Bajo Nechí (mi) | 1950.66 | 263.85 | 606 | 1696.53 | 1.49 | 0.87 | 0.31 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2801 | Alto Cesar | 3435.73 | 294.28 | 2625 | 5754.67 | 1.26 | 1.67 | 0.76 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2802 | Medio Cesar | 8260.98 | 459.97 | 2752 | 8256.57 | 1.27 | 1.0 | 0.33 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2804 | Río Ariguaní | 5325.51 | 428.45 | 1745 | 5650.34 | 1.47 | 1.06 | 0.33 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 28 | Cesar | 2805 | Bajo Cesar | 5869.81 | 391.02 | 2033 | 5779.91 | 1.28 | 0.98 | 0.35 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2901 | Directos al Bajo Magdalena entre El Plato y Calamar | 2010.94 | 231.53 | 850 | 2485.3 | 1.29 | 1.24 | 0.42 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2902 | Directos al Bajo Magdalena entre El Plato y Calamar | 2473.59 | 304.6 | 853 | 2596.2 | 1.53 | 1.05 | 0.34 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2903 | Canal del Dique margen derecho | 2103.34 | 312.05 | 656 | 2046.38 | 1.7 | 0.97 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2904 | Directos al Bajo Magdalena entre Calamar y desembocadura | 1151.53 | 215.04 | 278 | 914.23 | 1.58 | 0.79 | 0.24 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2905 | Canal del Dique margen izquierda | 2299.23 | 393.21 | 722 | 2008.96 | 2.05 | 0.87 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2906 | Cga Grande de Santa Marta | 8219.98 | 529.41 | 2713 | 7182.44 | 1.46 | 0.87 | 0.33 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2907 | Directos Bajo Magdalena entre El Banco y El Plato | 6998.88 | 568.62 | 1848 | 5324.61 | 1.7 | 0.76 | 0.26 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2908 | Ríos Chimicuica y Corozal | 3692.2 | 284.91 | 1070 | 3708.04 | 1.17 | 1.0 | 0.29 | Oval-redonda a oval oblonga |
| 2 | Magdalena Cauca | 29 | Bajo Magdalena | 2909 | Cienaga Mallorquin | 262.04 | 89.87 | 80 | 233.07 | 1.39 | 0.89 | 0.31 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 31 | Inírida | 3101 | Río Inírida Alto | 11752.53 | 654.03 | 2609 | 9654.83 | 1.51 | 0.82 | 0.22 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 31 | Inírida | 3104 | Río Inírida Medio | 18344.68 | 1250.21 | 7913 | 18306.77 | 2.31 | 1.0 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3105 | Río Papunaya | 6830.93 | 610.59 | 1459 | 5297.99 | 1.85 | 0.78 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3107 | Caño Nabuquén | 1728.93 | 288.14 | 1159 | 2276.91 | 1.73 | 1.32 | 0.67 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3108 | R._Inírida_(mi),_hasta_bocas_Caño_Bocón,_y_R._Las Viñas | 7983.66 | 902.09 | 4820 | 8811.12 | 2.52 | 1.1 | 0.6 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 31 | Inírida | 3110 | Caño Bocón | 6951.02 | 562.33 | 2980 | 6038.81 | 1.69 | 0.87 | 0.43 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3201 | Río Guayabero | 6264.86 | 555.18 | 3216 | 7015.84 | 1.75 | 1.12 | 0.51 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3202 | Río Guape | 3837.91 | 471.18 | 1553 | 3981.23 | 1.9 | 1.04 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3203 | Rio Losada | 3654.06 | 357.86 | 954 | 3175.2 | 1.48 | 0.87 | 0.26 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3204 | Alto Guaviare | 10351.53 | 599.86 | 2820 | 8668.36 | 1.47 | 0.84 | 0.27 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3206 | Río Ariari | 8069.11 | 673.73 | 3192 | 8212.24 | 1.88 | 1.02 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3207 | Río Guejar | 3291.47 | 386.5 | 693 | 2768.45 | 1.68 | 0.84 | 0.21 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3210 | Medio Guaviare | 13738.92 | 982.43 | 5038 | 11191.95 | 2.1 | 0.81 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3212 | Río Siare | 4433.73 | 581.29 | 2386 | 5426.39 | 2.18 | 1.22 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3213 | Río Iteviare | 4854.11 | 651.48 | 2363 | 5207.02 | 2.34 | 1.07 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3214 | Bajo Guaviare | 8872.89 | 1011.66 | 1296 | 4389.32 | 2.68 | 0.49 | 0.15 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3215 | Caño Minisiare | 2336.11 | 359.37 | 1808 | 3161.22 | 1.86 | 1.35 | 0.77 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 32 | Guaviare | 3216 | Alto Río Uvá | 4422.98 | 395.89 | 1833 | 4643.63 | 1.49 | 1.05 | 0.41 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3217 | Bajo Río Uvá | 5403.34 | 494.36 | 1429 | 4521.89 | 1.68 | 0.84 | 0.26 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 32 | Guaviare | 3218 | Caño Chupabe | 4817.24 | 625.02 | 767 | 2802.76 | 2.25 | 0.58 | 0.16 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3301 | Alto Vichada | 8049.09 | 524.47 | 6595 | 11362.17 | 1.46 | 1.41 | 0.82 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 33 | Vichada | 3302 | Río Guarrojo | 3646.74 | 484.86 | 2934 | 4458.82 | 2.01 | 1.22 | 0.8 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3303 | Río Muco | 4448.89 | 518.52 | 2643 | 4052.78 | 1.94 | 0.91 | 0.59 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 33 | Vichada | 3305 | Directos Vichada Medio | 4985.17 | 461.11 | 1846 | 3858.92 | 1.63 | 0.77 | 0.37 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 33 | Vichada | 3306 | Bajo Vichada | 4989.02 | 502.98 | 1925 | 4307.42 | 1.78 | 0.86 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3401 | Alto Río Tomo | 8023.92 | 642.65 | 3283 | 6620.73 | 1.79 | 0.83 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3402 | Río Elvita | 5554.77 | 507.91 | 1990 | 4069.19 | 1.7 | 0.73 | 0.36 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3403 | Bajo Río Tomo | 4080.21 | 635.41 | 1436 | 2995.64 | 2.49 | 0.73 | 0.35 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 34 | Tomo | 3405 | Caño Lioni o Terecay | 2554.4 | 447.49 | 1148 | 2293.34 | 2.21 | 0.9 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3501 | Rio Metica (Guamal - Humadea) | 3838.4 | 333.4 | 1404 | 4401.4 | 1.35 | 1.15 | 0.37 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3502 | Río Guayuriba | 3194.71 | 470.05 | 1413 | 3402.91 | 2.08 | 1.07 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3503 | Río Guatiquía | 1777.88 | 320.92 | 584 | 1881.12 | 1.9 | 1.06 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3504 | Río Guacavía | 848.92 | 158.1 | 183 | 716.79 | 1.36 | 0.84 | 0.22 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3505 | Río Humea | 1438.04 | 285.2 | 384 | 1090.0 | 1.88 | 0.76 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3506 | Río Guavio | 2285.13 | 307.65 | 1890 | 3354.73 | 1.61 | 1.47 | 0.83 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3507 | Río Garagoa | 2483.0 | 312.64 | 1226 | 2845.02 | 1.57 | 1.15 | 0.49 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3508 | Río Lengupá | 1875.21 | 245.24 | 1040 | 2186.42 | 1.42 | 1.17 | 0.55 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3509 | Río Upía | 1821.86 | 373.47 | 756 | 1794.95 | 2.19 | 0.99 | 0.41 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3510 | Río Negro | 925.75 | 203.36 | 157 | 1019.43 | 1.67 | 1.1 | 0.17 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3511 | Directos Rio Metica entre ríos Guayuriba y Yucao | 1964.36 | 456.75 | 766 | 1769.64 | 2.58 | 0.9 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3512 | Río Yucao | 2435.19 | 288.91 | 1395 | 2595.86 | 1.46 | 1.07 | 0.57 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3513 | Río Melúa | 1880.31 | 266.96 | 1047 | 2344.51 | 1.54 | 1.25 | 0.56 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3514 | Caño Cumaral | 1110.74 | 228.96 | 600 | 1417.38 | 1.72 | 1.28 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3515 | Río Manacacias | 6969.94 | 831.28 | 4478 | 9099.4 | 2.49 | 1.31 | 0.64 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3516 | Lago de Tota | 225.16 | 86.7 | 120 | 229.76 | 1.44 | 1.02 | 0.53 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3518 | Río Túa y otros directos al Meta | 4963.06 | 402.82 | 1086 | 3676.99 | 1.43 | 0.74 | 0.22 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3519 | Río Cusiana | 5089.28 | 456.32 | 1580 | 4519.56 | 1.6 | 0.89 | 0.31 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3520 | Directos al Meta entre ríos Cusiana y Cravo Sur | 1660.34 | 239.73 | 153 | 908.44 | 1.47 | 0.55 | 0.09 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3521 | Río Cravo Sur | 5148.16 | 502.04 | 1532 | 4470.54 | 1.75 | 0.87 | 0.3 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3522 | Caño Guanápalo y otros directos al Meta | 6225.95 | 411.43 | 539 | 3922.83 | 1.3 | 0.63 | 0.09 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3523 | Río Pauto | 7998.7 | 610.07 | 1030 | 6117.96 | 1.71 | 0.76 | 0.13 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3524 | Directos al Río Meta entre ríos Pauto y Carare | 5347.05 | 489.78 | 419 | 3209.2 | 1.67 | 0.6 | 0.08 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 35 | Meta | 3525 | Directos Bajo Meta entre ríos Casanare y Orinoco | 6323.0 | 777.79 | 1618 | 3634.07 | 2.45 | 0.57 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3526 | Directos al Río Meta entre ríos Cusiana y Carare | 3434.83 | 680.38 | 383 | 1607.95 | 2.9 | 0.47 | 0.11 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 35 | Meta | 3527 | Directos al Río Meta entre ríos Humea y Upia (mi) | 1241.07 | 188.44 | 314 | 1057.58 | 1.34 | 0.85 | 0.25 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 36 | Casanare | 3601 | Río Ariporo | 5268.11 | 619.92 | 631 | 3307.62 | 2.14 | 0.63 | 0.12 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3602 | Río Casanare | 6645.61 | 754.81 | 1195 | 4329.99 | 2.31 | 0.65 | 0.18 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 36 | Casanare | 3603 | Río Cravo Norte | 8876.2 | 522.09 | 879 | 5621.19 | 1.39 | 0.63 | 0.1 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 36 | Casanare | 3604 | Caño Samuco | 915.68 | 188.82 | 58 | 478.5 | 1.56 | 0.52 | 0.06 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 36 | Casanare | 3605 | Caño Aguaclarita | 2471.05 | 249.25 | 140 | 1071.07 | 1.25 | 0.43 | 0.06 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3701 | Río Chítaga | 2483.57 | 334.98 | 1099 | 2572.93 | 1.68 | 1.04 | 0.44 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3702 | Río Margua | 744.48 | 146.11 | 267 | 685.23 | 1.34 | 0.92 | 0.36 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3703 | Río Cobugón - Río Cobaría | 1974.35 | 203.74 | 683 | 1775.78 | 1.15 | 0.9 | 0.35 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3704 | Río Bojabá | 1130.39 | 215.18 | 402 | 979.61 | 1.6 | 0.87 | 0.36 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3705 | Rio Banadia y otros Directos al Río Arauca | 2097.01 | 294.04 | 287 | 1272.45 | 1.61 | 0.61 | 0.14 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 37 | Arauca | 3706 | Directos Río Arauca (md) | 2918.92 | 352.38 | 206 | 1890.95 | 1.63 | 0.65 | 0.07 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3801 | Río Vita | 8207.17 | 962.81 | 3982 | 6390.91 | 2.66 | 0.78 | 0.49 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3802 | Río Tuparro | 11505.4 | 813.17 | 6368 | 11782.29 | 1.9 | 1.02 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3803 | Caño Matavén | 10461.36 | 684.71 | 2225 | 7135.35 | 1.67 | 0.68 | 0.21 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3804 | Directos Río Atabapo (mi) | 4617.54 | 447.6 | 2272 | 4853.28 | 1.65 | 1.05 | 0.49 | Oval-redonda a oval oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3805 | Directos Orinoco entre ríos Tomo y Meta (mi) | 4171.25 | 439.65 | 1164 | 2454.53 | 1.7 | 0.59 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 38 | Orinoco Directos | 3809 | Río Cinaruco y Directos Río Orinoco | 4551.36 | 466.37 | 325 | 2078.64 | 1.73 | 0.46 | 0.07 | Oval-oblonga a rectangular-oblonga |
| 3 | Orinoco | 39 | Apure | 3901 | Alto Río Apure | 263.63 | 106.78 | 90 | 240.7 | 1.64 | 0.91 | 0.34 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 41 | Guanía | 4101 | Alto Rio Guanía | 3692.65 | 422.29 | 1617 | 3876.29 | 1.74 | 1.05 | 0.44 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4102 | Medio Rio Guanía | 2773.34 | 379.32 | 1698 | 3185.69 | 1.8 | 1.15 | 0.61 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4105 | Bajo Rio Guanía | 7911.65 | 838.55 | 3286 | 7441.47 | 2.36 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4106 | Río Aquió o Caño Aque | 2978.85 | 307.37 | 656 | 2166.78 | 1.41 | 0.73 | 0.22 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 41 | Guanía | 4107 | Directos Río Negro (md) | 3519.66 | 473.45 | 1951 | 3773.35 | 2.0 | 1.07 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4108 | Río Cuiary | 4387.85 | 594.84 | 1963 | 4526.71 | 2.24 | 1.03 | 0.45 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4109 | Río Isana | 3444.02 | 579.6 | 1152 | 3209.57 | 2.47 | 0.93 | 0.33 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 41 | Guanía | 4110 | Río Tomo | 2422.3 | 256.7 | 529 | 1699.51 | 1.3 | 0.7 | 0.22 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 42 | Vaupes | 4201 | Río Itilla | 2565.38 | 391.07 | 620 | 2233.21 | 1.93 | 0.87 | 0.24 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4202 | Río Unilla | 2303.8 | 353.11 | 447 | 1809.76 | 1.84 | 0.79 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4203 | Alto Vaupés | 8615.07 | 675.79 | 1749 | 6131.41 | 1.82 | 0.71 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4207 | Bajo Vaupés | 13402.76 | 1072.82 | 2743 | 8526.08 | 2.32 | 0.64 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4208 | Río Querary | 4275.8 | 582.99 | 857 | 2689.79 | 2.23 | 0.63 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4209 | Río Papurí | 5387.41 | 667.63 | 1101 | 3617.82 | 2.27 | 0.67 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 42 | Vaupes | 4211 | Río Tiquié | 1020.71 | 186.81 | 246 | 820.81 | 1.46 | 0.8 | 0.24 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 43 | Apaporis | 4301 | Río Tunia ó Macayá | 9253.02 | 849.66 | 2012 | 7260.7 | 2.21 | 0.78 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4302 | Río Ajaju | 7817.77 | 606.53 | 2458 | 7606.92 | 1.71 | 0.97 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4303 | Alto Río Apaporis | 12319.61 | 950.36 | 2814 | 9432.56 | 2.14 | 0.77 | 0.23 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4305 | Bajo Río Apaporis | 12739.33 | 991.16 | 2518 | 9084.08 | 2.2 | 0.71 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4306 | Río Cananari | 3839.19 | 419.52 | 931 | 3072.4 | 1.69 | 0.8 | 0.24 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 43 | Apaporis | 4307 | Río Pira Paraná | 5843.84 | 606.97 | 1556 | 5034.04 | 1.98 | 0.86 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 43 | Apaporis | 4309 | Directos Río Taraira | 1546.64 | 423.39 | 292 | 1196.87 | 2.69 | 0.77 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4401 | Alto Caqueta | 5813.76 | 448.5 | 4874 | 7969.25 | 1.47 | 1.37 | 0.84 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 44 | Caquetá | 4402 | Río Caqueta Medio | 15565.72 | 1684.37 | 4350 | 13222.47 | 3.38 | 0.85 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4403 | Río Orteguaza | 7905.2 | 608.09 | 3751 | 8899.37 | 1.71 | 1.13 | 0.47 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4404 | Río Pescado | 2066.91 | 301.11 | 1091 | 2376.67 | 1.66 | 1.15 | 0.53 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 44 | Caquetá | 4407 | Río Rutuya | 1134.73 | 173.78 | 356 | 1159.94 | 1.29 | 1.02 | 0.31 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 44 | Caquetá | 4408 | Río Mecaya | 4535.95 | 531.06 | 867 | 3140.71 | 1.97 | 0.69 | 0.19 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4409 | Río Sencella | 1741.46 | 343.43 | 376 | 1350.55 | 2.06 | 0.78 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4410 | Río Peneya | 1604.22 | 227.67 | 496 | 1543.41 | 1.42 | 0.96 | 0.31 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 44 | Caquetá | 4414 | Río Cuemaní | 2427.54 | 345.6 | 943 | 2748.25 | 1.75 | 1.13 | 0.39 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4415 | Río Caqueta Bajo | 25311.12 | 1753.12 | 7216 | 23202.18 | 2.75 | 0.92 | 0.29 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4417 | Río Cahuinarí | 15029.05 | 919.14 | 3897 | 13658.44 | 1.87 | 0.91 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4418 | Río Mirití-Paraná | 9004.68 | 872.51 | 1962 | 7349.48 | 2.3 | 0.82 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 44 | Caquetá | 4420 | Río Puré | 7628.25 | 565.65 | 1978 | 7199.08 | 1.62 | 0.94 | 0.26 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 45 | Yarí | 4501 | Alto Yarí | 7434.2 | 584.02 | 2988 | 7492.52 | 1.69 | 1.01 | 0.4 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 45 | Yarí | 4502 | Río Camuya | 2765.61 | 404.75 | 739 | 2244.45 | 1.92 | 0.81 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4504 | Medio Yarí | 5349.27 | 456.88 | 1059 | 4071.99 | 1.56 | 0.76 | 0.2 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 45 | Yarí | 4505 | Río Luisa | 3041.37 | 410.1 | 699 | 2910.25 | 1.86 | 0.96 | 0.23 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4506 | Bajo Yarí | 3863.39 | 513.83 | 1091 | 3396.76 | 2.07 | 0.88 | 0.28 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 45 | Yarí | 4509 | Río Cuñare | 5514.33 | 442.94 | 2020 | 5783.93 | 1.49 | 1.05 | 0.37 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 45 | Yarí | 4510 | Río Mesay | 8623.76 | 762.34 | 2197 | 7305.72 | 2.05 | 0.85 | 0.25 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4601 | Río Caguan Alto | 5837.11 | 612.17 | 2925 | 6346.7 | 2.0 | 1.09 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4602 | Río Guayas | 5491.62 | 477.6 | 3229 | 6759.71 | 1.61 | 1.23 | 0.59 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 46 | Caguán | 4604 | Río Caguan Bajo | 7413.53 | 721.41 | 1929 | 6074.55 | 2.09 | 0.82 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 46 | Caguán | 4605 | Río Sunsiya | 2465.71 | 430.93 | 654 | 2122.08 | 2.17 | 0.86 | 0.27 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4701 | Alto Río Putumayo | 6986.15 | 481.02 | 3477 | 7316.86 | 1.44 | 1.05 | 0.5 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 47 | Putumayo | 4702 | Río San_Miguel | 2244.85 | 373.51 | 588 | 2086.29 | 1.97 | 0.93 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4703 | Río Putumayo Medio | 5068.57 | 754.41 | 1049 | 3735.78 | 2.65 | 0.74 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4704 | Río Putumayo Directos (mi) | 3522.47 | 852.89 | 746 | 2198.03 | 3.59 | 0.62 | 0.21 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4705 | Río Cará-Paraná | 7315.68 | 737.49 | 2265 | 7190.22 | 2.16 | 0.98 | 0.31 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4706 | Río Putumayo Bajo | 14172.27 | 1779.28 | 3118 | 10514.43 | 3.74 | 0.74 | 0.22 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4707 | Río Igará-Paraná | 12879.11 | 872.39 | 3303 | 11189.37 | 1.92 | 0.87 | 0.26 | Oval-oblonga a rectangular-oblonga |
| 4 | Amazonas | 47 | Putumayo | 4710 | Río Cotuhe | 3643.88 | 355.47 | 760 | 2921.91 | 1.47 | 0.8 | 0.21 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 47 | Putumayo | 4711 | Río Purite | 1989.76 | 278.0 | 494 | 1686.79 | 1.56 | 0.85 | 0.25 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 48 | Amazonas - Directos | 4801 | Directos Río Amazonas (mi) | 3256.52 | 375.27 | 698 | 2444.36 | 1.64 | 0.75 | 0.21 | Oval-redonda a oval oblonga |
| 4 | Amazonas | 49 | Napo | 4901 | Río Chingual | 456.15 | 159.57 | 191 | 430.64 | 1.87 | 0.94 | 0.42 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5101 | Río San Juan (Frontera Ecuador) | 351.31 | 159.02 | 72 | 218.91 | 2.12 | 0.62 | 0.2 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5102 | Río Mira | 4093.84 | 623.44 | 1762 | 3257.49 | 2.44 | 0.8 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 51 | Mira | 5103 | Río Rosario | 833.46 | 151.6 | 438 | 636.91 | 1.31 | 0.76 | 0.53 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 51 | Mira | 5104 | Río Tola | 596.07 | 161.29 | 85 | 330.47 | 1.65 | 0.55 | 0.14 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5201 | Río Patia Alto | 3220.19 | 464.44 | 1201 | 3059.09 | 2.05 | 0.95 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5202 | Río Guachicono | 2627.15 | 281.07 | 2131 | 3992.4 | 1.37 | 1.52 | 0.81 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5203 | Río Mayo | 874.61 | 169.19 | 699 | 1261.15 | 1.43 | 1.44 | 0.8 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5204 | Río Juananbú | 2085.38 | 240.66 | 1278 | 2703.54 | 1.32 | 1.3 | 0.61 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5205 | Río Guáitara | 3653.86 | 377.21 | 1998 | 4607.85 | 1.56 | 1.26 | 0.55 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5206 | Río Telembí | 4641.09 | 377.59 | 1082 | 3235.67 | 1.39 | 0.7 | 0.23 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 52 | Patía | 5207 | Río Patia Medio | 2392.65 | 414.12 | 902 | 2233.99 | 2.12 | 0.93 | 0.38 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 52 | Patía | 5209 | Río Patia Bajo | 4534.66 | 454.54 | 892 | 2133.59 | 1.69 | 0.47 | 0.2 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5302 | Río Tapaje | 1604.0 | 251.96 | 660 | 1550.5 | 1.57 | 0.97 | 0.41 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5303 | Río Iscuandé | 2338.82 | 411.98 | 804 | 2010.59 | 2.13 | 0.86 | 0.34 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5304 | Río Guapi | 2626.35 | 278.84 | 1096 | 2631.89 | 1.36 | 1.0 | 0.42 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5305 | Río Timbiquí | 808.95 | 195.0 | 300 | 815.22 | 1.71 | 1.01 | 0.37 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5306 | Río Saija | 1089.23 | 200.98 | 518 | 1314.06 | 1.52 | 1.21 | 0.48 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5307 | Río San Juan del Micay | 4455.53 | 490.3 | 1775 | 4402.86 | 1.84 | 0.99 | 0.4 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5308 | Río Naya - Yurumanguí | 2667.43 | 319.11 | 1401 | 2885.23 | 1.54 | 1.08 | 0.53 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5309 | Ríos Cajambre - Mayorquín - Raposo | 2011.54 | 285.41 | 865 | 1596.64 | 1.59 | 0.79 | 0.43 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5310 | Río Anchicayá | 1293.58 | 231.68 | 460 | 1009.93 | 1.61 | 0.78 | 0.36 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 53 | Tapaje - Dagua - Directos | 5311 | Dagua - Buenaventura - Bahia Málaga | 1966.32 | 382.96 | 853 | 1962.14 | 2.16 | 1.0 | 0.43 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5401 | Río San Juan Alto | 2054.45 | 331.58 | 1025 | 2621.82 | 1.83 | 1.28 | 0.5 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5402 | Río Tamaná y otros Directos San Juan | 2827.0 | 329.17 | 1341 | 3447.38 | 1.55 | 1.22 | 0.47 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5403 | Río Sipí | 3028.03 | 334.48 | 1355 | 3683.39 | 1.52 | 1.22 | 0.45 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5404 | Río Cajón | 743.24 | 143.96 | 319 | 887.71 | 1.32 | 1.19 | 0.43 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5405 | Río Capoma y otros directos al San Juan | 2428.6 | 312.71 | 1259 | 3299.74 | 1.59 | 1.36 | 0.52 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5406 | Río Munguidó | 833.41 | 169.4 | 413 | 1147.54 | 1.47 | 1.38 | 0.5 | Oval-redonda a oval oblonga |
| 5 | Pacifico | 54 | San Juán | 5407 | Ríos Calima y  Bajo San Juan | 3543.49 | 554.72 | 1900 | 4440.96 | 2.33 | 1.25 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 54 | San Juán | 5408 | Río San Juan Medio | 935.33 | 291.72 | 544 | 1169.19 | 2.38 | 1.25 | 0.58 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5501 | Río Baudó | 4060.64 | 545.75 | 2238 | 5185.84 | 2.14 | 1.28 | 0.55 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 55 | Baudó - Directos Pacifico | 5502 | Río Docampadó y Directos Pacífico | 1908.15 | 324.3 | 1039 | 2428.37 | 1.86 | 1.27 | 0.54 | Oval-oblonga a rectangular-oblonga |
| 5 | Pacifico | 56 | Pacífico - Directos | 5601 | Directos Pacifico Frontera Panamá | 4256.46 | 1031.69 | 2419 | 5447.84 | 3.95 | 1.28 | 0.57 | Oval-oblonga a rectangular-oblonga |


### Referencias

* [Zonificación y Codificación de Cuencas Hidrográficas - Colombia - Suramérica](http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf)
* http://www.ideam.gov.co/capas-geo
* http://www.siac.gov.co/catalogo-de-mapas
* http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
* http://visor.ideam.gov.co/geovisor/#!/profiles/3
* [Hidrografía Colombiana - IDEAM y SiGaia (versión no oficial de zonificación a 2018)](https://www.arcgis.com/home/item.html?id=89f6818e093f4b0faa99b456ad98018d)
* https://desktop.arcgis.com/en/arcmap/10.6/tools/data-management-toolbox/calculate-geometry-attributes.htm

### Compatibilidad

* Compatible con ArcGIS for Desktop 10.6 o superior.
* Compatible con ArcGIS Pro.



[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6
[^5]: https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf