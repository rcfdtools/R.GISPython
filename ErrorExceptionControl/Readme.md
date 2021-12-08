## Control de excepción de errores

En el evento de que el usuario ingrese valores nulos o fuera de rango, el código deberá ser capaz de controlar estas excepciones para no devolver al usuario valores errados. Algunos controles de ejecución pueden ser implementados usando condicionales para la validación de los datos ingresados, o a través de los controles de ejecución propios de Python.

> `try`: Controla la ejecución del código a través de la evaluación de las instrucciones contenidas en la indentación, permitiendo además ejecutar acciones para cada tipo de error encontrado utilizando except.

Para el ejemplo de estimación del tiempo de concentración, además de permitir la entrada de datos del usuario, calcular la variación del tiempo obtenido cambiando la pendiente desde un valor bajo (p.ej, 0.001 m/m) hasta la pendiente ingresada por el usuario y para un determinado número de variaciones (p.ej, 12), crear la gráfica que permita analizar visualmente la tendencia de los datos; evaluaremos que los parámetros ingresados sean positivos y que sean ingresados correctamente.


### Objetivos

* En PyCharm, ejecutar el script usando la versión de Python 2.7 y 3.10.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Implementar control de excepción de errores en el script de cálculo del Tc.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.
* Sistema operativo Microsoft Windows.

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7 de Python.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\ErrorExceptionControl\ 


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.InteractiveScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Script Tc_v4.py
```

```


### Descripción instrucciones y comandos empleados



> En Python, por defecto se asume que la entrada ingresada por consola a través del comando `input()` es una cadena de texto, por tal motivo, cuando se trata de entradas numéricas, será necesaria la conversión a tipo flotante. <br><br>
> Dentro del paréntesis de la entrada `input()`, es necesario ingresar un texto descriptivo que permita al usuario entender el tipo y valor requerido.<br><br>
> Para la ejecución en Python 2, no se recomienda imprimir el título de la gráfica debido a que ha sido ensamblado a partir de la concatenación de varios de los valores ingresados.




### Ejecución desde Pycharm

> PyCharm requiere de configuración previa del intérprete de Python a utilizar en la ejecución del script. Oprima `Ctrl+Alt+S` para acceder a la ventana de configuración y en la pestaña _Project: R.GISPython_ configurar los intérpretes disponibles en su equipo.

![PyCharm2021.3SetupPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/PyCharm2021.3SetupPythonInterpreter.png)

Ejecución en PyCharm usando Python 2.7.5 de ArcGIS for Desktop 10.2.2. 
![Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/Python2.7.5ArcGISDesktop10.2.2PyCharm2021.3.png)

Ejecución en PyCharm usando Python 3.10.0.
![Python3.10.0StandalonePyCharm2021.3.png](https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/Python3.10.0StandalonePyCharm2021.3.png)


### Ejecución desde el Command o CMD de Microsoft Windows

Para ejecutar desde la consola de comandos CMD del sistema operativo Windows usando cualquier versión de Python instalada, usar el comando py, la versión requerida (por ejemplo, -3.10) y la ruta completa del archivo .py.

```C:\py -2.7 D:\R.GISPython\InstallPackageGraph\Tc_v3.py```

```C:\py -3.10 D:\R.GISPython\InstallPackageGraph\Tc_v3.py```

Ejecución en consola CMD Python 2.7.5 de ArcGIS for Desktop 10.2.2. 

> En esta versión, la codificación de texto no imprime correctamente caracteres acentuados del español.

![Python2.7.5ArcGISDesktop10.2.2CMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/Python2.7.5ArcGISDesktop10.2.2CMD.png)

Ejecución en consola CMD Python 3.10.0 Standalone.
![Python3.10.0StandaloneCMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/ErrorExceptionControl/Screenshot/Python3.10.0StandaloneCMD.png)


### Referencias

* https://docs.python.org/3/tutorial/errors.html


### Autores

* Creado por r.cfdtools@gmail.com


### Compatibilidad

* Compatible con cualquier versión de Python.


### Tags
`Concentration time` `Giandotti` `Subbasin` `Hydrology` `Interactive` `define` `while` `matplotlib`


### Control de versiones

| Versión    | Descripción                                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| v.20211201 | Versión inicial con incorporación de librería _sys_ para impresión en pantalla de la versión de Python.                                                            |
| v.20211208 | Inclusión de propiedades de estilo en gráfica de resultados. Inclusión de condicional para la inclusión o no del título de la gráfica, no recomendado en Python 2. |


### Licencia, cláusulas y condiciones de uso
https://github.com/rcfdtools/R.GISPython/wiki/License


| [Actividad anterior](https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScriptFunction) | [Actividad siguiente]() |
|-----------------------------------------------------------------------------------------|-------------------------|
