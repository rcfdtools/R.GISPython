
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PIE DE PATO - AUT [55015010] - Historical

### General parameters

* Weather date time: 2022-01-11 19:42:05.608768
* Unix time to eval: 1641843725
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Days before: 1
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220111.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4494
* CNE IDEAM attributes: 20
* CNE IDEAM station code filter: ['All', 26055120, 1508500053]
* CNE IDEAM category filter: ['Climática Principal']
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['All']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station55015010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.52108333,-76.97316667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.52108333&lon=-76.97316667)


| Parameter | Value |
|---|---|
| Code | 55015010 |
| Name | PIE DE PATO - AUT [55015010] |
| Latitude, ° | 5.52108333 |
| Longitude, ° | -76.97316667 |
| Elevation, m | 40 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-03-12 00:00:00 |
| Suspension date | NaT |
| State | Chocó |
| County | Alto Baudó (Pie De Pato) |
| Stream | Atrato |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Baudó - Directos Pacifico |
| SZH - Hydrographic subzone | Río Baudó |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit | openweathermap name |
|---|---|---|
| Temperature | °C | temp |
| Dew Point | °C | dew_point |
| Feels like | °C | feels_like |
| Clouds | % | clouds |
| Humidity | % | humidity |
| Pressure | hPa | pressure |
| Wind Direction | ° | wind_deg |
| Wind Speed | m/s | wind_speed |
| Wind Gust | m/s | wind_gust |
| Rain | mm | rain |
| Visibility | m | visibility |
| UV Index | DN | uvi |

> mi: Miles unit for imperial system

> DN: Dimensionless numbers

#### File parameters over the generated comma separated values - CSV

| r.cfdtools | CNE IDEAM | OpenWeather | Description |
|---|---|---|---|
| Station | CODIGO | N/A | Station code |
| Statname | nombre | N/A | Station name |
| Latitude | latitud | lat | Geolocalization latitude degrees |
| Longitude | longitud | lon | Geolocalization longitude degrees |
| Elevation | altitud | N/A | Elevation over the sea level |
| Category | CATEGORIA | N/A | Station category: pluviometric, limnimetric, pluviograph, limnigraph, ordinary climatology, principal climatology, special meteorologic, soil meteorological, main synoptic, secundary synotic, radiosonde, mareographic |
| Technology | TECNOLOGIA | N/A | Main technology: conventional, automatic assisted with telemetry, automatic not assisted with telemetry |
| Status | ESTADO | N/A | Functional status: active, suspended, under maintenance |
| InstDate | FECHA_INSTALACION | N/A | Installation date |
| SuspDate | FECHA_SUSPENSION | N/A | Suspension date |
| State | DEPARTAMENTO | N/A | Geopolitical location state |
| County | MUNICIPIO | N/A | Geopolitical location county |
| Stream | CORRIENTE | N/A | Stream point or near stream |
| Operator | AREA_OPERATIVA | N/A | Gouvernament operator |
| AHName | AREA_HIDROGRAFICA | N/A | AH - Hydrographic area. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZName | ZONA_HIDROGRAFICA | N/A | ZH - Hydrographic zone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| SZHName | SUBZONA_HIDROGRAFICA | N/A | SZH - Hydrographic subzone. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/HydroGeoZone) |
| Timezone | N/A | timezone | Global time zone |
| Datetime | N/A | N/A | Date and time of the weather values |
| Clouds | N/A | clouds | Cloudiness |
| Dewpoint | N/A | dew_point | Atmospheric temperature (varying according to pressure and humidity) below which water droplets begin to condense and dew can form. |
| Feelslike | N/A | feels_like | Temperature. This temperature parameter accounts for the human perception of weather |
| Humidity | N/A | humidity | Humidity |
| Pressure | N/A | pressure | Atmospheric pressure on the sea level |
| Rain | N/A | rain | Rain volume for last hour |
| Temp | N/A | temp | Temperature |
| UVI | N/A | uvi | Current UV index |
| Visibility | N/A | visibility | Average visibility |
| Winddeg | N/A | wind_deg | Wind direction, degrees (meteorological) |
| Windgust | N/A | wind_gust | Wind gust |
| Windspeed | N/A | wind_speed | Wind speed |
| OWMid | N/A | id | Weather identification over OWM |
| OWMmain | N/A | main | Group of weather parameters (Rain, Snow, Extreme etc.) |
| OWMdesc | N/A | description | Weather condition within the group. [More info.](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2) |
| OWMicon | N/A | icon | Weather icon id. [More info.](https://openweathermap.org/weather-conditions#How-to-get-icon-URL) |
| Hour | N/A | N/A | Hour can be used like a Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API

### (CNE index 142) Open Weather values for station 55015010 - PIE DE PATO - AUT [55015010]

JSON data from API OWM:

```
{'lat': 5.5211, 'lon': -76.9732, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813633, 'sunset': 1641856194, 'temp': 24.93, 'feels_like': 25.91, 'pressure': 1010, 'humidity': 93, 'dew_point': 23.72, 'uvi': 3.7, 'clouds': 99, 'visibility': 4686, 'wind_speed': 1.08, 'wind_deg': 185, 'wind_gust': 2.27, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.03}}, 'hourly': [{'dt': 1641772800, 'temp': 26.93, 'feels_like': 31.26, 'pressure': 1011, 'humidity': 97, 'dew_point': 26.41, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 204, 'wind_gust': 0.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.91}}, {'dt': 1641776400, 'temp': 22.68, 'feels_like': 23.56, 'pressure': 1012, 'humidity': 98, 'dew_point': 22.35, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 220, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641780000, 'temp': 22.59, 'feels_like': 23.46, 'pressure': 1013, 'humidity': 98, 'dew_point': 22.26, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 216, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 22.55, 'feels_like': 23.42, 'pressure': 1013, 'humidity': 98, 'dew_point': 22.22, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 202, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 22.32, 'feels_like': 23.19, 'pressure': 1013, 'humidity': 99, 'dew_point': 22.15, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 204, 'wind_gust': 0.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 22.15, 'feels_like': 23.01, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.99, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 193, 'wind_gust': 1.03, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 22.21, 'feels_like': 23.07, 'pressure': 1012, 'humidity': 99, 'dew_point': 22.05, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 211, 'wind_gust': 0.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 22.12, 'feels_like': 22.97, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.96, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 212, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641801600, 'temp': 22.09, 'feels_like': 22.94, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.93, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 208, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641805200, 'temp': 21.99, 'feels_like': 22.83, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.83, 'uvi': 0, 'clouds': 78, 'visibility': 9176, 'wind_speed': 0.84, 'wind_deg': 204, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641808800, 'temp': 22.03, 'feels_like': 22.87, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.87, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 193, 'wind_gust': 1.65, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.41}}, {'dt': 1641812400, 'temp': 23.93, 'feels_like': 24.96, 'pressure': 1012, 'humidity': 99, 'dew_point': 23.76, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 177, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.83}}, {'dt': 1641816000, 'temp': 23.93, 'feels_like': 24.96, 'pressure': 1013, 'humidity': 99, 'dew_point': 23.76, 'uvi': 0.07, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 169, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641819600, 'temp': 22.93, 'feels_like': 23.84, 'pressure': 1014, 'humidity': 98, 'dew_point': 22.6, 'uvi': 1.22, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 150, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641823200, 'temp': 22.93, 'feels_like': 23.81, 'pressure': 1015, 'humidity': 97, 'dew_point': 22.43, 'uvi': 3.17, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 124, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641826800, 'temp': 22.93, 'feels_like': 23.68, 'pressure': 1014, 'humidity': 92, 'dew_point': 21.56, 'uvi': 5.64, 'clouds': 99, 'visibility': 8448, 'wind_speed': 0.7, 'wind_deg': 122, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641830400, 'temp': 22.93, 'feels_like': 23.52, 'pressure': 1014, 'humidity': 86, 'dew_point': 20.46, 'uvi': 7.52, 'clouds': 100, 'visibility': 8993, 'wind_speed': 0.81, 'wind_deg': 165, 'wind_gust': 2.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641834000, 'temp': 22.93, 'feels_like': 23.52, 'pressure': 1013, 'humidity': 86, 'dew_point': 20.46, 'uvi': 8.46, 'clouds': 99, 'visibility': 9371, 'wind_speed': 1.24, 'wind_deg': 196, 'wind_gust': 2.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.56}}, {'dt': 1641837600, 'temp': 22.93, 'feels_like': 23.63, 'pressure': 1012, 'humidity': 90, 'dew_point': 21.2, 'uvi': 7.91, 'clouds': 98, 'visibility': 6856, 'wind_speed': 1.17, 'wind_deg': 198, 'wind_gust': 2.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.94}}, {'dt': 1641841200, 'temp': 23.93, 'feels_like': 24.7, 'pressure': 1011, 'humidity': 89, 'dew_point': 22.01, 'uvi': 6.11, 'clouds': 99, 'visibility': 5580, 'wind_speed': 1.16, 'wind_deg': 194, 'wind_gust': 2.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.86}}, {'dt': 1641844800, 'temp': 24.93, 'feels_like': 25.91, 'pressure': 1010, 'humidity': 93, 'dew_point': 23.72, 'uvi': 3.7, 'clouds': 99, 'visibility': 4686, 'wind_speed': 1.08, 'wind_deg': 185, 'wind_gust': 2.27, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.03}}, {'dt': 1641848400, 'temp': 24.93, 'feels_like': 25.96, 'pressure': 1010, 'humidity': 95, 'dew_point': 24.07, 'uvi': 1.61, 'clouds': 100, 'visibility': 7054, 'wind_speed': 0.74, 'wind_deg': 180, 'wind_gust': 1.85, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.72}}, {'dt': 1641852000, 'temp': 24.93, 'feels_like': 25.99, 'pressure': 1010, 'humidity': 96, 'dew_point': 24.25, 'uvi': 0.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 183, 'wind_gust': 1.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.29}}, {'dt': 1641855600, 'temp': 24.93, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 97, 'dew_point': 24.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 193, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 00:00:00 | 7.000000 | 26.410000 | 31.260000 | 97.000000 | 1011.000000 | 0.91 | 26.930000 | 0.000000 | 10000.000000 | 204.000000 | 0.32 | 0.140000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 22.350000 | 23.560000 | 98.000000 | 1012.000000 | 0.43 | 22.680000 | 0.000000 | 10000.000000 | 220.000000 | 0.59 | 0.520000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 02:00:00 | 14.000000 | 22.260000 | 23.460000 | 98.000000 | 1013.000000 | 0.13 | 22.590000 | 0.000000 | 10000.000000 | 216.000000 | 0.99 | 0.860000 | 500 | Rain | light rain | 10n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 03:00:00 | 38.000000 | 22.220000 | 23.420000 | 98.000000 | 1013.000000 |  | 22.550000 | 0.000000 | 10000.000000 | 202.000000 | 1.11 | 0.820000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 04:00:00 | 35.000000 | 22.150000 | 23.190000 | 99.000000 | 1013.000000 |  | 22.320000 | 0.000000 | 10000.000000 | 204.000000 | 0.99 | 0.750000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 05:00:00 | 33.000000 | 21.990000 | 23.010000 | 99.000000 | 1012.000000 |  | 22.150000 | 0.000000 | 10000.000000 | 193.000000 | 1.03 | 0.820000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 06:00:00 | 44.000000 | 22.050000 | 23.070000 | 99.000000 | 1012.000000 |  | 22.210000 | 0.000000 | 10000.000000 | 211.000000 | 0.97 | 0.760000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 07:00:00 | 69.000000 | 21.960000 | 22.970000 | 99.000000 | 1011.000000 | 0.24 | 22.120000 | 0.000000 | 10000.000000 | 212.000000 | 0.99 | 0.850000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 08:00:00 | 67.000000 | 21.930000 | 22.940000 | 99.000000 | 1011.000000 | 0.24 | 22.090000 | 0.000000 | 10000.000000 | 208.000000 | 1.14 | 0.900000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 09:00:00 | 78.000000 | 21.830000 | 22.830000 | 99.000000 | 1011.000000 | 0.4 | 21.990000 | 0.000000 | 9176.000000 | 204.000000 | 1.14 | 0.840000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 10:00:00 | 81.000000 | 21.870000 | 22.870000 | 99.000000 | 1012.000000 | 1.41 | 22.030000 | 0.000000 | 10000.000000 | 193.000000 | 1.65 | 0.920000 | 501 | Rain | moderate rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 11:00:00 | 84.000000 | 23.760000 | 24.960000 | 99.000000 | 1012.000000 | 0.83 | 23.930000 | 0.000000 | 10000.000000 | 177.000000 | 2.24 | 1.000000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 12:00:00 | 86.000000 | 23.760000 | 24.960000 | 99.000000 | 1013.000000 | 0.37 | 23.930000 | 0.070000 | 10000.000000 | 169.000000 | 1.59 | 0.750000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 22.600000 | 23.840000 | 98.000000 | 1014.000000 | 0.18 | 22.930000 | 1.220000 | 10000.000000 | 150.000000 | 1.78 | 0.750000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 22.430000 | 23.810000 | 97.000000 | 1015.000000 | 0.36 | 22.930000 | 3.170000 | 10000.000000 | 124.000000 | 1.42 | 0.730000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 21.560000 | 23.680000 | 92.000000 | 1014.000000 | 0.55 | 22.930000 | 5.640000 | 8448.000000 | 122.000000 | 1.4 | 0.700000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 20.460000 | 23.520000 | 86.000000 | 1014.000000 | 1.16 | 22.930000 | 7.520000 | 8993.000000 | 165.000000 | 2.01 | 0.810000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 20.460000 | 23.520000 | 86.000000 | 1013.000000 | 1.56 | 22.930000 | 8.460000 | 9371.000000 | 196.000000 | 2.39 | 1.240000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 21.200000 | 23.630000 | 90.000000 | 1012.000000 | 1.94 | 22.930000 | 7.910000 | 6856.000000 | 198.000000 | 2.32 | 1.170000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 22.010000 | 24.700000 | 89.000000 | 1011.000000 | 1.86 | 23.930000 | 6.110000 | 5580.000000 | 194.000000 | 2.05 | 1.160000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 23.720000 | 25.910000 | 93.000000 | 1010.000000 | 2.03 | 24.930000 | 3.700000 | 4686.000000 | 185.000000 | 2.27 | 1.080000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 24.070000 | 25.960000 | 95.000000 | 1010.000000 | 1.72 | 24.930000 | 1.610000 | 7054.000000 | 180.000000 | 1.85 | 0.740000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 24.250000 | 25.990000 | 96.000000 | 1010.000000 | 1.29 | 24.930000 | 0.360000 | 10000.000000 | 183.000000 | 1.57 | 0.890000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 55015010 | "PIE DE PATO - AUT [55015010]" | 5.521083 | -76.973167 | 40.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-12 00:00:00 | NaT | Chocó | Alto Baudó (Pie De Pato) | Atrato | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Baudó - Directos Pacifico | Río Baudó | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 24.420000 | 26.010000 | 97.000000 | 1011.000000 | 0.41 | 24.930000 | 0.000000 | 10000.000000 | 193.000000 | 1.46 | 0.910000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station55015010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station55015010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station55015010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station55015010_OWM_Windspeed_20220111.png)
