# -*- coding: UTF-8 -*-
# Nombre: GISListLayerFieldArcGIS.py
# Descripción: Consulta de capas vectoriales, propiedades y atributos en proyectos geográficos - ArcGIS for Desktop
# Requerimiento: PyCharm 2021.3+, Python 2.7.5 (ArcGIS 10.2.2)


#Consultar todas (opción 0) las capas disponibles en el directorio de trabajo, ver sus atributos y tipos.
#Permite consultar las propiedades de una capa específica y definir dos campos para su graficación.

# Librerías
import sys
import arcpy
import matplotlib
import matplotlib.pyplot as plt

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
arcpy.env.workspace = r'./Datos' # Definición del espacio de trabajo. Usar r para evitar salto de línea en directorios que empiezan por la letra n.

# Cabecera
Separador(100)
print ('Consulta de capas vectoriales, propiedades y atributos en proyectos geográficos - ArcGIS for Desktop')
Separador(100)
print ( 'Python versión: ' + str(sys.version)+
        '\nmatplotlib versión: ' + str(matplotlib.__version__)+
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/GISListLayerField'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com'
        '\nLa opción 0 muestra las capas disponibles en el directorio de trabajo, sus atributos y tipos.'
        '\nPara una capa específica muestra los atributos y permite definir dos campos para su graficación.\n')

# Consultar la lista de capas disponibles
featureList = arcpy.ListFeatureClasses() # Para el espacio de trabajo definido arcpy.env.workspace
Separador(28)
print('Listado de capas disponibles')
Separador(28)
print('Espacio de trabajo: '+arcpy.env.workspace)
cont = 1
for i in featureList:
    print('  ' + str(cont) + '  ' + i)
    cont += 1

# Mostrar la lista de campos disponibles en cada capa
try:
    numCapaEntrada = int(input('  >>> # capa a evaluar (0 -> Todas): '))
    if numCapaEntrada == 0:
        for i in featureList:
            CapaPropiedades(i)
    else:
        CapaPropiedades(featureList[numCapaEntrada-1])
        campoRotulo = input('  >>> Nombre del campo para rotulación (usar comillas): ')
        campoEvaluar = input('  >>> Nombre del campo a evaluar (usar comillas): ')
        graficoTipo = input('  >>> Tipo de gráfica (Bar, Pie) (usar comillas): ')
        campoFiltro = input('  >>> Mostrar valores >= a: ')
        cursor = arcpy.SearchCursor(featureList[numCapaEntrada-1]) # Records in properties table
        listaCampoRotulo, listaCampoEvaluar, listaCampoEtiqueta = [], [], []
        tituloLista = 'Lista de valores encontrados >= ' + str(campoFiltro)
        Separador(len(tituloLista))
        print(tituloLista)
        Separador(len(tituloLista))
        print('  ' + campoRotulo + ', ' + campoEvaluar)
        cont = 0
        # Propiedades encontradas para el campo a evaluar
        for fila in cursor:
            if fila.getValue(campoEvaluar) >= campoFiltro:
                listaCampoRotulo.append(cont)
                listaCampoEtiqueta.append(fila.getValue(campoRotulo))
                listaCampoEvaluar.append(fila.getValue(campoEvaluar))
                print('  ' +  str(listaCampoRotulo[cont]) + ', ' + str(listaCampoEtiqueta[cont]) + ', ' + str(listaCampoEvaluar[cont]))
                cont += 1
        print('  (' + str(cont) + ' registros)')
        # Graficación de datos
        Separador(20)
        print('Graficación de datos')
        Separador(20)
        if graficoTipo == 'Bar':
            plt.bar(listaCampoRotulo, listaCampoEvaluar, color = 'darkGray')
        else:
            plt.pie(listaCampoEvaluar, labels=listaCampoRotulo)
        plt.title('Valores encontrados')
        plt.xlabel(campoRotulo)
        plt.ylabel(campoEvaluar)
        plt.show()

except NameError as e:
    print('  >>> Error: dato ingresado inválido...')
except ValueError as e:
    print('  >>> Error: error en código fuente o en datos...')
except SyntaxError as e:
    print('  >>> Error: debe ingresar un número de capa...')
except IndexError as e:
    print('  >>> Error: capa o dato  no existe...')
except RuntimeError as e:
    print('  >>> Error: atributo no existe...')