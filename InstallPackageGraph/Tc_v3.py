#-*- coding: UTF-8 -*-
#Curso: TSIG - Sistemas de Información Geográfica Aplicados
#Microcontenido: HPSD0004 - Python - Instalación de librerías - Gráficas usando matplotlib
#Ejemplo: Cálculo del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti
#Créditos: william.aguilar@escuelaing.edu.co, r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://pruebacorreoescuelaingeduco.sharepoint.com/sites/TSIG626
#Ejecución: PyCharm 2020.1, Python 2.7.5 (ArcGIS 10.2.2), Python 3.7.7 (Instalación independiente)

print("Cálculo del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti")

#Importación de librerias
import matplotlib.pyplot as plt

#Variables internas
i, variaciones, Smin = 0, 24, 0.001 #Incremento, variaciones y pendiente mínima

#Función de cálculo
def TcGiandotti(A,L,S):
	return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

#Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

#Variables de entrada
Separador(18)
print("Datos de entrada")
Separador(18)
A = float(input("Área cuenca, km²: "))
L = float(input("Longitud cauce principal, km: "))
S = float(input("Pendiente media cauce principal, m/m: "))

#Calculos
print("\nTc(min): " + str(TcGiandotti(A,L,S)*60)) #Impresión en pantalla usando +
print("\nResultados variando la pendiente")
Separador()
print("i\tS (m/m)\tTc (min)")
Separador()
TcGiandottiGx, TcGiandottiGy = [], [] #Listas para graficación de datos
while i < variaciones:
	Svar =  (((S-Smin)/(variaciones-1))*i+Smin)
	#print(i+1, "\t", round(Svar,4), "\t", round(TcGiandotti(A,L,Svar)*60,4)) #Concatenación con coma
	print(str(i+1)+"\t"+str(round(Svar,4))+"\t"+str(round(TcGiandotti(A,L,Svar)*60,4))) #Concatenación con +
	TcGiandottiGx.append(Svar)
	TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)
	i += 1

#Graficación de datos
Separador()
print("Graficación de Datos")
Separador()
print("S (m/m)\n",TcGiandottiGx)
print("Tc (min)\n",TcGiandottiGy)
plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti (min)")
plt.title("TIEMPO DE CONCENTRACIÓN\nVariando la pendiente cada "+str(round(((S-Smin)/(variaciones-1)),4))+" m/m\nA (km²): "+str(A)+", L (km): "+str(L))
plt.xlabel("S (m/m)")
plt.ylabel("Tc (min)")
plt.show()