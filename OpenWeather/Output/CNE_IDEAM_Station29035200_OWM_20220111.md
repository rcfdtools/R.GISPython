
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - REPELON - AUT [29035200] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035200_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.49,-75.12694444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.49&lon=-75.12694444)


| Parameter | Value |
|---|---|
| Code | 29035200 |
| Name | REPELON - AUT [29035200] |
| Latitude, ° | 10.49 |
| Longitude, ° | -75.12694444 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-09-12 00:00:00 |
| Suspension date | NaT |
| State | Atlantico |
| County | Repelón |
| Stream | Cauca |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Canal del Dique margen derecho |

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

### (CNE index 222) Open Weather values for station 29035200 - REPELON - AUT [29035200]

JSON data from API OWM:

```
{'lat': 10.49, 'lon': -75.1269, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813677, 'sunset': 1641855263, 'temp': 29.95, 'feels_like': 30.39, 'pressure': 1008, 'humidity': 46, 'dew_point': 17.08, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.33, 'wind_deg': 328, 'wind_gust': 3.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.95, 'feels_like': 25.95, 'pressure': 1010, 'humidity': 73, 'dew_point': 20.74, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 2.48, 'wind_deg': 349, 'wind_gust': 3.93, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.95, 'feels_like': 25.95, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.61, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 355, 'wind_gust': 2.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 25.95, 'feels_like': 25.95, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.03, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 5, 'wind_gust': 2.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.95, 'feels_like': 25.59, 'pressure': 1011, 'humidity': 80, 'dew_point': 21.26, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 347, 'wind_gust': 2.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.95, 'feels_like': 25.62, 'pressure': 1011, 'humidity': 81, 'dew_point': 21.46, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 339, 'wind_gust': 2.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.95, 'feels_like': 25.62, 'pressure': 1011, 'humidity': 81, 'dew_point': 21.46, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 340, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.95, 'feels_like': 24.52, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 33, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.95, 'feels_like': 24.52, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 52, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.95, 'feels_like': 24.52, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 40, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.95, 'feels_like': 24.57, 'pressure': 1010, 'humidity': 83, 'dew_point': 20.89, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 62, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.95, 'feels_like': 24.62, 'pressure': 1011, 'humidity': 85, 'dew_point': 21.27, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 116, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.95, 'feels_like': 23.52, 'pressure': 1011, 'humidity': 85, 'dew_point': 20.29, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 98, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.95, 'feels_like': 23.39, 'pressure': 1012, 'humidity': 80, 'dew_point': 19.32, 'uvi': 0.27, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 68, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.95, 'feels_like': 25.17, 'pressure': 1014, 'humidity': 64, 'dew_point': 17.67, 'uvi': 1.41, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 103, 'wind_gust': 3.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.95, 'feels_like': 28.76, 'pressure': 1014, 'humidity': 54, 'dew_point': 17.78, 'uvi': 3.61, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 92, 'wind_gust': 3.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.95, 'feels_like': 29.14, 'pressure': 1014, 'humidity': 46, 'dew_point': 16.17, 'uvi': 6.4, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 107, 'wind_gust': 3.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.95, 'feels_like': 28.47, 'pressure': 1013, 'humidity': 39, 'dew_point': 13.61, 'uvi': 8.59, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 106, 'wind_gust': 2.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.95, 'feels_like': 28.08, 'pressure': 1012, 'humidity': 34, 'dew_point': 11.52, 'uvi': 9.51, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 61, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.95, 'feels_like': 28.86, 'pressure': 1010, 'humidity': 32, 'dew_point': 11.48, 'uvi': 8.71, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 314, 'wind_gust': 2.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.95, 'feels_like': 30.32, 'pressure': 1009, 'humidity': 36, 'dew_point': 14.15, 'uvi': 5.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.67, 'wind_deg': 321, 'wind_gust': 3.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.95, 'feels_like': 30.39, 'pressure': 1008, 'humidity': 46, 'dew_point': 17.08, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.33, 'wind_deg': 328, 'wind_gust': 3.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.95, 'feels_like': 30.37, 'pressure': 1009, 'humidity': 56, 'dew_point': 19.29, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.29, 'wind_deg': 335, 'wind_gust': 5.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.95, 'feels_like': 29.49, 'pressure': 1009, 'humidity': 61, 'dew_point': 19.73, 'uvi': 0.24, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.58, 'wind_deg': 352, 'wind_gust': 5.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.95, 'feels_like': 28.77, 'pressure': 1010, 'humidity': 70, 'dew_point': 21.01, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.25, 'wind_deg': 0, 'wind_gust': 7.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 00:00:00 | 28.000000 | 20.740000 | 25.950000 | 73.000000 | 1010.000000 |  | 25.950000 | 0.000000 | 10000.000000 | 349.000000 | 3.93 | 2.480000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 01:00:00 | 41.000000 | 21.610000 | 25.950000 | 77.000000 | 1011.000000 |  | 25.950000 | 0.000000 | 10000.000000 | 355.000000 | 2.37 | 1.960000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 02:00:00 | 65.000000 | 22.030000 | 25.950000 | 79.000000 | 1011.000000 |  | 25.950000 | 0.000000 | 10000.000000 | 5.000000 | 2.54 | 1.870000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 03:00:00 | 76.000000 | 21.260000 | 25.590000 | 80.000000 | 1011.000000 |  | 24.950000 | 0.000000 | 10000.000000 | 347.000000 | 2.58 | 1.540000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 21.460000 | 25.620000 | 81.000000 | 1011.000000 |  | 24.950000 | 0.000000 | 10000.000000 | 339.000000 | 2.21 | 1.640000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 05:00:00 | 86.000000 | 21.460000 | 25.620000 | 81.000000 | 1011.000000 |  | 24.950000 | 0.000000 | 10000.000000 | 340.000000 | 1.32 | 1.120000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 20.490000 | 24.520000 | 81.000000 | 1010.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 33.000000 | 0.98 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 20.490000 | 24.520000 | 81.000000 | 1010.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 52.000000 | 1.48 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 20.490000 | 24.520000 | 81.000000 | 1010.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 40.000000 | 1.93 | 1.530000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 09:00:00 | 95.000000 | 20.890000 | 24.570000 | 83.000000 | 1010.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 62.000000 | 1.62 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 10:00:00 | 88.000000 | 21.270000 | 24.620000 | 85.000000 | 1011.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 116.000000 | 1.12 | 0.850000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 11:00:00 | 77.000000 | 20.290000 | 23.520000 | 85.000000 | 1011.000000 |  | 22.950000 | 0.000000 | 10000.000000 | 98.000000 | 1.08 | 0.640000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 12:00:00 | 90.000000 | 19.320000 | 23.390000 | 80.000000 | 1012.000000 |  | 22.950000 | 0.270000 | 10000.000000 | 68.000000 | 1.37 | 1.040000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 13:00:00 | 93.000000 | 17.670000 | 25.170000 | 64.000000 | 1014.000000 |  | 24.950000 | 1.410000 | 10000.000000 | 103.000000 | 3.71 | 1.730000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 14:00:00 | 96.000000 | 17.780000 | 28.760000 | 54.000000 | 1014.000000 |  | 27.950000 | 3.610000 | 10000.000000 | 92.000000 | 3.49 | 2.110000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 16.170000 | 29.140000 | 46.000000 | 1014.000000 |  | 28.950000 | 6.400000 | 10000.000000 | 107.000000 | 3.48 | 2.240000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 16:00:00 | 97.000000 | 13.610000 | 28.470000 | 39.000000 | 1013.000000 |  | 28.950000 | 8.590000 | 10000.000000 | 106.000000 | 2.92 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 11.520000 | 28.080000 | 34.000000 | 1012.000000 |  | 28.950000 | 9.510000 | 10000.000000 | 61.000000 | 2.06 | 0.460000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 11.480000 | 28.860000 | 32.000000 | 1010.000000 |  | 29.950000 | 8.710000 | 10000.000000 | 314.000000 | 2.42 | 1.510000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 14.150000 | 30.320000 | 36.000000 | 1009.000000 |  | 30.950000 | 5.990000 | 10000.000000 | 321.000000 | 3.39 | 3.670000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 17.080000 | 30.390000 | 46.000000 | 1008.000000 |  | 29.950000 | 3.450000 | 10000.000000 | 328.000000 | 3.9 | 5.330000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 19.290000 | 30.370000 | 56.000000 | 1009.000000 |  | 28.950000 | 1.380000 | 10000.000000 | 335.000000 | 5.5 | 5.290000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 19.730000 | 29.490000 | 61.000000 | 1009.000000 |  | 27.950000 | 0.240000 | 10000.000000 | 352.000000 | 5.99 | 4.580000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035200 | "REPELON - AUT [29035200]" | 10.490000 | -75.126944 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 00:00:00 | NaT | Atlantico | Repelón | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 21.010000 | 28.770000 | 70.000000 | 1010.000000 |  | 26.950000 | 0.000000 | 10000.000000 | 0.000000 | 7.88 | 4.250000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035200_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035200_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035200_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035200_OWM_Windspeed_20220111.png)
