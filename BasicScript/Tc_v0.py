# -*- coding: UTF-8 -*-
# Nombre: Tc_v0.py
# Descripción: Script básico para el cálculo del tiempo de concentración
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente)

#Librerías
import sys

#Nombre
print ('------------------------')
print ('Script básico en Python')
print ('------------------------\n')
print ('Cálculo del tiempo de concentración de una cuenca hidrográfica utilizando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com')

#Variables
A = 9.1348		#Área cuenca, km²
L = 4.6106		#Longitud cauce principal, km
S = 0.144015	#Pendiente media cauce principal, m/m

#Cálculos e impresión
TcGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ('\nParámetros de entrada')
print ('\tÁrea cuenca, km²: ' + str(A))
print ('\tLongitud cauce principal, km: ' + str(L))
print ('\tPendiente media cauce principal, m/m: ' + str(S))
print ('\nResultados')
print ('Tc(min):',TcGiandotti*60) #Impresión en pantalla usando coma, no compatible con Python 2. Coma agrega espacio.
print ('Tc(min): ' + str(TcGiandotti*60)) #Impresión en pantalla usando +, compatible con cualquier versión de Python. + requiere de ingreso manual de espacio.
