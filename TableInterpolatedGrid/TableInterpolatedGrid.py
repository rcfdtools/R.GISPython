# -*- coding: utf-8 -*-

# Libraries
import arcpy
from arcpy import env
from arcpy.sa import *
import os
import os.path
import shutil
import time
import warnings
import TableInterpolatedGridModule as rtg
warnings.filterwarnings('ignore')

# Local variables
absolutePath = r'D:/R.GISPython/TableInterpolatedGrid/'
env.workspace = absolutePath + 'OutputGrid'
outputPath = absolutePath+'OutputGrid/'
outputPathColorMap = absolutePath+'OutputColorMap/'
outputTemp = absolutePath+'Temp/'
fileCSVIn = absolutePath+'Data/TablePrecipitationMonthly.csv'
shapefileTemp = outputTemp+'TempShapefile.shp'
colorMapStyleFolder = absolutePath+'ColorMapStyle/'
studyCase = 'Estudio de precipitación en el Departamento del Cesar - Colombia - Suramérica'
timeStart = time.time()
os.system('color 0E')
arcpy.env.overwriteOutput = True

# Welcome & Info screen
print('-------------------------------------------------------------'
      '\nMassive grid temporal interpolation with a dBASE table'
      '\nby r.cfdtools@gmail.com Python: 2.7.12. ArcGIS: 10.5'
      '\n-------------------------------------------------------------\n'
      '\nUsing a R Weather CDMS App tables, let build interpolate grids maps in a tiff format for daily or monthly values. With the generate tiff maps user can make a video for to study a weather parameter on the time.\n')
rtg.printtitle('Requirements')
print('\n\t* Valid table format file: comma separated values .csv'
      '\n\t* Float or double values required period as decimal separator.'
      '\n\t* CSV file with header row.'
      '\n\t* Field or attribute names can not content comma or special characters.'
      '\n\t* Header attributes names required: Julian (1-366), Month (1-12), CX, CX, CZ, Var.'
      '\n\t* Var correspond to the numeric variable for analysis. User can choice the var name.'
      '\n\t* Compatible with ArcGIS for Desktop 10+ and ArcGIS Pro.'
      '\n\t* ArcGIS Spatial analyst extension: ' + arcpy.CheckOutExtension('Spatial') + '\n')

# Preprocesing variables
rtg.printtitle('Study case & File data summary')
print('\n\t* Study case: ' + str(studyCase) +
      '\n\t* Input file: ' + fileCSVIn)
fieldsCSV = rtg.fCSVTotalFieldFound(fileCSVIn)
totalRecords = rtg.fCSVTotalRecordFound(fileCSVIn)
input('\n' + rtg.systemprompt() + 'Attention - Close all the ArcGIS for Desktop applications and press Enter >> ')
rtg.fCSVPreviewRecord(fileCSVIn, totalRecords+1)
fieldNumberEval=rtg.fCSVHeader(fileCSVIn,totalRecords,fieldsCSV)
print('\n')
rtg.fGraphTxt(fileCSVIn,totalRecords,fieldNumberEval[0])
StatisticCSV = rtg.fCSVStatistic(fileCSVIn,totalRecords,fieldNumberEval[0])
maxVal = StatisticCSV[3]
minVal = StatisticCSV[4]
spatialDomainCSV = rtg.fCSVSpacialDomain(fileCSVIn)
gidCellSizeRecommended = spatialDomainCSV[2]
fieldEvalStr = fieldNumberEval[1]
dataFrecuency = rtg.fDataFrecuency()
frecuencyFieldOpt = dataFrecuency[1]
frecuencyMaxVal = int(dataFrecuency[0])
numGrid = rtg.fOptionRange('Total grids to create ',1,frecuencyMaxVal)
userCRS = rtg.fCoordSystem()
gridResolution = rtg.fOptionRangeFloat(('Output grid resolution for the coordinate system selected (%f recommended)' %(round(gidCellSizeRecommended, 2))),0,10000)
colorMapFileArray = rtg.fColorMapStyle(colorMapStyleFolder)
colorMapFile = colorMapFileArray[0]
colorMapFilePrev = colorMapFileArray[1]
colorMapFileColors = float(colorMapFileArray[2])
numColor = int(colorMapFileColors)
slopeRampData = numColor / (maxVal - minVal)
os.system(colorMapFilePrev)


# Delete previous data Temp and Out folder created
try:
    shutil.rmtree(outputPath)  # Remove Out folder
except:
    print(rtg.systemprompt() + 'Out folder does not exists')
os.mkdir(outputPath)  # Create empty Out folder
try:
    shutil.rmtree(outputPathColorMap) #Remove Temp folder
except:
    print(rtg.systemprompt() + 'Out Color Map folder does not exists')
os.mkdir(outputPathColorMap)  # Create empty Temp folder
try:
    shutil.rmtree(outputTemp)  # Remove Temp folder
except:
    print(rtg.systemprompt() + 'Temp folder does not exists')
os.mkdir(outputTemp)  # Create empty Temp folder


# Grid builder section
numGridStr = str(numGrid)
incV=1; maxValPixelValue = -1e99; minValPixelValue = 1e99; dayMonthMax = 0; dayMonthMin = 0;
print('\n')
rtg.printtitle('Creating ' + numGridStr + ' file grids', 'Both')
while incV <= numGrid:
    incVStr = str(incV)

    # Process: Make XY Event Layer
    eventLyr = 'EventLyr' + incVStr
    arcpy.MakeXYEventLayer_management(fileCSVIn, 'CX', 'CY', eventLyr, userCRS, '')

    # Process: Select records from Julian day number
    frequencyFieldOptTxt = '\"'+frecuencyFieldOpt+'\" ='
    arcpy.Select_analysis(eventLyr, shapefileTemp, frequencyFieldOptTxt + incVStr)

    # Process: IDW - Inverse Distance Weight Intepolation
    gridDayNFileName = 'GRDM' + incVStr.zfill(3) + '.tif'
    gridDayNTiff = outputPath + gridDayNFileName
    #arcpy.gp.Idw_sa(shapefileTemp, 'Var', gridDayNTiff, gridResolution, '2', 'VAR 12', '')
    #arcpy.gp.Idw_sa(shapefileTemp, fieldEvalStr, gridDayNTiff, gridResolution, '2', '', '')
    power = 2
    searchRadius = RadiusVariable(10, 150000)
    outIDW = Idw(shapefileTemp, fieldEvalStr, gridResolution, power, searchRadius) 
    outIDW.save(gridDayNTiff)

    # Remove and create Temp folder
    shutil.rmtree(outputTemp) #Remove Temp folder
    os.mkdir(outputTemp) #Create empty Temp folder

    # Process: Show created raster properties
    cyMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'TOP', '')
    cyMaxAux = float (cyMax.getOutput(0))
    cyMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'BOTTOM', '')
    cyMinAux = float (cyMin.getOutput(0))
    ySize = (cyMaxAux - cyMinAux) / 1000
    cxMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'RIGHT', '')
    cxMaxAux = float (cxMax.getOutput(0))
    cxMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'LEFT', '')
    cxMinAux = float (cxMin.getOutput(0))
    xSize = (cxMaxAux - cxMinAux) / 1000
    valMax = arcpy.GetRasterProperties_management(gridDayNTiff, 'MAXIMUM', '')
    valMaxAux = float (valMax.getOutput(0))
    valMin = arcpy.GetRasterProperties_management(gridDayNTiff, 'MINIMUM', '')
    valMinAux = float (valMin.getOutput(0))
    print('\tFile', gridDayNFileName, '- High(km):', ySize, '- Width(km):', xSize, '- Min:', round(valMinAux, 4), '- Max:', round(valMaxAux, 4), '- Ok...')
    if valMaxAux > maxValPixelValue:
        maxValPixelValue = valMaxAux
        dayMonthMax = incV
    if valMinAux < minValPixelValue:
        minValPixelValue = valMinAux
        dayMonthMin = incV
    incV += 1


# Grid color map using integer scale
incV=1; maxValPixelValueStr = str(maxValPixelValue); minValStr = str(minVal); numColorStr = str(numColor); slopeRampDataStr = str(slopeRampData);
print('\n')
rtg.printtitle('Creating ' + str(numGridStr) + ' grid color scaled creation files ('+(str(numColor)) + ' colors)')
print('\tAll database values'
      '\n\tMax Data Value:',maxVal ,
      '\n\tMin Data Value:',minVal,
      '\n\tSlope Colors Ramp:',slopeRampData,
      '\n\tGrids created'
      '\n\tMax Pixel Value:',maxValPixelValue,
      '\n\tMin Pixel Value:',minValPixelValue)
while incV <= numGrid:
    incVStr = str(incV)
    gridDayNFileName = 'GRDM' + incVStr.zfill(3) + '.tif'
    gridDayNTiffSorce = outputPath + gridDayNFileName
    gridDayNTiffTarget = outputPathColorMap + gridDayNFileName
    vAlgebraMapClc = 'Con((Int(((\''+gridDayNTiffSorce+'\'-'+minValStr+')*'+slopeRampDataStr+')))>'+numColorStr+','+numColorStr+',(Int(((\''+gridDayNTiffSorce+'\'-'+minValStr+')*'+slopeRampDataStr+'))))'
    arcpy.gp.RasterCalculator_sa(vAlgebraMapClc, gridDayNTiffTarget)
    arcpy.AddColormap_management(gridDayNTiffTarget, '', colorMapFile)
    print('\tFile color map', gridDayNFileName, 'Ok...')
    incV += 1


# Show final process resume
timeEnd = time.time()
print('\n')
rtg.printtitle('Statistics and summary grid creation report')
print('\n\t* Grids created on:', outputPath ,
      '\n\t* Color Map Grids created on:', outputPathColorMap,
      '\n\t* Minimum pixel value all grids:', round(minValPixelValue, 4),
      '\n\t* Maximum pixel value all grids:', round(maxValPixelValue, 4) ,
      '\n\t* ArcScene Z Scale conversion:', round((maxValPixelValue/colorMapFileColors), 6),
      '\n\t* Day or Month with maximum value:', dayMonthMax,
      '\n\t* Process acomplished (dt = ', round(timeEnd - timeStart, 1), 'sec or', round((timeEnd - timeStart)/60, 1), 'min)')
vExit = input('\n%s Press Enter to Exit...' %(rtg.systemprompt()))
