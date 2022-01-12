
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO PLANADAS [22025010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station22025010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.16666667,-75.66666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.16666667&lon=-75.66666667)


| Parameter | Value |
|---|---|
| Code | 22025010 |
| Name | AEROPUERTO PLANADAS [22025010] |
| Latitude, ° | 3.16666667 |
| Longitude, ° | -75.66666667 |
| Elevation, m | 1355 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1964-10-15 00:00:00 |
| Suspension date | 2004-07-15 00:00:00 |
| State | Tolima |
| County | Planadas |
| Stream | Ata |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Saldaña |
| SZH - Hydrographic subzone | Río Atá |

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

### (CNE index 1892) Open Weather values for station 22025010 - AEROPUERTO PLANADAS [22025010]

JSON data from API OWM:

```
{'lat': 3.1667, 'lon': -75.6667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813091, 'sunset': 1641856108, 'temp': 23.51, 'feels_like': 24.14, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.84, 'uvi': 1.61, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 50, 'wind_gust': 1.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, 'hourly': [{'dt': 1641772800, 'temp': 19.51, 'feels_like': 19.97, 'pressure': 1014, 'humidity': 94, 'dew_point': 18.52, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 263, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641776400, 'temp': 19.51, 'feels_like': 19.97, 'pressure': 1016, 'humidity': 94, 'dew_point': 18.52, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 257, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641780000, 'temp': 18.51, 'feels_like': 18.87, 'pressure': 1017, 'humidity': 94, 'dew_point': 17.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 253, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641783600, 'temp': 18.51, 'feels_like': 18.87, 'pressure': 1017, 'humidity': 94, 'dew_point': 17.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 257, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.25, 'feels_like': 15.29, 'pressure': 1017, 'humidity': 94, 'dew_point': 14.29, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 251, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 15.26, 'feels_like': 15.27, 'pressure': 1016, 'humidity': 93, 'dew_point': 14.14, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 256, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.25, 'feels_like': 15.26, 'pressure': 1016, 'humidity': 93, 'dew_point': 14.13, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 258, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 15.07, 'feels_like': 15.06, 'pressure': 1015, 'humidity': 93, 'dew_point': 13.95, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 244, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641801600, 'temp': 15.21, 'feels_like': 15.21, 'pressure': 1014, 'humidity': 93, 'dew_point': 14.09, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 250, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 15.08, 'feels_like': 15.07, 'pressure': 1014, 'humidity': 93, 'dew_point': 13.96, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 244, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 14.75, 'feels_like': 14.71, 'pressure': 1015, 'humidity': 93, 'dew_point': 13.63, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 236, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 15.51, 'feels_like': 15.54, 'pressure': 1016, 'humidity': 93, 'dew_point': 14.38, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 227, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 15.51, 'feels_like': 15.52, 'pressure': 1016, 'humidity': 92, 'dew_point': 14.22, 'uvi': 0.21, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 228, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.51, 'feels_like': 17.59, 'pressure': 1017, 'humidity': 87, 'dew_point': 15.32, 'uvi': 0.65, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 89, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641823200, 'temp': 19.51, 'feels_like': 19.74, 'pressure': 1017, 'humidity': 85, 'dew_point': 16.92, 'uvi': 1.61, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 69, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641826800, 'temp': 19.51, 'feels_like': 19.63, 'pressure': 1017, 'humidity': 81, 'dew_point': 16.16, 'uvi': 2.78, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 70, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641830400, 'temp': 20.51, 'feels_like': 20.78, 'pressure': 1016, 'humidity': 83, 'dew_point': 17.52, 'uvi': 4.93, 'clouds': 97, 'visibility': 8429, 'wind_speed': 2.27, 'wind_deg': 69, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.98}}, {'dt': 1641834000, 'temp': 21.51, 'feels_like': 21.99, 'pressure': 1015, 'humidity': 87, 'dew_point': 19.26, 'uvi': 5.47, 'clouds': 95, 'visibility': 7582, 'wind_speed': 1.94, 'wind_deg': 62, 'wind_gust': 1.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641837600, 'temp': 23.51, 'feels_like': 24.16, 'pressure': 1014, 'humidity': 86, 'dew_point': 21.03, 'uvi': 5.05, 'clouds': 81, 'visibility': 6977, 'wind_speed': 1.59, 'wind_deg': 64, 'wind_gust': 1.46, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641841200, 'temp': 23.51, 'feels_like': 24.14, 'pressure': 1013, 'humidity': 85, 'dew_point': 20.84, 'uvi': 2.69, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 59, 'wind_gust': 1.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.3}}, {'dt': 1641844800, 'temp': 23.51, 'feels_like': 24.14, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.84, 'uvi': 1.61, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 50, 'wind_gust': 1.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641848400, 'temp': 22.51, 'feels_like': 23.06, 'pressure': 1012, 'humidity': 86, 'dew_point': 20.05, 'uvi': 0.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 58, 'wind_gust': 1.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641852000, 'temp': 21.51, 'feels_like': 22.04, 'pressure': 1012, 'humidity': 89, 'dew_point': 19.62, 'uvi': 0.17, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 66, 'wind_gust': 1.42, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641855600, 'temp': 20.51, 'feels_like': 21.07, 'pressure': 1013, 'humidity': 94, 'dew_point': 19.51, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 234, 'wind_gust': 0.71, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.71}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 00:00:00 | 98.000000 | 18.520000 | 19.970000 | 94.000000 | 1014.000000 | 0.1 | 19.510000 | 0.000000 | 10000.000000 | 263.000000 | 0.83 | 0.530000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 18.520000 | 19.970000 | 94.000000 | 1016.000000 | 0.37 | 19.510000 | 0.000000 | 10000.000000 | 257.000000 | 1.05 | 1.100000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 17.530000 | 18.870000 | 94.000000 | 1017.000000 | 0.28 | 18.510000 | 0.000000 | 10000.000000 | 253.000000 | 1.31 | 1.290000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 17.530000 | 18.870000 | 94.000000 | 1017.000000 |  | 18.510000 | 0.000000 | 10000.000000 | 257.000000 | 1.3 | 1.110000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 14.290000 | 15.290000 | 94.000000 | 1017.000000 |  | 15.250000 | 0.000000 | 10000.000000 | 251.000000 | 1.18 | 1.330000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 05:00:00 | 98.000000 | 14.140000 | 15.270000 | 93.000000 | 1016.000000 |  | 15.260000 | 0.000000 | 10000.000000 | 256.000000 | 1.33 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 14.130000 | 15.260000 | 93.000000 | 1016.000000 |  | 15.250000 | 0.000000 | 10000.000000 | 258.000000 | 1.02 | 1.050000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 13.950000 | 15.060000 | 93.000000 | 1015.000000 | 0.1 | 15.070000 | 0.000000 | 10000.000000 | 244.000000 | 0.94 | 0.830000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 14.090000 | 15.210000 | 93.000000 | 1014.000000 |  | 15.210000 | 0.000000 | 10000.000000 | 250.000000 | 0.98 | 0.850000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 13.960000 | 15.070000 | 93.000000 | 1014.000000 |  | 15.080000 | 0.000000 | 10000.000000 | 244.000000 | 0.95 | 0.990000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 13.630000 | 14.710000 | 93.000000 | 1015.000000 |  | 14.750000 | 0.000000 | 10000.000000 | 236.000000 | 1.02 | 1.070000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 11:00:00 | 95.000000 | 14.380000 | 15.540000 | 93.000000 | 1016.000000 |  | 15.510000 | 0.000000 | 10000.000000 | 227.000000 | 0.91 | 0.800000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 12:00:00 | 90.000000 | 14.220000 | 15.520000 | 92.000000 | 1016.000000 |  | 15.510000 | 0.210000 | 10000.000000 | 228.000000 | 0.83 | 0.720000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 13:00:00 | 96.000000 | 15.320000 | 17.590000 | 87.000000 | 1017.000000 | 0.13 | 17.510000 | 0.650000 | 10000.000000 | 89.000000 | 0.58 | 0.450000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 16.920000 | 19.740000 | 85.000000 | 1017.000000 | 0.39 | 19.510000 | 1.610000 | 10000.000000 | 69.000000 | 1.08 | 1.290000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 16.160000 | 19.630000 | 81.000000 | 1017.000000 | 0.56 | 19.510000 | 2.780000 | 10000.000000 | 70.000000 | 1.57 | 2.010000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 16:00:00 | 97.000000 | 17.520000 | 20.780000 | 83.000000 | 1016.000000 | 0.98 | 20.510000 | 4.930000 | 8429.000000 | 69.000000 | 1.94 | 2.270000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 17:00:00 | 95.000000 | 19.260000 | 21.990000 | 87.000000 | 1015.000000 | 1.16 | 21.510000 | 5.470000 | 7582.000000 | 62.000000 | 1.88 | 1.940000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | 21.030000 | 24.160000 | 86.000000 | 1014.000000 | 1.23 | 23.510000 | 5.050000 | 6977.000000 | 64.000000 | 1.46 | 1.590000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 20.840000 | 24.140000 | 85.000000 | 1013.000000 | 1.3 | 23.510000 | 2.690000 | 10000.000000 | 59.000000 | 1.35 | 1.560000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 20:00:00 | 86.000000 | 20.840000 | 24.140000 | 85.000000 | 1012.000000 | 1.15 | 23.510000 | 1.610000 | 10000.000000 | 50.000000 | 1.34 | 1.380000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 20.050000 | 23.060000 | 86.000000 | 1012.000000 | 1.03 | 22.510000 | 0.690000 | 10000.000000 | 58.000000 | 1.25 | 1.170000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 22:00:00 | 90.000000 | 19.620000 | 22.040000 | 89.000000 | 1012.000000 | 1.13 | 21.510000 | 0.170000 | 10000.000000 | 66.000000 | 1.42 | 0.970000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025010 | "AEROPUERTO PLANADAS [22025010]" | 3.166667 | -75.666667 | 1355.000000 | Climática Principal | Convencional | Suspendida | 1964-10-15 00:00:00 | 2004-07-15 00:00:00 | Tolima | Planadas | Ata | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Atá | America/Bogota | 2022-01-10 23:00:00 | 87.000000 | 19.510000 | 21.070000 | 94.000000 | 1013.000000 | 1.71 | 20.510000 | 0.000000 | 10000.000000 | 234.000000 | 0.71 | 0.280000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station22025010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station22025010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station22025010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025010_OWM_Windspeed_20220111.png)
