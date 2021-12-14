# -*- coding: UTF-8 -*-
# Name: CNEIDEAMStat.py
# Description: Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia, descarga y análisis.
# Requirements: PyCharm 2021.3+, Python 3.10.0 (instalación independiente),

# Libraries
import pandas as pd # Tested with 1.3.4 version.
# import numpy as np # Tested with 1.21.4 version. # Has to be installed with not import required.
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.
from datetime import datetime
from datetime import date
import requests
import matplotlib.pyplot as plt
import os.path

# General variables
urlFile = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileName = 'CNE_IDEAM'
fileExtension = '.xls'
downloadFile = False # Use False for process the last file downloaded
sampleRecord = 12 # Number of records to show in the sample
showRecordSample = False # Print some sample records
showAllRecords = False # Print all the records at the report tail
showGraphScreen = False # Show graphs on the screen. This script always update ./Graph & ./PivotTable
thermalLevelCaldas = True # True for Caldas classification, False for conventional classification range
stationName = 'nombre'
latitudeName = 'latitud'
longitudeName = 'longitud'
elevationName = 'altitud'
categoryName = 'CATEGORIA'
technologyName = 'TECNOLOGIA'
stateActiveName = 'ESTADO'
installationDate = 'FECHA_INSTALACION'
geoStateName = 'DEPARTAMENTO'
geoOperativeAreaName = 'AREA_OPERATIVA'
geoHydroAreaName = 'AREA_HIDROGRAFICA'
geoHydroZoneName = 'ZONA_HIDROGRAFICA'
geoHydroSubZoneName = 'SUBZONA_HIDROGRAFICA'
thermalLevelRefConv = [[1000,'Cálido, 24°C+, <= 1000 meters'],[2000,'Templado, 18°C+, <= 2000 meters'],[3000,'Frío, 12°C+, <= 3000 meters'],[4000,'Páramo, 0°C, <= 4000 meters'],[99999,'Glacial, 0°C-, > 4000 meters']] # Elevation value in meters
thermalLevelRefCaldas = [[800,'Cálido, T>=24°C, <=800meter'],[1800,'Templado, 24°C>T>18°C, <=1800meter'],[2800,'Frío, 18°C>T>12°C, <=2800meter'],[3700,'Muy Frío, 12°C>T>6°C, <=3700meter'],[4700,'Extremadamente Frio, 6°C>T>0°C, <=4700meter'],[99999,'Nival, T<0°C, >4700meter']] # Elevation value in meters
graphTitlePrefix='CNE IDEAM Colombia -  '
mySignature = 'https://github.com/rcfdtools/R.GISPython'
graphTransparency = 1 # Save color for paper print versions, 1 for full color. Doesn't apply for pie charts

# Separation title line function
def SeparatorTitle(n=24): # Default using 24 - characters
    nc = '-'
    print(nc*n)

# Thermal level evaluation function
def thermalLevelF(elevation):
    for i in thermalLevelRef[:]:
        if elevation <= i[0]:
            return i[1]

# Downloading and reading the file
fileDownloadText = 'File downloaded and updated = No'
currentDate = date.today()
currentDateTxt=str(currentDate.year)+str(currentDate.month)+str(currentDate.day)
fileRequest = requests.get(urlFile)
fileSave = './Data/'+fileName+'_'+currentDateTxt+fileExtension
#if downloadFile == True:
if fileRequest:
    if os.path.isfile(fileSave) == False:
        open(fileSave, 'wb').write(fileRequest.content)
        fileDownloadText = 'File downloaded and updated = Yes'
stationTable = pd.read_excel(fileSave)
pd.set_option('display.max_rows', stationTable.shape[0]+1) # Show all the records
pd.set_option('display.max_columns', None) # Show all the records

# Header and general file summary
shapeTable = stationTable.shape # Row and columns array size
SeparatorTitle(72)
print('Catálogo nacional de estaciones hidroclimatológicas del IDEAM - Colombia')
SeparatorTitle(72)
print(  '\nEjecutado en: '+str(datetime.now()),
        '\nData summary for '+fileSave,
        '\nUrl: '+urlFile,
        '\nStations file by: Instituto de Hidrología, Meteorología y Estudios Ambientales',
        '\nhttp://www.ideam.gov.co/web/atencion-y-participacion-ciudadana/condiciones-y-terminos-de-uso-de-la-informacion',
        '\nDataframe type: '+str(type(stationTable)),
        '\n'+fileDownloadText,
        '\nStations: '+ str(stationTable.shape[0])+'\nAttributes: '+ str(stationTable.shape[1]),
        '\nEncuentra este script en https://github.com/rcfdtools/R.GISPython/tree/main/CNEStationStatistic'
        '\nCláusulas y condiciones de uso en https://github.com/rcfdtools/R.GISPython/wiki/License'
        '\nCréditos: r.cfdtools@gmail.com\n')

# Sample records
if showRecordSample == True:
    SeparatorTitle(14)
    print('Sample records')
    SeparatorTitle(14)
    print('\nFirst '+str(sampleRecord)+' records: ')
    print(stationTable.head(sampleRecord)) # By default show 5 records
    print('Last '+str(sampleRecord)+' records: ')
    print(stationTable.tail(sampleRecord)) # By default show 5 records
    print('\n')

# Attributes summary
SeparatorTitle(27)
print('Attributes an types founded')
SeparatorTitle(27)
print(stationTable.columns)
print('\nTypes: ')
print(stationTable.dtypes) # With stationTable.columns you can get the attributes names in an array.
print('\nGeneral dataframe information: ')
print(stationTable.info())
print('\n')

# Basic dataframe statistics
SeparatorTitle(18)
print('General statistics')
SeparatorTitle(18)
print('\nBasic dataframe statistics: ')
print(stationTable.describe())
print('\nCategory - Count: ')
print(stationTable[categoryName].value_counts())
print('\nCategory - Normalize percentage rate: ')
print(stationTable[categoryName].value_counts(normalize=True).round(4))
print('\nTechnology - Count: ')
print(stationTable[technologyName].value_counts())
print('\nTechnology - Normalize percentage rate: ')
print(stationTable[technologyName].value_counts(normalize=True).round(4))
print('\nState active - Count: ')
print(stationTable[stateActiveName].value_counts())
print('\nState active - Normalize percentage rate: ')
print(stationTable[stateActiveName].value_counts(normalize=True).round(4))
print('\nGeographical state location- Count: ')
print(stationTable[geoStateName].value_counts())
print('\nGeographical state location - Normalize percentage rate: ')
print(stationTable[geoStateName].value_counts(normalize=True).round(4))
print('\nGeographical operative area - Count: ')
print(stationTable[geoOperativeAreaName].value_counts())
print('\nGeographical operative area - Normalize percentage rate: ')
print(stationTable[geoOperativeAreaName].value_counts(normalize=True).round(4))
print('\nHydrographic area - Count: ')
print(stationTable[geoHydroAreaName].value_counts())
print('\nHydrographic area - Normalize percentage rate: ')
print(stationTable[geoHydroAreaName].value_counts(normalize=True).round(4))
print('\nHydrographic zone - Count: ')
print(stationTable[geoHydroZoneName].value_counts())
print('\nHydrographic zone - Normalize percentage rate: ')
print(stationTable[geoHydroZoneName].value_counts(normalize=True).round(4))
print('\nHydrographic subzone - Count: ')
print(stationTable[geoHydroSubZoneName].value_counts())
print('\nHydrographic subzone - Normalize percentage rate: ')
print(stationTable[geoHydroSubZoneName].value_counts(normalize=True).round(4))
print('\nInstallation year - Count: ')
stationTable.sort_values(installationDate, ascending=True, inplace=True) # Reorder and uptate the dataframe by installation date records
stationTableYearCount = pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0)
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False).round(0))
print('\nInstallation year - Normalize percentage rate: ')
print(pd.DatetimeIndex(stationTable[installationDate]).year.value_counts(sort=False, normalize=True).round(4))
print('\n')


# Pivot tables
SeparatorTitle(12)
print('Pivot tables')
SeparatorTitle(12)
print('\n')
# Category
pivotTable=stationTable.pivot_table(index=categoryName, columns=stateActiveName, values=technologyName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='barh', xlabel='Category', ylabel='Stations', title=graphTitlePrefix+'Stations by Category - Date:  '+str(currentDate)+'\n'+mySignature, figsize=(16,10), alpha=graphTransparency, rot=0, stacked=True) # alpha for transparency
plt.savefig('./Graph/CategoryPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/CategoryPivot'+currentDateTxt+'.csv')
print('\n')
# Technology
pivotTable=stationTable.pivot_table(index=technologyName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Technology', ylabel='Stations', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(8,8), fontsize=11, alpha=graphTransparency, rot=0, stacked=True )
plt.savefig('./Graph/TechnologyPivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Technology - Date: '+str(currentDate)+'\n'+mySignature, figsize=(24,8), startangle=30, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/TechnologyPivotPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/TechnologyPivot'+currentDateTxt+'.csv')
print('\n')
# Geographical state
pivotTable=stationTable.pivot_table(index=geoStateName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical state', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical State - Date: '+str(currentDate)+'\n'+mySignature, figsize=(14,18), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoStatePivot'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoStatePivot'+currentDateTxt+'.csv')
print('\n')
# Geographical operative area
pivotTable=stationTable.pivot_table(index=geoOperativeAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical operative area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Operative Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,16), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoOperativeArea'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoOperativeArea'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological area
pivotTable=stationTable.pivot_table(index=geoHydroAreaName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological area', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Area - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,10), alpha=graphTransparency, rot=0, stacked=True, subplots=True, fontsize=11, grid=False, legend=False)
plt.savefig('./Graph/GeoHydroArea'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroArea'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological zone
pivotTable=stationTable.pivot_table(index=geoHydroZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological zone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Zone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), alpha=graphTransparency, rot=-90, stacked=True, fontsize=10)
plt.savefig('./Graph/GeoHydroZone'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroZone'+currentDateTxt+'.csv')
print('\n')
# Geographical hydrological subzone
pivotTable=stationTable.pivot_table(index=geoHydroSubZoneName, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Geographical hydrological subzone', ylabel='Stations', title=graphTitlePrefix+'Stations by Geographical Hydrological Subzone - Date: '+str(currentDate)+'\n'+mySignature, figsize=(44,20), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/GeoHydroSubzone'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/GeoHydroSubzone'+currentDateTxt+'.csv')
print('\n')
# Installed stations by year
pivotTable = stationTable.pivot_table(index=pd.DatetimeIndex(stationTable[installationDate]).year, columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Year', ylabel='Stations', title=graphTitlePrefix+'Installed Stations by year - Date: '+str(currentDate)+'\n'+mySignature, figsize=(22,12), alpha=graphTransparency, rot=-90, stacked=True)
plt.savefig('./Graph/InstallationYear'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/InstallationYear'+currentDateTxt+'.csv')

# Geospatial array
geoArray=stationTable[[latitudeName,longitudeName,elevationName]]
print('\n')
SeparatorTitle(39)
print('Geospatial array sample with '+str(sampleRecord)+' records')
SeparatorTitle(39)
print(geoArray.head(sampleRecord))
print('Dataframe type: '+str(type(geoArray))+'\n')

# Thermal level evaluation
if thermalLevelCaldas == True:
    thermalLevelRef = thermalLevelRefCaldas
    thermalLevelRefTitle = "Caldas classification"
    SeparatorTitleVal = 48
else:
    thermalLevelRef = thermalLevelRefConv
    thermalLevelRefTitle = "Conventional classification"
    SeparatorTitleVal = 54
SeparatorTitle(SeparatorTitleVal)
print('Thermal level evaluation - '+thermalLevelRefTitle)
SeparatorTitle(SeparatorTitleVal)
print('\nThermal level reference array:')
print(pd.DataFrame(thermalLevelRef,columns=['Elevation ref value','Thermic level']))
print('\n')
thermalLevelArray = []
for i in geoArray[elevationName]:
    thermalLevelArray.append(thermalLevelF(i))
stationTable['ThermalLevelValue']=thermalLevelArray
print('Geospatial array sample with '+str(sampleRecord)+' records:')
geoArray=stationTable[[stationName,latitudeName,longitudeName,elevationName,'ThermalLevelValue']]
print(geoArray.head(sampleRecord))
print('\nThermal level statistics:')
print('Count:')
print(geoArray['ThermalLevelValue'].value_counts())
print('\nNormalize percentage rate:')
print(geoArray['ThermalLevelValue'].value_counts(normalize=True).round(4))
print('\n')
pivotTable = stationTable.pivot_table(index='ThermalLevelValue', columns=stateActiveName, values=categoryName, aggfunc='count')
print(pivotTable)
pivotTable.plot(kind='bar', xlabel='Thermal level', ylabel='Stations', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(12,12), fontsize=11, rot=10, stacked=True, alpha=graphTransparency)
plt.savefig('./Graph/ThermalLevel'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.plot(kind='pie', title=graphTitlePrefix+'Stations by Thermal Level - Date: '+str(currentDate)+'\n'+mySignature, figsize=(36,8), startangle=60, subplots=True, autopct='%1.1f%%', fontsize=12, legend=False)
plt.savefig('./Graph/ThermalLevelPie'+currentDateTxt+'.png')
if showGraphScreen == True: plt.show()
pivotTable.to_csv('./PivotTable/ThermalLevel'+currentDateTxt+'.csv')
print('\n')

# General plot station
pivotTable=geoArray.plot.scatter(x=longitudeName, y=latitudeName, c=elevationName, colormap='viridis', colorbar=True, title=graphTitlePrefix+'Stations scatter plot map with altitude - Date: '+str(currentDate)+'\n'+mySignature, figsize=(10,11), grid=True, alpha=graphTransparency)
if showGraphScreen == True: plt.show()
plt.savefig('./Graph/StationScatterPlotMap'+currentDateTxt+'.png')
geoArray.to_csv('./PivotTable/StationScatterPlotMap'+currentDateTxt+'.csv')

# Show all data
if showAllRecords == True:
    SeparatorTitle(41)
    print('Stations in '+fileSave)
    SeparatorTitle(41)
    print('Index: ' + str(stationTable.index))
    pd.set_option('display.max_rows',stationTable.shape[0]+1)
    print(geoArray[[stationName,latitudeName,longitudeName]])
