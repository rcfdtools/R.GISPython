# -*- coding: UTF-8 -*-
# https://openweathermap.org/

# Libraries
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import matplotlib as mpl

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=8)
mpl.rc('axes', titlesize=8)
mpl.use("Agg")  # Prevent the error: Fail to create pixmap with Tk_GetPixmap in TkImgPhotoInstanceSetSize

# Variables
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
fileNameCNE = 'CNE_IDEAM'
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
graphTransparency = 0.75 # Save color for paper print versions, 1 for full color. Doesn't apply for pie charts
plotParameters = [  # Parameter, metric system unit, imperial system unit
                  ('Clouds', '%', '%'),
                  ('Dewpoint', '°C', '°F'),
                  ('Feelslike', '°C', '°F'),
                  ('Humidity', '%', '%'),
                  ('Pressure', 'hPa', 'hPa'),
                  ('Rain', 'mm', 'mm'),
                  ('Temp', '°C', '°F'),
                  ('UVI', 'DN', 'DN'),
                  ('Visibility', 'm', 'm'),
                  ('Windgust', 'm/s', 'm/s'),
                  ('Windspeed', 'm/s', 'm/s'),]
unitSys = 'metric'  # '' for default, 'metric' or 'imperial'
showGraphScreen = False

# Collection data analysis from CSV file
dataFrameCSV = pd.read_csv(filePath+'/Output/'+fileCSV, encoding='ISO-8859-1')
print('\n### Collection data analysis\n'
      '\n* Dataframe type: '+str(type(dataFrameCSV)),
      '\n* Records: ' + str(dataFrameCSV.shape[0]) +
      '\n* Attributes: ' + str(dataFrameCSV.shape[1]))
print('\n#### General CSV information\n')
print(dataFrameCSV.info())
print('\n')
print('\n### Plot hourly graph')
stationList = dataFrameCSV['Station'].unique()
for i in stationList:
    for parameter in plotParameters:
        dataFrameCSVFilter = dataFrameCSV[dataFrameCSV['Station'] == i]
        plotFile = filePath + '/Graph/' + fileNameCNE + '_Station' + str(i) + '_OWM_' + parameter[0] + '_' + currentDateTxt + '.png'
        print('Hourly graph - ' + str(i) + ': ' + plotFile)
        mainArray = dataFrameCSVFilter[
            ['Station', 'Statname', 'Clouds', 'Dewpoint', 'Feelslike', 'Humidity', 'Pressure', 'Rain', 'Temp', 'UVI', 'Visibility', 'Windgust', 'Windspeed', 'Hour', 'Datetime']]
        #print(dataFrameCSVFilter['Datetime'])
        #print(mainArray)
        if unitSys == 'metric':
            ylabelvar = parameter[0] + ', ' + parameter[1]
        else:
            ylabelvar = parameter[0] + ', ' + parameter[2]
        plotTitle = 'Station ' + str(i)
        plotLine = mainArray.plot.line(xlabel='Hour', ylabel=ylabelvar ,  x='Hour', y=parameter[0],title=plotTitle, figsize=(5, 4), c='k', grid=False, marker=".", markersize=8, alpha=graphTransparency)
        plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
        plt.yticks(rotation=0)
        plt.xticks(rotation=90)
        #plt.xlim(0, 23)
        plt.xticks(np.arange(0, 24, 1.0))
        plt.savefig(plotFile)
        if showGraphScreen == True: plt.show()
        plt.close('all')