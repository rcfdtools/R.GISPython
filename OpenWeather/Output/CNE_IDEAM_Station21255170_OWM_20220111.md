
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MURILLO - AUT [21255170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21255170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.87055556,-75.17327778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.87055556&lon=-75.17327778)


| Parameter | Value |
|---|---|
| Code | 21255170 |
| Name | MURILLO - AUT [21255170] |
| Latitude, ° | 4.87055556 |
| Longitude, ° | -75.17327778 |
| Elevation, m | 323 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-10-21 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Murillo |
| Stream | Lagunilla |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Lagunilla y Otros Directos al Magdalena |

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

### (CNE index 112) Open Weather values for station 21255170 - MURILLO - AUT [21255170]

JSON data from API OWM:

```
{'lat': 4.8706, 'lon': -75.1733, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813137, 'sunset': 1641855825, 'temp': 8.76, 'feels_like': 8.76, 'pressure': 1014, 'humidity': 82, 'dew_point': 5.86, 'uvi': 3, 'clouds': 83, 'visibility': 9934, 'wind_speed': 0.99, 'wind_deg': 36, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, 'hourly': [{'dt': 1641772800, 'temp': 9.44, 'feels_like': 9.44, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.52, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 303, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641776400, 'temp': 8.44, 'feels_like': 8.44, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.37, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 300, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 8.44, 'feels_like': 8.44, 'pressure': 1019, 'humidity': 92, 'dew_point': 7.22, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 286, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.44, 'feels_like': 8.02, 'pressure': 1019, 'humidity': 92, 'dew_point': 7.22, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 282, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 9.19, 'feels_like': 8.79, 'pressure': 1019, 'humidity': 91, 'dew_point': 7.8, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 279, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 9.19, 'feels_like': 8.76, 'pressure': 1019, 'humidity': 93, 'dew_point': 8.12, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 273, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 9.19, 'feels_like': 8.75, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.12, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 276, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 9.19, 'feels_like': 8.81, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.28, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 271, 'wind_gust': 1.1, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 7.09, 'feels_like': 6.25, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.19, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 272, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 6.76, 'feels_like': 5.68, 'pressure': 1017, 'humidity': 95, 'dew_point': 6.02, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 272, 'wind_gust': 1.31, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 8.19, 'feels_like': 7.18, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.28, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 272, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 7.79, 'feels_like': 6.65, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.89, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 275, 'wind_gust': 1.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 7.98, 'feels_like': 7.31, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0.14, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 273, 'wind_gust': 1.58, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 85, 'dew_point': 5.62, 'uvi': 1.92, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 20, 'wind_gust': 1.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 8.79, 'feels_like': 8.79, 'pressure': 1019, 'humidity': 80, 'dew_point': 5.53, 'uvi': 4.8, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 58, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641826800, 'temp': 10.79, 'feels_like': 9.83, 'pressure': 1018, 'humidity': 73, 'dew_point': 6.15, 'uvi': 8.25, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 56, 'wind_gust': 2.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641830400, 'temp': 13.39, 'feels_like': 12.74, 'pressure': 1018, 'humidity': 75, 'dew_point': 9.06, 'uvi': 9.29, 'clouds': 45, 'visibility': 9826, 'wind_speed': 1.86, 'wind_deg': 59, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641834000, 'temp': 11.18, 'feels_like': 10.42, 'pressure': 1017, 'humidity': 79, 'dew_point': 7.68, 'uvi': 10.23, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 53, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641837600, 'temp': 9.76, 'feels_like': 9.76, 'pressure': 1016, 'humidity': 83, 'dew_point': 7.01, 'uvi': 9.4, 'clouds': 71, 'visibility': 8307, 'wind_speed': 1.26, 'wind_deg': 42, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641841200, 'temp': 9.96, 'feels_like': 9.96, 'pressure': 1015, 'humidity': 83, 'dew_point': 7.21, 'uvi': 5.06, 'clouds': 86, 'visibility': 9089, 'wind_speed': 1, 'wind_deg': 29, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641844800, 'temp': 8.76, 'feels_like': 8.76, 'pressure': 1014, 'humidity': 82, 'dew_point': 5.86, 'uvi': 3, 'clouds': 83, 'visibility': 9934, 'wind_speed': 0.99, 'wind_deg': 36, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641848400, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1014, 'humidity': 84, 'dew_point': 6.81, 'uvi': 1.25, 'clouds': 87, 'visibility': 8881, 'wind_speed': 0.77, 'wind_deg': 37, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641852000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1015, 'humidity': 90, 'dew_point': 7.82, 'uvi': 0.4, 'clouds': 85, 'visibility': 3293, 'wind_speed': 0.8, 'wind_deg': 17, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641855600, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1016, 'humidity': 95, 'dew_point': 7.62, 'uvi': 0, 'clouds': 85, 'visibility': 7288, 'wind_speed': 0.99, 'wind_deg': 303, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.84}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 67.000000 | 8.520000 | 9.440000 | 94.000000 | 1017.000000 | 0.32 | 9.440000 | 0.000000 | 10000.000000 | 303.000000 | 1.07 | 1.080000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 89.000000 | 7.370000 | 8.440000 | 93.000000 | 1018.000000 | 0.12 | 8.440000 | 0.000000 | 10000.000000 | 300.000000 | 0.88 | 1.070000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 82.000000 | 7.220000 | 8.440000 | 92.000000 | 1019.000000 |  | 8.440000 | 0.000000 | 10000.000000 | 286.000000 | 1.02 | 1.320000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 7.220000 | 8.020000 | 92.000000 | 1019.000000 |  | 8.440000 | 0.000000 | 10000.000000 | 282.000000 | 1.07 | 1.370000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 80.000000 | 7.800000 | 8.790000 | 91.000000 | 1019.000000 |  | 9.190000 | 0.000000 | 10000.000000 | 279.000000 | 1.09 | 1.440000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 80.000000 | 8.120000 | 8.760000 | 93.000000 | 1019.000000 |  | 9.190000 | 0.000000 | 10000.000000 | 273.000000 | 1.05 | 1.470000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 36.000000 | 8.120000 | 8.750000 | 93.000000 | 1018.000000 |  | 9.190000 | 0.000000 | 10000.000000 | 276.000000 | 1.11 | 1.480000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 36.000000 | 8.280000 | 8.810000 | 94.000000 | 1017.000000 |  | 9.190000 | 0.000000 | 10000.000000 | 271.000000 | 1.1 | 1.420000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 41.000000 | 6.190000 | 6.250000 | 94.000000 | 1017.000000 | 0.13 | 7.090000 | 0.000000 | 10000.000000 | 272.000000 | 1.23 | 1.570000 | 500 | Rain | light rain | 10n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 45.000000 | 6.020000 | 5.680000 | 95.000000 | 1017.000000 |  | 6.760000 | 0.000000 | 10000.000000 | 272.000000 | 1.31 | 1.740000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 53.000000 | 7.280000 | 7.180000 | 94.000000 | 1018.000000 |  | 8.190000 | 0.000000 | 10000.000000 | 272.000000 | 1.7 | 1.890000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 59.000000 | 6.890000 | 6.650000 | 94.000000 | 1018.000000 |  | 7.790000 | 0.000000 | 10000.000000 | 275.000000 | 1.71 | 1.970000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 30.000000 | 6.760000 | 7.310000 | 92.000000 | 1019.000000 |  | 7.980000 | 0.140000 | 10000.000000 | 273.000000 | 1.58 | 1.530000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 38.000000 | 5.620000 | 7.980000 | 85.000000 | 1019.000000 |  | 7.980000 | 1.920000 | 10000.000000 | 20.000000 | 1.37 | 0.480000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 36.000000 | 5.530000 | 8.790000 | 80.000000 | 1019.000000 | 0.22 | 8.790000 | 4.800000 | 10000.000000 | 58.000000 | 2.04 | 1.320000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 32.000000 | 6.150000 | 9.830000 | 73.000000 | 1018.000000 | 0.26 | 10.790000 | 8.250000 | 10000.000000 | 56.000000 | 2.54 | 1.750000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 45.000000 | 9.060000 | 12.740000 | 75.000000 | 1018.000000 | 0.22 | 13.390000 | 9.290000 | 9826.000000 | 59.000000 | 2.04 | 1.860000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 53.000000 | 7.680000 | 10.420000 | 79.000000 | 1017.000000 | 0.31 | 11.180000 | 10.230000 | 10000.000000 | 53.000000 | 1.85 | 1.610000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 71.000000 | 7.010000 | 9.760000 | 83.000000 | 1016.000000 | 0.5 | 9.760000 | 9.400000 | 8307.000000 | 42.000000 | 1.5 | 1.260000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 86.000000 | 7.210000 | 9.960000 | 83.000000 | 1015.000000 | 0.58 | 9.960000 | 5.060000 | 9089.000000 | 29.000000 | 1.52 | 1.000000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 83.000000 | 5.860000 | 8.760000 | 82.000000 | 1014.000000 | 0.58 | 8.760000 | 3.000000 | 9934.000000 | 36.000000 | 1.33 | 0.990000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 87.000000 | 6.810000 | 9.370000 | 84.000000 | 1014.000000 | 0.57 | 9.370000 | 1.250000 | 8881.000000 | 37.000000 | 1.24 | 0.770000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 85.000000 | 7.820000 | 9.370000 | 90.000000 | 1015.000000 | 0.48 | 9.370000 | 0.400000 | 3293.000000 | 17.000000 | 1.81 | 0.800000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255170 | "MURILLO - AUT [21255170]" | 4.870556 | -75.173278 | 323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-21 00:00:00 | NaT | Tolima | Murillo | Lagunilla | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 7.620000 | 8.370000 | 95.000000 | 1016.000000 | 0.84 | 8.370000 | 0.000000 | 7288.000000 | 303.000000 | 1.34 | 0.990000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21255170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21255170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21255170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255170_OWM_Windspeed_20220111.png)
