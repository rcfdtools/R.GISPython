
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ARRAYANALES - AUT [26015040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26015040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.44804111,-76.43574694) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.44804111&lon=-76.43574694)


| Parameter | Value |
|---|---|
| Code | 26015040 |
| Name | ARRAYANALES - AUT [26015040] |
| Latitude, ° | 2.44804111 |
| Longitude, ° | -76.43574694 |
| Elevation, m | 2552 |
| Category | Climática Principal |
| Technology | Automática sin Telemetría |
| Status | Activa |
| Installation date | 2010-05-24 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Popayán |
| Stream | Piedras |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Alto Río Cauca |

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

### (CNE index 1098) Open Weather values for station 26015040 - ARRAYANALES - AUT [26015040]

JSON data from API OWM:

```
{'lat': 2.448, 'lon': -76.4357, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813206, 'sunset': 1641856363, 'temp': 13.38, 'feels_like': 13.23, 'pressure': 1014, 'humidity': 94, 'dew_point': 12.43, 'uvi': 3.92, 'clouds': 100, 'visibility': 4683, 'wind_speed': 1.34, 'wind_deg': 283, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, 'hourly': [{'dt': 1641772800, 'temp': 11.26, 'feels_like': 11.03, 'pressure': 1016, 'humidity': 99, 'dew_point': 11.11, 'uvi': 0, 'clouds': 100, 'visibility': 2555, 'wind_speed': 0.14, 'wind_deg': 164, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.52}}, {'dt': 1641776400, 'temp': 11.15, 'feels_like': 10.88, 'pressure': 1018, 'humidity': 98, 'dew_point': 10.85, 'uvi': 0, 'clouds': 100, 'visibility': 4044, 'wind_speed': 0.18, 'wind_deg': 200, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.44}}, {'dt': 1641780000, 'temp': 11.2, 'feels_like': 10.93, 'pressure': 1019, 'humidity': 98, 'dew_point': 10.9, 'uvi': 0, 'clouds': 97, 'visibility': 3474, 'wind_speed': 0.08, 'wind_deg': 130, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 11.2, 'feels_like': 10.93, 'pressure': 1019, 'humidity': 98, 'dew_point': 10.9, 'uvi': 0, 'clouds': 96, 'visibility': 3240, 'wind_speed': 0.19, 'wind_deg': 166, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 11.2, 'feels_like': 10.96, 'pressure': 1019, 'humidity': 99, 'dew_point': 11.05, 'uvi': 0, 'clouds': 97, 'visibility': 3448, 'wind_speed': 0.37, 'wind_deg': 208, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641790800, 'temp': 11.2, 'feels_like': 10.93, 'pressure': 1018, 'humidity': 98, 'dew_point': 10.9, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 143, 'wind_gust': 0.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 11.09, 'feels_like': 10.81, 'pressure': 1017, 'humidity': 98, 'dew_point': 10.79, 'uvi': 0, 'clouds': 89, 'visibility': 2935, 'wind_speed': 0.24, 'wind_deg': 220, 'wind_gust': 0.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641798000, 'temp': 10.93, 'feels_like': 10.66, 'pressure': 1017, 'humidity': 99, 'dew_point': 10.78, 'uvi': 0, 'clouds': 100, 'visibility': 8120, 'wind_speed': 0.42, 'wind_deg': 250, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641801600, 'temp': 10.76, 'feels_like': 10.48, 'pressure': 1016, 'humidity': 99, 'dew_point': 10.61, 'uvi': 0, 'clouds': 100, 'visibility': 3022, 'wind_speed': 0.44, 'wind_deg': 248, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641805200, 'temp': 10.77, 'feels_like': 10.49, 'pressure': 1016, 'humidity': 99, 'dew_point': 10.62, 'uvi': 0, 'clouds': 100, 'visibility': 2931, 'wind_speed': 0.45, 'wind_deg': 264, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641808800, 'temp': 10.7, 'feels_like': 10.41, 'pressure': 1017, 'humidity': 99, 'dew_point': 10.55, 'uvi': 0, 'clouds': 100, 'visibility': 3092, 'wind_speed': 0.62, 'wind_deg': 291, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641812400, 'temp': 10.65, 'feels_like': 10.38, 'pressure': 1017, 'humidity': 100, 'dew_point': 10.65, 'uvi': 0, 'clouds': 100, 'visibility': 2465, 'wind_speed': 0.73, 'wind_deg': 286, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641816000, 'temp': 11.21, 'feels_like': 10.97, 'pressure': 1018, 'humidity': 99, 'dew_point': 11.06, 'uvi': 0.26, 'clouds': 99, 'visibility': 1288, 'wind_speed': 0.59, 'wind_deg': 294, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641819600, 'temp': 11.99, 'feels_like': 11.78, 'pressure': 1019, 'humidity': 97, 'dew_point': 11.53, 'uvi': 1.55, 'clouds': 100, 'visibility': 1101, 'wind_speed': 0.59, 'wind_deg': 306, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641823200, 'temp': 13.07, 'feels_like': 12.83, 'pressure': 1019, 'humidity': 92, 'dew_point': 11.8, 'uvi': 3.88, 'clouds': 100, 'visibility': 5755, 'wind_speed': 0.78, 'wind_deg': 294, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641826800, 'temp': 13.92, 'feels_like': 13.72, 'pressure': 1019, 'humidity': 90, 'dew_point': 12.31, 'uvi': 6.73, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 290, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641830400, 'temp': 14.82, 'feels_like': 14.66, 'pressure': 1017, 'humidity': 88, 'dew_point': 12.85, 'uvi': 11.64, 'clouds': 100, 'visibility': 9726, 'wind_speed': 1.38, 'wind_deg': 302, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641834000, 'temp': 14.85, 'feels_like': 14.71, 'pressure': 1017, 'humidity': 89, 'dew_point': 13.06, 'uvi': 12.98, 'clouds': 100, 'visibility': 7623, 'wind_speed': 1.57, 'wind_deg': 291, 'wind_gust': 1.58, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641837600, 'temp': 14.72, 'feels_like': 14.6, 'pressure': 1016, 'humidity': 90, 'dew_point': 13.1, 'uvi': 12.07, 'clouds': 94, 'visibility': 6385, 'wind_speed': 1.43, 'wind_deg': 286, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.39}}, {'dt': 1641841200, 'temp': 14.13, 'feels_like': 14, 'pressure': 1015, 'humidity': 92, 'dew_point': 12.85, 'uvi': 6.43, 'clouds': 99, 'visibility': 7235, 'wind_speed': 1.4, 'wind_deg': 283, 'wind_gust': 1.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.39}}, {'dt': 1641844800, 'temp': 13.38, 'feels_like': 13.23, 'pressure': 1014, 'humidity': 94, 'dew_point': 12.43, 'uvi': 3.92, 'clouds': 100, 'visibility': 4683, 'wind_speed': 1.34, 'wind_deg': 283, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, {'dt': 1641848400, 'temp': 13.03, 'feels_like': 12.9, 'pressure': 1014, 'humidity': 96, 'dew_point': 12.41, 'uvi': 1.72, 'clouds': 100, 'visibility': 1176, 'wind_speed': 1.21, 'wind_deg': 264, 'wind_gust': 1.77, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.32}}, {'dt': 1641852000, 'temp': 12.52, 'feels_like': 12.39, 'pressure': 1015, 'humidity': 98, 'dew_point': 12.21, 'uvi': 0.54, 'clouds': 99, 'visibility': 1838, 'wind_speed': 1, 'wind_deg': 261, 'wind_gust': 1.9, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641855600, 'temp': 11.67, 'feels_like': 11.48, 'pressure': 1016, 'humidity': 99, 'dew_point': 11.52, 'uvi': 0, 'clouds': 94, 'visibility': 2261, 'wind_speed': 0.71, 'wind_deg': 261, 'wind_gust': 1.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 11.110000 | 11.030000 | 99.000000 | 1016.000000 | 0.52 | 11.260000 | 0.000000 | 2555.000000 | 164.000000 | 0.91 | 0.140000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 10.850000 | 10.880000 | 98.000000 | 1018.000000 | 0.44 | 11.150000 | 0.000000 | 4044.000000 | 200.000000 | 0.85 | 0.180000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 02:00:00 | 97.000000 | 10.900000 | 10.930000 | 98.000000 | 1019.000000 | 0.12 | 11.200000 | 0.000000 | 3474.000000 | 130.000000 | 0.82 | 0.080000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 10.900000 | 10.930000 | 98.000000 | 1019.000000 | 0.12 | 11.200000 | 0.000000 | 3240.000000 | 166.000000 | 0.74 | 0.190000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 11.050000 | 10.960000 | 99.000000 | 1019.000000 | 0.17 | 11.200000 | 0.000000 | 3448.000000 | 208.000000 | 0.69 | 0.370000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 05:00:00 | 98.000000 | 10.900000 | 10.930000 | 98.000000 | 1018.000000 |  | 11.200000 | 0.000000 | 10000.000000 | 143.000000 | 0.55 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 10.790000 | 10.810000 | 98.000000 | 1017.000000 | 0.11 | 11.090000 | 0.000000 | 2935.000000 | 220.000000 | 0.42 | 0.240000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 10.780000 | 10.660000 | 99.000000 | 1017.000000 | 0.18 | 10.930000 | 0.000000 | 8120.000000 | 250.000000 | 0.7 | 0.420000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 10.610000 | 10.480000 | 99.000000 | 1016.000000 | 0.22 | 10.760000 | 0.000000 | 3022.000000 | 248.000000 | 0.92 | 0.440000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 10.620000 | 10.490000 | 99.000000 | 1016.000000 | 0.19 | 10.770000 | 0.000000 | 2931.000000 | 264.000000 | 0.87 | 0.450000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 10.550000 | 10.410000 | 99.000000 | 1017.000000 | 0.29 | 10.700000 | 0.000000 | 3092.000000 | 291.000000 | 1.07 | 0.620000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 10.650000 | 10.380000 | 100.000000 | 1017.000000 | 0.17 | 10.650000 | 0.000000 | 2465.000000 | 286.000000 | 1.39 | 0.730000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 11.060000 | 10.970000 | 99.000000 | 1018.000000 | 0.26 | 11.210000 | 0.260000 | 1288.000000 | 294.000000 | 1.11 | 0.590000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 11.530000 | 11.780000 | 97.000000 | 1019.000000 | 0.19 | 11.990000 | 1.550000 | 1101.000000 | 306.000000 | 0.87 | 0.590000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 11.800000 | 12.830000 | 92.000000 | 1019.000000 | 0.37 | 13.070000 | 3.880000 | 5755.000000 | 294.000000 | 1.11 | 0.780000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 12.310000 | 13.720000 | 90.000000 | 1019.000000 | 0.7 | 13.920000 | 6.730000 | 10000.000000 | 290.000000 | 1.63 | 1.340000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 12.850000 | 14.660000 | 88.000000 | 1017.000000 | 0.92 | 14.820000 | 11.640000 | 9726.000000 | 302.000000 | 1.42 | 1.380000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 13.060000 | 14.710000 | 89.000000 | 1017.000000 | 1.23 | 14.850000 | 12.980000 | 7623.000000 | 291.000000 | 1.58 | 1.570000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 18:00:00 | 94.000000 | 13.100000 | 14.600000 | 90.000000 | 1016.000000 | 1.39 | 14.720000 | 12.070000 | 6385.000000 | 286.000000 | 1.45 | 1.430000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 12.850000 | 14.000000 | 92.000000 | 1015.000000 | 1.39 | 14.130000 | 6.430000 | 7235.000000 | 283.000000 | 1.7 | 1.400000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 12.430000 | 13.230000 | 94.000000 | 1014.000000 | 1.26 | 13.380000 | 3.920000 | 4683.000000 | 283.000000 | 1.75 | 1.340000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 12.410000 | 12.900000 | 96.000000 | 1014.000000 | 1.32 | 13.030000 | 1.720000 | 1176.000000 | 264.000000 | 1.77 | 1.210000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 12.210000 | 12.390000 | 98.000000 | 1015.000000 | 1.01 | 12.520000 | 0.540000 | 1838.000000 | 261.000000 | 1.9 | 1.000000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015040 | "ARRAYANALES - AUT [26015040]" | 2.448041 | -76.435747 | 2552.000000 | Climática Principal | Automática sin Telemetría | Activa | 2010-05-24 00:00:00 | NaT | Cauca | Popayán | Piedras | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 11.520000 | 11.480000 | 99.000000 | 1016.000000 | 0.77 | 11.670000 | 0.000000 | 2261.000000 | 261.000000 | 1.41 | 0.710000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26015040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26015040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26015040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015040_OWM_Windspeed_20220111.png)
