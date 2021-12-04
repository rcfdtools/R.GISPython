<div align="center">
  <br>
  <img alt="R.HydroTools" src="https://github.com/rcfdtools/R.GISPython/blob/main/.Icons/R.GISPython.svg" width="300px">
  <h2>Algoritmos y programación GIS con Python</h2>
  by r.cfdtools@gmail.com
  <br><br>
</div>

### Introducción

Python es un potente lenguaje de programación interpretado con licencia de código abierto que soporta orientación a objetos y es comúnmente utilizado para la automatización de tareas en herramientas geográficas en ArcGIS Desktop y QGIS. Las herramientas que hacen parte de Python están disponibles en versiones de 32 y 64 bits, existiendo una limitante de hasta máximo 2GB en el tamaño de los archivos que pueden ser cargados en memoria para sistemas de 32 bits. Para el procesamiento profesional de grandes volúmenes de datos se recomienda que el sistema operativo, la aplicación GIS y Python sean de 64 bits. Para el desarrollo de los ejercicios de este curso se puede utilizar cualquier versión.

En ArcGIS for Desktop (p.e, 10.2.2), la versión integrada de Python es 2.7.5 y por defecto se instala en Microsoft Windows en el directorio C:\Python27.

En ArcGIS Pro (p.e, 2.9.0), la versión integrada de Python es 3.7.11, por defecto se instala en C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3 y por clonación en el directorio de usuario (p.e, Admin) en C:\Users\Admin\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone.

En QGIS (p.e, 3.10), las versiones integradas de Python son la 2.7.x y la 3.7.x, por defecto se instalan en Microsoft Windows en el directorio de archivos de programa localizado en C:\Program Files\QGIS 3.10\apps cuando se trata de versiones de 64 bits.


### ¿Qué es un Script en Python?

Un script en Python, es un archivo que contiene diferentes instrucciones o código que pueden ser ejecutadas por el intérprete de comandos. Generalmente los archivos son almacenados con la extensión .py y son usados para ejecutar o automatizar tareas repetitivas. Para la creación de scripts, es recomendable utilizar un editor de código que permita identificar con facilidad la estructura y escritura propia del lenguaje o un entorno de desarrollo de aplicaciones (IDE), por ejemplo, Notepad++, Sublime Text, Gedit, Anaconda o PyCharm. En QGIS (p.e, 3.10), desde la consola de Python es posible acceder al editor de scripts, desde el cual se puede crear, abrir, editar y ejecutar directamente este tipo de archivos. En ArcGIS for Desktop, es posible editar y ejecutar archivos .py directamente desde el ambiente integrado de desarrollo o IDLE de Python incorporado.


### Requerimientos

* ESRI ArcGIS for Desktop 10+
* ESRI ArcGIS Pro 2.9+
* QGIS 2.18.28
* QGIS 3.12+
* Python 2.7.17 standalone
* Python 3.7.7 standalone
* Anaconda (opcional)
* PyCharm Community https://www.jetbrains.com/pycharm/download/#section=windows
* PyCharm for Anaconda (opcional)
* Requerimientos específicos adicionales son indicados en cada script.


### Tema 1. Fundamentos generales de Python

Este tema presenta fundamentos básicos necesarios para la comprensión de codificación de scripts usando el lenguaje Python.  

| Actividad                                                                                                                         | Descripción                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Identificar y ejecutar cualquier versión de Python instalada](https://github.com/rcfdtools/R.GISPython/tree/main/PythonVersion)  | En el sistema operativo pueden existir y convivir, además de las versiones integradas a las herramientas GIS, otras versiones de Python registradas y una como versión por defecto. Identificar las versiones instaladas le permitirá realizar pruebas de ejecución de comandos por consola o a través de scripts.                                                 |
| [Definir la versión por defecto en el OS y configurar PyCharm](https://github.com/rcfdtools/R.GISPython/tree/main/DefaultVersion) | Definir una versión por defecto de Python en el CMD de Microsoft Windows, le permitirá lanzar este intérprete desde cualquier directorio de su sistema operativo sin tener que ingresar la ruta completa del ejecutable Python.exe y la configuración de intérpretes en PyCharm, le permitirá ejecutar los scripts de un proyecto utilizando una versión predefinida de Python.|
| Consultar módulos disponibles, palabras reservadas y bloques de ayuda                                                             | Dependiendo de la versión de Python instalada, dispondrá de algunas librerías o módulos preinstalados. Python además, al igual que otros lenguajes de programación, dispone de palabras reservadas que no podrán ser utilizadas para definir variables u objetos de usuario.                                                                                       |
| Usar Python como una calculadora                                                                                                  | Desde la consola de Python, es posible realizar operaciones matemáticas simples o complejas, definir variables, listas, tuplas, funciones, llamar módulos y en general utilizar cualquier elemento integrado al lenguaje.                                                                                                                                          |
| [Script básico](https://github.com/rcfdtools/R.GISPython/tree/main/BasicScript)                                                   | Un script en Python, es un archivo que contiene diferentes instrucciones que pueden ser ejecutadas por el intérprete de comandos. Generalmente los archivos son almacenados con la extensión .py, y son usados para ejecutar o automatizar tareas repetitivas. Ejemplo usando PyCharm, Command CMD, ArcGIS For Desktop, ArcGIS Pro y QGIS.                         |
| Creación de scripts interactivos                                                                                                  | Los scripts en Python permiten la entrada directa de datos desde la consola de comandos o desde el intérprete de comandos, para ello puede utilizar el comando input().                                                                                                                                                                                            |
| Creación de scripts interactivos e iterativos con funciones                                                                       | Python dispone de múltiples estructuras para la ejecución de procesos iterativos, como while, for y range.                                                                                                                                                                                                                                                         |
| Instalación de librerías - Gráficas usando matplotlib                                                                             | Complementariamente a las librerías obtenidas con la instalación de Python, es posible adicionar nuevas librerías que posteriormente podrán ser invocadas desde la consola o desde scripts.                                                                                                                                                                        |
| Control de excepción de errores                                                                                                   | En el evento de que el usuario ingrese valores nulos o fuera de rango, el código deberá ser capaz de controlar estas excepciones para no devolver al usuario valores errados. Algunos controles de ejecución pueden ser implementados usando condicionales para la validación de los datos ingresados, o a través de los controles de ejecución propios de Python. |
| Script con archivo log de ejecución y resultados                                                                                  | Al ejecutar scripts, los resultados son mostrados en la consola del entorno de desarrollo o en el Command del sistema operativo. Los resultados también pueden ser volcados en un archivo de registro que puede ser creado y actualizado directamente desde el código. Para este procedimiento utilizaremos la instrucción .write().                               |

> Nota: los datos hidroclimatológicos utilizados para ejemplificar algunos de los ejemplos corresponden a información tomada y procesada a partir de datos del IDEAM - Colombia  y los archivos de formas vectoriales han sido descargados del IGAC - Colombia y de otras fuentes alternas.


### Referencias generales

* https://www.educba.com/programming-vs-scripting/


### Keywords

`Esri ArcGIS ModelBuilder` `Esri ArcGIS ArcToolBox` `QGIS Graphical Modeler`


### Clonación
Para compatibilidad completa de las rutas utilizadas en los scripts y herramientas de R.GISPython, en Microsoft Windows clonar y/o descomprimir en _D:\R.GISPython_. https://github.com/rcfdtools/R.GISPython.git
