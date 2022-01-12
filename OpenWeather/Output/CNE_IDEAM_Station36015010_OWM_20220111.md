
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PAZ DE ARIPORO [36015010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station36015010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.87852778,-71.88719444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.87852778&lon=-71.88719444)


| Parameter | Value |
|---|---|
| Code | 36015010 |
| Name | PAZ DE ARIPORO [36015010] |
| Latitude, ° | 5.87852778 |
| Longitude, ° | -71.88719444 |
| Elevation, m | 342 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1995-09-15 00:00:00 |
| Suspension date | NaT |
| State | Casanare |
| County | Paz De Ariporo |
| Stream | Moniquira |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Casanare |
| SZH - Hydrographic subzone | Río Ariporo |

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

### (CNE index 989) Open Weather values for station 36015010 - PAZ DE ARIPORO [36015010]

JSON data from API OWM:

```
{'lat': 5.8785, 'lon': -71.8872, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812447, 'sunset': 1641854938, 'temp': 31.14, 'feels_like': 30.81, 'pressure': 1009, 'humidity': 38, 'dew_point': 15.15, 'uvi': 3.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.36, 'wind_deg': 23, 'wind_gust': 5.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.33, 'feels_like': 25.35, 'pressure': 1012, 'humidity': 55, 'dew_point': 15.65, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 352, 'wind_gust': 5.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 24.24, 'feels_like': 24.26, 'pressure': 1013, 'humidity': 59, 'dew_point': 15.73, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 328, 'wind_gust': 4.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.65, 'feels_like': 23.66, 'pressure': 1013, 'humidity': 61, 'dew_point': 15.69, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 316, 'wind_gust': 2.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.26, 'feels_like': 23.23, 'pressure': 1013, 'humidity': 61, 'dew_point': 15.33, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 312, 'wind_gust': 2.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.05, 'feels_like': 23.03, 'pressure': 1013, 'humidity': 62, 'dew_point': 15.38, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 321, 'wind_gust': 2.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.82, 'feels_like': 22.8, 'pressure': 1013, 'humidity': 63, 'dew_point': 15.41, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 324, 'wind_gust': 2.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.5, 'feels_like': 22.48, 'pressure': 1012, 'humidity': 64, 'dew_point': 15.36, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 332, 'wind_gust': 2.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.32, 'feels_like': 22.28, 'pressure': 1011, 'humidity': 64, 'dew_point': 15.19, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 338, 'wind_gust': 2.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.25, 'feels_like': 22.2, 'pressure': 1011, 'humidity': 64, 'dew_point': 15.12, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 344, 'wind_gust': 3.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 22.35, 'feels_like': 22.31, 'pressure': 1011, 'humidity': 64, 'dew_point': 15.21, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 346, 'wind_gust': 3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 22.54, 'feels_like': 22.49, 'pressure': 1012, 'humidity': 63, 'dew_point': 15.15, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 3, 'wind_gust': 3.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.43, 'feels_like': 22.4, 'pressure': 1012, 'humidity': 64, 'dew_point': 15.29, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 15, 'wind_gust': 4.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.38, 'feels_like': 23.37, 'pressure': 1014, 'humidity': 61, 'dew_point': 15.44, 'uvi': 0.34, 'clouds': 85, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 15, 'wind_gust': 7.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.53, 'feels_like': 25.55, 'pressure': 1015, 'humidity': 54, 'dew_point': 15.54, 'uvi': 2.24, 'clouds': 87, 'visibility': 10000, 'wind_speed': 3.32, 'wind_deg': 26, 'wind_gust': 8.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.22, 'feels_like': 27.43, 'pressure': 1016, 'humidity': 47, 'dew_point': 14.94, 'uvi': 5, 'clouds': 85, 'visibility': 10000, 'wind_speed': 4.14, 'wind_deg': 40, 'wind_gust': 7.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.06, 'feels_like': 28.09, 'pressure': 1016, 'humidity': 45, 'dew_point': 15.02, 'uvi': 8.12, 'clouds': 86, 'visibility': 10000, 'wind_speed': 4.62, 'wind_deg': 46, 'wind_gust': 7.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.18, 'feels_like': 29.09, 'pressure': 1015, 'humidity': 43, 'dew_point': 15.33, 'uvi': 7.7, 'clouds': 88, 'visibility': 10000, 'wind_speed': 4.83, 'wind_deg': 46, 'wind_gust': 6.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.88, 'feels_like': 30.49, 'pressure': 1013, 'humidity': 38, 'dew_point': 14.92, 'uvi': 8.13, 'clouds': 91, 'visibility': 10000, 'wind_speed': 4.95, 'wind_deg': 42, 'wind_gust': 6.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.69, 'feels_like': 31.37, 'pressure': 1012, 'humidity': 37, 'dew_point': 15.22, 'uvi': 7.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.57, 'wind_deg': 34, 'wind_gust': 5.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.59, 'feels_like': 31.24, 'pressure': 1010, 'humidity': 37, 'dew_point': 15.13, 'uvi': 6.02, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.45, 'wind_deg': 28, 'wind_gust': 5.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.14, 'feels_like': 30.81, 'pressure': 1009, 'humidity': 38, 'dew_point': 15.15, 'uvi': 3.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.36, 'wind_deg': 23, 'wind_gust': 5.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.68, 'feels_like': 30.37, 'pressure': 1009, 'humidity': 39, 'dew_point': 15.15, 'uvi': 1.24, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.08, 'wind_deg': 26, 'wind_gust': 5.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.82, 'feels_like': 29.71, 'pressure': 1009, 'humidity': 42, 'dew_point': 15.53, 'uvi': 0.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.64, 'wind_deg': 25, 'wind_gust': 5.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.45, 'feels_like': 27.79, 'pressure': 1010, 'humidity': 49, 'dew_point': 15.79, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 13, 'wind_gust': 7.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 00:00:00 | 63.000000 | 15.650000 | 25.350000 | 55.000000 | 1012.000000 |  | 25.330000 | 0.000000 | 10000.000000 | 352.000000 | 5.68 | 2.310000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 01:00:00 | 74.000000 | 15.730000 | 24.260000 | 59.000000 | 1013.000000 |  | 24.240000 | 0.000000 | 10000.000000 | 328.000000 | 4.02 | 2.100000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 02:00:00 | 64.000000 | 15.690000 | 23.660000 | 61.000000 | 1013.000000 |  | 23.650000 | 0.000000 | 10000.000000 | 316.000000 | 2.94 | 2.040000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 03:00:00 | 73.000000 | 15.330000 | 23.230000 | 61.000000 | 1013.000000 |  | 23.260000 | 0.000000 | 10000.000000 | 312.000000 | 2.29 | 1.950000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 04:00:00 | 73.000000 | 15.380000 | 23.030000 | 62.000000 | 1013.000000 |  | 23.050000 | 0.000000 | 10000.000000 | 321.000000 | 2.04 | 1.770000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 05:00:00 | 76.000000 | 15.410000 | 22.800000 | 63.000000 | 1013.000000 |  | 22.820000 | 0.000000 | 10000.000000 | 324.000000 | 2.03 | 1.680000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 06:00:00 | 59.000000 | 15.360000 | 22.480000 | 64.000000 | 1012.000000 |  | 22.500000 | 0.000000 | 10000.000000 | 332.000000 | 2.33 | 1.670000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 07:00:00 | 68.000000 | 15.190000 | 22.280000 | 64.000000 | 1011.000000 |  | 22.320000 | 0.000000 | 10000.000000 | 338.000000 | 2.46 | 1.640000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 08:00:00 | 64.000000 | 15.120000 | 22.200000 | 64.000000 | 1011.000000 |  | 22.250000 | 0.000000 | 10000.000000 | 344.000000 | 3.06 | 1.810000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 15.210000 | 22.310000 | 64.000000 | 1011.000000 |  | 22.350000 | 0.000000 | 10000.000000 | 346.000000 | 3 | 1.650000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 10:00:00 | 70.000000 | 15.150000 | 22.490000 | 63.000000 | 1012.000000 |  | 22.540000 | 0.000000 | 10000.000000 | 3.000000 | 3.8 | 1.550000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 11:00:00 | 73.000000 | 15.290000 | 22.400000 | 64.000000 | 1012.000000 |  | 22.430000 | 0.000000 | 10000.000000 | 15.000000 | 4.78 | 1.660000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 12:00:00 | 85.000000 | 15.440000 | 23.370000 | 61.000000 | 1014.000000 |  | 23.380000 | 0.340000 | 10000.000000 | 15.000000 | 7.19 | 2.310000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 13:00:00 | 87.000000 | 15.540000 | 25.550000 | 54.000000 | 1015.000000 |  | 25.530000 | 2.240000 | 10000.000000 | 26.000000 | 8.66 | 3.320000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 14.940000 | 27.430000 | 47.000000 | 1016.000000 |  | 27.220000 | 5.000000 | 10000.000000 | 40.000000 | 7.69 | 4.140000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 15:00:00 | 86.000000 | 15.020000 | 28.090000 | 45.000000 | 1016.000000 |  | 28.060000 | 8.120000 | 10000.000000 | 46.000000 | 7.22 | 4.620000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 15.330000 | 29.090000 | 43.000000 | 1015.000000 |  | 29.180000 | 7.700000 | 10000.000000 | 46.000000 | 6.69 | 4.830000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 17:00:00 | 91.000000 | 14.920000 | 30.490000 | 38.000000 | 1013.000000 |  | 30.880000 | 8.130000 | 10000.000000 | 42.000000 | 6.26 | 4.950000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 15.220000 | 31.370000 | 37.000000 | 1012.000000 |  | 31.690000 | 7.140000 | 10000.000000 | 34.000000 | 5.3 | 4.570000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 15.130000 | 31.240000 | 37.000000 | 1010.000000 |  | 31.590000 | 6.020000 | 10000.000000 | 28.000000 | 5.13 | 4.450000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 15.150000 | 30.810000 | 38.000000 | 1009.000000 |  | 31.140000 | 3.300000 | 10000.000000 | 23.000000 | 5.31 | 4.360000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 15.150000 | 30.370000 | 39.000000 | 1009.000000 |  | 30.680000 | 1.240000 | 10000.000000 | 26.000000 | 5.39 | 4.080000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 15.530000 | 29.710000 | 42.000000 | 1009.000000 |  | 29.820000 | 0.220000 | 10000.000000 | 25.000000 | 5.72 | 3.640000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 36015010 | "PAZ DE ARIPORO [36015010]" | 5.878528 | -71.887194 | 342.000000 | Climática Principal | Convencional | Activa | 1995-09-15 00:00:00 | NaT | Casanare | Paz De Ariporo | Moniquira | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Ariporo | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 15.790000 | 27.790000 | 49.000000 | 1010.000000 |  | 27.450000 | 0.000000 | 10000.000000 | 13.000000 | 7.21 | 3.170000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station36015010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station36015010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station36015010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station36015010_OWM_Windspeed_20220111.png)
