
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TAJO SUR [15065140] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15065140_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.07688889,-72.675) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.07688889&lon=-72.675)


| Parameter | Value |
|---|---|
| Code | 15065140 |
| Name | TAJO SUR [15065140] |
| Latitude, ° | 11.07688889 |
| Longitude, ° | -72.675 |
| Elevation, m | 95 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1988-07-15 00:00:00 |
| Suspension date | 1989-04-15 00:00:00 |
| State | La Guajira |
| County | Barrancas |
| Stream | Rancheria |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río Ranchería |

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

### (CNE index 3886) Open Weather values for station 15065140 - TAJO SUR [15065140]

JSON data from API OWM:

```
{'lat': 11.0769, 'lon': -72.675, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813147, 'sunset': 1641854616, 'temp': 27.36, 'feels_like': 26.97, 'pressure': 1010, 'humidity': 37, 'dew_point': 11.4, 'uvi': 3.4, 'clouds': 47, 'visibility': 10000, 'wind_speed': 5.27, 'wind_deg': 67, 'wind_gust': 5.32, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.36, 'feels_like': 32.67, 'pressure': 1014, 'humidity': 78, 'dew_point': 24.15, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 2.4, 'wind_deg': 87, 'wind_gust': 5.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 28.36, 'feels_like': 33.56, 'pressure': 1015, 'humidity': 83, 'dew_point': 25.19, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.09, 'wind_deg': 94, 'wind_gust': 4.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 21.05, 'feels_like': 21.51, 'pressure': 1016, 'humidity': 88, 'dew_point': 18.99, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 101, 'wind_gust': 3.08, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 20.78, 'feels_like': 21.29, 'pressure': 1016, 'humidity': 91, 'dew_point': 19.26, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 106, 'wind_gust': 2.8, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 20.58, 'feels_like': 21.15, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.58, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 108, 'wind_gust': 2.57, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 20.48, 'feels_like': 21.06, 'pressure': 1015, 'humidity': 95, 'dew_point': 19.65, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 104, 'wind_gust': 2.46, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 20.43, 'feels_like': 21.04, 'pressure': 1014, 'humidity': 96, 'dew_point': 19.77, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 93, 'wind_gust': 2.61, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 20.32, 'feels_like': 20.91, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.66, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 95, 'wind_gust': 2.67, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 20.18, 'feels_like': 20.76, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.52, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 99, 'wind_gust': 2.03, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 20.14, 'feels_like': 20.72, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.48, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 100, 'wind_gust': 1.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 20.28, 'feels_like': 20.84, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.45, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 105, 'wind_gust': 2.04, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 22.36, 'feels_like': 23.11, 'pressure': 1014, 'humidity': 94, 'dew_point': 21.35, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 105, 'wind_gust': 2.22, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.36, 'feels_like': 22.95, 'pressure': 1015, 'humidity': 88, 'dew_point': 20.28, 'uvi': 0.36, 'clouds': 14, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 98, 'wind_gust': 2.93, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 24.36, 'feels_like': 24.71, 'pressure': 1016, 'humidity': 71, 'dew_point': 18.76, 'uvi': 1.7, 'clouds': 13, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 79, 'wind_gust': 4.63, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 26.36, 'feels_like': 26.36, 'pressure': 1016, 'humidity': 59, 'dew_point': 17.71, 'uvi': 4.11, 'clouds': 12, 'visibility': 10000, 'wind_speed': 3.02, 'wind_deg': 80, 'wind_gust': 4.67, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 28.36, 'feels_like': 28.86, 'pressure': 1016, 'humidity': 50, 'dew_point': 16.94, 'uvi': 6.93, 'clouds': 11, 'visibility': 10000, 'wind_speed': 3.46, 'wind_deg': 77, 'wind_gust': 5.27, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 31.36, 'feels_like': 31.88, 'pressure': 1015, 'humidity': 43, 'dew_point': 17.28, 'uvi': 9.27, 'clouds': 12, 'visibility': 10000, 'wind_speed': 4.06, 'wind_deg': 75, 'wind_gust': 5.64, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 30.36, 'feels_like': 29.99, 'pressure': 1013, 'humidity': 39, 'dew_point': 14.86, 'uvi': 9.94, 'clouds': 12, 'visibility': 10000, 'wind_speed': 4.44, 'wind_deg': 73, 'wind_gust': 5.6, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 31.36, 'feels_like': 30.95, 'pressure': 1012, 'humidity': 37, 'dew_point': 14.93, 'uvi': 8.8, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.78, 'wind_deg': 70, 'wind_gust': 5.4, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 32.36, 'feels_like': 32.09, 'pressure': 1010, 'humidity': 36, 'dew_point': 15.39, 'uvi': 6.22, 'clouds': 27, 'visibility': 10000, 'wind_speed': 5.21, 'wind_deg': 69, 'wind_gust': 5.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 27.36, 'feels_like': 26.97, 'pressure': 1010, 'humidity': 37, 'dew_point': 11.4, 'uvi': 3.4, 'clouds': 47, 'visibility': 10000, 'wind_speed': 5.27, 'wind_deg': 67, 'wind_gust': 5.32, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 27.36, 'feels_like': 27.19, 'pressure': 1010, 'humidity': 41, 'dew_point': 12.96, 'uvi': 1.23, 'clouds': 51, 'visibility': 10000, 'wind_speed': 4.95, 'wind_deg': 63, 'wind_gust': 5.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 26.36, 'feels_like': 26.36, 'pressure': 1011, 'humidity': 49, 'dew_point': 14.8, 'uvi': 0.2, 'clouds': 47, 'visibility': 10000, 'wind_speed': 4.38, 'wind_deg': 54, 'wind_gust': 5.95, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 28.36, 'feels_like': 30.38, 'pressure': 1012, 'humidity': 63, 'dew_point': 20.64, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 3.22, 'wind_deg': 55, 'wind_gust': 7.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 00:00:00 | 31.000000 | 24.150000 | 32.670000 | 78.000000 | 1014.000000 |  | 28.360000 | 0.000000 | 10000.000000 | 87.000000 | 5.45 | 2.400000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 01:00:00 | 26.000000 | 25.190000 | 33.560000 | 83.000000 | 1015.000000 |  | 28.360000 | 0.000000 | 10000.000000 | 94.000000 | 4.06 | 2.090000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 18.990000 | 21.510000 | 88.000000 | 1016.000000 |  | 21.050000 | 0.000000 | 10000.000000 | 101.000000 | 3.08 | 1.680000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 03:00:00 | 16.000000 | 19.260000 | 21.290000 | 91.000000 | 1016.000000 |  | 20.780000 | 0.000000 | 10000.000000 | 106.000000 | 2.8 | 1.630000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 04:00:00 | 13.000000 | 19.580000 | 21.150000 | 94.000000 | 1015.000000 |  | 20.580000 | 0.000000 | 10000.000000 | 108.000000 | 2.57 | 1.420000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 05:00:00 | 13.000000 | 19.650000 | 21.060000 | 95.000000 | 1015.000000 |  | 20.480000 | 0.000000 | 10000.000000 | 104.000000 | 2.46 | 1.410000 | 801 | Clouds | few clouds | 02n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 06:00:00 | 8.000000 | 19.770000 | 21.040000 | 96.000000 | 1014.000000 |  | 20.430000 | 0.000000 | 10000.000000 | 93.000000 | 2.61 | 1.340000 | 800 | Clear | clear sky | 01n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 07:00:00 | 13.000000 | 19.660000 | 20.910000 | 96.000000 | 1013.000000 |  | 20.320000 | 0.000000 | 10000.000000 | 95.000000 | 2.67 | 1.300000 | 801 | Clouds | few clouds | 02n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 08:00:00 | 14.000000 | 19.520000 | 20.760000 | 96.000000 | 1013.000000 |  | 20.180000 | 0.000000 | 10000.000000 | 99.000000 | 2.03 | 1.130000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 09:00:00 | 33.000000 | 19.480000 | 20.720000 | 96.000000 | 1013.000000 |  | 20.140000 | 0.000000 | 10000.000000 | 100.000000 | 1.72 | 1.010000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 10:00:00 | 49.000000 | 19.450000 | 20.840000 | 95.000000 | 1014.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 105.000000 | 2.04 | 0.940000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 21.350000 | 23.110000 | 94.000000 | 1014.000000 |  | 22.360000 | 0.000000 | 10000.000000 | 105.000000 | 2.22 | 0.960000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 12:00:00 | 14.000000 | 20.280000 | 22.950000 | 88.000000 | 1015.000000 |  | 22.360000 | 0.360000 | 10000.000000 | 98.000000 | 2.93 | 0.980000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 13:00:00 | 13.000000 | 18.760000 | 24.710000 | 71.000000 | 1016.000000 |  | 24.360000 | 1.700000 | 10000.000000 | 79.000000 | 4.63 | 2.450000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 14:00:00 | 12.000000 | 17.710000 | 26.360000 | 59.000000 | 1016.000000 |  | 26.360000 | 4.110000 | 10000.000000 | 80.000000 | 4.67 | 3.020000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 15:00:00 | 11.000000 | 16.940000 | 28.860000 | 50.000000 | 1016.000000 |  | 28.360000 | 6.930000 | 10000.000000 | 77.000000 | 5.27 | 3.460000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 16:00:00 | 12.000000 | 17.280000 | 31.880000 | 43.000000 | 1015.000000 |  | 31.360000 | 9.270000 | 10000.000000 | 75.000000 | 5.64 | 4.060000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 17:00:00 | 12.000000 | 14.860000 | 29.990000 | 39.000000 | 1013.000000 |  | 30.360000 | 9.940000 | 10000.000000 | 73.000000 | 5.6 | 4.440000 | 801 | Clouds | few clouds | 02d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 18:00:00 | 20.000000 | 14.930000 | 30.950000 | 37.000000 | 1012.000000 |  | 31.360000 | 8.800000 | 10000.000000 | 70.000000 | 5.4 | 4.780000 | 801 | Clouds | few clouds | 02d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 19:00:00 | 27.000000 | 15.390000 | 32.090000 | 36.000000 | 1010.000000 |  | 32.360000 | 6.220000 | 10000.000000 | 69.000000 | 5.47 | 5.210000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 20:00:00 | 47.000000 | 11.400000 | 26.970000 | 37.000000 | 1010.000000 |  | 27.360000 | 3.400000 | 10000.000000 | 67.000000 | 5.32 | 5.270000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 21:00:00 | 51.000000 | 12.960000 | 27.190000 | 41.000000 | 1010.000000 |  | 27.360000 | 1.230000 | 10000.000000 | 63.000000 | 5.29 | 4.950000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 22:00:00 | 47.000000 | 14.800000 | 26.360000 | 49.000000 | 1011.000000 |  | 26.360000 | 0.200000 | 10000.000000 | 54.000000 | 5.95 | 4.380000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065140 | "TAJO SUR [15065140]" | 11.076889 | -72.675000 | 95.000000 | Climática Principal | Convencional | Suspendida | 1988-07-15 00:00:00 | 1989-04-15 00:00:00 | La Guajira | Barrancas | Rancheria | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 23:00:00 | 48.000000 | 20.640000 | 30.380000 | 63.000000 | 1012.000000 |  | 28.360000 | 0.000000 | 10000.000000 | 55.000000 | 7.06 | 3.220000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station15065140_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15065140_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15065140_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065140_OWM_Windspeed_20220111.png)
