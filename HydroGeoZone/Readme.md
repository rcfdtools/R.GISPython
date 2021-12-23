## Zonificación hidrográfica de Colombia - Análisis usando Python

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p.ej, el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico. [^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales. [^2]

| ID  | AH - Área Hidrográfica |
|-----|------------------------|
| 1   | Caribe                 |
| 2   | Magdalena-Cauca        |
| 3   | Orinoco                |
| 4   | Amazonas               |
| 5   | Pacífico               |

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

* Drenajes de Colombia: tomados de los datos abiertos IGAC a escala 1:25k.
* Subzonas hidrográficas de Colombia: 




### Referencias

* [Zonificación y Codificación de Cuencas Hidrográficas - Colombia - Suramérica](http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf)
* http://www.ideam.gov.co/capas-geo
* http://www.siac.gov.co/catalogo-de-mapas
* http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
* http://visor.ideam.gov.co/geovisor/#!/profiles/3
* [Hidrografía Colombiana - IDEAM y SiGaia](https://www.arcgis.com/home/item.html?id=89f6818e093f4b0faa99b456ad98018d)



[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf