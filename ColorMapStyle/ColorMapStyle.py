# -*- coding: UTF-8 -*-
# Script name: ColorMapStyle.py, ColorMapStyleValue.py
# Description: Color ramp style generator
# Requirements: PyCharm 2021.3+, ArcGIS 10+, ArcGIS Pro 2.9.0

# Libraries
import ColorMapStyleValue as cmsv
import sys
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

# Python rgb color changing text function
def colorrgb(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# Print titles
def printtitle(titleText, titleType = 'both', showTab = False):
    # titleType: Top, Bottom, both
    nc = '-'
    valLen = len(titleText)
    tabTxt = ''
    if showTab:
        tabTxt = '\t'
    if titleType == 'both':
        print(tabTxt + nc * valLen)
        print(tabTxt + titleText)
        print(tabTxt + nc * valLen)
    elif titleType == 'Top':
        print(tabTxt + nc * valLen)
        print(tabTxt + titleText)
    else:
        print(tabTxt + titleText)
        print(tabTxt + nc * valLen)

def printfloat(n, decimals=3):
    print(f"{n:.{decimals}f}")

# Variables
baseRGBColors = cmsv.ColorMap7  # ✅✅✅ User can change ✅✅✅. Style values from ColorMapStyleValue.py
styleNumber = 7  # ✅✅✅ User can change ✅✅✅
numColor = 1024  # ✅✅✅ User can change ✅✅✅
filePath = r'D:/R.GISPython/ColorMapStyle'  # r'.' for relative path
fileName = 'ColorMapArcGIS'+str(numColor)+'s'+str(styleNumber)
fileNameOutput = filePath+'/Output/'+fileName+'.clr'
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle'
fileColorName = open(fileNameOutput, 'w+')
cutRamp = len(baseRGBColors)-1
discreteCutValue = int(numColor/cutRamp)
moduleEval = numColor % cutRamp
xVal, yVal, pyRBG = [], [], []
rgbSampleResolution = 96
printCutOnScreen = False
printPyRGBOnScreen = True

# Header
printtitle('Color ramp style generator', 'both', False)
print('\nExecution date & time: ' + str(datetime.now()) +
      '\nScript compatibility: Python 3'
      '\nPython version: ' + str(sys.version) +
      '\nPython path: ' + str(sys.path[0:5]) +
      '\nmatplotlib version: ' + str(matplotlib.__version__) +
      '\nRepository: https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle'
      '\nLicense and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License'
      '\nCredits: r.cfdtools@gmail.com\n')

# Parameters
printtitle('General parameters', 'both', False)
print('\nReference style #: ' + str(styleNumber) +
      '\nColors: ' + str(numColor) +
      '\nCuts: ' + str(cutRamp) +
      '\nModule operator: ' + str(numColor % cutRamp) +
      '\nColors per cut: ' + str(discreteCutValue) +
      '\nOutput file: ' + str(fileNameOutput) +
      '\nGitHub: ' + urlGitHub + '/Output/' + str(fileName) + '.clr' +
      '\nGitHub sample: ' + urlGitHub + '/Output/' + str(fileName) + '.png\n')

printtitle('Reference RGB color values')
for i in baseRGBColors:
    print(i)
print('\n')

# Calculation
i = 0
iAux = 0
printtitle('#    R   G   B   Sample')
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
        if iAux < numColor:
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
            pyRBG.append((abs(redColorRampValue / 255.00000001), abs(greenColorRampValue / 255.00000001),
                          abs(blueColorRampValue / 255.00000001)))
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
        pyRBG.append((abs(redColorRampValue / 255.00000001), abs(greenColorRampValue / 255.00000001),
                      abs(blueColorRampValue / 255.00000001)))
        iAux += 1
    i += 1
fileColorName.close()
print('\n')

# Matplotlib sample
printtitle('Matplotlib color style sample')
if printPyRGBOnScreen:
    print('\nPython value conversion')
    print('#    pyR   pyG   pyB')
    iAux = 1
    for i in pyRBG:
        print(str(iAux).zfill(4) + ' ' + (f'{round(i[0],3):.3f}') + ' ' + str(f'{round(i[1],3):.3f}') + ' ' + str(f'{round(i[2],3):.3f}'))
        iAux += 1
for i in range(1,numColor+1):
    xVal.append(-i)
    yVal.append(1)
matplotlib.rcParams.update({'font.size': 8})
plt.figure(figsize=(5, 6), dpi=rgbSampleResolution)
plt.box(False)
plt.xticks([])
plt.title(fileName+'.clr' + '\n' + urlGitHub)
plt.tight_layout(pad=1.5)
plt.yticks([0, -numColor/4, -numColor/2, -numColor*3/4, -numColor])
plt.barh(xVal, yVal, color=pyRBG, height=1, align='center')
plt.savefig(filePath+'/Output/'+fileName+'.png')
plt.show()

