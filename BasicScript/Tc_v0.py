#-*- coding: UTF-8 -*-
#Microcontenido: Python - Script básico
#Ejemplo: Cálculo del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti
#Créditos: r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.HydroTools/wiki/License
#Ejecución: PyCharm 2020.1, Python 2.7.5 (ArcGIS 10.2.2), Python 3.7.7 (Instalación independiente)

#Variables
A = 9.1348		#Área cuenca, km²
L = 4.6106		#Longitud cauce principal, km
S = 0.144015	#Pendiente media cauce principal, m/m

#Cálculos
TcGiandotti = (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)
print ("Scrit básico en Python.\nCálculo del tiempo de concentración de una cuenca hidrográfica utilizando la expresión de Giandotti.\n")
print("Tc(min):",TcGiandotti*60) #Impresión en pantalla usando coma
print("Tc(min): " + str(TcGiandotti*60)) #Impresión en pantalla usando +
