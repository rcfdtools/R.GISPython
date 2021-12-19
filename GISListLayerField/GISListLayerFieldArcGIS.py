#-*- coding: UTF-8 -*-
#Curso: TSIG - Sistemas de Información Geográfica Aplicados
#Microcontenido: HPSD0007 - Python - Cargar capas Vectoriales, consultar sus propiedades y atributos en ArcGIS
#Créditos: william.aguilar@escuelaing.edu.co, r.cfdtools@gmail.com
#Cláusulas y condiciones de uso en https://pruebacorreoescuelaingeduco.sharepoint.com/sites/TSIG626
#Ejecución: ArcGIS Desktop 10.2.2 con Python 2.7.5
#Consultar todas (opción 0) las capas disponibles en el directorio de trabajo, ver sus atributos y tipos.
#Permite consultar las propiedades de una capa específica y definir dos campos para su graficación.

#Importación de librerías
import arcpy
import matplotlib.pyplot as plt

#Función para creación de líneas de separación
def Separador(n=24): #Usando un valor por defecto de 24 guiones
    nc = '-'
    print(nc*n)

#Función para consultar los campos de atributos disponibles
#https://pro.arcgis.com/es/pro-app/arcpy/functions/listfields.htm
#https://pro.arcgis.com/es/pro-app/arcpy/classes/field.htm
#https://pro.arcgis.com/es/pro-app/tool-reference/data-management/get-count.htm
#https://community.esri.com/thread/36300
def CapaPropiedades(i):
    Cont = 1
    Separador(48)
    TotalEntidades = arcpy.GetCount_management(i)
    DescGeometria = arcpy.Describe(i)
    TipoGeometria = DescGeometria.shapeType
    print('Campos en ' + i + ' (' + TipoGeometria + 's ' + str(TotalEntidades) + ')')
    Separador(48)
    print('  #, Campo, Tipo')
    Campos = arcpy.ListFields(i)
    for Campo in Campos:
        print('  ' + str(Cont) + ', ' + Campo.name + ', ' + Campo.type)  # Print field properties
        Cont += 1

#Función para consultar los valores almacenados en los campos de atributos

#Definicion del espacio de trabajo
#arcpy.env.workspace = r'C:\HPSD\HPSD0007\Datos' #Usar r para evitar salto de línea en directorios que empiezan por la letra n.
arcpy.env.workspace = r'Datos' #Usar r para evitar salto de línea en directorios que empiezan por la letra n.

#Consultar la lista de capas disponibles
FeatureList = arcpy.ListFeatureClasses()
Separador(30)
print('Listado de capas disponibles')
Separador(30)
print(arcpy.env.workspace)
Cont = 1
for i in FeatureList:
    print('  ' + str(Cont) + '  ' + i)
    Cont += 1

#Mostrar la lista de campos disponibles en cada capa
try:
    NumCapaEntrada = int(input('  >>> # capa a evaluar (0 -> Todas): '))
    if NumCapaEntrada == 0:
        for i in FeatureList:
            CapaPropiedades(i)
    else:
        CapaPropiedades(FeatureList[NumCapaEntrada-1])
        CampoRotulo = input('  >>> Nombre del campo para rotulación (Usar comillas): ')
        CampoEvaluar = input('  >>> Nombre del campo a evaluar (Usar comillas): ')
        CampoFiltro = input('  >>> Mostrar valores >= a: ')
        Cursor = arcpy.SearchCursor(FeatureList[NumCapaEntrada-1]) #https://pro.arcgis.com/es/pro-app/arcpy/functions/searchcursor.htm
        ListaCampoRotulo, ListaCampoEvaluar = [], []
        Separador(38)
        print('Lista de valores encontrados >= ' + str(CampoFiltro))
        Separador(38)
        print('  ' + CampoRotulo + ', ' + CampoEvaluar)
        Cont = 0
        for Fila in Cursor:
            if Fila.getValue(CampoEvaluar) >= CampoFiltro:
                ListaCampoRotulo.append(Cont)
                #ListaCampoRotulo.append(Fila.getValue(CampoRotulo))
                ListaCampoEvaluar.append(Fila.getValue(CampoEvaluar))
                print('  ' +  str(ListaCampoRotulo[Cont]) + ', ' + str(ListaCampoEvaluar[Cont]))
                Cont += 1
        print('  (' + str(Cont) + ' registros)')

        # Graficación de datos
        Separador(30)
        print('Graficación de datos')
        Separador(30)
        plt.bar(ListaCampoRotulo, ListaCampoEvaluar, color = 'darkGray')
        plt.title('VALORES ENCONTRADOS')
        plt.xlabel(CampoRotulo)
        plt.ylabel(CampoEvaluar)
        plt.show()

except NameError as e:
    print('  >>> Error: Dato ingresado inválido...')
except ValueError as e:
    print('  >>> Error: Error en código fuente o en datos...')
except SyntaxError as e:
    print('  >>> Error: Debe ingresar un número de capa...')
except IndexError as e:
    print('  >>> Error: Capa o dato  no existe...')
except RuntimeError as e:
    print('  >>> Error: Atributo no existe...')