
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL PARAISO - AUT [52055220] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055220_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.07061111,-77.63688889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.07061111&lon=-77.63688889)


| Parameter | Value |
|---|---|
| Code | 52055220 |
| Name | EL PARAISO - AUT [52055220] |
| Latitude, ° | 1.07061111 |
| Longitude, ° | -77.63688889 |
| Elevation, m | 3120 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-03-01 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Túquerres |
| Stream | Guaitara |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Guáitara |

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

### (CNE index 3) Open Weather values for station 52055220 - EL PARAISO - AUT [52055220]

JSON data from API OWM:

```
{'lat': 1.0706, 'lon': -77.6369, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813361, 'sunset': 1641856784, 'temp': 13.2, 'feels_like': 12.8, 'pressure': 1014, 'humidity': 85, 'dew_point': 10.74, 'uvi': 4.32, 'clouds': 91, 'visibility': 8701, 'wind_speed': 2.69, 'wind_deg': 323, 'wind_gust': 2.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.78}}, 'hourly': [{'dt': 1641772800, 'temp': 11.75, 'feels_like': 11.41, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.66, 'uvi': 0, 'clouds': 100, 'visibility': 8840, 'wind_speed': 1.32, 'wind_deg': 336, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 8.79, 'feels_like': 8.79, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.88, 'uvi': 0, 'clouds': 100, 'visibility': 8941, 'wind_speed': 0.86, 'wind_deg': 349, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.37, 'feels_like': 8.37, 'pressure': 1019, 'humidity': 94, 'dew_point': 7.46, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 4, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.3, 'feels_like': 8.3, 'pressure': 1020, 'humidity': 94, 'dew_point': 7.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 98, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.26, 'feels_like': 8.26, 'pressure': 1019, 'humidity': 92, 'dew_point': 7.04, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 157, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 7.94, 'feels_like': 7.94, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.72, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 213, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 7.67, 'feels_like': 7.67, 'pressure': 1018, 'humidity': 92, 'dew_point': 6.45, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 254, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 7.38, 'feels_like': 7.38, 'pressure': 1018, 'humidity': 92, 'dew_point': 6.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 253, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 7.21, 'feels_like': 7.21, 'pressure': 1017, 'humidity': 92, 'dew_point': 6, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 250, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.18, 'feels_like': 7.18, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 283, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 6.85, 'feels_like': 6.85, 'pressure': 1018, 'humidity': 93, 'dew_point': 5.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 238, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 5.75, 'feels_like': 5.75, 'pressure': 1018, 'humidity': 92, 'dew_point': 4.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 258, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 6.75, 'feels_like': 6.75, 'pressure': 1019, 'humidity': 91, 'dew_point': 5.39, 'uvi': 0.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 215, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 8.58, 'feels_like': 8.58, 'pressure': 1019, 'humidity': 85, 'dew_point': 6.2, 'uvi': 1.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 302, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 11.2, 'feels_like': 10.46, 'pressure': 1019, 'humidity': 80, 'dew_point': 7.88, 'uvi': 4.46, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 340, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 13.58, 'feels_like': 13, 'pressure': 1018, 'humidity': 77, 'dew_point': 9.63, 'uvi': 7.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.21, 'wind_deg': 346, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641830400, 'temp': 15.2, 'feels_like': 14.84, 'pressure': 1017, 'humidity': 79, 'dew_point': 11.59, 'uvi': 8.79, 'clouds': 100, 'visibility': 9528, 'wind_speed': 2.75, 'wind_deg': 340, 'wind_gust': 2.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641834000, 'temp': 15.33, 'feels_like': 15.11, 'pressure': 1017, 'humidity': 84, 'dew_point': 12.64, 'uvi': 9.96, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 338, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641837600, 'temp': 16.33, 'feels_like': 16.24, 'pressure': 1016, 'humidity': 85, 'dew_point': 13.81, 'uvi': 9.45, 'clouds': 80, 'visibility': 4041, 'wind_speed': 2.61, 'wind_deg': 332, 'wind_gust': 2.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641841200, 'temp': 16.2, 'feels_like': 16.12, 'pressure': 1015, 'humidity': 86, 'dew_point': 13.86, 'uvi': 6.88, 'clouds': 100, 'visibility': 5001, 'wind_speed': 2.7, 'wind_deg': 323, 'wind_gust': 2.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}, {'dt': 1641844800, 'temp': 13.2, 'feels_like': 12.8, 'pressure': 1014, 'humidity': 85, 'dew_point': 10.74, 'uvi': 4.32, 'clouds': 91, 'visibility': 8701, 'wind_speed': 2.69, 'wind_deg': 323, 'wind_gust': 2.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.78}}, {'dt': 1641848400, 'temp': 11.58, 'feels_like': 11.09, 'pressure': 1014, 'humidity': 88, 'dew_point': 9.66, 'uvi': 1.98, 'clouds': 94, 'visibility': 6748, 'wind_speed': 2.57, 'wind_deg': 329, 'wind_gust': 2.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641852000, 'temp': 10.95, 'feels_like': 10.48, 'pressure': 1015, 'humidity': 91, 'dew_point': 9.54, 'uvi': 0.68, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 328, 'wind_gust': 2.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641855600, 'temp': 10.75, 'feels_like': 10.36, 'pressure': 1016, 'humidity': 95, 'dew_point': 9.98, 'uvi': 0, 'clouds': 96, 'visibility': 8702, 'wind_speed': 1.78, 'wind_deg': 322, 'wind_gust': 2.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 10.660000 | 11.410000 | 93.000000 | 1017.000000 |  | 11.750000 | 0.000000 | 8840.000000 | 336.000000 | 1.57 | 1.320000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 7.880000 | 8.790000 | 94.000000 | 1018.000000 |  | 8.790000 | 0.000000 | 8941.000000 | 349.000000 | 1.09 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 7.460000 | 8.370000 | 94.000000 | 1019.000000 |  | 8.370000 | 0.000000 | 10000.000000 | 4.000000 | 0.75 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 7.390000 | 8.300000 | 94.000000 | 1020.000000 |  | 8.300000 | 0.000000 | 10000.000000 | 98.000000 | 0.74 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 7.040000 | 8.260000 | 92.000000 | 1019.000000 |  | 8.260000 | 0.000000 | 10000.000000 | 157.000000 | 0.65 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 6.720000 | 7.940000 | 92.000000 | 1019.000000 |  | 7.940000 | 0.000000 | 10000.000000 | 213.000000 | 0.68 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 6.450000 | 7.670000 | 92.000000 | 1018.000000 |  | 7.670000 | 0.000000 | 10000.000000 | 254.000000 | 0.95 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 6.170000 | 7.380000 | 92.000000 | 1018.000000 |  | 7.380000 | 0.000000 | 10000.000000 | 253.000000 | 0.77 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 6.000000 | 7.210000 | 92.000000 | 1017.000000 |  | 7.210000 | 0.000000 | 10000.000000 | 250.000000 | 0.79 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 5.970000 | 7.180000 | 92.000000 | 1017.000000 |  | 7.180000 | 0.000000 | 10000.000000 | 283.000000 | 1.05 | 0.880000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 5.800000 | 6.850000 | 93.000000 | 1018.000000 |  | 6.850000 | 0.000000 | 10000.000000 | 238.000000 | 0.67 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 4.550000 | 5.750000 | 92.000000 | 1018.000000 |  | 5.750000 | 0.000000 | 10000.000000 | 258.000000 | 0.77 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 5.390000 | 6.750000 | 91.000000 | 1019.000000 |  | 6.750000 | 0.220000 | 10000.000000 | 215.000000 | 0.76 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 6.200000 | 8.580000 | 85.000000 | 1019.000000 |  | 8.580000 | 1.720000 | 10000.000000 | 302.000000 | 0.85 | 0.740000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 7.880000 | 10.460000 | 80.000000 | 1019.000000 |  | 11.200000 | 4.460000 | 10000.000000 | 340.000000 | 1 | 1.340000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 9.630000 | 13.000000 | 77.000000 | 1018.000000 | 0.26 | 13.580000 | 7.910000 | 10000.000000 | 346.000000 | 1.74 | 2.210000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 11.590000 | 14.840000 | 79.000000 | 1017.000000 | 0.67 | 15.200000 | 8.790000 | 9528.000000 | 340.000000 | 2.22 | 2.750000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 12.640000 | 15.110000 | 84.000000 | 1017.000000 | 0.73 | 15.330000 | 9.960000 | 10000.000000 | 338.000000 | 2.24 | 2.670000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 18:00:00 | 80.000000 | 13.810000 | 16.240000 | 85.000000 | 1016.000000 | 0.61 | 16.330000 | 9.450000 | 4041.000000 | 332.000000 | 2.46 | 2.610000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.860000 | 16.120000 | 86.000000 | 1015.000000 | 0.83 | 16.200000 | 6.880000 | 5001.000000 | 323.000000 | 2.73 | 2.700000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 20:00:00 | 91.000000 | 10.740000 | 12.800000 | 85.000000 | 1014.000000 | 0.78 | 13.200000 | 4.320000 | 8701.000000 | 323.000000 | 2.72 | 2.690000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 9.660000 | 11.090000 | 88.000000 | 1014.000000 | 0.6 | 11.580000 | 1.980000 | 6748.000000 | 329.000000 | 2.55 | 2.570000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 9.540000 | 10.480000 | 91.000000 | 1015.000000 | 0.52 | 10.950000 | 0.680000 | 10000.000000 | 328.000000 | 2.4 | 2.190000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055220 | "EL PARAISO - AUT [52055220]" | 1.070611 | -77.636889 | 3120.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Túquerres | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 9.980000 | 10.360000 | 95.000000 | 1016.000000 | 0.4 | 10.750000 | 0.000000 | 8702.000000 | 322.000000 | 2.25 | 1.780000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055220_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055220_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055220_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055220_OWM_Windspeed_20220111.png)
