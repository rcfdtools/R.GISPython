
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CAPURGANA - AUT [11155030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station11155030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.61625,-77.32819444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.61625&lon=-77.32819444)


| Parameter | Value |
|---|---|
| Code | 11155030 |
| Name | CAPURGANA - AUT [11155030] |
| Latitude, ° | 8.61625 |
| Longitude, ° | -77.32819444 |
| Elevation, m | 19 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-04-16 00:00:00 |
| Suspension date | NaT |
| State | Chocó |
| County | Acandí |
| Stream | Magdalena |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Atrato - Darién |
| SZH - Hydrographic subzone | Río Tolo y otros Directos al Caribe |

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

### (CNE index 3486) Open Weather values for station 11155030 - CAPURGANA - AUT [11155030]

JSON data from API OWM:

```
{'lat': 8.6163, 'lon': -77.3282, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641814020, 'sunset': 1641855977, 'temp': 27.52, 'feels_like': 30.33, 'pressure': 1010, 'humidity': 75, 'dew_point': 22.69, 'uvi': 3.57, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.15, 'wind_deg': 326, 'wind_gust': 4.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, 'hourly': [{'dt': 1641772800, 'temp': 25.84, 'feels_like': 26.7, 'pressure': 1011, 'humidity': 85, 'dew_point': 23.12, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 330, 'wind_gust': 4.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.67, 'feels_like': 26.51, 'pressure': 1012, 'humidity': 85, 'dew_point': 22.96, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 2.92, 'wind_deg': 338, 'wind_gust': 4.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.62, 'feels_like': 26.46, 'pressure': 1013, 'humidity': 85, 'dew_point': 22.91, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 341, 'wind_gust': 4.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.47, 'feels_like': 26.34, 'pressure': 1013, 'humidity': 87, 'dew_point': 23.15, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 3, 'wind_deg': 344, 'wind_gust': 4.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.32, 'feels_like': 26.18, 'pressure': 1012, 'humidity': 87, 'dew_point': 23, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 3.29, 'wind_deg': 346, 'wind_gust': 4.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.28, 'feels_like': 26.16, 'pressure': 1012, 'humidity': 88, 'dew_point': 23.15, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 340, 'wind_gust': 4.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.2, 'feels_like': 26.1, 'pressure': 1012, 'humidity': 89, 'dew_point': 23.26, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 3.34, 'wind_deg': 334, 'wind_gust': 4.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641798000, 'temp': 25.21, 'feels_like': 26.06, 'pressure': 1011, 'humidity': 87, 'dew_point': 22.89, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 3.14, 'wind_deg': 327, 'wind_gust': 4.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641801600, 'temp': 25.2, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 87, 'dew_point': 22.88, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 325, 'wind_gust': 4.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.51}}, {'dt': 1641805200, 'temp': 25.16, 'feels_like': 25.98, 'pressure': 1011, 'humidity': 86, 'dew_point': 22.65, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.18, 'wind_deg': 317, 'wind_gust': 4.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.66}}, {'dt': 1641808800, 'temp': 24.94, 'feels_like': 25.74, 'pressure': 1011, 'humidity': 86, 'dew_point': 22.44, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 3.07, 'wind_deg': 321, 'wind_gust': 4.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.92}}, {'dt': 1641812400, 'temp': 24.92, 'feels_like': 25.71, 'pressure': 1012, 'humidity': 86, 'dew_point': 22.42, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 322, 'wind_gust': 3.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.7}}, {'dt': 1641816000, 'temp': 25.07, 'feels_like': 25.85, 'pressure': 1013, 'humidity': 85, 'dew_point': 22.37, 'uvi': 0.22, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 325, 'wind_gust': 3.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641819600, 'temp': 26.09, 'feels_like': 26.09, 'pressure': 1013, 'humidity': 81, 'dew_point': 22.57, 'uvi': 1.25, 'clouds': 55, 'visibility': 10000, 'wind_speed': 2.62, 'wind_deg': 336, 'wind_gust': 4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641823200, 'temp': 26.94, 'feels_like': 29.25, 'pressure': 1014, 'humidity': 76, 'dew_point': 22.35, 'uvi': 3.39, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 341, 'wind_gust': 3.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641826800, 'temp': 27.6, 'feels_like': 30.14, 'pressure': 1014, 'humidity': 72, 'dew_point': 22.1, 'uvi': 6.2, 'clouds': 79, 'visibility': 10000, 'wind_speed': 3.03, 'wind_deg': 344, 'wind_gust': 3.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641830400, 'temp': 27.72, 'feels_like': 30.37, 'pressure': 1014, 'humidity': 72, 'dew_point': 22.21, 'uvi': 7.95, 'clouds': 84, 'visibility': 10000, 'wind_speed': 3.23, 'wind_deg': 341, 'wind_gust': 3.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 27.82, 'feels_like': 30.57, 'pressure': 1013, 'humidity': 72, 'dew_point': 22.31, 'uvi': 9.01, 'clouds': 87, 'visibility': 10000, 'wind_speed': 3.44, 'wind_deg': 335, 'wind_gust': 3.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641837600, 'temp': 27.8, 'feels_like': 30.66, 'pressure': 1012, 'humidity': 73, 'dew_point': 22.52, 'uvi': 8.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.69, 'wind_deg': 329, 'wind_gust': 3.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641841200, 'temp': 27.78, 'feels_like': 30.62, 'pressure': 1011, 'humidity': 73, 'dew_point': 22.5, 'uvi': 5.9, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.85, 'wind_deg': 328, 'wind_gust': 4.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641844800, 'temp': 27.52, 'feels_like': 30.33, 'pressure': 1010, 'humidity': 75, 'dew_point': 22.69, 'uvi': 3.57, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.15, 'wind_deg': 326, 'wind_gust': 4.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641848400, 'temp': 27.36, 'feels_like': 30.22, 'pressure': 1009, 'humidity': 77, 'dew_point': 22.97, 'uvi': 1.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.17, 'wind_deg': 327, 'wind_gust': 4.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641852000, 'temp': 26.87, 'feels_like': 29.45, 'pressure': 1010, 'humidity': 80, 'dew_point': 23.13, 'uvi': 0.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.17, 'wind_deg': 326, 'wind_gust': 5.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.07, 'feels_like': 26.07, 'pressure': 1011, 'humidity': 83, 'dew_point': 22.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.03, 'wind_deg': 323, 'wind_gust': 5.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 00:00:00 | 56.000000 | 23.120000 | 26.700000 | 85.000000 | 1011.000000 |  | 25.840000 | 0.000000 | 10000.000000 | 330.000000 | 4.59 | 3.100000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 01:00:00 | 67.000000 | 22.960000 | 26.510000 | 85.000000 | 1012.000000 |  | 25.670000 | 0.000000 | 10000.000000 | 338.000000 | 4.61 | 2.920000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 02:00:00 | 68.000000 | 22.910000 | 26.460000 | 85.000000 | 1013.000000 |  | 25.620000 | 0.000000 | 10000.000000 | 341.000000 | 4.7 | 2.840000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 23.150000 | 26.340000 | 87.000000 | 1013.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 344.000000 | 4.66 | 3.000000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 04:00:00 | 74.000000 | 23.000000 | 26.180000 | 87.000000 | 1012.000000 |  | 25.320000 | 0.000000 | 10000.000000 | 346.000000 | 4.82 | 3.290000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 05:00:00 | 74.000000 | 23.150000 | 26.160000 | 88.000000 | 1012.000000 |  | 25.280000 | 0.000000 | 10000.000000 | 340.000000 | 4.69 | 3.270000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 06:00:00 | 85.000000 | 23.260000 | 26.100000 | 89.000000 | 1012.000000 | 0.17 | 25.200000 | 0.000000 | 10000.000000 | 334.000000 | 4.71 | 3.340000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 07:00:00 | 93.000000 | 22.890000 | 26.060000 | 87.000000 | 1011.000000 | 0.5 | 25.210000 | 0.000000 | 10000.000000 | 327.000000 | 4.53 | 3.140000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 08:00:00 | 90.000000 | 22.880000 | 26.050000 | 87.000000 | 1011.000000 | 0.51 | 25.200000 | 0.000000 | 10000.000000 | 325.000000 | 4.67 | 3.190000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 22.650000 | 25.980000 | 86.000000 | 1011.000000 | 0.66 | 25.160000 | 0.000000 | 10000.000000 | 317.000000 | 4.53 | 3.180000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 10:00:00 | 83.000000 | 22.440000 | 25.740000 | 86.000000 | 1011.000000 | 0.92 | 24.940000 | 0.000000 | 10000.000000 | 321.000000 | 4.23 | 3.070000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 11:00:00 | 72.000000 | 22.420000 | 25.710000 | 86.000000 | 1012.000000 | 0.7 | 24.920000 | 0.000000 | 10000.000000 | 322.000000 | 3.94 | 2.780000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 12:00:00 | 40.000000 | 22.370000 | 25.850000 | 85.000000 | 1013.000000 | 0.58 | 25.070000 | 0.220000 | 10000.000000 | 325.000000 | 3.61 | 2.290000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 13:00:00 | 55.000000 | 22.570000 | 26.090000 | 81.000000 | 1013.000000 | 0.33 | 26.090000 | 1.250000 | 10000.000000 | 336.000000 | 4 | 2.620000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 14:00:00 | 68.000000 | 22.350000 | 29.250000 | 76.000000 | 1014.000000 | 0.22 | 26.940000 | 3.390000 | 10000.000000 | 341.000000 | 3.54 | 2.780000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 22.100000 | 30.140000 | 72.000000 | 1014.000000 | 0.17 | 27.600000 | 6.200000 | 10000.000000 | 344.000000 | 3.52 | 3.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 16:00:00 | 84.000000 | 22.210000 | 30.370000 | 72.000000 | 1014.000000 | 0.12 | 27.720000 | 7.950000 | 10000.000000 | 341.000000 | 3.63 | 3.230000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 17:00:00 | 87.000000 | 22.310000 | 30.570000 | 72.000000 | 1013.000000 | 0.23 | 27.820000 | 9.010000 | 10000.000000 | 335.000000 | 3.69 | 3.440000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 22.520000 | 30.660000 | 73.000000 | 1012.000000 | 0.22 | 27.800000 | 8.470000 | 10000.000000 | 329.000000 | 3.98 | 3.690000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 22.500000 | 30.620000 | 73.000000 | 1011.000000 | 0.22 | 27.780000 | 5.900000 | 10000.000000 | 328.000000 | 4.11 | 3.850000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 22.690000 | 30.330000 | 75.000000 | 1010.000000 | 0.2 | 27.520000 | 3.570000 | 10000.000000 | 326.000000 | 4.39 | 4.150000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 22.970000 | 30.220000 | 77.000000 | 1009.000000 | 0.13 | 27.360000 | 1.520000 | 10000.000000 | 327.000000 | 4.66 | 4.170000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 23.130000 | 29.450000 | 80.000000 | 1010.000000 |  | 26.870000 | 0.380000 | 10000.000000 | 326.000000 | 5.22 | 4.170000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11155030 | "CAPURGANA - AUT [11155030]" | 8.616250 | -77.328194 | 19.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-04-16 00:00:00 | NaT | Chocó | Acandí | Magdalena | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tolo y otros Directos al Caribe | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 22.960000 | 26.070000 | 83.000000 | 1011.000000 |  | 26.070000 | 0.000000 | 10000.000000 | 323.000000 | 5.38 | 4.030000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station11155030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station11155030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station11155030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11155030_OWM_Windspeed_20220111.png)
