
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL DIABLO - AUT [22025040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station22025040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.98,-76.06) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.98&lon=-76.06)


| Parameter | Value |
|---|---|
| Code | 22025040 |
| Name | EL DIABLO - AUT [22025040] |
| Latitude, ° | 2.98 |
| Longitude, ° | -76.06 |
| Elevation, m | 4100 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2005-05-31 00:00:00 |
| Suspension date | 2021-11-19 15:39:30 |
| State | Cauca |
| County | Páez (Belalcázar) |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Páez |

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

### (CNE index 4490) Open Weather values for station 22025040 - EL DIABLO - AUT [22025040]

JSON data from API OWM:

```
{'lat': 2.98, 'lon': -76.06, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813167, 'sunset': 1641856221, 'temp': 5.79, 'feels_like': 5.79, 'pressure': 1015, 'humidity': 91, 'dew_point': 4.44, 'uvi': 5.87, 'clouds': 97, 'visibility': 7988, 'wind_speed': 1.17, 'wind_deg': 285, 'wind_gust': 1.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.2}}, 'hourly': [{'dt': 1641772800, 'temp': 4.02, 'feels_like': 4.02, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.99, 'uvi': 0, 'clouds': 94, 'visibility': 9605, 'wind_speed': 0.18, 'wind_deg': 309, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641776400, 'temp': 3.89, 'feels_like': 3.89, 'pressure': 1018, 'humidity': 92, 'dew_point': 2.71, 'uvi': 0, 'clouds': 99, 'visibility': 9120, 'wind_speed': 0.11, 'wind_deg': 314, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641780000, 'temp': 3.74, 'feels_like': 3.74, 'pressure': 1019, 'humidity': 91, 'dew_point': 2.41, 'uvi': 0, 'clouds': 100, 'visibility': 8313, 'wind_speed': 0.17, 'wind_deg': 323, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641783600, 'temp': 3.43, 'feels_like': 3.43, 'pressure': 1019, 'humidity': 95, 'dew_point': 2.71, 'uvi': 0, 'clouds': 100, 'visibility': 8122, 'wind_speed': 0.35, 'wind_deg': 308, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641787200, 'temp': 2.59, 'feels_like': 2.59, 'pressure': 1020, 'humidity': 98, 'dew_point': 2.31, 'uvi': 0, 'clouds': 100, 'visibility': 8123, 'wind_speed': 0.34, 'wind_deg': 278, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641790800, 'temp': 2.43, 'feels_like': 2.43, 'pressure': 1019, 'humidity': 98, 'dew_point': 2.15, 'uvi': 0, 'clouds': 100, 'visibility': 8200, 'wind_speed': 0.22, 'wind_deg': 284, 'wind_gust': 0.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 2.24, 'feels_like': 2.24, 'pressure': 1018, 'humidity': 99, 'dew_point': 2.1, 'uvi': 0, 'clouds': 98, 'visibility': 9010, 'wind_speed': 0.72, 'wind_deg': 277, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641798000, 'temp': 2.15, 'feels_like': 2.15, 'pressure': 1018, 'humidity': 99, 'dew_point': 2.01, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 276, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641801600, 'temp': 1.94, 'feels_like': 1.94, 'pressure': 1017, 'humidity': 99, 'dew_point': 1.8, 'uvi': 0, 'clouds': 100, 'visibility': 8903, 'wind_speed': 0.94, 'wind_deg': 279, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641805200, 'temp': 2.16, 'feels_like': 2.16, 'pressure': 1017, 'humidity': 97, 'dew_point': 1.73, 'uvi': 0, 'clouds': 100, 'visibility': 8693, 'wind_speed': 1.29, 'wind_deg': 279, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 2.54, 'feels_like': 2.54, 'pressure': 1018, 'humidity': 98, 'dew_point': 2.26, 'uvi': 0, 'clouds': 100, 'visibility': 8622, 'wind_speed': 1.09, 'wind_deg': 286, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641812400, 'temp': 2.61, 'feels_like': 2.61, 'pressure': 1018, 'humidity': 97, 'dew_point': 2.18, 'uvi': 0, 'clouds': 100, 'visibility': 9404, 'wind_speed': 0.99, 'wind_deg': 294, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641816000, 'temp': 3.1, 'feels_like': 3.1, 'pressure': 1019, 'humidity': 97, 'dew_point': 2.67, 'uvi': 0.37, 'clouds': 95, 'visibility': 8763, 'wind_speed': 0.79, 'wind_deg': 293, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 3.6, 'feels_like': 3.6, 'pressure': 1019, 'humidity': 96, 'dew_point': 3.02, 'uvi': 1.49, 'clouds': 100, 'visibility': 9227, 'wind_speed': 0.48, 'wind_deg': 318, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641823200, 'temp': 4.11, 'feels_like': 4.11, 'pressure': 1020, 'humidity': 94, 'dew_point': 3.23, 'uvi': 3.77, 'clouds': 100, 'visibility': 8631, 'wind_speed': 0.44, 'wind_deg': 342, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641826800, 'temp': 5.19, 'feels_like': 5.19, 'pressure': 1020, 'humidity': 90, 'dew_point': 3.69, 'uvi': 6.55, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 311, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641830400, 'temp': 6.16, 'feels_like': 6.16, 'pressure': 1018, 'humidity': 87, 'dew_point': 4.16, 'uvi': 11.58, 'clouds': 100, 'visibility': 8686, 'wind_speed': 0.7, 'wind_deg': 295, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641834000, 'temp': 6.46, 'feels_like': 6.46, 'pressure': 1017, 'humidity': 88, 'dew_point': 4.62, 'uvi': 12.92, 'clouds': 99, 'visibility': 6117, 'wind_speed': 0.56, 'wind_deg': 285, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641837600, 'temp': 6.55, 'feels_like': 6.55, 'pressure': 1017, 'humidity': 88, 'dew_point': 4.71, 'uvi': 12.01, 'clouds': 83, 'visibility': 8769, 'wind_speed': 0.82, 'wind_deg': 279, 'wind_gust': 0.98, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.07}}, {'dt': 1641841200, 'temp': 6.39, 'feels_like': 6.39, 'pressure': 1015, 'humidity': 89, 'dew_point': 4.71, 'uvi': 9.66, 'clouds': 96, 'visibility': 6616, 'wind_speed': 0.9, 'wind_deg': 286, 'wind_gust': 1.14, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641844800, 'temp': 5.79, 'feels_like': 5.79, 'pressure': 1015, 'humidity': 91, 'dew_point': 4.44, 'uvi': 5.87, 'clouds': 97, 'visibility': 7988, 'wind_speed': 1.17, 'wind_deg': 285, 'wind_gust': 1.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.2}}, {'dt': 1641848400, 'temp': 5.16, 'feels_like': 5.16, 'pressure': 1015, 'humidity': 93, 'dew_point': 4.12, 'uvi': 2.57, 'clouds': 97, 'visibility': 8980, 'wind_speed': 0.98, 'wind_deg': 285, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}, {'dt': 1641852000, 'temp': 4.68, 'feels_like': 4.68, 'pressure': 1015, 'humidity': 95, 'dew_point': 3.95, 'uvi': 0.63, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 289, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641855600, 'temp': 3.3, 'feels_like': 3.3, 'pressure': 1017, 'humidity': 97, 'dew_point': 2.87, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 297, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.8}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 00:00:00 | 94.000000 | 2.990000 | 4.020000 | 93.000000 | 1017.000000 | 0.24 | 4.020000 | 0.000000 | 9605.000000 | 309.000000 | 0.77 | 0.180000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 2.710000 | 3.890000 | 92.000000 | 1018.000000 | 0.22 | 3.890000 | 0.000000 | 9120.000000 | 314.000000 | 0.67 | 0.110000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 2.410000 | 3.740000 | 91.000000 | 1019.000000 | 0.22 | 3.740000 | 0.000000 | 8313.000000 | 323.000000 | 0.67 | 0.170000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 2.710000 | 3.430000 | 95.000000 | 1019.000000 | 0.14 | 3.430000 | 0.000000 | 8122.000000 | 308.000000 | 0.72 | 0.350000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 2.310000 | 2.590000 | 98.000000 | 1020.000000 | 0.2 | 2.590000 | 0.000000 | 8123.000000 | 278.000000 | 0.55 | 0.340000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 2.150000 | 2.430000 | 98.000000 | 1019.000000 | 0.12 | 2.430000 | 0.000000 | 8200.000000 | 284.000000 | 0.34 | 0.220000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 2.100000 | 2.240000 | 99.000000 | 1018.000000 | 0.17 | 2.240000 | 0.000000 | 9010.000000 | 277.000000 | 0.89 | 0.720000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 2.010000 | 2.150000 | 99.000000 | 1018.000000 | 0.16 | 2.150000 | 0.000000 | 10000.000000 | 276.000000 | 1.09 | 0.880000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 1.800000 | 1.940000 | 99.000000 | 1017.000000 | 0.18 | 1.940000 | 0.000000 | 8903.000000 | 279.000000 | 1.4 | 0.940000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 1.730000 | 2.160000 | 97.000000 | 1017.000000 | 0.18 | 2.160000 | 0.000000 | 8693.000000 | 279.000000 | 1.69 | 1.290000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 2.260000 | 2.540000 | 98.000000 | 1018.000000 | 0.35 | 2.540000 | 0.000000 | 8622.000000 | 286.000000 | 1.85 | 1.090000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 2.180000 | 2.610000 | 97.000000 | 1018.000000 | 0.17 | 2.610000 | 0.000000 | 9404.000000 | 294.000000 | 1.5 | 0.990000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 12:00:00 | 95.000000 | 2.670000 | 3.100000 | 97.000000 | 1019.000000 |  | 3.100000 | 0.370000 | 8763.000000 | 293.000000 | 1.26 | 0.790000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 3.020000 | 3.600000 | 96.000000 | 1019.000000 | 0.31 | 3.600000 | 1.490000 | 9227.000000 | 318.000000 | 0.99 | 0.480000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 3.230000 | 4.110000 | 94.000000 | 1020.000000 | 0.3 | 4.110000 | 3.770000 | 8631.000000 | 342.000000 | 1.02 | 0.440000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 3.690000 | 5.190000 | 90.000000 | 1020.000000 | 0.21 | 5.190000 | 6.550000 | 10000.000000 | 311.000000 | 0.77 | 0.580000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 4.160000 | 6.160000 | 87.000000 | 1018.000000 | 0.55 | 6.160000 | 11.580000 | 8686.000000 | 295.000000 | 0.96 | 0.700000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 4.620000 | 6.460000 | 88.000000 | 1017.000000 | 0.91 | 6.460000 | 12.920000 | 6117.000000 | 285.000000 | 0.91 | 0.560000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 4.710000 | 6.550000 | 88.000000 | 1017.000000 | 1.07 | 6.550000 | 12.010000 | 8769.000000 | 279.000000 | 0.98 | 0.820000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 19:00:00 | 96.000000 | 4.710000 | 6.390000 | 89.000000 | 1015.000000 | 1.15 | 6.390000 | 9.660000 | 6616.000000 | 286.000000 | 1.14 | 0.900000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 20:00:00 | 97.000000 | 4.440000 | 5.790000 | 91.000000 | 1015.000000 | 1.2 | 5.790000 | 5.870000 | 7988.000000 | 285.000000 | 1.44 | 1.170000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 21:00:00 | 97.000000 | 4.120000 | 5.160000 | 93.000000 | 1015.000000 | 0.99 | 5.160000 | 2.570000 | 8980.000000 | 285.000000 | 1.32 | 0.980000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 3.950000 | 4.680000 | 95.000000 | 1015.000000 | 0.81 | 4.680000 | 0.630000 | 10000.000000 | 289.000000 | 1.22 | 0.880000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22025040 | "EL DIABLO - AUT [22025040]" | 2.980000 | -76.060000 | 4100.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-31 00:00:00 | 2021-11-19 15:39:30 | Cauca | Páez (Belalcázar) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 23:00:00 | 92.000000 | 2.870000 | 3.300000 | 97.000000 | 1017.000000 | 0.8 | 3.300000 | 0.000000 | 10000.000000 | 297.000000 | 1.03 | 0.720000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station22025040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station22025040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station22025040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22025040_OWM_Windspeed_20220111.png)
