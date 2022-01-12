
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - JHB CAUCASIA [26245040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26245040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.00563889,-75.14694444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.00563889&lon=-75.14694444)


| Parameter | Value |
|---|---|
| Code | 26245040 |
| Name | JHB CAUCASIA [26245040] |
| Latitude, ° | 8.00563889 |
| Longitude, ° | -75.14694444 |
| Elevation, m | 54 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2008-04-13 00:00:00 |
| Suspension date | 2018-05-25 07:39:57 |
| State | Antioquia |
| County | Caucasia |
| Stream | 0 |
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

### (CNE index 2578) Open Weather values for station 26245040 - JHB CAUCASIA [26245040]

JSON data from API OWM:

```
{'lat': 8.0056, 'lon': -75.1469, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813437, 'sunset': 1641855513, 'temp': 30.5, 'feels_like': 32.95, 'pressure': 1008, 'humidity': 56, 'dew_point': 20.73, 'uvi': 4.11, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 323, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.88, 'feels_like': 26.53, 'pressure': 1010, 'humidity': 77, 'dew_point': 21.54, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 279, 'wind_gust': 1.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.36, 'feels_like': 26.01, 'pressure': 1010, 'humidity': 79, 'dew_point': 21.45, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 290, 'wind_gust': 1.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 25.01, 'feels_like': 25.63, 'pressure': 1011, 'humidity': 79, 'dew_point': 21.11, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 272, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.46, 'feels_like': 25.08, 'pressure': 1011, 'humidity': 81, 'dew_point': 20.99, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 287, 'wind_gust': 1.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.57, 'feels_like': 24.25, 'pressure': 1012, 'humidity': 87, 'dew_point': 21.28, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 336, 'wind_gust': 3.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.02, 'feels_like': 23.75, 'pressure': 1012, 'humidity': 91, 'dew_point': 21.47, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 354, 'wind_gust': 4.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.31, 'feels_like': 23.1, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.64, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 346, 'wind_gust': 2.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641798000, 'temp': 22.03, 'feels_like': 22.85, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.7, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 328, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1641801600, 'temp': 21.71, 'feels_like': 22.5, 'pressure': 1010, 'humidity': 98, 'dew_point': 21.38, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 241, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.9}}, {'dt': 1641805200, 'temp': 21.57, 'feels_like': 22.37, 'pressure': 1010, 'humidity': 99, 'dew_point': 21.41, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 200, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.63}}, {'dt': 1641808800, 'temp': 21.47, 'feels_like': 22.26, 'pressure': 1011, 'humidity': 99, 'dew_point': 21.31, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 180, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.6}}, {'dt': 1641812400, 'temp': 21.43, 'feels_like': 22.21, 'pressure': 1012, 'humidity': 99, 'dew_point': 21.27, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 178, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641816000, 'temp': 22.09, 'feels_like': 22.89, 'pressure': 1013, 'humidity': 97, 'dew_point': 21.59, 'uvi': 0.21, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 160, 'wind_gust': 1.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.52, 'feels_like': 24.36, 'pressure': 1014, 'humidity': 93, 'dew_point': 22.32, 'uvi': 1.48, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 150, 'wind_gust': 1.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.07, 'feels_like': 25.9, 'pressure': 1014, 'humidity': 87, 'dew_point': 22.75, 'uvi': 3.75, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 151, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.1, 'feels_like': 29.67, 'pressure': 1014, 'humidity': 77, 'dew_point': 22.72, 'uvi': 6.57, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 137, 'wind_gust': 0.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.1, 'feels_like': 32.39, 'pressure': 1013, 'humidity': 67, 'dew_point': 22.35, 'uvi': 6.21, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 40, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.28, 'feels_like': 33.37, 'pressure': 1012, 'humidity': 60, 'dew_point': 21.65, 'uvi': 6.87, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 0, 'wind_gust': 1.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.75, 'feels_like': 33.2, 'pressure': 1011, 'humidity': 55, 'dew_point': 20.67, 'uvi': 6.29, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 348, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.88, 'feels_like': 33.23, 'pressure': 1009, 'humidity': 54, 'dew_point': 20.49, 'uvi': 7.04, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 333, 'wind_gust': 1.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.5, 'feels_like': 32.95, 'pressure': 1008, 'humidity': 56, 'dew_point': 20.73, 'uvi': 4.11, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 323, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.88, 'feels_like': 32.8, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.55, 'uvi': 1.66, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 311, 'wind_gust': 2.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.05, 'feels_like': 31.18, 'pressure': 1009, 'humidity': 73, 'dew_point': 22.76, 'uvi': 0.35, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 310, 'wind_gust': 4.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1009, 'humidity': 80, 'dew_point': 22.26, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 311, 'wind_gust': 4.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 00:00:00 | 39.000000 | 21.540000 | 26.530000 | 77.000000 | 1010.000000 |  | 25.880000 | 0.000000 | 10000.000000 | 279.000000 | 1.59 | 1.460000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 01:00:00 | 45.000000 | 21.450000 | 26.010000 | 79.000000 | 1010.000000 |  | 25.360000 | 0.000000 | 10000.000000 | 290.000000 | 1.63 | 1.550000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 02:00:00 | 52.000000 | 21.110000 | 25.630000 | 79.000000 | 1011.000000 |  | 25.010000 | 0.000000 | 10000.000000 | 272.000000 | 1.3 | 1.240000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 03:00:00 | 67.000000 | 20.990000 | 25.080000 | 81.000000 | 1011.000000 |  | 24.460000 | 0.000000 | 10000.000000 | 287.000000 | 1.42 | 1.080000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 04:00:00 | 74.000000 | 21.280000 | 24.250000 | 87.000000 | 1012.000000 |  | 23.570000 | 0.000000 | 10000.000000 | 336.000000 | 3.5 | 1.840000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 05:00:00 | 75.000000 | 21.470000 | 23.750000 | 91.000000 | 1012.000000 |  | 23.020000 | 0.000000 | 10000.000000 | 354.000000 | 4.77 | 1.850000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 06:00:00 | 67.000000 | 21.640000 | 23.100000 | 96.000000 | 1011.000000 | 0.26 | 22.310000 | 0.000000 | 10000.000000 | 346.000000 | 2.02 | 1.290000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 07:00:00 | 83.000000 | 21.700000 | 22.850000 | 98.000000 | 1011.000000 | 0.75 | 22.030000 | 0.000000 | 10000.000000 | 328.000000 | 1 | 0.830000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 08:00:00 | 63.000000 | 21.380000 | 22.500000 | 98.000000 | 1010.000000 | 0.9 | 21.710000 | 0.000000 | 10000.000000 | 241.000000 | 0.94 | 0.670000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 09:00:00 | 52.000000 | 21.410000 | 22.370000 | 99.000000 | 1010.000000 | 0.63 | 21.570000 | 0.000000 | 10000.000000 | 200.000000 | 1.14 | 1.110000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 10:00:00 | 49.000000 | 21.310000 | 22.260000 | 99.000000 | 1011.000000 | 0.6 | 21.470000 | 0.000000 | 10000.000000 | 180.000000 | 1.45 | 1.320000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 11:00:00 | 48.000000 | 21.270000 | 22.210000 | 99.000000 | 1012.000000 | 0.26 | 21.430000 | 0.000000 | 10000.000000 | 178.000000 | 1.33 | 1.130000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 12:00:00 | 74.000000 | 21.590000 | 22.890000 | 97.000000 | 1013.000000 |  | 22.090000 | 0.210000 | 10000.000000 | 160.000000 | 1.57 | 1.050000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 13:00:00 | 87.000000 | 22.320000 | 24.360000 | 93.000000 | 1014.000000 |  | 23.520000 | 1.480000 | 10000.000000 | 150.000000 | 1.31 | 1.260000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 14:00:00 | 86.000000 | 22.750000 | 25.900000 | 87.000000 | 1014.000000 |  | 25.070000 | 3.750000 | 10000.000000 | 151.000000 | 1.01 | 1.230000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 15:00:00 | 74.000000 | 22.720000 | 29.670000 | 77.000000 | 1014.000000 |  | 27.100000 | 6.570000 | 10000.000000 | 137.000000 | 0.5 | 1.000000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 16:00:00 | 80.000000 | 22.350000 | 32.390000 | 67.000000 | 1013.000000 |  | 29.100000 | 6.210000 | 10000.000000 | 40.000000 | 0.8 | 0.370000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 17:00:00 | 79.000000 | 21.650000 | 33.370000 | 60.000000 | 1012.000000 |  | 30.280000 | 6.870000 | 10000.000000 | 0.000000 | 1.54 | 1.180000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 18:00:00 | 72.000000 | 20.670000 | 33.200000 | 55.000000 | 1011.000000 |  | 30.750000 | 6.290000 | 10000.000000 | 348.000000 | 1.72 | 1.480000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 19:00:00 | 82.000000 | 20.490000 | 33.230000 | 54.000000 | 1009.000000 |  | 30.880000 | 7.040000 | 10000.000000 | 333.000000 | 1.99 | 1.850000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 20:00:00 | 91.000000 | 20.730000 | 32.950000 | 56.000000 | 1008.000000 |  | 30.500000 | 4.110000 | 10000.000000 | 323.000000 | 2.41 | 2.130000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 21:00:00 | 91.000000 | 21.550000 | 32.800000 | 61.000000 | 1008.000000 |  | 29.880000 | 1.660000 | 10000.000000 | 311.000000 | 2.61 | 2.280000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 22:00:00 | 92.000000 | 22.760000 | 31.180000 | 73.000000 | 1009.000000 |  | 28.050000 | 0.350000 | 10000.000000 | 310.000000 | 4.68 | 2.470000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26245040 | "JHB CAUCASIA [26245040]" | 8.005639 | -75.146944 | 54.000000 | Climática Principal | Convencional | Suspendida | 2008-04-13 00:00:00 | 2018-05-25 07:39:57 | Antioquia | Caucasia | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Cauca | Directos al Cauca entre Pto Valdivia y Río Nechí | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 22.260000 | 25.980000 | 80.000000 | 1009.000000 |  | 25.980000 | 0.000000 | 10000.000000 | 311.000000 | 4.82 | 2.340000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station26245040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26245040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26245040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26245040_OWM_Windspeed_20220111.png)
