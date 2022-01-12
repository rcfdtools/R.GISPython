
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CAJAMARCA - AUT [21215190] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21215190_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.43566667,-75.50036111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.43566667&lon=-75.50036111)


| Parameter | Value |
|---|---|
| Code | 21215190 |
| Name | CAJAMARCA - AUT [21215190] |
| Latitude, ° | 4.43566667 |
| Longitude, ° | -75.50036111 |
| Elevation, m | 2530 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-10 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Cajamarca |
| Stream | Saldana |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Coello |

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

### (CNE index 82) Open Weather values for station 21215190 - CAJAMARCA - AUT [21215190]

JSON data from API OWM:

```
{'lat': 4.4357, 'lon': -75.5004, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813174, 'sunset': 1641855946, 'temp': 15.25, 'feels_like': 15.23, 'pressure': 1014, 'humidity': 92, 'dew_point': 13.96, 'uvi': 5.22, 'clouds': 75, 'visibility': 6409, 'wind_speed': 1.19, 'wind_deg': 282, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.19}}, 'hourly': [{'dt': 1641772800, 'temp': 14.95, 'feels_like': 15.06, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.64, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 314, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641776400, 'temp': 13.95, 'feels_like': 13.93, 'pressure': 1017, 'humidity': 97, 'dew_point': 13.48, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 309, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641780000, 'temp': 13.11, 'feels_like': 13.01, 'pressure': 1018, 'humidity': 97, 'dew_point': 12.64, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 318, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.28, 'feels_like': 12.1, 'pressure': 1018, 'humidity': 97, 'dew_point': 11.82, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 311, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641787200, 'temp': 12.27, 'feels_like': 12.11, 'pressure': 1018, 'humidity': 98, 'dew_point': 11.96, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 324, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 12.27, 'feels_like': 12.09, 'pressure': 1018, 'humidity': 97, 'dew_point': 11.81, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 33, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.06, 'feels_like': 12.98, 'pressure': 1017, 'humidity': 98, 'dew_point': 12.75, 'uvi': 0, 'clouds': 59, 'visibility': 8027, 'wind_speed': 0.47, 'wind_deg': 284, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 13.06, 'feels_like': 12.98, 'pressure': 1016, 'humidity': 98, 'dew_point': 12.75, 'uvi': 0, 'clouds': 94, 'visibility': 7411, 'wind_speed': 0.54, 'wind_deg': 284, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 12, 'feels_like': 11.81, 'pressure': 1016, 'humidity': 98, 'dew_point': 11.69, 'uvi': 0, 'clouds': 95, 'visibility': 5888, 'wind_speed': 0.89, 'wind_deg': 288, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.84, 'feels_like': 11.64, 'pressure': 1016, 'humidity': 98, 'dew_point': 11.53, 'uvi': 0, 'clouds': 95, 'visibility': 4842, 'wind_speed': 0.95, 'wind_deg': 296, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 12.06, 'feels_like': 11.88, 'pressure': 1017, 'humidity': 98, 'dew_point': 11.75, 'uvi': 0, 'clouds': 96, 'visibility': 4874, 'wind_speed': 1.1, 'wind_deg': 291, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641812400, 'temp': 11.09, 'feels_like': 10.81, 'pressure': 1018, 'humidity': 98, 'dew_point': 10.79, 'uvi': 0, 'clouds': 96, 'visibility': 4997, 'wind_speed': 1.15, 'wind_deg': 290, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 11.5, 'feels_like': 11.26, 'pressure': 1018, 'humidity': 98, 'dew_point': 11.2, 'uvi': 0.26, 'clouds': 74, 'visibility': 4762, 'wind_speed': 0.88, 'wind_deg': 290, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641819600, 'temp': 12.09, 'feels_like': 11.84, 'pressure': 1019, 'humidity': 95, 'dew_point': 11.31, 'uvi': 0.38, 'clouds': 99, 'visibility': 5745, 'wind_speed': 0.97, 'wind_deg': 276, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641823200, 'temp': 13.52, 'feels_like': 13.33, 'pressure': 1019, 'humidity': 92, 'dew_point': 12.25, 'uvi': 0.94, 'clouds': 99, 'visibility': 7353, 'wind_speed': 0.79, 'wind_deg': 272, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641826800, 'temp': 15.27, 'feels_like': 15.18, 'pressure': 1018, 'humidity': 89, 'dew_point': 13.47, 'uvi': 1.63, 'clouds': 99, 'visibility': 7197, 'wind_speed': 0.92, 'wind_deg': 289, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641830400, 'temp': 14.97, 'feels_like': 14.72, 'pressure': 1017, 'humidity': 84, 'dew_point': 12.29, 'uvi': 10.37, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 299, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641834000, 'temp': 15.85, 'feels_like': 15.68, 'pressure': 1016, 'humidity': 84, 'dew_point': 13.15, 'uvi': 11.5, 'clouds': 96, 'visibility': 5059, 'wind_speed': 0.78, 'wind_deg': 285, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}, {'dt': 1641837600, 'temp': 16.13, 'feels_like': 16.1, 'pressure': 1015, 'humidity': 88, 'dew_point': 14.14, 'uvi': 10.63, 'clouds': 65, 'visibility': 7093, 'wind_speed': 1.08, 'wind_deg': 290, 'wind_gust': 1.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.12}}, {'dt': 1641841200, 'temp': 16.42, 'feels_like': 16.47, 'pressure': 1014, 'humidity': 90, 'dew_point': 14.78, 'uvi': 8.73, 'clouds': 78, 'visibility': 6559, 'wind_speed': 1.06, 'wind_deg': 286, 'wind_gust': 1.63, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.17}}, {'dt': 1641844800, 'temp': 15.25, 'feels_like': 15.23, 'pressure': 1014, 'humidity': 92, 'dew_point': 13.96, 'uvi': 5.22, 'clouds': 75, 'visibility': 6409, 'wind_speed': 1.19, 'wind_deg': 282, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.19}}, {'dt': 1641848400, 'temp': 14.5, 'feels_like': 14.43, 'pressure': 1014, 'humidity': 93, 'dew_point': 13.38, 'uvi': 2.23, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 294, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641852000, 'temp': 12.95, 'feels_like': 12.78, 'pressure': 1015, 'humidity': 95, 'dew_point': 12.17, 'uvi': 0.36, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 295, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641855600, 'temp': 11.6, 'feels_like': 11.32, 'pressure': 1016, 'humidity': 96, 'dew_point': 10.98, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 310, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 00:00:00 | 80.000000 | 14.640000 | 15.060000 | 98.000000 | 1016.000000 | 0.23 | 14.950000 | 0.000000 | 10000.000000 | 314.000000 | 0.56 | 0.450000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 13.480000 | 13.930000 | 97.000000 | 1017.000000 | 0.17 | 13.950000 | 0.000000 | 10000.000000 | 309.000000 | 0.68 | 0.630000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 12.640000 | 13.010000 | 97.000000 | 1018.000000 |  | 13.110000 | 0.000000 | 10000.000000 | 318.000000 | 0.75 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 11.820000 | 12.100000 | 97.000000 | 1018.000000 | 0.13 | 12.280000 | 0.000000 | 10000.000000 | 311.000000 | 0.8 | 0.420000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 11.960000 | 12.110000 | 98.000000 | 1018.000000 |  | 12.270000 | 0.000000 | 10000.000000 | 324.000000 | 0.61 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 11.810000 | 12.090000 | 97.000000 | 1018.000000 |  | 12.270000 | 0.000000 | 10000.000000 | 33.000000 | 0.67 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 06:00:00 | 59.000000 | 12.750000 | 12.980000 | 98.000000 | 1017.000000 |  | 13.060000 | 0.000000 | 8027.000000 | 284.000000 | 0.83 | 0.470000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 07:00:00 | 94.000000 | 12.750000 | 12.980000 | 98.000000 | 1016.000000 |  | 13.060000 | 0.000000 | 7411.000000 | 284.000000 | 0.81 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 11.690000 | 11.810000 | 98.000000 | 1016.000000 |  | 12.000000 | 0.000000 | 5888.000000 | 288.000000 | 1.41 | 0.890000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 09:00:00 | 95.000000 | 11.530000 | 11.640000 | 98.000000 | 1016.000000 |  | 11.840000 | 0.000000 | 4842.000000 | 296.000000 | 1.65 | 0.950000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 10:00:00 | 96.000000 | 11.750000 | 11.880000 | 98.000000 | 1017.000000 | 0.11 | 12.060000 | 0.000000 | 4874.000000 | 291.000000 | 1.83 | 1.100000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 11:00:00 | 96.000000 | 10.790000 | 10.810000 | 98.000000 | 1018.000000 |  | 11.090000 | 0.000000 | 4997.000000 | 290.000000 | 2.1 | 1.150000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 12:00:00 | 74.000000 | 11.200000 | 11.260000 | 98.000000 | 1018.000000 | 0.11 | 11.500000 | 0.260000 | 4762.000000 | 290.000000 | 1.55 | 0.880000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 11.310000 | 11.840000 | 95.000000 | 1019.000000 | 0.2 | 12.090000 | 0.380000 | 5745.000000 | 276.000000 | 1.63 | 0.970000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 12.250000 | 13.330000 | 92.000000 | 1019.000000 | 0.25 | 13.520000 | 0.940000 | 7353.000000 | 272.000000 | 1.33 | 0.790000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 13.470000 | 15.180000 | 89.000000 | 1018.000000 | 0.44 | 15.270000 | 1.630000 | 7197.000000 | 289.000000 | 1.59 | 0.920000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 12.290000 | 14.720000 | 84.000000 | 1017.000000 | 0.38 | 14.970000 | 10.370000 | 10000.000000 | 299.000000 | 1.23 | 0.670000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 17:00:00 | 96.000000 | 13.150000 | 15.680000 | 84.000000 | 1016.000000 | 0.75 | 15.850000 | 11.500000 | 5059.000000 | 285.000000 | 1.4 | 0.780000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 18:00:00 | 65.000000 | 14.140000 | 16.100000 | 88.000000 | 1015.000000 | 1.12 | 16.130000 | 10.630000 | 7093.000000 | 290.000000 | 1.7 | 1.080000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 19:00:00 | 78.000000 | 14.780000 | 16.470000 | 90.000000 | 1014.000000 | 1.17 | 16.420000 | 8.730000 | 6559.000000 | 286.000000 | 1.63 | 1.060000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 13.960000 | 15.230000 | 92.000000 | 1014.000000 | 1.19 | 15.250000 | 5.220000 | 6409.000000 | 282.000000 | 1.86 | 1.190000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 21:00:00 | 77.000000 | 13.380000 | 14.430000 | 93.000000 | 1014.000000 | 1.01 | 14.500000 | 2.230000 | 10000.000000 | 294.000000 | 1.6 | 1.030000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 22:00:00 | 82.000000 | 12.170000 | 12.780000 | 95.000000 | 1015.000000 | 0.63 | 12.950000 | 0.360000 | 10000.000000 | 295.000000 | 1.88 | 1.160000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215190 | "CAJAMARCA - AUT [21215190]" | 4.435667 | -75.500361 | 2530.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Tolima | Cajamarca | Saldana | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 10.980000 | 11.320000 | 96.000000 | 1016.000000 | 0.56 | 11.600000 | 0.000000 | 10000.000000 | 310.000000 | 1.25 | 0.920000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21215190_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21215190_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21215190_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215190_OWM_Windspeed_20220111.png)
