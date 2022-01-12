
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PAQUILO - AUT [21195170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21195170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.99361111,-74.39805556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.99361111&lon=-74.39805556)


| Parameter | Value |
|---|---|
| Code | 21195170 |
| Name | PAQUILO - AUT [21195170] |
| Latitude, ° | 3.99361111 |
| Longitude, ° | -74.39805556 |
| Elevation, m | 2957 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-23 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Cabrera (Cundinamarca) |
| Stream | Cuinde |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Sumapaz |

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

### (CNE index 73) Open Weather values for station 21195170 - PAQUILO - AUT [21195170]

JSON data from API OWM:

```
{'lat': 3.9936, 'lon': -74.3981, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812866, 'sunset': 1641855724, 'temp': 12.26, 'feels_like': 11.71, 'pressure': 1013, 'humidity': 83, 'dew_point': 9.46, 'uvi': 3.07, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 305, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, 'hourly': [{'dt': 1641772800, 'temp': 9.75, 'feels_like': 9.75, 'pressure': 1016, 'humidity': 89, 'dew_point': 8.03, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 43, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.64, 'feels_like': 9.64, 'pressure': 1017, 'humidity': 87, 'dew_point': 7.58, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 4, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1018, 'humidity': 89, 'dew_point': 7.19, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 42, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.52, 'feels_like': 8.52, 'pressure': 1019, 'humidity': 90, 'dew_point': 6.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 161, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 7.95, 'feels_like': 7.95, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.57, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 131, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641790800, 'temp': 7.57, 'feels_like': 7.57, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.2, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 114, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 6.95, 'feels_like': 6.95, 'pressure': 1018, 'humidity': 90, 'dew_point': 5.43, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 106, 'wind_gust': 1.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 7.08, 'feels_like': 7.08, 'pressure': 1017, 'humidity': 89, 'dew_point': 5.39, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 99, 'wind_gust': 1.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 7.09, 'feels_like': 7.09, 'pressure': 1016, 'humidity': 89, 'dew_point': 5.4, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 101, 'wind_gust': 1.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.17, 'feels_like': 7.17, 'pressure': 1016, 'humidity': 90, 'dew_point': 5.64, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 91, 'wind_gust': 1.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1017, 'humidity': 89, 'dew_point': 5.69, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 102, 'wind_gust': 1.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 7.1, 'feels_like': 7.1, 'pressure': 1018, 'humidity': 88, 'dew_point': 5.25, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 127, 'wind_gust': 1.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.17, 'feels_like': 8.17, 'pressure': 1018, 'humidity': 87, 'dew_point': 6.14, 'uvi': 0.55, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 106, 'wind_gust': 1.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 10.19, 'feels_like': 9.3, 'pressure': 1019, 'humidity': 78, 'dew_point': 6.53, 'uvi': 1.23, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 307, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.58, 'feels_like': 9.73, 'pressure': 1019, 'humidity': 78, 'dew_point': 6.91, 'uvi': 2.92, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 312, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 11.48, 'feels_like': 10.69, 'pressure': 1019, 'humidity': 77, 'dew_point': 7.59, 'uvi': 4.91, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 312, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 12.32, 'feels_like': 11.57, 'pressure': 1018, 'humidity': 75, 'dew_point': 8.02, 'uvi': 10.61, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 302, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 13.69, 'feels_like': 13.02, 'pressure': 1016, 'humidity': 73, 'dew_point': 8.94, 'uvi': 11.54, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 302, 'wind_gust': 2.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 13.37, 'feels_like': 12.77, 'pressure': 1015, 'humidity': 77, 'dew_point': 9.43, 'uvi': 10.48, 'clouds': 83, 'visibility': 10000, 'wind_speed': 2.59, 'wind_deg': 304, 'wind_gust': 2.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641841200, 'temp': 12.32, 'feels_like': 11.8, 'pressure': 1014, 'humidity': 84, 'dew_point': 9.7, 'uvi': 5.26, 'clouds': 91, 'visibility': 9097, 'wind_speed': 2.14, 'wind_deg': 302, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641844800, 'temp': 12.26, 'feels_like': 11.71, 'pressure': 1013, 'humidity': 83, 'dew_point': 9.46, 'uvi': 3.07, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 305, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641848400, 'temp': 11.75, 'feels_like': 11.12, 'pressure': 1013, 'humidity': 82, 'dew_point': 8.78, 'uvi': 1.25, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 310, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641852000, 'temp': 10.57, 'feels_like': 10.03, 'pressure': 1014, 'humidity': 90, 'dew_point': 9, 'uvi': 0.24, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 314, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641855600, 'temp': 9.92, 'feels_like': 9.92, 'pressure': 1015, 'humidity': 91, 'dew_point': 8.52, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 30, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 00:00:00 | 92.000000 | 8.030000 | 9.750000 | 89.000000 | 1016.000000 |  | 9.750000 | 0.000000 | 10000.000000 | 43.000000 | 0.95 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 7.580000 | 9.640000 | 87.000000 | 1017.000000 |  | 9.640000 | 0.000000 | 10000.000000 | 4.000000 | 0.96 | 0.890000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 7.190000 | 8.900000 | 89.000000 | 1018.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 42.000000 | 0.79 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 6.980000 | 8.520000 | 90.000000 | 1019.000000 |  | 8.520000 | 0.000000 | 10000.000000 | 161.000000 | 0.95 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 6.570000 | 7.950000 | 91.000000 | 1019.000000 | 0.11 | 7.950000 | 0.000000 | 10000.000000 | 131.000000 | 1.23 | 0.730000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 05:00:00 | 98.000000 | 6.200000 | 7.570000 | 91.000000 | 1018.000000 |  | 7.570000 | 0.000000 | 10000.000000 | 114.000000 | 1.45 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 06:00:00 | 54.000000 | 5.430000 | 6.950000 | 90.000000 | 1018.000000 |  | 6.950000 | 0.000000 | 10000.000000 | 106.000000 | 1.65 | 1.140000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 07:00:00 | 55.000000 | 5.390000 | 7.080000 | 89.000000 | 1017.000000 |  | 7.080000 | 0.000000 | 10000.000000 | 99.000000 | 1.54 | 0.920000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 08:00:00 | 72.000000 | 5.400000 | 7.090000 | 89.000000 | 1016.000000 |  | 7.090000 | 0.000000 | 10000.000000 | 101.000000 | 1.59 | 0.790000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 09:00:00 | 73.000000 | 5.640000 | 7.170000 | 90.000000 | 1016.000000 |  | 7.170000 | 0.000000 | 10000.000000 | 91.000000 | 1.81 | 0.580000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 10:00:00 | 67.000000 | 5.690000 | 7.380000 | 89.000000 | 1017.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 102.000000 | 1.81 | 0.290000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 11:00:00 | 65.000000 | 5.250000 | 7.100000 | 88.000000 | 1018.000000 |  | 7.100000 | 0.000000 | 10000.000000 | 127.000000 | 1.92 | 0.740000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 6.140000 | 8.170000 | 87.000000 | 1018.000000 |  | 8.170000 | 0.550000 | 10000.000000 | 106.000000 | 1.86 | 0.550000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 13:00:00 | 89.000000 | 6.530000 | 9.300000 | 78.000000 | 1019.000000 |  | 10.190000 | 1.230000 | 10000.000000 | 307.000000 | 1.45 | 1.120000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 6.910000 | 9.730000 | 78.000000 | 1019.000000 |  | 10.580000 | 2.920000 | 10000.000000 | 312.000000 | 1.6 | 1.420000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 15:00:00 | 93.000000 | 7.590000 | 10.690000 | 77.000000 | 1019.000000 |  | 11.480000 | 4.910000 | 10000.000000 | 312.000000 | 1.65 | 1.530000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 16:00:00 | 94.000000 | 8.020000 | 11.570000 | 75.000000 | 1018.000000 | 0.12 | 12.320000 | 10.610000 | 10000.000000 | 302.000000 | 1.92 | 2.130000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 17:00:00 | 89.000000 | 8.940000 | 13.020000 | 73.000000 | 1016.000000 |  | 13.690000 | 11.540000 | 10000.000000 | 302.000000 | 2.28 | 2.650000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 9.430000 | 12.770000 | 77.000000 | 1015.000000 | 0.31 | 13.370000 | 10.480000 | 10000.000000 | 304.000000 | 2.16 | 2.590000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 19:00:00 | 91.000000 | 9.700000 | 11.800000 | 84.000000 | 1014.000000 | 0.5 | 12.320000 | 5.260000 | 9097.000000 | 302.000000 | 1.78 | 2.140000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 20:00:00 | 92.000000 | 9.460000 | 11.710000 | 83.000000 | 1013.000000 | 0.36 | 12.260000 | 3.070000 | 10000.000000 | 305.000000 | 1.44 | 1.720000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 21:00:00 | 92.000000 | 8.780000 | 11.120000 | 82.000000 | 1013.000000 | 0.19 | 11.750000 | 1.250000 | 10000.000000 | 310.000000 | 1.31 | 1.440000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 22:00:00 | 93.000000 | 9.000000 | 10.030000 | 90.000000 | 1014.000000 | 0.21 | 10.570000 | 0.240000 | 10000.000000 | 314.000000 | 0.94 | 0.830000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195170 | "PAQUILO - AUT [21195170]" | 3.993611 | -74.398056 | 2957.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-23 00:00:00 | NaT | Cundinamarca | Cabrera (Cundinamarca) | Cuinde | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 8.520000 | 9.920000 | 91.000000 | 1015.000000 |  | 9.920000 | 0.000000 | 10000.000000 | 30.000000 | 0.88 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21195170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21195170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21195170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195170_OWM_Windspeed_20220111.png)
