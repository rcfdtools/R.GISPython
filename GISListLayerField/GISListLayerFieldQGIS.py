#-*- coding: UTF-8 -*-
#Curso: TSIG - Sistemas de Información Geográfica Aplicados
#Microcontenido: HPSD0007 - Python - Cargar capas Vectoriales, consultar sus propiedades y atributos en QGIS
#Créditos: william.aguilar@escuelaing.edu.co, r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://pruebacorreoescuelaingeduco.sharepoint.com/sites/TSIG626
#Ejecución: QGIS 3.10 con Python 3.7.0
#Consultar todas las capas cargadas en el proyecto actual, ver sus atributos y tipos.
#Permite consultar las propiedades de una capa específica y definir dos campos para su graficación.
#https://gis.stackexchange.com/questions/118862/getting-list-of-layer-names-using-pyqgis
#https://gis.stackexchange.com/questions/312153/how-to-test-the-geometry-type-from-a-list-of-layers-and-then-join-it-with-pyqgis

#Importación de módulos
from qgis.core import *
import qgis.utils
from qgis.core import QgsProject
import matplotlib.pyplot as plt

#Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

#Mostrar la lista de capas disponibles
Separador(30)
print('Listado de capas disponibles')
Separador(30)
FeatureList = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
Cont = 1
for i in FeatureList:
    print(' ',Cont, i)
    Cont += 1

#Mostrar la lista de atributos por cada capa disponible
#layer = iface.activeLayer()
for layer in QgsProject.instance().mapLayers().values():
    TotalEntidades = layer.featureCount()
    #Tipo de geometría
    #https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/geometry.html
    GeomTipo = ''
    if layer.wkbType() == QgsWkbTypes.Point:
        GeomTipo = 'G' + str(layer.wkbType()) + ' Puntos'
    elif layer.wkbType() == QgsWkbTypes.LineString:
        GeomTipo = 'G' + str(layer.wkbType()) + ' Lineas'
    elif layer.wkbType() == QgsWkbTypes.Polygon:
        GeomTipo = 'G' + str(layer.wkbType()) + ' Poligonos'
    elif layer.wkbType() == QgsWkbTypes.MultiPolygon:
        GeomTipo = 'G' + str(layer.wkbType()) + ' Multi-poligonos'
    else:
        GeomTipo = str(layer.wkbType())
    Separador(48)
    print("Campos en", layer.name(), '(' + GeomTipo + ' ' + str(TotalEntidades) + ')')
    Separador(48)
    Cont = 1
    for field in layer.fields():
        print('  ' + str(Cont) + ', '+ field.name() + ', ' + field.typeName())
        Cont += 1

#Mostrar valores encontrados
MainPathIn = r'C:/TSIG/Taller1/Datos/' #Ruta de datos de entrada
GISFileInput = MainPathIn+"Precipitacion.shp"
CampoRotulo = 'ESTACIONID'
CampoEvaluar = 'TotalAnno'
CampoFiltro = 4500
#LayerInput = iface.addVectorLayer(GISFileInput,'','ogr') #Cargar en mapa QGIS
LayerInput = QgsVectorLayer(GISFileInput,'','ogr') #Sin cargar en mapa QGIS
FCount = LayerInput.featureCount()
print('\nCapa a evaluar:', GISFileInput)
print('Campo para rotulación:', CampoRotulo)
print('Campo a evaluar:', CampoEvaluar)
print('Mostrar valores >= a:', CampoFiltro,'\n')
ListaCampoRotulo, ListaCampoEvaluar = [], []
Separador(38)
print('Lista de valores encontrados >=',CampoFiltro)
Separador(38)
print('  ' + CampoRotulo + ', ' + CampoEvaluar)
Cont = 0
for i in range(0, FCount):
    Feature = LayerInput.getFeature(i)
    if Feature[CampoEvaluar] >= CampoFiltro:
        #ListaCampoRotulo.append(int(Feature[CampoRotulo]))
        ListaCampoRotulo.append(Cont)
        ListaCampoEvaluar.append(Feature[CampoEvaluar])
        print('  ' + str(Feature[CampoRotulo]) + ', ' + str(Feature[CampoEvaluar]))
        Cont += 1
print('  (' + str(Cont) + ' registros)')
# Graficación de datos
Separador(30)
print('Graficación de datos')
Separador(30)
plt.bar(ListaCampoRotulo, ListaCampoEvaluar, color = 'darkGray')
plt.style.use('fast') #https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html
plt.title('VALORES ENCONTRADOS')
plt.xlabel(CampoRotulo)
plt.ylabel(CampoEvaluar)
plt.show()