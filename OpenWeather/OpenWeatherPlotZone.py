# This script is use for plot the scatter plot graph from all the stations

# Libraries
import OpenWeatherSetup as ows
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning
mpl.rc('font', size=10)
mpl.rc('axes', titlesize=10)
sns.set_style('white')  # darkgrid, whitegrid, dark, white, ticks

# Print in Markdown format
def printmd(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputMarkdown.write(txtPrint + '\n')

# Variables
dataFrameCSV = pd.read_csv(ows.filePath+'/Output/'+ows.fileCSV, encoding='ISO-8859-1')
fileNameMd = ows.fileNameCNE + '_OWM_Zonal_' + ows.currentDateTxt + '.md'
fileOutputMarkdownName = ows.filePath + '/Output/' + fileNameMd
fileOutputMarkdown = open(fileOutputMarkdownName, 'w+')
#dataFrameCSV['HourA'] = dataFrameCSV.Datetime.dt.hour
#dataFrameCSV.dropna(inplace=True)
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

# General information
printmd('\n## ' + ows.mainTitle + ' - Zonal Analysis'
        '\n\n* Study case: ' + ows.studyCase +
        '\n* File: ' + ows.fileCSV +
        '\n* Type: ' + str(type(dataFrameCSV)) +
        '\n* Shape: ' + str(dataFrameCSV.shape))
#print('\nDataframe info: '+ str(dataFrameCSV.info()))
#print('\nRecords sample\n %s' %(str(dataFrameCSV.head())))

# Plot vars with geographic location
#sns.set(rc={'figure.figsize': (6, 6)})
printmd('\n\n### Rel plots Latitude vs. Longitude Maps')
for i in ows.plotParameters:
    if ows.unitSys == 'metric':
        units = i[0] + ' (' + i[1] + ')'
    else:
        units = i[0] + ' (' + i[2] + ')'
    plotName = ows.fileNameCNE + '_RelPlotMap_OWM_' + i[0] + '_' + ows.currentDateTxt + '.png'
    plotFile = ows.filePath + '/Graph/' + plotName
    plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
    # sns.relplot(x=i[0], y=i[1], hue=i[2], col=i[3], palette=i[4], data=dataFrameCSV)
    #sns.relplot(x=i[0], y=i[1], hue=i[2], col='Hour', palette=i[4], col_wrap=4, height=5, aspect=8/8, data=dataFrameCSV)
    sns.relplot(x='Longitude', y='Latitude', hue=i[0], col='Hour', palette=i[3], col_wrap=4, height=2, data=dataFrameCSV)
    #plt.title('Stations Map for ' + i[2])
    #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
    plt.savefig(plotFile)
    if showPlot: plt.show()
    printmd('\n#### Map - ' + units )
    printmd('![%s](%s)' % (plotName, plotFileGitHub))

'''
# Plot confidence vars
for i in plotConfidence:
    for h in plotConfidenceHue:
        #sns.lineplot(x=dataFrameCSV.Hour, y=i[1], data=dataFrameCSV, hue=h)
        sns.relplot(data=dataFrameCSV, x='Hour', y=i[1], col='Status', hue=h, kind='line')
        #plt.title(i[0])
        plt.xticks(np.arange(0, 24, 1.0))
        #plt.grid(color='lightgray', linestyle='-', linewidth=0.25)
        if showPlot: plt.show()


#sns.relplot(x='Temp', y='Humidity', hue='Humidity', col='Hour', palette='viridis_r', col_wrap=4, height=2, data=dataFrameCSV)

#sns.kdeplot(x=dataFrameCSV.Latitude, y=dataFrameCSV.Longitude, shade=True, cbar=True)
#showPlot: plt.show()
'''

# JointPlots
iAux, jAux = 0, 0 # Variables for not repeat previous pair plots, p.ej, Temp vs. Clouds is the same as Clouds vs. Temp.
printmd('\n\n### Joint plots')
for i in ows.plotParameters:
    for j in ows.plotParameters:
        if i != j and jAux >= iAux:
            plotName = ows.fileNameCNE + '_JointPlot_OWM_' + i[0] + '_' + j[0] + '_' + ows.currentDateTxt + '.png'
            plotFile = ows.filePath + '/Graph/' + plotName
            plotFileGitHub = ows.urlGitHub + '/Graph/' + plotName
            if ows.unitSys == 'metric':
                xlabel = i[0] + ' (' + i[1] + ')'
                ylabel = j[0] + ' (' + j[1] + ')'
            else:
                xlabel = i[0] + ' (' + i[2] + ')'
                ylabel = j[0] + ' (' + j[2] + ')'
            g = sns.jointplot(data=dataFrameCSV, x=i[0], y=j[0], hue='Hour', palette='autumn', height=8, space=0, ratio=5)
            g.set_axis_labels(xlabel=xlabel, ylabel=ylabel, fontsize=11)
            plt.savefig(plotFile)
            if showPlot: plt.show()
            printmd('\n#### ' + xlabel + ' vs. ' + ylabel)
            printmd('![%s](%s)' %(plotName, plotFileGitHub))
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