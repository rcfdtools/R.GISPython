
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PARAMO CHINGAZA  - AUT [35035130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35035130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.71366667,-73.80325) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.71366667&lon=-73.80325)


| Parameter | Value |
|---|---|
| Code | 35035130 |
| Name | PARAMO CHINGAZA  - AUT [35035130] |
| Latitude, ° | 4.71366667 |
| Longitude, ° | -73.80325 |
| Elevation, m | 3863 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-11-23 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Guasca |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Guayuriba |

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

### (CNE index 102) Open Weather values for station 35035130 - PARAMO CHINGAZA  - AUT [35035130]

JSON data from API OWM:

```
{'lat': 4.7137, 'lon': -73.8033, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812793, 'sunset': 1641855511, 'temp': 11, 'feels_like': 10.27, 'pressure': 1013, 'humidity': 81, 'dew_point': 7.87, 'uvi': 4.16, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 67, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, 'hourly': [{'dt': 1641772800, 'temp': 6, 'feels_like': 6, 'pressure': 1016, 'humidity': 98, 'dew_point': 5.71, 'uvi': 0, 'clouds': 98, 'visibility': 4607, 'wind_speed': 0.42, 'wind_deg': 103, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641776400, 'temp': 7, 'feels_like': 7, 'pressure': 1018, 'humidity': 98, 'dew_point': 6.71, 'uvi': 0, 'clouds': 100, 'visibility': 2335, 'wind_speed': 0.37, 'wind_deg': 115, 'wind_gust': 0.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 6, 'feels_like': 6, 'pressure': 1018, 'humidity': 98, 'dew_point': 5.71, 'uvi': 0, 'clouds': 100, 'visibility': 4575, 'wind_speed': 0.38, 'wind_deg': 104, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641783600, 'temp': 6, 'feels_like': 6, 'pressure': 1018, 'humidity': 98, 'dew_point': 5.71, 'uvi': 0, 'clouds': 100, 'visibility': 4559, 'wind_speed': 0.32, 'wind_deg': 116, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 6, 'feels_like': 6, 'pressure': 1018, 'humidity': 99, 'dew_point': 5.85, 'uvi': 0, 'clouds': 100, 'visibility': 4834, 'wind_speed': 0.24, 'wind_deg': 155, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 4, 'feels_like': 4, 'pressure': 1018, 'humidity': 98, 'dew_point': 3.71, 'uvi': 0, 'clouds': 100, 'visibility': 5331, 'wind_speed': 0.15, 'wind_deg': 179, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 2, 'feels_like': 2, 'pressure': 1017, 'humidity': 98, 'dew_point': 1.72, 'uvi': 0, 'clouds': 85, 'visibility': 5698, 'wind_speed': 0.14, 'wind_deg': 157, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641798000, 'temp': 1, 'feels_like': 1, 'pressure': 1016, 'humidity': 98, 'dew_point': 0.72, 'uvi': 0, 'clouds': 93, 'visibility': 3965, 'wind_speed': 0.35, 'wind_deg': 202, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 1, 'feels_like': 1, 'pressure': 1016, 'humidity': 98, 'dew_point': 0.72, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 232, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 1, 'feels_like': 1, 'pressure': 1016, 'humidity': 98, 'dew_point': 0.72, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 235, 'wind_gust': 0.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 2, 'feels_like': 2, 'pressure': 1017, 'humidity': 98, 'dew_point': 1.72, 'uvi': 0, 'clouds': 82, 'visibility': 7836, 'wind_speed': 0.64, 'wind_deg': 262, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3, 'feels_like': 3, 'pressure': 1018, 'humidity': 98, 'dew_point': 2.72, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 262, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 3, 'feels_like': 3, 'pressure': 1019, 'humidity': 96, 'dew_point': 2.43, 'uvi': 0.42, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 242, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 4, 'feels_like': 4, 'pressure': 1019, 'humidity': 88, 'dew_point': 2.2, 'uvi': 2.46, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 264, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 7, 'feels_like': 7, 'pressure': 1019, 'humidity': 72, 'dew_point': 2.3, 'uvi': 5.81, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 285, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 9, 'feels_like': 9, 'pressure': 1017, 'humidity': 57, 'dew_point': 0.95, 'uvi': 9.73, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 310, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 10, 'feels_like': 10, 'pressure': 1015, 'humidity': 52, 'dew_point': 0.61, 'uvi': 9.4, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 16, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 10, 'feels_like': 10, 'pressure': 1014, 'humidity': 56, 'dew_point': 1.64, 'uvi': 10.18, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 80, 'wind_gust': 2.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 11, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 70, 'dew_point': 5.75, 'uvi': 9.17, 'clouds': 73, 'visibility': 8275, 'wind_speed': 0.88, 'wind_deg': 103, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641841200, 'temp': 11, 'feels_like': 10.09, 'pressure': 1013, 'humidity': 74, 'dew_point': 6.55, 'uvi': 7.23, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 55, 'wind_gust': 1.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641844800, 'temp': 11, 'feels_like': 10.27, 'pressure': 1013, 'humidity': 81, 'dew_point': 7.87, 'uvi': 4.16, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 67, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641848400, 'temp': 11, 'feels_like': 10.43, 'pressure': 1013, 'humidity': 87, 'dew_point': 8.92, 'uvi': 1.65, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 161, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641852000, 'temp': 10, 'feels_like': 10, 'pressure': 1014, 'humidity': 93, 'dew_point': 8.92, 'uvi': 0.41, 'clouds': 90, 'visibility': 7151, 'wind_speed': 0.61, 'wind_deg': 144, 'wind_gust': 1.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641855600, 'temp': 8, 'feels_like': 8, 'pressure': 1016, 'humidity': 97, 'dew_point': 7.55, 'uvi': 0, 'clouds': 92, 'visibility': 4520, 'wind_speed': 0.51, 'wind_deg': 145, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 00:00:00 | 98.000000 | 5.710000 | 6.000000 | 98.000000 | 1016.000000 | 0.11 | 6.000000 | 0.000000 | 4607.000000 | 103.000000 | 0.99 | 0.420000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 6.710000 | 7.000000 | 98.000000 | 1018.000000 |  | 7.000000 | 0.000000 | 2335.000000 | 115.000000 | 0.89 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 5.710000 | 6.000000 | 98.000000 | 1018.000000 | 0.1 | 6.000000 | 0.000000 | 4575.000000 | 104.000000 | 0.86 | 0.380000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 5.710000 | 6.000000 | 98.000000 | 1018.000000 |  | 6.000000 | 0.000000 | 4559.000000 | 116.000000 | 0.94 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 5.850000 | 6.000000 | 99.000000 | 1018.000000 |  | 6.000000 | 0.000000 | 4834.000000 | 155.000000 | 0.75 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 3.710000 | 4.000000 | 98.000000 | 1018.000000 | 0.12 | 4.000000 | 0.000000 | 5331.000000 | 179.000000 | 0.73 | 0.150000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 06:00:00 | 85.000000 | 1.720000 | 2.000000 | 98.000000 | 1017.000000 | 0.11 | 2.000000 | 0.000000 | 5698.000000 | 157.000000 | 0.62 | 0.140000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 07:00:00 | 93.000000 | 0.720000 | 1.000000 | 98.000000 | 1016.000000 |  | 1.000000 | 0.000000 | 3965.000000 | 202.000000 | 0.7 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 08:00:00 | 92.000000 | 0.720000 | 1.000000 | 98.000000 | 1016.000000 |  | 1.000000 | 0.000000 | 10000.000000 | 232.000000 | 0.94 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 09:00:00 | 83.000000 | 0.720000 | 1.000000 | 98.000000 | 1016.000000 |  | 1.000000 | 0.000000 | 10000.000000 | 235.000000 | 0.88 | 0.690000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 10:00:00 | 82.000000 | 1.720000 | 2.000000 | 98.000000 | 1017.000000 |  | 2.000000 | 0.000000 | 7836.000000 | 262.000000 | 0.78 | 0.640000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 11:00:00 | 82.000000 | 2.720000 | 3.000000 | 98.000000 | 1018.000000 |  | 3.000000 | 0.000000 | 10000.000000 | 262.000000 | 0.89 | 0.710000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 12:00:00 | 78.000000 | 2.430000 | 3.000000 | 96.000000 | 1019.000000 |  | 3.000000 | 0.420000 | 10000.000000 | 242.000000 | 1.02 | 0.540000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 13:00:00 | 92.000000 | 2.200000 | 4.000000 | 88.000000 | 1019.000000 |  | 4.000000 | 2.460000 | 10000.000000 | 264.000000 | 1.16 | 0.490000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 2.300000 | 7.000000 | 72.000000 | 1019.000000 |  | 7.000000 | 5.810000 | 10000.000000 | 285.000000 | 1.42 | 0.450000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 0.950000 | 9.000000 | 57.000000 | 1017.000000 |  | 9.000000 | 9.730000 | 10000.000000 | 310.000000 | 2.01 | 0.510000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 16:00:00 | 68.000000 | 0.610000 | 10.000000 | 52.000000 | 1015.000000 |  | 10.000000 | 9.400000 | 10000.000000 | 16.000000 | 2.59 | 0.430000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 17:00:00 | 71.000000 | 1.640000 | 10.000000 | 56.000000 | 1014.000000 | 0.11 | 10.000000 | 10.180000 | 10000.000000 | 80.000000 | 2.52 | 0.580000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 18:00:00 | 73.000000 | 5.750000 | 9.980000 | 70.000000 | 1015.000000 | 0.1 | 11.000000 | 9.170000 | 8275.000000 | 103.000000 | 1.93 | 0.880000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 19:00:00 | 80.000000 | 6.550000 | 10.090000 | 74.000000 | 1013.000000 | 0.29 | 11.000000 | 7.230000 | 10000.000000 | 55.000000 | 1.98 | 0.860000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 20:00:00 | 86.000000 | 7.870000 | 10.270000 | 81.000000 | 1013.000000 | 0.49 | 11.000000 | 4.160000 | 10000.000000 | 67.000000 | 1.81 | 0.470000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 21:00:00 | 91.000000 | 8.920000 | 10.430000 | 87.000000 | 1013.000000 | 0.65 | 11.000000 | 1.650000 | 10000.000000 | 161.000000 | 1.56 | 0.400000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 22:00:00 | 90.000000 | 8.920000 | 10.000000 | 93.000000 | 1014.000000 | 0.28 | 10.000000 | 0.410000 | 7151.000000 | 144.000000 | 1.64 | 0.610000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35035130 | "PARAMO CHINGAZA  - AUT [35035130]" | 4.713667 | -73.803250 | 3863.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-23 19:00:00 | NaT | Cundinamarca | Guasca | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 23:00:00 | 92.000000 | 7.550000 | 8.000000 | 97.000000 | 1016.000000 | 0.25 | 8.000000 | 0.000000 | 4520.000000 | 145.000000 | 1.54 | 0.510000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station35035130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35035130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35035130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035130_OWM_Windspeed_20220111.png)
