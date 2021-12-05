## Creación de scripts interactivos

Los scripts en Python permiten la entrada directa de datos desde la consola de comandos o desde el intérprete de comandos, para ello puede utilizar el comando `input()`.

> Atención: Actualmente, ArcGIS for Desktop, ArcGIS Pro a través de consola y QGIS no permiten entradas `input()` desde scripts ejecutadas directamente desde el entorno gráfico.<br>
> En QGIS es necesario realizar la entrada desde un cuadro de diálogo, sin embargo, el script puede ser ejecutado desde PyCharm si se encuentra asociado el intérprete de Python asociado a QGIS. Más información en: https://gis.stackexchange.com/questions/53958/how-to-use-raw-input-in-qgis-python-console.<br>
> En ArcGIS Pro, podrá ejecutar scripts interactivos desde la ventana de Python Netbook.


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

### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\InteractiveScript\ 


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.InteractiveScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Script Tc_v1.py

```
# -*- coding: UTF-8 -*-
# Nombre: Tc_v1.py
# Descripción: Script interactivo para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente)

# Librerías
import sys

# Cabecera
print ('-----------------------------')
print ('Script interactivo en Python')
print ('-----------------------------\n')
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables
A = float(input("Área cuenca, km²: "))
L = float(input("Longitud cauce principal, km: "))
S = float(input("Pendiente media cauce principal, m/m: "))

# Cálculos
TcGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ("Tc, min: " + str(TcGiandotti*60)) # Impresión en pantalla usando +
```

### Descripción instrucciones y comandos empleados

| Instrucción             | Explicación                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #                       | Comentario de una línea.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| """<br/>"""             | 3 comillas simples o dobles permiten definir el inicio y fin de comentarios en múltiples líneas.                                                                                                                                                                                                                                                                                                                                                           |
| # -*- coding: UTF-8 -*- | Permite definir la codificación de texto utilizada en el script.                                                                                                                                                                                                                                                                                                                                                                                           |
| import sys              | Importación de librería de systema _sys_.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| sys.version             | Muestra la versión actual de Python desde la que se está ejecutando el script.                                                                                                                                                                                                                                                                                                                                                                             |
| \n                      | Agrega un salto de línea en impresiones en pantalla.                                                                                                                                                                                                                                                                                                                                                                                                       |
| print                   | Permite realizar la impresión de un resultado en la consola. En las versiones de Python 2.x, todo aquello que aparezca después del print será impreso en pantalla, incluso los paréntesis sí existen concatenaciones con comas. En las versiones de Python 3.x, solo se imprimirá aquello que esté entre paréntesis. Nótese que es posible realizar cálculos adicionales en la impresión (TcGiandotti*60) e incluso concatenar resultados usando coma o +. |
| str()                   | Permite convertir una variable o resultado numérico en una cadena de texto. Requerido para concatenación usando +                                                                                                                                                                                                                                                                                                                                          |
| input('mensaje')         | Entrada de usuario por consola.                                                                                                                                                                                                                                                                                                                                                      |
| float()                 | Convierte la entrada de usuario por consola a un valor numérico flotante.|

> En Python, por defecto se asume que la entrada ingresada por consola a través del comando `input()` es una cadena de texto, por tal motivo, cuando se trata de entradas numéricas será necesaria la conversión a tipo flotante. <br>
> Dentro del paréntesis de la entrada `input()`, es necesario ingresar un texto descriptivo que permita al usuario entender el tipo y valor que está ingresando.


### Ejecución desde Pycharm

> PyCharm requiere de configuración previa del intérprete de Python a utilizar en la ejecución del script. Oprima `Ctrl+Alt+S` para acceder a la ventana de configuración y en la pestaña _Project: R.GISPython_ configurar los intérpretes disponibles en su equipo.

![PyCharm2021.3SetupPythonInterpreter.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/PyCharm2021.3SetupPythonInterpreter.png)

Ejecución en PyCharm usando Python 2.7.5 de ArcGIS for Desktop 10.2.2. 
![PyCharm2021.3Python2.7.5ArcGISDesktop10.2.2.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/PyCharm2021.3Python2.7.5ArcGISDesktop10.2.2.png)

Ejecución en PyCharm usando Python 3.10.0.
![PyCharm2021.3Python3.10.0ArcGISDesktop10.2.2.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/PyCharm2021.3Python3.10.0ArcGISDesktop10.2.2.png)

Ejecución en PyCharm usando Python 3.9.5 de QGIS 3.22.1. 
![PyCharm2021.3Python3.10.0ArcGISDesktop10.2.2.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/PyCharm2021.3Python3.10.0ArcGISDesktop10.2.2.png)

Ejecución en PyCharm usando Python 3.7.11 de ArcGIS Pro 2.9. 
![PyCharm2021.3Python3.7.11ArcGISPro2.9.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/PyCharm2021.3Python3.7.11ArcGISPro2.9.png)


### Ejecución usando el IDLE de Python de ArcGIS for Desktop

En el explorador de Windows abrir la carpeta D:\R.GISPython\InteractiveScript y dar clic derecho en Tc_v1.py; seleccionar la opción _Edit With IDLE_. Ejecutar oprimiendo F5. 

> En Windows 11 podrá lanzar manualmente la interfaz gráfica del IDLE buscando la aplicación _IDLE (Python GUI)_.

Script sobre IDLE de Python 2.7.5 en ArcGIS for Desktop.
![Python2.7.5ArcGISDesktop10.2.2IDLE.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/Python2.7.5ArcGISDesktop10.2.2IDLE.png)

> Nota: para lanzar correctamente el IDLE de ArcGIS Desktop, es necesario definir, en variables del sistema operativo Windows, el direccionamiento al directorio C:\Python27.<br>
> Opcionalmente podrá utilizar el IDLE de Python 3.10 que aparece en la lista de programas de Windows luego de su instalación.


### Ejecución desde el Command o CMD de Microsoft Windows

Para ejecutar desde la consola de comandos CMD del sistema operativo Windows usando cualquier versión de Python instalada, usar el comando py, la versión requerida (por ejemplo, -3.10) y la ruta completa del archivo .py.

```C:\py -2.7 D:\R.GISPython\InteractiveScript\Tc_v1.py```

```C:\py -3.10 D:\R.GISPython\InteractiveScript\Tc_v1.py```

Ejecución en consola CMD Python 2.7.5 de ArcGIS for Desktop 10.2.2. En esta versión, la codificación de texto no imprime correctamente caracteres acentuados del español.
![Python2.7.5ArcGISDesktop10.2.2CMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/Python2.7.5ArcGISDesktop10.2.2CMD.png)

Ejecución en consola CMD Python 3.10.0 Standalone.
![Python3.10.0ArcGISDesktop10.2.2CMD.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/Python3.10.0ArcGISDesktop10.2.2CMD.png)


#### Desde Python Window dentro de ArcGIS Pro

#### Desde Jupiter dentro de ArcGIS Pro

En el menú _Analysis_ dar clic en el ícono de opciones de Python y seleccionar Python NoteBook, luego en la celda ingresar el comando `%run -i` y la ruta del script y ejecutar. Opcionalmente en la celda de entrada de comandos podrá copiar y pegar todo el código contenido dentro del script. 

```%run -i D:\R.GISPython\InteractiveScript\Tc_v1.py```

![Python3.7.11ArcGISPro2.9PythonNotebook.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/Python3.7.11ArcGISPro2.9PythonNotebook.png)

![Python3.7.11ArcGISPro2.9PythonNotebookCode.png](https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScript/Screenshot/Python3.7.11ArcGISPro2.9PythonNotebookCode.png)