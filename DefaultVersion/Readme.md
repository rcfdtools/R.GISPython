## Definir la versión por defecto de Python en el OS y configurar PyCharm

Definir una versión por defecto de Python en el CMD de Microsoft Windows, le permitirá lanzar este intérprete desde cualquier directorio de su sistema operativo sin tener que ingresar la ruta completa del ejecutable Python.exe.


### Objetivos

* Establecer una versión de Python como la versión por defecto del OS.
* Configurar él (los) intérprete (s) a usar en PyCharm para la ejecución de scripts.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda. 

> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.


### Versión por defecto en el sistema operativo

1. En Microsoft Windows oprimir `Windows+R` y ejecutar `sysdm.cpl` para ingresar a las propiedades avanzadas del sistema.

![R.GISPython.BasicScript.WindowsOSRunSysdm](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSRunSysdm.png)

2. En la ventana dar clic en la pestaña _Opciones Avanzadas_ y luego en _Variables de Entorno_.

![R.GISPython.BasicScript.WindowsOSSystemProperties](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSSystemProperties.png)

3. En _Variables del sistema_, seleccionar _Path_ y dar clic en _Editar_.

![R.GISPython.BasicScript.WindowsOSEnvironmentVariables](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSEnvironmentVariables.png)

4. Para establecer la versión de Python integrada a ArcGIS (p.ej, Python 2.7.5 sobre ArcGIS 10.2.2 for Desktop), ingresar (utilizando la opción _Nuevo_) o verificar que existan las variables de entorno direccionandas a las rutas _C:\Python27\ArcGIS10.2\Scripts_ y _C:\Python27\ArcGIS10.2_.

![R.GISPython.BasicScript.WindowsOSEnvironmentVariablesEdit](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsOSEnvironmentVariablesEdit.png)

> En caso de que su instalación de ArcGIS for Desktop corresponda a una versión diferente, identifique las rutas de instalación e ingrese o modifique las variables de entorno. Más información en https://github.com/rcfdtools/R.GISPython/tree/main/PythonVersion

> Luego de la modificación de las variables de entorno, en algunas versiones de su sistema operativo, será necesario reiniciar su equipo o cerrar y abrir su sesión de usuario.

5. Para verificar el direccionamiento correcto, abra una nueva ventana de comandos oprimiendo la combinación de teclas `Windows+R` y _CMD_ ó busque el _Command Prompt_ en su lista de programas (no es necesaria la ejecución como Administrador).

![R.GISPython.BasicScript.WindowsCMD](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsCMD.png)

6. En el intérprete de comandos de Windows, ejecute el comando Python. Observará que la versión por defecto es la 2.7.5.

![R.GISPython.BasicScript.WindowsCMDPythonVersion](https://github.com/rcfdtools/R.GISPython/blob/main/DefaultVersion/Screenshot/WindowsCMDPythonVersion.png)

