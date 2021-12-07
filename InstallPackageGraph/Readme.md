## Instalación, actualización de paquetes y creación de gráficas básicas usando matplotlib

Complementariamente a las librerías obtenidas con la instalación de Python, es posible adicionar nuevas librerías que posteriormente podrán ser invocadas desde la consola o desde scripts.

El procedimiento más común de instalación automatizada se realiza a través del comando de consola `pip` disponible en el directorio _Scripts_ de la versión instalada de Python. 

> Dentro de la versión 2.7.5 de Python obtenida con la instalación con ArcGIS for Desktop 10.2.2, no se incorpora esta herramienta, sin embargo, puede ser incorporada manualmente o desde PyCharm.


## Objetivos

* Instalar el paquete o librería matplotlib y actualizar paquetes preinstalados en Python.
* En PyCharm, ejecutar el script usando la versión de Python 2.7 y 3.10.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Graficar diferentes tiempos de concentración Tc variando la pendiente.


¿Qué es matplotlib?

Matplotlib es una librería que permite la graficación 2D de datos en múltiples estilos de visualización, por defecto, esta librería viene incorporada en la instalación de Python en ArcGIS for Desktop, ArcGIS Pro y QGIS 3.

> Para conocer la versión instalada de esta o cualquier librería disponible, en la consola de Python, importar la librería e ingresar la instrucción o etiqueta de versión `libreria.__version__`