
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SERRANIA DEL PERIJA  - AUT [28025120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28025120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.02908333,-73.04619444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.02908333&lon=-73.04619444)


| Parameter | Value |
|---|---|
| Code | 28025120 |
| Name | SERRANIA DEL PERIJA  - AUT [28025120] |
| Latitude, ° | 10.02908333 |
| Longitude, ° | -73.04619444 |
| Elevation, m | 2256 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-12-19 19:00:00 |
| Suspension date | NaT |
| State | Cesar |
| County | Agustín Codazzi |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Medio Cesar |

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

### (CNE index 221) Open Weather values for station 28025120 - SERRANIA DEL PERIJA  - AUT [28025120]

JSON data from API OWM:

```
{'lat': 10.0291, 'lon': -73.0462, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813132, 'sunset': 1641854809, 'temp': 20.4, 'feels_like': 20.01, 'pressure': 1013, 'humidity': 58, 'dew_point': 11.87, 'uvi': 2.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 167, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.4, 'feels_like': 15.01, 'pressure': 1017, 'humidity': 77, 'dew_point': 11.39, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.97, 'wind_deg': 84, 'wind_gust': 5.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 14.4, 'feels_like': 13.85, 'pressure': 1017, 'humidity': 75, 'dew_point': 10.03, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 83, 'wind_gust': 4.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 13.4, 'feels_like': 12.7, 'pressure': 1018, 'humidity': 73, 'dew_point': 8.66, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.72, 'wind_deg': 83, 'wind_gust': 3.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 13.4, 'feels_like': 12.57, 'pressure': 1018, 'humidity': 68, 'dew_point': 7.62, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 82, 'wind_gust': 3.85, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 13.4, 'feels_like': 12.47, 'pressure': 1018, 'humidity': 64, 'dew_point': 6.74, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.88, 'wind_deg': 80, 'wind_gust': 3.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 8.33, 'feels_like': 6.5, 'pressure': 1017, 'humidity': 59, 'dew_point': 0.79, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 79, 'wind_gust': 4.09, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 8.16, 'feels_like': 6.41, 'pressure': 1017, 'humidity': 68, 'dew_point': 2.61, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 81, 'wind_gust': 3.91, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 7.91, 'feels_like': 6.33, 'pressure': 1016, 'humidity': 72, 'dew_point': 3.18, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.52, 'wind_deg': 78, 'wind_gust': 3.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 7.87, 'feels_like': 6.44, 'pressure': 1016, 'humidity': 71, 'dew_point': 2.94, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 76, 'wind_gust': 2.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.81, 'feels_like': 6.45, 'pressure': 1016, 'humidity': 71, 'dew_point': 2.89, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 73, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 7.81, 'feels_like': 6.42, 'pressure': 1016, 'humidity': 70, 'dew_point': 2.69, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 74, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 9.4, 'feels_like': 8.2, 'pressure': 1017, 'humidity': 70, 'dew_point': 4.21, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 2.38, 'wind_deg': 75, 'wind_gust': 2.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 10.4, 'feels_like': 9.17, 'pressure': 1017, 'humidity': 64, 'dew_point': 3.89, 'uvi': 0.4, 'clouds': 66, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 78, 'wind_gust': 2.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 12.4, 'feels_like': 10.98, 'pressure': 1017, 'humidity': 49, 'dew_point': 1.99, 'uvi': 1.95, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 123, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 14.4, 'feels_like': 13.04, 'pressure': 1018, 'humidity': 44, 'dew_point': 2.31, 'uvi': 4.76, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 216, 'wind_gust': 1.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 16.4, 'feels_like': 15.14, 'pressure': 1017, 'humidity': 40, 'dew_point': 2.78, 'uvi': 8.08, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 238, 'wind_gust': 1.84, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 17.4, 'feels_like': 16.21, 'pressure': 1016, 'humidity': 39, 'dew_point': 3.32, 'uvi': 10.65, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 244, 'wind_gust': 2.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.4, 'feels_like': 18.47, 'pressure': 1015, 'humidity': 41, 'dew_point': 5.82, 'uvi': 11.48, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 245, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 19.4, 'feels_like': 18.49, 'pressure': 1014, 'humidity': 42, 'dew_point': 6.17, 'uvi': 10.24, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 241, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 20.4, 'feels_like': 19.7, 'pressure': 1013, 'humidity': 46, 'dew_point': 8.41, 'uvi': 5.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 230, 'wind_gust': 1.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 20.4, 'feels_like': 20.01, 'pressure': 1013, 'humidity': 58, 'dew_point': 11.87, 'uvi': 2.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 167, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 20.4, 'feels_like': 20.3, 'pressure': 1014, 'humidity': 69, 'dew_point': 14.53, 'uvi': 1.11, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 87, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 19.4, 'feels_like': 19.28, 'pressure': 1014, 'humidity': 72, 'dew_point': 14.23, 'uvi': 0.08, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 81, 'wind_gust': 2.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 17.4, 'feels_like': 17.26, 'pressure': 1015, 'humidity': 79, 'dew_point': 13.72, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 84, 'wind_gust': 2.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 00:00:00 | 94.000000 | 11.390000 | 15.010000 | 77.000000 | 1017.000000 |  | 15.400000 | 0.000000 | 10000.000000 | 84.000000 | 5.04 | 2.970000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 01:00:00 | 97.000000 | 10.030000 | 13.850000 | 75.000000 | 1017.000000 |  | 14.400000 | 0.000000 | 10000.000000 | 83.000000 | 4.22 | 2.810000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 8.660000 | 12.700000 | 73.000000 | 1018.000000 |  | 13.400000 | 0.000000 | 10000.000000 | 83.000000 | 3.69 | 2.720000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 03:00:00 | 50.000000 | 7.620000 | 12.570000 | 68.000000 | 1018.000000 |  | 13.400000 | 0.000000 | 10000.000000 | 82.000000 | 3.85 | 2.810000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 04:00:00 | 40.000000 | 6.740000 | 12.470000 | 64.000000 | 1018.000000 |  | 13.400000 | 0.000000 | 10000.000000 | 80.000000 | 3.97 | 2.880000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 05:00:00 | 33.000000 | 0.790000 | 6.500000 | 59.000000 | 1017.000000 |  | 8.330000 | 0.000000 | 10000.000000 | 79.000000 | 4.09 | 3.010000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 06:00:00 | 6.000000 | 2.610000 | 6.410000 | 68.000000 | 1017.000000 |  | 8.160000 | 0.000000 | 10000.000000 | 81.000000 | 3.91 | 2.840000 | 800 | Clear | clear sky | 01n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 07:00:00 | 11.000000 | 3.180000 | 6.330000 | 72.000000 | 1016.000000 |  | 7.910000 | 0.000000 | 10000.000000 | 78.000000 | 3.55 | 2.520000 | 801 | Clouds | few clouds | 02n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 08:00:00 | 55.000000 | 2.940000 | 6.440000 | 71.000000 | 1016.000000 |  | 7.870000 | 0.000000 | 10000.000000 | 76.000000 | 2.83 | 2.320000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 09:00:00 | 68.000000 | 2.890000 | 6.450000 | 71.000000 | 1016.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 73.000000 | 2.59 | 2.220000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 10:00:00 | 75.000000 | 2.690000 | 6.420000 | 70.000000 | 1016.000000 |  | 7.810000 | 0.000000 | 10000.000000 | 74.000000 | 2.59 | 2.260000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 11:00:00 | 65.000000 | 4.210000 | 8.200000 | 70.000000 | 1017.000000 |  | 9.400000 | 0.000000 | 10000.000000 | 75.000000 | 2.72 | 2.380000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 12:00:00 | 66.000000 | 3.890000 | 9.170000 | 64.000000 | 1017.000000 |  | 10.400000 | 0.400000 | 10000.000000 | 78.000000 | 2.84 | 2.020000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 13:00:00 | 49.000000 | 1.990000 | 10.980000 | 49.000000 | 1017.000000 |  | 12.400000 | 1.950000 | 10000.000000 | 123.000000 | 1.43 | 0.300000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 14:00:00 | 48.000000 | 2.310000 | 13.040000 | 44.000000 | 1018.000000 |  | 14.400000 | 4.760000 | 10000.000000 | 216.000000 | 1.72 | 0.380000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 15:00:00 | 50.000000 | 2.780000 | 15.140000 | 40.000000 | 1017.000000 |  | 16.400000 | 8.080000 | 10000.000000 | 238.000000 | 1.84 | 0.960000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 16:00:00 | 55.000000 | 3.320000 | 16.210000 | 39.000000 | 1016.000000 |  | 17.400000 | 10.650000 | 10000.000000 | 244.000000 | 2.04 | 1.620000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 5.820000 | 18.470000 | 41.000000 | 1015.000000 |  | 19.400000 | 11.480000 | 10000.000000 | 245.000000 | 2.3 | 1.880000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 18:00:00 | 99.000000 | 6.170000 | 18.490000 | 42.000000 | 1014.000000 |  | 19.400000 | 10.240000 | 10000.000000 | 241.000000 | 2.05 | 1.680000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 8.410000 | 19.700000 | 46.000000 | 1013.000000 |  | 20.400000 | 5.370000 | 10000.000000 | 230.000000 | 1.62 | 1.030000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 11.870000 | 20.010000 | 58.000000 | 1013.000000 |  | 20.400000 | 2.970000 | 10000.000000 | 167.000000 | 1.34 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 14.530000 | 20.300000 | 69.000000 | 1014.000000 |  | 20.400000 | 1.110000 | 10000.000000 | 87.000000 | 2.1 | 0.810000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 14.230000 | 19.280000 | 72.000000 | 1014.000000 |  | 19.400000 | 0.080000 | 10000.000000 | 81.000000 | 2.13 | 1.080000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025120 | "SERRANIA DEL PERIJA  - AUT [28025120]" | 10.029083 | -73.046194 | 2256.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-12-19 19:00:00 | NaT | Cesar | Agustín Codazzi | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 23:00:00 | 82.000000 | 13.720000 | 17.260000 | 79.000000 | 1015.000000 |  | 17.400000 | 0.000000 | 10000.000000 | 84.000000 | 2.53 | 2.060000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28025120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28025120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28025120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025120_OWM_Windspeed_20220111.png)
