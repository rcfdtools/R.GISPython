#-*- coding: UTF-8 -*-
#Curso: TSIG - Sistemas de Información Geográfica Aplicados
#Microcontenido: HPSD0010 - Python - Estadísticos de una capa geográfica con comparación por filtrado en QGIS
#Créditos: william.aguilar@escuelaing.edu.co, r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://pruebacorreoescuelaingeduco.sharepoint.com/sites/TSIG626
#Ejecución: QGIS 3.12, Python 3.7

PYTHONPATH = r"C:\Program Files\QGIS 3.12\apps\Python37\python"

#Importación de módulos
from qgis.core import *
import qgis.utils
#qgs = QgsApplication([], False)

#Función para creación de líneas de separación
def Separador(n = 24): #Usando un valor por defecto de 24 guiones
	nc = "-"
	print(nc*n)

# Definicion de rutas, archivos y variables generales
vMainPathIn = r"D:/OneDrive - ESCUELA COLOMBIANA DE INGENIERIA/ECI_Class_Sourcecode/HPSD/HPSD0010/Datos/" #Ruta de datos de entrada
vGISFileInput = vMainPathIn+"Precipitacion.shp"
vAnalysis = "TotalAnno" #Variable para filtrado
vCut = 300 #Variable de corte para seleccion

# Ejecución de procesos geograficos
Separador(66)
print("Estadísticos de una capa geográfica con comparación por filtrado en QGIS")
Separador(66)
print("Archivo GIS de entrada: "+vGISFileInput)
#vLayerInput = iface.addVectorLayer(vGISFileInput,'','ogr') #Cargar en mapa QGIS
vLayerInput = QgsVectorLayer(vGISFileInput,'','ogr') #Sin cargar en mapa QGIS
print("\nCampos disponibles en la capa:",end=" ")
for field in vLayerInput.fields():
    print(field.name(), end = ', ')
vFCount = vLayerInput.featureCount()
print('\n\n# Entidades:', vFCount)
print('\nLayer Id:', vLayerInput.id())
print("\nEjecutando estadisticas...")
print("\nEjemplo de datos...")
Separador(36)
print('Estacion\t Total Anual')
Separador(36)
vTotalAnnProm = 0
vTotalAnnPromSelect = 0
vFCountSel = 0
for i in range(0, vFCount):
    vFeature = vLayerInput.getFeature(i)
    #print(vFeature[0])
    if i < 10:
        print(vFeature['ESTACIONID'],'\t',round(vFeature[vAnalysis],3))
    vTotalAnnProm = vTotalAnnProm + vFeature['TotalAnno']
    if vFeature['TotalAnno'] > vCut:
        vFCountSel += 1
        vTotalAnnPromSelect = vTotalAnnPromSelect + vFeature[vAnalysis]
Separador(36)
print("Promedio\t",vTotalAnnProm / vFCount)
print("Promedio >",vCut,"\t",vTotalAnnPromSelect / vFCountSel)
Separador(36)

#Visualizar la propiedades de una capa seleccionada en el proyecto actual
#Requiere una capa cargada y seleccionada en QGIS
'''
layer = qgis.utils.iface.activeLayer()
print(layer.id())
print(layer.featureCount())
'''
