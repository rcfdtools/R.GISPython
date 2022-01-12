
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SALAZAR [16025030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16025030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.77458333,-72.83055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.77458333&lon=-72.83055556)


| Parameter | Value |
|---|---|
| Code | 16025030 |
| Name | SALAZAR [16025030] |
| Latitude, ° | 7.77458333 |
| Longitude, ° | -72.83055556 |
| Elevation, m | 860 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1973-03-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Salazar |
| Stream | Carepa |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Zulia |

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

### (CNE index 512) Open Weather values for station 16025030 - SALAZAR [16025030]

JSON data from API OWM:

```
{'lat': 7.7746, 'lon': -72.8306, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812858, 'sunset': 1641854979, 'temp': 24.61, 'feels_like': 24.72, 'pressure': 1013, 'humidity': 61, 'dew_point': 16.59, 'uvi': 1.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 36, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 19.61, 'feels_like': 20.13, 'pressure': 1017, 'humidity': 96, 'dew_point': 18.95, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 205, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 19.61, 'feels_like': 20.13, 'pressure': 1018, 'humidity': 96, 'dew_point': 18.95, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 224, 'wind_gust': 2.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 18.61, 'feels_like': 19.03, 'pressure': 1019, 'humidity': 96, 'dew_point': 17.96, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 226, 'wind_gust': 2.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 17.61, 'feels_like': 17.88, 'pressure': 1019, 'humidity': 94, 'dew_point': 16.63, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 225, 'wind_gust': 2.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 16.61, 'feels_like': 16.73, 'pressure': 1019, 'humidity': 92, 'dew_point': 15.31, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 228, 'wind_gust': 2.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 16.61, 'feels_like': 16.65, 'pressure': 1019, 'humidity': 89, 'dew_point': 14.79, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 231, 'wind_gust': 2.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 16.61, 'feels_like': 16.57, 'pressure': 1018, 'humidity': 86, 'dew_point': 14.26, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 231, 'wind_gust': 2.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.36, 'feels_like': 13.99, 'pressure': 1017, 'humidity': 82, 'dew_point': 11.33, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 235, 'wind_gust': 2.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14.33, 'feels_like': 13.93, 'pressure': 1017, 'humidity': 81, 'dew_point': 11.12, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 233, 'wind_gust': 2.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 14.46, 'feels_like': 14.05, 'pressure': 1017, 'humidity': 80, 'dew_point': 11.06, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 232, 'wind_gust': 2.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 14.61, 'feels_like': 14.19, 'pressure': 1017, 'humidity': 79, 'dew_point': 11.01, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 233, 'wind_gust': 2.03, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 13.61, 'feels_like': 13.12, 'pressure': 1018, 'humidity': 80, 'dew_point': 10.23, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 231, 'wind_gust': 2.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 13.61, 'feels_like': 12.96, 'pressure': 1018, 'humidity': 74, 'dew_point': 9.07, 'uvi': 0.54, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 228, 'wind_gust': 1.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.61, 'feels_like': 16.99, 'pressure': 1018, 'humidity': 60, 'dew_point': 9.76, 'uvi': 2.11, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 62, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 20.61, 'feels_like': 20.16, 'pressure': 1018, 'humidity': 55, 'dew_point': 11.26, 'uvi': 4.98, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 54, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.61, 'feels_like': 21.16, 'pressure': 1018, 'humidity': 51, 'dew_point': 11.05, 'uvi': 8.27, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 47, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 23.61, 'feels_like': 23.28, 'pressure': 1016, 'humidity': 48, 'dew_point': 11.97, 'uvi': 9.89, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 48, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 23.61, 'feels_like': 23.23, 'pressure': 1015, 'humidity': 46, 'dew_point': 11.32, 'uvi': 10.61, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 44, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 24.61, 'feels_like': 24.35, 'pressure': 1014, 'humidity': 47, 'dew_point': 12.56, 'uvi': 9.4, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 48, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 25.61, 'feels_like': 25.58, 'pressure': 1013, 'humidity': 52, 'dew_point': 15.03, 'uvi': 2.74, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 51, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 24.61, 'feels_like': 24.72, 'pressure': 1013, 'humidity': 61, 'dew_point': 16.59, 'uvi': 1.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 36, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 23.61, 'feels_like': 23.83, 'pressure': 1013, 'humidity': 69, 'dew_point': 17.59, 'uvi': 0.58, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 4, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 22.61, 'feels_like': 22.86, 'pressure': 1014, 'humidity': 74, 'dew_point': 17.74, 'uvi': 0.18, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 16, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 22.61, 'feels_like': 23.04, 'pressure': 1015, 'humidity': 81, 'dew_point': 19.18, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 4, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 00:00:00 | 77.000000 | 18.950000 | 20.130000 | 96.000000 | 1017.000000 |  | 19.610000 | 0.000000 | 10000.000000 | 205.000000 | 2.01 | 0.330000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 01:00:00 | 91.000000 | 18.950000 | 20.130000 | 96.000000 | 1018.000000 |  | 19.610000 | 0.000000 | 10000.000000 | 224.000000 | 2.51 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 02:00:00 | 92.000000 | 17.960000 | 19.030000 | 96.000000 | 1019.000000 |  | 18.610000 | 0.000000 | 10000.000000 | 226.000000 | 2.62 | 0.800000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 16.630000 | 17.880000 | 94.000000 | 1019.000000 |  | 17.610000 | 0.000000 | 10000.000000 | 225.000000 | 2.61 | 1.220000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 04:00:00 | 66.000000 | 15.310000 | 16.730000 | 92.000000 | 1019.000000 |  | 16.610000 | 0.000000 | 10000.000000 | 228.000000 | 2.91 | 1.530000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 05:00:00 | 57.000000 | 14.790000 | 16.650000 | 89.000000 | 1019.000000 |  | 16.610000 | 0.000000 | 10000.000000 | 231.000000 | 2.9 | 1.660000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 06:00:00 | 58.000000 | 14.260000 | 16.570000 | 86.000000 | 1018.000000 |  | 16.610000 | 0.000000 | 10000.000000 | 231.000000 | 2.74 | 1.680000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 07:00:00 | 58.000000 | 11.330000 | 13.990000 | 82.000000 | 1017.000000 |  | 14.360000 | 0.000000 | 10000.000000 | 235.000000 | 2.45 | 1.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 08:00:00 | 38.000000 | 11.120000 | 13.930000 | 81.000000 | 1017.000000 |  | 14.330000 | 0.000000 | 10000.000000 | 233.000000 | 2.3 | 1.600000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 09:00:00 | 38.000000 | 11.060000 | 14.050000 | 80.000000 | 1017.000000 |  | 14.460000 | 0.000000 | 10000.000000 | 232.000000 | 2.17 | 1.520000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 10:00:00 | 31.000000 | 11.010000 | 14.190000 | 79.000000 | 1017.000000 |  | 14.610000 | 0.000000 | 10000.000000 | 233.000000 | 2.03 | 1.480000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 11:00:00 | 39.000000 | 10.230000 | 13.120000 | 80.000000 | 1018.000000 |  | 13.610000 | 0.000000 | 10000.000000 | 231.000000 | 2.12 | 1.550000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 12:00:00 | 88.000000 | 9.070000 | 12.960000 | 74.000000 | 1018.000000 |  | 13.610000 | 0.540000 | 10000.000000 | 228.000000 | 1.86 | 1.230000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 13:00:00 | 89.000000 | 9.760000 | 16.990000 | 60.000000 | 1018.000000 |  | 17.610000 | 2.110000 | 10000.000000 | 62.000000 | 0.51 | 0.210000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 14:00:00 | 92.000000 | 11.260000 | 20.160000 | 55.000000 | 1018.000000 |  | 20.610000 | 4.980000 | 10000.000000 | 54.000000 | 0.96 | 1.080000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 15:00:00 | 94.000000 | 11.050000 | 21.160000 | 51.000000 | 1018.000000 |  | 21.610000 | 8.270000 | 10000.000000 | 47.000000 | 1.42 | 1.530000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 16:00:00 | 96.000000 | 11.970000 | 23.280000 | 48.000000 | 1016.000000 |  | 23.610000 | 9.890000 | 10000.000000 | 48.000000 | 1.87 | 1.800000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 17:00:00 | 87.000000 | 11.320000 | 23.230000 | 46.000000 | 1015.000000 |  | 23.610000 | 10.610000 | 10000.000000 | 44.000000 | 1.84 | 2.050000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 12.560000 | 24.350000 | 47.000000 | 1014.000000 |  | 24.610000 | 9.400000 | 10000.000000 | 48.000000 | 1.75 | 1.950000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 15.030000 | 25.580000 | 52.000000 | 1013.000000 |  | 25.610000 | 2.740000 | 10000.000000 | 51.000000 | 1.4 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 16.590000 | 24.720000 | 61.000000 | 1013.000000 |  | 24.610000 | 1.520000 | 10000.000000 | 36.000000 | 1.38 | 1.370000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 17.590000 | 23.830000 | 69.000000 | 1013.000000 |  | 23.610000 | 0.580000 | 10000.000000 | 4.000000 | 1.74 | 0.810000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 17.740000 | 22.860000 | 74.000000 | 1014.000000 |  | 22.610000 | 0.180000 | 10000.000000 | 16.000000 | 1.93 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025030 | "SALAZAR [16025030]" | 7.774583 | -72.830556 | 860.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Salazar | Carepa | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 19.180000 | 23.040000 | 81.000000 | 1015.000000 |  | 22.610000 | 0.000000 | 10000.000000 | 4.000000 | 1.28 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16025030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16025030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16025030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025030_OWM_Windspeed_20220111.png)
