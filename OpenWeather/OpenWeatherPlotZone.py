# This script is use for plot the scatter plot graph from all the stations
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import date


# Variables
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
fileNameCNE = 'CNE_IDEAM'
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
dataFrameCSV = pd.read_csv(filePath+'/Output/'+fileCSV, encoding='ISO-8859-1')
#dataFrameCSV['HourA'] = dataFrameCSV.Datetime.dt.hour
#dataFrameCSV.dropna(inplace=True)
plotCombo = ( # x, y, hue, col, palette
            ['Longitude', 'Latitude', 'Clouds', 'Status', 'flare'],
            ['Longitude', 'Latitude', 'Dewpoint', 'Status', 'Spectral'],
            ['Longitude', 'Latitude', 'Temp', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'Feelslike', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'Humidity', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'Pressure', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'Rain', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'UVI', 'Status', 'coolwarm'],
            ['Longitude', 'Latitude', 'Visibility', 'Status', 'viridis'],
            ['Longitude', 'Latitude', 'Winddeg', 'Status', 'cubehelix'],
            ['Longitude', 'Latitude', 'Windgust', 'Status', 'cubehelix'],
            ['Longitude', 'Latitude', 'Windspeed', 'Status', 'cubehelix'])
showPlot = False

print(fileCSV)
print(dataFrameCSV.info())
print('Type: %s' %(type(dataFrameCSV)))
print('Shape: %s' %(str(dataFrameCSV.shape)))
print('Records sample\n %s' %(str(dataFrameCSV.head())))
#sns.relplot(x='Longitude', y='Latitude', col='SZName', hue='Elevation', data=dataFrameCSV)
if showPlot:
    for i in plotCombo:
        # sns.relplot(x=i[0], y=i[1], hue=i[2], col=i[3], palette=i[4], data=dataFrameCSV)
        sns.relplot(x=i[0], y=i[1], hue=i[2], palette=i[4], data=dataFrameCSV)
        plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    plt.show()

sns.set_style('dark')
sns.lineplot(dataFrameCSV.Hour, dataFrameCSV.Humidity)
plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
plt.show()

# References
# Introduction to Seaborn | How seaborn Python works with matplotlib along with seaborn and pandas
# https://www.youtube.com/watch?v=vaf4ir8eT38
# https://seaborn.pydata.org/tutorial/color_palettes.html
# Seaborn Color Palette Basics | Using named and custom color palettes in Python seaborn
# https://www.youtube.com/watch?v=2wRHBodrWuY