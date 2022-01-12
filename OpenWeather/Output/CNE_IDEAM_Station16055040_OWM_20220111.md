
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ABREGO CENTRO ADMO [16055040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16055040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.08722222,-73.22305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.08722222&lon=-73.22305556)


| Parameter | Value |
|---|---|
| Code | 16055040 |
| Name | ABREGO CENTRO ADMO [16055040] |
| Latitude, ° | 8.08722222 |
| Longitude, ° | -73.22305556 |
| Elevation, m | 1430 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1969-07-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Ábrego |
| Stream | Canal Zulia |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Algodonal (Alto Catatumbo) |

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

### (CNE index 2767) Open Weather values for station 16055040 - ABREGO CENTRO ADMO [16055040]

JSON data from API OWM:

```
{'lat': 8.0872, 'lon': -73.2231, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812983, 'sunset': 1641855043, 'temp': 22.95, 'feels_like': 22.74, 'pressure': 1012, 'humidity': 55, 'dew_point': 13.44, 'uvi': 3.96, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 7, 'wind_gust': 2.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.85, 'feels_like': 15.79, 'pressure': 1016, 'humidity': 88, 'dew_point': 13.87, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 79, 'wind_gust': 2.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 15.22, 'feels_like': 15.12, 'pressure': 1017, 'humidity': 89, 'dew_point': 13.42, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 3.07, 'wind_deg': 83, 'wind_gust': 2.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 14.71, 'feels_like': 14.53, 'pressure': 1018, 'humidity': 88, 'dew_point': 12.74, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 3.16, 'wind_deg': 85, 'wind_gust': 3.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 14.24, 'feels_like': 13.91, 'pressure': 1018, 'humidity': 84, 'dew_point': 11.58, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 3.22, 'wind_deg': 88, 'wind_gust': 3.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 13.89, 'feels_like': 13.4, 'pressure': 1018, 'humidity': 79, 'dew_point': 10.31, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 3.15, 'wind_deg': 93, 'wind_gust': 2.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 13.55, 'feels_like': 13, 'pressure': 1017, 'humidity': 78, 'dew_point': 9.79, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 3.2, 'wind_deg': 92, 'wind_gust': 2.84, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 13.19, 'feels_like': 12.6, 'pressure': 1017, 'humidity': 78, 'dew_point': 9.44, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 90, 'wind_gust': 2.49, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 12.9, 'feels_like': 12.28, 'pressure': 1016, 'humidity': 78, 'dew_point': 9.16, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 2.83, 'wind_deg': 90, 'wind_gust': 2.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 12.75, 'feels_like': 12.14, 'pressure': 1016, 'humidity': 79, 'dew_point': 9.2, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.91, 'wind_deg': 89, 'wind_gust': 2.66, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 12.77, 'feels_like': 12.22, 'pressure': 1016, 'humidity': 81, 'dew_point': 9.6, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 2.89, 'wind_deg': 88, 'wind_gust': 2.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 12.89, 'feels_like': 12.38, 'pressure': 1016, 'humidity': 82, 'dew_point': 9.9, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.91, 'wind_deg': 89, 'wind_gust': 2.85, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 12.9, 'feels_like': 12.36, 'pressure': 1017, 'humidity': 81, 'dew_point': 9.72, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.76, 'wind_deg': 89, 'wind_gust': 2.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 14.24, 'feels_like': 13.73, 'pressure': 1018, 'humidity': 77, 'dew_point': 10.27, 'uvi': 0.45, 'clouds': 81, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 88, 'wind_gust': 2.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.53, 'feels_like': 17.06, 'pressure': 1018, 'humidity': 66, 'dew_point': 11.11, 'uvi': 1.93, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 72, 'wind_gust': 2.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 19.78, 'feels_like': 19.35, 'pressure': 1018, 'humidity': 59, 'dew_point': 11.55, 'uvi': 4.66, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 48, 'wind_gust': 1.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.21, 'feels_like': 20.8, 'pressure': 1017, 'humidity': 54, 'dew_point': 11.54, 'uvi': 7.83, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 7, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 22.67, 'feels_like': 22.32, 'pressure': 1016, 'humidity': 51, 'dew_point': 12.03, 'uvi': 10.36, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 338, 'wind_gust': 1.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 23.54, 'feels_like': 23.26, 'pressure': 1015, 'humidity': 50, 'dew_point': 12.52, 'uvi': 11.18, 'clouds': 66, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 334, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 23.87, 'feels_like': 23.62, 'pressure': 1014, 'humidity': 50, 'dew_point': 12.83, 'uvi': 9.98, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 344, 'wind_gust': 2.22, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 23.9, 'feels_like': 23.7, 'pressure': 1012, 'humidity': 52, 'dew_point': 13.45, 'uvi': 7.09, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 354, 'wind_gust': 2.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 22.95, 'feels_like': 22.74, 'pressure': 1012, 'humidity': 55, 'dew_point': 13.44, 'uvi': 3.96, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 7, 'wind_gust': 2.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 21.39, 'feels_like': 21.28, 'pressure': 1012, 'humidity': 65, 'dew_point': 14.55, 'uvi': 1.52, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 27, 'wind_gust': 2.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 20.05, 'feels_like': 19.99, 'pressure': 1013, 'humidity': 72, 'dew_point': 14.85, 'uvi': 0.15, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 44, 'wind_gust': 2.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 18.36, 'feels_like': 18.29, 'pressure': 1014, 'humidity': 78, 'dew_point': 14.46, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 67, 'wind_gust': 2.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 00:00:00 | 78.000000 | 13.870000 | 15.790000 | 88.000000 | 1016.000000 |  | 15.850000 | 0.000000 | 10000.000000 | 79.000000 | 2.97 | 3.010000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 01:00:00 | 80.000000 | 13.420000 | 15.120000 | 89.000000 | 1017.000000 |  | 15.220000 | 0.000000 | 10000.000000 | 83.000000 | 2.96 | 3.070000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 02:00:00 | 63.000000 | 12.740000 | 14.530000 | 88.000000 | 1018.000000 |  | 14.710000 | 0.000000 | 10000.000000 | 85.000000 | 3.01 | 3.160000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 03:00:00 | 65.000000 | 11.580000 | 13.910000 | 84.000000 | 1018.000000 |  | 14.240000 | 0.000000 | 10000.000000 | 88.000000 | 3.01 | 3.220000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 04:00:00 | 51.000000 | 10.310000 | 13.400000 | 79.000000 | 1018.000000 |  | 13.890000 | 0.000000 | 10000.000000 | 93.000000 | 2.88 | 3.150000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 05:00:00 | 42.000000 | 9.790000 | 13.000000 | 78.000000 | 1017.000000 |  | 13.550000 | 0.000000 | 10000.000000 | 92.000000 | 2.84 | 3.200000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 06:00:00 | 36.000000 | 9.440000 | 12.600000 | 78.000000 | 1017.000000 |  | 13.190000 | 0.000000 | 10000.000000 | 90.000000 | 2.49 | 2.960000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 07:00:00 | 43.000000 | 9.160000 | 12.280000 | 78.000000 | 1016.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 90.000000 | 2.4 | 2.830000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 08:00:00 | 33.000000 | 9.200000 | 12.140000 | 79.000000 | 1016.000000 |  | 12.750000 | 0.000000 | 10000.000000 | 89.000000 | 2.66 | 2.910000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 09:00:00 | 35.000000 | 9.600000 | 12.220000 | 81.000000 | 1016.000000 |  | 12.770000 | 0.000000 | 10000.000000 | 88.000000 | 2.6 | 2.890000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 10:00:00 | 42.000000 | 9.900000 | 12.380000 | 82.000000 | 1016.000000 |  | 12.890000 | 0.000000 | 10000.000000 | 89.000000 | 2.85 | 2.910000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 11:00:00 | 42.000000 | 9.720000 | 12.360000 | 81.000000 | 1017.000000 |  | 12.900000 | 0.000000 | 10000.000000 | 89.000000 | 2.12 | 2.760000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 12:00:00 | 81.000000 | 10.270000 | 13.730000 | 77.000000 | 1018.000000 |  | 14.240000 | 0.450000 | 10000.000000 | 88.000000 | 2.52 | 2.540000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 13:00:00 | 83.000000 | 11.110000 | 17.060000 | 66.000000 | 1018.000000 |  | 17.530000 | 1.930000 | 10000.000000 | 72.000000 | 2.18 | 1.960000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 14:00:00 | 79.000000 | 11.550000 | 19.350000 | 59.000000 | 1018.000000 |  | 19.780000 | 4.660000 | 10000.000000 | 48.000000 | 1.74 | 1.610000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 15:00:00 | 84.000000 | 11.540000 | 20.800000 | 54.000000 | 1017.000000 |  | 21.210000 | 7.830000 | 10000.000000 | 7.000000 | 1.7 | 1.500000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 16:00:00 | 73.000000 | 12.030000 | 22.320000 | 51.000000 | 1016.000000 |  | 22.670000 | 10.360000 | 10000.000000 | 338.000000 | 1.82 | 1.880000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 17:00:00 | 66.000000 | 12.520000 | 23.260000 | 50.000000 | 1015.000000 |  | 23.540000 | 11.180000 | 10000.000000 | 334.000000 | 2.2 | 2.220000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 18:00:00 | 74.000000 | 12.830000 | 23.620000 | 50.000000 | 1014.000000 |  | 23.870000 | 9.980000 | 10000.000000 | 344.000000 | 2.22 | 2.310000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 13.450000 | 23.700000 | 52.000000 | 1012.000000 |  | 23.900000 | 7.090000 | 10000.000000 | 354.000000 | 2.46 | 2.410000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 20:00:00 | 91.000000 | 13.440000 | 22.740000 | 55.000000 | 1012.000000 |  | 22.950000 | 3.960000 | 10000.000000 | 7.000000 | 2.49 | 2.140000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 21:00:00 | 93.000000 | 14.550000 | 21.280000 | 65.000000 | 1012.000000 |  | 21.390000 | 1.520000 | 10000.000000 | 27.000000 | 2.77 | 1.870000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 14.850000 | 19.990000 | 72.000000 | 1013.000000 |  | 20.050000 | 0.150000 | 10000.000000 | 44.000000 | 2.58 | 1.920000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055040 | "ABREGO CENTRO ADMO [16055040]" | 8.087222 | -73.223056 | 1430.000000 | Climática Principal | Convencional | Activa | 1969-07-15 00:00:00 | NaT | Norte de Santander | Ábrego | Canal Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 14.460000 | 18.290000 | 78.000000 | 1014.000000 |  | 18.360000 | 0.000000 | 10000.000000 | 67.000000 | 2.23 | 2.280000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16055040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16055040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16055040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055040_OWM_Windspeed_20220111.png)
