# iamr.knowhow@gmail.com
# Tested in Python 2.7.12
# CSV FILES PROCESS MODULES v0.0

import numpy as np

# System prompt
def systemprompt():
    systemprompt = "{R} "
    return systemprompt


# OPTION RANGE FOR INTEGER OR LIST VALUES
def fOptionRange(vMsg,vMinOpt,vMaxOpt):
    vVal = 0
    while vVal == 0:
        vValueUser = raw_input("\n%s %s (%d/%d) >> " %(systemprompt(), vMsg, vMinOpt, vMaxOpt))
        if type(vValueUser) != int:
            try:
                vValueUser = int(vValueUser)
                if vValueUser >= vMinOpt and vValueUser <= vMaxOpt:
                    print "\tOption entry is %d." %(vValueUser)
                    vVal = 1
                else:
                    print "%s Atention, value out of range (%d-%d)." %(systemprompt(),vMinOpt, vMaxOpt)
            except:
                #print "%s Atention, invalid value. Enter an integer value." %(systemprompt())
                vExcept = 0
    return vValueUser


# OPTION RANGE FOR FLOAT VALUES IN A RANGE
# For example for grid resolutions
def fOptionRangeFloat(vMsg,vMinOpt,vMaxOpt):
    vVal = 0
    while vVal == 0:
        vValueUser = raw_input("%s %s (%d/%d) >> " %(systemprompt(), vMsg, vMinOpt, vMaxOpt))
        if type(vValueUser) != float:
            try:
                vValueUser = float(vValueUser)
                if vValueUser >= vMinOpt and vValueUser <= vMaxOpt:
                    print "\tOption entry is %f." %(vValueUser)
                    vVal = 1
                else:
                    print "%s Atention, value out of range (%d-%d)." %(systemprompt(),vMinOpt, vMaxOpt)
            except:
                #print "%s Atention, invalid value. Enter an integer value." %(systemprompt())
                vExcept = 0
    return vValueUser


# OPTION YES/NO
def fOptionYesNo(vMsg):
    vVal = 0
    while vVal == 0:
        vValueUser = raw_input("%s %s (y/n) >> " %(systemprompt(), vMsg))
        if type(vValueUser) == str:
            vValueUserlow = vValueUser.lower()
            if vValueUserlow == "y" or vValueUserlow == "n": 
                vVal = 1
            else:
                print "\tOption %s invalid. Try again.\n" %(vValueUser)
    print "\tOption entry is %s.\n" %(vValueUser)
    return vValueUser.lower()


# TOTAL FIELDS FOUND INTO A CSV FILE
# vFileName: Complete File name to process
def fCSVTotalFieldFound(vFileName):
    vFile = open (vFileName)
    vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
    vRegisterArray = vRegister.split(",")
    vFields = len(vRegisterArray)
    print "\t%d Atributes fields found." %(vFields)
    vFile.close()
    return vFields


# TOTAL RECORDS FOUND
# vFileName: Complete File name to process
def fCSVTotalRecordFound(vFileName):
    vFile = open (vFileName) #Open only for reading
    vRowTotal = len(open(vFileName).readlines())
    if vRowTotal == 0:
        print "\tNo records found."
    else:
        print "\t%d records found." %(vRowTotal-1)
    vRowTotal -= 1
    vFile.close()
    return vRowTotal


# SPATIAL DOMAIN AND GRID SIZE RECOMMENDED
# vFileName: Complete File name to process
def fCSVSpacialDomain(vFileName):
    print "\t-----------------------"
    print "\tSTATION SPATIAL DOMAIN"
    print "\t-----------------------"
    vFields = fCSVTotalFieldFound(vFileName)
    vFile = open (vFileName) #Open only for reading
    vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line #Read de header line
    vRegisterArray = vRegister.split(",")
    #Eval column number with CX Values
    vCXNum, vCYNum = -1, -1
    for vInc0 in range (0,vFields):
        if vRegisterArray[vInc0].upper() == "CX":
            vCXNum = vInc0
            print "\tCX Field number is:",(vCXNum+1)
        elif vRegisterArray[vInc0].upper() == "CY":
            vCYNum = vInc0
            print "\tCY Field number is:",(vCYNum+1)
    if vCXNum == -1 or vCYNum == -1:
        print "\tAlert: Cy or CY fiends not found"
    vRowTotal = len(open(vFileName).readlines())
    if vRowTotal == 0:
        print "\tNo records found."
    else:
        print "\t%d records found." %(vRowTotal-1)
    vRowTotal -= 1
    vCYMax, vCYMin, vCXMax, vCXMin = 0, 1e99, 0, 1e99
    for vInc in range (0,vRowTotal):
        vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
        vRegisterArray = vRegister.split(",")
        if vRegisterArray[vCXNum] != "\n" and vRegisterArray[vCXNum] != "" and vRegisterArray[vCYNum] != "\n" and vRegisterArray[vCYNum] != "":
            if float(vRegisterArray[vCXNum]) > vCXMax: vCXMax = float(vRegisterArray[vCXNum])
            if float(vRegisterArray[vCXNum]) < vCXMin: vCXMin = float(vRegisterArray[vCXNum])
            if float(vRegisterArray[vCYNum]) > vCYMax: vCYMax = float(vRegisterArray[vCYNum])
            if float(vRegisterArray[vCYNum]) < vCYMin: vCYMin = float(vRegisterArray[vCYNum])
    vSpatialDomainWidth = vCXMax - vCXMin
    vSpatialDomaintHeigh = vCYMax - vCYMin
    if vSpatialDomainWidth > vSpatialDomaintHeigh:
        vGridCellSizeRecommended = vSpatialDomaintHeigh / 150 #Divide minor value into 150 pixels
    else:
        vGridCellSizeRecommended = vSpatialDomainWidth / 150 #Divide minor value into 150 pixels    
    print "\tCX Max: %f \tCX Min: %f \tWidth: %f" %(vCXMax, vCXMin, vSpatialDomainWidth)
    print "\tCY Max: %f \tCY Min: %f \tHeigh: %f" %(vCYMax, vCYMin, vSpatialDomaintHeigh)
    print "\tRecommended grid size:",vGridCellSizeRecommended
    print ""
    vFile.close()
    return (vSpatialDomainWidth, vSpatialDomaintHeigh, vGridCellSizeRecommended)


# PREVIEW RECORDS
# vFileName: Complete File name to process
# vRowTotal: Total rows in the file
def fCSVPreviewRecord(vFileName,vRowTotal):
    vFile = open (vFileName)
    vCSVNumRecordPreview = fOptionRange("Input number of preview records to see with header",0,vRowTotal)
    print "\n\t---------------------------------------"
    print "\tPREVIOUS DATAFILE CONTENTS (%d records)" %(vCSVNumRecordPreview)
    print "\t---------------------------------------"
    for vInc0 in range(0,vCSVNumRecordPreview):
        vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
        vRegisterArray = vRegister.split(",")
        print "\t("+(str(vInc0+1).zfill(5))+")",vRegisterArray
    print ""
    vFile.close()  


# DATA DAILY OR MONTHLY
def fDataFrecuency():
    lDataFrecuency = np.array([
        (1,366,"Dayly","Julian"),
        (2,12,"Monthly","Month")])
    lDataFrecuencyCount = len(lDataFrecuency)
    print "\tFrecuencies:",lDataFrecuencyCount
    print "\t--------------------------------------"
    print "\tID    Max Val Frecuency Field Required"
    print "\t--------------------------------------"
    for vInc0 in range (0,lDataFrecuencyCount):
        print "\t",(lDataFrecuency[vInc0,0]).zfill(2),"  ",(lDataFrecuency[vInc0,1].zfill(4)),"  ",lDataFrecuency[vInc0,2],"\t",lDataFrecuency[vInc0,3]
    vDataFrecuencyOpt = fOptionRange("Frecuency to use",1,(lDataFrecuencyCount))
    vFrecuenciaMaxVal = lDataFrecuency[(vDataFrecuencyOpt-1),1]
    vFrecuenciaField = lDataFrecuency[(vDataFrecuencyOpt-1),3]
    return (vFrecuenciaMaxVal,vFrecuenciaField)


# COORDINATES SYSTEM
def fCoordSystem():
    lCoordSystem = np.array([
        (1,"WGS-1984","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"),
        (2,"GAUSS - BOGOTA - MAGNA","PROJCS['GAUSS_BTA_MAGNA',GEOGCS['CGS_SIRGAS',DATUM['CGS_SIRGAS',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1000000.0],PARAMETER['False_Northing',1000000.0],PARAMETER['Central_Meridian',-74.077507917],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',4.596200417],UNIT['Meter',1.0]];-4623200 -9510300 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision")])
    lCoordSystemCount = len(lCoordSystem)
    print "\n\tCoordinate Systems:",lCoordSystemCount
    print "\t--------------------------------------"
    print "\tID    Coordinate System"
    print "\t--------------------------------------"
    for vInc0 in range (0,lCoordSystemCount):
        print "\t",(lCoordSystem[vInc0,0]).zfill(2),"  ",(lCoordSystem[vInc0,1].zfill(4))
    vCoordSystemOpt = fOptionRange("Coordinate system to use",1,(lCoordSystemCount))
    vCoordSystemVal = lCoordSystem[(vCoordSystemOpt-1),2]
    print "\n",vCoordSystemVal,"\n"
    return (vCoordSystemVal)


# HEADERS
# vFileName: Complete File name to process
# vRowTotal: Total rows in the file
# vRowTotal: Total fields in the file
def fCSVHeader(vFileName,vRowTotal,vFields):
    vFile = open (vFileName)
    vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
    vRegisterArray = vRegister.split(",")
    print "\tHEADERS FOUND ON DATAFILE"
    print "\t--------------------------"
    print "\t #  Field Name"
    print "\t--------------------------"
    for vInc1 in range(0,vFields):
        print "\t("+(str(vInc1+1).zfill(2))+")",vRegisterArray[vInc1]
    vFieldNumberEval = fOptionRange("Field number to eval",1,vFields)
    vFieldEvalStr = vRegisterArray[vFieldNumberEval-1]
    vFile.close()
    print "\tVariable in use is ["+vFieldEvalStr+"]\n"
    return (vFieldNumberEval,vFieldEvalStr)


# STATISTICS
# vFileName: Complete File name to process
# vRowTotal: Total rows in the file
# vFieldNumberEval: Column field number to eval
def fCSVStatistic(vFileName,vRowTotal,vFieldNumberEval):
    print "\t--------------------------"
    print "\tSTATISTICS"
    print "\t--------------------------"
    vFile = open (vFileName)
    vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
    vSum = 0
    vMax = -1e-99
    vMin = 1e99
    vCount = 0
    for i in range(0,vRowTotal):
        vRegister = vFile.readline().rstrip('\n') #rstrip remove jump line
        vRegisterArray = vRegister.split(",")
        #print "\tVar ",i," ",vRegisterArray[vFieldNumberEval-1]
        if vRegisterArray[vFieldNumberEval-1] != "\n" and vRegisterArray[vFieldNumberEval-1] != "":
            vCount +=1
            # Eval Total
            vSum += float(vRegisterArray[vFieldNumberEval-1])
            # Eval Maximum
            if float(vRegisterArray[vFieldNumberEval-1]) > vMax:
                vMax = float(vRegisterArray[vFieldNumberEval-1])
            # Eval Minimum
            if float(vRegisterArray[vFieldNumberEval-1]) < vMin:
                vMin = float(vRegisterArray[vFieldNumberEval-1])      
    vAverage = vSum/vCount
    vNulls = vRowTotal-vCount
    print "\tRegs:\t",vRowTotal
    print "\tCount:\t",vCount,"(Not nulls)"
    print "\tNulls:\t",vNulls
    print "\tMax:\t",vMax
    print "\tMin:\t",vMin
    print "\tSum:\t",vSum
    print "\tAvg:\t",vAverage
    print ""
    return (vRowTotal, vCount, vNulls, vMax, vMin, vSum, vAverage)
    vFile.close()


# COLOR MAP STYLES
# vFolderColorMapStyle: Complete folder color map styles path
def fColorMapStyle(vFolderColorMapStyle):
    lColorMapStyle = np.array([
        (0,256,"Grayscale"),
        (1,256,"White - Magenta"),
        (2,256,"White - Red"),
        (3,256,"Cyan - Red"),
        (4,256,"Green - Magenta"),
        (5,256,"Magenta - Green"),
        (6,256,"Purple - Green - Yellow"),
        (7,256,"Green - Light Green - Pink - Dark Pink - Purple (x5)"),
        (8,256,"Green - Light Green - Pink - Dark Pink - Purple (x8)"),
        (9,256,"Lila - Khaki - Blue (x15)"),
        (10,256,"Lila - Khaki - Blue (x13)"),
        (11,256,"Yellow - Pink - Green - Blue"),
        (12,256,"Gray - Aquamarina - Sea Blue"),
        (13,512,"Green Sea - Blue Sea - Purple - Red - Orange - Yellow (x18)"),
        (14,1024,"Dark Pink - Mercury - Lime - Green (x13)")])
    vColorMapStyleCount = len(lColorMapStyle)
    print "\n\tTotal Color Map Styles:",vColorMapStyleCount
    print "\t----------------------------------------------------------------"
    print "\tID   Colors Color Map Style Name"
    print "\t----------------------------------------------------------------"
    for vInc0 in range (0,vColorMapStyleCount):
        print "\t",(lColorMapStyle[vInc0,0]).zfill(2)," ",(lColorMapStyle[vInc0,1].zfill(4))," ",lColorMapStyle[vInc0,2]
    vColorMapFileOpt = fOptionRange("Ramp color number",0,(vColorMapStyleCount-1))
    vColorMapFileColors = lColorMapStyle[vColorMapFileOpt,1]    
    vColorMapFile = vFolderColorMapStyle+"ColorMapArcGIS"+vColorMapFileColors+"_v"+str(vColorMapFileOpt)+".clr"
    vColorMapFilePrev = vFolderColorMapStyle+"ColorMapArcGIS"+vColorMapFileColors+"_v"+str(vColorMapFileOpt)+".jpg"
    print "\n\tColor map file:  ",vColorMapFile
    print "\tColor map sample:",vColorMapFilePrev
    return (vColorMapFile, vColorMapFilePrev, vColorMapFileColors)


# GRAPH VALUES BETWEEN 0 TO MAX VALUE
# vMaxVal: Max val into all data set
# vVal: Value to scale respect max val
def fGraphTxt(vFileName,vRowTotal,vFieldNumberEval):
    vOptionYesNo = fOptionYesNo("Show Text Data Graph Analysis (all records in file)")
    if vOptionYesNo == "y":
        print "\t--------------------------"
        print "\tGRAPH SELECTED VAR",vFieldNumberEval
        print "\t--------------------------"
        vFile = open (vFileName)
        vRegister = vFile.readline().rstrip('\n')
        vMax = -1e-99
        for i in range(0,vRowTotal):
            vRegister = vFile.readline().rstrip('\n')
            vRegisterArray = vRegister.split(",")
            if vRegisterArray[vFieldNumberEval-1] != "\n" and vRegisterArray[vFieldNumberEval-1] != "":
                if float(vRegisterArray[vFieldNumberEval-1]) > vMax:
                    vMax = float(vRegisterArray[vFieldNumberEval-1])
        print "\tMax value: ",vMax
        vFile.close()
        vFile = open (vFileName)
        vRegister = vFile.readline().rstrip('\n')
        for vInc in range (1,vRowTotal+1):
            vRegister = vFile.readline().rstrip('\n')
            vRegisterArray = vRegister.split(",")
            if vRegisterArray[vFieldNumberEval-1] != "\n" and vRegisterArray[vFieldNumberEval-1] != "":
                vVal = float(vRegisterArray[vFieldNumberEval-1])
                #print "\vInc:",vVal
                vBarChar = "|"
                vBarCharMaxChar = 50
                vBarFactorAmpVar = 100
                vBar = ((int(vVal*vBarFactorAmpVar)) * vBarCharMaxChar) / (int(vMax*vBarFactorAmpVar))
                vBarCharMaxCharLess = (vBarCharMaxChar - vBar)
                vBarPorc = vVal * 100 / vMax
                print "\t",(str(vInc).zfill(5)),"["+(vBar*vBarChar)+(vBarCharMaxCharLess*" ")+"] "+str(round(vVal,4)),"of",vMax,"("+str(round(vBarPorc,1))+"%)"
        print ""
        vFile.close()


# GRAPH ONE VALUES BETWEEN 0 TO MAX VALUE
# vMaxVal: Max val into all data set
# vVal: Value to scale respect max val
def fGraphTxtOneValue(vMax, vVal):
    vMax = float(vMax)
    vBarChar = "|"
    vBarCharMaxChar = 50
    vBarFactorAmpVar = 100
    vBar = ((int(vVal*vBarFactorAmpVar)) * vBarCharMaxChar) / (int(vMax*vBarFactorAmpVar))
    vBarCharMaxCharLess = (vBarCharMaxChar - vBar)
    vBarPorc = str(round((vVal * 100) / vMax , 2))
    print "\t["+(vBar*vBarChar)+(vBarCharMaxCharLess*" "),"]",vVal,"of",vMax,"("+vBarPorc+"%)"
