
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - DON ANTONIO CAMELI [35095020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35095020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.68333333,-73.03333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.68333333&lon=-73.03333333)


| Parameter | Value |
|---|---|
| Code | 35095020 |
| Name | DON ANTONIO CAMELI [35095020] |
| Latitude, ° | 4.68333333 |
| Longitude, ° | -73.03333333 |
| Elevation, m | 300 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-10-15 00:00:00 |
| Suspension date | 1993-05-15 00:00:00 |
| State | Casanare |
| County | Sabanalarga (Casanare) |
| Stream | San Juan |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Upía |

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

### (CNE index 1170) Open Weather values for station 35095020 - DON ANTONIO CAMELI [35095020]

JSON data from API OWM:

```
{'lat': 4.6833, 'lon': -73.0333, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812606, 'sunset': 1641855329, 'temp': 31.91, 'feels_like': 31.65, 'pressure': 1008, 'humidity': 37, 'dew_point': 15.42, 'uvi': 2.71, 'clouds': 78, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 78, 'wind_gust': 3.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.2, 'feels_like': 27.61, 'pressure': 1011, 'humidity': 50, 'dew_point': 15.88, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 23, 'wind_gust': 2.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.81, 'feels_like': 27.3, 'pressure': 1012, 'humidity': 51, 'dew_point': 15.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 25, 'wind_gust': 2.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.71, 'feels_like': 27.2, 'pressure': 1013, 'humidity': 51, 'dew_point': 15.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 24, 'wind_gust': 3.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.86, 'feels_like': 25.89, 'pressure': 1013, 'humidity': 53, 'dew_point': 15.56, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 25, 'wind_gust': 3.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.75, 'feels_like': 24.77, 'pressure': 1013, 'humidity': 57, 'dew_point': 15.66, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 340, 'wind_gust': 2.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.05, 'feels_like': 24.08, 'pressure': 1012, 'humidity': 60, 'dew_point': 15.81, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 313, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.91, 'feels_like': 23.95, 'pressure': 1011, 'humidity': 61, 'dew_point': 15.94, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 314, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.57, 'feels_like': 23.6, 'pressure': 1011, 'humidity': 62, 'dew_point': 15.87, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 326, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.26, 'feels_like': 24.31, 'pressure': 1010, 'humidity': 60, 'dew_point': 16.01, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 332, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.16, 'feels_like': 24.22, 'pressure': 1010, 'humidity': 61, 'dew_point': 16.17, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 327, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.11, 'feels_like': 24.17, 'pressure': 1011, 'humidity': 61, 'dew_point': 16.12, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 335, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.62, 'feels_like': 23.68, 'pressure': 1012, 'humidity': 63, 'dew_point': 16.17, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 12, 'wind_gust': 0.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.62, 'feels_like': 24.73, 'pressure': 1013, 'humidity': 61, 'dew_point': 16.6, 'uvi': 0.25, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 17, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.75, 'feels_like': 25.87, 'pressure': 1015, 'humidity': 57, 'dew_point': 16.6, 'uvi': 2.12, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 87, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.54, 'feels_like': 26.54, 'pressure': 1015, 'humidity': 54, 'dew_point': 16.48, 'uvi': 4.93, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 83, 'wind_gust': 3.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.26, 'feels_like': 27.67, 'pressure': 1015, 'humidity': 50, 'dew_point': 15.94, 'uvi': 8.18, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 72, 'wind_gust': 3.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.74, 'feels_like': 29.74, 'pressure': 1014, 'humidity': 43, 'dew_point': 15.83, 'uvi': 8.56, 'clouds': 91, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 66, 'wind_gust': 3.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 31.95, 'feels_like': 31.71, 'pressure': 1012, 'humidity': 37, 'dew_point': 15.45, 'uvi': 9.21, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.79, 'wind_deg': 74, 'wind_gust': 3.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 32.24, 'feels_like': 32.1, 'pressure': 1011, 'humidity': 37, 'dew_point': 15.71, 'uvi': 8.25, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.92, 'wind_deg': 79, 'wind_gust': 3.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 32.83, 'feels_like': 32.74, 'pressure': 1009, 'humidity': 36, 'dew_point': 15.8, 'uvi': 4.76, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 79, 'wind_gust': 2.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.91, 'feels_like': 31.65, 'pressure': 1008, 'humidity': 37, 'dew_point': 15.42, 'uvi': 2.71, 'clouds': 78, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 78, 'wind_gust': 3.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.38, 'feels_like': 30.4, 'pressure': 1008, 'humidity': 42, 'dew_point': 16.04, 'uvi': 1.06, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 86, 'wind_gust': 3.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.89, 'feels_like': 29.18, 'pressure': 1009, 'humidity': 47, 'dew_point': 16.45, 'uvi': 0.23, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 64, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.94, 'feels_like': 28.3, 'pressure': 1009, 'humidity': 49, 'dew_point': 16.24, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 353, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 00:00:00 | 97.000000 | 15.880000 | 27.610000 | 50.000000 | 1011.000000 |  | 27.200000 | 0.000000 | 10000.000000 | 23.000000 | 2.42 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 15.830000 | 27.300000 | 51.000000 | 1012.000000 |  | 26.810000 | 0.000000 | 10000.000000 | 25.000000 | 2.73 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 15.740000 | 27.200000 | 51.000000 | 1013.000000 |  | 26.710000 | 0.000000 | 10000.000000 | 24.000000 | 3.43 | 1.310000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 15.560000 | 25.890000 | 53.000000 | 1013.000000 |  | 25.860000 | 0.000000 | 10000.000000 | 25.000000 | 3.28 | 1.260000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 04:00:00 | 92.000000 | 15.660000 | 24.770000 | 57.000000 | 1013.000000 |  | 24.750000 | 0.000000 | 10000.000000 | 340.000000 | 2.04 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 15.810000 | 24.080000 | 60.000000 | 1012.000000 |  | 24.050000 | 0.000000 | 10000.000000 | 313.000000 | 1.37 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 06:00:00 | 57.000000 | 15.940000 | 23.950000 | 61.000000 | 1011.000000 |  | 23.910000 | 0.000000 | 10000.000000 | 314.000000 | 1.15 | 1.250000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 07:00:00 | 76.000000 | 15.870000 | 23.600000 | 62.000000 | 1011.000000 |  | 23.570000 | 0.000000 | 10000.000000 | 326.000000 | 1.02 | 1.040000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 08:00:00 | 87.000000 | 16.010000 | 24.310000 | 60.000000 | 1010.000000 |  | 24.260000 | 0.000000 | 10000.000000 | 332.000000 | 0.88 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 09:00:00 | 91.000000 | 16.170000 | 24.220000 | 61.000000 | 1010.000000 |  | 24.160000 | 0.000000 | 10000.000000 | 327.000000 | 0.75 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 16.120000 | 24.170000 | 61.000000 | 1011.000000 |  | 24.110000 | 0.000000 | 10000.000000 | 335.000000 | 0.57 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 11:00:00 | 94.000000 | 16.170000 | 23.680000 | 63.000000 | 1012.000000 |  | 23.620000 | 0.000000 | 10000.000000 | 12.000000 | 0.48 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 12:00:00 | 92.000000 | 16.600000 | 24.730000 | 61.000000 | 1013.000000 |  | 24.620000 | 0.250000 | 10000.000000 | 17.000000 | 0.91 | 0.330000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 16.600000 | 25.870000 | 57.000000 | 1015.000000 |  | 25.750000 | 2.120000 | 10000.000000 | 87.000000 | 1.87 | 0.690000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 16.480000 | 26.540000 | 54.000000 | 1015.000000 |  | 26.540000 | 4.930000 | 10000.000000 | 83.000000 | 3.12 | 1.250000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 15:00:00 | 96.000000 | 15.940000 | 27.670000 | 50.000000 | 1015.000000 |  | 27.260000 | 8.180000 | 10000.000000 | 72.000000 | 3.91 | 1.960000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 16:00:00 | 91.000000 | 15.830000 | 29.740000 | 43.000000 | 1014.000000 |  | 29.740000 | 8.560000 | 10000.000000 | 66.000000 | 3.77 | 3.100000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 17:00:00 | 86.000000 | 15.450000 | 31.710000 | 37.000000 | 1012.000000 |  | 31.950000 | 9.210000 | 10000.000000 | 74.000000 | 3.04 | 2.790000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 18:00:00 | 52.000000 | 15.710000 | 32.100000 | 37.000000 | 1011.000000 |  | 32.240000 | 8.250000 | 10000.000000 | 79.000000 | 3.01 | 2.920000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 19:00:00 | 61.000000 | 15.800000 | 32.740000 | 36.000000 | 1009.000000 |  | 32.830000 | 4.760000 | 10000.000000 | 79.000000 | 2.69 | 2.690000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 20:00:00 | 78.000000 | 15.420000 | 31.650000 | 37.000000 | 1008.000000 |  | 31.910000 | 2.710000 | 10000.000000 | 78.000000 | 3.19 | 2.540000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 21:00:00 | 85.000000 | 16.040000 | 30.400000 | 42.000000 | 1008.000000 |  | 30.380000 | 1.060000 | 10000.000000 | 86.000000 | 3.9 | 1.870000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 16.450000 | 29.180000 | 47.000000 | 1009.000000 |  | 28.890000 | 0.230000 | 10000.000000 | 64.000000 | 1.14 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095020 | "DON ANTONIO CAMELI [35095020]" | 4.683333 | -73.033333 | 300.000000 | Climática Principal | Convencional | Suspendida | 1968-10-15 00:00:00 | 1993-05-15 00:00:00 | Casanare | Sabanalarga (Casanare) | San Juan | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Upía | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 16.240000 | 28.300000 | 49.000000 | 1009.000000 |  | 27.940000 | 0.000000 | 10000.000000 | 353.000000 | 0.82 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35095020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35095020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35095020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095020_OWM_Windspeed_20220111.png)
