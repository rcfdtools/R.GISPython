# https://openweathermap.org/

# Libraries
#import keyword
import os
import requests
import json
import pandas as pd
from pprint import pprint
from datetime import timezone
from datetime import datetime
import matplotlib as mpl
from datetime import date

# Markdown header separator table function
def tableseparatormarkdown(n=2):
    lineSep = '|---'
    printmd(lineSep * n + '|', False)

# Print in CSV format
def printcsv(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputCNEWeather.write(txtPrint + '\n')

# Print in Markdown format
def printmd(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileOutputMarkdown.write(txtPrint + '\n')

# Variables
currentDateTime = datetime.now()  # datetime.utcnow()
unitValMetric = [  # Parameter, unit, openweathermap name.
    ('Temperature', '°C', 'temp'),
    ('Feels like', '°C', 'feels_like'),
    ('Clouds', '%', 'clouds'),
    ('Humidity', '%', 'humidity'),
    ('Pressure', 'hPa', 'pressure'),
    ('Wind Direction', '°', 'wind_deg'),
    ('Wind Speed', 'm/s', 'wind_speed'),
    ('Wind Gust', 'm/s', 'wind_gust'),
    ('Rain', 'mm', 'rain'),
    ('Visibility','m', 'visibility'),
    ('UV Index','DN', 'uvi')]
unitValImperial = [
    ('Temperature', '°F', 'temp'),
    ('Feels like', '°F', 'feels_like'),
    ('Clouds', '%', 'clouds'),
    ('Humidity', '%', 'humidity'),
    ('Pressure', 'hPa', 'pressure'),
    ('Wind Direction', '°', 'wind_deg'),
    ('Wind Speed', 'mi/h', 'wind_speed'),
    ('Wind Gust', 'mi/h', 'wind_gust'),
    ('Rain','mm', 'rain'),
    ('visibility','m', 'visibility'),
    ('UV Index','DN', 'uvi')]
apiKey = 'b53cede1d6b83b6a7800cf923dfe9396'  # For r.cfdtools@gmail.com
latDD = 5.027451  # Set latitude in decimals degrees using period
lonDD = -73.996917  # Set longitude in decimals degrees using period
excludeVal = 'minutely,alerts'  # current,minutely,hourly,daily,alerts
unitSys = 'metric'  # '' for default, 'metric' or 'imperial'
urlFileCNE = 'http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls'
fileNameCNE = 'CNE_IDEAM'
fileExtensionCNE = '.xls'
stationCodeCNE = 'CODIGO'
stationNameCNE = 'nombre'
latitudeCNE = 'latitud'
longitudeCNE = 'longitud'
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
daysBefore = 1  # Max to 4 days, current day count like a part of 5 days in openweather
printDetail = False
showHistorical = False  # True for use the timemachine. False for get the current forecast
showYesterday = True

# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Downloading and reading the CNE file
fileDownloadText = 'File downloaded and updated = No'
fileRequest = requests.get(urlFileCNE)
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileSaveCNE = filePath+'/Data/'+fileNameCNE+'_'+currentDateTxt+fileExtensionCNE
fileOutputCNEWeather = open(filePath+'/Output/'+fileNameCNE+'_OWM_'+currentDateTxt+'.csv', 'w+')
fileOutputMarkdown = open(filePath+'/Output/'+fileNameCNE+'_OWM_'+currentDateTxt+'.md', 'w+')
if fileRequest:
    if os.path.isfile(fileSaveCNE) == False:
        open(fileSaveCNE, 'wb').write(fileRequest.content)
        fileDownloadText = 'File downloaded and updated = Yes'
stationTableCNE = pd.read_excel(fileSaveCNE, index_col=0, sheet_name='CNE')
pd.set_option('display.max_rows', stationTableCNE.shape[0]+1)  # Show all the records
pd.set_option('display.max_columns', None)  # Show all the records

# Print units system
unitVal = ''
if unitSys == 'metric':
    unitVal = unitValMetric
else:
    unitVal = unitValImperial
print('\n ### Unit system (%s)\n' %(unitSys))
print('| Parameter | Unit | openweathermap name |')
tableseparatormarkdown(3)
for i in unitVal:
    print('| %s | %s | %s |' % (i[0],i[1],i[2]))
print('\n> mi: Miles unit for imperial system')
print('\n> DN: Dimensionless numbers')


# Show CNE records and weather values
timeStampVal = int(currentDateTime.replace(tzinfo=timezone.utc).timestamp())
print('\nWeather values for each CNE starion from https://openweathermap.org\n')
print('Current date time: ' + str(currentDateTime))
print('Unix time to eval: ' + str(timeStampVal))
print('Show historical: ' + str(showHistorical))
print('Show yesterday: ' + str(showYesterday))
if showYesterday: timeStampVal -= 86400 * daysBefore
#numStationsCNE = stationTableCNE.shape[0]
numStationsCNE = 3
print('\n## Estaciones encontradas\n')
print('Stations: %i\nAttributes: %i' %(numStationsCNE, stationTableCNE.shape[1]))
geoArrayCNE = stationTableCNE[[stationCodeCNE, stationNameCNE, latitudeCNE, longitudeCNE]]
printcsv(
    'station,name,lat,lon,timezone,date,time,clouds,dewpoint,feelslike,humidity,pressure,rain,temp,uvi,visibility,winddeg,windgust,windspeed,julian',
    False)
for i in range(1, numStationsCNE):
    print('\n%s Getting values for station %s: %s' % (str(i).zfill(5), str(geoArrayCNE[stationCodeCNE][i]).zfill(12), str(geoArrayCNE[stationNameCNE][i])))
    if showHistorical:
        url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%f&lon=%f&dt=%i&units=%s&appid=%s' % (geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], timeStampVal, unitSys, apiKey)
    else:
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%f&lon=%f&&units=%s&appid=%s' % (latDD, lonDD, unitSys, apiKey)
    print('URL: ' + url)
    response = requests.get(url)
    data = json.loads(response.text)
    '''
    print('Type: ' + str(type(data)))
    print('\nPrimary keys:')
    for i in data:
        print('  '+str(i))
    if printDetail:
        print('\nCurrent data:')
        pprint(data)  # General print
    print('\nGet values')
    print('Temperature at same today time: ' + str(data['current']['temp']))
    '''
    # CSV conversion
    hourly = data['hourly']
    printmd('\n| station | name | lat | lon | timezone | date | time | clouds | dewpoint | feelslike | humidity | pressure | rain | temp | uvi | visibility | winddeg | windgust | windspeed | julian |', True)
    tableseparatormarkdown(20)
    for entry in hourly:
        if 'rain' in entry:
            rain = entry['rain']['1h']
        else:
            rain = ''
        txtPrintCSV = '%s,"%s",%f,%f,%s,%s,%f,%f,%f,%f,%f,%s,%f,%f,%f,%f,%f,%f,%s' % (str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y/%m/%d,%H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], entry['wind_gust'], entry['wind_speed'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
        printcsv(txtPrintCSV, False)
        txtPrintMd = '| %s | "%s" | %f | %f | %s | %s | %f | %f | %f | %f | %f | %s | %f | %f | %f | %f | %f | %f | %s |' % (str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y/%m/%d | %H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], entry['wind_gust'], entry['wind_speed'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
        printmd(txtPrintMd, True)

# References
# https://openweathermap.org/guide
# https://towardsdatascience.com/develop-your-weather-application-with-python-in-less-than-10-lines-6d092c6dcbc9
# https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timeStamp
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://realpython.com/python-json/
# https://knasmueller.net/using-the-open-weather-map-api-with-python
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
# https://stackoverflow.com/questions/3327946/how-can-i-get-the-current-time-now-in-utc
# https://pynative.com/python-check-if-key-exists-in-json-and-iterate-the-json-array/