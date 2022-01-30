# This script is use for plot the scatter plot graph from all the stations
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from datetime import date
import OpenWeatherSetup as ows

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=10)
mpl.rc('axes', titlesize=10)

# Variables
dataFrameCSV = pd.read_csv(ows.filePath+'/Output/'+ows.fileCSV, encoding='ISO-8859-1')
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
plotConfidence = [['Clouds - Confidence', 'Clouds'],
                  ['Dew point - Confidence', 'Dewpoint'],
                  ['Temperature - Confidence', 'Temp'],
                  ['Feels like - Confidence', 'Feelslike'],
                  ['Humidity - Confidence', 'Humidity'],
                  ['Pressure - Confidence', 'Pressure'],
                  ['Rain - Confidence', 'Rain'],
                  ['UVI - Confidence', 'UVI'],
                  ['Visibility - Confidence', 'Visibility'],
                  ['Winddeg - Confidence', 'Winddeg'],
                  ['Windgust - Confidence', 'Windgust'],
                  ['Windspeed - Confidence', 'Windspeed']]
plotConfidenceHue = ['Category', 'Technology', 'State', 'County', 'Operator', 'AHName', 'SZName', 'SZHName']
showPlot = False

print(ows.fileCSV)
print(dataFrameCSV.info())
print('Type: %s' %(type(dataFrameCSV)))
print('Shape: %s' %(str(dataFrameCSV.shape)))
print('Records sample\n %s' %(str(dataFrameCSV.head())))
#sns.relplot(x='Longitude', y='Latitude', col='SZName', hue='Elevation', data=dataFrameCSV)
# Plot vars with geographic location
sns.set_style('white')  # darkgrid, whitegrid, dark, white, ticks
#sns.set(rc={'figure.figsize': (6, 6)})
'''
for i in plotXY:
    # sns.relplot(x=i[0], y=i[1], hue=i[2], col=i[3], palette=i[4], data=dataFrameCSV)
    #sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=5, aspect=8/8, data=dataFrameCSV)
    sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=2, data=dataFrameCSV)
    #plt.title('Stations Map for ' + i[2])
    #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    if showPlot: plt.show()

# Plot confidence vars
for i in plotConfidence:
    for h in plotConfidenceHue:
        #sns.lineplot(x=dataFrameCSV.Hour, y=i[1], data=dataFrameCSV, hue=h)
        sns.relplot(data=dataFrameCSV, x='Hour', y=i[1], col='Status', hue=h, kind='line')
        #plt.title(i[0])
        plt.xticks(np.arange(0, 24, 1.0))
        #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
        if showPlot: plt.show()
'''

#sns.relplot(x='Temp', y='Humidity', hue='Humidity', col='Hour', palette='viridis_r', col_wrap=4, height=2, data=dataFrameCSV)

#sns.kdeplot(x=dataFrameCSV.Latitude, y=dataFrameCSV.Longitude, shade=True, cbar=True)
#showPlot: plt.show()

# JointPlots
iAux, jAux = 0, 0 # Variables for not repeat previous pair plots, p.ej, Temp vs. Clouds is the same as Clouds vs. Temp.
print('\n### Joint plots')
for i in ows.plotParameters:
    for j in ows.plotParameters:
        if i != j and jAux >= iAux:
            if ows.unitSys == 'metric':
                xlabel = i[0] + ' (' + i[1] + ')'
                ylabel = j[0] + ' (' + j[1] + ')'
            else:
                xlabel = i[0] + ' (' + i[2] + ')'
                ylabel = j[0] + ' (' + j[2] + ')'
            g = sns.jointplot(data=dataFrameCSV, x=i[0], y=j[0], hue='Hour', palette='autumn', height=8, space=0, ratio=5)
            g.set_axis_labels(xlabel=xlabel, ylabel=ylabel, fontsize=11)
            plotName = ows.fileNameCNE + '_JointPlot_OWM_' + i[0] + '_' + j[0] + '_' + ows.currentDateTxt + '.png'
            plotFile = ows.filePath + '/Graph/' + plotName
            plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
            plt.savefig(plotFile)
            if showPlot: plt.show()
            print('\n#### ' + xlabel + ' vs. ' + ylabel)
            print('![%s](%s)' %(plotName, plotFileGitHub))
            #print('Plotting ' + plotName)
        jAux += 1
    iAux += 1
    jAux = 0


print('\n{R} Process completed.')
# References
# Introduction to Seaborn | How seaborn Python works with matplotlib along with seaborn and pandas
# https://www.youtube.com/watch?v=vaf4ir8eT38
# https://seaborn.pydata.org/tutorial/color_palettes.html
# Seaborn Color Palette Basics | Using named and custom color palettes in Python seaborn
# https://www.youtube.com/watch?v=2wRHBodrWuY
# sns.lineplot >> https://www.youtube.com/watch?v=CMRVEKf9jWA
# https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot