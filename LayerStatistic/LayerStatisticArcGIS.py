# -*- coding: UTF-8 -*-
# Nombre: LayerStatisticArcGIS.py
# Descripción: Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro
# Requerimiento: PyCharm 2021.3+, ArcGIS 10.2.2, ArcGIS Pro 2.9.0

# Librerías
import arcpy                        # Importación de arcpy de ArcGIS for Desktop.
from arcpy import env               # Importación de librería para manejo del entorno de trabajo.
arcpy.env.overwriteOutput = True    # Permitir sobreescribir archivos en directorio del entorno de trabajo.
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Función para creación de líneas de separación
def Separador(n=24): # Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

# Función para consultar los campos de atributos disponibles
def CapaPropiedades(i):
    cont = 1
    totalEntidades = arcpy.GetCount_management(i)
    descGeometria = arcpy.Describe(i)
    tipoGeometria = descGeometria.shapeType
    tituloCapa = 'Campos en ' + i + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')'
    Separador(len(tituloCapa))
    print(tituloCapa)
    Separador(len(tituloCapa))
    print('  #, Campo, Tipo')
    campos = arcpy.ListFields(i)
    for campo in campos:
        print('  ' + str(cont) + ', ' + campo.name + ', ' + campo.type)  # Print field properties
        cont += 1

# Variables
absolutePath = r'D:/R.GISPython/LayerStatistic' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Datos/'
outputFolder = absolutePath+'/Output/'
layerInput = 'Precipitacion.shp'
layerSelect = outputFolder+'LayerSelect.shp'
layerStatistic = outputFolder+'LayerStat.dbf'
layerStatisticXLS = outputFolder+'LayerStat.xls'
layerStatisticFilter = outputFolder+'LayerStatFilter.dbf'
layerStatisticFilterXLS = outputFolder+'LayerStatFilter.xls'


# Cabecera
Separador(67)
print ('Estadísticos de capas geográficas - ArcGIS for Desktop - ArcGIS Pro')
Separador(67)
print ( 'Compatible con: ArcGIS for Desktop y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__)+
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/LayerStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Ejecución
print(  'Archivos de entrada: '+layerInput+'\n'
        'Archivos de filtrado: '+layerSelect+'\n'
        'Archivos de estadísticos:  '+layerStatistic+'\n'
        'Archivos de estadísticos filtro:  '+layerStatisticFilter+'\n')
CapaPropiedades(layerInput)
print('\n  Antes de continuar, cierre ArcGIS...')
fieldEval = input('  >>> Nombre del campo a evaluar (usar comillas): ')
fieldValue = input('  >>> Mostrar valores >= a: ')
print('\nEjecutando estadística para ' + outputFolder + layerInput + '...')
# Estadísticos compatibles con ArcGIS for Desktop
statisticsType = [[fieldEval,'SUM'],[fieldEval,'MEAN'],[fieldEval,'MIN'],[fieldEval,'MAX'],[fieldEval,'RANGE'],[fieldEval,'STD'],[fieldEval,'COUNT'],[fieldEval,'FIRST'],[fieldEval,'LAST']]
arcpy.Statistics_analysis(layerInput,layerStatistic,statisticsType)
print('Ejecutando estadística para ' + layerSelect + ' con '+ fieldEval + ' >= ' + str(fieldValue) + '...')
arcpy.Select_analysis(layerInput, layerSelect, fieldEval+'>='+str(fieldValue))
arcpy.Statistics_analysis(layerSelect,layerStatisticFilter,statisticsType)
# Conversión a libro de Microsoft Excel
print ('Conversión de estadísticos a XLS file...')
arcpy.TableToExcel_conversion(layerStatistic,layerStatisticXLS)
arcpy.TableToExcel_conversion(layerStatisticFilter,layerStatisticFilterXLS)

# Visualización de resultados usando pandas



print('Proceso completado, visualice la capa filtrada y las tablas de resultados estadísticos en ArcGIS.')
