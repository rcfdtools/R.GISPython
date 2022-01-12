
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL ESPINO - AUT [24035370] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035370_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.50672222,-72.45266667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.50672222&lon=-72.45266667)


| Parameter | Value |
|---|---|
| Code | 24035370 |
| Name | EL ESPINO - AUT [24035370] |
| Latitude, ° | 6.50672222 |
| Longitude, ° | -72.45266667 |
| Elevation, m | 3510 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-11-19 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | El Espino |
| Stream | Magdalena |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Chicamocha |

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

### (CNE index 164) Open Weather values for station 24035370 - EL ESPINO - AUT [24035370]

JSON data from API OWM:

```
{'lat': 6.5067, 'lon': -72.4527, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812643, 'sunset': 1641855013, 'temp': 11.77, 'feels_like': 10.6, 'pressure': 1013, 'humidity': 61, 'dew_point': 4.5, 'uvi': 1.62, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 271, 'wind_gust': 2.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 6.72, 'feels_like': 6.72, 'pressure': 1018, 'humidity': 95, 'dew_point': 5.98, 'uvi': 0, 'clouds': 47, 'visibility': 2796, 'wind_speed': 0.14, 'wind_deg': 320, 'wind_gust': 1.16, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 6.19, 'feels_like': 6.19, 'pressure': 1019, 'humidity': 96, 'dew_point': 5.6, 'uvi': 0, 'clouds': 60, 'visibility': 1161, 'wind_speed': 0.25, 'wind_deg': 196, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 5.91, 'feels_like': 5.91, 'pressure': 1020, 'humidity': 96, 'dew_point': 5.32, 'uvi': 0, 'clouds': 52, 'visibility': 2976, 'wind_speed': 0.3, 'wind_deg': 187, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 5.21, 'feels_like': 5.21, 'pressure': 1020, 'humidity': 95, 'dew_point': 4.48, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 98, 'wind_gust': 1.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 4.68, 'feels_like': 4.68, 'pressure': 1020, 'humidity': 94, 'dew_point': 3.8, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 103, 'wind_gust': 1.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 4.65, 'feels_like': 4.65, 'pressure': 1020, 'humidity': 92, 'dew_point': 3.46, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 100, 'wind_gust': 1.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 4.1, 'feels_like': 4.1, 'pressure': 1019, 'humidity': 94, 'dew_point': 3.22, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 106, 'wind_gust': 1.08, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 4.18, 'feels_like': 4.18, 'pressure': 1018, 'humidity': 91, 'dew_point': 2.84, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 71, 'wind_gust': 1.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 3.77, 'feels_like': 3.77, 'pressure': 1018, 'humidity': 90, 'dew_point': 2.28, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 280, 'wind_gust': 1.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 3.49, 'feels_like': 3.49, 'pressure': 1018, 'humidity': 89, 'dew_point': 1.85, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.03, 'wind_deg': 77, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 3.43, 'feels_like': 3.43, 'pressure': 1019, 'humidity': 87, 'dew_point': 1.47, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 73, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.34, 'feels_like': 3.34, 'pressure': 1019, 'humidity': 87, 'dew_point': 1.39, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 88, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 5.01, 'feels_like': 5.01, 'pressure': 1020, 'humidity': 84, 'dew_point': 2.54, 'uvi': 0.15, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 239, 'wind_gust': 1.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 7.08, 'feels_like': 7.08, 'pressure': 1020, 'humidity': 78, 'dew_point': 3.51, 'uvi': 1.16, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 263, 'wind_gust': 0.9, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 8.56, 'feels_like': 8.13, 'pressure': 1020, 'humidity': 73, 'dew_point': 4, 'uvi': 2.66, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 260, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 10.1, 'feels_like': 8.86, 'pressure': 1019, 'humidity': 65, 'dew_point': 3.83, 'uvi': 4.37, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 264, 'wind_gust': 1.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 11.58, 'feels_like': 10.33, 'pressure': 1018, 'humidity': 59, 'dew_point': 3.85, 'uvi': 7.34, 'clouds': 64, 'visibility': 10000, 'wind_speed': 3.06, 'wind_deg': 267, 'wind_gust': 2.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 12.15, 'feels_like': 10.94, 'pressure': 1017, 'humidity': 58, 'dew_point': 4.14, 'uvi': 7.81, 'clouds': 58, 'visibility': 10000, 'wind_speed': 3.35, 'wind_deg': 267, 'wind_gust': 2.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 12.36, 'feels_like': 11.17, 'pressure': 1016, 'humidity': 58, 'dew_point': 4.34, 'uvi': 6.9, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 268, 'wind_gust': 2.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 12.35, 'feels_like': 11.16, 'pressure': 1014, 'humidity': 58, 'dew_point': 4.33, 'uvi': 2.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 270, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 11.77, 'feels_like': 10.6, 'pressure': 1013, 'humidity': 61, 'dew_point': 4.5, 'uvi': 1.62, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 271, 'wind_gust': 2.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 10.8, 'feels_like': 9.66, 'pressure': 1014, 'humidity': 66, 'dew_point': 4.71, 'uvi': 0.61, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 279, 'wind_gust': 2.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 9.35, 'feels_like': 8.57, 'pressure': 1015, 'humidity': 77, 'dew_point': 5.53, 'uvi': 0.06, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 276, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 6.42, 'feels_like': 6.42, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.37, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 284, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 47.000000 | 5.980000 | 6.720000 | 95.000000 | 1018.000000 |  | 6.720000 | 0.000000 | 2796.000000 | 320.000000 | 1.16 | 0.140000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 60.000000 | 5.600000 | 6.190000 | 96.000000 | 1019.000000 |  | 6.190000 | 0.000000 | 1161.000000 | 196.000000 | 1.21 | 0.250000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 52.000000 | 5.320000 | 5.910000 | 96.000000 | 1020.000000 |  | 5.910000 | 0.000000 | 2976.000000 | 187.000000 | 1.24 | 0.300000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 68.000000 | 4.480000 | 5.210000 | 95.000000 | 1020.000000 |  | 5.210000 | 0.000000 | 10000.000000 | 98.000000 | 1.1 | 0.340000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 76.000000 | 3.800000 | 4.680000 | 94.000000 | 1020.000000 |  | 4.680000 | 0.000000 | 10000.000000 | 103.000000 | 1.38 | 0.850000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 81.000000 | 3.460000 | 4.650000 | 92.000000 | 1020.000000 |  | 4.650000 | 0.000000 | 10000.000000 | 100.000000 | 1.17 | 0.290000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 48.000000 | 3.220000 | 4.100000 | 94.000000 | 1019.000000 |  | 4.100000 | 0.000000 | 10000.000000 | 106.000000 | 1.08 | 0.320000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 48.000000 | 2.840000 | 4.180000 | 91.000000 | 1018.000000 |  | 4.180000 | 0.000000 | 10000.000000 | 71.000000 | 1.26 | 0.400000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 49.000000 | 2.280000 | 3.770000 | 90.000000 | 1018.000000 |  | 3.770000 | 0.000000 | 10000.000000 | 280.000000 | 1.21 | 0.070000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 59.000000 | 1.850000 | 3.490000 | 89.000000 | 1018.000000 |  | 3.490000 | 0.000000 | 10000.000000 | 77.000000 | 1.39 | 0.030000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 67.000000 | 1.470000 | 3.430000 | 87.000000 | 1019.000000 |  | 3.430000 | 0.000000 | 10000.000000 | 73.000000 | 1.26 | 0.310000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 66.000000 | 1.390000 | 3.340000 | 87.000000 | 1019.000000 |  | 3.340000 | 0.000000 | 10000.000000 | 88.000000 | 1.27 | 0.280000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 41.000000 | 2.540000 | 5.010000 | 84.000000 | 1020.000000 |  | 5.010000 | 0.150000 | 10000.000000 | 239.000000 | 1.13 | 0.090000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 49.000000 | 3.510000 | 7.080000 | 78.000000 | 1020.000000 |  | 7.080000 | 1.160000 | 10000.000000 | 263.000000 | 0.9 | 0.930000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 74.000000 | 4.000000 | 8.130000 | 73.000000 | 1020.000000 |  | 8.560000 | 2.660000 | 10000.000000 | 260.000000 | 0.92 | 1.390000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 68.000000 | 3.830000 | 8.860000 | 65.000000 | 1019.000000 |  | 10.100000 | 4.370000 | 10000.000000 | 264.000000 | 1.64 | 2.240000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 64.000000 | 3.850000 | 10.330000 | 59.000000 | 1018.000000 |  | 11.580000 | 7.340000 | 10000.000000 | 267.000000 | 2.28 | 3.060000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 58.000000 | 4.140000 | 10.940000 | 58.000000 | 1017.000000 |  | 12.150000 | 7.810000 | 10000.000000 | 267.000000 | 2.5 | 3.350000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 99.000000 | 4.340000 | 11.170000 | 58.000000 | 1016.000000 |  | 12.360000 | 6.900000 | 10000.000000 | 268.000000 | 2.5 | 3.170000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 4.330000 | 11.160000 | 58.000000 | 1014.000000 |  | 12.350000 | 2.940000 | 10000.000000 | 270.000000 | 2.3 | 2.860000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 4.500000 | 10.600000 | 61.000000 | 1013.000000 |  | 11.770000 | 1.620000 | 10000.000000 | 271.000000 | 2.4 | 2.810000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 4.710000 | 9.660000 | 66.000000 | 1014.000000 |  | 10.800000 | 0.610000 | 10000.000000 | 279.000000 | 2.2 | 2.410000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 5.530000 | 8.570000 | 77.000000 | 1015.000000 |  | 9.350000 | 0.060000 | 10000.000000 | 276.000000 | 1.85 | 1.850000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035370 | "EL ESPINO - AUT [24035370]" | 6.506722 | -72.452667 | 3510.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-19 00:00:00 | NaT | Boyacá | El Espino | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 5.370000 | 6.420000 | 93.000000 | 1017.000000 |  | 6.420000 | 0.000000 | 10000.000000 | 284.000000 | 0.71 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station24035370_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035370_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035370_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035370_OWM_Windspeed_20220111.png)
