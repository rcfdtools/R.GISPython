# This script is use for plot the scatter plot graph from all the stations
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from datetime import date

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=10)
mpl.rc('axes', titlesize=10)

# Variables
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
fileNameCNE = 'CNE_IDEAM'
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
dataFrameCSV = pd.read_csv(filePath+'/Output/'+fileCSV, encoding='ISO-8859-1')
#dataFrameCSV['HourA'] = dataFrameCSV.Datetime.dt.hour
#dataFrameCSV.dropna(inplace=True)
plotXY = ( # x, y, hue, col, palette
            ['Longitude', 'Latitude', 'Clouds', 'Status', 'light:k'],
            ['Longitude', 'Latitude', 'Dewpoint', 'Status', 'viridis_r'],
            ['Longitude', 'Latitude', 'Temp', 'Status', 'viridis_r'],
            ['Longitude', 'Latitude', 'Feelslike', 'Status', 'viridis_r'],
            ['Longitude', 'Latitude', 'Humidity', 'Status', 'light:b'],
            ['Longitude', 'Latitude', 'Pressure', 'Status', 'light:k'],
            ['Longitude', 'Latitude', 'Rain', 'Status', 'Blues'],
            ['Longitude', 'Latitude', 'UVI', 'Status', 'viridis_r'],
            ['Longitude', 'Latitude', 'Visibility', 'Status', 'light:k'],
            ['Longitude', 'Latitude', 'Winddeg', 'Status', 'Spectral'],
            ['Longitude', 'Latitude', 'Windgust', 'Status', 'YlOrBr'],
            ['Longitude', 'Latitude', 'Windspeed', 'Status', 'YlOrBr'])
plotConfidence = [['Clouds - Confidence', dataFrameCSV.Clouds],
                  ['Dew point - Confidence', dataFrameCSV.Dewpoint],
                  ['Temperature - Confidence', dataFrameCSV.Temp],
                  ['Feels like - Confidence', dataFrameCSV.Feelslike],
                  ['Humidity - Confidence', dataFrameCSV.Humidity],
                  ['Pressure - Confidence', dataFrameCSV.Pressure],
                  ['Rain - Confidence', dataFrameCSV.Rain],
                  ['UVI - Confidence', dataFrameCSV.UVI],
                  ['Visibility - Confidence', dataFrameCSV.Visibility],
                  ['Winddeg - Confidence', dataFrameCSV.Winddeg],
                  ['Windgust - Confidence', dataFrameCSV.Windgust],
                  ['Windspeed - Confidence', dataFrameCSV.Windspeed]]
showPlot = True

print(fileCSV)
print(dataFrameCSV.info())
print('Type: %s' %(type(dataFrameCSV)))
print('Shape: %s' %(str(dataFrameCSV.shape)))
print('Records sample\n %s' %(str(dataFrameCSV.head())))
#sns.relplot(x='Longitude', y='Latitude', col='SZName', hue='Elevation', data=dataFrameCSV)
# Plot vars with geographic location
sns.set_style('white')  # darkgrid, whitegrid, dark, white, ticks
#sns.set(rc={'figure.figsize': (6, 6)})
#'''
for i in plotXY:
    # sns.relplot(x=i[0], y=i[1], hue=i[2], col=i[3], palette=i[4], data=dataFrameCSV)
    #sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=5, aspect=8/8, data=dataFrameCSV)
    sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=2, data=dataFrameCSV)
    #plt.title('Stations Map for ' + i[2])
    #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    if showPlot: plt.show()
#'''
# Plot confidence vars
for i in plotConfidence:
    sns.lineplot(x=dataFrameCSV.Hour, y=i[1], data=dataFrameCSV, hue='AHName')
    plt.title(i[0])
    plt.xticks(np.arange(0, 24, 1.0))
    plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    if showPlot: plt.show()

# References
# Introduction to Seaborn | How seaborn Python works with matplotlib along with seaborn and pandas
# https://www.youtube.com/watch?v=vaf4ir8eT38
# https://seaborn.pydata.org/tutorial/color_palettes.html
# Seaborn Color Palette Basics | Using named and custom color palettes in Python seaborn
# https://www.youtube.com/watch?v=2wRHBodrWuY
# sns.lineplot >> https://www.youtube.com/watch?v=CMRVEKf9jWA
# https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot