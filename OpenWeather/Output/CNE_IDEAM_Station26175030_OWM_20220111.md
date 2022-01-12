
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NACIONAL GRANJA LA [26175030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26175030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.71733333,-75.69091667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.71733333&lon=-75.69091667)


| Parameter | Value |
|---|---|
| Code | 26175030 |
| Name | NACIONAL GRANJA LA [26175030] |
| Latitude, ° | 5.71733333 |
| Longitude, ° | -75.69091667 |
| Elevation, m | 1153 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1977-07-15 00:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Támesis |
| Stream | Mongui |
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

### (CNE index 1610) Open Weather values for station 26175030 - NACIONAL GRANJA LA [26175030]

JSON data from API OWM:

```
{'lat': 5.7173, 'lon': -75.6909, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813344, 'sunset': 1641855867, 'temp': 26.38, 'feels_like': 26.38, 'pressure': 1010, 'humidity': 73, 'dew_point': 21.15, 'uvi': 4.44, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 222, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.43}}, 'hourly': [{'dt': 1641772800, 'temp': 23.05, 'feels_like': 23.87, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.03, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 214, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641776400, 'temp': 22.48, 'feels_like': 23.26, 'pressure': 1014, 'humidity': 95, 'dew_point': 21.64, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 210, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641780000, 'temp': 22.48, 'feels_like': 23.29, 'pressure': 1015, 'humidity': 96, 'dew_point': 21.81, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 213, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 22.16, 'feels_like': 22.94, 'pressure': 1016, 'humidity': 96, 'dew_point': 21.49, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 214, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.16, 'feels_like': 22.94, 'pressure': 1015, 'humidity': 96, 'dew_point': 21.49, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 211, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.82, 'feels_like': 21.46, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.16, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 213, 'wind_gust': 0.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.82, 'feels_like': 21.46, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.16, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 226, 'wind_gust': 0.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.82, 'feels_like': 21.46, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.16, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 261, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641801600, 'temp': 20.26, 'feels_like': 20.87, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.77, 'uvi': 0, 'clouds': 99, 'visibility': 8374, 'wind_speed': 0.23, 'wind_deg': 230, 'wind_gust': 0.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641805200, 'temp': 20.26, 'feels_like': 20.87, 'pressure': 1014, 'humidity': 97, 'dew_point': 19.77, 'uvi': 0, 'clouds': 99, 'visibility': 4019, 'wind_speed': 0.14, 'wind_deg': 250, 'wind_gust': 0.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 20.26, 'feels_like': 20.9, 'pressure': 1014, 'humidity': 98, 'dew_point': 19.93, 'uvi': 0, 'clouds': 99, 'visibility': 3933, 'wind_speed': 0.14, 'wind_deg': 215, 'wind_gust': 0.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641812400, 'temp': 20.58, 'feels_like': 21.25, 'pressure': 1015, 'humidity': 98, 'dew_point': 20.25, 'uvi': 0, 'clouds': 99, 'visibility': 5516, 'wind_speed': 0.23, 'wind_deg': 203, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641816000, 'temp': 20.82, 'feels_like': 21.49, 'pressure': 1016, 'humidity': 97, 'dew_point': 20.33, 'uvi': 0.2, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 139, 'wind_gust': 0.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 21.3, 'feels_like': 21.94, 'pressure': 1017, 'humidity': 94, 'dew_point': 20.29, 'uvi': 1.19, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 71, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641823200, 'temp': 22.73, 'feels_like': 23.36, 'pressure': 1017, 'humidity': 88, 'dew_point': 20.64, 'uvi': 3.02, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 87, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641826800, 'temp': 22.81, 'feels_like': 23.37, 'pressure': 1017, 'humidity': 85, 'dew_point': 20.16, 'uvi': 5.28, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 90, 'wind_gust': 0.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641830400, 'temp': 23.27, 'feels_like': 23.77, 'pressure': 1015, 'humidity': 81, 'dew_point': 19.83, 'uvi': 6.88, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 80, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641834000, 'temp': 22.72, 'feels_like': 22.88, 'pressure': 1014, 'humidity': 70, 'dew_point': 16.97, 'uvi': 7.65, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 302, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641837600, 'temp': 23.6, 'feels_like': 23.79, 'pressure': 1012, 'humidity': 68, 'dew_point': 17.35, 'uvi': 7.06, 'clouds': 19, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 260, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.69}}, {'dt': 1641841200, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 69, 'dew_point': 19.92, 'uvi': 7.46, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 245, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641844800, 'temp': 26.38, 'feels_like': 26.38, 'pressure': 1010, 'humidity': 73, 'dew_point': 21.15, 'uvi': 4.44, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 222, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.43}}, {'dt': 1641848400, 'temp': 25.59, 'feels_like': 26.45, 'pressure': 1010, 'humidity': 86, 'dew_point': 23.07, 'uvi': 1.86, 'clouds': 71, 'visibility': 8338, 'wind_speed': 1.06, 'wind_deg': 207, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641852000, 'temp': 24.71, 'feels_like': 25.64, 'pressure': 1012, 'humidity': 92, 'dew_point': 23.32, 'uvi': 0.37, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 212, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1641855600, 'temp': 23.59, 'feels_like': 24.49, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.74, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 220, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 00:00:00 | 70.000000 | 22.030000 | 23.870000 | 94.000000 | 1013.000000 | 0.31 | 23.050000 | 0.000000 | 10000.000000 | 214.000000 | 1.73 | 1.050000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 01:00:00 | 74.000000 | 21.640000 | 23.260000 | 95.000000 | 1014.000000 | 0.11 | 22.480000 | 0.000000 | 10000.000000 | 210.000000 | 1.5 | 0.920000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 02:00:00 | 87.000000 | 21.810000 | 23.290000 | 96.000000 | 1015.000000 | 0.15 | 22.480000 | 0.000000 | 10000.000000 | 213.000000 | 1.02 | 0.800000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 03:00:00 | 88.000000 | 21.490000 | 22.940000 | 96.000000 | 1016.000000 |  | 22.160000 | 0.000000 | 10000.000000 | 214.000000 | 0.92 | 0.740000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 04:00:00 | 89.000000 | 21.490000 | 22.940000 | 96.000000 | 1015.000000 |  | 22.160000 | 0.000000 | 10000.000000 | 211.000000 | 0.65 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 05:00:00 | 90.000000 | 20.160000 | 21.460000 | 96.000000 | 1015.000000 |  | 20.820000 | 0.000000 | 10000.000000 | 213.000000 | 0.55 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 06:00:00 | 78.000000 | 20.160000 | 21.460000 | 96.000000 | 1014.000000 |  | 20.820000 | 0.000000 | 10000.000000 | 226.000000 | 0.41 | 0.410000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 20.160000 | 21.460000 | 96.000000 | 1014.000000 | 0.22 | 20.820000 | 0.000000 | 10000.000000 | 261.000000 | 0.41 | 0.150000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 19.770000 | 20.870000 | 97.000000 | 1013.000000 | 0.18 | 20.260000 | 0.000000 | 8374.000000 | 230.000000 | 0.51 | 0.230000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 19.770000 | 20.870000 | 97.000000 | 1014.000000 | 0.18 | 20.260000 | 0.000000 | 4019.000000 | 250.000000 | 0.5 | 0.140000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 19.930000 | 20.900000 | 98.000000 | 1014.000000 | 0.3 | 20.260000 | 0.000000 | 3933.000000 | 215.000000 | 0.46 | 0.140000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 20.250000 | 21.250000 | 98.000000 | 1015.000000 | 0.18 | 20.580000 | 0.000000 | 5516.000000 | 203.000000 | 0.54 | 0.230000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 12:00:00 | 74.000000 | 20.330000 | 21.490000 | 97.000000 | 1016.000000 |  | 20.820000 | 0.200000 | 10000.000000 | 139.000000 | 0.43 | 0.080000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 20.290000 | 21.940000 | 94.000000 | 1017.000000 | 0.16 | 21.300000 | 1.190000 | 10000.000000 | 71.000000 | 0.63 | 0.290000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 14:00:00 | 91.000000 | 20.640000 | 23.360000 | 88.000000 | 1017.000000 | 0.25 | 22.730000 | 3.020000 | 10000.000000 | 87.000000 | 0.77 | 0.370000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 15:00:00 | 81.000000 | 20.160000 | 23.370000 | 85.000000 | 1017.000000 | 0.41 | 22.810000 | 5.280000 | 10000.000000 | 90.000000 | 0.95 | 0.420000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 16:00:00 | 76.000000 | 19.830000 | 23.770000 | 81.000000 | 1015.000000 | 0.41 | 23.270000 | 6.880000 | 10000.000000 | 80.000000 | 0.77 | 0.190000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 17:00:00 | 71.000000 | 16.970000 | 22.880000 | 70.000000 | 1014.000000 | 0.46 | 22.720000 | 7.650000 | 10000.000000 | 302.000000 | 0.86 | 0.280000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 18:00:00 | 19.000000 | 17.350000 | 23.790000 | 68.000000 | 1012.000000 | 0.69 | 23.600000 | 7.060000 | 10000.000000 | 260.000000 | 1.05 | 0.580000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 19:00:00 | 36.000000 | 19.920000 | 26.050000 | 69.000000 | 1011.000000 | 1.13 | 26.050000 | 7.460000 | 10000.000000 | 245.000000 | 1.36 | 0.940000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 20:00:00 | 57.000000 | 21.150000 | 26.380000 | 73.000000 | 1010.000000 | 1.43 | 26.380000 | 4.440000 | 10000.000000 | 222.000000 | 1.36 | 1.060000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 21:00:00 | 71.000000 | 23.070000 | 26.450000 | 86.000000 | 1010.000000 | 0.96 | 25.590000 | 1.860000 | 8338.000000 | 207.000000 | 1.67 | 1.060000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 22:00:00 | 78.000000 | 23.320000 | 25.640000 | 92.000000 | 1012.000000 | 1 | 24.710000 | 0.370000 | 10000.000000 | 212.000000 | 1.23 | 0.960000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26175030 | "NACIONAL GRANJA LA [26175030]" | 5.717333 | -75.690917 | 1153.000000 | Climática Principal | Convencional | Activa | 1977-07-15 00:00:00 | NaT | Antioquia | Támesis | Mongui | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Río Frío y Otros Directos al Cauca | America/Bogota | 2022-01-10 23:00:00 | 83.000000 | 22.740000 | 24.490000 | 95.000000 | 1013.000000 | 0.51 | 23.590000 | 0.000000 | 10000.000000 | 220.000000 | 1.08 | 0.740000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26175030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26175030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26175030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26175030_OWM_Windspeed_20220111.png)
