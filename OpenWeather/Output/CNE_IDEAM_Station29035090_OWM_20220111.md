
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - INGENIO SANTA CRUZ [29035090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.13333333,-75.25) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.13333333&lon=-75.25)


| Parameter | Value |
|---|---|
| Code | 29035090 |
| Name | INGENIO SANTA CRUZ [29035090] |
| Latitude, ° | 10.13333333 |
| Longitude, ° | -75.25 |
| Elevation, m | 9 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-02-15 00:00:00 |
| Suspension date | 1976-09-15 00:00:00 |
| State | Bolívar |
| County | Mahates |
| Stream | Mulatos |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Canal del Dique margen izquierda |

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

### (CNE index 2985) Open Weather values for station 29035090 - INGENIO SANTA CRUZ [29035090]

JSON data from API OWM:

```
{'lat': 10.1333, 'lon': -75.25, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813671, 'sunset': 1641855328, 'temp': 29.92, 'feels_like': 29.28, 'pressure': 1008, 'humidity': 37, 'dew_point': 13.66, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.81, 'wind_deg': 251, 'wind_gust': 2.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.92, 'feels_like': 26.5, 'pressure': 1010, 'humidity': 74, 'dew_point': 20.93, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 296, 'wind_gust': 1.95, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.92, 'feels_like': 26.55, 'pressure': 1011, 'humidity': 76, 'dew_point': 21.36, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 272, 'wind_gust': 1.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 25.92, 'feels_like': 26.55, 'pressure': 1012, 'humidity': 76, 'dew_point': 21.36, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 174, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.92, 'feels_like': 25.45, 'pressure': 1012, 'humidity': 76, 'dew_point': 20.4, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 308, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.92, 'feels_like': 25.48, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.61, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.06, 'wind_deg': 282, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.92, 'feels_like': 25.45, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.4, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 168, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.92, 'feels_like': 24.38, 'pressure': 1010, 'humidity': 77, 'dew_point': 19.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 161, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.92, 'feels_like': 24.38, 'pressure': 1010, 'humidity': 77, 'dew_point': 19.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 121, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.92, 'feels_like': 24.4, 'pressure': 1010, 'humidity': 78, 'dew_point': 19.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 90, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.92, 'feels_like': 24.43, 'pressure': 1010, 'humidity': 79, 'dew_point': 20.06, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 89, 'wind_gust': 2.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.92, 'feels_like': 24.46, 'pressure': 1011, 'humidity': 80, 'dew_point': 20.26, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 102, 'wind_gust': 2.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.92, 'feels_like': 23.25, 'pressure': 1011, 'humidity': 76, 'dew_point': 18.47, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 109, 'wind_gust': 3.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.92, 'feels_like': 23.04, 'pressure': 1012, 'humidity': 68, 'dew_point': 16.7, 'uvi': 0.27, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.72, 'wind_deg': 113, 'wind_gust': 8.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.92, 'feels_like': 24.98, 'pressure': 1013, 'humidity': 58, 'dew_point': 16.09, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.4, 'wind_deg': 111, 'wind_gust': 9.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.92, 'feels_like': 28.45, 'pressure': 1014, 'humidity': 51, 'dew_point': 16.85, 'uvi': 3.61, 'clouds': 98, 'visibility': 10000, 'wind_speed': 4.94, 'wind_deg': 110, 'wind_gust': 7.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.92, 'feels_like': 29, 'pressure': 1014, 'humidity': 45, 'dew_point': 15.8, 'uvi': 6.4, 'clouds': 98, 'visibility': 10000, 'wind_speed': 4.69, 'wind_deg': 112, 'wind_gust': 6.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.92, 'feels_like': 28.53, 'pressure': 1013, 'humidity': 40, 'dew_point': 13.97, 'uvi': 8.59, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.94, 'wind_deg': 122, 'wind_gust': 4.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.92, 'feels_like': 28.28, 'pressure': 1012, 'humidity': 37, 'dew_point': 12.78, 'uvi': 9.51, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.89, 'wind_deg': 137, 'wind_gust': 3.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.92, 'feels_like': 29, 'pressure': 1011, 'humidity': 34, 'dew_point': 12.37, 'uvi': 8.71, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 171, 'wind_gust': 2.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.92, 'feels_like': 29.94, 'pressure': 1009, 'humidity': 33, 'dew_point': 12.79, 'uvi': 5.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 224, 'wind_gust': 2.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.92, 'feels_like': 29.28, 'pressure': 1008, 'humidity': 37, 'dew_point': 13.66, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.81, 'wind_deg': 251, 'wind_gust': 2.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.92, 'feels_like': 29.68, 'pressure': 1008, 'humidity': 51, 'dew_point': 17.77, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.96, 'wind_deg': 276, 'wind_gust': 4.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.92, 'feels_like': 30.02, 'pressure': 1009, 'humidity': 66, 'dew_point': 20.98, 'uvi': 0.24, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.04, 'wind_deg': 302, 'wind_gust': 6.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.92, 'feels_like': 29.05, 'pressure': 1010, 'humidity': 74, 'dew_point': 21.89, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.11, 'wind_deg': 329, 'wind_gust': 5.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 00:00:00 | 43.000000 | 20.930000 | 26.500000 | 74.000000 | 1010.000000 |  | 25.920000 | 0.000000 | 10000.000000 | 296.000000 | 1.95 | 1.370000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 01:00:00 | 48.000000 | 21.360000 | 26.550000 | 76.000000 | 1011.000000 |  | 25.920000 | 0.000000 | 10000.000000 | 272.000000 | 1.15 | 0.680000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 21.360000 | 26.550000 | 76.000000 | 1012.000000 |  | 25.920000 | 0.000000 | 10000.000000 | 174.000000 | 0.94 | 0.180000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 03:00:00 | 82.000000 | 20.400000 | 25.450000 | 76.000000 | 1012.000000 |  | 24.920000 | 0.000000 | 10000.000000 | 308.000000 | 0.9 | 0.210000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 04:00:00 | 87.000000 | 20.610000 | 25.480000 | 77.000000 | 1011.000000 |  | 24.920000 | 0.000000 | 10000.000000 | 282.000000 | 0.8 | 0.060000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 05:00:00 | 89.000000 | 20.400000 | 25.450000 | 76.000000 | 1011.000000 |  | 24.920000 | 0.000000 | 10000.000000 | 168.000000 | 0.67 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 19.640000 | 24.380000 | 77.000000 | 1010.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 161.000000 | 0.63 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.640000 | 24.380000 | 77.000000 | 1010.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 121.000000 | 0.85 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 19.850000 | 24.400000 | 78.000000 | 1010.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 90.000000 | 1.34 | 1.300000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 09:00:00 | 71.000000 | 20.060000 | 24.430000 | 79.000000 | 1010.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 89.000000 | 2.14 | 2.150000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 20.260000 | 24.460000 | 80.000000 | 1011.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 102.000000 | 2.28 | 2.190000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 11:00:00 | 57.000000 | 18.470000 | 23.250000 | 76.000000 | 1011.000000 |  | 22.920000 | 0.000000 | 10000.000000 | 109.000000 | 3.02 | 2.410000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 16.700000 | 23.040000 | 68.000000 | 1012.000000 |  | 22.920000 | 0.270000 | 10000.000000 | 113.000000 | 8.91 | 2.720000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.090000 | 24.980000 | 58.000000 | 1013.000000 |  | 24.920000 | 1.410000 | 10000.000000 | 111.000000 | 9.71 | 4.400000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 16.850000 | 28.450000 | 51.000000 | 1014.000000 |  | 27.920000 | 3.610000 | 10000.000000 | 110.000000 | 7.57 | 4.940000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 15.800000 | 29.000000 | 45.000000 | 1014.000000 |  | 28.920000 | 6.400000 | 10000.000000 | 112.000000 | 6.01 | 4.690000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 13.970000 | 28.530000 | 40.000000 | 1013.000000 |  | 28.920000 | 8.590000 | 10000.000000 | 122.000000 | 4.31 | 3.940000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 12.780000 | 28.280000 | 37.000000 | 1012.000000 |  | 28.920000 | 9.510000 | 10000.000000 | 137.000000 | 3.07 | 2.890000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 12.370000 | 29.000000 | 34.000000 | 1011.000000 |  | 29.920000 | 8.710000 | 10000.000000 | 171.000000 | 2.28 | 2.110000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 12.790000 | 29.940000 | 33.000000 | 1009.000000 |  | 30.920000 | 5.990000 | 10000.000000 | 224.000000 | 2.01 | 2.140000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 13.660000 | 29.280000 | 37.000000 | 1008.000000 |  | 29.920000 | 3.450000 | 10000.000000 | 251.000000 | 2.9 | 3.810000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 17.770000 | 29.680000 | 51.000000 | 1008.000000 |  | 28.920000 | 1.380000 | 10000.000000 | 276.000000 | 4.42 | 4.960000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 20.980000 | 30.020000 | 66.000000 | 1009.000000 |  | 27.920000 | 0.240000 | 10000.000000 | 302.000000 | 6.58 | 4.040000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035090 | "INGENIO SANTA CRUZ [29035090]" | 10.133333 | -75.250000 | 9.000000 | Climática Principal | Convencional | Suspendida | 1968-02-15 00:00:00 | 1976-09-15 00:00:00 | Bolívar | Mahates | Mulatos | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 21.890000 | 29.050000 | 74.000000 | 1010.000000 |  | 26.920000 | 0.000000 | 10000.000000 | 329.000000 | 5.66 | 3.110000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035090_OWM_Windspeed_20220111.png)
