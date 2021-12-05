## Creación de scripts interactivos

Los scripts en Python permiten la entrada directa de datos desde la consola de comandos o desde el intérprete de comandos, para ello puede utilizar el comando `input()`.

> Atención: Actualmente, PyQGIS no permite entradas input desde scripts ejecutadas directamente desde el entorno gráfico, es necesario realizar la entrada desde un cuadro de dialogo. Más información en: https://gis.stackexchange.com/questions/53958/how-to-use-raw-input-in-qgis-python-console


### Objetivos

* En PyCharm, ejecutar el script usando la versión de Python 3.10.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Solicitar al usuario los valores de entrada de los parámetros requeridos.
* Verificar si los caracteres especiales como tildes y eñes se visualizan correctamente en Python 2.7 y 3.10.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* ArcGIS Pro 2.9+.
* PyCharm 2021.3+ for Anaconda. 

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.BasicScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/BasicScript/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


