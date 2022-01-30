
# General libraries
from datetime import date

# General variables
studyCase = 'Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica'
filePath = r'D:/R.GISPython/OpenWeather'  # r'.' for relative path
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather'
fileNameCNE = 'CNE_IDEAM'
currentDate = date.today()
currentDateTxt = str(currentDate.year).zfill(4)+str(currentDate.month).zfill(2)+str(currentDate.day).zfill(2)
fileCSV = fileNameCNE+'_OWM_'+currentDateTxt+'.csv'
unitSys = 'metric'  # '' for default, 'metric' or 'imperial'
plotParameters = [  # Parameter, metric system units, imperial system units
                  ('Clouds', '%', '%'),
                  ('Dewpoint', '°C', '°F'),
                  ('Feelslike', '°C', '°F'),
                  ('Humidity', '%', '%'),
                  ('Pressure', 'hPa', 'hPa'),
                  ('Rain', 'mm', 'mm'),
                  ('Temp', '°C', '°F'),
                  ('UVI', 'DN', 'DN'),
                  ('Visibility', 'm', 'm'),
                  ('Winddeg', '°', '°'),
                  ('Windgust', 'm/s', 'm/s'),
                  ('Windspeed', 'm/s', 'm/s'),]