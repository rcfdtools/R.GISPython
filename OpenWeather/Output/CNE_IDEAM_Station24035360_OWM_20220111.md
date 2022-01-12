
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SOCHA - AUT [24035360] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035360_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.98541667,-72.99702778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.98541667&lon=-72.99702778)


| Parameter | Value |
|---|---|
| Code | 24035360 |
| Name | SOCHA - AUT [24035360] |
| Latitude, ° | 5.98541667 |
| Longitude, ° | -72.99702778 |
| Elevation, m | 2503 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-10 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Socha |
| Stream | Cauca |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Fonce |

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

### (CNE index 153) Open Weather values for station 24035360 - SOCHA - AUT [24035360]

JSON data from API OWM:

```
{'lat': 5.9854, 'lon': -72.997, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812723, 'sunset': 1641855194, 'temp': 11.36, 'feels_like': 10.09, 'pressure': 1012, 'humidity': 59, 'dew_point': 3.64, 'uvi': 4.8, 'clouds': 83, 'visibility': 10000, 'wind_speed': 3.72, 'wind_deg': 312, 'wind_gust': 3.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 4.87, 'feels_like': 4.87, 'pressure': 1018, 'humidity': 98, 'dew_point': 4.58, 'uvi': 0, 'clouds': 81, 'visibility': 2100, 'wind_speed': 1.05, 'wind_deg': 324, 'wind_gust': 1.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 4.56, 'feels_like': 4.56, 'pressure': 1019, 'humidity': 97, 'dew_point': 4.13, 'uvi': 0, 'clouds': 97, 'visibility': 3183, 'wind_speed': 0.99, 'wind_deg': 326, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 4.07, 'feels_like': 4.07, 'pressure': 1020, 'humidity': 97, 'dew_point': 3.64, 'uvi': 0, 'clouds': 98, 'visibility': 8570, 'wind_speed': 0.87, 'wind_deg': 342, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 3.55, 'feels_like': 3.55, 'pressure': 1020, 'humidity': 97, 'dew_point': 3.12, 'uvi': 0, 'clouds': 98, 'visibility': 9387, 'wind_speed': 0.66, 'wind_deg': 4, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 2.89, 'feels_like': 2.89, 'pressure': 1020, 'humidity': 97, 'dew_point': 2.46, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 34, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 2.4, 'feels_like': 2.4, 'pressure': 1020, 'humidity': 97, 'dew_point': 1.97, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 75, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 2.61, 'feels_like': 2.61, 'pressure': 1019, 'humidity': 97, 'dew_point': 2.18, 'uvi': 0, 'clouds': 61, 'visibility': 7632, 'wind_speed': 0.19, 'wind_deg': 30, 'wind_gust': 0.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 2.54, 'feels_like': 2.54, 'pressure': 1018, 'humidity': 97, 'dew_point': 2.11, 'uvi': 0, 'clouds': 92, 'visibility': 7650, 'wind_speed': 0.42, 'wind_deg': 343, 'wind_gust': 0.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 2.52, 'feels_like': 2.52, 'pressure': 1017, 'humidity': 97, 'dew_point': 2.09, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 330, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 2.89, 'feels_like': 2.89, 'pressure': 1017, 'humidity': 97, 'dew_point': 2.46, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 321, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 3.15, 'feels_like': 3.15, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.13, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 313, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.1, 'feels_like': 3.1, 'pressure': 1018, 'humidity': 94, 'dew_point': 2.23, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 343, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 3.15, 'feels_like': 3.15, 'pressure': 1019, 'humidity': 95, 'dew_point': 2.43, 'uvi': 0.42, 'clouds': 27, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 349, 'wind_gust': 0.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 5.83, 'feels_like': 5.83, 'pressure': 1019, 'humidity': 85, 'dew_point': 3.51, 'uvi': 2.52, 'clouds': 42, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 315, 'wind_gust': 1.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 8.22, 'feels_like': 8.22, 'pressure': 1019, 'humidity': 73, 'dew_point': 3.67, 'uvi': 5.81, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 300, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 10.42, 'feels_like': 9.11, 'pressure': 1018, 'humidity': 61, 'dew_point': 3.23, 'uvi': 9.59, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 299, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 11.45, 'feels_like': 10.11, 'pressure': 1016, 'humidity': 56, 'dew_point': 2.99, 'uvi': 12.58, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 301, 'wind_gust': 3.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 12.04, 'feels_like': 10.68, 'pressure': 1015, 'humidity': 53, 'dew_point': 2.76, 'uvi': 13.45, 'clouds': 47, 'visibility': 10000, 'wind_speed': 3.52, 'wind_deg': 302, 'wind_gust': 3.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 12.59, 'feels_like': 11.21, 'pressure': 1014, 'humidity': 50, 'dew_point': 2.45, 'uvi': 11.95, 'clouds': 64, 'visibility': 10000, 'wind_speed': 3.67, 'wind_deg': 307, 'wind_gust': 3.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 12.38, 'feels_like': 11.03, 'pressure': 1012, 'humidity': 52, 'dew_point': 2.81, 'uvi': 8.57, 'clouds': 66, 'visibility': 10000, 'wind_speed': 3.89, 'wind_deg': 309, 'wind_gust': 3.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 11.36, 'feels_like': 10.09, 'pressure': 1012, 'humidity': 59, 'dew_point': 3.64, 'uvi': 4.8, 'clouds': 83, 'visibility': 10000, 'wind_speed': 3.72, 'wind_deg': 312, 'wind_gust': 3.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 9.71, 'feels_like': 8.09, 'pressure': 1013, 'humidity': 69, 'dew_point': 4.3, 'uvi': 1.85, 'clouds': 88, 'visibility': 10000, 'wind_speed': 3.13, 'wind_deg': 314, 'wind_gust': 3.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 7.68, 'feels_like': 6.18, 'pressure': 1014, 'humidity': 85, 'dew_point': 5.32, 'uvi': 0.34, 'clouds': 85, 'visibility': 8803, 'wind_speed': 2.36, 'wind_deg': 317, 'wind_gust': 2.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641855600, 'temp': 5.17, 'feels_like': 3.8, 'pressure': 1016, 'humidity': 96, 'dew_point': 4.59, 'uvi': 0, 'clouds': 88, 'visibility': 2819, 'wind_speed': 1.78, 'wind_deg': 322, 'wind_gust': 2.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 00:00:00 | 81.000000 | 4.580000 | 4.870000 | 98.000000 | 1018.000000 |  | 4.870000 | 0.000000 | 2100.000000 | 324.000000 | 1.42 | 1.050000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 01:00:00 | 97.000000 | 4.130000 | 4.560000 | 97.000000 | 1019.000000 |  | 4.560000 | 0.000000 | 3183.000000 | 326.000000 | 1.33 | 0.990000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | 3.640000 | 4.070000 | 97.000000 | 1020.000000 |  | 4.070000 | 0.000000 | 8570.000000 | 342.000000 | 1.24 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 03:00:00 | 98.000000 | 3.120000 | 3.550000 | 97.000000 | 1020.000000 |  | 3.550000 | 0.000000 | 9387.000000 | 4.000000 | 1.03 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 2.460000 | 2.890000 | 97.000000 | 1020.000000 |  | 2.890000 | 0.000000 | 10000.000000 | 34.000000 | 0.92 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 05:00:00 | 87.000000 | 1.970000 | 2.400000 | 97.000000 | 1020.000000 |  | 2.400000 | 0.000000 | 10000.000000 | 75.000000 | 0.8 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 06:00:00 | 61.000000 | 2.180000 | 2.610000 | 97.000000 | 1019.000000 |  | 2.610000 | 0.000000 | 7632.000000 | 30.000000 | 0.41 | 0.190000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 07:00:00 | 92.000000 | 2.110000 | 2.540000 | 97.000000 | 1018.000000 |  | 2.540000 | 0.000000 | 7650.000000 | 343.000000 | 0.42 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 2.090000 | 2.520000 | 97.000000 | 1017.000000 |  | 2.520000 | 0.000000 | 10000.000000 | 330.000000 | 0.63 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 2.460000 | 2.890000 | 97.000000 | 1017.000000 |  | 2.890000 | 0.000000 | 10000.000000 | 321.000000 | 0.8 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 10:00:00 | 90.000000 | 2.130000 | 3.150000 | 93.000000 | 1017.000000 |  | 3.150000 | 0.000000 | 10000.000000 | 313.000000 | 0.81 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 11:00:00 | 91.000000 | 2.230000 | 3.100000 | 94.000000 | 1018.000000 |  | 3.100000 | 0.000000 | 10000.000000 | 343.000000 | 0.54 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 12:00:00 | 27.000000 | 2.430000 | 3.150000 | 95.000000 | 1019.000000 |  | 3.150000 | 0.420000 | 10000.000000 | 349.000000 | 0.81 | 0.380000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 13:00:00 | 42.000000 | 3.510000 | 5.830000 | 85.000000 | 1019.000000 |  | 5.830000 | 2.520000 | 10000.000000 | 315.000000 | 1.02 | 0.900000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 3.670000 | 8.220000 | 73.000000 | 1019.000000 |  | 8.220000 | 5.810000 | 10000.000000 | 300.000000 | 1.61 | 1.210000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 15:00:00 | 69.000000 | 3.230000 | 9.110000 | 61.000000 | 1018.000000 |  | 10.420000 | 9.590000 | 10000.000000 | 299.000000 | 2.59 | 1.860000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 16:00:00 | 56.000000 | 2.990000 | 10.110000 | 56.000000 | 1016.000000 |  | 11.450000 | 12.580000 | 10000.000000 | 301.000000 | 3.3 | 2.780000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 17:00:00 | 47.000000 | 2.760000 | 10.680000 | 53.000000 | 1015.000000 |  | 12.040000 | 13.450000 | 10000.000000 | 302.000000 | 3.63 | 3.520000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 18:00:00 | 64.000000 | 2.450000 | 11.210000 | 50.000000 | 1014.000000 |  | 12.590000 | 11.950000 | 10000.000000 | 307.000000 | 3.56 | 3.670000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 19:00:00 | 66.000000 | 2.810000 | 11.030000 | 52.000000 | 1012.000000 |  | 12.380000 | 8.570000 | 10000.000000 | 309.000000 | 3.67 | 3.890000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 20:00:00 | 83.000000 | 3.640000 | 10.090000 | 59.000000 | 1012.000000 |  | 11.360000 | 4.800000 | 10000.000000 | 312.000000 | 3.57 | 3.720000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 21:00:00 | 88.000000 | 4.300000 | 8.090000 | 69.000000 | 1013.000000 |  | 9.710000 | 1.850000 | 10000.000000 | 314.000000 | 3.41 | 3.130000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 22:00:00 | 85.000000 | 5.320000 | 6.180000 | 85.000000 | 1014.000000 | 0.24 | 7.680000 | 0.340000 | 8803.000000 | 317.000000 | 2.93 | 2.360000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035360 | "SOCHA - AUT [24035360]" | 5.985417 | -72.997028 | 2503.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Boyacá | Socha | Cauca | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 4.590000 | 3.800000 | 96.000000 | 1016.000000 | 0.12 | 5.170000 | 0.000000 | 2819.000000 | 322.000000 | 2.54 | 1.780000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24035360_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035360_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035360_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035360_OWM_Windspeed_20220111.png)
