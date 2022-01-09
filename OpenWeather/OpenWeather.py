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
    printmd(lineSep * n + '|', True)

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
    ('Dew Point', '°C', 'dew_point'),
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
    ('Dew Point', '°F', 'dew_point'),
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
csvParameters = [  # Parameter names for the output CSV file: r.cfdtools, IDEAM, OpenWeather.
    ('Station', 'CODIGO', 'N/A', 'Station code'),
    ('Statname', 'nombre', 'N/A', 'Station name'),
    ('Latitude', 'latitud', 'lat', 'Geolocalitation latitude degrees'),
    ('Longitude', 'longitud' ,'lon', 'Geolocalitation longitude degrees'),
    ('Elevation', 'altitud', 'N/A', 'Elevation over the sea level'),
    ('Category', 'CATEGORIA', 'N/A', 'Station category: pluviometric, limnimetric, pluviograph, limnigraph, ordinary climatology, principal climatology, special meteorologic, soil meteorological, main synoptic, secundary synotic, radiosonde, mareographic'),
    ('Technology', 'TECNOLOGIA', 'N/A', 'Main technology: conventional, automatic assisted with telemetry, automatic not assisted with telemetry'),
    ('Status', 'ESTADO', 'N/A', 'Functional status: active, suspended, under maintenance'),
    ('InstDate', 'FECHA_INSTALACION', 'N/A', 'Installation date'),
    ('SuspDate', 'FECHA_SUSPENSION', 'N/A', 'Suspension date'),
    ('State', 'DEPARTAMENTO', 'N/A', 'Geopolitical location state'),
    ('County', 'MUNICIPIO', 'N/A', 'Geopolitical location county'),
    ('Stream', 'CORRIENTE', 'N/A', 'Stream point or near stream'),
    ('Operator', 'AREA_OPERATIVA', 'N/A', 'Gouvernament operator'),
    ('AHName', 'AREA_HIDROGRAFICA', 'N/A', 'AH - Hydrographic area. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('SZName', 'ZONA_HIDROGRAFICA', 'N/A', 'ZH - Hydrographic zone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('SZHName', 'SUBZONA_HIDROGRAFICA', 'N/A', 'SZH - Hydrographic subzone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone)'),
    ('Timezone', 'N/A', 'timezone', 'Global time zone'),
    ('Datetime', 'N/A', 'N/A', 'Date and time of the weather values'),
    ('Clouds', 'N/A', 'clouds', 'Cloudiness'),
    ('Dewpoint', 'N/A', 'dew_point', 'Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form.'),
    ('Feelslike', 'N/A', 'feels_like', 'Temperature. This temperature parameter accounts for the human perception of weather'),
    ('Humidity', 'N/A', 'humidity', 'Humidity'),
    ('Pressure', 'N/A', 'pressure', 'Atmospheric pressure on the sea level'),
    ('Rain', 'N/A', 'rain', 'Rain volume for last hour'),
    ('Temp', 'N/A', 'temp', 'Temperature'),
    ('UVI', 'N/A', 'uvi', 'Current UV index'),
    ('Visibility', 'N/A', 'visibility', 'Average visibility'),
    ('Winddeg', 'N/A', 'wind_deg', 'Wind direction, degrees (meteorological)'),
    ('Windgust', 'N/A', 'wind_gust', 'Wind gust'),
    ('Windspeed', 'N/A', 'wind_speed', 'Wind speed'),
    ('Julian', 'N/A', 'N/A', 'Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid)')]
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
elevationNameCNE = 'altitud'
categoryNameCNE = 'CATEGORIA'
technologyNameCNE = 'TECNOLOGIA'
statusNameCNE = 'ESTADO'
installationDateCNE = 'FECHA_INSTALACION'
suspensionDateCNE = 'FECHA_SUSPENSION'
geoStateNameCNE = 'DEPARTAMENTO'
geoCountyNameCNE = 'MUNICIPIO'
geoStreamNameCNE = 'CORRIENTE'
geoOperativeAreaNameCNE = 'AREA_OPERATIVA'
geoHydroAreaNameCNE = 'AREA_HIDROGRAFICA'
geoHydroZoneNameCNE = 'ZONA_HIDROGRAFICA'
geoHydroSubZoneNameCNE = 'SUBZONA_HIDROGRAFICA'
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
daysBefore = 1  # Max to 4 days, current day count like a part of 5 days in openweather
printDetail = False  # Print JSON dictionary on screen
showHistorical = False  # True for use the timemachine. False for get the current forecast
showYesterday = True
updateCNEFile = False


# General pandas and matplotlib settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)
mpl.rc('figure', max_open_warning = 0) # Don't show the python figure.max_open_warning

# Downloading and reading the CNE file
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileSaveCNE = filePath+'/Data/'+fileNameCNE+'_'+currentDateTxt+fileExtensionCNE
fileOutputCNEWeather = open(filePath+'/Output/'+fileNameCNE+'_OWM_'+currentDateTxt+'.csv', 'w+')
fileOutputMarkdown = open(filePath+'/Output/'+fileNameCNE+'_OWM_'+currentDateTxt+'.md', 'w+')
if updateCNEFile:
    fileRequest = requests.get(urlFileCNE)
    if fileRequest:
        if os.path.isfile(fileSaveCNE) == False:
            open(fileSaveCNE, 'wb').write(fileRequest.content)
            fileDownloadText = 'CNE IDEAM file downloaded and updated: Yes'
else:
    open(fileSaveCNE)
    fileDownloadText = 'CNE IDEAM file downloaded and updated: No'
stationTableCNE = pd.read_excel(fileSaveCNE, index_col=0, sheet_name='CNE')
pd.set_option('display.max_rows', stationTableCNE.shape[0]+1)  # Show all the records
pd.set_option('display.max_columns', None)  # Show all the records

# Show CNE records and weather values
timeStampVal = int(currentDateTime.replace(tzinfo=timezone.utc).timestamp())
if showYesterday: timeStampVal -= 86400 * daysBefore
#numStationsCNE = stationTableCNE.shape[0]
numStationsCNE = 3
printmd('\n### Weather values for each IDEAM CNE station from https://openweathermap.org')
printmd('\n* Current date time: ' + str(currentDateTime) +
        '\n* Unix time to eval: ' + str(timeStampVal) +
        '\n* Show historical: ' + str(showHistorical) +
        '\n* Show yesterday: ' + str(showYesterday) +
        '\n* Days before: ' + str(daysBefore) +
        '\n* ' + str(fileDownloadText) +
        '\n* Stations: ' + str(numStationsCNE) +
        '\n* Attributes: ' + str(stationTableCNE.shape[1]))
printmd('\n> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.')

# Print units system
if unitSys == 'metric':
    unitVal = unitValMetric
else:
    unitVal = unitValImperial
printmd('\n ### Unit system (%s)\n' %(unitSys))
printmd('| Parameter | Unit | openweathermap name |')
tableseparatormarkdown(3)
for i in unitVal:
    printmd('| %s | %s | %s |' % (i[0],i[1],i[2]))
printmd('\n> mi: Miles unit for imperial system')
printmd('\n> DN: Dimensionless numbers')

# Print CSV parameters
printmd('\n ### File parameters over the generated comma separated values - CSV\n')
printmd('| r.cfdtools | IDEAM | OpenWeather | Description |')
tableseparatormarkdown(4)
for i in csvParameters:
    printmd('| %s | %s | %s | %s |' % (i[0],i[1],i[2],i[3]))
printmd('\n> Some definitions are taken from https://openweathermap.org/')
printmd('\n> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API')

# Print and export CNE stations and weather parameters
printmd('\n ### CNE stations and weather parameters\n')
geoArrayCNE = stationTableCNE[[stationCodeCNE, stationNameCNE, latitudeCNE, longitudeCNE, elevationNameCNE, categoryNameCNE, technologyNameCNE, statusNameCNE, installationDateCNE, suspensionDateCNE, geoStateNameCNE, geoCountyNameCNE, geoStreamNameCNE, geoOperativeAreaNameCNE, geoHydroAreaNameCNE, geoHydroZoneNameCNE, geoHydroSubZoneNameCNE]]
printcsv(
    'Station,Statname,Latitude,Longitude,Elevation,Category,Technology,Status,InstDate,SuspDate,State,County,Stream,Operator,AHName,SZName,SZHName,Timezone,Datetime,Clouds,Dewpoint,Feelslike,Humidity,Pressure,Rain,Temp,UVI,Visibility,Winddeg,Windgust,Windspeed,Julian', False)
for i in range(1, numStationsCNE+1):
    printmd('\n#### %s - Open Weather values for station %s: %s' % (str(i), str(geoArrayCNE[stationCodeCNE][i]).zfill(12), str(geoArrayCNE[stationNameCNE][i])))
    if showHistorical:
        url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%f&lon=%f&dt=%i&units=%s&appid=%s' % (geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], timeStampVal, unitSys, apiKey)
    else:
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%f&lon=%f&&units=%s&appid=%s' % (latDD, lonDD, unitSys, apiKey)
    print('\n* URL: ' + url)
    printmd('\n* Station in: [Google Maps](http://maps.google.com/maps?q=' + str(geoArrayCNE[latitudeCNE][i]) + ',' + str(geoArrayCNE[longitudeCNE][i]) + '), [Openstreet Map](https://www.openstreetmap.org/query?lat='+ str(geoArrayCNE[latitudeCNE][i]) + '&lon=' + str(geoArrayCNE[longitudeCNE][i]) + ').')
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
    printmd('\n| Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | Julian |', True)
    tableseparatormarkdown(32)
    for entry in hourly:
        if 'rain' in entry:
            rain = entry['rain']['1h']
        else:
            rain = ''
        if 'wind_gust' in entry:
            wind_gust = entry['wind_gust']
        else:
            wind_gust = ''
        txtPrintCSV = '%s,"%s",%f,%f,%f,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%f,%f,%f,%f,%f,%s,%f,%f,%f,%f,%f,%f,%s' % (str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], geoArrayCNE[elevationNameCNE][i], geoArrayCNE[categoryNameCNE][i], geoArrayCNE[technologyNameCNE][i], geoArrayCNE[statusNameCNE][i], geoArrayCNE[installationDateCNE][i], geoArrayCNE[suspensionDateCNE][i], geoArrayCNE[geoStateNameCNE][i], geoArrayCNE[geoCountyNameCNE][i], geoArrayCNE[geoStreamNameCNE][i], geoArrayCNE[geoOperativeAreaNameCNE][i], geoArrayCNE[geoHydroAreaNameCNE][i], geoArrayCNE[geoHydroZoneNameCNE][i], geoArrayCNE[geoHydroSubZoneNameCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], entry['wind_gust'], entry['wind_speed'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
        printcsv(txtPrintCSV, False)
        txtPrintMd = '| %s | "%s" | %f | %f | %f | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %f | %f | %f | %f | %f | %s | %f | %f | %f | %f | %f | %f | %s |' % (str(geoArrayCNE[stationCodeCNE][i]), geoArrayCNE[stationNameCNE][i], geoArrayCNE[latitudeCNE][i], geoArrayCNE[longitudeCNE][i], geoArrayCNE[elevationNameCNE][i], geoArrayCNE[categoryNameCNE][i], geoArrayCNE[technologyNameCNE][i], geoArrayCNE[statusNameCNE][i], geoArrayCNE[installationDateCNE][i], geoArrayCNE[suspensionDateCNE][i], geoArrayCNE[geoStateNameCNE][i], geoArrayCNE[geoCountyNameCNE][i], geoArrayCNE[geoStreamNameCNE][i], geoArrayCNE[geoOperativeAreaNameCNE][i], geoArrayCNE[geoHydroAreaNameCNE][i], geoArrayCNE[geoHydroZoneNameCNE][i], geoArrayCNE[geoHydroSubZoneNameCNE][i], data['timezone'], datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'), entry['clouds'], entry['dew_point'], entry['feels_like'], entry['humidity'], entry['pressure'], rain, entry['temp'], entry['uvi'], entry['visibility'], entry['wind_deg'], entry['wind_gust'], entry['wind_speed'], datetime.utcfromtimestamp(entry['dt']).strftime('%H'))
        printmd(txtPrintMd, True)

# References
# https://openweathermap.org
# https://towardsdatascience.com/develop-your-weather-application-with-python-in-less-than-10-lines-6d092c6dcbc9
# https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timeStamp
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://realpython.com/python-json/
# https://knasmueller.net/using-the-open-weather-map-api-with-python
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
# https://stackoverflow.com/questions/3327946/how-can-i-get-the-current-time-now-in-utc
# https://pynative.com/python-check-if-key-exists-in-json-and-iterate-the-json-array/
# https://www.epa.gov/sites/default/files/documents/uviguide.pdf
# https://stackoverflow.com/questions/44177417/how-to-display-openweathermap-weather-icon