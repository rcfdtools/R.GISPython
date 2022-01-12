
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LAGUNA LA PLAZA [35095130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35095130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.362,-72.28201667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.362&lon=-72.28201667)


| Parameter | Value |
|---|---|
| Code | 35095130 |
| Name | LAGUNA LA PLAZA [35095130] |
| Latitude, ° | 6.362 |
| Longitude, ° | -72.28201667 |
| Elevation, m | 4378 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2010-09-17 00:00:00 |
| Suspension date | NaT |
| State | Arauca |
| County | Saravena |
| Stream | Cauca |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Casanare |
| SZH - Hydrographic subzone | Río Casanare |

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

### (CNE index 842) Open Weather values for station 35095130 - LAGUNA LA PLAZA [35095130]

JSON data from API OWM:

```
{'lat': 6.362, 'lon': -72.282, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812588, 'sunset': 1641854986, 'temp': 4.14, 'feels_like': 4.14, 'pressure': 1015, 'humidity': 74, 'dew_point': -0.06, 'uvi': 4.62, 'clouds': 99, 'visibility': 7960, 'wind_speed': 0.4, 'wind_deg': 215, 'wind_gust': 2.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 0.56, 'feels_like': 0.56, 'pressure': 1019, 'humidity': 93, 'dew_point': -0.39, 'uvi': 0, 'clouds': 59, 'visibility': 1678, 'wind_speed': 1.11, 'wind_deg': 316, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 0.03, 'feels_like': 0.03, 'pressure': 1020, 'humidity': 93, 'dew_point': -0.85, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 316, 'wind_gust': 1.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': -0.58, 'feels_like': -2.59, 'pressure': 1021, 'humidity': 93, 'dew_point': -1.45, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 311, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': -1.02, 'feels_like': -3.27, 'pressure': 1021, 'humidity': 91, 'dew_point': -2.15, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 312, 'wind_gust': 1.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': -1.5, 'feels_like': -3.77, 'pressure': 1021, 'humidity': 90, 'dew_point': -2.76, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 319, 'wind_gust': 1.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': -1.67, 'feels_like': -4.32, 'pressure': 1021, 'humidity': 90, 'dew_point': -2.93, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 314, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': -1.97, 'feels_like': -4.37, 'pressure': 1020, 'humidity': 91, 'dew_point': -3.09, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 309, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': -2.14, 'feels_like': -4.89, 'pressure': 1019, 'humidity': 89, 'dew_point': -3.53, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 313, 'wind_gust': 1.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': -2.58, 'feels_like': -5.45, 'pressure': 1019, 'humidity': 87, 'dew_point': -4.23, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 310, 'wind_gust': 1.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': -2.7, 'feels_like': -5.75, 'pressure': 1019, 'humidity': 83, 'dew_point': -4.9, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 308, 'wind_gust': 1.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': -2.85, 'feels_like': -5.72, 'pressure': 1019, 'humidity': 80, 'dew_point': -5.48, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 308, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': -2.9, 'feels_like': -5.86, 'pressure': 1020, 'humidity': 78, 'dew_point': -5.82, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 305, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': -0.43, 'feels_like': -0.43, 'pressure': 1020, 'humidity': 74, 'dew_point': -4.03, 'uvi': 0.33, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 302, 'wind_gust': 1.49, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 2, 'feels_like': 2, 'pressure': 1020, 'humidity': 68, 'dew_point': -2.9, 'uvi': 2.17, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 221, 'wind_gust': 1.39, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 3.57, 'feels_like': 3.57, 'pressure': 1020, 'humidity': 65, 'dew_point': -2.11, 'uvi': 4.94, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 167, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 4.54, 'feels_like': 4.54, 'pressure': 1019, 'humidity': 65, 'dew_point': -1.29, 'uvi': 8.11, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 166, 'wind_gust': 2.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 4.67, 'feels_like': 4.67, 'pressure': 1019, 'humidity': 67, 'dew_point': -0.82, 'uvi': 12.58, 'clouds': 71, 'visibility': 8849, 'wind_speed': 1.02, 'wind_deg': 179, 'wind_gust': 2.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 4.79, 'feels_like': 4.79, 'pressure': 1018, 'humidity': 67, 'dew_point': -0.71, 'uvi': 13.38, 'clouds': 71, 'visibility': 8126, 'wind_speed': 0.93, 'wind_deg': 187, 'wind_gust': 2.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 4.59, 'feels_like': 4.59, 'pressure': 1017, 'humidity': 71, 'dew_point': -0.18, 'uvi': 11.82, 'clouds': 98, 'visibility': 8112, 'wind_speed': 0.65, 'wind_deg': 206, 'wind_gust': 2.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 4.62, 'feels_like': 4.62, 'pressure': 1016, 'humidity': 71, 'dew_point': -0.16, 'uvi': 8.37, 'clouds': 98, 'visibility': 8061, 'wind_speed': 0.41, 'wind_deg': 203, 'wind_gust': 2.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 4.14, 'feels_like': 4.14, 'pressure': 1015, 'humidity': 74, 'dew_point': -0.06, 'uvi': 4.62, 'clouds': 99, 'visibility': 7960, 'wind_speed': 0.4, 'wind_deg': 215, 'wind_gust': 2.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 3.43, 'feels_like': 3.43, 'pressure': 1015, 'humidity': 77, 'dew_point': -0.19, 'uvi': 1.75, 'clouds': 98, 'visibility': 7956, 'wind_speed': 0.52, 'wind_deg': 255, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 2.34, 'feels_like': 2.34, 'pressure': 1016, 'humidity': 83, 'dew_point': -0.22, 'uvi': 0.32, 'clouds': 98, 'visibility': 7967, 'wind_speed': 0.68, 'wind_deg': 271, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 0.32, 'feels_like': 0.32, 'pressure': 1018, 'humidity': 92, 'dew_point': -0.73, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 293, 'wind_gust': 1.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 00:00:00 | 59.000000 | -0.390000 | 0.560000 | 93.000000 | 1019.000000 |  | 0.560000 | 0.000000 | 1678.000000 | 316.000000 | 1.33 | 1.110000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 01:00:00 | 73.000000 | -0.850000 | 0.030000 | 93.000000 | 1020.000000 |  | 0.030000 | 0.000000 | 10000.000000 | 316.000000 | 1.28 | 1.170000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 02:00:00 | 63.000000 | -1.450000 | -2.590000 | 93.000000 | 1021.000000 |  | -0.580000 | 0.000000 | 10000.000000 | 311.000000 | 1.61 | 1.610000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 03:00:00 | 75.000000 | -2.150000 | -3.270000 | 91.000000 | 1021.000000 |  | -1.020000 | 0.000000 | 10000.000000 | 312.000000 | 1.65 | 1.730000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 04:00:00 | 81.000000 | -2.760000 | -3.770000 | 90.000000 | 1021.000000 |  | -1.500000 | 0.000000 | 10000.000000 | 319.000000 | 1.62 | 1.690000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 05:00:00 | 83.000000 | -2.930000 | -4.320000 | 90.000000 | 1021.000000 |  | -1.670000 | 0.000000 | 10000.000000 | 314.000000 | 1.76 | 1.940000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 06:00:00 | 66.000000 | -3.090000 | -4.370000 | 91.000000 | 1020.000000 |  | -1.970000 | 0.000000 | 10000.000000 | 309.000000 | 1.61 | 1.730000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 07:00:00 | 70.000000 | -3.530000 | -4.890000 | 89.000000 | 1019.000000 |  | -2.140000 | 0.000000 | 10000.000000 | 313.000000 | 1.73 | 1.960000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 08:00:00 | 68.000000 | -4.230000 | -5.450000 | 87.000000 | 1019.000000 |  | -2.580000 | 0.000000 | 10000.000000 | 310.000000 | 1.78 | 1.990000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 09:00:00 | 68.000000 | -4.900000 | -5.750000 | 83.000000 | 1019.000000 |  | -2.700000 | 0.000000 | 10000.000000 | 308.000000 | 1.88 | 2.110000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 10:00:00 | 68.000000 | -5.480000 | -5.720000 | 80.000000 | 1019.000000 |  | -2.850000 | 0.000000 | 10000.000000 | 308.000000 | 1.75 | 1.960000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 11:00:00 | 58.000000 | -5.820000 | -5.860000 | 78.000000 | 1020.000000 |  | -2.900000 | 0.000000 | 10000.000000 | 305.000000 | 1.79 | 2.020000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 12:00:00 | 34.000000 | -4.030000 | -0.430000 | 74.000000 | 1020.000000 |  | -0.430000 | 0.330000 | 10000.000000 | 302.000000 | 1.49 | 1.280000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 13:00:00 | 45.000000 | -2.900000 | 2.000000 | 68.000000 | 1020.000000 |  | 2.000000 | 2.170000 | 10000.000000 | 221.000000 | 1.39 | 0.410000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 14:00:00 | 71.000000 | -2.110000 | 3.570000 | 65.000000 | 1020.000000 |  | 3.570000 | 4.940000 | 10000.000000 | 167.000000 | 1.7 | 0.950000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | -1.290000 | 4.540000 | 65.000000 | 1019.000000 |  | 4.540000 | 8.110000 | 10000.000000 | 166.000000 | 2.07 | 1.260000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 16:00:00 | 71.000000 | -0.820000 | 4.670000 | 67.000000 | 1019.000000 |  | 4.670000 | 12.580000 | 8849.000000 | 179.000000 | 2.45 | 1.020000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 17:00:00 | 71.000000 | -0.710000 | 4.790000 | 67.000000 | 1018.000000 |  | 4.790000 | 13.380000 | 8126.000000 | 187.000000 | 2.66 | 0.930000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | -0.180000 | 4.590000 | 71.000000 | 1017.000000 |  | 4.590000 | 11.820000 | 8112.000000 | 206.000000 | 2.42 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | -0.160000 | 4.620000 | 71.000000 | 1016.000000 |  | 4.620000 | 8.370000 | 8061.000000 | 203.000000 | 2.24 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | -0.060000 | 4.140000 | 74.000000 | 1015.000000 |  | 4.140000 | 4.620000 | 7960.000000 | 215.000000 | 2.21 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | -0.190000 | 3.430000 | 77.000000 | 1015.000000 |  | 3.430000 | 1.750000 | 7956.000000 | 255.000000 | 2.16 | 0.520000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | -0.220000 | 2.340000 | 83.000000 | 1016.000000 |  | 2.340000 | 0.320000 | 7967.000000 | 271.000000 | 1.59 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095130 | "LAGUNA LA PLAZA [35095130]" | 6.362000 | -72.282017 | 4378.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-09-17 00:00:00 | NaT | Arauca | Saravena | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Casanare | Río Casanare | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | -0.730000 | 0.320000 | 92.000000 | 1018.000000 |  | 0.320000 | 0.000000 | 10000.000000 | 293.000000 | 1.19 | 1.060000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35095130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35095130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35095130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095130_OWM_Windspeed_20220111.png)
