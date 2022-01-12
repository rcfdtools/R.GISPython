
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BATALLON ROOKE  - AUT [21215180] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21215180_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.41838889,-75.24866667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.41838889&lon=-75.24866667)


| Parameter | Value |
|---|---|
| Code | 21215180 |
| Name | BATALLON ROOKE  - AUT [21215180] |
| Latitude, ° | 4.41838889 |
| Longitude, ° | -75.24866667 |
| Elevation, m | 1323 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-09 19:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Ibagué |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Coello |

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

### (CNE index 103) Open Weather values for station 21215180 - BATALLON ROOKE  - AUT [21215180]

JSON data from API OWM:

```
{'lat': 4.4184, 'lon': -75.2487, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813112, 'sunset': 1641855887, 'temp': 22.31, 'feels_like': 22.5, 'pressure': 1016, 'humidity': 73, 'dew_point': 17.24, 'uvi': 4.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, 'hourly': [{'dt': 1641772800, 'temp': 20.4, 'feels_like': 20.53, 'pressure': 1016, 'humidity': 78, 'dew_point': 16.44, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641776400, 'temp': 19.4, 'feels_like': 19.56, 'pressure': 1017, 'humidity': 83, 'dew_point': 16.44, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641780000, 'temp': 19.36, 'feels_like': 19.65, 'pressure': 1018, 'humidity': 88, 'dew_point': 17.32, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641783600, 'temp': 19.31, 'feels_like': 19.59, 'pressure': 1018, 'humidity': 88, 'dew_point': 17.27, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641787200, 'temp': 19.28, 'feels_like': 19.69, 'pressure': 1017, 'humidity': 93, 'dew_point': 18.12, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 301, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641790800, 'temp': 19.28, 'feels_like': 19.67, 'pressure': 1016, 'humidity': 92, 'dew_point': 17.95, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 312, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 20.06, 'feels_like': 20.55, 'pressure': 1015, 'humidity': 93, 'dew_point': 18.89, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 302, 'wind_gust': 0.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.06, 'feels_like': 20.58, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.06, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 303, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 18.08, 'feels_like': 18.4, 'pressure': 1014, 'humidity': 94, 'dew_point': 17.1, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 299, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 17.56, 'feels_like': 17.83, 'pressure': 1014, 'humidity': 94, 'dew_point': 16.58, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 314, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641808800, 'temp': 19.06, 'feels_like': 19.45, 'pressure': 1015, 'humidity': 93, 'dew_point': 17.9, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 317, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641812400, 'temp': 17.36, 'feels_like': 17.76, 'pressure': 1018, 'humidity': 100, 'dew_point': 17.36, 'uvi': 0, 'clouds': 75, 'visibility': 3000, 'wind_speed': 1.54, 'wind_deg': 90, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 18.31, 'feels_like': 18.81, 'pressure': 1019, 'humidity': 100, 'dew_point': 18.31, 'uvi': 0.2, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 18.36, 'feels_like': 18.86, 'pressure': 1020, 'humidity': 100, 'dew_point': 18.36, 'uvi': 1.15, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641823200, 'temp': 18.45, 'feels_like': 18.96, 'pressure': 1021, 'humidity': 100, 'dew_point': 18.45, 'uvi': 2.85, 'clouds': 75, 'visibility': 8000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641826800, 'temp': 20.45, 'feels_like': 20.85, 'pressure': 1021, 'humidity': 88, 'dew_point': 18.4, 'uvi': 4.9, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641830400, 'temp': 21.36, 'feels_like': 21.72, 'pressure': 1020, 'humidity': 83, 'dew_point': 18.36, 'uvi': 10.26, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641834000, 'temp': 22.36, 'feels_like': 22.56, 'pressure': 1019, 'humidity': 73, 'dew_point': 17.29, 'uvi': 11.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 80, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641837600, 'temp': 23.31, 'feels_like': 23.5, 'pressure': 1018, 'humidity': 69, 'dew_point': 17.31, 'uvi': 10.39, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 70, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641841200, 'temp': 24.27, 'feels_like': 24.45, 'pressure': 1017, 'humidity': 65, 'dew_point': 17.28, 'uvi': 7.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 50, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, {'dt': 1641844800, 'temp': 22.31, 'feels_like': 22.5, 'pressure': 1016, 'humidity': 73, 'dew_point': 17.24, 'uvi': 4.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641848400, 'temp': 21.31, 'feels_like': 21.66, 'pressure': 1016, 'humidity': 83, 'dew_point': 18.31, 'uvi': 1.88, 'clouds': 90, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 40, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.1}}, {'dt': 1641852000, 'temp': 21.22, 'feels_like': 21.56, 'pressure': 1016, 'humidity': 83, 'dew_point': 18.22, 'uvi': 0.43, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641855600, 'temp': 20.18, 'feels_like': 20.55, 'pressure': 1017, 'humidity': 88, 'dew_point': 18.13, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 16.440000 | 20.530000 | 78.000000 | 1016.000000 | 0.4 | 20.400000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 16.440000 | 19.560000 | 83.000000 | 1017.000000 | 0.29 | 19.400000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 17.320000 | 19.650000 | 88.000000 | 1018.000000 | 0.49 | 19.360000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 17.270000 | 19.590000 | 88.000000 | 1018.000000 | 0.31 | 19.310000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 04:00:00 | 90.000000 | 18.120000 | 19.690000 | 93.000000 | 1017.000000 | 0.17 | 19.280000 | 0.000000 | 10000.000000 | 301.000000 | 1.24 | 1.470000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 05:00:00 | 91.000000 | 17.950000 | 19.670000 | 92.000000 | 1016.000000 | 0.12 | 19.280000 | 0.000000 | 10000.000000 | 312.000000 | 1.16 | 1.330000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 06:00:00 | 70.000000 | 18.890000 | 20.550000 | 93.000000 | 1015.000000 |  | 20.060000 | 0.000000 | 10000.000000 | 302.000000 | 0.43 | 0.610000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 19.060000 | 20.580000 | 94.000000 | 1015.000000 |  | 20.060000 | 0.000000 | 10000.000000 | 303.000000 | 0.67 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 08:00:00 | 96.000000 | 17.100000 | 18.400000 | 94.000000 | 1014.000000 | 0.15 | 18.080000 | 0.000000 | 10000.000000 | 299.000000 | 0.81 | 0.980000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 16.580000 | 17.830000 | 94.000000 | 1014.000000 | 0.19 | 17.560000 | 0.000000 | 10000.000000 | 314.000000 | 1.2 | 1.470000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 17.900000 | 19.450000 | 93.000000 | 1015.000000 | 0.14 | 19.060000 | 0.000000 | 10000.000000 | 317.000000 | 1.34 | 1.750000 | 500 | Rain | light rain | 10n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 17.360000 | 17.760000 | 100.000000 | 1018.000000 |  | 17.360000 | 0.000000 | 3000.000000 | 90.000000 |  | 1.540000 | 701 | Mist | mist | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 18.310000 | 18.810000 | 100.000000 | 1019.000000 |  | 18.310000 | 0.200000 | 5000.000000 | 230.000000 |  | 1.540000 | 701 | Mist | mist | 50d | 12 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 18.360000 | 18.860000 | 100.000000 | 1020.000000 | 0.1 | 18.360000 | 1.150000 | 5000.000000 | 140.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 13 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 18.450000 | 18.960000 | 100.000000 | 1021.000000 | 0.33 | 18.450000 | 2.850000 | 8000.000000 | 360.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 18.400000 | 20.850000 | 88.000000 | 1021.000000 | 0.6 | 20.450000 | 4.900000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 18.360000 | 21.720000 | 83.000000 | 1020.000000 | 0.85 | 21.360000 | 10.260000 | 10000.000000 | 30.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 17.290000 | 22.560000 | 73.000000 | 1019.000000 | 0.81 | 22.360000 | 11.300000 | 10000.000000 | 80.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 17.310000 | 23.500000 | 69.000000 | 1018.000000 | 0.6 | 23.310000 | 10.390000 | 10000.000000 | 70.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 17.280000 | 24.450000 | 65.000000 | 1017.000000 | 1.22 | 24.270000 | 7.550000 | 10000.000000 | 50.000000 |  | 5.140000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 17.240000 | 22.500000 | 73.000000 | 1016.000000 | 1.08 | 22.310000 | 4.480000 | 10000.000000 | 60.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 18.310000 | 21.660000 | 83.000000 | 1016.000000 | 1.1 | 21.310000 | 1.880000 | 10000.000000 | 40.000000 |  | 4.120000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 18.220000 | 21.560000 | 83.000000 | 1016.000000 | 0.77 | 21.220000 | 0.430000 | 10000.000000 | 20.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215180 | "BATALLON ROOKE  - AUT [21215180]" | 4.418389 | -75.248667 | 1323.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-09 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 18.130000 | 20.550000 | 88.000000 | 1017.000000 | 1.02 | 20.180000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21215180_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21215180_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21215180_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215180_OWM_Windspeed_20220111.png)
