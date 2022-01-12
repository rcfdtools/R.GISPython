
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21235030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.30533333,-74.80811111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.30533333&lon=-74.80811111)


| Parameter | Value |
|---|---|
| Code | 21235030 |
| Name | UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030] |
| Latitude, ° | 4.30533333 |
| Longitude, ° | -74.80811111 |
| Elevation, m | 309 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-09-29 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Girardot |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Seco y otros Directos al Magdalena |

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

### (CNE index 93) Open Weather values for station 21235030 - UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]

JSON data from API OWM:

```
{'lat': 4.3053, 'lon': -74.8081, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812995, 'sunset': 1641855792, 'temp': 28.98, 'feels_like': 29.51, 'pressure': 1006, 'humidity': 49, 'dew_point': 17.19, 'uvi': 5.14, 'clouds': 13, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 133, 'wind_gust': 2.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.98, 'feels_like': 28.35, 'pressure': 1009, 'humidity': 64, 'dew_point': 19.59, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 5, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1010, 'humidity': 69, 'dew_point': 19.85, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 33, 'wind_gust': 2.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1011, 'humidity': 75, 'dew_point': 21.21, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 23, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641783600, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1012, 'humidity': 79, 'dew_point': 22.06, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 27, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641787200, 'temp': 23.47, 'feels_like': 24.01, 'pressure': 1012, 'humidity': 82, 'dew_point': 20.22, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 31, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 23.06, 'feels_like': 23.61, 'pressure': 1011, 'humidity': 84, 'dew_point': 20.21, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 35, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641794400, 'temp': 22.58, 'feels_like': 23.14, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.12, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 50, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.24, 'feels_like': 22.82, 'pressure': 1010, 'humidity': 88, 'dew_point': 20.16, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 57, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641801600, 'temp': 21.87, 'feels_like': 22.46, 'pressure': 1010, 'humidity': 90, 'dew_point': 20.16, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 35, 'wind_gust': 0.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641805200, 'temp': 21.7, 'feels_like': 22.3, 'pressure': 1010, 'humidity': 91, 'dew_point': 20.17, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 26, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641808800, 'temp': 21.61, 'feels_like': 22.2, 'pressure': 1011, 'humidity': 91, 'dew_point': 20.08, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 52, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641812400, 'temp': 23.98, 'feels_like': 24.84, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.6, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 42, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.55}}, {'dt': 1641816000, 'temp': 24.98, 'feels_like': 25.86, 'pressure': 1013, 'humidity': 89, 'dew_point': 23.04, 'uvi': 0.21, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 13, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641819600, 'temp': 24.98, 'feels_like': 25.75, 'pressure': 1014, 'humidity': 85, 'dew_point': 22.28, 'uvi': 1.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 346, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641823200, 'temp': 24.98, 'feels_like': 25.67, 'pressure': 1014, 'humidity': 82, 'dew_point': 21.69, 'uvi': 4.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 97, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641826800, 'temp': 26.98, 'feels_like': 29.25, 'pressure': 1014, 'humidity': 75, 'dew_point': 22.17, 'uvi': 8.02, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 77, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 27.98, 'feels_like': 30.12, 'pressure': 1013, 'humidity': 66, 'dew_point': 21.04, 'uvi': 11.69, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 36, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.98, 'feels_like': 30.7, 'pressure': 1011, 'humidity': 58, 'dew_point': 19.88, 'uvi': 12.8, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 12, 'wind_gust': 2.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.98, 'feels_like': 31.51, 'pressure': 1009, 'humidity': 53, 'dew_point': 19.36, 'uvi': 11.69, 'clouds': 5, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 70, 'wind_gust': 2.21, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 30.98, 'feels_like': 32.58, 'pressure': 1008, 'humidity': 50, 'dew_point': 19.34, 'uvi': 8.74, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 151, 'wind_gust': 2.39, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641844800, 'temp': 28.98, 'feels_like': 29.51, 'pressure': 1006, 'humidity': 49, 'dew_point': 17.19, 'uvi': 5.14, 'clouds': 13, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 133, 'wind_gust': 2.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641848400, 'temp': 27.98, 'feels_like': 28.43, 'pressure': 1006, 'humidity': 50, 'dew_point': 16.6, 'uvi': 2.12, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 117, 'wind_gust': 2.02, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641852000, 'temp': 27.98, 'feels_like': 29, 'pressure': 1007, 'humidity': 56, 'dew_point': 18.39, 'uvi': 0.49, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 73, 'wind_gust': 2.41, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 26.98, 'feels_like': 28.35, 'pressure': 1008, 'humidity': 64, 'dew_point': 19.59, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 1, 'wind_gust': 1.58, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 74.000000 | 19.590000 | 28.350000 | 64.000000 | 1009.000000 |  | 26.980000 | 0.000000 | 10000.000000 | 5.000000 | 1.72 | 1.440000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 76.000000 | 19.850000 | 25.980000 | 69.000000 | 1010.000000 | 0.12 | 25.980000 | 0.000000 | 10000.000000 | 33.000000 | 2.02 | 1.650000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 70.000000 | 21.210000 | 25.980000 | 75.000000 | 1011.000000 | 0.31 | 25.980000 | 0.000000 | 10000.000000 | 23.000000 | 1.57 | 1.380000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 22.060000 | 25.980000 | 79.000000 | 1012.000000 | 0.29 | 25.980000 | 0.000000 | 10000.000000 | 27.000000 | 1.72 | 1.570000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 84.000000 | 20.220000 | 24.010000 | 82.000000 | 1012.000000 | 0.13 | 23.470000 | 0.000000 | 10000.000000 | 31.000000 | 1.42 | 1.200000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 87.000000 | 20.210000 | 23.610000 | 84.000000 | 1011.000000 | 0.14 | 23.060000 | 0.000000 | 10000.000000 | 35.000000 | 0.93 | 0.720000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 62.000000 | 20.120000 | 23.140000 | 86.000000 | 1011.000000 |  | 22.580000 | 0.000000 | 10000.000000 | 50.000000 | 0.81 | 0.530000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 67.000000 | 20.160000 | 22.820000 | 88.000000 | 1010.000000 | 0.11 | 22.240000 | 0.000000 | 10000.000000 | 57.000000 | 0.82 | 0.590000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 51.000000 | 20.160000 | 22.460000 | 90.000000 | 1010.000000 | 0.28 | 21.870000 | 0.000000 | 10000.000000 | 35.000000 | 0.48 | 0.330000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 47.000000 | 20.170000 | 22.300000 | 91.000000 | 1010.000000 | 0.24 | 21.700000 | 0.000000 | 10000.000000 | 26.000000 | 0.7 | 0.590000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 53.000000 | 20.080000 | 22.200000 | 91.000000 | 1011.000000 | 0.34 | 21.610000 | 0.000000 | 10000.000000 | 52.000000 | 0.87 | 0.690000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 22.600000 | 24.840000 | 92.000000 | 1012.000000 | 0.55 | 23.980000 | 0.000000 | 10000.000000 | 42.000000 | 0.75 | 0.610000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 23.040000 | 25.860000 | 89.000000 | 1013.000000 | 0.51 | 24.980000 | 0.210000 | 10000.000000 | 13.000000 | 0.98 | 0.750000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 22.280000 | 25.750000 | 85.000000 | 1014.000000 | 0.47 | 24.980000 | 1.940000 | 10000.000000 | 346.000000 | 0.99 | 0.440000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 21.690000 | 25.670000 | 82.000000 | 1014.000000 | 0.14 | 24.980000 | 4.720000 | 10000.000000 | 97.000000 | 1.25 | 0.260000 | 500 | Rain | light rain | 10d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 22.170000 | 29.250000 | 75.000000 | 1014.000000 |  | 26.980000 | 8.020000 | 10000.000000 | 77.000000 | 1.82 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 87.000000 | 21.040000 | 30.120000 | 66.000000 | 1013.000000 |  | 27.980000 | 11.690000 | 10000.000000 | 36.000000 | 2.06 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 19.880000 | 30.700000 | 58.000000 | 1011.000000 |  | 28.980000 | 12.800000 | 10000.000000 | 12.000000 | 2.07 | 0.740000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 5.000000 | 19.360000 | 31.510000 | 53.000000 | 1009.000000 |  | 29.980000 | 11.690000 | 10000.000000 | 70.000000 | 2.21 | 0.390000 | 800 | Clear | clear sky | 01d | 18 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 8.000000 | 19.340000 | 32.580000 | 50.000000 | 1008.000000 |  | 30.980000 | 8.740000 | 10000.000000 | 151.000000 | 2.39 | 0.840000 | 800 | Clear | clear sky | 01d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 13.000000 | 17.190000 | 29.510000 | 49.000000 | 1006.000000 |  | 28.980000 | 5.140000 | 10000.000000 | 133.000000 | 2.55 | 0.940000 | 801 | Clouds | few clouds | 02d | 20 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 20.000000 | 16.600000 | 28.430000 | 50.000000 | 1006.000000 |  | 27.980000 | 2.120000 | 10000.000000 | 117.000000 | 2.02 | 0.720000 | 801 | Clouds | few clouds | 02d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 34.000000 | 18.390000 | 29.000000 | 56.000000 | 1007.000000 |  | 27.980000 | 0.490000 | 10000.000000 | 73.000000 | 2.41 | 0.820000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21235030 | "UNIVERSIDAD DE CUNDINAMARCA - AUT [21235030]" | 4.305333 | -74.808111 | 309.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-09-29 19:00:00 | NaT | Cundinamarca | Girardot | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Seco y otros Directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 33.000000 | 19.590000 | 28.350000 | 64.000000 | 1008.000000 |  | 26.980000 | 0.000000 | 10000.000000 | 1.000000 | 1.58 | 0.700000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station21235030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21235030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21235030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21235030_OWM_Windspeed_20220111.png)
