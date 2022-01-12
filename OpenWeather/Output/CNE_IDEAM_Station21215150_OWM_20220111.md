
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NEVADO DEL TOLIMA  - AUT [21215150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21215150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.67077778,-75.32777778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.67077778&lon=-75.32777778)


| Parameter | Value |
|---|---|
| Code | 21215150 |
| Name | NEVADO DEL TOLIMA  - AUT [21215150] |
| Latitude, ° | 4.67077778 |
| Longitude, ° | -75.32777778 |
| Elevation, m | 4635 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-10-17 19:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Anzoátegui |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Totare |

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

### (CNE index 324) Open Weather values for station 21215150 - NEVADO DEL TOLIMA  - AUT [21215150]

JSON data from API OWM:

```
{'lat': 4.6708, 'lon': -75.3278, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813155, 'sunset': 1641855881, 'temp': 1.11, 'feels_like': 1.11, 'pressure': 1015, 'humidity': 92, 'dew_point': -0.04, 'uvi': 3, 'clouds': 92, 'visibility': 3047, 'wind_speed': 0.4, 'wind_deg': 235, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, 'hourly': [{'dt': 1641772800, 'temp': 0.11, 'feels_like': 0.11, 'pressure': 1018, 'humidity': 96, 'dew_point': -0.4, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 337, 'wind_gust': 0.91, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'snow': {'1h': 0.22}}, {'dt': 1641776400, 'temp': -0.8, 'feels_like': -0.8, 'pressure': 1019, 'humidity': 93, 'dew_point': -1.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 328, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': -0.89, 'feels_like': -0.89, 'pressure': 1020, 'humidity': 94, 'dew_point': -1.63, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 308, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': -0.89, 'feels_like': -0.89, 'pressure': 1020, 'humidity': 93, 'dew_point': -1.76, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 300, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': -0.29, 'feels_like': -0.29, 'pressure': 1020, 'humidity': 93, 'dew_point': -1.17, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 305, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': -0.29, 'feels_like': -0.29, 'pressure': 1020, 'humidity': 94, 'dew_point': -1.04, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 300, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': -0.29, 'feels_like': -0.29, 'pressure': 1019, 'humidity': 94, 'dew_point': -1.04, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 288, 'wind_gust': 0.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': -0.29, 'feels_like': -0.29, 'pressure': 1018, 'humidity': 95, 'dew_point': -0.91, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 288, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': -1.61, 'feels_like': -1.61, 'pressure': 1018, 'humidity': 95, 'dew_point': -2.22, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 291, 'wind_gust': 1.03, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'snow': {'1h': 0.1}}, {'dt': 1641805200, 'temp': -1.92, 'feels_like': -1.92, 'pressure': 1018, 'humidity': 96, 'dew_point': -2.41, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 299, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': -1.29, 'feels_like': -3.09, 'pressure': 1019, 'humidity': 95, 'dew_point': -1.91, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 301, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': -2.51, 'feels_like': -4.62, 'pressure': 1020, 'humidity': 95, 'dew_point': -3.12, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 299, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': -1.76, 'feels_like': -1.76, 'pressure': 1020, 'humidity': 93, 'dew_point': -2.63, 'uvi': 0.14, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 303, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': -1.76, 'feels_like': -1.76, 'pressure': 1020, 'humidity': 89, 'dew_point': -3.15, 'uvi': 1.92, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 240, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': -1.37, 'feels_like': -1.37, 'pressure': 1020, 'humidity': 84, 'dew_point': -3.45, 'uvi': 4.8, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 136, 'wind_gust': 1.24, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.17}}, {'dt': 1641826800, 'temp': 0.49, 'feels_like': 0.49, 'pressure': 1019, 'humidity': 81, 'dew_point': -2.11, 'uvi': 8.25, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 137, 'wind_gust': 1.45, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.35}}, {'dt': 1641830400, 'temp': 1.93, 'feels_like': 1.93, 'pressure': 1019, 'humidity': 87, 'dew_point': 0, 'uvi': 9.29, 'clouds': 73, 'visibility': 4336, 'wind_speed': 0.59, 'wind_deg': 127, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641834000, 'temp': 1.86, 'feels_like': 1.86, 'pressure': 1018, 'humidity': 90, 'dew_point': 0.4, 'uvi': 10.23, 'clouds': 78, 'visibility': 6702, 'wind_speed': 0.17, 'wind_deg': 164, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641837600, 'temp': 2.04, 'feels_like': 2.04, 'pressure': 1017, 'humidity': 91, 'dew_point': 0.73, 'uvi': 9.4, 'clouds': 74, 'visibility': 2925, 'wind_speed': 0.27, 'wind_deg': 230, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641841200, 'temp': 2.72, 'feels_like': 2.72, 'pressure': 1016, 'humidity': 91, 'dew_point': 1.4, 'uvi': 5.06, 'clouds': 91, 'visibility': 2774, 'wind_speed': 0.42, 'wind_deg': 230, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.9}}, {'dt': 1641844800, 'temp': 1.11, 'feels_like': 1.11, 'pressure': 1015, 'humidity': 92, 'dew_point': -0.04, 'uvi': 3, 'clouds': 92, 'visibility': 3047, 'wind_speed': 0.4, 'wind_deg': 235, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, {'dt': 1641848400, 'temp': 0.74, 'feels_like': 0.74, 'pressure': 1016, 'humidity': 94, 'dew_point': -0.1, 'uvi': 1.25, 'clouds': 94, 'visibility': 5949, 'wind_speed': 0.34, 'wind_deg': 255, 'wind_gust': 0.86, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.85}}, {'dt': 1641852000, 'temp': 0.54, 'feels_like': 0.54, 'pressure': 1016, 'humidity': 96, 'dew_point': -0.02, 'uvi': 0.4, 'clouds': 95, 'visibility': 4376, 'wind_speed': 0.42, 'wind_deg': 287, 'wind_gust': 0.99, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.52}}, {'dt': 1641855600, 'temp': -0.33, 'feels_like': -0.33, 'pressure': 1017, 'humidity': 98, 'dew_point': -0.57, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 292, 'wind_gust': 0.69, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.62}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![13n.png](http://openweathermap.org/img/w/13n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 00:00:00 | 72.000000 | -0.400000 | 0.110000 | 96.000000 | 1018.000000 |  | 0.110000 | 0.000000 | 10000.000000 | 337.000000 | 0.91 | 0.700000 | 600 | Snow | light snow | 13n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | -1.670000 | -0.800000 | 93.000000 | 1019.000000 |  | -0.800000 | 0.000000 | 10000.000000 | 328.000000 | 0.8 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | -1.630000 | -0.890000 | 94.000000 | 1020.000000 |  | -0.890000 | 0.000000 | 10000.000000 | 308.000000 | 0.91 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | -1.760000 | -0.890000 | 93.000000 | 1020.000000 |  | -0.890000 | 0.000000 | 10000.000000 | 300.000000 | 0.9 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | -1.170000 | -0.290000 | 93.000000 | 1020.000000 |  | -0.290000 | 0.000000 | 10000.000000 | 305.000000 | 0.83 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | -1.040000 | -0.290000 | 94.000000 | 1020.000000 |  | -0.290000 | 0.000000 | 10000.000000 | 300.000000 | 0.86 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 06:00:00 | 45.000000 | -1.040000 | -0.290000 | 94.000000 | 1019.000000 |  | -0.290000 | 0.000000 | 10000.000000 | 288.000000 | 0.77 | 0.660000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 07:00:00 | 57.000000 | -0.910000 | -0.290000 | 95.000000 | 1018.000000 |  | -0.290000 | 0.000000 | 10000.000000 | 288.000000 | 0.89 | 0.660000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![13n.png](http://openweathermap.org/img/w/13n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 08:00:00 | 61.000000 | -2.220000 | -1.610000 | 95.000000 | 1018.000000 |  | -1.610000 | 0.000000 | 10000.000000 | 291.000000 | 1.03 | 0.830000 | 600 | Snow | light snow | 13n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 09:00:00 | 63.000000 | -2.410000 | -1.920000 | 96.000000 | 1018.000000 |  | -1.920000 | 0.000000 | 10000.000000 | 299.000000 | 1.18 | 1.210000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 10:00:00 | 71.000000 | -1.910000 | -3.090000 | 95.000000 | 1019.000000 |  | -1.290000 | 0.000000 | 10000.000000 | 301.000000 | 1.31 | 1.420000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 11:00:00 | 76.000000 | -3.120000 | -4.620000 | 95.000000 | 1020.000000 |  | -2.510000 | 0.000000 | 10000.000000 | 299.000000 | 1.32 | 1.500000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 12:00:00 | 63.000000 | -2.630000 | -1.760000 | 93.000000 | 1020.000000 |  | -1.760000 | 0.140000 | 10000.000000 | 303.000000 | 1.12 | 0.960000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 13:00:00 | 63.000000 | -3.150000 | -1.760000 | 89.000000 | 1020.000000 |  | -1.760000 | 1.920000 | 10000.000000 | 240.000000 | 0.95 | 0.250000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 14:00:00 | 64.000000 | -3.450000 | -1.370000 | 84.000000 | 1020.000000 |  | -1.370000 | 4.800000 | 10000.000000 | 136.000000 | 1.24 | 0.500000 | 600 | Snow | light snow | 13d | 14 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 15:00:00 | 66.000000 | -2.110000 | 0.490000 | 81.000000 | 1019.000000 |  | 0.490000 | 8.250000 | 10000.000000 | 137.000000 | 1.45 | 0.660000 | 600 | Snow | light snow | 13d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 16:00:00 | 73.000000 | 0.000000 | 1.930000 | 87.000000 | 1019.000000 | 0.45 | 1.930000 | 9.290000 | 4336.000000 | 127.000000 | 1.08 | 0.590000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 17:00:00 | 78.000000 | 0.400000 | 1.860000 | 90.000000 | 1018.000000 | 0.56 | 1.860000 | 10.230000 | 6702.000000 | 164.000000 | 1.22 | 0.170000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 18:00:00 | 74.000000 | 0.730000 | 2.040000 | 91.000000 | 1017.000000 | 0.7 | 2.040000 | 9.400000 | 2925.000000 | 230.000000 | 1.02 | 0.270000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 19:00:00 | 91.000000 | 1.400000 | 2.720000 | 91.000000 | 1016.000000 | 0.9 | 2.720000 | 5.060000 | 2774.000000 | 230.000000 | 1.12 | 0.420000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 20:00:00 | 92.000000 | -0.040000 | 1.110000 | 92.000000 | 1015.000000 | 0.89 | 1.110000 | 3.000000 | 3047.000000 | 235.000000 | 1.13 | 0.400000 | 500 | Rain | light rain | 10d | 20 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | -0.100000 | 0.740000 | 94.000000 | 1016.000000 |  | 0.740000 | 1.250000 | 5949.000000 | 255.000000 | 0.86 | 0.340000 | 601 | Snow | snow | 13d | 21 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | -0.020000 | 0.540000 | 96.000000 | 1016.000000 |  | 0.540000 | 0.400000 | 4376.000000 | 287.000000 | 0.99 | 0.420000 | 601 | Snow | snow | 13d | 22 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 21215150 | "NEVADO DEL TOLIMA  - AUT [21215150]" | 4.670778 | -75.327778 | 4635.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Anzoátegui | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Totare | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | -0.570000 | -0.330000 | 98.000000 | 1017.000000 |  | -0.330000 | 0.000000 | 10000.000000 | 292.000000 | 0.69 | 0.540000 | 601 | Snow | snow | 13d | 23 |


### Weather plots

![CNE_IDEAM_Station21215150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21215150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21215150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215150_OWM_Windspeed_20220111.png)
