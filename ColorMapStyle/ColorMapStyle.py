
# Libraries
import ColorMapStyleValue as cmsv
from datetime import datetime

# Python rgb color changing text function
def colorrgb(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# Variables
baseRGBColors = cmsv.ColorMapArcGISs13  # Style values from ColorMapStyleValue.py
filePath = r'D:/R.GISPython/ColorMapStyle'  # r'.' for relative path
numColor = 512
styleNumber = 13
fileName = filePath+'/Output/ColorMapArcGIS'+str(numColor)+'s'+str(styleNumber)+'.clr'
urlGitHub = ''
fileColorName = open(fileName, 'w+')
cutRamp = len(baseRGBColors)-1
discreteCutValue = int(numColor / (cutRamp))
moduleEval = numColor % cutRamp
printCutOnScreen = False

# Header
print('\nDate: ' + str(datetime.utcnow()) +
      '\nColors: ' + str(numColor) +
      '\nCuts: ' + str(cutRamp) +
      '\nModule operator: ' + str(numColor%cutRamp) +
      '\nColors per cut: '+ str(discreteCutValue) +
      '\nOutput file: '+ str(fileName) + '\n')

# Calculation
i = 0
iAux = 0
print('#    R   G   B   Sample')
while i < cutRamp:
    redColorFrom = baseRGBColors[i][0]
    redColorTo = baseRGBColors[i+1][0]
    redColorJump = abs((redColorFrom-redColorTo)/discreteCutValue)
    redColorRampValue = redColorFrom
    greenColorFrom = baseRGBColors[i][1]
    greenColorTo = baseRGBColors[i+1][1]
    greenColorJump = abs((greenColorFrom-greenColorTo)/discreteCutValue)
    greenColorRampValue = greenColorFrom
    blueColorFrom = baseRGBColors[i][2]
    blueColorTo = baseRGBColors[i+1][2]
    blueColorJump = abs((blueColorFrom-blueColorTo)/discreteCutValue)
    blueColorRampValue = blueColorFrom
    if printCutOnScreen:
        print('Red color from ' + str(redColorFrom) + ' To ' + str(redColorTo) + ' with ' + str(redColorJump) + ' variation')
        print('Green color from ' + str(greenColorFrom) + ' To ' + str(greenColorTo) + ' with ' + str(greenColorJump) + ' variation')
        print('Blue color from ' + str(blueColorFrom) + ' To ' + str(blueColorTo) + ' with ' + str(blueColorJump) + ' variation')
    for j in range(1, discreteCutValue+1):
        if iAux == numColor-1:
            printTxt = str(iAux).zfill(4) + ' ' + str(int(redColorTo)).zfill(3) + ' ' + str(int(greenColorTo)).zfill(3) + ' ' + str(int(blueColorTo)).zfill(3)
        else:
            printTxt = str(iAux).zfill(4) + ' ' + str(int(redColorRampValue)).zfill(3) + ' ' + str(
                int(greenColorRampValue)).zfill(3) + ' ' + str(int(blueColorRampValue)).zfill(3)
        printSample = ' ■■■■■■■■■■■'
        print(printTxt + colorrgb(int(redColorRampValue), int(greenColorRampValue), int(blueColorRampValue), printSample))
        fileColorName.write(printTxt + '\n')
        if redColorFrom < redColorTo:
            redColorRampValue += redColorJump
            if redColorRampValue > redColorTo:
                redColorRampValue = redColorTo
        else:
            redColorRampValue -= redColorJump
            if redColorRampValue > redColorFrom:
                redColorRampValue = redColorFrom
        if greenColorFrom < greenColorTo:
            greenColorRampValue += greenColorJump
            if greenColorRampValue > greenColorTo:
                greenColorRampValue = greenColorTo
        else:
            greenColorRampValue -= greenColorJump
            if greenColorRampValue > greenColorFrom:
                greenColorRampValue = greenColorFrom
        if blueColorFrom < blueColorTo:
            blueColorRampValue += blueColorJump
            if blueColorRampValue > blueColorTo:
                blueColorRampValue = blueColorTo
        else:
            blueColorRampValue -= blueColorJump
            if blueColorRampValue > blueColorFrom:
                blueColorRampValue = blueColorFrom
        iAux += 1
    if moduleEval >= 1 and iAux < numColor:
        if iAux == numColor-1:
            printTxt = str(iAux).zfill(4) + ' ' + str(int(redColorTo)).zfill(3) + ' ' + str(int(greenColorTo)).zfill(3) + ' ' + str(int(blueColorTo)).zfill(3)
        else:
            printTxt = str(iAux).zfill(4) + ' ' + str(int(redColorRampValue)).zfill(3) + ' ' + str(
                int(greenColorRampValue)).zfill(3) + ' ' + str(int(blueColorRampValue)).zfill(3)
        printSample = ' ■■■■■■■■■■■'
        print(printTxt + colorrgb(int(redColorRampValue), int(greenColorRampValue), int(blueColorRampValue), printSample) + str(i+1) + ' cut')
        fileColorName.write(printTxt + '\n')
        iAux += 1
    i += 1
fileColorName.close()