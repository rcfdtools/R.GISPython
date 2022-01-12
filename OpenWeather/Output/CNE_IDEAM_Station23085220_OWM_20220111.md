
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN CARLOS [23085220] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23085220_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.15766667,-75.03891667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.15766667&lon=-75.03891667)


| Parameter | Value |
|---|---|
| Code | 23085220 |
| Name | SAN CARLOS [23085220] |
| Latitude, ° | 6.15766667 |
| Longitude, ° | -75.03891667 |
| Elevation, m | 1113 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1983-05-15 00:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | San Carlos (Antioquia) |
| Stream | Casanare |
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

### (CNE index 743) Open Weather values for station 23085220 - SAN CARLOS [23085220]

JSON data from API OWM:

```
{'lat': 6.1577, 'lon': -75.0389, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813230, 'sunset': 1641855668, 'temp': 24.73, 'feels_like': 25.63, 'pressure': 1011, 'humidity': 91, 'dew_point': 23.16, 'uvi': 1.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 17, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, 'hourly': [{'dt': 1641772800, 'temp': 22.34, 'feels_like': 23.19, 'pressure': 1014, 'humidity': 98, 'dew_point': 22.01, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 310, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641776400, 'temp': 22.25, 'feels_like': 23.09, 'pressure': 1015, 'humidity': 98, 'dew_point': 21.92, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 290, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 21.33, 'feels_like': 22.05, 'pressure': 1015, 'humidity': 97, 'dew_point': 20.83, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 285, 'wind_gust': 0.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 21.29, 'feels_like': 22.03, 'pressure': 1016, 'humidity': 98, 'dew_point': 20.96, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 275, 'wind_gust': 1.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 21.29, 'feels_like': 22.03, 'pressure': 1015, 'humidity': 98, 'dew_point': 20.96, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 272, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.28, 'feels_like': 20.92, 'pressure': 1015, 'humidity': 98, 'dew_point': 19.95, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 277, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.28, 'feels_like': 20.9, 'pressure': 1014, 'humidity': 97, 'dew_point': 19.79, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 275, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.28, 'feels_like': 20.9, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.79, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 280, 'wind_gust': 1.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.23, 'feels_like': 20.84, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.74, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 282, 'wind_gust': 1.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 19.31, 'feels_like': 19.83, 'pressure': 1013, 'humidity': 97, 'dew_point': 18.82, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 281, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 20.23, 'feels_like': 20.82, 'pressure': 1014, 'humidity': 96, 'dew_point': 19.57, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 283, 'wind_gust': 1.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 19.52, 'feels_like': 20.03, 'pressure': 1014, 'humidity': 96, 'dew_point': 18.87, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 280, 'wind_gust': 1.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 20.28, 'feels_like': 20.79, 'pressure': 1015, 'humidity': 93, 'dew_point': 19.11, 'uvi': 0.35, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 288, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641819600, 'temp': 21.08, 'feels_like': 21.54, 'pressure': 1016, 'humidity': 88, 'dew_point': 19.02, 'uvi': 1.93, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 289, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641823200, 'temp': 22.23, 'feels_like': 22.73, 'pressure': 1017, 'humidity': 85, 'dew_point': 19.59, 'uvi': 4.84, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 85, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 22.3, 'feels_like': 22.7, 'pressure': 1016, 'humidity': 81, 'dew_point': 18.88, 'uvi': 8.39, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 93, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641830400, 'temp': 23.1, 'feels_like': 23.42, 'pressure': 1015, 'humidity': 75, 'dew_point': 18.43, 'uvi': 6.44, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 89, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 22.94, 'feels_like': 23.04, 'pressure': 1014, 'humidity': 67, 'dew_point': 16.49, 'uvi': 7.1, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 84, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 21.79, 'feels_like': 22.01, 'pressure': 1013, 'humidity': 76, 'dew_point': 17.37, 'uvi': 6.51, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 75, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641841200, 'temp': 23.9, 'feels_like': 24.59, 'pressure': 1012, 'humidity': 86, 'dew_point': 21.41, 'uvi': 2.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 57, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641844800, 'temp': 24.73, 'feels_like': 25.63, 'pressure': 1011, 'humidity': 91, 'dew_point': 23.16, 'uvi': 1.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 17, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641848400, 'temp': 24.52, 'feels_like': 25.43, 'pressure': 1011, 'humidity': 92, 'dew_point': 23.13, 'uvi': 0.65, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 13, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641852000, 'temp': 23.53, 'feels_like': 24.37, 'pressure': 1012, 'humidity': 93, 'dew_point': 22.33, 'uvi': 0.21, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 11, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641855600, 'temp': 22.5, 'feels_like': 23.34, 'pressure': 1013, 'humidity': 97, 'dew_point': 22, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 331, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 22.010000 | 23.190000 | 98.000000 | 1014.000000 | 0.11 | 22.340000 | 0.000000 | 10000.000000 | 310.000000 | 1.02 | 1.130000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 01:00:00 | 51.000000 | 21.920000 | 23.090000 | 98.000000 | 1015.000000 |  | 22.250000 | 0.000000 | 10000.000000 | 290.000000 | 1.01 | 1.170000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 02:00:00 | 64.000000 | 20.830000 | 22.050000 | 97.000000 | 1015.000000 |  | 21.330000 | 0.000000 | 10000.000000 | 285.000000 | 0.98 | 1.240000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 03:00:00 | 66.000000 | 20.960000 | 22.030000 | 98.000000 | 1016.000000 |  | 21.290000 | 0.000000 | 10000.000000 | 275.000000 | 1.1 | 1.330000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 04:00:00 | 71.000000 | 20.960000 | 22.030000 | 98.000000 | 1015.000000 |  | 21.290000 | 0.000000 | 10000.000000 | 272.000000 | 1.07 | 1.370000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 05:00:00 | 71.000000 | 19.950000 | 20.920000 | 98.000000 | 1015.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 277.000000 | 1.15 | 1.420000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 06:00:00 | 59.000000 | 19.790000 | 20.900000 | 97.000000 | 1014.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 275.000000 | 1.13 | 1.510000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 07:00:00 | 52.000000 | 19.790000 | 20.900000 | 97.000000 | 1013.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 280.000000 | 1.16 | 1.490000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 08:00:00 | 40.000000 | 19.740000 | 20.840000 | 97.000000 | 1013.000000 |  | 20.230000 | 0.000000 | 10000.000000 | 282.000000 | 1.17 | 1.460000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 09:00:00 | 36.000000 | 18.820000 | 19.830000 | 97.000000 | 1013.000000 |  | 19.310000 | 0.000000 | 10000.000000 | 281.000000 | 1.11 | 1.440000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 10:00:00 | 40.000000 | 19.570000 | 20.820000 | 96.000000 | 1014.000000 |  | 20.230000 | 0.000000 | 10000.000000 | 283.000000 | 1.13 | 1.420000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 11:00:00 | 47.000000 | 18.870000 | 20.030000 | 96.000000 | 1014.000000 |  | 19.520000 | 0.000000 | 10000.000000 | 280.000000 | 1.06 | 1.270000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 12:00:00 | 68.000000 | 19.110000 | 20.790000 | 93.000000 | 1015.000000 | 0.14 | 20.280000 | 0.350000 | 10000.000000 | 288.000000 | 0.83 | 0.970000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 19.020000 | 21.540000 | 88.000000 | 1016.000000 | 0.11 | 21.080000 | 1.930000 | 10000.000000 | 289.000000 | 0.54 | 0.330000 | 500 | Rain | light rain | 10d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 19.590000 | 22.730000 | 85.000000 | 1017.000000 |  | 22.230000 | 4.840000 | 10000.000000 | 85.000000 | 0.94 | 0.610000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 15:00:00 | 69.000000 | 18.880000 | 22.700000 | 81.000000 | 1016.000000 | 0.14 | 22.300000 | 8.390000 | 10000.000000 | 93.000000 | 1.08 | 0.910000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 18.430000 | 23.420000 | 75.000000 | 1015.000000 | 0.11 | 23.100000 | 6.440000 | 10000.000000 | 89.000000 | 1.13 | 1.330000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 16.490000 | 23.040000 | 67.000000 | 1014.000000 |  | 22.940000 | 7.100000 | 10000.000000 | 84.000000 | 1.72 | 1.550000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 18:00:00 | 89.000000 | 17.370000 | 22.010000 | 76.000000 | 1013.000000 | 0.17 | 21.790000 | 6.510000 | 10000.000000 | 75.000000 | 1.85 | 1.310000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 21.410000 | 24.590000 | 86.000000 | 1012.000000 | 0.48 | 23.900000 | 2.710000 | 10000.000000 | 57.000000 | 1.53 | 0.920000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 23.160000 | 25.630000 | 91.000000 | 1011.000000 | 0.56 | 24.730000 | 1.600000 | 10000.000000 | 17.000000 | 1.18 | 0.640000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 23.130000 | 25.430000 | 92.000000 | 1011.000000 | 0.58 | 24.520000 | 0.650000 | 10000.000000 | 13.000000 | 1.27 | 0.650000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 22.330000 | 24.370000 | 93.000000 | 1012.000000 | 0.61 | 23.530000 | 0.210000 | 10000.000000 | 11.000000 | 1.27 | 0.720000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085220 | "SAN CARLOS [23085220]" | 6.157667 | -75.038917 | 1113.000000 | Climática Principal | Convencional | Activa | 1983-05-15 00:00:00 | NaT | Antioquia | San Carlos (Antioquia) | Casanare | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 22.000000 | 23.340000 | 97.000000 | 1013.000000 | 0.49 | 22.500000 | 0.000000 | 10000.000000 | 331.000000 | 0.89 | 0.960000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23085220_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23085220_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23085220_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085220_OWM_Windspeed_20220111.png)
