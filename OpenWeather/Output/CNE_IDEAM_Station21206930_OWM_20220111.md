
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PARAMO GUERRERO  - AUT [21206930] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206930_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.08644444,-74.02216667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.08644444&lon=-74.02216667)


| Parameter | Value |
|---|---|
| Code | 21206930 |
| Name | PARAMO GUERRERO  - AUT [21206930] |
| Latitude, ° | 5.08644444 |
| Longitude, ° | -74.02216667 |
| Elevation, m | 3257 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-11-30 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Zipaquirá |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 328) Open Weather values for station 21206930 - PARAMO GUERRERO  - AUT [21206930]

JSON data from API OWM:

```
{'lat': 5.0864, 'lon': -74.0222, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812882, 'sunset': 1641855528, 'temp': 13.5, 'feels_like': 12.89, 'pressure': 1012, 'humidity': 76, 'dew_point': 9.36, 'uvi': 4.34, 'clouds': 85, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 298, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, 'hourly': [{'dt': 1641772800, 'temp': 8.5, 'feels_like': 8.5, 'pressure': 1016, 'humidity': 95, 'dew_point': 7.75, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 329, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.5, 'feels_like': 9.5, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.89, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 326, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.5, 'feels_like': 8.5, 'pressure': 1018, 'humidity': 95, 'dew_point': 7.75, 'uvi': 0, 'clouds': 93, 'visibility': 9792, 'wind_speed': 0.65, 'wind_deg': 348, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.5, 'feels_like': 8.5, 'pressure': 1019, 'humidity': 95, 'dew_point': 7.75, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 3, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.5, 'feels_like': 8.5, 'pressure': 1019, 'humidity': 95, 'dew_point': 7.75, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 351, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 6.5, 'feels_like': 6.5, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.61, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 49, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 4.5, 'feels_like': 4.5, 'pressure': 1018, 'humidity': 94, 'dew_point': 3.62, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 44, 'wind_gust': 1.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 3.5, 'feels_like': 3.5, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.48, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 36, 'wind_gust': 0.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 3.5, 'feels_like': 3.5, 'pressure': 1016, 'humidity': 93, 'dew_point': 2.48, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 327, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 3.5, 'feels_like': 3.5, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.48, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 315, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.5, 'feels_like': 4.5, 'pressure': 1017, 'humidity': 93, 'dew_point': 3.47, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 352, 'wind_gust': 0.83, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 5.5, 'feels_like': 5.5, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.46, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 67, 'wind_gust': 0.76, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 5.5, 'feels_like': 5.5, 'pressure': 1019, 'humidity': 89, 'dew_point': 3.83, 'uvi': 0.32, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 88, 'wind_gust': 0.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 6.5, 'feels_like': 6.5, 'pressure': 1019, 'humidity': 81, 'dew_point': 3.48, 'uvi': 2.05, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 221, 'wind_gust': 0.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 9.5, 'feels_like': 9.5, 'pressure': 1019, 'humidity': 72, 'dew_point': 4.71, 'uvi': 4.95, 'clouds': 42, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 265, 'wind_gust': 0.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 11.5, 'feels_like': 10.43, 'pressure': 1018, 'humidity': 66, 'dew_point': 5.38, 'uvi': 8.38, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 273, 'wind_gust': 1.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 12.5, 'feels_like': 11.45, 'pressure': 1016, 'humidity': 63, 'dew_point': 5.66, 'uvi': 10.81, 'clouds': 47, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 279, 'wind_gust': 1.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 12.5, 'feels_like': 11.45, 'pressure': 1015, 'humidity': 63, 'dew_point': 5.66, 'uvi': 11.77, 'clouds': 53, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 289, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641837600, 'temp': 13.5, 'feels_like': 12.63, 'pressure': 1014, 'humidity': 66, 'dew_point': 7.28, 'uvi': 10.67, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.4, 'wind_deg': 300, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 13.5, 'feels_like': 12.76, 'pressure': 1013, 'humidity': 71, 'dew_point': 8.35, 'uvi': 7.48, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 300, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641844800, 'temp': 13.5, 'feels_like': 12.89, 'pressure': 1012, 'humidity': 76, 'dew_point': 9.36, 'uvi': 4.34, 'clouds': 85, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 298, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641848400, 'temp': 13.5, 'feels_like': 12.99, 'pressure': 1013, 'humidity': 80, 'dew_point': 10.12, 'uvi': 1.74, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 302, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641852000, 'temp': 12.5, 'feels_like': 12, 'pressure': 1013, 'humidity': 84, 'dew_point': 9.87, 'uvi': 0.39, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 302, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641855600, 'temp': 10.5, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 91, 'dew_point': 9.09, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 314, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 00:00:00 | 77.000000 | 7.750000 | 8.500000 | 95.000000 | 1016.000000 |  | 8.500000 | 0.000000 | 10000.000000 | 329.000000 | 1.2 | 0.640000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 01:00:00 | 91.000000 | 8.890000 | 9.500000 | 96.000000 | 1017.000000 |  | 9.500000 | 0.000000 | 10000.000000 | 326.000000 | 1.15 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 02:00:00 | 93.000000 | 7.750000 | 8.500000 | 95.000000 | 1018.000000 |  | 8.500000 | 0.000000 | 9792.000000 | 348.000000 | 1.07 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 7.750000 | 8.500000 | 95.000000 | 1019.000000 |  | 8.500000 | 0.000000 | 10000.000000 | 3.000000 | 1.04 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 04:00:00 | 92.000000 | 7.750000 | 8.500000 | 95.000000 | 1019.000000 |  | 8.500000 | 0.000000 | 10000.000000 | 351.000000 | 1.01 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | 5.610000 | 6.500000 | 94.000000 | 1018.000000 |  | 6.500000 | 0.000000 | 10000.000000 | 49.000000 | 0.92 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 06:00:00 | 42.000000 | 3.620000 | 4.500000 | 94.000000 | 1018.000000 |  | 4.500000 | 0.000000 | 10000.000000 | 44.000000 | 1.13 | 0.570000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 07:00:00 | 58.000000 | 2.480000 | 3.500000 | 93.000000 | 1017.000000 |  | 3.500000 | 0.000000 | 10000.000000 | 36.000000 | 0.99 | 0.250000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 08:00:00 | 55.000000 | 2.480000 | 3.500000 | 93.000000 | 1016.000000 |  | 3.500000 | 0.000000 | 10000.000000 | 327.000000 | 1.07 | 0.160000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 09:00:00 | 54.000000 | 2.480000 | 3.500000 | 93.000000 | 1017.000000 |  | 3.500000 | 0.000000 | 10000.000000 | 315.000000 | 1.05 | 0.290000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 10:00:00 | 49.000000 | 3.470000 | 4.500000 | 93.000000 | 1017.000000 |  | 4.500000 | 0.000000 | 10000.000000 | 352.000000 | 0.83 | 0.140000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 11:00:00 | 48.000000 | 4.460000 | 5.500000 | 93.000000 | 1018.000000 |  | 5.500000 | 0.000000 | 10000.000000 | 67.000000 | 0.76 | 0.250000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 12:00:00 | 38.000000 | 3.830000 | 5.500000 | 89.000000 | 1019.000000 |  | 5.500000 | 0.320000 | 10000.000000 | 88.000000 | 0.63 | 0.550000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 13:00:00 | 47.000000 | 3.480000 | 6.500000 | 81.000000 | 1019.000000 |  | 6.500000 | 2.050000 | 10000.000000 | 221.000000 | 0.6 | 0.320000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 14:00:00 | 42.000000 | 4.710000 | 9.500000 | 72.000000 | 1019.000000 |  | 9.500000 | 4.950000 | 10000.000000 | 265.000000 | 0.91 | 0.940000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 15:00:00 | 41.000000 | 5.380000 | 10.430000 | 66.000000 | 1018.000000 |  | 11.500000 | 8.380000 | 10000.000000 | 273.000000 | 1.77 | 1.670000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 16:00:00 | 47.000000 | 5.660000 | 11.450000 | 63.000000 | 1016.000000 |  | 12.500000 | 10.810000 | 10000.000000 | 279.000000 | 1.99 | 2.040000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 17:00:00 | 53.000000 | 5.660000 | 11.450000 | 63.000000 | 1015.000000 | 0.16 | 12.500000 | 11.770000 | 10000.000000 | 289.000000 | 1.82 | 2.310000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 18:00:00 | 77.000000 | 7.280000 | 12.630000 | 66.000000 | 1014.000000 |  | 13.500000 | 10.670000 | 10000.000000 | 300.000000 | 1.63 | 2.400000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 19:00:00 | 91.000000 | 8.350000 | 12.760000 | 71.000000 | 1013.000000 | 0.25 | 13.500000 | 7.480000 | 10000.000000 | 300.000000 | 1.85 | 2.240000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 20:00:00 | 85.000000 | 9.360000 | 12.890000 | 76.000000 | 1012.000000 | 0.38 | 13.500000 | 4.340000 | 10000.000000 | 298.000000 | 1.73 | 2.110000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 21:00:00 | 86.000000 | 10.120000 | 12.990000 | 80.000000 | 1013.000000 | 0.33 | 13.500000 | 1.740000 | 10000.000000 | 302.000000 | 1.46 | 1.700000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 22:00:00 | 84.000000 | 9.870000 | 12.000000 | 84.000000 | 1013.000000 | 0.14 | 12.500000 | 0.390000 | 10000.000000 | 302.000000 | 1.58 | 1.510000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206930 | "PARAMO GUERRERO  - AUT [21206930]" | 5.086444 | -74.022167 | 3257.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-30 19:00:00 | NaT | Cundinamarca | Zipaquirá | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 9.090000 | 9.980000 | 91.000000 | 1015.000000 | 0.22 | 10.500000 | 0.000000 | 10000.000000 | 314.000000 | 1.11 | 1.050000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station21206930_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206930_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206930_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206930_OWM_Windspeed_20220111.png)
