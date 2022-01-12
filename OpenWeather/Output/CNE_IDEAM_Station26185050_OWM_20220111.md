
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SANTA BARBARA - AUT [26185050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26185050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.85958333,-75.55627778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.85958333&lon=-75.55627778)


| Parameter | Value |
|---|---|
| Code | 26185050 |
| Name | SANTA BARBARA - AUT [26185050] |
| Latitude, ° | 5.85958333 |
| Longitude, ° | -75.55627778 |
| Elevation, m | 1680 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-11-29 19:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Santa Bárbara (Antioquia) |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Arma |

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

### (CNE index 156) Open Weather values for station 26185050 - SANTA BARBARA - AUT [26185050]

JSON data from API OWM:

```
{'lat': 5.8596, 'lon': -75.5563, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813325, 'sunset': 1641855821, 'temp': 23.12, 'feels_like': 23.45, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.45, 'uvi': 4.44, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 230, 'wind_gust': 1.14, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.4}}, 'hourly': [{'dt': 1641772800, 'temp': 19.86, 'feels_like': 20.38, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.04, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 70, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641776400, 'temp': 19.3, 'feels_like': 19.79, 'pressure': 1015, 'humidity': 96, 'dew_point': 18.65, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 72, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641780000, 'temp': 19.3, 'feels_like': 19.79, 'pressure': 1016, 'humidity': 96, 'dew_point': 18.65, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 68, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641783600, 'temp': 18.92, 'feels_like': 19.4, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.43, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 74, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641787200, 'temp': 18.92, 'feels_like': 19.4, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.43, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 80, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 17.63, 'feels_like': 17.98, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.15, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 99, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 17.63, 'feels_like': 17.98, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.15, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 85, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641798000, 'temp': 17.63, 'feels_like': 18.01, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.31, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 39, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641801600, 'temp': 17.08, 'feels_like': 17.4, 'pressure': 1013, 'humidity': 98, 'dew_point': 16.76, 'uvi': 0, 'clouds': 99, 'visibility': 8968, 'wind_speed': 0.14, 'wind_deg': 99, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641805200, 'temp': 17.08, 'feels_like': 17.43, 'pressure': 1014, 'humidity': 99, 'dew_point': 16.92, 'uvi': 0, 'clouds': 99, 'visibility': 5971, 'wind_speed': 0.06, 'wind_deg': 50, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.72}}, {'dt': 1641808800, 'temp': 17.08, 'feels_like': 17.43, 'pressure': 1015, 'humidity': 99, 'dew_point': 16.92, 'uvi': 0, 'clouds': 98, 'visibility': 5790, 'wind_speed': 0.02, 'wind_deg': 228, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.95}}, {'dt': 1641812400, 'temp': 17.39, 'feels_like': 17.77, 'pressure': 1015, 'humidity': 99, 'dew_point': 17.23, 'uvi': 0, 'clouds': 98, 'visibility': 7123, 'wind_speed': 0.16, 'wind_deg': 165, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641816000, 'temp': 17.64, 'feels_like': 18.02, 'pressure': 1016, 'humidity': 98, 'dew_point': 17.32, 'uvi': 0.2, 'clouds': 81, 'visibility': 8367, 'wind_speed': 0.19, 'wind_deg': 119, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641819600, 'temp': 18.1, 'feels_like': 18.47, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.45, 'uvi': 1.19, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 100, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641823200, 'temp': 19.53, 'feels_like': 19.89, 'pressure': 1017, 'humidity': 90, 'dew_point': 17.85, 'uvi': 3.02, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 176, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641826800, 'temp': 19.65, 'feels_like': 19.89, 'pressure': 1017, 'humidity': 85, 'dew_point': 17.06, 'uvi': 5.28, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 216, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641830400, 'temp': 20.11, 'feels_like': 20.29, 'pressure': 1016, 'humidity': 81, 'dew_point': 16.75, 'uvi': 6.88, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 237, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641834000, 'temp': 19.58, 'feels_like': 19.42, 'pressure': 1014, 'humidity': 70, 'dew_point': 13.97, 'uvi': 7.65, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 260, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641837600, 'temp': 20.33, 'feels_like': 20.17, 'pressure': 1013, 'humidity': 67, 'dew_point': 14.01, 'uvi': 7.06, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 255, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641841200, 'temp': 22.74, 'feels_like': 22.95, 'pressure': 1011, 'humidity': 72, 'dew_point': 17.43, 'uvi': 7.46, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 255, 'wind_gust': 1.24, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641844800, 'temp': 23.12, 'feels_like': 23.45, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.45, 'uvi': 4.44, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 230, 'wind_gust': 1.14, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.4}}, {'dt': 1641848400, 'temp': 22.39, 'feels_like': 22.93, 'pressure': 1011, 'humidity': 86, 'dew_point': 19.93, 'uvi': 1.86, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 205, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641852000, 'temp': 21.49, 'feels_like': 22.12, 'pressure': 1012, 'humidity': 93, 'dew_point': 20.31, 'uvi': 0.37, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 201, 'wind_gust': 0.69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641855600, 'temp': 20.38, 'feels_like': 20.95, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.55, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 74, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 00:00:00 | 86.000000 | 19.040000 | 20.380000 | 95.000000 | 1014.000000 | 0.43 | 19.860000 | 0.000000 | 10000.000000 | 70.000000 | 1.81 | 1.110000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 01:00:00 | 92.000000 | 18.650000 | 19.790000 | 96.000000 | 1015.000000 | 0.15 | 19.300000 | 0.000000 | 10000.000000 | 72.000000 | 1.81 | 0.980000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 02:00:00 | 95.000000 | 18.650000 | 19.790000 | 96.000000 | 1016.000000 | 0.21 | 19.300000 | 0.000000 | 10000.000000 | 68.000000 | 1.18 | 0.790000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 18.430000 | 19.400000 | 97.000000 | 1016.000000 | 0.1 | 18.920000 | 0.000000 | 10000.000000 | 74.000000 | 0.91 | 0.650000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 04:00:00 | 92.000000 | 18.430000 | 19.400000 | 97.000000 | 1016.000000 |  | 18.920000 | 0.000000 | 10000.000000 | 80.000000 | 0.61 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 05:00:00 | 92.000000 | 17.150000 | 17.980000 | 97.000000 | 1015.000000 |  | 17.630000 | 0.000000 | 10000.000000 | 99.000000 | 0.51 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 06:00:00 | 79.000000 | 17.150000 | 17.980000 | 97.000000 | 1015.000000 | 0.18 | 17.630000 | 0.000000 | 10000.000000 | 85.000000 | 0.41 | 0.150000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 17.310000 | 18.010000 | 98.000000 | 1014.000000 | 0.43 | 17.630000 | 0.000000 | 10000.000000 | 39.000000 | 0.41 | 0.120000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 16.760000 | 17.400000 | 98.000000 | 1013.000000 | 0.53 | 17.080000 | 0.000000 | 8968.000000 | 99.000000 | 0.56 | 0.140000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 16.920000 | 17.430000 | 99.000000 | 1014.000000 | 0.72 | 17.080000 | 0.000000 | 5971.000000 | 50.000000 | 0.68 | 0.060000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 16.920000 | 17.430000 | 99.000000 | 1015.000000 | 0.95 | 17.080000 | 0.000000 | 5790.000000 | 228.000000 | 0.77 | 0.020000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 17.230000 | 17.770000 | 99.000000 | 1015.000000 | 0.64 | 17.390000 | 0.000000 | 7123.000000 | 165.000000 | 0.82 | 0.160000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 12:00:00 | 81.000000 | 17.320000 | 18.020000 | 98.000000 | 1016.000000 | 0.24 | 17.640000 | 0.200000 | 8367.000000 | 119.000000 | 0.57 | 0.190000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 17.450000 | 18.470000 | 96.000000 | 1017.000000 | 0.26 | 18.100000 | 1.190000 | 10000.000000 | 100.000000 | 0.68 | 0.260000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 14:00:00 | 86.000000 | 17.850000 | 19.890000 | 90.000000 | 1017.000000 | 0.16 | 19.530000 | 3.020000 | 10000.000000 | 176.000000 | 0.62 | 0.350000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 17.060000 | 19.890000 | 85.000000 | 1017.000000 | 0.28 | 19.650000 | 5.280000 | 10000.000000 | 216.000000 | 0.86 | 0.640000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 16.750000 | 20.290000 | 81.000000 | 1016.000000 | 0.35 | 20.110000 | 6.880000 | 10000.000000 | 237.000000 | 0.8 | 0.790000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | 13.970000 | 19.420000 | 70.000000 | 1014.000000 | 0.31 | 19.580000 | 7.650000 | 10000.000000 | 260.000000 | 0.87 | 0.990000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 18:00:00 | 33.000000 | 14.010000 | 20.170000 | 67.000000 | 1013.000000 | 0.45 | 20.330000 | 7.060000 | 10000.000000 | 255.000000 | 1.13 | 1.150000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 19:00:00 | 54.000000 | 17.430000 | 22.950000 | 72.000000 | 1011.000000 | 1.09 | 22.740000 | 7.460000 | 10000.000000 | 255.000000 | 1.24 | 0.970000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 20:00:00 | 56.000000 | 18.450000 | 23.450000 | 75.000000 | 1011.000000 | 1.4 | 23.120000 | 4.440000 | 10000.000000 | 230.000000 | 1.14 | 0.720000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 21:00:00 | 70.000000 | 19.930000 | 22.930000 | 86.000000 | 1011.000000 | 1.25 | 22.390000 | 1.860000 | 10000.000000 | 205.000000 | 1.26 | 0.660000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 22:00:00 | 78.000000 | 20.310000 | 22.120000 | 93.000000 | 1012.000000 | 1.15 | 21.490000 | 0.370000 | 10000.000000 | 201.000000 | 0.69 | 0.410000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26185050 | "SANTA BARBARA - AUT [26185050]" | 5.859583 | -75.556278 | 1680.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-29 19:00:00 | NaT | Antioquia | Santa Bárbara (Antioquia) | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Arma | America/Bogota | 2022-01-10 23:00:00 | 82.000000 | 19.550000 | 20.950000 | 95.000000 | 1013.000000 | 0.65 | 20.380000 | 0.000000 | 10000.000000 | 74.000000 | 0.69 | 0.420000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26185050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26185050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26185050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26185050_OWM_Windspeed_20220111.png)
