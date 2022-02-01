
# General libraries
from datetime import date

# General variables
mainTitle = 'Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org'
studyCase = 'Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica'
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather'
fileNameCNE = 'CNE_IDEAM'
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
unitSys = 'metric'  # '' for default, 'metric' or 'imperial'
plotParameters = [  # Parameter, metric system units, imperial system units
                  ('Clouds', '%', '%', 'light:k'),
                  ('Dewpoint', '°C', '°F', 'viridis_r'),
                  ('Feelslike', '°C', '°F', 'viridis_r'),
                  ('Humidity', '%', '%', 'light:b'),
                  ('Pressure', 'hPa', 'hPa', 'light:k'),
                  ('Rain', 'mm', 'mm', 'Blues'),
                  ('Temp', '°C', '°F', 'viridis_r'),
                  ('UVI', 'DN', 'DN', 'viridis_r'),
                  ('Visibility', 'm', 'm', 'light:k'),
                  ('Winddeg', '°', '°', 'Spectral'),
                  ('Windgust', 'm/s', 'm/s', 'YlOrBr'),
                  ('Windspeed', 'm/s', 'm/s', 'YlOrBr'),]

