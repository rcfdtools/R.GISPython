
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GUAMO [21185030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21185030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.00883333,-74.98138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.00883333&lon=-74.98138889)


| Parameter | Value |
|---|---|
| Code | 21185030 |
| Name | GUAMO [21185030] |
| Latitude, ° | 4.00883333 |
| Longitude, ° | -74.98138889 |
| Elevation, m | 332 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1953-12-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Guamo |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Saldaña |
| SZH - Hydrographic subzone | Bajo Saldaña |

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

### (CNE index 1319) Open Weather values for station 21185030 - GUAMO [21185030]

JSON data from API OWM:

```
{'lat': 4.0088, 'lon': -74.9814, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813008, 'sunset': 1641855862, 'temp': 28.77, 'feels_like': 29.6, 'pressure': 1006, 'humidity': 52, 'dew_point': 17.94, 'uvi': 5.14, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 97, 'wind_gust': 2.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.77, 'feels_like': 28.12, 'pressure': 1008, 'humidity': 65, 'dew_point': 19.64, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 292, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641776400, 'temp': 25.77, 'feels_like': 26.15, 'pressure': 1009, 'humidity': 67, 'dew_point': 19.18, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 55, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641780000, 'temp': 25.77, 'feels_like': 26.39, 'pressure': 1011, 'humidity': 76, 'dew_point': 21.22, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 38, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.79}}, {'dt': 1641783600, 'temp': 25.77, 'feels_like': 26.47, 'pressure': 1011, 'humidity': 79, 'dew_point': 21.85, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 220, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.54}}, {'dt': 1641787200, 'temp': 23.09, 'feels_like': 23.62, 'pressure': 1012, 'humidity': 83, 'dew_point': 20.05, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 222, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.53, 'feels_like': 23.08, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.07, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 225, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 21.7, 'feels_like': 22.33, 'pressure': 1011, 'humidity': 92, 'dew_point': 20.34, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 195, 'wind_gust': 0.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641798000, 'temp': 21.58, 'feels_like': 22.22, 'pressure': 1010, 'humidity': 93, 'dew_point': 20.4, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 152, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641801600, 'temp': 21.25, 'feels_like': 21.88, 'pressure': 1010, 'humidity': 94, 'dew_point': 20.25, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 29, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1641805200, 'temp': 21.63, 'feels_like': 22.3, 'pressure': 1010, 'humidity': 94, 'dew_point': 20.62, 'uvi': 0, 'clouds': 62, 'visibility': 8257, 'wind_speed': 0.95, 'wind_deg': 40, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.69}}, {'dt': 1641808800, 'temp': 21.51, 'feels_like': 22.2, 'pressure': 1011, 'humidity': 95, 'dew_point': 20.68, 'uvi': 0, 'clouds': 70, 'visibility': 8950, 'wind_speed': 0.99, 'wind_deg': 6, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.94}}, {'dt': 1641812400, 'temp': 23.77, 'feels_like': 24.66, 'pressure': 1011, 'humidity': 94, 'dew_point': 22.75, 'uvi': 0, 'clouds': 76, 'visibility': 8840, 'wind_speed': 0.72, 'wind_deg': 17, 'wind_gust': 0.79, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.12}}, {'dt': 1641816000, 'temp': 24.77, 'feels_like': 25.76, 'pressure': 1012, 'humidity': 94, 'dew_point': 23.74, 'uvi': 0.21, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 35, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641819600, 'temp': 24.77, 'feels_like': 25.6, 'pressure': 1014, 'humidity': 88, 'dew_point': 22.65, 'uvi': 1.94, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 44, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641823200, 'temp': 24.77, 'feels_like': 25.5, 'pressure': 1014, 'humidity': 84, 'dew_point': 21.88, 'uvi': 4.72, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 76, 'wind_gust': 2.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 26.77, 'feels_like': 29.08, 'pressure': 1014, 'humidity': 78, 'dew_point': 22.61, 'uvi': 8.02, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 76, 'wind_gust': 2.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 27.77, 'feels_like': 30.23, 'pressure': 1013, 'humidity': 70, 'dew_point': 21.8, 'uvi': 11.69, 'clouds': 79, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 54, 'wind_gust': 3.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.77, 'feels_like': 30.94, 'pressure': 1011, 'humidity': 62, 'dew_point': 20.77, 'uvi': 12.8, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 32, 'wind_gust': 3.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.77, 'feels_like': 31.85, 'pressure': 1009, 'humidity': 57, 'dew_point': 20.34, 'uvi': 11.69, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 60, 'wind_gust': 2.61, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 30.77, 'feels_like': 32.82, 'pressure': 1008, 'humidity': 53, 'dew_point': 20.09, 'uvi': 8.74, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 92, 'wind_gust': 2.25, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 28.77, 'feels_like': 29.6, 'pressure': 1006, 'humidity': 52, 'dew_point': 17.94, 'uvi': 5.14, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 97, 'wind_gust': 2.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 27.77, 'feels_like': 28.45, 'pressure': 1006, 'humidity': 53, 'dew_point': 17.32, 'uvi': 2.12, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 119, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.77, 'feels_like': 29.32, 'pressure': 1007, 'humidity': 62, 'dew_point': 19.83, 'uvi': 0.49, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 136, 'wind_gust': 2.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.77, 'feels_like': 28.26, 'pressure': 1007, 'humidity': 67, 'dew_point': 20.13, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 114, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 00:00:00 | 29.000000 | 19.640000 | 28.120000 | 65.000000 | 1008.000000 | 0.12 | 26.770000 | 0.000000 | 10000.000000 | 292.000000 | 0.77 | 0.480000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 01:00:00 | 43.000000 | 19.180000 | 26.150000 | 67.000000 | 1009.000000 | 0.29 | 25.770000 | 0.000000 | 10000.000000 | 55.000000 | 0.89 | 0.850000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 02:00:00 | 63.000000 | 21.220000 | 26.390000 | 76.000000 | 1011.000000 | 0.79 | 25.770000 | 0.000000 | 10000.000000 | 38.000000 | 1.02 | 0.880000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 03:00:00 | 76.000000 | 21.850000 | 26.470000 | 79.000000 | 1011.000000 | 0.54 | 25.770000 | 0.000000 | 10000.000000 | 220.000000 | 0.66 | 0.480000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 20.050000 | 23.620000 | 83.000000 | 1012.000000 |  | 23.090000 | 0.000000 | 10000.000000 | 222.000000 | 1.18 | 1.130000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 05:00:00 | 81.000000 | 20.070000 | 23.080000 | 86.000000 | 1011.000000 |  | 22.530000 | 0.000000 | 10000.000000 | 225.000000 | 1.24 | 1.120000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 06:00:00 | 36.000000 | 20.340000 | 22.330000 | 92.000000 | 1011.000000 | 0.29 | 21.700000 | 0.000000 | 10000.000000 | 195.000000 | 0.43 | 0.340000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 07:00:00 | 51.000000 | 20.400000 | 22.220000 | 93.000000 | 1010.000000 | 0.53 | 21.580000 | 0.000000 | 10000.000000 | 152.000000 | 0.53 | 0.370000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 08:00:00 | 47.000000 | 20.250000 | 21.880000 | 94.000000 | 1010.000000 | 0.65 | 21.250000 | 0.000000 | 10000.000000 | 29.000000 | 0.54 | 0.490000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 09:00:00 | 62.000000 | 20.620000 | 22.300000 | 94.000000 | 1010.000000 | 0.69 | 21.630000 | 0.000000 | 8257.000000 | 40.000000 | 1.09 | 0.950000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 10:00:00 | 70.000000 | 20.680000 | 22.200000 | 95.000000 | 1011.000000 | 0.94 | 21.510000 | 0.000000 | 8950.000000 | 6.000000 | 1.18 | 0.990000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 11:00:00 | 76.000000 | 22.750000 | 24.660000 | 94.000000 | 1011.000000 | 1.12 | 23.770000 | 0.000000 | 8840.000000 | 17.000000 | 0.79 | 0.720000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 12:00:00 | 86.000000 | 23.740000 | 25.760000 | 94.000000 | 1012.000000 | 0.85 | 24.770000 | 0.210000 | 10000.000000 | 35.000000 | 1.22 | 0.910000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 22.650000 | 25.600000 | 88.000000 | 1014.000000 | 0.29 | 24.770000 | 1.940000 | 10000.000000 | 44.000000 | 1.62 | 1.220000 | 500 | Rain | light rain | 10d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 14:00:00 | 96.000000 | 21.880000 | 25.500000 | 84.000000 | 1014.000000 |  | 24.770000 | 4.720000 | 10000.000000 | 76.000000 | 2.11 | 1.990000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 15:00:00 | 96.000000 | 22.610000 | 29.080000 | 78.000000 | 1014.000000 |  | 26.770000 | 8.020000 | 10000.000000 | 76.000000 | 2.67 | 2.310000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 16:00:00 | 79.000000 | 21.800000 | 30.230000 | 70.000000 | 1013.000000 |  | 27.770000 | 11.690000 | 10000.000000 | 54.000000 | 3.39 | 2.440000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 17:00:00 | 68.000000 | 20.770000 | 30.940000 | 62.000000 | 1011.000000 |  | 28.770000 | 12.800000 | 10000.000000 | 32.000000 | 3.07 | 2.060000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 18:00:00 | 6.000000 | 20.340000 | 31.850000 | 57.000000 | 1009.000000 |  | 29.770000 | 11.690000 | 10000.000000 | 60.000000 | 2.61 | 1.570000 | 800 | Clear | clear sky | 01d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 19:00:00 | 12.000000 | 20.090000 | 32.820000 | 53.000000 | 1008.000000 |  | 30.770000 | 8.740000 | 10000.000000 | 92.000000 | 2.25 | 1.230000 | 801 | Clouds | few clouds | 02d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 20:00:00 | 54.000000 | 17.940000 | 29.600000 | 52.000000 | 1006.000000 |  | 28.770000 | 5.140000 | 10000.000000 | 97.000000 | 2.46 | 1.590000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 21:00:00 | 68.000000 | 17.320000 | 28.450000 | 53.000000 | 1006.000000 |  | 27.770000 | 2.120000 | 10000.000000 | 119.000000 | 1.79 | 1.640000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 22:00:00 | 74.000000 | 19.830000 | 29.320000 | 62.000000 | 1007.000000 |  | 27.770000 | 0.490000 | 10000.000000 | 136.000000 | 2.8 | 2.160000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185030 | "GUAMO [21185030]" | 4.008833 | -74.981389 | 332.000000 | Climática Principal | Convencional | Activa | 1953-12-15 00:00:00 | NaT | Tolima | Guamo | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Bajo Saldaña | America/Bogota | 2022-01-10 23:00:00 | 67.000000 | 20.130000 | 28.260000 | 67.000000 | 1007.000000 |  | 26.770000 | 0.000000 | 10000.000000 | 114.000000 | 1.39 | 1.410000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21185030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21185030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21185030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185030_OWM_Windspeed_20220111.png)
