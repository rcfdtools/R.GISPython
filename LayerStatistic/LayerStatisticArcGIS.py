# -*- coding: utf-8 -*-
'''***************************************************************************
    Curso: TSIG - Sistemas de Información Geográfica Aplicados
    Microcontenido: HPSD0010 - Python - Estadísticos de una capa geográfica en ArcGIS
    Date                 : Marzo 2020
    Copyright            : Copyleft
    Version inicial por  : karel.sanchez@mail.escuelaing.edu.co
                           luis.sierra-p@mail.escuelaing.edu.co
                           fernando.montejo@mail.escuelaing.edu.co
                           miguel.jimenez-b@mail.escuelaing.edu.co
    Implementación de valores de corte y actualización de código:
                           william.aguilar@escuelaing.edu.co

    Este programa es de libre uso, puede modificarlo a gusto, siempre que
    se mantenga el nombre del autor y la referencia al desarrolo de sistemas
    de información geográfica de la Escuela Colombiana de Ingeniería.

	Descripción:
	- Ejecutado desde el IDE Python de ArcGIS
    - Se asume que la carpeta '/Datos' que contiene el shape 'Precipitación.shp' se encuentra en la misma ruta del script .py
    - Ejecución: ArcGIS for Desktop 10.2.2 con Python 2.7.5
***************************************************************************'''

#Librerias
import arcpy                        #Importación de arcpy para ArcGIS for Desktop.
from arcpy import env               #importación de librería para manejo del entorno de trabajo.
arcpy.env.overwriteOutput = True    #Permitir sobreescribir archivos en directorio del entorno de trabajo.

# Funcion separador
def separador(n=24):
    nc='-'
    print(nc*n)

# Datos
workspaceFolder = r'Datos/'
outputFolder = r'Output/'
arcpy.env.workspace = workspaceFolder
vGISFileInput = 'Precipitacion.shp'
vGISFileSelect = outputFolder+'LayerSelect.shp'
vGISFileaStatistic = outputFolder+'LayerStat.dbf'
vAnalysis = 'TotalAnno' #Atributo para resumen estadístico
vCut = 300

# Ejecución
separador(65)
print('Estadísticos de una capa geográfica en ArcGIS')
separador(65)
print('Archivos de entrada: '+vGISFileInput)
print('Archivos de salida:  '+vGISFileaStatistic)
print('Ejecutando estadistica para ' + vAnalysis + ' >= ' + str(vCut) + '...')
arcpy.Select_analysis(vGISFileInput, vGISFileSelect, vAnalysis+'>='+str(vCut))
arcpy.Statistics_analysis(vGISFileSelect,vGISFileaStatistic,[[vAnalysis,'MIN'],
                                                            [vAnalysis,'MEAN'],
                                                            [vAnalysis,'MAX'],
                                                            [vAnalysis,'STD'],
                                                            [vAnalysis,'RANGE'],
                                                            [vAnalysis,'COUNT']])
print('Proceso compledado.')
print('Visualice tabla de resultados en ArcMap.')

'''
ArcGIS: Summary Statistics (Analysis)
SUM—Adds the total value for the specified field. 
MEAN—Calculates the average for the specified field. 
MIN—Finds the smallest value for all records of the specified field. 
MAX—Finds the largest value for all records of the specified field. 
RANGE—Finds the range of values (MAX minus MIN) for the specified field. 
STD—Finds the standard deviation on values in the specified field.
COUNT—Finds the number of values included in statistical calculations. This counts each value except null values. To determine the number of null values in a field, use the COUNT statistic on the field in question, and a COUNT statistic on a different field which does not contain nulls (for example, the OID if present), then subtract the two values. 
FIRST—Finds the first record in the Input Table and uses its specified field value. 
LAST—Finds the last record in the Input Table and uses its specified field value.'''
