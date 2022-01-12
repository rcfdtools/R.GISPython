
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNIVERSIDAD TECNOLOGICA  - AUT [15015120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15015120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.22305556,-74.18591667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.22305556&lon=-74.18591667)


| Parameter | Value |
|---|---|
| Code | 15015120 |
| Name | UNIVERSIDAD TECNOLOGICA  - AUT [15015120] |
| Latitude, ° | 11.22305556 |
| Longitude, ° | -74.18591667 |
| Elevation, m | 7 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-09-12 19:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | Santa Marta |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río  Piedras - Río Manzanares |

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

### (CNE index 212) Open Weather values for station 15015120 - UNIVERSIDAD TECNOLOGICA  - AUT [15015120]

JSON data from API OWM:

```
{'lat': 11.2231, 'lon': -74.1859, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813524, 'sunset': 1641854964, 'temp': 30.99, 'feels_like': 33.65, 'pressure': 1008, 'humidity': 55, 'dew_point': 20.89, 'uvi': 3.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.02, 'wind_deg': 259, 'wind_gust': 7.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.97, 'feels_like': 30.13, 'pressure': 1010, 'humidity': 54, 'dew_point': 18.73, 'uvi': 0, 'clouds': 10, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 28.21, 'feels_like': 29.76, 'pressure': 1011, 'humidity': 60, 'dew_point': 19.71, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 7.6, 'wind_deg': 274, 'wind_gust': 12.07, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 27.97, 'feels_like': 28.79, 'pressure': 1011, 'humidity': 54, 'dew_point': 17.8, 'uvi': 0, 'clouds': 17, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 30, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 27.97, 'feels_like': 28.5, 'pressure': 1012, 'humidity': 51, 'dew_point': 16.9, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 30, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 28.21, 'feels_like': 28.99, 'pressure': 1008, 'humidity': 53, 'dew_point': 17.73, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 10.28, 'wind_deg': 271, 'wind_gust': 16.09, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 27.1, 'feels_like': 28.21, 'pressure': 1009, 'humidity': 60, 'dew_point': 18.67, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 9.39, 'wind_deg': 272, 'wind_gust': 15.65, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 27.1, 'feels_like': 28.13, 'pressure': 1009, 'humidity': 59, 'dew_point': 18.4, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 7.15, 'wind_deg': 279, 'wind_gust': 12.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 26.55, 'feels_like': 26.55, 'pressure': 1009, 'humidity': 61, 'dew_point': 18.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.6, 'wind_deg': 274, 'wind_gust': 12.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 26.55, 'feels_like': 26.55, 'pressure': 1008, 'humidity': 61, 'dew_point': 18.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 8.94, 'wind_deg': 281, 'wind_gust': 13.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 26.55, 'feels_like': 26.55, 'pressure': 1008, 'humidity': 61, 'dew_point': 18.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 7.6, 'wind_deg': 279, 'wind_gust': 12.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.62, 'feels_like': 24.05, 'pressure': 1012, 'humidity': 77, 'dew_point': 19.35, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.72, 'wind_deg': 76, 'wind_gust': 7.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.97, 'feels_like': 23.23, 'pressure': 1012, 'humidity': 73, 'dew_point': 17.87, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 90, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 25.44, 'feels_like': 25.74, 'pressure': 1008, 'humidity': 65, 'dew_point': 18.38, 'uvi': 0.28, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.02, 'wind_deg': 243, 'wind_gust': 7.6, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 27.1, 'feels_like': 28.28, 'pressure': 1008, 'humidity': 61, 'dew_point': 18.93, 'uvi': 1.51, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.47, 'wind_deg': 275, 'wind_gust': 9.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.77, 'feels_like': 29.97, 'pressure': 1008, 'humidity': 55, 'dew_point': 18.84, 'uvi': 3.79, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.81, 'wind_deg': 276, 'wind_gust': 9.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 30.44, 'feels_like': 31.55, 'pressure': 1008, 'humidity': 49, 'dew_point': 18.53, 'uvi': 6.62, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.02, 'wind_deg': 273, 'wind_gust': 7.15, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 30.97, 'feels_like': 36.36, 'pressure': 1014, 'humidity': 66, 'dew_point': 23.87, 'uvi': 8.69, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 240, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 29.32, 'feels_like': 31.93, 'pressure': 1008, 'humidity': 62, 'dew_point': 21.28, 'uvi': 9.5, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 250, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 30.44, 'feels_like': 32.07, 'pressure': 1008, 'humidity': 52, 'dew_point': 19.48, 'uvi': 8.58, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.58, 'wind_deg': 260, 'wind_gust': 8.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 30.97, 'feels_like': 34.3, 'pressure': 1011, 'humidity': 58, 'dew_point': 21.74, 'uvi': 5.91, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 230, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 30.99, 'feels_like': 33.87, 'pressure': 1008, 'humidity': 56, 'dew_point': 21.19, 'uvi': 3.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.68, 'wind_deg': 240, 'wind_gust': 8.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.88, 'feels_like': 32.23, 'pressure': 1007, 'humidity': 58, 'dew_point': 20.72, 'uvi': 1.28, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.81, 'wind_deg': 275, 'wind_gust': 9.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.77, 'feels_like': 30.79, 'pressure': 1008, 'humidity': 61, 'dew_point': 20.5, 'uvi': 0.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 7.6, 'wind_deg': 276, 'wind_gust': 13.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.21, 'feels_like': 30.01, 'pressure': 1008, 'humidity': 62, 'dew_point': 20.24, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 9.39, 'wind_deg': 280, 'wind_gust': 13.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 00:00:00 | 10.000000 | 18.730000 | 30.130000 | 54.000000 | 1010.000000 |  | 28.970000 | 0.000000 | 10000.000000 | 30.000000 |  | 5.660000 | 800 | Clear | clear sky | 01n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 01:00:00 | 14.000000 | 19.710000 | 29.760000 | 60.000000 | 1011.000000 |  | 28.210000 | 0.000000 | 10000.000000 | 274.000000 | 12.07 | 7.600000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 02:00:00 | 17.000000 | 17.800000 | 28.790000 | 54.000000 | 1011.000000 |  | 27.970000 | 0.000000 | 10000.000000 | 30.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 16.900000 | 28.500000 | 51.000000 | 1012.000000 |  | 27.970000 | 0.000000 | 10000.000000 | 30.000000 |  | 5.660000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 04:00:00 | 23.000000 | 17.730000 | 28.990000 | 53.000000 | 1008.000000 |  | 28.210000 | 0.000000 | 10000.000000 | 271.000000 | 16.09 | 10.280000 | 801 | Clouds | few clouds | 02n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 05:00:00 | 38.000000 | 18.670000 | 28.210000 | 60.000000 | 1009.000000 |  | 27.100000 | 0.000000 | 10000.000000 | 272.000000 | 15.65 | 9.390000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 18.400000 | 28.130000 | 59.000000 | 1009.000000 |  | 27.100000 | 0.000000 | 10000.000000 | 279.000000 | 12.52 | 7.150000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 18.420000 | 26.550000 | 61.000000 | 1009.000000 |  | 26.550000 | 0.000000 | 10000.000000 | 274.000000 | 12.52 | 7.600000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 18.420000 | 26.550000 | 61.000000 | 1008.000000 |  | 26.550000 | 0.000000 | 10000.000000 | 281.000000 | 13.41 | 8.940000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 18.420000 | 26.550000 | 61.000000 | 1008.000000 |  | 26.550000 | 0.000000 | 10000.000000 | 279.000000 | 12.52 | 7.600000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 19.350000 | 24.050000 | 77.000000 | 1012.000000 |  | 23.620000 | 0.000000 | 10000.000000 | 76.000000 | 7.54 | 5.720000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 17.870000 | 23.230000 | 73.000000 | 1012.000000 |  | 22.970000 | 0.000000 | 10000.000000 | 90.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 18.380000 | 25.740000 | 65.000000 | 1008.000000 |  | 25.440000 | 0.280000 | 10000.000000 | 243.000000 | 7.6 | 4.020000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 18.930000 | 28.280000 | 61.000000 | 1008.000000 |  | 27.100000 | 1.510000 | 10000.000000 | 275.000000 | 9.83 | 4.470000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 18.840000 | 29.970000 | 55.000000 | 1008.000000 |  | 28.770000 | 3.790000 | 10000.000000 | 276.000000 | 9.83 | 5.810000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 15:00:00 | 20.000000 | 18.530000 | 31.550000 | 49.000000 | 1008.000000 |  | 30.440000 | 6.620000 | 10000.000000 | 273.000000 | 7.15 | 4.020000 | 801 | Clouds | few clouds | 02d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 23.870000 | 36.360000 | 66.000000 | 1014.000000 |  | 30.970000 | 8.690000 | 10000.000000 | 240.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 21.280000 | 31.930000 | 62.000000 | 1008.000000 |  | 29.320000 | 9.500000 | 10000.000000 | 250.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 19.480000 | 32.070000 | 52.000000 | 1008.000000 |  | 30.440000 | 8.580000 | 10000.000000 | 260.000000 | 8.05 | 3.580000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 21.740000 | 34.300000 | 58.000000 | 1011.000000 |  | 30.970000 | 5.910000 | 10000.000000 | 230.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 21.190000 | 33.870000 | 56.000000 | 1008.000000 |  | 30.990000 | 3.330000 | 10000.000000 | 240.000000 | 8.05 | 2.680000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 20.720000 | 32.230000 | 58.000000 | 1007.000000 |  | 29.880000 | 1.280000 | 10000.000000 | 275.000000 | 9.83 | 5.810000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 20.500000 | 30.790000 | 61.000000 | 1008.000000 |  | 28.770000 | 0.240000 | 10000.000000 | 276.000000 | 13.41 | 7.600000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015120 | "UNIVERSIDAD TECNOLOGICA  - AUT [15015120]" | 11.223056 | -74.185917 | 7.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-12 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 20.240000 | 30.010000 | 62.000000 | 1008.000000 |  | 28.210000 | 0.000000 | 10000.000000 | 280.000000 | 13.41 | 9.390000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15015120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15015120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15015120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015120_OWM_Windspeed_20220111.png)
