## Python - Script básico

Un script en Python, es un archivo que contiene diferentes instrucciones que pueden ser ejecutadas por el intérprete de comandos. Generalmente los archivos son almacenados con la extensión .py, y son usados para ejecutar o automatizar tareas repetitivas. Para la creación de los scripts, es recomendable utilizar un editor de código que permita identificar con facilidad la estructura y escritura propia del lenguaje o un entorno de desarrollo de aplicaciones (IDE), por ejemplo, Notepad++, Sublime Text, Gedit, Anaconda o PyCharm. En QGIS 3.10, desde la consola de Python es posible acceder al editor de scripts, desde el cual se puede crear, abrir, editar y ejecutar directamente este tipo de archivos. En ArcGIS Desktop, es posible editar y ejecutar archivos .py directamente desde el ambiente integrado de desarrollo o IDLE de Python incorporado.


### Objetivos

* En PyCharm, ejecutar el script usando la versión de Python 2.7.
* En PyCharm, ejecutar el script usando la versión de Python 3.7.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Entender las diferencias en impresión de pantalla usando la versión 2 y 3 de Python.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2. Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.
* Python 3.7.7 como instalación independiente.
* PyCharm 2020.1 for Anaconda.


### Editores

Para el desarrollo de este ejercicio podrá utilizar diferentes editores y comprobar su funcionamiento, por ejemplo:

* Editor de texto Sublime Text. https://www.sublimetext.com/. Sublime Text, no solamente 
permite la creación y edición de scripts en múltiples lenguajes, sino que a su vez permite ejecutar y visualizar scripts básicos, facilitando así el proceso de depuración.
* PyCharm. https://www.jetbrains.com/pycharm/ 
* PyCharm para Anaconda. https://www.jetbrains.com/pycharm/promo/anaconda/
* Notepad++. https://notepad-plus-plus.org/downloads/


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\BasicScript\ 


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo calcularemos el tiempo de concentración de una cuenca usando la expresión de Giandotti.

<div align="center">
  <br>
  <img alt="R.GISPython.BasicScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/TcGiangotti.png" width="200px">
</div>


### Parámetros de entrada
* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Descripción de archivos y carpetas

| Instrucción  | Explicación                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------|
| #            | Comentario de una línea.                                                                         |
| """<br/>"""  | 3 comillas simples o dobles permiten definir el inicio y fin de comentarios en múltiples líneas. |
| #-*- coding: UTF-8 -*- | Permite definir la codificación de texto utilizada en el script.  |
| print | Permite realizar la impresión de un resultado en la consola. En las versiones de Python 2.x, todo aquello que aparezca después del print será impreso en pantalla, incluso los paréntesis sí existen concatenaciones con comas. En las versiones de Python 3.x, solo se imprimirá aquello que esté entre paréntesis. Nótese que es posible realizar cálculos adicionales en la impresión (TcGiandotti*60) e incluso concatenar resultados usando coma o +. |
| str() | Permite convertir una variable o resultado numérico en una cadena de texto. Requerido para concatenación usando + |


Para ejecutar o modificar desde el IDLE de Python de ArcGIS for Desktop, en el explorador de Windows abrir la carpeta D:\R.GISPython\BasicScript y dar clic derecho en Tc_v0.py; seleccionar la opción Edit With IDLE. Ejecutar oprimiendo F5. Nota: Para lanzar correctamente el IDLE de ArcGIS Desktop, es necesario definir, en variables del sistema operativo Windows, el direccionamiento al directorio C:\Python27.

Para ejecutar desde la consola de comandos CMD del sistema operativo Windows usando cualquier versión de Python instalada, usar el comando py, la versión requerida (por ejemplo, -3.8) y la ruta completa del archivo .py.

* py -2.7 C:\HPSD\HPSD0001\Tc_v0.py
* py -3.7 C:\HPSD\HPSD0001\Tc_v0.py
* py -3.8 C:\HPSD\HPSD0001\Tc_v0.py

Para ejecutar desde QGIS, abrir la consola de Python, luego el editor de texto y el archivo creado. Observará que los resultados de los dos print son idénticos debido a que se ejecutó con la versión 3.7.0.


## Ilustraciones

![R.GISPython.BasicScript.Screenshot1](https://github.com/rcfdtools/R.HydroTools/blob/main/NombreHerramienta/Screenshot/Screenshot1.png)
![R.GISPython.BasicScript.Screenshot2](https://github.com/rcfdtools/R.HydroTools/blob/main/NombreHerramienta/Screenshot/Screenshot2.png)
![R.GISPython.BasicScript.Screenshot3](https://github.com/rcfdtools/R.HydroTools/blob/main/NombreHerramienta/Screenshot/Screenshot3.png)


## Referencias

* http://docs.python.org/2.7/tutorial/
* https://www.delftstack.com/howto/python/python-print-tab/


## Colaboradores

* Creado por r.cfdtools@gmail.com


## Compatibilidad

* Compatible con cualquier versión de Python.


## Keywords
Concentration time. Giandotti.


## Control de versiones

| Versión    | Descripción      |
|------------|------------------|
| v.20211201 | Versión inicial. | 


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License
