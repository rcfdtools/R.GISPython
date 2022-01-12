
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CACAOTERAS DEL DIQ [26255040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26255040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.98333333,-75.11666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.98333333&lon=-75.11666667)


| Parameter | Value |
|---|---|
| Code | 26255040 |
| Name | CACAOTERAS DEL DIQ [26255040] |
| Latitude, ° | 7.98333333 |
| Longitude, ° | -75.11666667 |
| Elevation, m | 55 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-08-15 00:00:00 |
| Suspension date | 2008-12-10 00:00:00 |
| State | Antioquia |
| County | Caucasia |
| Stream | Cauca |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Directos al Cauca entre Pto Valdivia y Río Nechí |

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

### (CNE index 347) Open Weather values for station 26255040 - CACAOTERAS DEL DIQ [26255040]

JSON data from API OWM:

```
{'lat': 7.9833, 'lon': -75.1167, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813427, 'sunset': 1641855508, 'temp': 30.53, 'feels_like': 32.81, 'pressure': 1008, 'humidity': 55, 'dew_point': 20.47, 'uvi': 4.14, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 324, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.72, 'feels_like': 26.36, 'pressure': 1010, 'humidity': 77, 'dew_point': 21.38, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 273, 'wind_gust': 1.52, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.17, 'feels_like': 25.83, 'pressure': 1010, 'humidity': 80, 'dew_point': 21.47, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 284, 'wind_gust': 1.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 24.8, 'feels_like': 25.45, 'pressure': 1011, 'humidity': 81, 'dew_point': 21.32, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 269, 'wind_gust': 1.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 24.28, 'feels_like': 24.9, 'pressure': 1011, 'humidity': 82, 'dew_point': 21.01, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 277, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.48, 'feels_like': 24.16, 'pressure': 1012, 'humidity': 87, 'dew_point': 21.19, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 335, 'wind_gust': 2.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.94, 'feels_like': 23.67, 'pressure': 1012, 'humidity': 91, 'dew_point': 21.39, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 352, 'wind_gust': 4.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.2, 'feels_like': 22.98, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.53, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 349, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641798000, 'temp': 21.95, 'feels_like': 22.76, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.62, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 331, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1641801600, 'temp': 21.65, 'feels_like': 22.46, 'pressure': 1010, 'humidity': 99, 'dew_point': 21.49, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 230, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.88}}, {'dt': 1641805200, 'temp': 21.5, 'feels_like': 22.29, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.34, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 199, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.59}}, {'dt': 1641808800, 'temp': 21.46, 'feels_like': 22.25, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.3, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 179, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.54}}, {'dt': 1641812400, 'temp': 21.41, 'feels_like': 22.19, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.25, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 174, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641816000, 'temp': 22.04, 'feels_like': 22.86, 'pressure': 1013, 'humidity': 98, 'dew_point': 21.71, 'uvi': 0.34, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 159, 'wind_gust': 1.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.44, 'feels_like': 24.27, 'pressure': 1014, 'humidity': 93, 'dew_point': 22.24, 'uvi': 1.66, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 152, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 24.97, 'feels_like': 25.79, 'pressure': 1014, 'humidity': 87, 'dew_point': 22.65, 'uvi': 4.19, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 150, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.05, 'feels_like': 29.57, 'pressure': 1014, 'humidity': 77, 'dew_point': 22.67, 'uvi': 7.31, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 135, 'wind_gust': 0.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.16, 'feels_like': 32.51, 'pressure': 1013, 'humidity': 67, 'dew_point': 22.4, 'uvi': 9.16, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 36, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.4, 'feels_like': 33.4, 'pressure': 1012, 'humidity': 59, 'dew_point': 21.49, 'uvi': 10.13, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 359, 'wind_gust': 1.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.86, 'feels_like': 33.19, 'pressure': 1011, 'humidity': 54, 'dew_point': 20.47, 'uvi': 9.28, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 347, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.95, 'feels_like': 33.14, 'pressure': 1009, 'humidity': 53, 'dew_point': 20.26, 'uvi': 7.08, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 332, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.53, 'feels_like': 32.81, 'pressure': 1008, 'humidity': 55, 'dew_point': 20.47, 'uvi': 4.14, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 324, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.89, 'feels_like': 32.82, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.55, 'uvi': 1.67, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 312, 'wind_gust': 2.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.98, 'feels_like': 31.03, 'pressure': 1009, 'humidity': 73, 'dew_point': 22.69, 'uvi': 0.36, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 308, 'wind_gust': 4.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 25.92, 'feels_like': 26.66, 'pressure': 1009, 'humidity': 80, 'dew_point': 22.2, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 309, 'wind_gust': 4.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 00:00:00 | 34.000000 | 21.380000 | 26.360000 | 77.000000 | 1010.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 273.000000 | 1.52 | 1.400000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 01:00:00 | 40.000000 | 21.470000 | 25.830000 | 80.000000 | 1010.000000 |  | 25.170000 | 0.000000 | 10000.000000 | 284.000000 | 1.56 | 1.460000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 02:00:00 | 44.000000 | 21.320000 | 25.450000 | 81.000000 | 1011.000000 |  | 24.800000 | 0.000000 | 10000.000000 | 269.000000 | 1.21 | 1.140000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 03:00:00 | 62.000000 | 21.010000 | 24.900000 | 82.000000 | 1011.000000 |  | 24.280000 | 0.000000 | 10000.000000 | 277.000000 | 1.12 | 0.810000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 04:00:00 | 71.000000 | 21.190000 | 24.160000 | 87.000000 | 1012.000000 |  | 23.480000 | 0.000000 | 10000.000000 | 335.000000 | 2.93 | 1.580000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 05:00:00 | 73.000000 | 21.390000 | 23.670000 | 91.000000 | 1012.000000 |  | 22.940000 | 0.000000 | 10000.000000 | 352.000000 | 4.47 | 1.730000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 06:00:00 | 68.000000 | 21.530000 | 22.980000 | 96.000000 | 1011.000000 | 0.27 | 22.200000 | 0.000000 | 10000.000000 | 349.000000 | 1.78 | 1.210000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 07:00:00 | 83.000000 | 21.620000 | 22.760000 | 98.000000 | 1011.000000 | 0.75 | 21.950000 | 0.000000 | 10000.000000 | 331.000000 | 0.85 | 0.680000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 08:00:00 | 62.000000 | 21.490000 | 22.460000 | 99.000000 | 1010.000000 | 0.88 | 21.650000 | 0.000000 | 10000.000000 | 230.000000 | 0.82 | 0.570000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 09:00:00 | 53.000000 | 21.340000 | 22.290000 | 99.000000 | 1011.000000 | 0.59 | 21.500000 | 0.000000 | 10000.000000 | 199.000000 | 1.06 | 1.030000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 10:00:00 | 51.000000 | 21.300000 | 22.250000 | 99.000000 | 1011.000000 | 0.54 | 21.460000 | 0.000000 | 10000.000000 | 179.000000 | 1.44 | 1.250000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 11:00:00 | 50.000000 | 21.250000 | 22.190000 | 99.000000 | 1012.000000 | 0.29 | 21.410000 | 0.000000 | 10000.000000 | 174.000000 | 1.32 | 1.070000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 12:00:00 | 78.000000 | 21.710000 | 22.860000 | 98.000000 | 1013.000000 |  | 22.040000 | 0.340000 | 10000.000000 | 159.000000 | 1.58 | 1.000000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 13:00:00 | 90.000000 | 22.240000 | 24.270000 | 93.000000 | 1014.000000 |  | 23.440000 | 1.660000 | 10000.000000 | 152.000000 | 1.31 | 1.210000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 22.650000 | 25.790000 | 87.000000 | 1014.000000 |  | 24.970000 | 4.190000 | 10000.000000 | 150.000000 | 1.01 | 1.180000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 15:00:00 | 74.000000 | 22.670000 | 29.570000 | 77.000000 | 1014.000000 |  | 27.050000 | 7.310000 | 10000.000000 | 135.000000 | 0.48 | 0.940000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 16:00:00 | 80.000000 | 22.400000 | 32.510000 | 67.000000 | 1013.000000 |  | 29.160000 | 9.160000 | 10000.000000 | 36.000000 | 0.83 | 0.380000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 17:00:00 | 79.000000 | 21.490000 | 33.400000 | 59.000000 | 1012.000000 |  | 30.400000 | 10.130000 | 10000.000000 | 359.000000 | 1.56 | 1.160000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 18:00:00 | 65.000000 | 20.470000 | 33.190000 | 54.000000 | 1011.000000 |  | 30.860000 | 9.280000 | 10000.000000 | 347.000000 | 1.75 | 1.480000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 19:00:00 | 76.000000 | 20.260000 | 33.140000 | 53.000000 | 1009.000000 |  | 30.950000 | 7.080000 | 10000.000000 | 332.000000 | 2.01 | 1.840000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 20:00:00 | 88.000000 | 20.470000 | 32.810000 | 55.000000 | 1008.000000 |  | 30.530000 | 4.140000 | 10000.000000 | 324.000000 | 2.41 | 2.070000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 21.550000 | 32.820000 | 61.000000 | 1008.000000 |  | 29.890000 | 1.670000 | 10000.000000 | 312.000000 | 2.59 | 2.120000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 22:00:00 | 91.000000 | 22.690000 | 31.030000 | 73.000000 | 1009.000000 |  | 27.980000 | 0.360000 | 10000.000000 | 308.000000 | 4.5 | 2.250000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26255040 | "CACAOTERAS DEL DIQ [26255040]" | 7.983333 | -75.116667 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-08-15 00:00:00 | 2008-12-10 00:00:00 | Antioquia | Caucasia | Cauca | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 22.200000 | 26.660000 | 80.000000 | 1009.000000 |  | 25.920000 | 0.000000 | 10000.000000 | 309.000000 | 4.78 | 2.220000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station26255040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26255040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26255040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26255040_OWM_Windspeed_20220111.png)
