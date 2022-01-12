
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LLORO [11035010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station11035010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.51,-76.58) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.51&lon=-76.58)


| Parameter | Value |
|---|---|
| Code | 11035010 |
| Name | LLORO [11035010] |
| Latitude, ° | 5.51 |
| Longitude, ° | -76.58 |
| Elevation, m | 41 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2018-04-18 00:00:00 |
| Suspension date | NaT |
| State | Chocó |
| County | Lloró |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Atrato - Darién |
| SZH - Hydrographic subzone | Río Quito |

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

### (CNE index 4397) Open Weather values for station 11035010 - LLORO [11035010]

JSON data from API OWM:

```
{'lat': 5.51, 'lon': -76.58, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813537, 'sunset': 1641856101, 'temp': 25.09, 'feels_like': 25.95, 'pressure': 1010, 'humidity': 88, 'dew_point': 22.96, 'uvi': 3.7, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 204, 'wind_gust': 3.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.62}}, 'hourly': [{'dt': 1641772800, 'temp': 27.09, 'feels_like': 31.68, 'pressure': 1011, 'humidity': 96, 'dew_point': 26.4, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 194, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641776400, 'temp': 22.88, 'feels_like': 23.76, 'pressure': 1012, 'humidity': 97, 'dew_point': 22.38, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 165, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641780000, 'temp': 22.64, 'feels_like': 23.52, 'pressure': 1013, 'humidity': 98, 'dew_point': 22.31, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 168, 'wind_gust': 1.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.54, 'feels_like': 23.41, 'pressure': 1013, 'humidity': 98, 'dew_point': 22.21, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 158, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641787200, 'temp': 22.32, 'feels_like': 23.19, 'pressure': 1013, 'humidity': 99, 'dew_point': 22.15, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 163, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.17, 'feels_like': 23.03, 'pressure': 1012, 'humidity': 99, 'dew_point': 22.01, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 157, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.08, 'feels_like': 22.93, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.92, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 158, 'wind_gust': 1.27, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 21.88, 'feels_like': 22.71, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.72, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 167, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641801600, 'temp': 21.7, 'feels_like': 22.51, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.54, 'uvi': 0, 'clouds': 67, 'visibility': 8799, 'wind_speed': 0.75, 'wind_deg': 187, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.62}}, {'dt': 1641805200, 'temp': 21.64, 'feels_like': 22.44, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.48, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 172, 'wind_gust': 1.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.18}}, {'dt': 1641808800, 'temp': 21.58, 'feels_like': 22.38, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.42, 'uvi': 0, 'clouds': 80, 'visibility': 3936, 'wind_speed': 0.75, 'wind_deg': 150, 'wind_gust': 1.83, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.9}}, {'dt': 1641812400, 'temp': 24.09, 'feels_like': 25.14, 'pressure': 1012, 'humidity': 99, 'dew_point': 23.92, 'uvi': 0, 'clouds': 84, 'visibility': 7091, 'wind_speed': 0.85, 'wind_deg': 149, 'wind_gust': 2.08, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.65}}, {'dt': 1641816000, 'temp': 24.09, 'feels_like': 25.14, 'pressure': 1013, 'humidity': 99, 'dew_point': 23.92, 'uvi': 0.07, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 132, 'wind_gust': 1.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, {'dt': 1641819600, 'temp': 23.09, 'feels_like': 23.96, 'pressure': 1014, 'humidity': 96, 'dew_point': 22.42, 'uvi': 1.22, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 141, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641823200, 'temp': 23.09, 'feels_like': 23.94, 'pressure': 1015, 'humidity': 95, 'dew_point': 22.24, 'uvi': 3.17, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 130, 'wind_gust': 1.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641826800, 'temp': 23.09, 'feels_like': 23.8, 'pressure': 1014, 'humidity': 90, 'dew_point': 21.36, 'uvi': 5.64, 'clouds': 93, 'visibility': 8099, 'wind_speed': 0.53, 'wind_deg': 90, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.79}}, {'dt': 1641830400, 'temp': 23.09, 'feels_like': 23.62, 'pressure': 1013, 'humidity': 83, 'dew_point': 20.05, 'uvi': 7.52, 'clouds': 93, 'visibility': 8908, 'wind_speed': 0.56, 'wind_deg': 211, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.49}}, {'dt': 1641834000, 'temp': 23.09, 'feels_like': 23.62, 'pressure': 1013, 'humidity': 83, 'dew_point': 20.05, 'uvi': 8.46, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 215, 'wind_gust': 2.53, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.75}}, {'dt': 1641837600, 'temp': 23.09, 'feels_like': 23.67, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.43, 'uvi': 7.91, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 217, 'wind_gust': 2.71, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.66}}, {'dt': 1641841200, 'temp': 24.09, 'feels_like': 24.75, 'pressure': 1011, 'humidity': 84, 'dew_point': 21.22, 'uvi': 6.11, 'clouds': 98, 'visibility': 8196, 'wind_speed': 1.44, 'wind_deg': 206, 'wind_gust': 2.68, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.59}}, {'dt': 1641844800, 'temp': 25.09, 'feels_like': 25.95, 'pressure': 1010, 'humidity': 88, 'dew_point': 22.96, 'uvi': 3.7, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 204, 'wind_gust': 3.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.62}}, {'dt': 1641848400, 'temp': 25.09, 'feels_like': 26.06, 'pressure': 1010, 'humidity': 92, 'dew_point': 23.7, 'uvi': 1.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 210, 'wind_gust': 3.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.97}}, {'dt': 1641852000, 'temp': 25.09, 'feels_like': 26.14, 'pressure': 1010, 'humidity': 95, 'dew_point': 24.23, 'uvi': 0.36, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 203, 'wind_gust': 3.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.91}}, {'dt': 1641855600, 'temp': 25.09, 'feels_like': 26.16, 'pressure': 1011, 'humidity': 96, 'dew_point': 24.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 201, 'wind_gust': 3.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.28}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 00:00:00 | 73.000000 | 26.400000 | 31.680000 | 96.000000 | 1011.000000 | 0.33 | 27.090000 | 0.000000 | 10000.000000 | 194.000000 | 0.93 | 0.920000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 01:00:00 | 86.000000 | 22.380000 | 23.760000 | 97.000000 | 1012.000000 | 0.19 | 22.880000 | 0.000000 | 10000.000000 | 165.000000 | 1.16 | 1.040000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 02:00:00 | 63.000000 | 22.310000 | 23.520000 | 98.000000 | 1013.000000 |  | 22.640000 | 0.000000 | 10000.000000 | 168.000000 | 1.82 | 1.160000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 03:00:00 | 65.000000 | 22.210000 | 23.410000 | 98.000000 | 1013.000000 | 0.16 | 22.540000 | 0.000000 | 10000.000000 | 158.000000 | 2.13 | 1.050000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 04:00:00 | 62.000000 | 22.150000 | 23.190000 | 99.000000 | 1013.000000 |  | 22.320000 | 0.000000 | 10000.000000 | 163.000000 | 1.72 | 0.890000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 05:00:00 | 67.000000 | 22.010000 | 23.030000 | 99.000000 | 1012.000000 |  | 22.170000 | 0.000000 | 10000.000000 | 157.000000 | 1.43 | 0.770000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 21.920000 | 22.930000 | 99.000000 | 1012.000000 |  | 22.080000 | 0.000000 | 10000.000000 | 158.000000 | 1.27 | 0.730000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 07:00:00 | 73.000000 | 21.720000 | 22.710000 | 99.000000 | 1011.000000 | 0.4 | 21.880000 | 0.000000 | 10000.000000 | 167.000000 | 1.33 | 0.710000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 08:00:00 | 67.000000 | 21.540000 | 22.510000 | 99.000000 | 1011.000000 | 0.62 | 21.700000 | 0.000000 | 8799.000000 | 187.000000 | 1.55 | 0.750000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 09:00:00 | 74.000000 | 21.480000 | 22.440000 | 99.000000 | 1011.000000 | 1.18 | 21.640000 | 0.000000 | 10000.000000 | 172.000000 | 1.57 | 0.760000 | 501 | Rain | moderate rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 10:00:00 | 80.000000 | 21.420000 | 22.380000 | 99.000000 | 1012.000000 | 1.9 | 21.580000 | 0.000000 | 3936.000000 | 150.000000 | 1.83 | 0.750000 | 501 | Rain | moderate rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 11:00:00 | 84.000000 | 23.920000 | 25.140000 | 99.000000 | 1012.000000 | 1.65 | 24.090000 | 0.000000 | 7091.000000 | 149.000000 | 2.08 | 0.850000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 12:00:00 | 57.000000 | 23.920000 | 25.140000 | 99.000000 | 1013.000000 | 0.71 | 24.090000 | 0.070000 | 10000.000000 | 132.000000 | 1.29 | 0.440000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 22.420000 | 23.960000 | 96.000000 | 1014.000000 | 0.24 | 23.090000 | 1.220000 | 10000.000000 | 141.000000 | 1.51 | 0.570000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 14:00:00 | 93.000000 | 22.240000 | 23.940000 | 95.000000 | 1015.000000 | 0.16 | 23.090000 | 3.170000 | 10000.000000 | 130.000000 | 1.41 | 0.610000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 15:00:00 | 93.000000 | 21.360000 | 23.800000 | 90.000000 | 1014.000000 | 0.79 | 23.090000 | 5.640000 | 8099.000000 | 90.000000 | 1.5 | 0.530000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 16:00:00 | 93.000000 | 20.050000 | 23.620000 | 83.000000 | 1013.000000 | 1.49 | 23.090000 | 7.520000 | 8908.000000 | 211.000000 | 1.45 | 0.560000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 17:00:00 | 86.000000 | 20.050000 | 23.620000 | 83.000000 | 1013.000000 | 1.75 | 23.090000 | 8.460000 | 10000.000000 | 215.000000 | 2.53 | 1.430000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 18:00:00 | 85.000000 | 20.430000 | 23.670000 | 85.000000 | 1012.000000 | 1.66 | 23.090000 | 7.910000 | 10000.000000 | 217.000000 | 2.71 | 1.520000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 21.220000 | 24.750000 | 84.000000 | 1011.000000 | 1.59 | 24.090000 | 6.110000 | 8196.000000 | 206.000000 | 2.68 | 1.440000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 22.960000 | 25.950000 | 88.000000 | 1010.000000 | 1.62 | 25.090000 | 3.700000 | 10000.000000 | 204.000000 | 3.18 | 1.530000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 23.700000 | 26.060000 | 92.000000 | 1010.000000 | 1.97 | 25.090000 | 1.610000 | 10000.000000 | 210.000000 | 3.35 | 1.300000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 24.230000 | 26.140000 | 95.000000 | 1010.000000 | 1.91 | 25.090000 | 0.360000 | 10000.000000 | 203.000000 | 3.02 | 1.170000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11035010 | "LLORO [11035010]" | 5.510000 | -76.580000 | 41.000000 | Climática Principal | Automática con Telemetría | Activa | 2018-04-18 00:00:00 | NaT | Chocó | Lloró | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Quito | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 24.410000 | 26.160000 | 96.000000 | 1011.000000 | 1.28 | 25.090000 | 0.000000 | 10000.000000 | 201.000000 | 3.57 | 1.360000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station11035010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station11035010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station11035010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11035010_OWM_Windspeed_20220111.png)
