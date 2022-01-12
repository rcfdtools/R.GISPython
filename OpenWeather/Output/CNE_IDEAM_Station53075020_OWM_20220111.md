
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL DIVISO - AUT [53075020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station53075020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.31141667,-77.25877778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.31141667&lon=-77.25877778)


| Parameter | Value |
|---|---|
| Code | 53075020 |
| Name | EL DIVISO - AUT [53075020] |
| Latitude, ° | 2.31141667 |
| Longitude, ° | -77.25877778 |
| Elevation, m | 1750 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-09-29 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Argelia (Cauca) |
| Stream | Magdalena |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Tapaje - Dagua - Directos |
| SZH - Hydrographic subzone | Río San Juan del Micay |

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

### (CNE index 32) Open Weather values for station 53075020 - EL DIVISO - AUT [53075020]

JSON data from API OWM:

```
{'lat': 2.3114, 'lon': -77.2588, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813390, 'sunset': 1641856573, 'temp': 18.8, 'feels_like': 19.27, 'pressure': 1014, 'humidity': 97, 'dew_point': 18.31, 'uvi': 3.14, 'clouds': 100, 'visibility': 1034, 'wind_speed': 0.9, 'wind_deg': 305, 'wind_gust': 1.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.07}}, 'hourly': [{'dt': 1641772800, 'temp': 17.47, 'feels_like': 17.86, 'pressure': 1015, 'humidity': 99, 'dew_point': 17.31, 'uvi': 0, 'clouds': 100, 'visibility': 541, 'wind_speed': 0.91, 'wind_deg': 304, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641776400, 'temp': 17.58, 'feels_like': 17.95, 'pressure': 1016, 'humidity': 98, 'dew_point': 17.26, 'uvi': 0, 'clouds': 100, 'visibility': 687, 'wind_speed': 0.56, 'wind_deg': 293, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 17.63, 'feels_like': 18.01, 'pressure': 1017, 'humidity': 98, 'dew_point': 17.31, 'uvi': 0, 'clouds': 100, 'visibility': 3443, 'wind_speed': 0.28, 'wind_deg': 264, 'wind_gust': 0.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 17.54, 'feels_like': 17.88, 'pressure': 1017, 'humidity': 97, 'dew_point': 17.06, 'uvi': 0, 'clouds': 100, 'visibility': 2408, 'wind_speed': 0.34, 'wind_deg': 179, 'wind_gust': 0.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 17.46, 'feels_like': 17.82, 'pressure': 1017, 'humidity': 98, 'dew_point': 17.14, 'uvi': 0, 'clouds': 99, 'visibility': 6953, 'wind_speed': 0.68, 'wind_deg': 148, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 17.28, 'feels_like': 17.62, 'pressure': 1017, 'humidity': 98, 'dew_point': 16.96, 'uvi': 0, 'clouds': 98, 'visibility': 6690, 'wind_speed': 0.49, 'wind_deg': 164, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641794400, 'temp': 17.18, 'feels_like': 17.49, 'pressure': 1016, 'humidity': 97, 'dew_point': 16.7, 'uvi': 0, 'clouds': 94, 'visibility': 2060, 'wind_speed': 0.28, 'wind_deg': 220, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641798000, 'temp': 16.99, 'feels_like': 17.3, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.67, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 260, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641801600, 'temp': 16.92, 'feels_like': 17.23, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.6, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 267, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641805200, 'temp': 16.89, 'feels_like': 17.19, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.57, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 233, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641808800, 'temp': 16.86, 'feels_like': 17.16, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.54, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 231, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641812400, 'temp': 16.79, 'feels_like': 17.08, 'pressure': 1016, 'humidity': 98, 'dew_point': 16.47, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 250, 'wind_gust': 0.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641816000, 'temp': 17.2, 'feels_like': 17.53, 'pressure': 1017, 'humidity': 98, 'dew_point': 16.88, 'uvi': 0.36, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 294, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641819600, 'temp': 18.03, 'feels_like': 18.4, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.38, 'uvi': 1.56, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 323, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641823200, 'temp': 18.73, 'feels_like': 19.14, 'pressure': 1018, 'humidity': 95, 'dew_point': 17.91, 'uvi': 4, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 285, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641826800, 'temp': 18.96, 'feels_like': 19.39, 'pressure': 1018, 'humidity': 95, 'dew_point': 18.14, 'uvi': 7.08, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 315, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.79}}, {'dt': 1641830400, 'temp': 20.06, 'feels_like': 20.55, 'pressure': 1017, 'humidity': 93, 'dew_point': 18.89, 'uvi': 9.19, 'clouds': 99, 'visibility': 6854, 'wind_speed': 0.6, 'wind_deg': 316, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.24}}, {'dt': 1641834000, 'temp': 20.14, 'feels_like': 20.64, 'pressure': 1016, 'humidity': 93, 'dew_point': 18.97, 'uvi': 10.36, 'clouds': 99, 'visibility': 1655, 'wind_speed': 0.66, 'wind_deg': 311, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.34}}, {'dt': 1641837600, 'temp': 19.34, 'feels_like': 19.78, 'pressure': 1016, 'humidity': 94, 'dew_point': 18.35, 'uvi': 9.76, 'clouds': 100, 'visibility': 4056, 'wind_speed': 0.78, 'wind_deg': 317, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, {'dt': 1641841200, 'temp': 19.12, 'feels_like': 19.57, 'pressure': 1015, 'humidity': 95, 'dew_point': 18.3, 'uvi': 5.06, 'clouds': 100, 'visibility': 1273, 'wind_speed': 1, 'wind_deg': 313, 'wind_gust': 1.68, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.3}}, {'dt': 1641844800, 'temp': 18.8, 'feels_like': 19.27, 'pressure': 1014, 'humidity': 97, 'dew_point': 18.31, 'uvi': 3.14, 'clouds': 100, 'visibility': 1034, 'wind_speed': 0.9, 'wind_deg': 305, 'wind_gust': 1.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.07}}, {'dt': 1641848400, 'temp': 18.75, 'feels_like': 19.21, 'pressure': 1013, 'humidity': 97, 'dew_point': 18.26, 'uvi': 1.42, 'clouds': 100, 'visibility': 140, 'wind_speed': 0.84, 'wind_deg': 298, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641852000, 'temp': 18.45, 'feels_like': 18.91, 'pressure': 1014, 'humidity': 98, 'dew_point': 18.13, 'uvi': 0.17, 'clouds': 99, 'visibility': 93, 'wind_speed': 0.82, 'wind_deg': 302, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.74}}, {'dt': 1641855600, 'temp': 17.86, 'feels_like': 18.29, 'pressure': 1015, 'humidity': 99, 'dew_point': 17.7, 'uvi': 0, 'clouds': 99, 'visibility': 77, 'wind_speed': 0.83, 'wind_deg': 279, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 17.310000 | 17.860000 | 99.000000 | 1015.000000 | 0.35 | 17.470000 | 0.000000 | 541.000000 | 304.000000 | 1.23 | 0.910000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 17.260000 | 17.950000 | 98.000000 | 1016.000000 | 0.12 | 17.580000 | 0.000000 | 687.000000 | 293.000000 | 0.77 | 0.560000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 17.310000 | 18.010000 | 98.000000 | 1017.000000 |  | 17.630000 | 0.000000 | 3443.000000 | 264.000000 | 0.36 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 17.060000 | 17.880000 | 97.000000 | 1017.000000 |  | 17.540000 | 0.000000 | 2408.000000 | 179.000000 | 0.37 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 17.140000 | 17.820000 | 98.000000 | 1017.000000 |  | 17.460000 | 0.000000 | 6953.000000 | 148.000000 | 0.85 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 05:00:00 | 98.000000 | 16.960000 | 17.620000 | 98.000000 | 1017.000000 | 0.16 | 17.280000 | 0.000000 | 6690.000000 | 164.000000 | 0.57 | 0.490000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 06:00:00 | 94.000000 | 16.700000 | 17.490000 | 97.000000 | 1016.000000 | 0.43 | 17.180000 | 0.000000 | 2060.000000 | 220.000000 | 0.53 | 0.280000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 07:00:00 | 98.000000 | 16.670000 | 17.300000 | 98.000000 | 1015.000000 | 0.29 | 16.990000 | 0.000000 | 10000.000000 | 260.000000 | 0.63 | 0.260000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 16.600000 | 17.230000 | 98.000000 | 1015.000000 | 0.31 | 16.920000 | 0.000000 | 10000.000000 | 267.000000 | 0.69 | 0.490000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 16.570000 | 17.190000 | 98.000000 | 1015.000000 | 0.16 | 16.890000 | 0.000000 | 10000.000000 | 233.000000 | 0.6 | 0.440000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 16.540000 | 17.160000 | 98.000000 | 1015.000000 | 0.11 | 16.860000 | 0.000000 | 10000.000000 | 231.000000 | 0.41 | 0.290000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 16.470000 | 17.080000 | 98.000000 | 1016.000000 | 0.23 | 16.790000 | 0.000000 | 10000.000000 | 250.000000 | 0.46 | 0.390000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 12:00:00 | 65.000000 | 16.880000 | 17.530000 | 98.000000 | 1017.000000 | 0.22 | 17.200000 | 0.360000 | 10000.000000 | 294.000000 | 0.61 | 0.350000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 17.380000 | 18.400000 | 96.000000 | 1017.000000 | 0.28 | 18.030000 | 1.560000 | 10000.000000 | 323.000000 | 0.79 | 0.360000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 17.910000 | 19.140000 | 95.000000 | 1018.000000 | 0.61 | 18.730000 | 4.000000 | 10000.000000 | 285.000000 | 0.67 | 0.250000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 18.140000 | 19.390000 | 95.000000 | 1018.000000 | 0.79 | 18.960000 | 7.080000 | 10000.000000 | 315.000000 | 0.91 | 0.510000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 18.890000 | 20.550000 | 93.000000 | 1017.000000 | 1.24 | 20.060000 | 9.190000 | 6854.000000 | 316.000000 | 1.26 | 0.600000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 18.970000 | 20.640000 | 93.000000 | 1016.000000 | 1.34 | 20.140000 | 10.360000 | 1655.000000 | 311.000000 | 1.3 | 0.660000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 18.350000 | 19.780000 | 94.000000 | 1016.000000 | 1.44 | 19.340000 | 9.760000 | 4056.000000 | 317.000000 | 1.26 | 0.780000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 18.300000 | 19.570000 | 95.000000 | 1015.000000 | 1.3 | 19.120000 | 5.060000 | 1273.000000 | 313.000000 | 1.68 | 1.000000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 18.310000 | 19.270000 | 97.000000 | 1014.000000 | 1.07 | 18.800000 | 3.140000 | 1034.000000 | 305.000000 | 1.72 | 0.900000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 18.260000 | 19.210000 | 97.000000 | 1013.000000 | 0.88 | 18.750000 | 1.420000 | 140.000000 | 298.000000 | 1.6 | 0.840000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 18.130000 | 18.910000 | 98.000000 | 1014.000000 | 0.74 | 18.450000 | 0.170000 | 93.000000 | 302.000000 | 1.71 | 0.820000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53075020 | "EL DIVISO - AUT [53075020]" | 2.311417 | -77.258778 | 1750.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-29 00:00:00 | NaT | Cauca | Argelia (Cauca) | Magdalena | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río San Juan del Micay | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 17.700000 | 18.290000 | 99.000000 | 1015.000000 | 0.86 | 17.860000 | 0.000000 | 77.000000 | 279.000000 | 1.57 | 0.830000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station53075020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station53075020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station53075020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53075020_OWM_Windspeed_20220111.png)
