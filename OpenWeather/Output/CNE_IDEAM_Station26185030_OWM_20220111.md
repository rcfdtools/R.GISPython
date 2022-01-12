
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - JERICO - AUT [26185030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26185030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.79916667,-75.78952778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.79916667&lon=-75.78952778)


| Parameter | Value |
|---|---|
| Code | 26185030 |
| Name | JERICO - AUT [26185030] |
| Latitude, ° | 5.79916667 |
| Longitude, ° | -75.78952778 |
| Elevation, m | 2313 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2004-11-28 00:00:00 |
| Suspension date | 2016-01-06 00:00:00 |
| State | Antioquia |
| County | Jericó (Antioquia) |
| Stream | La Miel |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Frío y Otros Directos al Cauca |

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

### (CNE index 159) Open Weather values for station 26185030 - JERICO - AUT [26185030]

JSON data from API OWM:

```
{'lat': 5.7992, 'lon': -75.7895, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813376, 'sunset': 1641855883, 'temp': 20.12, 'feels_like': 20.02, 'pressure': 1010, 'humidity': 70, 'dew_point': 14.48, 'uvi': 4.44, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 237, 'wind_gust': 1.41, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, 'hourly': [{'dt': 1641772800, 'temp': 16.84, 'feels_like': 17.01, 'pressure': 1013, 'humidity': 93, 'dew_point': 15.7, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 230, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641776400, 'temp': 16.04, 'feels_like': 16.18, 'pressure': 1014, 'humidity': 95, 'dew_point': 15.24, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 226, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 16.04, 'feels_like': 16.18, 'pressure': 1015, 'humidity': 95, 'dew_point': 15.24, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 225, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 15.76, 'feels_like': 15.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.12, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 229, 'wind_gust': 1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.76, 'feels_like': 15.9, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.12, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 231, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 14.37, 'feels_like': 14.37, 'pressure': 1015, 'humidity': 96, 'dew_point': 13.74, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 242, 'wind_gust': 0.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.37, 'feels_like': 14.34, 'pressure': 1014, 'humidity': 95, 'dew_point': 13.58, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 252, 'wind_gust': 0.55, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.37, 'feels_like': 14.34, 'pressure': 1014, 'humidity': 95, 'dew_point': 13.58, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 304, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 13.82, 'feels_like': 13.76, 'pressure': 1013, 'humidity': 96, 'dew_point': 13.19, 'uvi': 0, 'clouds': 99, 'visibility': 8783, 'wind_speed': 0.33, 'wind_deg': 280, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 13.82, 'feels_like': 13.76, 'pressure': 1013, 'humidity': 96, 'dew_point': 13.19, 'uvi': 0, 'clouds': 99, 'visibility': 4524, 'wind_speed': 0.25, 'wind_deg': 302, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641808800, 'temp': 13.82, 'feels_like': 13.79, 'pressure': 1014, 'humidity': 97, 'dew_point': 13.35, 'uvi': 0, 'clouds': 99, 'visibility': 4265, 'wind_speed': 0.2, 'wind_deg': 296, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641812400, 'temp': 14.12, 'feels_like': 14.12, 'pressure': 1015, 'humidity': 97, 'dew_point': 13.65, 'uvi': 0, 'clouds': 98, 'visibility': 7853, 'wind_speed': 0.23, 'wind_deg': 257, 'wind_gust': 0.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 14.36, 'feels_like': 14.36, 'pressure': 1016, 'humidity': 96, 'dew_point': 13.73, 'uvi': 0.2, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 267, 'wind_gust': 0.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 15.13, 'feels_like': 15.1, 'pressure': 1017, 'humidity': 92, 'dew_point': 13.84, 'uvi': 1.19, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 45, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641823200, 'temp': 16.46, 'feels_like': 16.38, 'pressure': 1017, 'humidity': 85, 'dew_point': 13.93, 'uvi': 3.02, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 75, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641826800, 'temp': 16.45, 'feels_like': 16.27, 'pressure': 1016, 'humidity': 81, 'dew_point': 13.18, 'uvi': 5.28, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 78, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641830400, 'temp': 16.8, 'feels_like': 16.55, 'pressure': 1015, 'humidity': 77, 'dew_point': 12.75, 'uvi': 6.88, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 82, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641834000, 'temp': 16.32, 'feels_like': 15.81, 'pressure': 1014, 'humidity': 69, 'dew_point': 10.63, 'uvi': 7.65, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 279, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641837600, 'temp': 17.31, 'feels_like': 16.85, 'pressure': 1012, 'humidity': 67, 'dew_point': 11.13, 'uvi': 7.06, 'clouds': 24, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 264, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.64}}, {'dt': 1641841200, 'temp': 19.6, 'feels_like': 19.37, 'pressure': 1011, 'humidity': 67, 'dew_point': 13.31, 'uvi': 7.46, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 252, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641844800, 'temp': 20.12, 'feels_like': 20.02, 'pressure': 1010, 'humidity': 70, 'dew_point': 14.48, 'uvi': 4.44, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 237, 'wind_gust': 1.41, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641848400, 'temp': 19.26, 'feels_like': 19.41, 'pressure': 1010, 'humidity': 83, 'dew_point': 16.3, 'uvi': 1.86, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 219, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.78}}, {'dt': 1641852000, 'temp': 18.41, 'feels_like': 18.68, 'pressure': 1011, 'humidity': 91, 'dew_point': 16.91, 'uvi': 0.37, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 215, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641855600, 'temp': 17.17, 'feels_like': 17.4, 'pressure': 1013, 'humidity': 94, 'dew_point': 16.2, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 226, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 00:00:00 | 56.000000 | 15.700000 | 17.010000 | 93.000000 | 1013.000000 | 0.34 | 16.840000 | 0.000000 | 10000.000000 | 230.000000 | 1.58 | 1.360000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 01:00:00 | 66.000000 | 15.240000 | 16.180000 | 95.000000 | 1014.000000 | 0.12 | 16.040000 | 0.000000 | 10000.000000 | 226.000000 | 1.42 | 1.200000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 02:00:00 | 79.000000 | 15.240000 | 16.180000 | 95.000000 | 1015.000000 | 0.12 | 16.040000 | 0.000000 | 10000.000000 | 225.000000 | 1.05 | 1.050000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 03:00:00 | 84.000000 | 15.120000 | 15.900000 | 96.000000 | 1015.000000 |  | 15.760000 | 0.000000 | 10000.000000 | 229.000000 | 1 | 0.980000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 04:00:00 | 86.000000 | 15.120000 | 15.900000 | 96.000000 | 1015.000000 |  | 15.760000 | 0.000000 | 10000.000000 | 231.000000 | 0.68 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 05:00:00 | 88.000000 | 13.740000 | 14.370000 | 96.000000 | 1015.000000 |  | 14.370000 | 0.000000 | 10000.000000 | 242.000000 | 0.62 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 06:00:00 | 79.000000 | 13.580000 | 14.340000 | 95.000000 | 1014.000000 |  | 14.370000 | 0.000000 | 10000.000000 | 252.000000 | 0.55 | 0.480000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 13.580000 | 14.340000 | 95.000000 | 1014.000000 | 0.19 | 14.370000 | 0.000000 | 10000.000000 | 304.000000 | 0.58 | 0.270000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 13.190000 | 13.760000 | 96.000000 | 1013.000000 | 0.15 | 13.820000 | 0.000000 | 8783.000000 | 280.000000 | 0.6 | 0.330000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 13.190000 | 13.760000 | 96.000000 | 1013.000000 | 0.15 | 13.820000 | 0.000000 | 4524.000000 | 302.000000 | 0.64 | 0.250000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 13.350000 | 13.790000 | 97.000000 | 1014.000000 | 0.22 | 13.820000 | 0.000000 | 4265.000000 | 296.000000 | 0.55 | 0.200000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 13.650000 | 14.120000 | 97.000000 | 1015.000000 | 0.12 | 14.120000 | 0.000000 | 7853.000000 | 257.000000 | 0.46 | 0.230000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 12:00:00 | 74.000000 | 13.730000 | 14.360000 | 96.000000 | 1016.000000 |  | 14.360000 | 0.200000 | 10000.000000 | 267.000000 | 0.37 | 0.090000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 13.840000 | 15.100000 | 92.000000 | 1017.000000 | 0.12 | 15.130000 | 1.190000 | 10000.000000 | 45.000000 | 0.53 | 0.190000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 14:00:00 | 89.000000 | 13.930000 | 16.380000 | 85.000000 | 1017.000000 | 0.24 | 16.460000 | 3.020000 | 10000.000000 | 75.000000 | 0.73 | 0.280000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 15:00:00 | 78.000000 | 13.180000 | 16.270000 | 81.000000 | 1016.000000 | 0.39 | 16.450000 | 5.280000 | 10000.000000 | 78.000000 | 0.87 | 0.460000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 16:00:00 | 74.000000 | 12.750000 | 16.550000 | 77.000000 | 1015.000000 | 0.38 | 16.800000 | 6.880000 | 10000.000000 | 82.000000 | 0.76 | 0.240000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | 10.630000 | 15.810000 | 69.000000 | 1014.000000 | 0.41 | 16.320000 | 7.650000 | 10000.000000 | 279.000000 | 0.91 | 0.100000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 18:00:00 | 24.000000 | 11.130000 | 16.850000 | 67.000000 | 1012.000000 | 0.64 | 17.310000 | 7.060000 | 10000.000000 | 264.000000 | 1.09 | 0.510000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 19:00:00 | 48.000000 | 13.310000 | 19.370000 | 67.000000 | 1011.000000 | 0.96 | 19.600000 | 7.460000 | 10000.000000 | 252.000000 | 1.38 | 0.910000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 20:00:00 | 70.000000 | 14.480000 | 20.020000 | 70.000000 | 1010.000000 | 1.16 | 20.120000 | 4.440000 | 10000.000000 | 237.000000 | 1.41 | 1.040000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 21:00:00 | 80.000000 | 16.300000 | 19.410000 | 83.000000 | 1010.000000 | 0.78 | 19.260000 | 1.860000 | 10000.000000 | 219.000000 | 1.62 | 1.050000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 22:00:00 | 85.000000 | 16.910000 | 18.680000 | 91.000000 | 1011.000000 | 0.86 | 18.410000 | 0.370000 | 10000.000000 | 215.000000 | 1.32 | 1.030000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185030 | "JERICO - AUT [26185030]" | 5.799167 | -75.789528 | 2313.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-11-28 00:00:00 | 2016-01-06 00:00:00 | Antioquia | Jericó (Antioquia) | La Miel | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 16.200000 | 17.400000 | 94.000000 | 1013.000000 | 0.31 | 17.170000 | 0.000000 | 10000.000000 | 226.000000 | 1.24 | 0.970000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26185030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26185030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26185030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185030_OWM_Windspeed_20220111.png)
