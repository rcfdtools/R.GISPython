## Python - Script básico

Un script en Python, es un archivo que contiene diferentes instrucciones que pueden ser ejecutadas por el intérprete de comandos. Generalmente los archivos son almacenados con la extensión .py, y son usados para ejecutar o automatizar tareas repetitivas. Para la creación de los scripts, es recomendable utilizar un editor de código que permita identificar con facilidad la estructura y escritura propia del lenguaje o un entorno de desarrollo de aplicaciones (IDE), por ejemplo, Notepad++, Sublime Text, Gedit, Anaconda o PyCharm. En QGIS (p.e, 3.10), desde la consola de Python es posible acceder al editor de scripts, desde el cual se puede crear, abrir, editar y ejecutar directamente este tipo de archivos. En ArcGIS Desktop, es posible editar y ejecutar archivos .py directamente desde el ambiente integrado de desarrollo o IDLE de Python incorporado.


### Objetivos

* En PyCharm, ejecutar el script usando la versión de Python 2.7.5.
* En PyCharm, ejecutar el script usando la versión de Python 3.10.0.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Entender las diferencias en impresión de pantalla usando la versión 2 y 3 de Python.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2. Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.
* Python 3.10.0 como instalación independiente.
* PyCharm 2021.3 for Anaconda. 


### Editores

Para el desarrollo de este ejercicio podrá utilizar diferentes editores y comprobar su funcionamiento, por ejemplo:

* Editor de texto Sublime Text. https://www.sublimetext.com/. Sublime Text, no solamente permite la creación y edición de scripts en múltiples lenguajes, sino que a su vez permite ejecutar y visualizar scripts básicos, facilitando así el proceso de depuración.
* PyCharm Community. https://www.jetbrains.com/pycharm/download/
* PyCharm para Anaconda para integración conJupiter. https://www.jetbrains.com/pycharm/promo/anaconda/
* Notepad++. https://notepad-plus-plus.org/downloads/


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\BasicScript\ 


## Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<img alt="R.GISPython.BasicScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/TcGiangotti.png" width="300px">


### Parámetros
* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m

### Script

```
# -*- coding: UTF-8 -*-
# Nombre: Tc_v0.py
# Descripción: Script básico para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente)

# Librerías
import sys

# Cabecera
print ('------------------------')
print ('Script básico en Python')
print ('------------------------\n')
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com')

# Variables
A = 9.1348		#Área cuenca, km²
L = 4.6106		#Longitud cauce principal, km
S = 0.144015	#Pendiente media cauce principal, m/m

# Cálculos e impresión de resultados
TcGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ('\nParámetros de entrada')
print ('\tÁrea cuenca, km²: ' + str(A))
print ('\tLongitud cauce principal, km: ' + str(L))
print ('\tPendiente media cauce principal, m/m: ' + str(S))
print ('\nResultados')
print ('\tTc(min):', TcGiandotti*60) #Impresión en pantalla usando coma, no compatible con Python 2. Coma agrega espacio.
print ('\tTc(min): ' + str(TcGiandotti*60)) #Impresión en pantalla usando +, compatible con cualquier versión de Python. + requiere de ingreso manual de espacio.
```

## Descripción instrucciones empleadas

| Instrucción  | Explicación                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #            | Comentario de una línea.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| """<br/>"""  | 3 comillas simples o dobles permiten definir el inicio y fin de comentarios en múltiples líneas.                                                                                                                                                                                                                                                                                                                                                            |
| #-*- coding: UTF-8 -*- | Permite definir la codificación de texto utilizada en el script.                                                                                                                                                                                                                                                                                                                                                                                            |
| print | Permite realizar la impresión de un resultado en la consola. En las versiones de Python 2.x, todo aquello que aparezca después del print será impreso en pantalla, incluso los paréntesis sí existen concatenaciones con comas. En las versiones de Python 3.x, solo se imprimirá aquello que esté entre paréntesis. Nótese que es posible realizar cálculos adicionales en la impresión (TcGiandotti*60) e incluso concatenar resultados usando coma o +. |
| str() | Permite convertir una variable o resultado numérico en una cadena de texto. Requerido para concatenación usando +                                                                                                                                                                                                                                                                                                                                           |


Para ejecutar o modificar desde el IDLE de Python de ArcGIS for Desktop, en el explorador de Windows abrir la carpeta D:\R.GISPython\BasicScript y dar clic derecho en Tc_v0.py; seleccionar la opción Edit With IDLE. Ejecutar oprimiendo F5. Nota: para lanzar correctamente el IDLE de ArcGIS Desktop, es necesario definir, en variables del sistema operativo Windows, el direccionamiento al directorio C:\Python27.

Para ejecutar desde la consola de comandos CMD del sistema operativo Windows usando cualquier versión de Python instalada, usar el comando py, la versión requerida (por ejemplo, -3.10) y la ruta completa del archivo .py.

```py -2.7 D:\R.GISPython\BasicScript\Tc_v0.py```

```py -3.10 D:\R.GISPython\BasicScript\Tc_v0.py```

Para ejecutar desde QGIS, abrir la consola de Python, luego el editor de texto y el archivo creado. Observará que los resultados de los dos print son idénticos debido a que se ejecutó con la versión 3.7.0.


## Ilustraciones

Ejecución en PyCharm usando Python 2.7.5 de ArcGIS for Desktop 10.2.2. En esta versión podrá notar diferencias en la impresión concatenada usando comas o +.
![R.GISPython.BasicScript.Python2.7.5PyCharm2021.3](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python2.7.5PyCharm2021.3.png)

Ejecución en PyCharm usando Python 3.10.0. En esta versión las dos impresiones son idénticas sin importar si se concatenó con comas o +.
![R.GISPython.BasicScript.Python3.10.0PyCharm2021.3](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python3.10.0PyCharm2021.3.png)

Ejecución en consola CMD Python 2.7.5 de ArcGIS for Desktop 10.2.2. En esta versión, la codificación de texto no imprime correctamente caracteres acentuados del español.
![R.GISPython.BasicScript.Python2.7.5ArcGISDesktop10.2.2CMD](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python2.7.5ArcGISDesktop10.2.2CMD.png)

Ejecución en consola CMD Python 3.10.0 Standalone.
![R.GISPython.BasicScript.Python3.10.0StandaloneCMD](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python3.10.0StandaloneCMD.png)

Script sobre IDLE de Python 2.7.5 en ArcGIS for Desktop.
![R.GISPython.BasicScript.Python2.7.5ArcGISDesktopIDLE](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python2.7.5ArcGISDesktopIDLE.png)

Ejecución en Python 3.9.5 sobre QGIS 3.22.1.
![R.GISPython.BasicScript.Python3.9.5QGIS3.22.1](https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/Python3.9.5QGIS3.22.1.png)


## Referencias

* http://docs.python.org/2.7/tutorial/
* https://www.delftstack.com/howto/python/python-print-tab/


## Colaboradores

* Creado por r.cfdtools@gmail.com


## Compatibilidad

* Compatible con cualquier versión de Python.


## Keywords
Concentration time. Giandotti. Subbasin. Hydrology.


## Control de versiones

| Versión    | Descripción                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------|
| v.20211201 | Versión inicial con incorporación de librería _sys_ para impresión en pantalla de la versión de Python.| 


## Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License
