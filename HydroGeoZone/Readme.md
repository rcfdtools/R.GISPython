## Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p.ej, el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico. [^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.


| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales. [^2]

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




### Resultados

Áreas hidrográficas
| COD_AH | NOM_AH | Area | Perm | FREQUENCY | SUM_LDre | Kc | Dd | Dc |
|---|---|---|---|---|---|---|---|---|
| 1 | Caribe | 102803.08 | 4814.69 | 39119 | 108190.65 | 3.75 | 1.05 | 0.38 |
| 2 | Magdalena Cauca | 270888.94 | 3763.38 | 134281 | 314458.56 | 1.81 | 1.16 | 0.5 |
| 3 | Orinoco | 346081.36 | 3736.08 | 122458 | 301766.4 | 1.59 | 0.87 | 0.35 |
| 4 | Amazonas | 341164.55 | 6122.88 | 101572 | 298438.97 | 2.62 | 0.87 | 0.3 |
| 5 | Pacifico | 77372.03 | 3360.07 | 35124 | 81609.93 | 3.02 | 1.05 | 0.45 |


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