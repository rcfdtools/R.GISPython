
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAIZA - AUT [29045150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29045150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.74602778,-76.4325) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.74602778&lon=-76.4325)


| Parameter | Value |
|---|---|
| Code | 29045150 |
| Name | SAIZA - AUT [29045150] |
| Latitude, ° | 7.74602778 |
| Longitude, ° | -76.4325 |
| Elevation, m | 287 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2002-11-15 00:00:00 |
| Suspension date | 2010-08-10 00:00:00 |
| State | Córdoba |
| County | Tierralta |
| Stream | Tachira |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Alto Sinú - Urrá |

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

### (CNE index 192) Open Weather values for station 29045150 - SAIZA - AUT [29045150]

JSON data from API OWM:

```
{'lat': 7.746, 'lon': -76.4325, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813720, 'sunset': 1641855847, 'temp': 24.57, 'feels_like': 25.07, 'pressure': 1010, 'humidity': 76, 'dew_point': 20.06, 'uvi': 3.66, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 307, 'wind_gust': 2.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, 'hourly': [{'dt': 1641772800, 'temp': 22.57, 'feels_like': 23.39, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.9, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 69, 'wind_gust': 0.79, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 22.57, 'feels_like': 23.39, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.9, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 77, 'wind_gust': 0.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 20.44, 'feels_like': 21.05, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.78, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 79, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 20.28, 'feels_like': 20.9, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.79, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 87, 'wind_gust': 0.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 20.02, 'feels_like': 20.61, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.53, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 126, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 19.68, 'feels_like': 20.26, 'pressure': 1013, 'humidity': 98, 'dew_point': 19.36, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 176, 'wind_gust': 0.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 19.45, 'feels_like': 20.01, 'pressure': 1012, 'humidity': 98, 'dew_point': 19.13, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 180, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641798000, 'temp': 19.4, 'feels_like': 19.95, 'pressure': 1012, 'humidity': 98, 'dew_point': 19.08, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 203, 'wind_gust': 0.54, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 19.1, 'feels_like': 19.62, 'pressure': 1011, 'humidity': 98, 'dew_point': 18.78, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 187, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641805200, 'temp': 19.28, 'feels_like': 19.82, 'pressure': 1011, 'humidity': 98, 'dew_point': 18.96, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 179, 'wind_gust': 0.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 19.46, 'feels_like': 20.02, 'pressure': 1012, 'humidity': 98, 'dew_point': 19.14, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 181, 'wind_gust': 0.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.57, 'feels_like': 22.34, 'pressure': 1013, 'humidity': 98, 'dew_point': 21.24, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 229, 'wind_gust': 0.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.57, 'feels_like': 22.32, 'pressure': 1013, 'humidity': 97, 'dew_point': 21.07, 'uvi': 0.28, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 143, 'wind_gust': 0.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 21.57, 'feels_like': 22.24, 'pressure': 1014, 'humidity': 94, 'dew_point': 20.56, 'uvi': 1.48, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 309, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 22.57, 'feels_like': 23.15, 'pressure': 1015, 'humidity': 87, 'dew_point': 20.3, 'uvi': 3.83, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 317, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641826800, 'temp': 23.57, 'feels_like': 23.99, 'pressure': 1015, 'humidity': 77, 'dew_point': 19.3, 'uvi': 6.85, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 338, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641830400, 'temp': 23.57, 'feels_like': 23.84, 'pressure': 1014, 'humidity': 71, 'dew_point': 18.01, 'uvi': 8.66, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 344, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641834000, 'temp': 24.57, 'feels_like': 24.86, 'pressure': 1013, 'humidity': 68, 'dew_point': 18.28, 'uvi': 9.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 322, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641837600, 'temp': 24.57, 'feels_like': 24.99, 'pressure': 1012, 'humidity': 73, 'dew_point': 19.41, 'uvi': 8.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 308, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.69}}, {'dt': 1641841200, 'temp': 24.57, 'feels_like': 24.94, 'pressure': 1011, 'humidity': 71, 'dew_point': 18.97, 'uvi': 6.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 310, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641844800, 'temp': 24.57, 'feels_like': 25.07, 'pressure': 1010, 'humidity': 76, 'dew_point': 20.06, 'uvi': 3.66, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 307, 'wind_gust': 2.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641848400, 'temp': 24.57, 'feels_like': 25.2, 'pressure': 1010, 'humidity': 81, 'dew_point': 21.09, 'uvi': 1.52, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 308, 'wind_gust': 2.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641852000, 'temp': 23.57, 'feels_like': 24.28, 'pressure': 1010, 'humidity': 88, 'dew_point': 21.47, 'uvi': 0.33, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 307, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641855600, 'temp': 22.57, 'feels_like': 23.31, 'pressure': 1011, 'humidity': 93, 'dew_point': 21.38, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 298, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 00:00:00 | 45.000000 | 21.900000 | 23.390000 | 96.000000 | 1011.000000 |  | 22.570000 | 0.000000 | 10000.000000 | 69.000000 | 0.79 | 0.500000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 01:00:00 | 45.000000 | 21.900000 | 23.390000 | 96.000000 | 1012.000000 |  | 22.570000 | 0.000000 | 10000.000000 | 77.000000 | 0.71 | 0.380000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 19.780000 | 21.050000 | 96.000000 | 1013.000000 |  | 20.440000 | 0.000000 | 10000.000000 | 79.000000 | 0.75 | 0.550000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 03:00:00 | 82.000000 | 19.790000 | 20.900000 | 97.000000 | 1013.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 87.000000 | 0.68 | 0.440000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 04:00:00 | 85.000000 | 19.530000 | 20.610000 | 97.000000 | 1013.000000 |  | 20.020000 | 0.000000 | 10000.000000 | 126.000000 | 0.68 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 05:00:00 | 87.000000 | 19.360000 | 20.260000 | 98.000000 | 1013.000000 |  | 19.680000 | 0.000000 | 10000.000000 | 176.000000 | 0.58 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 06:00:00 | 35.000000 | 19.130000 | 20.010000 | 98.000000 | 1012.000000 | 0.2 | 19.450000 | 0.000000 | 10000.000000 | 180.000000 | 0.63 | 0.320000 | 500 | Rain | light rain | 10n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 07:00:00 | 36.000000 | 19.080000 | 19.950000 | 98.000000 | 1012.000000 |  | 19.400000 | 0.000000 | 10000.000000 | 203.000000 | 0.54 | 0.330000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 08:00:00 | 65.000000 | 18.780000 | 19.620000 | 98.000000 | 1011.000000 | 0.14 | 19.100000 | 0.000000 | 10000.000000 | 187.000000 | 0.55 | 0.340000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 09:00:00 | 64.000000 | 18.960000 | 19.820000 | 98.000000 | 1011.000000 |  | 19.280000 | 0.000000 | 10000.000000 | 179.000000 | 0.56 | 0.470000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 10:00:00 | 73.000000 | 19.140000 | 20.020000 | 98.000000 | 1012.000000 |  | 19.460000 | 0.000000 | 10000.000000 | 181.000000 | 0.57 | 0.560000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 11:00:00 | 78.000000 | 21.240000 | 22.340000 | 98.000000 | 1013.000000 |  | 21.570000 | 0.000000 | 10000.000000 | 229.000000 | 0.37 | 0.290000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 12:00:00 | 76.000000 | 21.070000 | 22.320000 | 97.000000 | 1013.000000 |  | 21.570000 | 0.280000 | 10000.000000 | 143.000000 | 0.46 | 0.170000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 13:00:00 | 93.000000 | 20.560000 | 22.240000 | 94.000000 | 1014.000000 |  | 21.570000 | 1.480000 | 10000.000000 | 309.000000 | 0.64 | 0.110000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 14:00:00 | 96.000000 | 20.300000 | 23.150000 | 87.000000 | 1015.000000 | 0.19 | 22.570000 | 3.830000 | 10000.000000 | 317.000000 | 1.34 | 0.540000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 15:00:00 | 97.000000 | 19.300000 | 23.990000 | 77.000000 | 1015.000000 | 0.31 | 23.570000 | 6.850000 | 10000.000000 | 338.000000 | 1.1 | 0.850000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 18.010000 | 23.840000 | 71.000000 | 1014.000000 | 0.2 | 23.570000 | 8.660000 | 10000.000000 | 344.000000 | 1.42 | 1.260000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 18.280000 | 24.860000 | 68.000000 | 1013.000000 | 0.35 | 24.570000 | 9.710000 | 10000.000000 | 322.000000 | 1.4 | 1.280000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 19.410000 | 24.990000 | 73.000000 | 1012.000000 | 0.69 | 24.570000 | 8.990000 | 10000.000000 | 308.000000 | 1.54 | 1.370000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 18.970000 | 24.940000 | 71.000000 | 1011.000000 | 0.53 | 24.570000 | 6.140000 | 10000.000000 | 310.000000 | 1.85 | 1.460000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 20.060000 | 25.070000 | 76.000000 | 1010.000000 | 0.43 | 24.570000 | 3.660000 | 10000.000000 | 307.000000 | 2.21 | 1.340000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 21.090000 | 25.200000 | 81.000000 | 1010.000000 | 0.67 | 24.570000 | 1.520000 | 10000.000000 | 308.000000 | 2.09 | 1.190000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 21.470000 | 24.280000 | 88.000000 | 1010.000000 | 0.38 | 23.570000 | 0.330000 | 10000.000000 | 307.000000 | 1.5 | 1.000000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 29045150 | "SAIZA - AUT [29045150]" | 7.746028 | -76.432500 | 287.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2002-11-15 00:00:00 | 2010-08-10 00:00:00 | Córdoba | Tierralta | Tachira | Area Operativa 01 - Antioquia-Chocó | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 21.380000 | 23.310000 | 93.000000 | 1011.000000 | 0.2 | 22.570000 | 0.000000 | 10000.000000 | 298.000000 | 0.6 | 0.510000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station29045150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29045150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29045150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045150_OWM_Windspeed_20220111.png)
