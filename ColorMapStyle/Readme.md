## Generador de rampas de color para representación de grillas en ArcGIS
Keywords: `ArcGIS` `Python 3` `matplotlib` `sys` `datetime` `open()` `write()` `close()` `abs()` `append()` `range()` `zfill()`

Las rampas de color son utilizadas para representar los valores de celdas o pixeles contenidos dentro de una grilla o mapa raster. Esri ArcGIS for Desktop y ArcGIS Pro, dispone de múltiples estilos de representación y a partir de la versión Desktop 10.6, estos estilos pueden ser creados por el usuario a través del administrador de estilos disponible en el menú Personalización; sin embargo, la creación de estilos en versiones anteriores y el reescalamiento y representación de grillas interpolas de resultados en una serie temporal, requieren de la creación manual de archivos .clr que luego pueden ser asociados a cada grilla de salida, perimitiendo de esta forma representar un mismo valor de celda en diferentes grillas con un mismo color. El propósito principal de este microcontenido, es crear estilos personalizados que luego serán utilizados en las actividades relacionadas con [Interpolación y representación espacial de series de datos meteorológicos con simbología de rampa única](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid).


### Caso de estudio

Representar manualmente en múltiples estilos de color personalizados el mapa de precipitación media multianual de Colombia Suramérica, disponible en la base de datos [HidroSIG](https://minas.medellin.unal.edu.co/departamentos/geocienciasymedioambiente/hidrosig/es/hidrosig-4-0.html) creada por la [Facultad de Minas de la Universidad Nacional de Colombia - Sede Medellín](https://minas.medellin.unal.edu.co/).


### Requerimientos

* [PyCharm 2021.3 Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows)
* [Python 3+](https://www.python.org/) 
* [Sistema operativo Microsoft Windows](https://www.microsoft.com/en-us/windows?r=1)
* [matplotlib](https://matplotlib.org/)


### Funcionalidades

* Generación de archivos de rampa de color .clr a partir de arreglos de colores definidos por el usuario en formato RGB.
* Definición del número de colores discretos que contendrá la rampa, p.ej, 128, 256, 512, 1024, 2048.
* Archivo `ColorMapStyleValue.py` independiente con múltiples estilos de color de referencia personalizados. 
* Conversión de valores RGB a valores escalados de representación en Python entre 0 y 1.
* Generación y exportación a formato PNG de gráfica de rampa de color usando matplotlib.
* Generación de registro de ejecución detallado en formado Markdown.
* Visualización de rampa de colores en formato texto sobre la consola de ejecución.

> Dependiendo de la combinación de los colores de referencia y eel número de colores discretos, es posible que algunos valores discretos RGB se repitan, p.ej, en una rampa de color de blanco a negro solo pueden existir 255 colores discretos y sin en la definición de generación del archivo .clr se han definido 512 colores, por cada color se crearan dos registros con los mismos valores. 

 
### Ruta de ejecución

Para el desarrollo de este microcontenido se recomienda que los scripts y demás archivos requeridos se alojen en `D:\R.GISPython\ColorMapStyle` utilizando la siguiente estructura de directorios. 

| Directorio                                                                                 | Descripción                                                                                           |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [/Data](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Data)             | Directorio de datos del caso de estudio.                                                              |
| [/Map](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Map)               | Directorio con mapas para visualización en ArcGIS for Desktop y ArcGIS Pro.                           |
| [/Old](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Old)               | Directorio con versiones antiguas del script.                                                         |
| [/Output](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output)         | Directorio de salida con rampas de color .clr, previsualización en .png y registro de ejecución .md.  |
| [/Screenshot](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Screenshot) | Capturas de pantalla con resultados de ejecución.                                                     |

> El directorio `/Output` contiene mapas ejemplo para cada rampa de color generada usando la grilla de precipitación mensual media multianual. Para la representación se generaron y utilizaron archivos .clr con 16000 colores. 


### Procedimiento para la obtención de la grilla de precipitación media

1. Descargar e instale HidroSIG 4.0 y descomprima la Base de datos de Colombia, [clic aquí](https://minas.medellin.unal.edu.co/departamentos/geocienciasymedioambiente/hidrosig/es/descargas.html).

![HidroSIG4.0Descarga.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/HidroSIG4.0Descarga.png) 

> HidroSIG 4.0 requiere de la instalación de de MapWindow GIS 4.6.

2. En MapWindow GIS, clic en el menú _HidroSIG_ - _Base de Datos_ - _Conectar / Desconectar_, seleccione el proveedor _BD SQLite_ y defina la fuente de datos correspondiente al archivo _Colombia.db_.

![HidroSIG4.0Conectar.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/HidroSIG4.0Conectar.png) 

3. En MapWindow GIS, clic en el menú _HidroSIG_ - _Base de Datos_ - Explorar datos. En el panel derecho, expanda Conexiones - Data y de _doble clic_ sobre _Precipitación KDE_, correspondiente a la precipitación analizada mediante el núcleo de estimación de densidad. Luego de dar _doble clic_ el mapa será cargado automáticamente en el visor de MapWindow GIS.

![HidroSIG4.0Visualizar.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/HidroSIG4.0Visualizar.png)

4. Exporte la grilla utilizando el botón _Exportar_ que se encuentra en la esquina inferior derecha del Explorador de bases de datos, nombre como `PrecipitacionKDE.asc` en la carpeta `D:\R.GISPython\ColorMapStyle\Data`. La grilla será exportada en formato Ascii (.asc) y sin sistema de proyección de coordenadas embebido.

![HidroSIG4.0Exportar.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/HidroSIG4.0Exportar.png)

> Complementaria a la grilla de precipitación KDE, se ha incluido en la carpeta `/Datos`, una capa vectorial en formato Shapefile (Country.shp) con el límite de Colombia - Suramérica, el cual ha sido creado a partir de la Subzonas Hidrográficas - SZH realizada por el [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia y es utilizado para ejemplificar el límite de la zona de estudio. Más información acerca de las SZH en [Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone).


### Procedimiento para la generación de rampas utilizando el script 

1. Utilizando GitHub, clone el presente directorio o manualmente realice la descarga los script en Python y cree la estructura de directorio recomendada en `D:\R.GISPython\ColorMapStyle`.

![MicrosoftWindowsFolder.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/MicrosoftWindowsFolder.png)

2. En PyCharm, abra y explore el archivo de definición de rampas de color denominado `ColorMapStyleValue.py`, encontrará múltiples estilos predefinidos. 

![PyCharmColorMapStyleValue.png](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Screenshot/PyCharmColorMapStyleValue.png)

> En caso de que quiera crear un nuevo estilo, al final de este script, agregue un nuevo arreglo continuando con el número consecutivo de la secuencia definida, p.ej, `ColorMap14 = []`.

3. En PyCharm, abra el script `ColorMapStyle.py` y modifique las líneas de código asociadas al arreglo definido en la definición de estilos realizada en el archivo `ColorMapStyleValue.py`, p.ej, para generar o actualizar la rampa de color 13, defina `baseRGBColors = cmsv.ColorMap13` con `styleNumber = 13` y 

```
baseRGBColors = cmsv.ColorMap13  # ✅✅✅ User can change ✅✅✅ - Style values from ColorMapStyleValue.py
styleNumber = 13  # ✅✅✅ User can change ✅✅✅
numColor = 1024  # ✅✅✅ User can change ✅✅✅
```


## Rampas disponibles

### Style 1

* Name: ColorMap1 - Grayscale
* RGB Color values: 2
* Colors: White - Black
* Deep color file (.clr): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s1.clr)
[256. ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s1.clr)
* Log de ejecución (.md): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s1.md)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s1.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS128s1.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs1Map.png) |


### Style 2

* Name: ColorMap2 - Grayscale invert
* RGB Color values: 2
* Colors: Black - White
* Deep color file (.clr): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s2.clr)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s2.clr)
* Log de ejecución (.md): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s2.md)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s2.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS128s2.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs2Map.png) |


### Style 3

* Name: ColorMap3 - Pantone 2
* RGB Color values: 2
* Colors: Blue - Red
* Deep color file (.clr): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s3.clr)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s3.clr)
* Log de ejecución (.md): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s3.md)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s3.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS128s3.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs3Map.png) |


### Style 4

* Name: ColorMap4 - Pantone 3
* RGB Color values: 3
* Colors: Blue - Red - Green
* Deep color file (.clr): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s4.clr)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s4.clr)
* Log de ejecución (.md): 
[128, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS128s4.md)
[256.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s4.md)

| Sample ramp                                                                                              | Sample map                                                                                               |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS128s4.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs4Map.png) |


### Style 5

* Name: ColorMap5 - Pantone 4
* RGB Color values: 4
* Colors: Blue - Red - Green - Yellow
* Deep color file (.clr): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s5.clr)
[512.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s5.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s5.md)
[512.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s5.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s5.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs5Map.png) |


### Style 6

* Name: ColorMap6 - Laser print
* RGB Color values: 7
* Colors: Orange - Light BLue - Magenta - Dark Blue - Yellow - Green - Red
* Deep color file (.clr):
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s6.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s6.clr)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s6.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s6.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s6.md)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s6.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s6.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs6Map.png) |


### Style 7

* Name: ColorMap7
* RGB Color values: 7
* Colors: Yellow - Pink - Green - Blue
* Deep color file (.clr):
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s7.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s7.clr)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s7.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s7.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s7.md)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s7.md)

| Sample ramp                                                                                               | Sample map                                                                                               |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s7.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs7Map.png) |


### Style 8

* Name: ColorMap8
* RGB Color values: 7
* Colors: Gray - Aquamarine - Sea Blue
* Deep color file (.clr):
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s8.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s8.clr)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s8.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s8.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s8.md)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s8.md)

| Sample ramp                                                                                               | Sample map                                                                                                |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s8.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs8Map.png) |


### Style 9

* Name: ColorMap9
* RGB Color values: 13
* Colors: Dark Pink - Mercury - Lime - Green
* Deep color file (.clr):
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s9.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s9.clr)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s9.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s9.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s9.md)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s9.md)

| Sample ramp                                                                                               | Sample map                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s9.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs9Map.png) |

### Style 10

* Name: ColorMap10 - HKS Color
* RGB Color values: 15
* Colors: Green to yellow to red
* Deep color file (.clr):
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s10.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s10.clr)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s10.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s10.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s10.md)
[1024.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s10.md)

| Sample ramp                                                                                               | Sample map                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS256s10.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs10Map.png) |

### Style 11

* Name: ColorMap11 - HKS Colors Extend
* RGB Color values: 22
* Colors: Green to yellow to red to purple
* Deep color file (.clr): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s11.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s11.clr)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s11.clr)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s11.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s11.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s11.md)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s11.md)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s11.md)

| Sample ramp                                                                                               | Sample map                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS512s11.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs11Map.png) |


### Style 12

* Name: ColorMap12
* RGB Color values: 20
* Colors: Green Sea - Blue Sea - Purple - Red - Orange - Yellow
* Deep color file (.clr): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s12.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s12.clr)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s12.clr)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s12.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s12.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s12.md)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s12.md)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s12.md)

| Sample ramp                                                                                               | Sample map                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS512s12.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs12Map.png) |

### Style 13

* Name: ColorMap13
* RGB Color values: 42
* Colors: Green Sea - Blue Sea - Purple - Red - Orange - Yellow - Green to yellow to red to purple
* Deep color file (.clr): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s13.clr)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s13.clr)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s13.clr)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s13.clr)
* Log de ejecución (.md): 
[256, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS256s13.md)
[512, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS512s13.md)
[1024, ](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS1024s13.md)
[2048.](https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle/Output/ColorMapArcGIS2048s13.md)

| Sample ramp                                                                                              | Sample map                                                                                                 |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![512](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGIS512s13.png) | ![1024](https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle/Output/ColorMapArcGISs13Map.png)  |


### References

* https://desktop.arcgis.com/en/arcmap/latest/map/styles-and-symbols/working-with-color.htm
* https://desktop.arcgis.com/en/arcmap/latest/map/styles-and-symbols/working-with-color-ramps.htm
* https://matplotlib.org/stable/gallery/axes_grid1/simple_colorbar.html
* https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
* http://www.zonums.com/online/color_ramp/
* [Python rgb color changing text](https://www.codegrepper.com/code-examples/python/python+rgb+color+changing+text)
* https://matplotlib.org/stable/tutorials/colors/colormaps.html
* https://matplotlib.org/stable/tutorials/colors/colors.html
* https://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame
* https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
* https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
* https://es.stackoverflow.com/questions/334170/es-posible-agregar-ceros-a-la-derecha
* https://pro.arcgis.com/en/pro-app/2.8/tool-reference/spatial-analyst/kernel-density.htm