
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TAMA PARQUE NAL [16015090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16015090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.42444444,-72.44211111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.42444444&lon=-72.44211111)


| Parameter | Value |
|---|---|
| Code | 16015090 |
| Name | TAMA PARQUE NAL [16015090] |
| Latitude, ° | 7.42444444 |
| Longitude, ° | -72.44211111 |
| Elevation, m | 2500 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1989-04-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Herrán |
| Stream | Tachira |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Pamplonita |

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

### (CNE index 2924) Open Weather values for station 16015090 - TAMA PARQUE NAL [16015090]

JSON data from API OWM:

```
{'lat': 7.4244, 'lon': -72.4421, 'timezone': 'America/Caracas', 'timezone_offset': -14400, 'current': {'dt': 1641843725, 'sunrise': 1641812731, 'sunset': 1641854920, 'temp': 14.94, 'feels_like': 14.29, 'pressure': 1014, 'humidity': 69, 'dew_point': 9.31, 'uvi': 2.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 22, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 9.94, 'feels_like': 9.94, 'pressure': 1018, 'humidity': 97, 'dew_point': 9.49, 'uvi': 0, 'clouds': 85, 'visibility': 4555, 'wind_speed': 1.01, 'wind_deg': 330, 'wind_gust': 2.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641776400, 'temp': 9.94, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 97, 'dew_point': 9.49, 'uvi': 0, 'clouds': 97, 'visibility': 4462, 'wind_speed': 0.9, 'wind_deg': 321, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641780000, 'temp': 8.94, 'feels_like': 8.94, 'pressure': 1019, 'humidity': 96, 'dew_point': 8.34, 'uvi': 0, 'clouds': 97, 'visibility': 8022, 'wind_speed': 1.01, 'wind_deg': 305, 'wind_gust': 1.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 7.94, 'feels_like': 7.94, 'pressure': 1019, 'humidity': 96, 'dew_point': 7.34, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 285, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 6.94, 'feels_like': 6.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 6.2, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 268, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 6.94, 'feels_like': 6.94, 'pressure': 1019, 'humidity': 95, 'dew_point': 6.2, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 240, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 6.94, 'feels_like': 6.94, 'pressure': 1019, 'humidity': 94, 'dew_point': 6.04, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 217, 'wind_gust': 1.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 6.87, 'feels_like': 6.87, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.97, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 203, 'wind_gust': 1.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 6.74, 'feels_like': 6.74, 'pressure': 1017, 'humidity': 94, 'dew_point': 5.84, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 189, 'wind_gust': 1.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 6.59, 'feels_like': 6.59, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.54, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 187, 'wind_gust': 1.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.94, 'feels_like': 4.94, 'pressure': 1018, 'humidity': 93, 'dew_point': 3.9, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 177, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.94, 'feels_like': 3.94, 'pressure': 1018, 'humidity': 93, 'dew_point': 2.91, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 169, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 3.94, 'feels_like': 3.94, 'pressure': 1019, 'humidity': 91, 'dew_point': 2.61, 'uvi': 0.43, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 162, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 7.94, 'feels_like': 7.94, 'pressure': 1020, 'humidity': 85, 'dew_point': 5.58, 'uvi': 1.51, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 116, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.94, 'feels_like': 10.15, 'pressure': 1020, 'humidity': 79, 'dew_point': 7.44, 'uvi': 3.49, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 95, 'wind_gust': 1.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 11.94, 'feels_like': 11.07, 'pressure': 1019, 'humidity': 72, 'dew_point': 7.06, 'uvi': 5.74, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 79, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 13.94, 'feels_like': 13.14, 'pressure': 1018, 'humidity': 67, 'dew_point': 7.92, 'uvi': 5.35, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 58, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 13.94, 'feels_like': 13.17, 'pressure': 1017, 'humidity': 68, 'dew_point': 8.14, 'uvi': 5.69, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 54, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 14.94, 'feels_like': 14.29, 'pressure': 1017, 'humidity': 69, 'dew_point': 9.31, 'uvi': 5.02, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 52, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 15.94, 'feels_like': 15.34, 'pressure': 1015, 'humidity': 67, 'dew_point': 9.83, 'uvi': 4.4, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 38, 'wind_gust': 1.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 14.94, 'feels_like': 14.29, 'pressure': 1014, 'humidity': 69, 'dew_point': 9.31, 'uvi': 2.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 22, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 13.94, 'feels_like': 13.35, 'pressure': 1015, 'humidity': 75, 'dew_point': 9.59, 'uvi': 0.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 19, 'wind_gust': 2.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 12.94, 'feels_like': 12.4, 'pressure': 1015, 'humidity': 81, 'dew_point': 9.76, 'uvi': 0.1, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 18, 'wind_gust': 2.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 12.94, 'feels_like': 12.61, 'pressure': 1016, 'humidity': 89, 'dew_point': 11.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 351, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 00:00:00 | 85.000000 | 9.490000 | 9.940000 | 97.000000 | 1018.000000 | 0.14 | 9.940000 | 0.000000 | 4555.000000 | 330.000000 | 2.12 | 1.010000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 01:00:00 | 97.000000 | 9.490000 | 9.940000 | 97.000000 | 1019.000000 | 0.13 | 9.940000 | 0.000000 | 4462.000000 | 321.000000 | 2.01 | 0.900000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 02:00:00 | 97.000000 | 8.340000 | 8.940000 | 96.000000 | 1019.000000 |  | 8.940000 | 0.000000 | 8022.000000 | 305.000000 | 1.96 | 1.010000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 03:00:00 | 94.000000 | 7.340000 | 7.940000 | 96.000000 | 1019.000000 |  | 7.940000 | 0.000000 | 10000.000000 | 285.000000 | 1.95 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 04:00:00 | 90.000000 | 6.200000 | 6.940000 | 95.000000 | 1019.000000 |  | 6.940000 | 0.000000 | 10000.000000 | 268.000000 | 1.88 | 1.000000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 05:00:00 | 88.000000 | 6.200000 | 6.940000 | 95.000000 | 1019.000000 |  | 6.940000 | 0.000000 | 10000.000000 | 240.000000 | 1.44 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 06:00:00 | 52.000000 | 6.040000 | 6.940000 | 94.000000 | 1019.000000 |  | 6.940000 | 0.000000 | 10000.000000 | 217.000000 | 1.49 | 1.080000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 07:00:00 | 69.000000 | 5.970000 | 6.870000 | 94.000000 | 1018.000000 |  | 6.870000 | 0.000000 | 10000.000000 | 203.000000 | 1.78 | 1.180000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 08:00:00 | 63.000000 | 5.840000 | 6.740000 | 94.000000 | 1017.000000 |  | 6.740000 | 0.000000 | 10000.000000 | 189.000000 | 1.62 | 1.190000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 09:00:00 | 61.000000 | 5.540000 | 6.590000 | 93.000000 | 1017.000000 |  | 6.590000 | 0.000000 | 10000.000000 | 187.000000 | 1.52 | 1.250000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 10:00:00 | 59.000000 | 3.900000 | 4.940000 | 93.000000 | 1018.000000 |  | 4.940000 | 0.000000 | 10000.000000 | 177.000000 | 1.21 | 1.160000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 11:00:00 | 64.000000 | 2.910000 | 3.940000 | 93.000000 | 1018.000000 |  | 3.940000 | 0.000000 | 10000.000000 | 169.000000 | 1.34 | 1.130000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 12:00:00 | 73.000000 | 2.610000 | 3.940000 | 91.000000 | 1019.000000 |  | 3.940000 | 0.430000 | 10000.000000 | 162.000000 | 1.75 | 1.000000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 13:00:00 | 91.000000 | 5.580000 | 7.940000 | 85.000000 | 1020.000000 |  | 7.940000 | 1.510000 | 10000.000000 | 116.000000 | 1.58 | 0.820000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 14:00:00 | 96.000000 | 7.440000 | 10.150000 | 79.000000 | 1020.000000 |  | 10.940000 | 3.490000 | 10000.000000 | 95.000000 | 1.52 | 0.970000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 15:00:00 | 97.000000 | 7.060000 | 11.070000 | 72.000000 | 1019.000000 |  | 11.940000 | 5.740000 | 10000.000000 | 79.000000 | 1.24 | 1.160000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 16:00:00 | 98.000000 | 7.920000 | 13.140000 | 67.000000 | 1018.000000 |  | 13.940000 | 5.350000 | 10000.000000 | 58.000000 | 1.43 | 1.530000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 17:00:00 | 98.000000 | 8.140000 | 13.170000 | 68.000000 | 1017.000000 |  | 13.940000 | 5.690000 | 10000.000000 | 54.000000 | 1.67 | 1.750000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 18:00:00 | 98.000000 | 9.310000 | 14.290000 | 69.000000 | 1017.000000 |  | 14.940000 | 5.020000 | 10000.000000 | 52.000000 | 1.43 | 1.400000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 19:00:00 | 100.000000 | 9.830000 | 15.340000 | 67.000000 | 1015.000000 |  | 15.940000 | 4.400000 | 10000.000000 | 38.000000 | 1.53 | 1.340000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 20:00:00 | 100.000000 | 9.310000 | 14.290000 | 69.000000 | 1014.000000 |  | 14.940000 | 2.420000 | 10000.000000 | 22.000000 | 1.72 | 1.240000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 21:00:00 | 100.000000 | 9.590000 | 13.350000 | 75.000000 | 1015.000000 |  | 13.940000 | 0.910000 | 10000.000000 | 19.000000 | 2.02 | 1.100000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 22:00:00 | 100.000000 | 9.760000 | 12.400000 | 81.000000 | 1015.000000 |  | 12.940000 | 0.100000 | 10000.000000 | 18.000000 | 2.41 | 1.050000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015090 | "TAMA PARQUE NAL [16015090]" | 7.424444 | -72.442111 | 2500.000000 | Climática Principal | Convencional | Activa | 1989-04-15 00:00:00 | NaT | Norte de Santander | Herrán | Tachira | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Caracas | 2022-01-10 23:00:00 | 100.000000 | 11.170000 | 12.610000 | 89.000000 | 1016.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 351.000000 | 1.81 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16015090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16015090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16015090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015090_OWM_Windspeed_20220111.png)
