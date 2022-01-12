
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CAMP INTERCOR [15065050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15065050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.14286111,-72.51466667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.14286111&lon=-72.51466667)


| Parameter | Value |
|---|---|
| Code | 15065050 |
| Name | CAMP INTERCOR [15065050] |
| Latitude, ° | 11.14286111 |
| Longitude, ° | -72.51466667 |
| Elevation, m | 122 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1978-06-15 00:00:00 |
| Suspension date | 2016-01-06 00:00:00 |
| State | La Guajira |
| County | Albania (La guajira) |
| Stream | Ay Bruno |
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

### (CNE index 3890) Open Weather values for station 15065050 - CAMP INTERCOR [15065050]

JSON data from API OWM:

```
{'lat': 11.1429, 'lon': -72.5147, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813115, 'sunset': 1641854571, 'temp': 27.27, 'feels_like': 27.23, 'pressure': 1010, 'humidity': 43, 'dew_point': 13.61, 'uvi': 3.4, 'clouds': 70, 'visibility': 10000, 'wind_speed': 4.87, 'wind_deg': 78, 'wind_gust': 5.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.27, 'feels_like': 33.31, 'pressure': 1014, 'humidity': 83, 'dew_point': 25.1, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 113, 'wind_gust': 4.73, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 28.27, 'feels_like': 34.04, 'pressure': 1015, 'humidity': 87, 'dew_point': 25.9, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.37, 'wind_deg': 116, 'wind_gust': 4.66, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 21.38, 'feels_like': 21.9, 'pressure': 1016, 'humidity': 89, 'dew_point': 19.49, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 119, 'wind_gust': 4.23, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 21.29, 'feels_like': 21.85, 'pressure': 1016, 'humidity': 91, 'dew_point': 19.76, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.21, 'wind_deg': 123, 'wind_gust': 4.09, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 21.18, 'feels_like': 21.78, 'pressure': 1015, 'humidity': 93, 'dew_point': 20, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 123, 'wind_gust': 4.28, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 20.96, 'feels_like': 21.57, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.96, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 124, 'wind_gust': 3.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 20.76, 'feels_like': 21.37, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.93, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 118, 'wind_gust': 3.86, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 20.6, 'feels_like': 21.22, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.94, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 2, 'wind_deg': 126, 'wind_gust': 3.43, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 20.51, 'feels_like': 21.12, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.85, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 124, 'wind_gust': 2.82, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 20.68, 'feels_like': 21.28, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.85, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 122, 'wind_gust': 2.49, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 21.34, 'feels_like': 21.93, 'pressure': 1013, 'humidity': 92, 'dew_point': 19.99, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 111, 'wind_gust': 3.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.27, 'feels_like': 22.9, 'pressure': 1014, 'humidity': 90, 'dew_point': 20.55, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 106, 'wind_gust': 3.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.27, 'feels_like': 22.8, 'pressure': 1015, 'humidity': 86, 'dew_point': 19.82, 'uvi': 0.36, 'clouds': 28, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 103, 'wind_gust': 4.94, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 24.27, 'feels_like': 24.68, 'pressure': 1016, 'humidity': 74, 'dew_point': 19.34, 'uvi': 1.7, 'clouds': 25, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 95, 'wind_gust': 5.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1016, 'humidity': 64, 'dew_point': 18.92, 'uvi': 4.11, 'clouds': 23, 'visibility': 10000, 'wind_speed': 3.64, 'wind_deg': 94, 'wind_gust': 5.56, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 28.27, 'feels_like': 29.28, 'pressure': 1016, 'humidity': 55, 'dew_point': 18.37, 'uvi': 6.93, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.98, 'wind_deg': 95, 'wind_gust': 5.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 31.27, 'feels_like': 32.87, 'pressure': 1015, 'humidity': 49, 'dew_point': 19.28, 'uvi': 9.27, 'clouds': 19, 'visibility': 10000, 'wind_speed': 4.32, 'wind_deg': 90, 'wind_gust': 6.16, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 30.27, 'feels_like': 30.39, 'pressure': 1014, 'humidity': 43, 'dew_point': 16.31, 'uvi': 9.94, 'clouds': 18, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 85, 'wind_gust': 6.03, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 31.27, 'feels_like': 31.42, 'pressure': 1012, 'humidity': 41, 'dew_point': 16.45, 'uvi': 8.8, 'clouds': 36, 'visibility': 10000, 'wind_speed': 4.95, 'wind_deg': 81, 'wind_gust': 5.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 32.27, 'feels_like': 32.86, 'pressure': 1011, 'humidity': 41, 'dew_point': 17.35, 'uvi': 6.22, 'clouds': 51, 'visibility': 10000, 'wind_speed': 5.2, 'wind_deg': 80, 'wind_gust': 6.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 27.27, 'feels_like': 27.23, 'pressure': 1010, 'humidity': 43, 'dew_point': 13.61, 'uvi': 3.4, 'clouds': 70, 'visibility': 10000, 'wind_speed': 4.87, 'wind_deg': 78, 'wind_gust': 5.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 27.27, 'feels_like': 27.42, 'pressure': 1011, 'humidity': 46, 'dew_point': 14.65, 'uvi': 1.23, 'clouds': 64, 'visibility': 10000, 'wind_speed': 4.41, 'wind_deg': 77, 'wind_gust': 5.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1011, 'humidity': 55, 'dew_point': 16.52, 'uvi': 0.2, 'clouds': 59, 'visibility': 10000, 'wind_speed': 3.85, 'wind_deg': 71, 'wind_gust': 5.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.27, 'feels_like': 31.05, 'pressure': 1012, 'humidity': 69, 'dew_point': 22.04, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 3.05, 'wind_deg': 80, 'wind_gust': 6.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 00:00:00 | 21.000000 | 25.100000 | 33.310000 | 83.000000 | 1014.000000 |  | 28.270000 | 0.000000 | 10000.000000 | 113.000000 | 4.73 | 2.560000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 25.900000 | 34.040000 | 87.000000 | 1015.000000 |  | 28.270000 | 0.000000 | 10000.000000 | 116.000000 | 4.66 | 2.370000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 02:00:00 | 13.000000 | 19.490000 | 21.900000 | 89.000000 | 1016.000000 |  | 21.380000 | 0.000000 | 10000.000000 | 119.000000 | 4.23 | 2.200000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 03:00:00 | 11.000000 | 19.760000 | 21.850000 | 91.000000 | 1016.000000 |  | 21.290000 | 0.000000 | 10000.000000 | 123.000000 | 4.09 | 2.210000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 04:00:00 | 11.000000 | 20.000000 | 21.780000 | 93.000000 | 1015.000000 |  | 21.180000 | 0.000000 | 10000.000000 | 123.000000 | 4.28 | 2.240000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 05:00:00 | 11.000000 | 19.960000 | 21.570000 | 94.000000 | 1015.000000 |  | 20.960000 | 0.000000 | 10000.000000 | 124.000000 | 3.89 | 2.110000 | 801 | Clouds | few clouds | 02n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 06:00:00 | 11.000000 | 19.930000 | 21.370000 | 95.000000 | 1014.000000 |  | 20.760000 | 0.000000 | 10000.000000 | 118.000000 | 3.86 | 2.120000 | 801 | Clouds | few clouds | 02n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 07:00:00 | 16.000000 | 19.940000 | 21.220000 | 96.000000 | 1013.000000 |  | 20.600000 | 0.000000 | 10000.000000 | 126.000000 | 3.43 | 2.000000 | 801 | Clouds | few clouds | 02n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 08:00:00 | 21.000000 | 19.850000 | 21.120000 | 96.000000 | 1013.000000 |  | 20.510000 | 0.000000 | 10000.000000 | 124.000000 | 2.82 | 1.850000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 09:00:00 | 37.000000 | 19.850000 | 21.280000 | 95.000000 | 1013.000000 |  | 20.680000 | 0.000000 | 10000.000000 | 122.000000 | 2.49 | 1.750000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 10:00:00 | 52.000000 | 19.990000 | 21.930000 | 92.000000 | 1013.000000 |  | 21.340000 | 0.000000 | 10000.000000 | 111.000000 | 3.96 | 1.760000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 11:00:00 | 61.000000 | 20.550000 | 22.900000 | 90.000000 | 1014.000000 |  | 22.270000 | 0.000000 | 10000.000000 | 106.000000 | 3.9 | 2.030000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 12:00:00 | 28.000000 | 19.820000 | 22.800000 | 86.000000 | 1015.000000 |  | 22.270000 | 0.360000 | 10000.000000 | 103.000000 | 4.94 | 1.970000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 13:00:00 | 25.000000 | 19.340000 | 24.680000 | 74.000000 | 1016.000000 |  | 24.270000 | 1.700000 | 10000.000000 | 95.000000 | 5.56 | 3.280000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 14:00:00 | 23.000000 | 18.920000 | 26.270000 | 64.000000 | 1016.000000 |  | 26.270000 | 4.110000 | 10000.000000 | 94.000000 | 5.56 | 3.640000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 15:00:00 | 20.000000 | 18.370000 | 29.280000 | 55.000000 | 1016.000000 |  | 28.270000 | 6.930000 | 10000.000000 | 95.000000 | 5.89 | 3.980000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 16:00:00 | 19.000000 | 19.280000 | 32.870000 | 49.000000 | 1015.000000 |  | 31.270000 | 9.270000 | 10000.000000 | 90.000000 | 6.16 | 4.320000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 17:00:00 | 18.000000 | 16.310000 | 30.390000 | 43.000000 | 1014.000000 |  | 30.270000 | 9.940000 | 10000.000000 | 85.000000 | 6.03 | 4.630000 | 801 | Clouds | few clouds | 02d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 18:00:00 | 36.000000 | 16.450000 | 31.420000 | 41.000000 | 1012.000000 |  | 31.270000 | 8.800000 | 10000.000000 | 81.000000 | 5.92 | 4.950000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 19:00:00 | 51.000000 | 17.350000 | 32.860000 | 41.000000 | 1011.000000 |  | 32.270000 | 6.220000 | 10000.000000 | 80.000000 | 6.01 | 5.200000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 20:00:00 | 70.000000 | 13.610000 | 27.230000 | 43.000000 | 1010.000000 |  | 27.270000 | 3.400000 | 10000.000000 | 78.000000 | 5.64 | 4.870000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 21:00:00 | 64.000000 | 14.650000 | 27.420000 | 46.000000 | 1011.000000 |  | 27.270000 | 1.230000 | 10000.000000 | 77.000000 | 5.35 | 4.410000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 22:00:00 | 59.000000 | 16.520000 | 26.270000 | 55.000000 | 1011.000000 |  | 26.270000 | 0.200000 | 10000.000000 | 71.000000 | 5.48 | 3.850000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065050 | "CAMP INTERCOR [15065050]" | 11.142861 | -72.514667 | 122.000000 | Climática Principal | Convencional | Suspendida | 1978-06-15 00:00:00 | 2016-01-06 00:00:00 | La Guajira | Albania (La guajira) | Ay Bruno | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 23:00:00 | 53.000000 | 22.040000 | 31.050000 | 69.000000 | 1012.000000 |  | 28.270000 | 0.000000 | 10000.000000 | 80.000000 | 6.41 | 3.050000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15065050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15065050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15065050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065050_OWM_Windspeed_20220111.png)
