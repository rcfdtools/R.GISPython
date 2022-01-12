
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - FLORENCIA - AUT [44035040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44035040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.733,-75.64502778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.733&lon=-75.64502778)


| Parameter | Value |
|---|---|
| Code | 44035040 |
| Name | FLORENCIA - AUT [44035040] |
| Latitude, ° | 1.733 |
| Longitude, ° | -75.64502778 |
| Elevation, m | 600 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-02-03 19:00:00 |
| Suspension date | NaT |
| State | Caquetá |
| County | Florencia (Caquetá) |
| Stream | 0 |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Caquetá |
| SZH - Hydrographic subzone | Río Orteguaza |

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

### (CNE index 415) Open Weather values for station 44035040 - FLORENCIA - AUT [44035040]

JSON data from API OWM:

```
{'lat': 1.733, 'lon': -75.645, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812947, 'sunset': 1641856242, 'temp': 25.9, 'feels_like': 26.58, 'pressure': 1010, 'humidity': 78, 'dew_point': 21.77, 'uvi': 5.88, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 122, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, 'hourly': [{'dt': 1641772800, 'temp': 22.84, 'feels_like': 23.35, 'pressure': 1011, 'humidity': 83, 'dew_point': 19.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 341, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 22.66, 'feels_like': 23.15, 'pressure': 1013, 'humidity': 83, 'dew_point': 19.63, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 346, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 22.72, 'feels_like': 23.19, 'pressure': 1014, 'humidity': 82, 'dew_point': 19.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 351, 'wind_gust': 1.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.62, 'feels_like': 23.08, 'pressure': 1014, 'humidity': 82, 'dew_point': 19.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 354, 'wind_gust': 1.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.67, 'feels_like': 23.13, 'pressure': 1014, 'humidity': 82, 'dew_point': 19.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 349, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.48, 'feels_like': 22.95, 'pressure': 1013, 'humidity': 83, 'dew_point': 19.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 348, 'wind_gust': 1.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.27, 'feels_like': 22.77, 'pressure': 1013, 'humidity': 85, 'dew_point': 19.63, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 341, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641798000, 'temp': 22.33, 'feels_like': 22.84, 'pressure': 1012, 'humidity': 85, 'dew_point': 19.69, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 340, 'wind_gust': 1.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.36, 'feels_like': 22.87, 'pressure': 1011, 'humidity': 85, 'dew_point': 19.72, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 339, 'wind_gust': 1.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641805200, 'temp': 22.11, 'feels_like': 22.62, 'pressure': 1012, 'humidity': 86, 'dew_point': 19.66, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 331, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641808800, 'temp': 21.76, 'feels_like': 22.29, 'pressure': 1012, 'humidity': 88, 'dew_point': 19.68, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 340, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.92, 'feels_like': 22.41, 'pressure': 1013, 'humidity': 86, 'dew_point': 19.47, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 347, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.52, 'feels_like': 23.05, 'pressure': 1014, 'humidity': 85, 'dew_point': 19.87, 'uvi': 0.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 344, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641819600, 'temp': 23.21, 'feels_like': 23.75, 'pressure': 1015, 'humidity': 83, 'dew_point': 20.16, 'uvi': 1.02, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 13, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641823200, 'temp': 23.39, 'feels_like': 24, 'pressure': 1016, 'humidity': 85, 'dew_point': 20.72, 'uvi': 2.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 141, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641826800, 'temp': 24.2, 'feels_like': 24.82, 'pressure': 1015, 'humidity': 82, 'dew_point': 20.93, 'uvi': 4.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 136, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641830400, 'temp': 26.18, 'feels_like': 26.18, 'pressure': 1014, 'humidity': 74, 'dew_point': 21.18, 'uvi': 12.32, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 153, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641834000, 'temp': 27.66, 'feels_like': 30.02, 'pressure': 1013, 'humidity': 70, 'dew_point': 21.69, 'uvi': 13.65, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 155, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641837600, 'temp': 27.84, 'feels_like': 30.36, 'pressure': 1012, 'humidity': 70, 'dew_point': 21.86, 'uvi': 12.63, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 158, 'wind_gust': 1.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.07}}, {'dt': 1641841200, 'temp': 27.07, 'feels_like': 29.15, 'pressure': 1011, 'humidity': 72, 'dew_point': 21.59, 'uvi': 9.73, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 157, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641844800, 'temp': 25.9, 'feels_like': 26.58, 'pressure': 1010, 'humidity': 78, 'dew_point': 21.77, 'uvi': 5.88, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 122, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641848400, 'temp': 25.21, 'feels_like': 25.9, 'pressure': 1010, 'humidity': 81, 'dew_point': 21.72, 'uvi': 2.56, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 348, 'wind_gust': 1.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641852000, 'temp': 24.69, 'feels_like': 25.38, 'pressure': 1010, 'humidity': 83, 'dew_point': 21.61, 'uvi': 0.41, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 3, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641855600, 'temp': 23.3, 'feels_like': 23.93, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.83, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 354, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 19.800000 | 23.350000 | 83.000000 | 1011.000000 |  | 22.840000 | 0.000000 | 10000.000000 | 341.000000 | 1.28 | 1.230000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 19.630000 | 23.150000 | 83.000000 | 1013.000000 |  | 22.660000 | 0.000000 | 10000.000000 | 346.000000 | 1.58 | 1.460000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 19.490000 | 23.190000 | 82.000000 | 1014.000000 |  | 22.720000 | 0.000000 | 10000.000000 | 351.000000 | 1.98 | 1.510000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 19.390000 | 23.080000 | 82.000000 | 1014.000000 |  | 22.620000 | 0.000000 | 10000.000000 | 354.000000 | 1.91 | 1.550000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 19.440000 | 23.130000 | 82.000000 | 1014.000000 |  | 22.670000 | 0.000000 | 10000.000000 | 349.000000 | 1.89 | 1.580000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 19.450000 | 22.950000 | 83.000000 | 1013.000000 |  | 22.480000 | 0.000000 | 10000.000000 | 348.000000 | 1.8 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 19.630000 | 22.770000 | 85.000000 | 1013.000000 | 0.13 | 22.270000 | 0.000000 | 10000.000000 | 341.000000 | 1.47 | 1.440000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.690000 | 22.840000 | 85.000000 | 1012.000000 |  | 22.330000 | 0.000000 | 10000.000000 | 340.000000 | 1.48 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 19.720000 | 22.870000 | 85.000000 | 1011.000000 | 0.17 | 22.360000 | 0.000000 | 10000.000000 | 339.000000 | 1.41 | 1.360000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 09:00:00 | 97.000000 | 19.660000 | 22.620000 | 86.000000 | 1012.000000 | 0.11 | 22.110000 | 0.000000 | 10000.000000 | 331.000000 | 1.08 | 1.370000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 10:00:00 | 94.000000 | 19.680000 | 22.290000 | 88.000000 | 1012.000000 |  | 21.760000 | 0.000000 | 10000.000000 | 340.000000 | 1.16 | 1.410000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 11:00:00 | 95.000000 | 19.470000 | 22.410000 | 86.000000 | 1013.000000 |  | 21.920000 | 0.000000 | 10000.000000 | 347.000000 | 1.22 | 1.330000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 19.870000 | 23.050000 | 85.000000 | 1014.000000 | 0.17 | 22.520000 | 0.360000 | 10000.000000 | 344.000000 | 1.21 | 1.020000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 20.160000 | 23.750000 | 83.000000 | 1015.000000 | 0.14 | 23.210000 | 1.020000 | 10000.000000 | 13.000000 | 0.54 | 0.190000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 20.720000 | 24.000000 | 85.000000 | 1016.000000 | 0.25 | 23.390000 | 2.480000 | 10000.000000 | 141.000000 | 0.93 | 0.400000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 20.930000 | 24.820000 | 82.000000 | 1015.000000 | 0.38 | 24.200000 | 4.260000 | 10000.000000 | 136.000000 | 0.92 | 0.540000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 16:00:00 | 89.000000 | 21.180000 | 26.180000 | 74.000000 | 1014.000000 | 0.43 | 26.180000 | 12.320000 | 10000.000000 | 153.000000 | 1.31 | 1.390000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 17:00:00 | 87.000000 | 21.690000 | 30.020000 | 70.000000 | 1013.000000 | 0.86 | 27.660000 | 13.650000 | 10000.000000 | 155.000000 | 1.67 | 1.390000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 18:00:00 | 92.000000 | 21.860000 | 30.360000 | 70.000000 | 1012.000000 | 1.07 | 27.840000 | 12.630000 | 10000.000000 | 158.000000 | 1.87 | 1.170000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 21.590000 | 29.150000 | 72.000000 | 1011.000000 | 0.86 | 27.070000 | 9.730000 | 10000.000000 | 157.000000 | 1.82 | 0.760000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 20:00:00 | 93.000000 | 21.770000 | 26.580000 | 78.000000 | 1010.000000 | 0.6 | 25.900000 | 5.880000 | 10000.000000 | 122.000000 | 1.27 | 0.170000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 21.720000 | 25.900000 | 81.000000 | 1010.000000 | 0.54 | 25.210000 | 2.560000 | 10000.000000 | 348.000000 | 1.49 | 0.190000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 22:00:00 | 84.000000 | 21.610000 | 25.380000 | 83.000000 | 1010.000000 | 0.29 | 24.690000 | 0.410000 | 10000.000000 | 3.000000 | 1.73 | 0.340000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44035040 | "FLORENCIA - AUT [44035040]" | 1.733000 | -75.645028 | 600.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-02-03 19:00:00 | NaT | Caquetá | Florencia (Caquetá) | 0 | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 23:00:00 | 84.000000 | 20.830000 | 23.930000 | 86.000000 | 1011.000000 | 0.21 | 23.300000 | 0.000000 | 10000.000000 | 354.000000 | 1.3 | 0.820000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station44035040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44035040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44035040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44035040_OWM_Windspeed_20220111.png)
