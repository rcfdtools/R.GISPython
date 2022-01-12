
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CALDERAS [23085010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23085010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.15,-75.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.15&lon=-75.06666667)


| Parameter | Value |
|---|---|
| Code | 23085010 |
| Name | CALDERAS [23085010] |
| Latitude, ° | 6.15 |
| Longitude, ° | -75.06666667 |
| Elevation, m | 1320 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1985-08-15 00:00:00 |
| Suspension date | 1988-07-15 00:00:00 |
| State | Antioquia |
| County | San Carlos (Antioquia) |
| Stream | Meta |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Nare |

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

### (CNE index 740) Open Weather values for station 23085010 - CALDERAS [23085010]

JSON data from API OWM:

```
{'lat': 6.15, 'lon': -75.0667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813236, 'sunset': 1641855675, 'temp': 22.05, 'feels_like': 22.66, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.33, 'uvi': 1.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 24, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, 'hourly': [{'dt': 1641772800, 'temp': 19.66, 'feels_like': 20.24, 'pressure': 1014, 'humidity': 98, 'dew_point': 19.34, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 314, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641776400, 'temp': 19.56, 'feels_like': 20.13, 'pressure': 1015, 'humidity': 98, 'dew_point': 19.24, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 292, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 18.64, 'feels_like': 19.12, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.32, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 286, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 18.6, 'feels_like': 19.07, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.28, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 276, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.6, 'feels_like': 19.07, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.28, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 271, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 17.59, 'feels_like': 17.96, 'pressure': 1015, 'humidity': 98, 'dew_point': 17.27, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 277, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 17.59, 'feels_like': 17.96, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.27, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 275, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 17.59, 'feels_like': 17.94, 'pressure': 1014, 'humidity': 97, 'dew_point': 17.11, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 281, 'wind_gust': 1.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 17.55, 'feels_like': 17.89, 'pressure': 1013, 'humidity': 97, 'dew_point': 17.07, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 284, 'wind_gust': 1.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 16.63, 'feels_like': 16.88, 'pressure': 1013, 'humidity': 97, 'dew_point': 16.15, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 283, 'wind_gust': 1.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 17.55, 'feels_like': 17.89, 'pressure': 1014, 'humidity': 97, 'dew_point': 17.07, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 284, 'wind_gust': 1.04, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 16.84, 'feels_like': 17.11, 'pressure': 1015, 'humidity': 97, 'dew_point': 16.36, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 280, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641816000, 'temp': 17.59, 'feels_like': 17.86, 'pressure': 1016, 'humidity': 94, 'dew_point': 16.61, 'uvi': 0.35, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 289, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641819600, 'temp': 18.39, 'feels_like': 18.63, 'pressure': 1017, 'humidity': 90, 'dew_point': 16.72, 'uvi': 1.93, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 292, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641823200, 'temp': 19.54, 'feels_like': 19.8, 'pressure': 1017, 'humidity': 86, 'dew_point': 17.14, 'uvi': 4.84, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 84, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 19.61, 'feels_like': 19.77, 'pressure': 1017, 'humidity': 82, 'dew_point': 16.45, 'uvi': 8.39, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 93, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641830400, 'temp': 20.41, 'feels_like': 20.46, 'pressure': 1015, 'humidity': 75, 'dew_point': 15.83, 'uvi': 6.44, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 88, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641834000, 'temp': 20.25, 'feels_like': 20.13, 'pressure': 1014, 'humidity': 69, 'dew_point': 14.38, 'uvi': 7.1, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 84, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 19.11, 'feels_like': 19.09, 'pressure': 1013, 'humidity': 77, 'dew_point': 14.99, 'uvi': 6.51, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 75, 'wind_gust': 1.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641841200, 'temp': 21.23, 'feels_like': 21.68, 'pressure': 1012, 'humidity': 87, 'dew_point': 18.98, 'uvi': 2.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 58, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641844800, 'temp': 22.05, 'feels_like': 22.66, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.33, 'uvi': 1.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 24, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641848400, 'temp': 21.84, 'feels_like': 22.48, 'pressure': 1011, 'humidity': 92, 'dew_point': 20.48, 'uvi': 0.65, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 19, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641852000, 'temp': 20.85, 'feels_like': 21.42, 'pressure': 1012, 'humidity': 93, 'dew_point': 19.68, 'uvi': 0.21, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 15, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641855600, 'temp': 19.82, 'feels_like': 20.39, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.33, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 334, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 00:00:00 | 43.000000 | 19.340000 | 20.240000 | 98.000000 | 1014.000000 | 0.13 | 19.660000 | 0.000000 | 10000.000000 | 314.000000 | 0.98 | 1.000000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 01:00:00 | 57.000000 | 19.240000 | 20.130000 | 98.000000 | 1015.000000 |  | 19.560000 | 0.000000 | 10000.000000 | 292.000000 | 0.95 | 1.020000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 02:00:00 | 68.000000 | 18.320000 | 19.120000 | 98.000000 | 1016.000000 |  | 18.640000 | 0.000000 | 10000.000000 | 286.000000 | 0.9 | 1.100000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 03:00:00 | 70.000000 | 18.280000 | 19.070000 | 98.000000 | 1016.000000 |  | 18.600000 | 0.000000 | 10000.000000 | 276.000000 | 1.01 | 1.180000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 04:00:00 | 74.000000 | 18.280000 | 19.070000 | 98.000000 | 1016.000000 |  | 18.600000 | 0.000000 | 10000.000000 | 271.000000 | 0.97 | 1.220000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 05:00:00 | 74.000000 | 17.270000 | 17.960000 | 98.000000 | 1015.000000 |  | 17.590000 | 0.000000 | 10000.000000 | 277.000000 | 1.04 | 1.250000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 06:00:00 | 62.000000 | 17.270000 | 17.960000 | 98.000000 | 1014.000000 |  | 17.590000 | 0.000000 | 10000.000000 | 275.000000 | 1.03 | 1.350000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 07:00:00 | 59.000000 | 17.110000 | 17.940000 | 97.000000 | 1014.000000 |  | 17.590000 | 0.000000 | 10000.000000 | 281.000000 | 1.06 | 1.330000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 08:00:00 | 48.000000 | 17.070000 | 17.890000 | 97.000000 | 1013.000000 |  | 17.550000 | 0.000000 | 10000.000000 | 284.000000 | 1.07 | 1.280000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 09:00:00 | 45.000000 | 16.150000 | 16.880000 | 97.000000 | 1013.000000 |  | 16.630000 | 0.000000 | 10000.000000 | 283.000000 | 1.02 | 1.270000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 10:00:00 | 48.000000 | 17.070000 | 17.890000 | 97.000000 | 1014.000000 |  | 17.550000 | 0.000000 | 10000.000000 | 284.000000 | 1.04 | 1.300000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 11:00:00 | 54.000000 | 16.360000 | 17.110000 | 97.000000 | 1015.000000 | 0.11 | 16.840000 | 0.000000 | 10000.000000 | 280.000000 | 0.99 | 1.170000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 12:00:00 | 71.000000 | 16.610000 | 17.860000 | 94.000000 | 1016.000000 | 0.18 | 17.590000 | 0.350000 | 10000.000000 | 289.000000 | 0.76 | 0.870000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 13:00:00 | 79.000000 | 16.720000 | 18.630000 | 90.000000 | 1017.000000 | 0.13 | 18.390000 | 1.930000 | 10000.000000 | 292.000000 | 0.54 | 0.310000 | 500 | Rain | light rain | 10d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 14:00:00 | 70.000000 | 17.140000 | 19.800000 | 86.000000 | 1017.000000 |  | 19.540000 | 4.840000 | 10000.000000 | 84.000000 | 0.86 | 0.550000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 15:00:00 | 72.000000 | 16.450000 | 19.770000 | 82.000000 | 1017.000000 | 0.14 | 19.610000 | 8.390000 | 10000.000000 | 93.000000 | 1.01 | 0.820000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 15.830000 | 20.460000 | 75.000000 | 1015.000000 | 0.13 | 20.410000 | 6.440000 | 10000.000000 | 88.000000 | 1.11 | 1.300000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 17:00:00 | 77.000000 | 14.380000 | 20.130000 | 69.000000 | 1014.000000 | 0.11 | 20.250000 | 7.100000 | 10000.000000 | 84.000000 | 1.69 | 1.560000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 18:00:00 | 89.000000 | 14.990000 | 19.090000 | 77.000000 | 1013.000000 | 0.21 | 19.110000 | 6.510000 | 10000.000000 | 75.000000 | 1.76 | 1.320000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 18.980000 | 21.680000 | 87.000000 | 1012.000000 | 0.53 | 21.230000 | 2.710000 | 10000.000000 | 58.000000 | 1.51 | 0.970000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 20.330000 | 22.660000 | 90.000000 | 1011.000000 | 0.65 | 22.050000 | 1.600000 | 10000.000000 | 24.000000 | 1.21 | 0.670000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 20.480000 | 22.480000 | 92.000000 | 1011.000000 | 0.62 | 21.840000 | 0.650000 | 10000.000000 | 19.000000 | 1.25 | 0.640000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 19.680000 | 21.420000 | 93.000000 | 1012.000000 | 0.63 | 20.850000 | 0.210000 | 10000.000000 | 15.000000 | 1.22 | 0.680000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085010 | "CALDERAS [23085010]" | 6.150000 | -75.066667 | 1320.000000 | Climática Principal | Convencional | Suspendida | 1985-08-15 00:00:00 | 1988-07-15 00:00:00 | Antioquia | San Carlos (Antioquia) | Meta | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 19.330000 | 20.390000 | 97.000000 | 1013.000000 | 0.53 | 19.820000 | 0.000000 | 10000.000000 | 334.000000 | 0.85 | 0.890000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23085010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23085010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23085010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085010_OWM_Windspeed_20220111.png)
