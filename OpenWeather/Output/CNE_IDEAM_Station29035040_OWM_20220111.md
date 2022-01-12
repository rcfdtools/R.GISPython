
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NUEVA FLORIDA [29035040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.94416667,-75.35138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.94416667&lon=-75.35138889)


| Parameter | Value |
|---|---|
| Code | 29035040 |
| Name | NUEVA FLORIDA [29035040] |
| Latitude, ° | 9.94416667 |
| Longitude, ° | -75.35138889 |
| Elevation, m | 13 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1963-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | María La Baja |
| Stream | Canal Principal |
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

### (CNE index 3157) Open Weather values for station 29035040 - NUEVA FLORIDA [29035040]

JSON data from API OWM:

```
{'lat': 9.9442, 'lon': -75.3514, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813677, 'sunset': 1641855371, 'temp': 29.93, 'feels_like': 30.65, 'pressure': 1009, 'humidity': 48, 'dew_point': 17.73, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.93, 'wind_deg': 285, 'wind_gust': 3.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.93, 'feels_like': 26.64, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.01, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 327, 'wind_gust': 2.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.93, 'feels_like': 26.64, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.01, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 340, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.93, 'feels_like': 26.62, 'pressure': 1012, 'humidity': 78, 'dew_point': 21.8, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 293, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.93, 'feels_like': 25.52, 'pressure': 1012, 'humidity': 78, 'dew_point': 20.83, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 286, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.93, 'feels_like': 25.49, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.62, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 190, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.93, 'feels_like': 25.46, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.41, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 147, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.93, 'feels_like': 24.39, 'pressure': 1010, 'humidity': 77, 'dew_point': 19.65, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 137, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.93, 'feels_like': 24.36, 'pressure': 1010, 'humidity': 76, 'dew_point': 19.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 142, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.93, 'feels_like': 24.36, 'pressure': 1010, 'humidity': 76, 'dew_point': 19.44, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 114, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.93, 'feels_like': 24.39, 'pressure': 1010, 'humidity': 77, 'dew_point': 19.65, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 105, 'wind_gust': 1.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.93, 'feels_like': 24.39, 'pressure': 1011, 'humidity': 77, 'dew_point': 19.65, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 108, 'wind_gust': 2.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.93, 'feels_like': 23.26, 'pressure': 1011, 'humidity': 76, 'dew_point': 18.48, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 2.37, 'wind_deg': 109, 'wind_gust': 2.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.93, 'feels_like': 23.13, 'pressure': 1012, 'humidity': 71, 'dew_point': 17.39, 'uvi': 0.28, 'clouds': 81, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 119, 'wind_gust': 5.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.93, 'feels_like': 25.07, 'pressure': 1013, 'humidity': 61, 'dew_point': 16.9, 'uvi': 1.48, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.99, 'wind_deg': 114, 'wind_gust': 6.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.93, 'feels_like': 28.64, 'pressure': 1014, 'humidity': 53, 'dew_point': 17.47, 'uvi': 3.78, 'clouds': 80, 'visibility': 10000, 'wind_speed': 3.34, 'wind_deg': 120, 'wind_gust': 5.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.93, 'feels_like': 29.34, 'pressure': 1014, 'humidity': 48, 'dew_point': 16.82, 'uvi': 6.69, 'clouds': 85, 'visibility': 10000, 'wind_speed': 3.31, 'wind_deg': 120, 'wind_gust': 4.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.93, 'feels_like': 28.91, 'pressure': 1013, 'humidity': 44, 'dew_point': 15.46, 'uvi': 8.76, 'clouds': 88, 'visibility': 10000, 'wind_speed': 3.04, 'wind_deg': 124, 'wind_gust': 3.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.93, 'feels_like': 28.63, 'pressure': 1012, 'humidity': 41, 'dew_point': 14.36, 'uvi': 9.7, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 131, 'wind_gust': 2.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.93, 'feels_like': 29.5, 'pressure': 1011, 'humidity': 39, 'dew_point': 14.48, 'uvi': 8.88, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 243, 'wind_gust': 1.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.93, 'feels_like': 31.12, 'pressure': 1010, 'humidity': 42, 'dew_point': 16.53, 'uvi': 5.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 281, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.93, 'feels_like': 30.65, 'pressure': 1009, 'humidity': 48, 'dew_point': 17.73, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.93, 'wind_deg': 285, 'wind_gust': 3.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.93, 'feels_like': 31.07, 'pressure': 1009, 'humidity': 61, 'dew_point': 20.65, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.47, 'wind_deg': 288, 'wind_gust': 4.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.93, 'feels_like': 30.53, 'pressure': 1009, 'humidity': 70, 'dew_point': 21.95, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.24, 'wind_deg': 292, 'wind_gust': 5.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.93, 'feels_like': 29.23, 'pressure': 1010, 'humidity': 76, 'dew_point': 22.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 316, 'wind_gust': 4.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 00:00:00 | 76.000000 | 22.010000 | 26.640000 | 79.000000 | 1011.000000 |  | 25.930000 | 0.000000 | 10000.000000 | 327.000000 | 2.21 | 1.030000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 01:00:00 | 85.000000 | 22.010000 | 26.640000 | 79.000000 | 1011.000000 |  | 25.930000 | 0.000000 | 10000.000000 | 340.000000 | 1.76 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 02:00:00 | 92.000000 | 21.800000 | 26.620000 | 78.000000 | 1012.000000 |  | 25.930000 | 0.000000 | 10000.000000 | 293.000000 | 1.3 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 03:00:00 | 95.000000 | 20.830000 | 25.520000 | 78.000000 | 1012.000000 |  | 24.930000 | 0.000000 | 10000.000000 | 286.000000 | 1.05 | 0.450000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 04:00:00 | 96.000000 | 20.620000 | 25.490000 | 77.000000 | 1011.000000 |  | 24.930000 | 0.000000 | 10000.000000 | 190.000000 | 0.97 | 0.130000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 20.410000 | 25.460000 | 76.000000 | 1011.000000 |  | 24.930000 | 0.000000 | 10000.000000 | 147.000000 | 1.09 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 19.650000 | 24.390000 | 77.000000 | 1010.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 137.000000 | 1.04 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.440000 | 24.360000 | 76.000000 | 1010.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 142.000000 | 0.95 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 19.440000 | 24.360000 | 76.000000 | 1010.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 114.000000 | 1.16 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 19.650000 | 24.390000 | 77.000000 | 1010.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 105.000000 | 1.66 | 1.730000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 10:00:00 | 53.000000 | 19.650000 | 24.390000 | 77.000000 | 1011.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 108.000000 | 2.16 | 2.130000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 11:00:00 | 62.000000 | 18.480000 | 23.260000 | 76.000000 | 1011.000000 |  | 22.930000 | 0.000000 | 10000.000000 | 109.000000 | 2.6 | 2.370000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 12:00:00 | 81.000000 | 17.390000 | 23.130000 | 71.000000 | 1012.000000 |  | 22.930000 | 0.280000 | 10000.000000 | 119.000000 | 5.31 | 2.470000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 13:00:00 | 87.000000 | 16.900000 | 25.070000 | 61.000000 | 1013.000000 |  | 24.930000 | 1.480000 | 10000.000000 | 114.000000 | 6.69 | 2.990000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 14:00:00 | 80.000000 | 17.470000 | 28.640000 | 53.000000 | 1014.000000 |  | 27.930000 | 3.780000 | 10000.000000 | 120.000000 | 5.6 | 3.340000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 15:00:00 | 85.000000 | 16.820000 | 29.340000 | 48.000000 | 1014.000000 |  | 28.930000 | 6.690000 | 10000.000000 | 120.000000 | 4.51 | 3.310000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 15.460000 | 28.910000 | 44.000000 | 1013.000000 |  | 28.930000 | 8.760000 | 10000.000000 | 124.000000 | 3.44 | 3.040000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 17:00:00 | 91.000000 | 14.360000 | 28.630000 | 41.000000 | 1012.000000 |  | 28.930000 | 9.700000 | 10000.000000 | 131.000000 | 2.4 | 1.750000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 14.480000 | 29.500000 | 39.000000 | 1011.000000 |  | 29.930000 | 8.880000 | 10000.000000 | 243.000000 | 1.99 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 16.530000 | 31.120000 | 42.000000 | 1010.000000 |  | 30.930000 | 5.940000 | 10000.000000 | 281.000000 | 2.11 | 2.610000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 17.730000 | 30.650000 | 48.000000 | 1009.000000 |  | 29.930000 | 3.430000 | 10000.000000 | 285.000000 | 3.4 | 3.930000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 20.650000 | 31.070000 | 61.000000 | 1009.000000 |  | 28.930000 | 1.380000 | 10000.000000 | 288.000000 | 4.94 | 4.470000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 21.950000 | 30.530000 | 70.000000 | 1009.000000 |  | 27.930000 | 0.270000 | 10000.000000 | 292.000000 | 5.57 | 3.240000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035040 | "NUEVA FLORIDA [29035040]" | 9.944167 | -75.351389 | 13.000000 | Climática Principal | Convencional | Activa | 1963-01-15 00:00:00 | NaT | Bolívar | María La Baja | Canal Principal | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 22.340000 | 29.230000 | 76.000000 | 1010.000000 |  | 26.930000 | 0.000000 | 10000.000000 | 316.000000 | 4.18 | 2.540000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035040_OWM_Windspeed_20220111.png)
