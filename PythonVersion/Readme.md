## Identificar y ejecutar cualquier versión de Python instalada

En el sistema operativo pueden existir y convivir, además de las versiones integradas a las herramientas GIS, otras versiones de Python registradas y una como versión por defecto. Identificar las versiones instaladas le permitirá realizar pruebas de ejecución de comandos por consola o a través de scripts.

### Objetivos

* Identificar las versiones instaladas de Python en su sistema operativo SO.
* Identificar los directorios de instalación de Python.
* Identificar la versión instalada de Python en ArcGIS for Desktop.
* Identificar la versión instalada de Python en ArcGIS Pro.
* Identificar la versión instalada de Python en QGIS.

### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* ArcGIS Pro 2.9+.
* PyCharm 2021.3+ for Anaconda. 

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.


### Consulta de versiones desde el command CMD de Microsoft Windows

Para conocer la versión asociada en las rutas por defecto del sistema operativo Microsoft Windows:

1. Ir a Inicio, en el cuadro de búsqueda digitar `CMD` y dar Enter o presionar la combinación de teclas `Windows+R` ingresando CMD y dando clic en Ok. 
2. En el prompt del sistema digitar `C:\Python` y dar Enter o utilizar el comando `Python.exe --version` de esta forma podrá conocer la versión por defecto definida en las variables de entorno.
3. Para salir de la consola de Python usar `Ctrl+Z` y enter o usar el comando `quit()`. 

>Es posible al ingresar Python y dar Enter no se ejecute ninguna instrucción o el SO devuelva un error indicado que el comando ingresado no existe, esto significa que su sistema operativo no dispone por defecto de una versión de Python definida en el entorno de trabajo.
