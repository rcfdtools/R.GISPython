
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VOLCAN CHILES  - AUT [52055160] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055160_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=0.84658333,-77.92122222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=0.84658333&lon=-77.92122222)


| Parameter | Value |
|---|---|
| Code | 52055160 |
| Name | VOLCAN CHILES  - AUT [52055160] |
| Latitude, ° | 0.84658333 |
| Longitude, ° | -77.92122222 |
| Elevation, m | 442 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-16 19:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Cumbal |
| Stream | 0 |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Mira |
| SZH - Hydrographic subzone | Río San Juan (Frontera Ecuador) |

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

### (CNE index 918) Open Weather values for station 52055160 - VOLCAN CHILES  - AUT [52055160]

JSON data from API OWM:

```
{'lat': 0.8466, 'lon': -77.9212, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813408, 'sunset': 1641856874, 'temp': 6.8, 'feels_like': 5.4, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.59, 'uvi': 1.56, 'clouds': 99, 'visibility': 2654, 'wind_speed': 2.07, 'wind_deg': 302, 'wind_gust': 2.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, 'hourly': [{'dt': 1641772800, 'temp': 6.26, 'feels_like': 6.26, 'pressure': 1017, 'humidity': 97, 'dew_point': 5.82, 'uvi': 0, 'clouds': 100, 'visibility': 3069, 'wind_speed': 0.8, 'wind_deg': 313, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641776400, 'temp': 4.11, 'feels_like': 4.11, 'pressure': 1018, 'humidity': 96, 'dew_point': 3.53, 'uvi': 0, 'clouds': 100, 'visibility': 8512, 'wind_speed': 0.41, 'wind_deg': 349, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641780000, 'temp': 4.02, 'feels_like': 4.02, 'pressure': 1019, 'humidity': 94, 'dew_point': 3.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 34, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 3.96, 'feels_like': 3.96, 'pressure': 1020, 'humidity': 94, 'dew_point': 3.08, 'uvi': 0, 'clouds': 100, 'visibility': 8856, 'wind_speed': 0.46, 'wind_deg': 74, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 3.84, 'feels_like': 3.84, 'pressure': 1019, 'humidity': 94, 'dew_point': 2.96, 'uvi': 0, 'clouds': 100, 'visibility': 8795, 'wind_speed': 0.22, 'wind_deg': 100, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 3.46, 'feels_like': 3.46, 'pressure': 1019, 'humidity': 95, 'dew_point': 2.74, 'uvi': 0, 'clouds': 100, 'visibility': 6113, 'wind_speed': 0.13, 'wind_deg': 197, 'wind_gust': 0.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641794400, 'temp': 3.14, 'feels_like': 3.14, 'pressure': 1018, 'humidity': 95, 'dew_point': 2.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 254, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641798000, 'temp': 2.78, 'feels_like': 2.78, 'pressure': 1018, 'humidity': 95, 'dew_point': 2.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 248, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 2.61, 'feels_like': 2.61, 'pressure': 1017, 'humidity': 94, 'dew_point': 1.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 85, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 2.6, 'feels_like': 2.6, 'pressure': 1017, 'humidity': 93, 'dew_point': 1.58, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 322, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 2.31, 'feels_like': 2.31, 'pressure': 1018, 'humidity': 92, 'dew_point': 1.15, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 47, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 0.26, 'feels_like': 0.26, 'pressure': 1018, 'humidity': 91, 'dew_point': -0.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 65, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 1.26, 'feels_like': 1.26, 'pressure': 1019, 'humidity': 89, 'dew_point': -0.31, 'uvi': 0.36, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 31, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 2.8, 'feels_like': 2.8, 'pressure': 1019, 'humidity': 85, 'dew_point': 0.53, 'uvi': 1.69, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 314, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 4.8, 'feels_like': 4.8, 'pressure': 1019, 'humidity': 81, 'dew_point': 1.82, 'uvi': 4.37, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 300, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 7.8, 'feels_like': 7.21, 'pressure': 1019, 'humidity': 77, 'dew_point': 4.03, 'uvi': 7.72, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 304, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641830400, 'temp': 8.8, 'feels_like': 7.97, 'pressure': 1018, 'humidity': 79, 'dew_point': 5.36, 'uvi': 7.18, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 304, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641834000, 'temp': 10.8, 'feels_like': 10.13, 'pressure': 1018, 'humidity': 84, 'dew_point': 8.21, 'uvi': 8.13, 'clouds': 99, 'visibility': 5986, 'wind_speed': 1.69, 'wind_deg': 307, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641837600, 'temp': 11.8, 'feels_like': 11.33, 'pressure': 1017, 'humidity': 88, 'dew_point': 9.88, 'uvi': 7.71, 'clouds': 93, 'visibility': 5148, 'wind_speed': 1.81, 'wind_deg': 311, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641841200, 'temp': 9.8, 'feels_like': 9.02, 'pressure': 1016, 'humidity': 91, 'dew_point': 8.4, 'uvi': 2.48, 'clouds': 100, 'visibility': 3180, 'wind_speed': 1.93, 'wind_deg': 306, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641844800, 'temp': 6.8, 'feels_like': 5.4, 'pressure': 1016, 'humidity': 92, 'dew_point': 5.59, 'uvi': 1.56, 'clouds': 99, 'visibility': 2654, 'wind_speed': 2.07, 'wind_deg': 302, 'wind_gust': 2.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641848400, 'temp': 5.8, 'feels_like': 4.29, 'pressure': 1015, 'humidity': 94, 'dew_point': 4.91, 'uvi': 0.72, 'clouds': 99, 'visibility': 948, 'wind_speed': 2.01, 'wind_deg': 301, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641852000, 'temp': 5.8, 'feels_like': 4.52, 'pressure': 1015, 'humidity': 95, 'dew_point': 5.06, 'uvi': 0.22, 'clouds': 99, 'visibility': 1091, 'wind_speed': 1.79, 'wind_deg': 307, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641855600, 'temp': 5.26, 'feels_like': 5.26, 'pressure': 1017, 'humidity': 96, 'dew_point': 4.68, 'uvi': 0, 'clouds': 100, 'visibility': 4015, 'wind_speed': 1.21, 'wind_deg': 312, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 5.820000 | 6.260000 | 97.000000 | 1017.000000 | 0.13 | 6.260000 | 0.000000 | 3069.000000 | 313.000000 | 1.14 | 0.800000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 3.530000 | 4.110000 | 96.000000 | 1018.000000 | 0.18 | 4.110000 | 0.000000 | 8512.000000 | 349.000000 | 0.86 | 0.410000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 3.140000 | 4.020000 | 94.000000 | 1019.000000 |  | 4.020000 | 0.000000 | 10000.000000 | 34.000000 | 0.66 | 0.200000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 3.080000 | 3.960000 | 94.000000 | 1020.000000 |  | 3.960000 | 0.000000 | 8856.000000 | 74.000000 | 0.84 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 2.960000 | 3.840000 | 94.000000 | 1019.000000 |  | 3.840000 | 0.000000 | 8795.000000 | 100.000000 | 0.75 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 2.740000 | 3.460000 | 95.000000 | 1019.000000 | 0.14 | 3.460000 | 0.000000 | 6113.000000 | 197.000000 | 0.5 | 0.130000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 2.420000 | 3.140000 | 95.000000 | 1018.000000 | 0.14 | 3.140000 | 0.000000 | 10000.000000 | 254.000000 | 0.64 | 0.430000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 2.060000 | 2.780000 | 95.000000 | 1018.000000 |  | 2.780000 | 0.000000 | 10000.000000 | 248.000000 | 0.79 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 1.740000 | 2.610000 | 94.000000 | 1017.000000 |  | 2.610000 | 0.000000 | 10000.000000 | 85.000000 | 0.51 | 0.130000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 1.580000 | 2.600000 | 93.000000 | 1017.000000 |  | 2.600000 | 0.000000 | 10000.000000 | 322.000000 | 0.74 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 1.150000 | 2.310000 | 92.000000 | 1018.000000 |  | 2.310000 | 0.000000 | 10000.000000 | 47.000000 | 0.96 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | -0.910000 | 0.260000 | 91.000000 | 1018.000000 |  | 0.260000 | 0.000000 | 10000.000000 | 65.000000 | 0.88 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 12:00:00 | 94.000000 | -0.310000 | 1.260000 | 89.000000 | 1019.000000 |  | 1.260000 | 0.360000 | 10000.000000 | 31.000000 | 0.73 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 13:00:00 | 95.000000 | 0.530000 | 2.800000 | 85.000000 | 1019.000000 |  | 2.800000 | 1.690000 | 10000.000000 | 314.000000 | 0.79 | 0.860000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 1.820000 | 4.800000 | 81.000000 | 1019.000000 |  | 4.800000 | 4.370000 | 10000.000000 | 300.000000 | 0.75 | 1.110000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 4.030000 | 7.210000 | 77.000000 | 1019.000000 | 0.22 | 7.800000 | 7.720000 | 10000.000000 | 304.000000 | 1.22 | 1.440000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 5.360000 | 7.970000 | 79.000000 | 1018.000000 | 0.53 | 8.800000 | 7.180000 | 10000.000000 | 304.000000 | 1.6 | 1.810000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 8.210000 | 10.130000 | 84.000000 | 1018.000000 | 0.65 | 10.800000 | 8.130000 | 5986.000000 | 307.000000 | 1.62 | 1.690000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 18:00:00 | 93.000000 | 9.880000 | 11.330000 | 88.000000 | 1017.000000 | 0.67 | 11.800000 | 7.710000 | 5148.000000 | 311.000000 | 1.74 | 1.810000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 8.400000 | 9.020000 | 91.000000 | 1016.000000 | 0.86 | 9.800000 | 2.480000 | 3180.000000 | 306.000000 | 1.99 | 1.930000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 5.590000 | 5.400000 | 92.000000 | 1016.000000 | 0.66 | 6.800000 | 1.560000 | 2654.000000 | 302.000000 | 2.16 | 2.070000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 4.910000 | 4.290000 | 94.000000 | 1015.000000 | 0.53 | 5.800000 | 0.720000 | 948.000000 | 301.000000 | 2.06 | 2.010000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 5.060000 | 4.520000 | 95.000000 | 1015.000000 | 0.45 | 5.800000 | 0.220000 | 1091.000000 | 307.000000 | 1.88 | 1.790000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055160 | "VOLCAN CHILES  - AUT [52055160]" | 0.846583 | -77.921222 | 442.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-16 19:00:00 | NaT | Nariño | Cumbal | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río San Juan (Frontera Ecuador) | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 4.680000 | 5.260000 | 96.000000 | 1017.000000 | 0.54 | 5.260000 | 0.000000 | 4015.000000 | 312.000000 | 1.46 | 1.210000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055160_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055160_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055160_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055160_OWM_Windspeed_20220111.png)
