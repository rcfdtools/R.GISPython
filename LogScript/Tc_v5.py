# -*- coding: UTF-8 -*-
# Nombre: Tc_v4.py
# Descripción: Script interactivo e iterativo para el cálculo y graficación del tiempo de concentración con control de excepción de errores y archivo de registro log.
# Requerimiento: PyCharm 2020.1+, Python 2.7.5 (ArcGIS 10.2.2), Python 3.10.0 (instalación independiente).

# Librerías
import sys
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

# Variables internas y archivo log de resultados
i, variaciones, pendienteMinima = 0, 12, 0.001 # Incremento, variaciones y pendiente mínima
fileLog = open('TC_v5Log.txt','w+') # w+ para crear el archivo si no existe

# Función de cálculo
def TcGiandotti(A,L,S):
    return (4*(A**0.5)+1.5*L)/(25.3*(S*L)**0.5)

# Función para creación de líneas de separación
def Separador(n, enLog): #Usando un valor por defecto de 24 guiones
    nc = "-"
    print(nc*n)
    if enLog == True:
        fileLog.write(nc*n + '\n')

# Función de impresión en pantalla y log de resultados
def PrintLog(txtPrint, enPantalla):
    if enPantalla == True:
        print(txtPrint)
    fileLog.write(txtPrint + '\n')

# Cabecera
Separador(90)
print ('Script interactivo e iterativo en Python con graficación, control de excepción de errores y archivo log de resultados')
Separador(90)
print ('Cálculo y graficación del Tiempo de Concentración de una cuenca hidrográfica usando la expresión de Giandotti.')
print ('Python versión: ' + str(sys.version))
print ('matplotlib versión: ' + str(matplotlib.__version__))
print ('Encuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/ErrorExceptionControl')
print ('Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License')
print ('Créditos: r.cfdtools@gmail.com\n')


# Procedimiento
PrintLog('ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO\n'
         'CURSO TALLER DE SISTEMAS DE INFORMACIÓN GEOGRÁFICA - TSIG\n'
         'CALCULO DEL TIEMPO DE CONCENTRACIÓN USANDO LA EXPRESIÓN DE GIANDOTTI\n'
         'Ejecutado en: '+str(datetime.now())+'\n', True)
Separador(44, True)
PrintLog("Datos de entrada", True)
Separador(44, True)
try:
    ATxt, LTxt, STxt = "A, Área cuenca, km²: ", "L, Longitud cauce principal, km: ", "S, Pendiente media cauce principal, m/m: "
    A = float(input(ATxt))
    PrintLog(ATxt + str(A), False)
    L = float(input(LTxt))
    PrintLog(LTxt + str(L), False)
    S = float(input(STxt))
    PrintLog(STxt + str(S), False)
    if A > 0 and L > 0 and S > 0:
        #Calculos
        PrintLog("Valores ingresados son válidos...", True)
        PrintLog("Tc, Tiempo de Concentración, min: " + str(round(TcGiandotti(A,L,S)*60,4)), True) #Impresión en pantalla usando +
        Separador(44, True)
        PrintLog("RESULTADOS VARIANDO LA PENDIENTE", True)
        Separador(44, True)
        PrintLog("i\tS (m/m)\tTc (min)", True)
        TcGiandottiGx, TcGiandottiGy = [], [] #Listas para graficación de datos
        while i < variaciones:
            Svar =  (((S-pendienteMinima)/(variaciones-1))*i+pendienteMinima)
            #print(i+1, "\t", round(Svar,4), "\t", round(TcGiandotti(A,L,Svar)*60,4)) #Concatenación con coma
            PrintLog(str(i+1)+"\t"+str(round(Svar,4))+"\t"+str(round(TcGiandotti(A,L,Svar)*60,4)), True) #Concatenación con +
            TcGiandottiGx.append(Svar)
            TcGiandottiGy.append(TcGiandotti(A,L,Svar)*60)
            i += 1

        #Graficación de datos sin registro en Log de resultados
        Separador(44, True)
        PrintLog("GRAFICACIÓN DE DATOS", True)
        Separador(44, True)
        PrintLog("S (m/m): " + str(TcGiandottiGx), True)
        PrintLog("Tc (min): " + str(TcGiandottiGy), True)
        plt.plot(TcGiandottiGx,TcGiandottiGy, label="Tc Giandotti (min)")
        plt.title("TIEMPO DE CONCENTRACIÓN\nVariando la pendiente cada "+str(round(((S-pendienteMinima)/(variaciones-1)),4))+" m/m\nA (km²): "+str(A)+", L (km): "+str(L))
        plt.xlabel("S (m/m)")
        plt.ylabel("Tc (min)")
        plt.show()
    else:
        print(">>>Error: Ningún valor puede ser menor o igual a cero.")
except ValueError as e:
    print(">>>Error: Dato ingresado no numérico...")

''' 
Referencias
https://www.programiz.com/python-programming/datetime/current-datetime
'''