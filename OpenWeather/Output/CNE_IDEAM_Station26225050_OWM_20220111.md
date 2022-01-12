
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PALMAR EL [26225050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26225050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.11666667,-75.66666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.11666667&lon=-75.66666667)


| Parameter | Value |
|---|---|
| Code | 26225050 |
| Name | PALMAR EL [26225050] |
| Latitude, ° | 7.11666667 |
| Longitude, ° | -75.66666667 |
| Elevation, m | 580 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1982-11-15 00:00:00 |
| Suspension date | 1992-11-15 00:00:00 |
| State | Antioquia |
| County | Ituango |
| Stream | Cga. San Silvestre |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Directos Río Cauca entre Río San Juan y Pto Valdia |

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

### (CNE index 4036) Open Weather values for station 26225050 - PALMAR EL [26225050]

JSON data from API OWM:

```
{'lat': 7.1167, 'lon': -75.6667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813475, 'sunset': 1641855725, 'temp': 27.07, 'feels_like': 30.09, 'pressure': 1012, 'humidity': 82, 'dew_point': 23.73, 'uvi': 2.51, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 7, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, 'hourly': [{'dt': 1641772800, 'temp': 23.45, 'feels_like': 24.41, 'pressure': 1015, 'humidity': 98, 'dew_point': 23.12, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 35, 'wind_gust': 0.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 23.18, 'feels_like': 24.09, 'pressure': 1016, 'humidity': 97, 'dew_point': 22.68, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 292, 'wind_gust': 0.65, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 22.93, 'feels_like': 23.81, 'pressure': 1017, 'humidity': 97, 'dew_point': 22.43, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 233, 'wind_gust': 0.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.64, 'feels_like': 23.47, 'pressure': 1017, 'humidity': 96, 'dew_point': 21.97, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 207, 'wind_gust': 0.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.36, 'feels_like': 23.16, 'pressure': 1016, 'humidity': 96, 'dew_point': 21.69, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 215, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.02, 'feels_like': 22.78, 'pressure': 1016, 'humidity': 96, 'dew_point': 21.35, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 201, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 21.76, 'feels_like': 22.5, 'pressure': 1016, 'humidity': 96, 'dew_point': 21.09, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 200, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.49, 'feels_like': 22.2, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.83, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 203, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.26, 'feels_like': 21.95, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.6, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 206, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.04, 'feels_like': 21.71, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.38, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 223, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.98, 'feels_like': 21.64, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.32, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 215, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.89, 'feels_like': 21.54, 'pressure': 1016, 'humidity': 96, 'dew_point': 20.23, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 227, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.6, 'feels_like': 22.24, 'pressure': 1017, 'humidity': 93, 'dew_point': 20.42, 'uvi': 0.33, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 218, 'wind_gust': 0.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 24.39, 'feels_like': 25.1, 'pressure': 1017, 'humidity': 85, 'dew_point': 21.7, 'uvi': 1.65, 'clouds': 13, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 10, 'wind_gust': 0.49, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 26.66, 'feels_like': 26.66, 'pressure': 1017, 'humidity': 75, 'dew_point': 21.86, 'uvi': 4.21, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 29, 'wind_gust': 0.65, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 28.42, 'feels_like': 30.91, 'pressure': 1017, 'humidity': 66, 'dew_point': 21.45, 'uvi': 7.4, 'clouds': 35, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 28, 'wind_gust': 1.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 29.31, 'feels_like': 32.09, 'pressure': 1015, 'humidity': 63, 'dew_point': 21.54, 'uvi': 8.6, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 32, 'wind_gust': 1.18, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 29.27, 'feels_like': 32.19, 'pressure': 1015, 'humidity': 64, 'dew_point': 21.76, 'uvi': 9.57, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 32, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 28.57, 'feels_like': 31.81, 'pressure': 1014, 'humidity': 70, 'dew_point': 22.56, 'uvi': 8.82, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 21, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641841200, 'temp': 27.57, 'feels_like': 30.67, 'pressure': 1013, 'humidity': 77, 'dew_point': 23.17, 'uvi': 4.25, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 8, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641844800, 'temp': 27.07, 'feels_like': 30.09, 'pressure': 1012, 'humidity': 82, 'dew_point': 23.73, 'uvi': 2.51, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 7, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641848400, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1012, 'humidity': 88, 'dew_point': 24.13, 'uvi': 1.04, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 21, 'wind_gust': 2.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641852000, 'temp': 25.25, 'feels_like': 26.34, 'pressure': 1013, 'humidity': 96, 'dew_point': 24.57, 'uvi': 0.21, 'clouds': 98, 'visibility': 7657, 'wind_speed': 1, 'wind_deg': 26, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641855600, 'temp': 24.02, 'feels_like': 25.04, 'pressure': 1014, 'humidity': 98, 'dew_point': 23.68, 'uvi': 0, 'clouds': 99, 'visibility': 9928, 'wind_speed': 0.76, 'wind_deg': 31, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 00:00:00 | 32.000000 | 23.120000 | 24.410000 | 98.000000 | 1015.000000 |  | 23.450000 | 0.000000 | 10000.000000 | 35.000000 | 0.69 | 0.170000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 01:00:00 | 46.000000 | 22.680000 | 24.090000 | 97.000000 | 1016.000000 |  | 23.180000 | 0.000000 | 10000.000000 | 292.000000 | 0.65 | 0.170000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 02:00:00 | 51.000000 | 22.430000 | 23.810000 | 97.000000 | 1017.000000 |  | 22.930000 | 0.000000 | 10000.000000 | 233.000000 | 0.72 | 0.260000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 03:00:00 | 54.000000 | 21.970000 | 23.470000 | 96.000000 | 1017.000000 |  | 22.640000 | 0.000000 | 10000.000000 | 207.000000 | 0.79 | 0.430000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 04:00:00 | 64.000000 | 21.690000 | 23.160000 | 96.000000 | 1016.000000 |  | 22.360000 | 0.000000 | 10000.000000 | 215.000000 | 0.87 | 0.740000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 05:00:00 | 70.000000 | 21.350000 | 22.780000 | 96.000000 | 1016.000000 |  | 22.020000 | 0.000000 | 10000.000000 | 201.000000 | 0.83 | 0.670000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 06:00:00 | 80.000000 | 21.090000 | 22.500000 | 96.000000 | 1016.000000 |  | 21.760000 | 0.000000 | 10000.000000 | 200.000000 | 0.85 | 0.730000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 20.830000 | 22.200000 | 96.000000 | 1015.000000 |  | 21.490000 | 0.000000 | 10000.000000 | 203.000000 | 0.82 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 08:00:00 | 85.000000 | 20.600000 | 21.950000 | 96.000000 | 1014.000000 |  | 21.260000 | 0.000000 | 10000.000000 | 206.000000 | 0.91 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 09:00:00 | 73.000000 | 20.380000 | 21.710000 | 96.000000 | 1015.000000 |  | 21.040000 | 0.000000 | 10000.000000 | 223.000000 | 1.09 | 1.050000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 10:00:00 | 65.000000 | 20.320000 | 21.640000 | 96.000000 | 1015.000000 |  | 20.980000 | 0.000000 | 10000.000000 | 215.000000 | 1.09 | 0.970000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 11:00:00 | 58.000000 | 20.230000 | 21.540000 | 96.000000 | 1016.000000 |  | 20.890000 | 0.000000 | 10000.000000 | 227.000000 | 1.21 | 1.080000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 12:00:00 | 8.000000 | 20.420000 | 22.240000 | 93.000000 | 1017.000000 |  | 21.600000 | 0.330000 | 10000.000000 | 218.000000 | 0.96 | 0.670000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 13:00:00 | 13.000000 | 21.700000 | 25.100000 | 85.000000 | 1017.000000 |  | 24.390000 | 1.650000 | 10000.000000 | 10.000000 | 0.49 | 0.140000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 21.860000 | 26.660000 | 75.000000 | 1017.000000 |  | 26.660000 | 4.210000 | 10000.000000 | 29.000000 | 0.65 | 0.810000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 15:00:00 | 35.000000 | 21.450000 | 30.910000 | 66.000000 | 1017.000000 |  | 28.420000 | 7.400000 | 10000.000000 | 28.000000 | 1.02 | 1.210000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 16:00:00 | 46.000000 | 21.540000 | 32.090000 | 63.000000 | 1015.000000 |  | 29.310000 | 8.600000 | 10000.000000 | 32.000000 | 1.18 | 1.620000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 17:00:00 | 55.000000 | 21.760000 | 32.190000 | 64.000000 | 1015.000000 |  | 29.270000 | 9.570000 | 10000.000000 | 32.000000 | 1.29 | 1.740000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | 22.560000 | 31.810000 | 70.000000 | 1014.000000 | 0.12 | 28.570000 | 8.820000 | 10000.000000 | 21.000000 | 1.37 | 1.670000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 19:00:00 | 94.000000 | 23.170000 | 30.670000 | 77.000000 | 1013.000000 | 0.23 | 27.570000 | 4.250000 | 10000.000000 | 8.000000 | 1.81 | 1.590000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 20:00:00 | 97.000000 | 23.730000 | 30.090000 | 82.000000 | 1012.000000 | 0.34 | 27.070000 | 2.510000 | 10000.000000 | 7.000000 | 1.9 | 1.530000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 24.130000 | 26.280000 | 88.000000 | 1012.000000 | 0.46 | 26.280000 | 1.040000 | 10000.000000 | 21.000000 | 2.02 | 1.310000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 24.570000 | 26.340000 | 96.000000 | 1013.000000 | 0.62 | 25.250000 | 0.210000 | 7657.000000 | 26.000000 | 1.93 | 1.000000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26225050 | "PALMAR EL [26225050]" | 7.116667 | -75.666667 | 580.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 1992-11-15 00:00:00 | Antioquia | Ituango | Cga. San Silvestre | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos Río Cauca entre Río San Juan y Pto Valdia | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 23.680000 | 25.040000 | 98.000000 | 1014.000000 | 0.29 | 24.020000 | 0.000000 | 9928.000000 | 31.000000 | 1.26 | 0.760000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26225050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26225050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26225050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26225050_OWM_Windspeed_20220111.png)
