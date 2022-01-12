
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TERMOZIPA [21206450] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206450_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.98333333,-73.93333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.98333333&lon=-73.93333333)


| Parameter | Value |
|---|---|
| Code | 21206450 |
| Name | TERMOZIPA [21206450] |
| Latitude, ° | 4.98333333 |
| Longitude, ° | -73.93333333 |
| Elevation, m | 2497 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1992-05-15 00:00:00 |
| Suspension date | 1996-01-15 00:00:00 |
| State | Cundinamarca |
| County | Tocancipá |
| Stream | Lagunilla |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 365) Open Weather values for station 21206450 - TERMOZIPA [21206450]

JSON data from API OWM:

```
{'lat': 4.9833, 'lon': -73.9333, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812851, 'sunset': 1641855516, 'temp': 17.91, 'feels_like': 17.53, 'pressure': 1012, 'humidity': 68, 'dew_point': 11.93, 'uvi': 4.16, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 291, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, 'hourly': [{'dt': 1641772800, 'temp': 12.91, 'feels_like': 12.71, 'pressure': 1016, 'humidity': 94, 'dew_point': 11.97, 'uvi': 0, 'clouds': 96, 'visibility': 9867, 'wind_speed': 0.6, 'wind_deg': 321, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 13.91, 'feels_like': 13.84, 'pressure': 1017, 'humidity': 95, 'dew_point': 13.12, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 323, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.91, 'feels_like': 12.71, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.97, 'uvi': 0, 'clouds': 100, 'visibility': 9076, 'wind_speed': 0.7, 'wind_deg': 337, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.91, 'feels_like': 12.74, 'pressure': 1018, 'humidity': 95, 'dew_point': 12.13, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 350, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 12.91, 'feels_like': 12.71, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.97, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 336, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.91, 'feels_like': 10.51, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.98, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 340, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 8.91, 'feels_like': 8.91, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.84, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 357, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 7.91, 'feels_like': 7.91, 'pressure': 1016, 'humidity': 93, 'dew_point': 6.85, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 329, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 7.91, 'feels_like': 7.91, 'pressure': 1016, 'humidity': 93, 'dew_point': 6.85, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 314, 'wind_gust': 1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.91, 'feels_like': 7.91, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.85, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 316, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.91, 'feels_like': 8.91, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.84, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 311, 'wind_gust': 0.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 9.91, 'feels_like': 9.91, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.83, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 316, 'wind_gust': 0.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 9.91, 'feels_like': 9.91, 'pressure': 1019, 'humidity': 89, 'dew_point': 8.18, 'uvi': 0.42, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 7, 'wind_gust': 0.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 10.91, 'feels_like': 10.15, 'pressure': 1019, 'humidity': 80, 'dew_point': 7.6, 'uvi': 2.46, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 214, 'wind_gust': 0.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 13.91, 'feels_like': 13.16, 'pressure': 1019, 'humidity': 69, 'dew_point': 8.32, 'uvi': 5.81, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 237, 'wind_gust': 1.01, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 15.91, 'feels_like': 15.15, 'pressure': 1017, 'humidity': 61, 'dew_point': 8.41, 'uvi': 9.73, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 257, 'wind_gust': 1.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 16.91, 'feels_like': 16.09, 'pressure': 1016, 'humidity': 55, 'dew_point': 7.82, 'uvi': 9.4, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 268, 'wind_gust': 2.18, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 16.91, 'feels_like': 16.07, 'pressure': 1014, 'humidity': 54, 'dew_point': 7.55, 'uvi': 10.18, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 285, 'wind_gust': 2.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 17.91, 'feels_like': 17.35, 'pressure': 1014, 'humidity': 61, 'dew_point': 10.29, 'uvi': 9.17, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 302, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 17.91, 'feels_like': 17.48, 'pressure': 1013, 'humidity': 66, 'dew_point': 11.47, 'uvi': 7.23, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 299, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641844800, 'temp': 17.91, 'feels_like': 17.53, 'pressure': 1012, 'humidity': 68, 'dew_point': 11.93, 'uvi': 4.16, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 291, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641848400, 'temp': 17.91, 'feels_like': 17.71, 'pressure': 1012, 'humidity': 75, 'dew_point': 13.42, 'uvi': 1.65, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 298, 'wind_gust': 1.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641852000, 'temp': 16.91, 'feels_like': 16.75, 'pressure': 1013, 'humidity': 80, 'dew_point': 13.44, 'uvi': 0.41, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 298, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641855600, 'temp': 14.91, 'feels_like': 14.83, 'pressure': 1015, 'humidity': 91, 'dew_point': 13.46, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 314, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 00:00:00 | 96.000000 | 11.970000 | 12.710000 | 94.000000 | 1016.000000 |  | 12.910000 | 0.000000 | 9867.000000 | 321.000000 | 1.24 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 13.120000 | 13.840000 | 95.000000 | 1017.000000 |  | 13.910000 | 0.000000 | 10000.000000 | 323.000000 | 1.28 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 11.970000 | 12.710000 | 94.000000 | 1018.000000 |  | 12.910000 | 0.000000 | 9076.000000 | 337.000000 | 1.15 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 12.130000 | 12.740000 | 95.000000 | 1018.000000 |  | 12.910000 | 0.000000 | 10000.000000 | 350.000000 | 1.14 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 11.970000 | 12.710000 | 94.000000 | 1018.000000 |  | 12.910000 | 0.000000 | 10000.000000 | 336.000000 | 1.07 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 9.980000 | 10.510000 | 94.000000 | 1018.000000 |  | 10.910000 | 0.000000 | 10000.000000 | 340.000000 | 0.84 | 0.560000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 06:00:00 | 51.000000 | 7.840000 | 8.910000 | 93.000000 | 1017.000000 |  | 8.910000 | 0.000000 | 10000.000000 | 357.000000 | 1.05 | 0.840000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 07:00:00 | 73.000000 | 6.850000 | 7.910000 | 93.000000 | 1016.000000 |  | 7.910000 | 0.000000 | 10000.000000 | 329.000000 | 0.85 | 0.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 08:00:00 | 67.000000 | 6.850000 | 7.910000 | 93.000000 | 1016.000000 |  | 7.910000 | 0.000000 | 10000.000000 | 314.000000 | 1 | 0.750000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 09:00:00 | 65.000000 | 6.850000 | 7.910000 | 93.000000 | 1017.000000 |  | 7.910000 | 0.000000 | 10000.000000 | 316.000000 | 1.03 | 0.910000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 10:00:00 | 58.000000 | 7.840000 | 8.910000 | 93.000000 | 1017.000000 |  | 8.910000 | 0.000000 | 10000.000000 | 311.000000 | 0.71 | 0.660000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 11:00:00 | 56.000000 | 8.830000 | 9.910000 | 93.000000 | 1018.000000 |  | 9.910000 | 0.000000 | 10000.000000 | 316.000000 | 0.72 | 0.500000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 12:00:00 | 31.000000 | 8.180000 | 9.910000 | 89.000000 | 1019.000000 |  | 9.910000 | 0.420000 | 10000.000000 | 7.000000 | 0.63 | 0.260000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 13:00:00 | 41.000000 | 7.600000 | 10.150000 | 80.000000 | 1019.000000 |  | 10.910000 | 2.460000 | 10000.000000 | 214.000000 | 0.71 | 0.490000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 14:00:00 | 34.000000 | 8.320000 | 13.160000 | 69.000000 | 1019.000000 |  | 13.910000 | 5.810000 | 10000.000000 | 237.000000 | 1.01 | 0.880000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 15:00:00 | 32.000000 | 8.410000 | 15.150000 | 61.000000 | 1017.000000 |  | 15.910000 | 9.730000 | 10000.000000 | 257.000000 | 1.77 | 1.450000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 16:00:00 | 39.000000 | 7.820000 | 16.090000 | 55.000000 | 1016.000000 |  | 16.910000 | 9.400000 | 10000.000000 | 268.000000 | 2.18 | 1.730000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 17:00:00 | 48.000000 | 7.550000 | 16.070000 | 54.000000 | 1014.000000 |  | 16.910000 | 10.180000 | 10000.000000 | 285.000000 | 2.12 | 1.920000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 18:00:00 | 79.000000 | 10.290000 | 17.350000 | 61.000000 | 1014.000000 |  | 17.910000 | 9.170000 | 10000.000000 | 302.000000 | 1.72 | 1.610000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 11.470000 | 17.480000 | 66.000000 | 1013.000000 | 0.17 | 17.910000 | 7.230000 | 10000.000000 | 299.000000 | 1.85 | 1.180000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 20:00:00 | 83.000000 | 11.930000 | 17.530000 | 68.000000 | 1012.000000 | 0.32 | 17.910000 | 4.160000 | 10000.000000 | 291.000000 | 1.65 | 1.290000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 21:00:00 | 79.000000 | 13.420000 | 17.710000 | 75.000000 | 1012.000000 | 0.44 | 17.910000 | 1.650000 | 10000.000000 | 298.000000 | 1.64 | 1.130000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 13.440000 | 16.750000 | 80.000000 | 1013.000000 | 0.18 | 16.910000 | 0.410000 | 10000.000000 | 298.000000 | 1.69 | 0.810000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206450 | "TERMOZIPA [21206450]" | 4.983333 | -73.933333 | 2497.000000 | Climática Principal | Convencional | Suspendida | 1992-05-15 00:00:00 | 1996-01-15 00:00:00 | Cundinamarca | Tocancipá | Lagunilla | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 23:00:00 | 77.000000 | 13.460000 | 14.830000 | 91.000000 | 1015.000000 | 0.29 | 14.910000 | 0.000000 | 10000.000000 | 314.000000 | 1.46 | 0.650000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station21206450_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206450_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206450_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206450_OWM_Windspeed_20220111.png)
