## Instalación, actualización de paquetes y creación de gráficas básicas usando matplotlib

Complementariamente a las librerías obtenidas con la instalación de Python, es posible adicionar nuevas librerías que posteriormente podrán ser invocadas desde la consola o desde scripts y también se pueden actualizar las librerías preinstaladas. El procedimiento más común de instalación automatizada se realiza a través del comando de consola `pip` disponible en el directorio _Scripts_ de Python. 

Para el ejemplo de estimación del tiempo de concentración, además de permitir la entrada de datos del usuario y calcular la variación del tiempo obtenido cambiando la pendiente desde un valor bajo (p.ej, 0.001 m/m) hasta la pendiente ingresada por el usuario y para un determinado número de variaciones (p.ej, 12), crearemos una gráfica que permita analizar visualmente la tendencia de los datos.

> Dentro de las versiones independientes o standalone de Python no se incorpora el paquete matplotlib, sin embargo, puede ser instalada manualmente o desde PyCharm.


### Objetivos

* Instalar el paquete o librería matplotlib y actualizar paquetes preinstalados en Python.
* En PyCharm, ejecutar el script usando la versión de Python 2.7 y 3.10.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Graficar diferentes tiempos de concentración Tc variando la pendiente.

> Atención: no es recomendable actualizar las librerías preinstaladas de Python para ArcGIS, lo anterior debido a que son utilizadas por todo el entorno del paquete y su modificación puede ocasionar resultados inesperados debido al orden y etiquetado en la entrada de parámetros.


### ¿Qué es matplotlib?

Matplotlib es una librería que permite la graficación de datos en múltiples estilos de visualización; por defecto, esta librería viene incorporada en la instalación de Python en ArcGIS for Desktop, ArcGIS Pro y QGIS 3.

> Para conocer la versión instalada de esta o cualquier librería disponible, en la consola de Python, importar la librería e ingresar la instrucción o etiqueta de versión `libreria.__version__`.<br><br>
> Para conocer la localización de los archivos usar `matplotlib.__file__`.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\InstallPackageGraph\ 


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.InteractiveScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Script Tc_v3.py

```

```


### Descripción instrucciones y comandos empleados


> En Python, por defecto se asume que la entrada ingresada por consola a través del comando `input()` es una cadena de texto, por tal motivo, cuando se trata de entradas numéricas, será necesaria la conversión a tipo flotante. <br><br>
> Dentro del paréntesis de la entrada `input()`, es necesario ingresar un texto descriptivo que permita al usuario entender el tipo y valor requerido.


### Procedimiento en Python 3.10.0

1. En el command o _CMD_ de Windows ejecutar `py -3.10 -m pip install -U pip`. Esta instrucción permite actualizar la versión existente de `pip` antes de instalar paquetes adicionales recientes.

> En el evento de que el paquete _pip_ no se encuentre instalado, la instrucción anterior realizará la instalación. 

![Python3.10.0StandaloneCMDpipUpdate.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDpipUpdate.png)

> La actualización también puede ser realizada directamente desde PyCharm, oprimir `Ctrl+Alt+S`, ir a la pestaña _Project_, seleccionar _Python Interpreter_, seleccionar _Python 3.10_, dar doble clic en el paquete _pip_ y en la ventana _Available Packages_ seleccionar _pip_, especificar la versión a actualizar y dar clic en Install Package.

![Python3.10.0StandalonePyCharm2021.3pipUpdate.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandalonePyCharm2021.3pipUpdate.png)

2. Para la instalación de la versión más actual de _matplotlib_, en el CMD ejecutar `py -3.10 -m pip install -U matplotlib`.

![Python3.10.0StandaloneCMDmatplotlibInstall.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDmatplotlibInstall.png)

> matplotlib también puede ser instalado directamente desde el administrador de paquetes de PyCharm para el intérprete de Python seleccionado por el usuario.

3. Para verificar la correcta instalación de la librería, en el CMD del sistema, ejecutar Python `C:\py -3.10` y realizar el llamado de la librería y consultar la versión y ruta de instalación a través de los comandos `import matplotlib', `matplotlib.__version__' y `matplotlib.__path__`

![Python3.10.0StandaloneCMDmatplotlibCheck.png](https://github.com/rcfdtools/R.GISPython/blob/main/InstallPackageGraph/Screenshot/Python3.10.0StandaloneCMDmatplotlibCheck.png)







### Referencias

* https://packaging.python.org/en/latest/tutorials/installing-packages/