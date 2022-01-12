
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BASE PALANQUERO  - AUT [23035030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23035030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.49286111,-74.658) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.49286111&lon=-74.658)


| Parameter | Value |
|---|---|
| Code | 23035030 |
| Name | BASE PALANQUERO  - AUT [23035030] |
| Latitude, ° | 5.49286111 |
| Longitude, ° | -74.658 |
| Elevation, m | 170 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-11-02 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Puerto Salgar |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Directos al Magdalena entre Ríos Seco y Negro (md) |

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

### (CNE index 137) Open Weather values for station 23035030 - BASE PALANQUERO  - AUT [23035030]

JSON data from API OWM:

```
{'lat': 5.4929, 'lon': -74.658, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813074, 'sunset': 1641855641, 'temp': 29.53, 'feels_like': 32.7, 'pressure': 1008, 'humidity': 64, 'dew_point': 22, 'uvi': 4.96, 'clouds': 46, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 13, 'wind_gust': 3.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.25, 'feels_like': 25.03, 'pressure': 1010, 'humidity': 88, 'dew_point': 22.14, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 353, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641776400, 'temp': 23.54, 'feels_like': 24.33, 'pressure': 1012, 'humidity': 91, 'dew_point': 21.98, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 54, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641780000, 'temp': 23.23, 'feels_like': 24.01, 'pressure': 1012, 'humidity': 92, 'dew_point': 21.86, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 124, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.62, 'feels_like': 23.42, 'pressure': 1013, 'humidity': 95, 'dew_point': 21.78, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 122, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641787200, 'temp': 22.39, 'feels_like': 23.17, 'pressure': 1013, 'humidity': 95, 'dew_point': 21.55, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 166, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641790800, 'temp': 22.18, 'feels_like': 22.93, 'pressure': 1012, 'humidity': 95, 'dew_point': 21.34, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 174, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 21.92, 'feels_like': 22.67, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.25, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 170, 'wind_gust': 0.81, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 21.74, 'feels_like': 22.48, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.07, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 116, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641801600, 'temp': 21.53, 'feels_like': 22.25, 'pressure': 1010, 'humidity': 96, 'dew_point': 20.87, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 99, 'wind_gust': 0.59, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 21.33, 'feels_like': 22.03, 'pressure': 1011, 'humidity': 96, 'dew_point': 20.67, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 96, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641808800, 'temp': 21.14, 'feels_like': 21.84, 'pressure': 1011, 'humidity': 97, 'dew_point': 20.64, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 63, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641812400, 'temp': 21.09, 'feels_like': 21.79, 'pressure': 1012, 'humidity': 97, 'dew_point': 20.6, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 74, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641816000, 'temp': 21.87, 'feels_like': 22.62, 'pressure': 1013, 'humidity': 96, 'dew_point': 21.2, 'uvi': 0.45, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 90, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641819600, 'temp': 23.69, 'feels_like': 24.49, 'pressure': 1015, 'humidity': 91, 'dew_point': 22.13, 'uvi': 1.94, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 19, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.41, 'feels_like': 26.2, 'pressure': 1015, 'humidity': 84, 'dew_point': 22.51, 'uvi': 4.78, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 11, 'wind_gust': 2.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641826800, 'temp': 27.01, 'feels_like': 29.48, 'pressure': 1015, 'humidity': 77, 'dew_point': 22.63, 'uvi': 8.15, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 10, 'wind_gust': 2.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641830400, 'temp': 28.28, 'feels_like': 31.37, 'pressure': 1014, 'humidity': 71, 'dew_point': 22.52, 'uvi': 11.5, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 359, 'wind_gust': 3.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641834000, 'temp': 29.36, 'feels_like': 32.55, 'pressure': 1012, 'humidity': 65, 'dew_point': 22.09, 'uvi': 12.61, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 355, 'wind_gust': 3.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.99, 'feels_like': 33.22, 'pressure': 1011, 'humidity': 62, 'dew_point': 21.91, 'uvi': 11.5, 'clouds': 45, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 353, 'wind_gust': 3.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 30.07, 'feels_like': 33.17, 'pressure': 1009, 'humidity': 61, 'dew_point': 21.72, 'uvi': 8.47, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 3, 'wind_gust': 3.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.53, 'feels_like': 32.7, 'pressure': 1008, 'humidity': 64, 'dew_point': 22, 'uvi': 4.96, 'clouds': 46, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 13, 'wind_gust': 3.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 28.81, 'feels_like': 32.14, 'pressure': 1008, 'humidity': 69, 'dew_point': 22.55, 'uvi': 2.02, 'clouds': 51, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 19, 'wind_gust': 3.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.69, 'feels_like': 31.2, 'pressure': 1009, 'humidity': 79, 'dew_point': 23.71, 'uvi': 0.43, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 11, 'wind_gust': 2.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641855600, 'temp': 24.8, 'feels_like': 25.63, 'pressure': 1009, 'humidity': 88, 'dew_point': 22.68, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 8, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 00:00:00 | 45.000000 | 22.140000 | 25.030000 | 88.000000 | 1010.000000 | 0.43 | 24.250000 | 0.000000 | 10000.000000 | 353.000000 | 1.22 | 0.410000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 01:00:00 | 61.000000 | 21.980000 | 24.330000 | 91.000000 | 1012.000000 | 0.43 | 23.540000 | 0.000000 | 10000.000000 | 54.000000 | 1.08 | 0.190000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 02:00:00 | 75.000000 | 21.860000 | 24.010000 | 92.000000 | 1012.000000 |  | 23.230000 | 0.000000 | 10000.000000 | 124.000000 | 1.01 | 0.200000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 03:00:00 | 59.000000 | 21.780000 | 23.420000 | 95.000000 | 1013.000000 | 0.35 | 22.620000 | 0.000000 | 10000.000000 | 122.000000 | 0.91 | 0.140000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 04:00:00 | 54.000000 | 21.550000 | 23.170000 | 95.000000 | 1013.000000 | 0.14 | 22.390000 | 0.000000 | 10000.000000 | 166.000000 | 0.92 | 0.520000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 05:00:00 | 51.000000 | 21.340000 | 22.930000 | 95.000000 | 1012.000000 |  | 22.180000 | 0.000000 | 10000.000000 | 174.000000 | 0.97 | 0.530000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 06:00:00 | 6.000000 | 21.250000 | 22.670000 | 96.000000 | 1011.000000 |  | 21.920000 | 0.000000 | 10000.000000 | 170.000000 | 0.81 | 0.450000 | 800 | Clear | clear sky | 01n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 07:00:00 | 13.000000 | 21.070000 | 22.480000 | 96.000000 | 1011.000000 | 0.12 | 21.740000 | 0.000000 | 10000.000000 | 116.000000 | 0.58 | 0.420000 | 500 | Rain | light rain | 10n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 08:00:00 | 14.000000 | 20.870000 | 22.250000 | 96.000000 | 1010.000000 |  | 21.530000 | 0.000000 | 10000.000000 | 99.000000 | 0.59 | 0.520000 | 801 | Clouds | few clouds | 02n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 09:00:00 | 29.000000 | 20.670000 | 22.030000 | 96.000000 | 1011.000000 | 0.11 | 21.330000 | 0.000000 | 10000.000000 | 96.000000 | 0.58 | 0.500000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 10:00:00 | 28.000000 | 20.640000 | 21.840000 | 97.000000 | 1011.000000 | 0.23 | 21.140000 | 0.000000 | 10000.000000 | 63.000000 | 0.8 | 0.460000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 11:00:00 | 37.000000 | 20.600000 | 21.790000 | 97.000000 | 1012.000000 | 0.14 | 21.090000 | 0.000000 | 10000.000000 | 74.000000 | 0.67 | 0.300000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 12:00:00 | 81.000000 | 21.200000 | 22.620000 | 96.000000 | 1013.000000 | 0.2 | 21.870000 | 0.450000 | 10000.000000 | 90.000000 | 0.55 | 0.370000 | 500 | Rain | light rain | 10d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 13:00:00 | 84.000000 | 22.130000 | 24.490000 | 91.000000 | 1015.000000 |  | 23.690000 | 1.940000 | 10000.000000 | 19.000000 | 1.21 | 0.670000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 14:00:00 | 69.000000 | 22.510000 | 26.200000 | 84.000000 | 1015.000000 | 0.18 | 25.410000 | 4.780000 | 10000.000000 | 11.000000 | 2.27 | 1.250000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 15:00:00 | 64.000000 | 22.630000 | 29.480000 | 77.000000 | 1015.000000 | 0.26 | 27.010000 | 8.150000 | 10000.000000 | 10.000000 | 2.98 | 1.800000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 16:00:00 | 58.000000 | 22.520000 | 31.370000 | 71.000000 | 1014.000000 | 0.21 | 28.280000 | 11.500000 | 10000.000000 | 359.000000 | 3.21 | 2.160000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 17:00:00 | 52.000000 | 22.090000 | 32.550000 | 65.000000 | 1012.000000 |  | 29.360000 | 12.610000 | 10000.000000 | 355.000000 | 3.38 | 2.490000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 18:00:00 | 45.000000 | 21.910000 | 33.220000 | 62.000000 | 1011.000000 |  | 29.990000 | 11.500000 | 10000.000000 | 353.000000 | 3.21 | 2.440000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 19:00:00 | 61.000000 | 21.720000 | 33.170000 | 61.000000 | 1009.000000 |  | 30.070000 | 8.470000 | 10000.000000 | 3.000000 | 3.37 | 2.460000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 20:00:00 | 46.000000 | 22.000000 | 32.700000 | 64.000000 | 1008.000000 |  | 29.530000 | 4.960000 | 10000.000000 | 13.000000 | 3.4 | 2.440000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 21:00:00 | 51.000000 | 22.550000 | 32.140000 | 69.000000 | 1008.000000 |  | 28.810000 | 2.020000 | 10000.000000 | 19.000000 | 3.45 | 2.010000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 22:00:00 | 43.000000 | 23.710000 | 31.200000 | 79.000000 | 1009.000000 | 0.2 | 27.690000 | 0.430000 | 10000.000000 | 11.000000 | 2.57 | 1.130000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23035030 | "BASE PALANQUERO  - AUT [23035030]" | 5.492861 | -74.658000 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-02 19:00:00 | NaT | Cundinamarca | Puerto Salgar | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Medio Magdalena | Directos al Magdalena entre Ríos Seco y Negro (md) | America/Bogota | 2022-01-10 23:00:00 | 53.000000 | 22.680000 | 25.630000 | 88.000000 | 1009.000000 | 0.81 | 24.800000 | 0.000000 | 10000.000000 | 8.000000 | 1.11 | 0.970000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23035030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23035030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23035030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23035030_OWM_Windspeed_20220111.png)
