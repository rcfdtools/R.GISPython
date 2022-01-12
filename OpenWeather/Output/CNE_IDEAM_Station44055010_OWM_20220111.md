
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TRES ESQUINAS - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44055010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=0.7375,-75.23611111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=0.7375&lon=-75.23611111)


| Parameter | Value |
|---|---|
| Code | 44055010 |
| Name | TRES ESQUINAS |
| Latitude, ° | 0.7375 |
| Longitude, ° | -75.23611111 |
| Elevation, m | 219 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1971-04-14 00:00:00 |
| Suspension date | NaT |
| State | Caquetá |
| County | Solano |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
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

### (CNE index 2514) Open Weather values for station 44055010 - TRES ESQUINAS

JSON data from API OWM:

```
{'lat': 0.7375, 'lon': -75.2361, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812753, 'sunset': 1641856240, 'temp': 32.53, 'feels_like': 33.46, 'pressure': 1006, 'humidity': 42, 'dew_point': 17.96, 'uvi': 4.27, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 52, 'wind_gust': 2.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.95, 'feels_like': 28.96, 'pressure': 1007, 'humidity': 56, 'dew_point': 18.36, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 35, 'wind_gust': 2.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 27.63, 'feels_like': 28.46, 'pressure': 1009, 'humidity': 55, 'dew_point': 17.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 57, 'wind_gust': 8.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 27.15, 'feels_like': 27.9, 'pressure': 1010, 'humidity': 55, 'dew_point': 17.33, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 52, 'wind_gust': 10.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.68, 'feels_like': 25.87, 'pressure': 1011, 'humidity': 60, 'dew_point': 17.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 44, 'wind_gust': 10.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.4, 'feels_like': 24.59, 'pressure': 1011, 'humidity': 65, 'dew_point': 17.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 43, 'wind_gust': 9.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.6, 'feels_like': 23.79, 'pressure': 1010, 'humidity': 68, 'dew_point': 17.35, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 48, 'wind_gust': 8.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.8, 'feels_like': 23.04, 'pressure': 1010, 'humidity': 73, 'dew_point': 17.71, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 46, 'wind_gust': 7.41, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 22.49, 'feels_like': 22.73, 'pressure': 1009, 'humidity': 74, 'dew_point': 17.63, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 55, 'wind_gust': 5.35, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 22.3, 'feels_like': 22.54, 'pressure': 1009, 'humidity': 75, 'dew_point': 17.66, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 70, 'wind_gust': 1.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.21, 'feels_like': 23.47, 'pressure': 1009, 'humidity': 72, 'dew_point': 17.88, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 54, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.33, 'feels_like': 23.57, 'pressure': 1010, 'humidity': 71, 'dew_point': 17.78, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.01, 'wind_deg': 52, 'wind_gust': 0.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.23, 'feels_like': 23.49, 'pressure': 1010, 'humidity': 72, 'dew_point': 17.9, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 261, 'wind_gust': 0.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.4, 'feels_like': 23.75, 'pressure': 1012, 'humidity': 75, 'dew_point': 18.72, 'uvi': 0.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 256, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.92, 'feels_like': 26.26, 'pressure': 1013, 'humidity': 65, 'dew_point': 18.84, 'uvi': 2.15, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 340, 'wind_gust': 2.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 29.05, 'feels_like': 29.72, 'pressure': 1013, 'humidity': 50, 'dew_point': 17.58, 'uvi': 5.08, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 37, 'wind_gust': 7.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 31.32, 'feels_like': 31.49, 'pressure': 1013, 'humidity': 41, 'dew_point': 16.5, 'uvi': 8.6, 'clouds': 84, 'visibility': 10000, 'wind_speed': 3.14, 'wind_deg': 43, 'wind_gust': 5.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 32.38, 'feels_like': 32.46, 'pressure': 1012, 'humidity': 38, 'dew_point': 16.25, 'uvi': 11.46, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.95, 'wind_deg': 47, 'wind_gust': 5.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.85, 'feels_like': 34.03, 'pressure': 1010, 'humidity': 35, 'dew_point': 16.25, 'uvi': 12.59, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 43, 'wind_gust': 3.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 34.65, 'feels_like': 34.8, 'pressure': 1009, 'humidity': 33, 'dew_point': 16.03, 'uvi': 11.59, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 32, 'wind_gust': 3.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.87, 'feels_like': 35.14, 'pressure': 1007, 'humidity': 33, 'dew_point': 16.22, 'uvi': 7.1, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 30, 'wind_gust': 2.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 32.53, 'feels_like': 33.46, 'pressure': 1006, 'humidity': 42, 'dew_point': 17.96, 'uvi': 4.27, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 52, 'wind_gust': 2.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.92, 'feels_like': 30.19, 'pressure': 1006, 'humidity': 55, 'dew_point': 18.97, 'uvi': 1.86, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 69, 'wind_gust': 3.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.67, 'feels_like': 28.69, 'pressure': 1006, 'humidity': 57, 'dew_point': 18.38, 'uvi': 0.12, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 24, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.64, 'feels_like': 28.39, 'pressure': 1007, 'humidity': 54, 'dew_point': 17.5, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 4, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 18.360000 | 28.960000 | 56.000000 | 1007.000000 |  | 27.950000 | 0.000000 | 10000.000000 | 35.000000 | 2.46 | 1.290000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 17.780000 | 28.460000 | 55.000000 | 1009.000000 |  | 27.630000 | 0.000000 | 10000.000000 | 57.000000 | 8.53 | 1.810000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 17.330000 | 27.900000 | 55.000000 | 1010.000000 |  | 27.150000 | 0.000000 | 10000.000000 | 52.000000 | 10.83 | 2.040000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 17.340000 | 25.870000 | 60.000000 | 1011.000000 |  | 25.680000 | 0.000000 | 10000.000000 | 44.000000 | 10.25 | 1.950000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 17.400000 | 24.590000 | 65.000000 | 1011.000000 |  | 24.400000 | 0.000000 | 10000.000000 | 43.000000 | 9.62 | 1.640000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 05:00:00 | 92.000000 | 17.350000 | 23.790000 | 68.000000 | 1010.000000 |  | 23.600000 | 0.000000 | 10000.000000 | 48.000000 | 8.92 | 1.500000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 06:00:00 | 25.000000 | 17.710000 | 23.040000 | 73.000000 | 1010.000000 |  | 22.800000 | 0.000000 | 10000.000000 | 46.000000 | 7.41 | 1.320000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 07:00:00 | 38.000000 | 17.630000 | 22.730000 | 74.000000 | 1009.000000 |  | 22.490000 | 0.000000 | 10000.000000 | 55.000000 | 5.35 | 1.280000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 08:00:00 | 64.000000 | 17.660000 | 22.540000 | 75.000000 | 1009.000000 |  | 22.300000 | 0.000000 | 10000.000000 | 70.000000 | 1.35 | 0.730000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 09:00:00 | 75.000000 | 17.880000 | 23.470000 | 72.000000 | 1009.000000 |  | 23.210000 | 0.000000 | 10000.000000 | 54.000000 | 0.97 | 0.310000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 10:00:00 | 81.000000 | 17.780000 | 23.570000 | 71.000000 | 1010.000000 |  | 23.330000 | 0.000000 | 10000.000000 | 52.000000 | 0.48 | 0.010000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 11:00:00 | 84.000000 | 17.900000 | 23.490000 | 72.000000 | 1010.000000 |  | 23.230000 | 0.000000 | 10000.000000 | 261.000000 | 0.26 | 0.090000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 18.720000 | 23.750000 | 75.000000 | 1012.000000 |  | 23.400000 | 0.160000 | 10000.000000 | 256.000000 | 0.71 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 18.840000 | 26.260000 | 65.000000 | 1013.000000 |  | 25.920000 | 2.150000 | 10000.000000 | 340.000000 | 2.54 | 0.390000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 17.580000 | 29.720000 | 50.000000 | 1013.000000 |  | 29.050000 | 5.080000 | 10000.000000 | 37.000000 | 7.11 | 2.390000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 15:00:00 | 84.000000 | 16.500000 | 31.490000 | 41.000000 | 1013.000000 |  | 31.320000 | 8.600000 | 10000.000000 | 43.000000 | 5.9 | 3.140000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 16:00:00 | 86.000000 | 16.250000 | 32.460000 | 38.000000 | 1012.000000 |  | 32.380000 | 11.460000 | 10000.000000 | 47.000000 | 5.06 | 2.950000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 17:00:00 | 74.000000 | 16.250000 | 34.030000 | 35.000000 | 1010.000000 |  | 33.850000 | 12.590000 | 10000.000000 | 43.000000 | 3.88 | 2.220000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 18:00:00 | 54.000000 | 16.030000 | 34.800000 | 33.000000 | 1009.000000 |  | 34.650000 | 11.590000 | 10000.000000 | 32.000000 | 3.37 | 2.130000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 19:00:00 | 71.000000 | 16.220000 | 35.140000 | 33.000000 | 1007.000000 |  | 34.870000 | 7.100000 | 10000.000000 | 30.000000 | 2.99 | 1.670000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 20:00:00 | 85.000000 | 17.960000 | 33.460000 | 42.000000 | 1006.000000 |  | 32.530000 | 4.270000 | 10000.000000 | 52.000000 | 2.69 | 1.090000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 18.970000 | 30.190000 | 55.000000 | 1006.000000 |  | 28.920000 | 1.860000 | 10000.000000 | 69.000000 | 3.67 | 1.300000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 22:00:00 | 92.000000 | 18.380000 | 28.690000 | 57.000000 | 1006.000000 |  | 27.670000 | 0.120000 | 10000.000000 | 24.000000 | 1.46 | 0.990000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44055010 | "TRES ESQUINAS" | 0.737500 | -75.236111 | 219.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-04-14 00:00:00 | NaT | Caquetá | Solano | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Caquetá | Río Orteguaza | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 17.500000 | 28.390000 | 54.000000 | 1007.000000 |  | 27.640000 | 0.000000 | 10000.000000 | 4.000000 | 1.06 | 1.060000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station44055010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44055010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44055010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44055010_OWM_Windspeed_20220111.png)
