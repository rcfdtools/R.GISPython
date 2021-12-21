#-*- coding: UTF-8 -*-
#Curso: TSIG - Sistemas de Información Geográfica Aplicados
#Microcontenido: HPSD0010 - Python - Estadísticos de una capa geográfica con comparación por filtrado en ArcGIS
#Créditos: william.aguilar@escuelaing.edu.co, r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://pruebacorreoescuelaingeduco.sharepoint.com/sites/TSIG626
#Ejecución: PyCharm 2020.1, Python 2.7.5 (ArcGIS 10.2.2)

# Importación de módulos
import arcpy
from arcpy import env               #importación de librería para manejo del entorno de trabajo.
arcpy.env.overwriteOutput = True    #Permitir sobreescribir archivos en directorio del entorno de trabajo.

# Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

# Definicion de rutas, archivos y variables generales
vMainPathIn = r"Datos/" #Ruta de datos de entrada
arcpy.env.workspace = vMainPathIn #Usar r para evitar salto de línea en directorios que empiezan por la letra n.
vMainPathOut = r"Output/" #Ruta de datos de salida
vGISFileInput = vMainPathIn+"Precipitacion.shp"
vGISFileOutput = vMainPathOut+"PrecipitacionSelect.shp"
vGISFileInputStat = vMainPathOut+"PrecipitacionStatInput.dbf"
vGISFileOutputStat = vMainPathOut+"PrecipitacionStatOutput.dbf"
vAnalysis = "TotalAnno" #Variable para filtrado
vCut = 300 #Variable de corte para seleccion

# Ejecución de procesos geograficos
Separador(80)
print("Estadísticos de una capa geográfica con comparación por filtrado en ArcGIS")
Separador(80)
print("Archivo GIS de entrada: "+vGISFileInput)
print("Archivo GIS de salida: "+vGISFileOutput)
print("Ejecutando estadistica en archivo original...")
arcpy.Statistics_analysis(vGISFileInput, vGISFileInputStat, [[vAnalysis, "MEAN"]], "")
print("Ejecutando seleccion...")
arcpy.Select_analysis(vGISFileInput, vGISFileOutput, vAnalysis+">="+str(vCut))
print("Ejecutando estadistica en archivo filtrado...")
arcpy.Statistics_analysis(vGISFileOutput, vGISFileOutputStat, [[vAnalysis, "MEAN"]], "")
print("Estaditica de entrada: "+vGISFileInputStat)
print("Estadistica de salida: "+vGISFileOutputStat)
print("Proceso completado. Visualice los resultados obtenidos en ArcMap...")
