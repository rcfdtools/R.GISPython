
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO RAFAEL BARVO [25025080] - Historical

### General parameters

* Weather date time: 2022-01-11 19:01:08.491859
* Unix time to eval: 1641841268
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
* CNE IDEAM station code filter: ['All']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['All']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.33388889,-75.28305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.33388889&lon=-75.28305556)


| Parameter | Value |
|---|---|
| Code | 25025080 |
| Name | AEROPUERTO RAFAEL BARVO [25025080] |
| Latitude, ° | 9.33388889 |
| Longitude, ° | -75.28305556 |
| Elevation, m | 166 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1940-06-15 00:00:00 |
| Suspension date | NaT |
| State | Sucre |
| County | Corozal |
| Stream | Ay Libra Arriba |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena- Cauca -San Jorge |
| SZH - Hydrographic subzone | Bajo San Jorge - La Mojana |

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

### (CNE index 2606) Open Weather values for station 25025080 - AEROPUERTO RAFAEL BARVO [25025080]

JSON data from API OWM:

```
{'lat': 9.3339, 'lon': -75.2831, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641841268, 'sunrise': 1641813600, 'sunset': 1641855415, 'temp': 30.36, 'feels_like': 30.24, 'pressure': 1010, 'humidity': 41, 'dew_point': 15.64, 'uvi': 5.89, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 163, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 23.96, 'feels_like': 24.66, 'pressure': 1010, 'humidity': 86, 'dew_point': 21.47, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 4.39, 'wind_deg': 306, 'wind_gust': 7.36, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 23.89, 'feels_like': 24.58, 'pressure': 1011, 'humidity': 86, 'dew_point': 21.41, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 4.83, 'wind_deg': 320, 'wind_gust': 8.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.64, 'feels_like': 24.28, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.97, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3.98, 'wind_deg': 324, 'wind_gust': 7.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.44, 'feels_like': 24.01, 'pressure': 1012, 'humidity': 83, 'dew_point': 20.39, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.87, 'wind_deg': 321, 'wind_gust': 5.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.25, 'feels_like': 23.77, 'pressure': 1011, 'humidity': 82, 'dew_point': 20.01, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 316, 'wind_gust': 3.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.13, 'feels_like': 23.56, 'pressure': 1011, 'humidity': 79, 'dew_point': 19.29, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 313, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.04, 'feels_like': 23.41, 'pressure': 1011, 'humidity': 77, 'dew_point': 18.79, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 305, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.85, 'feels_like': 23.18, 'pressure': 1010, 'humidity': 76, 'dew_point': 18.4, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 295, 'wind_gust': 0.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.6, 'feels_like': 22.93, 'pressure': 1010, 'humidity': 77, 'dew_point': 18.37, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 11, 'wind_gust': 0.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 22.28, 'feels_like': 22.63, 'pressure': 1010, 'humidity': 79, 'dew_point': 18.46, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 67, 'wind_gust': 1.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.84, 'feels_like': 22.22, 'pressure': 1011, 'humidity': 82, 'dew_point': 18.63, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 76, 'wind_gust': 2.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.46, 'feels_like': 21.83, 'pressure': 1012, 'humidity': 83, 'dew_point': 18.45, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 77, 'wind_gust': 2.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.93, 'feels_like': 22.27, 'pressure': 1013, 'humidity': 80, 'dew_point': 18.32, 'uvi': 0.29, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 80, 'wind_gust': 3.48, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 24, 'feels_like': 24.26, 'pressure': 1014, 'humidity': 69, 'dew_point': 17.96, 'uvi': 1.54, 'clouds': 15, 'visibility': 10000, 'wind_speed': 2.87, 'wind_deg': 88, 'wind_gust': 3.81, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 26, 'feels_like': 26, 'pressure': 1014, 'humidity': 63, 'dew_point': 18.41, 'uvi': 3.93, 'clouds': 16, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 99, 'wind_gust': 3.87, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 27.75, 'feels_like': 28.89, 'pressure': 1014, 'humidity': 58, 'dew_point': 18.74, 'uvi': 6.93, 'clouds': 37, 'visibility': 10000, 'wind_speed': 3.39, 'wind_deg': 102, 'wind_gust': 3.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 29.13, 'feels_like': 30.09, 'pressure': 1013, 'humidity': 52, 'dew_point': 18.27, 'uvi': 8.67, 'clouds': 45, 'visibility': 10000, 'wind_speed': 3.24, 'wind_deg': 108, 'wind_gust': 3.33, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 29.89, 'feels_like': 30.59, 'pressure': 1012, 'humidity': 48, 'dew_point': 17.7, 'uvi': 9.59, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.72, 'wind_deg': 113, 'wind_gust': 2.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.32, 'feels_like': 30.32, 'pressure': 1011, 'humidity': 42, 'dew_point': 15.98, 'uvi': 8.78, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 117, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.36, 'feels_like': 30.24, 'pressure': 1010, 'humidity': 41, 'dew_point': 15.64, 'uvi': 5.89, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 163, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.23, 'feels_like': 30.21, 'pressure': 1009, 'humidity': 42, 'dew_point': 15.9, 'uvi': 3.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 242, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.85, 'feels_like': 30.12, 'pressure': 1009, 'humidity': 45, 'dew_point': 16.64, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 285, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.27, 'feels_like': 29.5, 'pressure': 1009, 'humidity': 57, 'dew_point': 18.94, 'uvi': 0.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 297, 'wind_gust': 3.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 25.41, 'feels_like': 25.81, 'pressure': 1010, 'humidity': 69, 'dew_point': 19.31, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.23, 'wind_deg': 304, 'wind_gust': 4.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 00:00:00 | 83.000000 | 21.470000 | 24.660000 | 86.000000 | 1010.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 306.000000 | 7.36 | 4.390000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 21.410000 | 24.580000 | 86.000000 | 1011.000000 |  | 23.890000 | 0.000000 | 10000.000000 | 320.000000 | 8.27 | 4.830000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | 20.970000 | 24.280000 | 85.000000 | 1012.000000 |  | 23.640000 | 0.000000 | 10000.000000 | 324.000000 | 7.45 | 3.980000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 20.390000 | 24.010000 | 83.000000 | 1012.000000 |  | 23.440000 | 0.000000 | 10000.000000 | 321.000000 | 5.78 | 2.870000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 20.010000 | 23.770000 | 82.000000 | 1011.000000 |  | 23.250000 | 0.000000 | 10000.000000 | 316.000000 | 3.87 | 2.260000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 19.290000 | 23.560000 | 79.000000 | 1011.000000 |  | 23.130000 | 0.000000 | 10000.000000 | 313.000000 | 1.72 | 1.510000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 06:00:00 | 62.000000 | 18.790000 | 23.410000 | 77.000000 | 1011.000000 |  | 23.040000 | 0.000000 | 10000.000000 | 305.000000 | 1.01 | 0.900000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 07:00:00 | 74.000000 | 18.400000 | 23.180000 | 76.000000 | 1010.000000 |  | 22.850000 | 0.000000 | 10000.000000 | 295.000000 | 0.77 | 0.520000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 08:00:00 | 59.000000 | 18.370000 | 22.930000 | 77.000000 | 1010.000000 |  | 22.600000 | 0.000000 | 10000.000000 | 11.000000 | 0.98 | 0.630000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 09:00:00 | 59.000000 | 18.460000 | 22.630000 | 79.000000 | 1010.000000 |  | 22.280000 | 0.000000 | 10000.000000 | 67.000000 | 1.53 | 1.390000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 18.630000 | 22.220000 | 82.000000 | 1011.000000 |  | 21.840000 | 0.000000 | 10000.000000 | 76.000000 | 2.39 | 2.280000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 11:00:00 | 58.000000 | 18.450000 | 21.830000 | 83.000000 | 1012.000000 |  | 21.460000 | 0.000000 | 10000.000000 | 77.000000 | 2.86 | 2.420000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 12:00:00 | 5.000000 | 18.320000 | 22.270000 | 80.000000 | 1013.000000 |  | 21.930000 | 0.290000 | 10000.000000 | 80.000000 | 3.48 | 2.460000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 13:00:00 | 15.000000 | 17.960000 | 24.260000 | 69.000000 | 1014.000000 |  | 24.000000 | 1.540000 | 10000.000000 | 88.000000 | 3.81 | 2.870000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 14:00:00 | 16.000000 | 18.410000 | 26.000000 | 63.000000 | 1014.000000 |  | 26.000000 | 3.930000 | 10000.000000 | 99.000000 | 3.87 | 3.090000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 15:00:00 | 37.000000 | 18.740000 | 28.890000 | 58.000000 | 1014.000000 |  | 27.750000 | 6.930000 | 10000.000000 | 102.000000 | 3.88 | 3.390000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 16:00:00 | 45.000000 | 18.270000 | 30.090000 | 52.000000 | 1013.000000 |  | 29.130000 | 8.670000 | 10000.000000 | 108.000000 | 3.33 | 3.240000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 17:00:00 | 56.000000 | 17.700000 | 30.590000 | 48.000000 | 1012.000000 |  | 29.890000 | 9.590000 | 10000.000000 | 113.000000 | 2.68 | 2.720000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 15.980000 | 30.320000 | 42.000000 | 1011.000000 |  | 30.320000 | 8.780000 | 10000.000000 | 117.000000 | 1.85 | 1.910000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 15.640000 | 30.240000 | 41.000000 | 1010.000000 |  | 30.360000 | 5.890000 | 10000.000000 | 163.000000 | 0.91 | 0.830000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 15.900000 | 30.210000 | 42.000000 | 1009.000000 |  | 30.230000 | 3.420000 | 10000.000000 | 242.000000 | 1 | 0.900000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 16.640000 | 30.120000 | 45.000000 | 1009.000000 |  | 29.850000 | 1.380000 | 10000.000000 | 285.000000 | 1.59 | 1.560000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 18.940000 | 29.500000 | 57.000000 | 1009.000000 |  | 28.270000 | 0.320000 | 10000.000000 | 297.000000 | 3.06 | 2.260000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 19.310000 | 25.810000 | 69.000000 | 1010.000000 |  | 25.410000 | 0.000000 | 10000.000000 | 304.000000 | 4.64 | 3.230000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025080_OWM_Windspeed_20220111.png)
