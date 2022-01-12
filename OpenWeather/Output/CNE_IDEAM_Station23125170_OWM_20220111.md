
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN CAYETANO - AUT [23125170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23125170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.33333333,-74.01666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.33333333&lon=-74.01666667)


| Parameter | Value |
|---|---|
| Code | 23125170 |
| Name | SAN CAYETANO - AUT [23125170] |
| Latitude, ° | 5.33333333 |
| Longitude, ° | -74.01666667 |
| Elevation, m | 2807 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-01 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | San Cayetano (Cundinamarca) |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Carare (Minero) |

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

### (CNE index 84) Open Weather values for station 23125170 - SAN CAYETANO - AUT [23125170]

JSON data from API OWM:

```
{'lat': 5.3333, 'lon': -74.0167, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812905, 'sunset': 1641855502, 'temp': 13.26, 'feels_like': 12.94, 'pressure': 1013, 'humidity': 88, 'dew_point': 11.32, 'uvi': 4.34, 'clouds': 89, 'visibility': 6119, 'wind_speed': 1.81, 'wind_deg': 310, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, 'hourly': [{'dt': 1641772800, 'temp': 10.03, 'feels_like': 9.65, 'pressure': 1016, 'humidity': 98, 'dew_point': 9.73, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 83, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.51, 'feels_like': 9.51, 'pressure': 1017, 'humidity': 97, 'dew_point': 9.06, 'uvi': 0, 'clouds': 75, 'visibility': 9914, 'wind_speed': 0.5, 'wind_deg': 104, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641780000, 'temp': 8.84, 'feels_like': 8.84, 'pressure': 1018, 'humidity': 97, 'dew_point': 8.39, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 97, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.51, 'feels_like': 8.51, 'pressure': 1019, 'humidity': 97, 'dew_point': 8.06, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 110, 'wind_gust': 0.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1019, 'humidity': 97, 'dew_point': 7.69, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 129, 'wind_gust': 0.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 7.77, 'feels_like': 7.11, 'pressure': 1018, 'humidity': 97, 'dew_point': 7.32, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 129, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 7.61, 'feels_like': 6.97, 'pressure': 1017, 'humidity': 95, 'dew_point': 6.86, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 124, 'wind_gust': 1.08, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 7.19, 'feels_like': 6.57, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.44, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 124, 'wind_gust': 1.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 6.9, 'feels_like': 6.32, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.16, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 123, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 6.68, 'feels_like': 6.68, 'pressure': 1016, 'humidity': 95, 'dew_point': 5.94, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 130, 'wind_gust': 1.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 6.57, 'feels_like': 6.57, 'pressure': 1017, 'humidity': 96, 'dew_point': 5.98, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 123, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 6.91, 'feels_like': 6.91, 'pressure': 1018, 'humidity': 96, 'dew_point': 6.32, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 123, 'wind_gust': 0.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.2, 'feels_like': 8.2, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.14, 'uvi': 0.32, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 123, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 11.26, 'feels_like': 10.63, 'pressure': 1018, 'humidity': 84, 'dew_point': 8.66, 'uvi': 2.05, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 297, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 13.26, 'feels_like': 12.6, 'pressure': 1018, 'humidity': 75, 'dew_point': 8.93, 'uvi': 4.95, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 308, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 14.7, 'feels_like': 14.05, 'pressure': 1018, 'humidity': 70, 'dew_point': 9.29, 'uvi': 8.38, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 305, 'wind_gust': 1.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 15.39, 'feels_like': 14.76, 'pressure': 1016, 'humidity': 68, 'dew_point': 9.52, 'uvi': 10.81, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.33, 'wind_deg': 308, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 15.56, 'feels_like': 14.97, 'pressure': 1015, 'humidity': 69, 'dew_point': 9.9, 'uvi': 11.77, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 307, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641837600, 'temp': 15.48, 'feels_like': 14.94, 'pressure': 1014, 'humidity': 71, 'dew_point': 10.25, 'uvi': 10.67, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 306, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641841200, 'temp': 14.25, 'feels_like': 13.82, 'pressure': 1013, 'humidity': 80, 'dew_point': 10.85, 'uvi': 7.48, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 308, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641844800, 'temp': 13.26, 'feels_like': 12.94, 'pressure': 1013, 'humidity': 88, 'dew_point': 11.32, 'uvi': 4.34, 'clouds': 89, 'visibility': 6119, 'wind_speed': 1.81, 'wind_deg': 310, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641848400, 'temp': 12.72, 'feels_like': 12.4, 'pressure': 1013, 'humidity': 90, 'dew_point': 11.12, 'uvi': 1.74, 'clouds': 92, 'visibility': 5914, 'wind_speed': 1.27, 'wind_deg': 314, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641852000, 'temp': 11.89, 'feels_like': 11.54, 'pressure': 1014, 'humidity': 92, 'dew_point': 10.63, 'uvi': 0.39, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 326, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641855600, 'temp': 10.59, 'feels_like': 10.19, 'pressure': 1015, 'humidity': 95, 'dew_point': 9.82, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 2, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 00:00:00 | 52.000000 | 9.730000 | 9.650000 | 98.000000 | 1016.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 83.000000 | 1.08 | 0.590000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 9.060000 | 9.510000 | 97.000000 | 1017.000000 | 0.14 | 9.510000 | 0.000000 | 9914.000000 | 104.000000 | 0.84 | 0.500000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 02:00:00 | 78.000000 | 8.390000 | 8.840000 | 97.000000 | 1018.000000 |  | 8.840000 | 0.000000 | 10000.000000 | 97.000000 | 0.85 | 0.730000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 03:00:00 | 81.000000 | 8.060000 | 8.510000 | 97.000000 | 1019.000000 |  | 8.510000 | 0.000000 | 10000.000000 | 110.000000 | 0.91 | 0.950000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 04:00:00 | 77.000000 | 7.690000 | 8.140000 | 97.000000 | 1019.000000 |  | 8.140000 | 0.000000 | 10000.000000 | 129.000000 | 0.96 | 1.150000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 05:00:00 | 81.000000 | 7.320000 | 7.110000 | 97.000000 | 1018.000000 |  | 7.770000 | 0.000000 | 10000.000000 | 129.000000 | 1.05 | 1.500000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 06:00:00 | 29.000000 | 6.860000 | 6.970000 | 95.000000 | 1017.000000 |  | 7.610000 | 0.000000 | 10000.000000 | 124.000000 | 1.08 | 1.460000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 07:00:00 | 40.000000 | 6.440000 | 6.570000 | 95.000000 | 1016.000000 |  | 7.190000 | 0.000000 | 10000.000000 | 124.000000 | 1.05 | 1.400000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 08:00:00 | 54.000000 | 6.160000 | 6.320000 | 95.000000 | 1016.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 123.000000 | 1.09 | 1.340000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 09:00:00 | 49.000000 | 5.940000 | 6.680000 | 95.000000 | 1016.000000 |  | 6.680000 | 0.000000 | 10000.000000 | 130.000000 | 1.06 | 1.150000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 10:00:00 | 51.000000 | 5.980000 | 6.570000 | 96.000000 | 1017.000000 |  | 6.570000 | 0.000000 | 10000.000000 | 123.000000 | 1.03 | 1.200000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 11:00:00 | 52.000000 | 6.320000 | 6.910000 | 96.000000 | 1018.000000 |  | 6.910000 | 0.000000 | 10000.000000 | 123.000000 | 0.93 | 1.190000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 12:00:00 | 62.000000 | 7.140000 | 8.200000 | 93.000000 | 1018.000000 |  | 8.200000 | 0.320000 | 10000.000000 | 123.000000 | 0.92 | 1.160000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 13:00:00 | 68.000000 | 8.660000 | 10.630000 | 84.000000 | 1018.000000 |  | 11.260000 | 2.050000 | 10000.000000 | 297.000000 | 0.74 | 0.410000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 14:00:00 | 67.000000 | 8.930000 | 12.600000 | 75.000000 | 1018.000000 |  | 13.260000 | 4.950000 | 10000.000000 | 308.000000 | 0.97 | 1.370000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 15:00:00 | 60.000000 | 9.290000 | 14.050000 | 70.000000 | 1018.000000 |  | 14.700000 | 8.380000 | 10000.000000 | 305.000000 | 1.59 | 2.080000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 16:00:00 | 58.000000 | 9.520000 | 14.760000 | 68.000000 | 1016.000000 | 0.12 | 15.390000 | 10.810000 | 10000.000000 | 308.000000 | 1.62 | 2.330000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 9.900000 | 14.970000 | 69.000000 | 1015.000000 | 0.2 | 15.560000 | 11.770000 | 10000.000000 | 307.000000 | 1.51 | 2.360000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 18:00:00 | 76.000000 | 10.250000 | 14.940000 | 71.000000 | 1014.000000 | 0.12 | 15.480000 | 10.670000 | 10000.000000 | 306.000000 | 1.45 | 2.230000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 10.850000 | 13.820000 | 80.000000 | 1013.000000 | 0.43 | 14.250000 | 7.480000 | 10000.000000 | 308.000000 | 1.83 | 2.240000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 20:00:00 | 89.000000 | 11.320000 | 12.940000 | 88.000000 | 1013.000000 | 0.51 | 13.260000 | 4.340000 | 6119.000000 | 310.000000 | 1.62 | 1.810000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 21:00:00 | 92.000000 | 11.120000 | 12.400000 | 90.000000 | 1013.000000 | 0.37 | 12.720000 | 1.740000 | 5914.000000 | 314.000000 | 1.12 | 1.270000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 10.630000 | 11.540000 | 92.000000 | 1014.000000 | 0.24 | 11.890000 | 0.390000 | 10000.000000 | 326.000000 | 1.45 | 1.180000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125170 | "SAN CAYETANO - AUT [23125170]" | 5.333333 | -74.016667 | 2807.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-01 00:00:00 | NaT | Cundinamarca | San Cayetano (Cundinamarca) | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 23:00:00 | 92.000000 | 9.820000 | 10.190000 | 95.000000 | 1015.000000 | 0.16 | 10.590000 | 0.000000 | 10000.000000 | 2.000000 | 0.87 | 0.620000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station23125170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23125170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23125170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125170_OWM_Windspeed_20220111.png)
