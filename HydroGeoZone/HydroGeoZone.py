# -*- coding: UTF-8 -*-

# Librerías
import arcpy
from arcpy import env
import sys
import matplotlib
import matplotlib.pyplot as plt

def TitleSeparator(titleText,titleType='Both'):
    # titleType: Top, Bottom, Both
    nc='-'
    nVal=len(titleText)
    if titleType == 'Both':
        print(nc*nVal)
        print(titleText)
        print(nc * nVal)
    elif  titleType == 'Top':
        print(nc*nVal)
        print(titleText)
    else:
        print(titleText)
        print(nc*nVal)

# Función para consultar los campos de atributos disponibles
def CapaPropiedades(i):
    cont = 1
    totalEntidades = arcpy.GetCount_management(i)
    descGeometria = arcpy.Describe(i)
    tipoGeometria = descGeometria.shapeType
    tituloCapa = 'Campos en ' + i + ' (' + tipoGeometria + 's ' + str(totalEntidades) + ')'
    TitleSeparator(tituloCapa)
    print('  #, Campo, Tipo')
    campos = arcpy.ListFields(i)
    for campo in campos:
        print('  ' + str(cont) + ', ' + campo.name + ', ' + campo.type)  # Print field properties
        cont += 1

# Datos
absolutePath = r'D:/R.GISPython/HydroGeoZone' # Usar r'.' para retornar a ruta relativa
arcpy.env.workspace = absolutePath+'/Data/'
arcpy.env.overwriteOutput = True
dataPath = absolutePath+'/Data/'
outputPath = absolutePath+'/Output/'
hydroSubZoneLayer = dataPath+'Zonificacion_hidrografica_2013.shp'    # Capa que será utilizada como máscara de selección
drainageLayer = dataPath+'Drenaje_Sencillo.shp' # Capa con entidades que se seleccionaran
hydroAreaLayer = outputPath+'AreaHidrografica.shp'
hydroZoneLayer = outputPath+'ZonaHidrografica.shp'
hydroSubZoneLayerProject = outputPath+'SubZonaHidrograficaProject.shp'
hydroSubZoneLayerCopy = outputPath+'SubZonaHidrografica.shp'
drainageLayerIntersect = outputPath+'DrenajeSencilloIntersect.shp'
#statisticsTableDBF = outputPath+'Estadistica.dbf'
statisticsTableAHDBF = outputPath+'AreaHidrograficaEstadistica.dbf'
statisticsTableZHDBF = outputPath+'ZonaHidrograficaEstadistica.dbf'
statisticsTableSZHDBF = outputPath+'SubZonaHidrograficaEstadistica.dbf'
statisticsTableAHXLS = outputPath+'AreaHidrograficaEstadistica.xls'
statisticsTableZHXLS = outputPath+'ZonaHidrograficaEstadistica.xls'
statisticsTableSZHXLS = outputPath+'SubZonaHidrograficaEstadistica.xls
fieldAHCode, fieldZHCode, fieldSZHCode= 'COD_AH', 'COD_ZH', 'COD_SZH'
fieldAHName, fieldZHName, fieldSZHName= 'NOM_AH', 'NOM_ZH', 'NOM_SZH'
outCoordinateSystem = "PROJCS['MAGNA-SIRGAS / Origen-Nacional',GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',5000000.0],PARAMETER['False_Northing',2000000.0],PARAMETER['Central_Meridian',-73.0],PARAMETER['Scale_Factor',0.9992],PARAMETER['Latitude_Of_Origin',4.0],UNIT['Meter',1.0]] # GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
intersectActive = False # Volver a realizar la intersección espacial y calcular las longitudes de los drenajes intersecados.

# Cabecera
TitleSeparator('Zonificación hidrográfica de Colombia - Análisis de forma y densidad usando Python')
print ( 'Compatible con: ArcGIS for Desktop 10.6+ y ArcGIS Pro'
        '\nPython versión: ' + str(sys.version)+
        '\nPython rutas: ' + str(sys.path[0:5])+
        '\nmatplotlib versión: ' + str(matplotlib.__version__) +
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')
print('Antes de iniciar cierre las aplicaciones de ArcGIS for Desktop...\n')


print('Propiedades encontradas para las capas de entrada:')
CapaPropiedades(drainageLayer)
CapaPropiedades(hydroSubZoneLayer)
print('\n')

# Procesos y cálculos
TitleSeparator('Reproyección de subzonas','Both')
#print('Copiando SZH - subzonas hidrográficas: '+hydroZoneLayer)
#arcpy.Select_analysis(hydroSubZoneLayer, hydroSubZoneLayerCopy, '')
print('Reproyectando SZH a '+hydroSubZoneLayerProject+'...')
print('Sistema de coordenadas: '+outCoordinateSystem)
arcpy.Project_management(hydroSubZoneLayer, hydroSubZoneLayerProject, outCoordinateSystem)
print('\n')

TitleSeparator('Disolución de subzona, zona y área hidrográfica','Both')
print('La capa de subzonas hidrográficas contiene polígonos con el mismo código y en entidades separadas por lo que se requiere su conversión a multiparte.')
print('Disolviendo a multiparte SZH - subzonas hidrográfica '+hydroSubZoneLayerCopy+'...')
arcpy.Dissolve_management(hydroSubZoneLayerProject, hydroSubZoneLayerCopy, fieldSZHCode, '','MULTI_PART', '')
print('Incorporando atributos a capa disuelta SZH - subzona hidrográfica ' + hydroSubZoneLayerCopy+'...')
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', hydroSubZoneLayerProject, 'COD_SZH') # Siempre se ejecuta antes de las demás disoluciones
print('Disolviendo a multiparte AH - áreas hidrográficas '+hydroAreaLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroAreaLayer, fieldAHCode, '','MULTI_PART', '')
print('Disolviendo a multiparte ZH - zonas hidrográficas '+hydroZoneLayer+'...')
arcpy.Dissolve_management(hydroSubZoneLayerCopy, hydroZoneLayer, fieldZHCode, '','MULTI_PART', '')
print('\n')

TitleSeparator('Inclusión de campos para cálculo de áreas, perímetros, longitudes, forma y densidad','Both')
print('Agregando campo area (Area) en km²')
print('Agregando campo perimetro (Perm) en km')
print('\tAH - áreas hidrográficas...')
arcpy.AddField_management(hydroAreaLayer, 'Area', 'Double')
arcpy.AddField_management(hydroAreaLayer, 'Perm', 'Double')
print('\tZH - zonas hidrográficas...')
arcpy.AddField_management(hydroZoneLayer, 'Area', 'Double')
arcpy.AddField_management(hydroZoneLayer, 'Perm', 'Double')
print('\tSZH - subzonas hidrográficas...')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Area', 'Double')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Perm', 'Double')
print('Agregando Kc - Coeficiente de Compacidad')
print('Agregando Dd - Densidad de Drenaje km/km²')
print('Agregando Dc - Densidad de corrientes 1/Km²')
print('\tAH - áreas hidrográficas...')
arcpy.AddField_management(hydroAreaLayer, 'Kc', 'Double')
arcpy.AddField_management(hydroAreaLayer, 'Dd', 'Double')
arcpy.AddField_management(hydroAreaLayer, 'Dc', 'Double')
print('\tZH - zonas hidrográficas...')
arcpy.AddField_management(hydroZoneLayer, 'Kc', 'Double')
arcpy.AddField_management(hydroZoneLayer, 'Dd', 'Double')
arcpy.AddField_management(hydroZoneLayer, 'Dc', 'Double')
print('\tSZH - subzonas hidrográficas...')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Kc', 'Double')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Dd', 'Double')
arcpy.AddField_management(hydroSubZoneLayerCopy, 'Dc', 'Double')

print('\n')

TitleSeparator('Cálculo de áreas y perímetros','Both')
print('Compatible con ArcGIS for Desktop 10.6+ y ArcGIS Pro.')
print('Calculando area (Area) en km² y perimetro (Perm) en km')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroAreaLayer,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroZoneLayer,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateGeometryAttributes_management(hydroSubZoneLayerCopy,[['Area','AREA'],['Perm','PERIMETER_LENGTH']],'KILOMETERS','SQUARE_KILOMETERS')
print('\n')

TitleSeparator('Intersección de drenajes con subzonas hidrográficas y cálculo de longitud por segmento','Both')
print('Tenga en cuenta que la definición de las subzonas hidrográficas se realizó a escala 1:500k y los drenajes a escala 1:100k, por lo que espacialmente pueden existir fragmentos de tramos de drenaje que cruzan entre zonas. Los cálculos de densidad y forma se realizan a partir de la intersección espacial fraccionada de drenajes dentro de cada área teniendo en cuenta la consideración anterior.')
if intersectActive == True:
    print('Intersecando drenajes con subzonas ' + drainageLayerIntersect+'...')
    print('Este proceso tardara varios minutos...')
    arcpy.Intersect_analysis([hydroSubZoneLayerCopy,drainageLayer],drainageLayerIntersect,'ALL','','LINE')
    print('Intersección completada...')
    print('Agregando campo longitud (LDre) en km a drenajes intersecados...')
    arcpy.AddField_management(drainageLayer, 'LDre', 'Double')
    print('Calculando longitud (LDre) en km de cada segmento de drenaje intersecado...')
    print('Este proceso tardara varios minutos...')
    arcpy.CalculateGeometryAttributes_management(drainageLayerIntersect, [['LDre', 'LENGTH']], 'KILOMETERS')
    print('Calculo de longitudes completado...')
else:
    print('Intersección de drenajes desactivada...')
print('\n')

TitleSeparator('Estadísticos de análisis','Both')
print('Generando estadísticos en DBF')
print('\tAH - área hidrográfica ' + statisticsTableAHDBF)
arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableAHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName])
print('\tZH - zona hidrográfica ' + statisticsTableZHDBF)
arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableZHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName])
print('\tSZH - subzona hidrográfica ' + statisticsTableSZHDBF)
arcpy.Statistics_analysis(drainageLayerIntersect, statisticsTableSZHDBF, [['LDre','SUM']], [fieldAHCode, fieldAHName, fieldZHCode, fieldZHName, fieldSZHCode, fieldSZHName])
print('\n')

TitleSeparator('Unión de capas geográficas y estadísticos')
print('Tenga en cuenta que en algunas subzonas hidrográficas pueden no existir drenajes restituidos.')
print('Uniendo capa con estadísticos ' + hydroAreaLayer)
print('\tAH - área hidrográfica ' + hydroAreaLayer)
arcpy.JoinField_management(hydroAreaLayer, 'COD_AH', statisticsTableAHDBF, 'COD_AH')
print('\tZH - zona hidrográfica ' + hydroZoneLayer)
arcpy.JoinField_management(hydroZoneLayer, 'COD_ZH', statisticsTableZHDBF, 'COD_ZH')
print('\tSZH - subzona hidrográfica ' + hydroSubZoneLayerCopy)
arcpy.JoinField_management(hydroSubZoneLayerCopy, 'COD_SZH', statisticsTableSZHDBF, 'COD_SZH')
print('\n')

TitleSeparator('Análisis de forma y densidad', 'Both')
print('Calculando Kc - Coeficiente de Compacidad, Dd - Densidad de Drenaje km/km² y Dc - Densidad de corrientes 1/Km²')
print('\tAH - áreas hidrográficas...')
arcpy.CalculateField_management (hydroAreaLayer, 'Kc', '0.25*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroAreaLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroAreaLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tZH - zonas hidrográficas...')
arcpy.CalculateField_management (hydroZoneLayer, 'Kc', '0.25*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroZoneLayer, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroZoneLayer, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\tSZH - subzonas hidrográficas...')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Kc', '0.25*!Perm!/(!Area!**0.5)', 'Python')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Dd', '!SUM_LDre!/!Area!', 'Python')
arcpy.CalculateField_management (hydroSubZoneLayerCopy, 'Dc', '!FREQUENCY!/!Area!', 'Python')
print('\n')

TitleSeparator('Convirtiendo estadísticos y resultados a XLS', 'Both')
print('\tAH - área hidrográfica ' + statisticsTableAHXLS)
arcpy.TableToExcel_conversion(hydroAreaLayer,statisticsTableAHXLS)
print('\tZH - zona hidrográfica ' + statisticsTableZHXLS)
arcpy.TableToExcel_conversion(hydroZoneLayer,statisticsTableZHXLS)
print('\tSZH - subzona hidrográfica ' + statisticsTableSZHXLS)
arcpy.TableToExcel_conversion(hydroSubZoneLayerCopy,statisticsTableSZHXLS)

print('\nProceso terminado.')

