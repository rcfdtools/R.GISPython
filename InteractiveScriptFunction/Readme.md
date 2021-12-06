## Creación de scripts interactivos e iterativos con funciones

Python dispone de múltiples estructuras para la ejecución de procesos iterativos, como el while, for y range.

Para el ejemplo de estimación del tiempo de concentración, además de permitir la entrada de datos del usuario, calcular la variación del tiempo obtenido, cambiando la pendiente desde un valor bajo (p.ej, 0.001 m/m) hasta la pendiente ingresada por el usuario y para un determinado número de variaciones (p.ej, 24).

> Para conocer la compatibilidad de entradas por consola en ArcGIS y QGIS utilizando el comando `input()`, consultar la actividad anterior relacionada con la [creación de scripts interactivos](https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScript).

### Objetivos

* En PyCharm, ejecutar el script usando la versión de Python 3.7.
* Ejecutar el script desde la consola del sistema operativo o CMD.
* Solicitar al usuario los valores de entrada de los parámetros requeridos.
* Imprimir diferentes valores del Tc en función del cambio gradual de la pendiente media del cauce principal.
* Ingresar valores errados como valores con unidades o cadenas de texto en los datos de entrada para así observar el volcamiento del script. Esto le permitirá entender por qué es necesario implementar control de excepción de errores en futuros scripts.


### Requerimientos

* Python 2.7.5 de ArcGIS for Desktop 10.2.2.
* Python 3.10.0+ como instalación independiente o standalone.
* PyCharm 2021.3+ for Anaconda.


> Nota: en caso de no disponer de ArcGIS en su equipo, puede realizar las pruebas de funcionamiento realizando la instalación independiente de la versión 2.7.17 de Python.


### Ruta de ejecución
 
Para el desarrollo de este ejercicio se recomienda que los scripts y demás archivos requeridos se encuentren en D:\R.GISPython\InteractiveScriptFunction\ 


### Caso de estudio

Tiempo de concentración en una cuenca hidrográfica: el tiempo de concentración tc, es el tiempo que tarda una gota de agua que cae en una cuenca desde el punto más lejano hasta su punto de salida. Para este ejemplo utilizaremos la expresión de Giandotti.

<br>
<div  align="center">
    <img align="center"  alt="R.GISPython.InteractiveScript.TcGiangotti" src="https://github.com/rcfdtools/R.GISPython/blob/main/InteractiveScriptFunction/Screenshot/TcGiangotti.png" width="240px"/>
</div>


#### Parámetros

* tc, tiempo de concentración en horas.
* A, área de la cuenca = 9.1348 km².
* L, longitud del cauce principal = 4.6106 km.
* S, pendiente media del cauce principal = 0.144015 m/m


### Script Tc_v2.py

```
# -*- coding: UTF-8 -*-
# Nombre: Tc_v2.py
# Descripción: Script interactivo e iterativo para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys

# Variables
i, variaciones, Smin = 0, 12, 0.001 # Incremento, variaciones y pendiente mínima

# Función de cálculo
def TcGiandotti(A,L,S):
	return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
	nc = '—'
	print(nc*n)

# Función para crear tablas basadas en textos
def fTablaTexto(var, ancho): # Variable a formatear, ancho de columna.
    return (' ' *  (ancho-len(str(var))))

# Cabecera
Separador(40)
print ('Script interactivo e iterativo en Python')
Separador(40)
print ('Cálculo del tiempo de concentración Tc de una cuenca hidrográfica utilizando la expresión de Giandotti con pendiente variable.')
print ('Python versión: ' + str(sys.version))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/InteractiveScriptFunction')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')

# Variables
Separador(18)
print('Datos de entrada')
Separador(18)
A = float(input('Área cuenca, km²: '))
L = float(input('Longitud cauce principal, km: '))
S = float(input('Pendiente media cauce principal, m/m: '))
tipoImpresion = input('Imprimir con formato de tabla de texto Python 3 (y/n), Python 2 y 3 ("y"/"n"): ')

# Cálculos
if str(tipoImpresion.lower()) == 'n':
    print('\nTc, min: ' + str(TcGiandotti(A,L,S)*60)) # Impresión en pantalla usando +
    print('\nResultados variando la pendiente y utilizando columnas tabuladas')
    Separador()
    print('i\tS, m/m\tTc, min')
    Separador()
    while i < variaciones:
        Svar =  (((S-Smin)/(variaciones-1))*i+Smin)
        #print(i+1, '\t', round(Svar,4), '\t', round(TcGiandotti(A,L,Svar)*60,4)) #Concatenación con coma
        print(str(i+1)+'\t'+str(round(Svar,4))+'\t'+str(round(TcGiandotti(A,L,Svar)*60,4))) #Concatenación con +
        i += 1
else:
    print('\nTc, min: ' + str(TcGiandotti(A,L,S)*60)) #Impresión en pantalla usando +
    print('\nResultados variando la pendiente y con formato de tabla de texto')
    vColumnaAncho = 10 # Para impresión con concatenación usando coma, al ancho total por columna se le resta 3 debido a que por cada concatenación con comas se agrega un espacio.
    vColumnas = 3
    vFilaAncho = vColumnaAncho*vColumnas+4 # Para impresión con concatenación usando coma, sumar vColumnas*3
    Separador(vFilaAncho)
    # print('|', 'i', fTablaTexto("i", vColumnaAncho), '|', 'S, m/m', fTablaTexto('S, m/m', vColumnaAncho), '|', 'Tc, min', fTablaTexto('Tc, min', vColumnaAncho), '|')  # Python 3
    print('|' + 'i' + fTablaTexto("i",vColumnaAncho) + '|' + 'S, m/m' + fTablaTexto('S, m/m',vColumnaAncho) + '|' + 'Tc, min' + fTablaTexto('Tc, min',vColumnaAncho) + '|') # Python 2
    Separador(vFilaAncho)
    i=0
    while i < variaciones:
        Svar =  (((S-Smin)/(variaciones-1))*i+Smin)
        # print('|', i + 1, fTablaTexto((i + 1), vColumnaAncho), '|', round(Svar, 4), fTablaTexto(round(Svar, 4), vColumnaAncho), '|', round(TcGiandotti(A, L, Svar) * 60, 4), fTablaTexto(round(TcGiandotti(A, L, Svar) * 60, 4), vColumnaAncho), '|')
        print('|' + str(i + 1) + (fTablaTexto((i + 1), vColumnaAncho)) + '|' + str(round(Svar, 4)) + (fTablaTexto(round(Svar, 4), vColumnaAncho)) + '|' + str(round(TcGiandotti(A, L, Svar) * 60, 4)) + (fTablaTexto(round(TcGiandotti(A, L, Svar) * 60, 4), vColumnaAncho)) + '|')
        i += 1
    Separador(vFilaAncho)
```