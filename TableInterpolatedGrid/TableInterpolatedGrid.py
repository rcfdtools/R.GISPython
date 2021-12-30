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
import TableToGridModule as rtg
warnings.filterwarnings("ignore")

# Local variables
vFolderMain = r"D:/R.GISPython/TableToGrid/"
env.workspace = vFolderMain + 'OutputGrid'
vFolderOutput = vFolderMain+"OutputGrid/"
vFolderOutputColorMap = vFolderMain+"OutputColorMap/"
vFolderTemp = vFolderMain+"Temp/"
vFileName = vFolderMain+"Data/TablePrecipitationMonthly.csv"
vShapeFile = vFolderTemp+"TempShapefile.shp"
vFolderColorMapStyle = vFolderMain+"ColorMapStyle/"
vTimeStart = time.time()
os.system("color 0E")

# Welcome & Info screen
print ""
print "-----------------------------------------------------------------------------------------"
print " CREATE WEATHER PARAMETER GRID SETS USING dBASE TABLE v1.15"
print " by r.cfdtools@gmail.com Python: 2.7.12. ArcGIS: 10.5"
print "-----------------------------------------------------------------------------------------"
print " Description: Using a R Weather CDMS App tables, let build interpolate"
print " grids maps in a tiff format for daily or monthly values. With the generate"
print " tiff maps user can make a video for to study a weather parameter on the time."
print ""
print " Table format file input valid: comma separated values .csv"
print " Float or doubles values required dot as decimal separator."
print ""
print " Requirements:"
print "   csv file with header row."
print "   Decimal values always been separated using dot."
print "   Field with text values can't content comma."
print "   Header row minimun required: Julian, Month, CX, CX, CZ, Var."
print "   Var content values to analysis."
print('   Spatial Analyst: ' + arcpy.CheckOutExtension('Spatial') + '\n')
print raw_input(rtg.systemprompt()+"Alert - Close ARCGIS applications and press Enter >> ")
print "\tProcessing file",vFileName


# Preprocesing variables
vFields=rtg.fCSVTotalFieldFound(vFileName)
vRowTotal = rtg.fCSVTotalRecordFound(vFileName)
rtg.fCSVPreviewRecord(vFileName,vRowTotal+1)
vFieldNumberEval=rtg.fCSVHeader(vFileName,vRowTotal,vFields)
rtg.fGraphTxt(vFileName,vRowTotal,vFieldNumberEval[0])
vCSVStatistic = rtg.fCSVStatistic(vFileName,vRowTotal,vFieldNumberEval[0])
vMax =  vCSVStatistic[3]
vMin =  vCSVStatistic[4]
vCSVSpacialDomain = rtg.fCSVSpacialDomain(vFileName)
vGridCellSizeRecommended = vCSVSpacialDomain[2]
vFieldEvalStr = vFieldNumberEval[1]
vDataFrecuency=rtg.fDataFrecuency()
vFrecuencyFieldOpt = vDataFrecuency[1]
vFrecuenciaMaxVal = int(vDataFrecuency[0])
vNumGrid = rtg.fOptionRange("Total Grids to create",1,vFrecuenciaMaxVal)
vCoordSystem = rtg.fCoordSystem()
vResGrid = rtg.fOptionRangeFloat(("Output grid resolution for the coordinate system selected (%f recommended)" %(vGridCellSizeRecommended)),0,10000)
vColorMapFileArray = rtg.fColorMapStyle(vFolderColorMapStyle)
vColorMapFile = vColorMapFileArray[0]
vColorMapFilePrev = vColorMapFileArray[1]
vColorMapFileColors = float(vColorMapFileArray[2])
vNumColor = int(vColorMapFileColors)
vSlopeRampData = vNumColor / (vMax - vMin)
os.system(vColorMapFilePrev)


# Delete previous data Temp and Out folder created
try:
    shutil.rmtree(vFolderOutput) #Remove Out folder
except:
    print rtg.systemprompt(),"Out folder doesn't exists"
os.mkdir(vFolderOutput) #Create empty Out folder
try:
    shutil.rmtree(vFolderOutputColorMap) #Remove Temp folder
except:
    print rtg.systemprompt(),"Out Color Map folder doesn't exists"
os.mkdir(vFolderOutputColorMap) #Create empty Temp folder
try:
    shutil.rmtree(vFolderTemp) #Remove Temp folder
except:
    print rtg.systemprompt(),"Temp folder doesn't exists"
os.mkdir(vFolderTemp) #Create empty Temp folder


# Grid builder section
vNumGridStr = str(vNumGrid)
vInc=1; vMaxPixelValue = -1e99; vMinPixelValue = 1e99; vDayMonthMax = 0; vDayMonthMin = 0;
print "\n\t-----------------------------------------------------------------------------------------"
print "\tSTARTING", vNumGridStr, "GRIDS CREATION FILES"
print "\t-----------------------------------------------------------------------------------------"
while vInc <= vNumGrid:
    vIncStr = str(vInc)

    # Process: Make XY Event Layer
    vEventLyr = "EventLyr" + vIncStr
    #vCoordSystem = "PROJCS['GAUSS_BTA_MAGNA',GEOGCS['CGS_SIRGAS',DATUM['CGS_SIRGAS',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1000000.0],PARAMETER['False_Northing',1000000.0],PARAMETER['Central_Meridian',-74.077507917],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',4.596200417],UNIT['Meter',1.0]];-4623200 -9510300 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
    #arcpy.MakeXYEventLayer_management(vFileName, "CX", "CY", vEventLyr, vCoordSystem, "CZ")
    arcpy.MakeXYEventLayer_management(vFileName, "CX", "CY", vEventLyr, vCoordSystem, "")

    # Process: Select records from Julian day number
    vFrecuencyFieldOptTxt = "\""+vFrecuencyFieldOpt+"\" ="
    arcpy.Select_analysis(vEventLyr, vShapeFile, vFrecuencyFieldOptTxt + vIncStr)

    # Process: IDW - Inverse Distance Weight Intepolation
    vGRDayNFileName = "GRDM" + vIncStr.zfill(3) + ".tif"
    vGRDayNTif = vFolderOutput + vGRDayNFileName
    #arcpy.gp.Idw_sa(vShapeFile, "Var", vGRDayNTif, vResGrid, "2", "VAR 12", "")
    #arcpy.gp.Idw_sa(vShapeFile, vFieldEvalStr, vGRDayNTif, vResGrid, "2", "", "")
    power = 2
    searchRadius = RadiusVariable(10, 150000)
    outIDW = Idw(vShapeFile, vFieldEvalStr, vResGrid, power, searchRadius) ############
    outIDW.save(vGRDayNTif)

    # Remove and create Temp folder
    shutil.rmtree(vFolderTemp) #Remove Temp folder
    os.mkdir(vFolderTemp) #Create empty Temp folder

    # Process: Show created raster properties
    vCYMax = arcpy.GetRasterProperties_management(vGRDayNTif, "TOP", "")
    vCYMaxAux = float (vCYMax.getOutput(0))
    vCYMin = arcpy.GetRasterProperties_management(vGRDayNTif, "BOTTOM", "")
    vCYMinAux = float (vCYMin.getOutput(0))
    vYSize = (vCYMaxAux - vCYMinAux) / 1000
    vCXMax = arcpy.GetRasterProperties_management(vGRDayNTif, "RIGHT", "")
    vCXMaxAux = float (vCXMax.getOutput(0))
    vCXMin = arcpy.GetRasterProperties_management(vGRDayNTif, "LEFT", "")
    vCXMinAux = float (vCXMin.getOutput(0))
    vXSize = (vCXMaxAux - vCXMinAux) / 1000
    vValMax = arcpy.GetRasterProperties_management(vGRDayNTif, "MAXIMUM", "")
    vValMaxAux = float (vValMax.getOutput(0))
    vValMin = arcpy.GetRasterProperties_management(vGRDayNTif, "MINIMUM", "")
    vValMinAux = float (vValMin.getOutput(0))
    print "\tFile", vGRDayNFileName, "- High(km):",vYSize,"- Width(km):",vXSize,"- Min:",round(vValMinAux,4),"- Max:",round(vValMaxAux,4),"- Ok..."
    if vValMaxAux > vMaxPixelValue:
        vMaxPixelValue = vValMaxAux
        vDayMonthMax = vInc
    if vValMinAux < vMinPixelValue:
        vMinPixelValue = vValMinAux
        vDayMonthMin = vInc
    vInc += 1


# Grid color map using integer scale
vInc=1; vMaxPixelValueStr = str(vMaxPixelValue); vMinStr = str(vMin); vNumColorStr = str(vNumColor); vSlopeRampDataStr = str(vSlopeRampData); 
print "\n\t-----------------------------------------------------------------------------------------"
print "\tSTARTING", vNumGridStr, "GRIDS COLOR SCALED CREATION FILES ("+(str(vNumColor))+" colors)"
print "\t-----------------------------------------------------------------------------------------"
print "\tAll database values"
print "\t  Max Data Value:\t",vMax
print "\t  Min Data Value:\t",vMin
print "\t  Slope Colors Ramp:\t",vSlopeRampData
print "\tGrids created"
print "\t  Max Pixel Value:\t",vMaxPixelValue
print "\t  Min Pixel Value:\t",vMinPixelValue
while vInc <= vNumGrid:
    vIncStr = str(vInc)
    vGRDayNFileName = "GRDM" + vIncStr.zfill(3) + ".tif"
    vGRDayNTifSorce = vFolderOutput + vGRDayNFileName
    vGRDayNTifTarget = vFolderOutputColorMap + vGRDayNFileName
    vAlgebraMapClc = "Con((Int(((\""+vGRDayNTifSorce+"\"-"+vMinStr+")*"+vSlopeRampDataStr+")))>"+vNumColorStr+","+vNumColorStr+",(Int(((\""+vGRDayNTifSorce+"\"-"+vMinStr+")*"+vSlopeRampDataStr+"))))"
    arcpy.gp.RasterCalculator_sa(vAlgebraMapClc, vGRDayNTifTarget)
    arcpy.AddColormap_management(vGRDayNTifTarget, "", vColorMapFile)
    print "\tFile Color Map", vGRDayNFileName,"Ok..."
    vInc += 1


# Show final process resume
vTimeEnd = time.time()
print "\n\t-----------------------------------------------------------------------------------------"
print "\tSTATISTICS AND RESUME GRID CREATION REPORT"
print "\t-----------------------------------------------------------------------------------------"
print "\tGrids created on                ", vFolderOutput
print "\tColor Map Grids created on      ", vFolderOutputColorMap
print "\tMinimun pixel value all grids   ", round(vMinPixelValue,4)
print "\tMaximun pixel value all grids   ", round(vMaxPixelValue,4)
print "\tArcScene Z Scale conversion     ", round((vMaxPixelValue/vColorMapFileColors),6)
print "\tDay or Month with maximum value ", vDayMonthMax
print "\tProcess Acomplished              (dt = ", round(vTimeEnd - vTimeStart,1) , "sec(s) or" , round((vTimeEnd - vTimeStart)/60,1) , "min(s))"
vExit = raw_input("\n%s Press Enter to Exit" %(rtg.systemprompt()))
