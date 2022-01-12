
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ISLAS DEL ROSARIO [14015060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station14015060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.18333333,-75.75) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.18333333&lon=-75.75)


| Parameter | Value |
|---|---|
| Code | 14015060 |
| Name | ISLAS DEL ROSARIO [14015060] |
| Latitude, ° | 10.18333333 |
| Longitude, ° | -75.75 |
| Elevation, m | 3 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1983-12-15 00:00:00 |
| Suspension date | 1996-08-15 00:00:00 |
| State | Bolívar |
| County | Cartagena De Indias |
| Stream | Cno Caribona |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Bajo Sinú |

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

### (CNE index 267) Open Weather values for station 14015060 - ISLAS DEL ROSARIO [14015060]

JSON data from API OWM:

```
{'lat': 10.1833, 'lon': -75.75, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813796, 'sunset': 1641855443, 'temp': 30.01, 'feels_like': 35.81, 'pressure': 1009, 'humidity': 73, 'dew_point': 24.64, 'uvi': 3.53, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.92, 'wind_deg': 350, 'wind_gust': 5.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1010, 'humidity': 73, 'dew_point': 20.8, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 9.76, 'wind_deg': 23, 'wind_gust': 9.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 76, 'dew_point': 21.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 9.85, 'wind_deg': 27, 'wind_gust': 10.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1012, 'humidity': 76, 'dew_point': 21.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 9.12, 'wind_deg': 25, 'wind_gust': 9.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.01, 'feels_like': 25.55, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.17, 'wind_deg': 29, 'wind_gust': 8.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.01, 'feels_like': 25.52, 'pressure': 1011, 'humidity': 75, 'dew_point': 20.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 6.89, 'wind_deg': 32, 'wind_gust': 7.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.01, 'feels_like': 25.5, 'pressure': 1011, 'humidity': 74, 'dew_point': 20.05, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 6.41, 'wind_deg': 37, 'wind_gust': 6.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.01, 'feels_like': 24.4, 'pressure': 1010, 'humidity': 74, 'dew_point': 19.09, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 6.58, 'wind_deg': 37, 'wind_gust': 6.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.01, 'feels_like': 24.37, 'pressure': 1010, 'humidity': 73, 'dew_point': 18.87, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 5.23, 'wind_deg': 41, 'wind_gust': 5.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.01, 'feels_like': 24.35, 'pressure': 1009, 'humidity': 72, 'dew_point': 18.65, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 3.67, 'wind_deg': 59, 'wind_gust': 3.64, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 24.01, 'feels_like': 24.35, 'pressure': 1009, 'humidity': 72, 'dew_point': 18.65, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 2.74, 'wind_deg': 85, 'wind_gust': 2.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 24.01, 'feels_like': 24.4, 'pressure': 1010, 'humidity': 74, 'dew_point': 19.09, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.09, 'wind_deg': 101, 'wind_gust': 3.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 23.01, 'feels_like': 23.3, 'pressure': 1011, 'humidity': 74, 'dew_point': 18.13, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 5.08, 'wind_deg': 98, 'wind_gust': 5.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.01, 'feels_like': 23.22, 'pressure': 1012, 'humidity': 71, 'dew_point': 17.47, 'uvi': 0.27, 'clouds': 36, 'visibility': 10000, 'wind_speed': 4.83, 'wind_deg': 85, 'wind_gust': 5.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 25.01, 'feels_like': 25.29, 'pressure': 1013, 'humidity': 66, 'dew_point': 18.22, 'uvi': 1.35, 'clouds': 15, 'visibility': 10000, 'wind_speed': 5.26, 'wind_deg': 90, 'wind_gust': 6.3, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.01, 'feels_like': 29.58, 'pressure': 1014, 'humidity': 61, 'dew_point': 19.79, 'uvi': 3.53, 'clouds': 46, 'visibility': 10000, 'wind_speed': 5.37, 'wind_deg': 102, 'wind_gust': 6.39, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 29.01, 'feels_like': 30.9, 'pressure': 1014, 'humidity': 59, 'dew_point': 20.19, 'uvi': 6.3, 'clouds': 64, 'visibility': 10000, 'wind_speed': 4.13, 'wind_deg': 90, 'wind_gust': 5.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.01, 'feels_like': 30.75, 'pressure': 1013, 'humidity': 58, 'dew_point': 19.91, 'uvi': 8.29, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 56, 'wind_gust': 3.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.01, 'feels_like': 30.9, 'pressure': 1012, 'humidity': 59, 'dew_point': 20.19, 'uvi': 9.24, 'clouds': 78, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 358, 'wind_gust': 3.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.01, 'feels_like': 34.59, 'pressure': 1011, 'humidity': 68, 'dew_point': 23.46, 'uvi': 8.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.4, 'wind_deg': 343, 'wind_gust': 4.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.01, 'feels_like': 37.93, 'pressure': 1010, 'humidity': 71, 'dew_point': 25.13, 'uvi': 6.05, 'clouds': 100, 'visibility': 10000, 'wind_speed': 6.04, 'wind_deg': 343, 'wind_gust': 5.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.01, 'feels_like': 35.81, 'pressure': 1009, 'humidity': 73, 'dew_point': 24.64, 'uvi': 3.53, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.92, 'wind_deg': 350, 'wind_gust': 5.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.01, 'feels_like': 33.52, 'pressure': 1009, 'humidity': 74, 'dew_point': 23.9, 'uvi': 1.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 6.42, 'wind_deg': 359, 'wind_gust': 5.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.01, 'feels_like': 31.24, 'pressure': 1010, 'humidity': 74, 'dew_point': 22.94, 'uvi': 0.31, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.1, 'wind_deg': 5, 'wind_gust': 6.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.01, 'feels_like': 29.3, 'pressure': 1010, 'humidity': 75, 'dew_point': 22.2, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.18, 'wind_deg': 8, 'wind_gust': 7.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 00:00:00 | 99.000000 | 20.800000 | 26.010000 | 73.000000 | 1010.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 23.000000 | 9.24 | 9.760000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 21.450000 | 26.010000 | 76.000000 | 1011.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 27.000000 | 10.03 | 9.850000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 21.450000 | 26.010000 | 76.000000 | 1012.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 25.000000 | 9.19 | 9.120000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 20.490000 | 25.550000 | 76.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 29.000000 | 8.63 | 8.170000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 20.270000 | 25.520000 | 75.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 32.000000 | 7.51 | 6.890000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 20.050000 | 25.500000 | 74.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 37.000000 | 6.92 | 6.410000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 06:00:00 | 86.000000 | 19.090000 | 24.400000 | 74.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 37.000000 | 6.83 | 6.580000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 18.870000 | 24.370000 | 73.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 41.000000 | 5.29 | 5.230000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 08:00:00 | 46.000000 | 18.650000 | 24.350000 | 72.000000 | 1009.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 59.000000 | 3.64 | 3.670000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 09:00:00 | 35.000000 | 18.650000 | 24.350000 | 72.000000 | 1009.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 85.000000 | 2.63 | 2.740000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 10:00:00 | 40.000000 | 19.090000 | 24.400000 | 74.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 101.000000 | 3.97 | 4.090000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 11:00:00 | 52.000000 | 18.130000 | 23.300000 | 74.000000 | 1011.000000 |  | 23.010000 | 0.000000 | 10000.000000 | 98.000000 | 5.49 | 5.080000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 12:00:00 | 36.000000 | 17.470000 | 23.220000 | 71.000000 | 1012.000000 |  | 23.010000 | 0.270000 | 10000.000000 | 85.000000 | 5.56 | 4.830000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 13:00:00 | 15.000000 | 18.220000 | 25.290000 | 66.000000 | 1013.000000 |  | 25.010000 | 1.350000 | 10000.000000 | 90.000000 | 6.3 | 5.260000 | 801 | Clouds | few clouds | 02d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 14:00:00 | 46.000000 | 19.790000 | 29.580000 | 61.000000 | 1014.000000 |  | 28.010000 | 3.530000 | 10000.000000 | 102.000000 | 6.39 | 5.370000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 15:00:00 | 64.000000 | 20.190000 | 30.900000 | 59.000000 | 1014.000000 |  | 29.010000 | 6.300000 | 10000.000000 | 90.000000 | 5.32 | 4.130000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 16:00:00 | 73.000000 | 19.910000 | 30.750000 | 58.000000 | 1013.000000 |  | 29.010000 | 8.290000 | 10000.000000 | 56.000000 | 3.65 | 2.600000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 17:00:00 | 78.000000 | 20.190000 | 30.900000 | 59.000000 | 1012.000000 |  | 29.010000 | 9.240000 | 10000.000000 | 358.000000 | 3.14 | 3.190000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 23.460000 | 34.590000 | 68.000000 | 1011.000000 |  | 30.010000 | 8.510000 | 10000.000000 | 343.000000 | 4.9 | 5.400000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 25.130000 | 37.930000 | 71.000000 | 1010.000000 |  | 31.010000 | 6.050000 | 10000.000000 | 343.000000 | 5.51 | 6.040000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 24.640000 | 35.810000 | 73.000000 | 1009.000000 |  | 30.010000 | 3.530000 | 10000.000000 | 350.000000 | 5.33 | 5.920000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 23.900000 | 33.520000 | 74.000000 | 1009.000000 |  | 29.010000 | 1.430000 | 10000.000000 | 359.000000 | 5.81 | 6.420000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 22.940000 | 31.240000 | 74.000000 | 1010.000000 |  | 28.010000 | 0.310000 | 10000.000000 | 5.000000 | 6.42 | 7.100000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015060 | "ISLAS DEL ROSARIO [14015060]" | 10.183333 | -75.750000 | 3.000000 | Climática Principal | Convencional | Suspendida | 1983-12-15 00:00:00 | 1996-08-15 00:00:00 | Bolívar | Cartagena De Indias | Cno Caribona | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 22.200000 | 29.300000 | 75.000000 | 1010.000000 |  | 27.010000 | 0.000000 | 10000.000000 | 8.000000 | 7.83 | 8.180000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station14015060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station14015060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station14015060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015060_OWM_Windspeed_20220111.png)
