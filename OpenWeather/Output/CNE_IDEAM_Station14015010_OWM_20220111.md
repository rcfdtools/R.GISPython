
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GALERAZAMBA  - AUT [14015010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station14015010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.79416667,-75.26055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.79416667&lon=-75.26055556)


| Parameter | Value |
|---|---|
| Code | 14015010 |
| Name | GALERAZAMBA  - AUT [14015010] |
| Latitude, ° | 10.79416667 |
| Longitude, ° | -75.26055556 |
| Elevation, m | 20 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1945-12-14 19:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | Santa Catalina |
| Stream | 0 |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Litoral |
| SZH - Hydrographic subzone | Arroyos Directos al Caribe |

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

### (CNE index 453) Open Weather values for station 14015010 - GALERAZAMBA  - AUT [14015010]

JSON data from API OWM:

```
{'lat': 10.7942, 'lon': -75.2606, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813740, 'sunset': 1641855265, 'temp': 30.01, 'feels_like': 36.07, 'pressure': 1009, 'humidity': 74, 'dew_point': 24.87, 'uvi': 3.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.24, 'wind_deg': 31, 'wind_gust': 7.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1010, 'humidity': 79, 'dew_point': 22.08, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 10.67, 'wind_deg': 46, 'wind_gust': 14.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.08, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 9.68, 'wind_deg': 49, 'wind_gust': 13.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.08, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 9.25, 'wind_deg': 54, 'wind_gust': 12.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.01, 'feels_like': 25.6, 'pressure': 1012, 'humidity': 78, 'dew_point': 20.91, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 8.27, 'wind_deg': 55, 'wind_gust': 11.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.01, 'feels_like': 25.58, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.7, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 8.46, 'wind_deg': 53, 'wind_gust': 11.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.01, 'feels_like': 25.58, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.7, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 9.06, 'wind_deg': 54, 'wind_gust': 11.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.01, 'feels_like': 24.48, 'pressure': 1010, 'humidity': 77, 'dew_point': 19.73, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.93, 'wind_deg': 60, 'wind_gust': 11.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.01, 'feels_like': 24.5, 'pressure': 1010, 'humidity': 78, 'dew_point': 19.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.03, 'wind_deg': 66, 'wind_gust': 9.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.01, 'feels_like': 24.53, 'pressure': 1010, 'humidity': 79, 'dew_point': 20.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.3, 'wind_deg': 67, 'wind_gust': 8.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.01, 'feels_like': 24.56, 'pressure': 1010, 'humidity': 80, 'dew_point': 20.35, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 6.71, 'wind_deg': 68, 'wind_gust': 7.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.01, 'feels_like': 24.58, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.55, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 6.08, 'wind_deg': 71, 'wind_gust': 6.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.01, 'feels_like': 23.48, 'pressure': 1011, 'humidity': 81, 'dew_point': 19.57, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 5.41, 'wind_deg': 78, 'wind_gust': 5.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.01, 'feels_like': 23.46, 'pressure': 1012, 'humidity': 80, 'dew_point': 19.37, 'uvi': 0.26, 'clouds': 12, 'visibility': 10000, 'wind_speed': 5.13, 'wind_deg': 75, 'wind_gust': 5.37, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 25.01, 'feels_like': 25.6, 'pressure': 1014, 'humidity': 78, 'dew_point': 20.91, 'uvi': 1.4, 'clouds': 11, 'visibility': 10000, 'wind_speed': 5.49, 'wind_deg': 65, 'wind_gust': 5.51, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.01, 'feels_like': 31.24, 'pressure': 1014, 'humidity': 74, 'dew_point': 22.94, 'uvi': 3.62, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.86, 'wind_deg': 60, 'wind_gust': 5.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 29.01, 'feels_like': 32.94, 'pressure': 1014, 'humidity': 71, 'dew_point': 23.22, 'uvi': 6.42, 'clouds': 60, 'visibility': 10000, 'wind_speed': 5.65, 'wind_deg': 49, 'wind_gust': 4.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.01, 'feels_like': 32.94, 'pressure': 1014, 'humidity': 71, 'dew_point': 23.22, 'uvi': 8.29, 'clouds': 70, 'visibility': 10000, 'wind_speed': 5.87, 'wind_deg': 40, 'wind_gust': 4.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.01, 'feels_like': 33.13, 'pressure': 1013, 'humidity': 72, 'dew_point': 23.45, 'uvi': 9.18, 'clouds': 76, 'visibility': 10000, 'wind_speed': 7.14, 'wind_deg': 32, 'wind_gust': 5.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.01, 'feels_like': 36.33, 'pressure': 1012, 'humidity': 75, 'dew_point': 25.09, 'uvi': 8.4, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.77, 'wind_deg': 30, 'wind_gust': 5.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.01, 'feels_like': 38.01, 'pressure': 1010, 'humidity': 75, 'dew_point': 26.05, 'uvi': 5.9, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.64, 'wind_deg': 29, 'wind_gust': 6.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.01, 'feels_like': 36.07, 'pressure': 1009, 'humidity': 74, 'dew_point': 24.87, 'uvi': 3.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.24, 'wind_deg': 31, 'wind_gust': 7.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.01, 'feels_like': 33.72, 'pressure': 1009, 'humidity': 75, 'dew_point': 24.13, 'uvi': 1.35, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.99, 'wind_deg': 33, 'wind_gust': 8.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.01, 'feels_like': 31.82, 'pressure': 1010, 'humidity': 78, 'dew_point': 23.81, 'uvi': 0.28, 'clouds': 100, 'visibility': 10000, 'wind_speed': 9.52, 'wind_deg': 35, 'wind_gust': 9.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.01, 'feels_like': 29.76, 'pressure': 1010, 'humidity': 80, 'dew_point': 23.26, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 9.16, 'wind_deg': 39, 'wind_gust': 9.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 22.080000 | 26.010000 | 79.000000 | 1010.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 46.000000 | 14.21 | 10.670000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 01:00:00 | 45.000000 | 22.080000 | 26.010000 | 79.000000 | 1011.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 49.000000 | 13.3 | 9.680000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 02:00:00 | 71.000000 | 22.080000 | 26.010000 | 79.000000 | 1011.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 54.000000 | 12.27 | 9.250000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 03:00:00 | 81.000000 | 20.910000 | 25.600000 | 78.000000 | 1012.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 55.000000 | 11.31 | 8.270000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 04:00:00 | 86.000000 | 20.700000 | 25.580000 | 77.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 53.000000 | 11.61 | 8.460000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 05:00:00 | 89.000000 | 20.700000 | 25.580000 | 77.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 54.000000 | 11.73 | 9.060000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 19.730000 | 24.480000 | 77.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 60.000000 | 11.28 | 8.930000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.940000 | 24.500000 | 78.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 66.000000 | 9.75 | 8.030000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 20.140000 | 24.530000 | 79.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 67.000000 | 8.41 | 7.300000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 09:00:00 | 72.000000 | 20.350000 | 24.560000 | 80.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 68.000000 | 7.34 | 6.710000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 10:00:00 | 65.000000 | 20.550000 | 24.580000 | 81.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 71.000000 | 6.6 | 6.080000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 11:00:00 | 54.000000 | 19.570000 | 23.480000 | 81.000000 | 1011.000000 |  | 23.010000 | 0.000000 | 10000.000000 | 78.000000 | 5.94 | 5.410000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 12:00:00 | 12.000000 | 19.370000 | 23.460000 | 80.000000 | 1012.000000 |  | 23.010000 | 0.260000 | 10000.000000 | 75.000000 | 5.37 | 5.130000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 13:00:00 | 11.000000 | 20.910000 | 25.600000 | 78.000000 | 1014.000000 |  | 25.010000 | 1.400000 | 10000.000000 | 65.000000 | 5.51 | 5.490000 | 801 | Clouds | few clouds | 02d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 14:00:00 | 40.000000 | 22.940000 | 31.240000 | 74.000000 | 1014.000000 |  | 28.010000 | 3.620000 | 10000.000000 | 60.000000 | 5.37 | 5.860000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 15:00:00 | 60.000000 | 23.220000 | 32.940000 | 71.000000 | 1014.000000 |  | 29.010000 | 6.420000 | 10000.000000 | 49.000000 | 4.98 | 5.650000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 16:00:00 | 70.000000 | 23.220000 | 32.940000 | 71.000000 | 1014.000000 |  | 29.010000 | 8.290000 | 10000.000000 | 40.000000 | 4.78 | 5.870000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 17:00:00 | 76.000000 | 23.450000 | 33.130000 | 72.000000 | 1013.000000 |  | 29.010000 | 9.180000 | 10000.000000 | 32.000000 | 5.12 | 7.140000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 25.090000 | 36.330000 | 75.000000 | 1012.000000 |  | 30.010000 | 8.400000 | 10000.000000 | 30.000000 | 5.21 | 7.770000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 26.050000 | 38.010000 | 75.000000 | 1010.000000 |  | 31.010000 | 5.900000 | 10000.000000 | 29.000000 | 6.11 | 7.640000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 24.870000 | 36.070000 | 74.000000 | 1009.000000 |  | 30.010000 | 3.390000 | 10000.000000 | 31.000000 | 7.48 | 8.240000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 24.130000 | 33.720000 | 75.000000 | 1009.000000 |  | 29.010000 | 1.350000 | 10000.000000 | 33.000000 | 8.79 | 8.990000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 23.810000 | 31.820000 | 78.000000 | 1010.000000 |  | 28.010000 | 0.280000 | 10000.000000 | 35.000000 | 9.89 | 9.520000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 14015010 | "GALERAZAMBA  - AUT [14015010]" | 10.794167 | -75.260556 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 1945-12-14 19:00:00 | NaT | Bolívar | Santa Catalina | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Arroyos Directos al Caribe | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 23.260000 | 29.760000 | 80.000000 | 1010.000000 |  | 27.010000 | 0.000000 | 10000.000000 | 39.000000 | 9.89 | 9.160000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station14015010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station14015010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station14015010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station14015010_OWM_Windspeed_20220111.png)
