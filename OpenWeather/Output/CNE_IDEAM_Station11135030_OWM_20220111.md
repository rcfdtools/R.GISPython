
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNGUIA - AUT [11135030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station11135030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.03672222,-77.08786111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.03672222&lon=-77.08786111)


| Parameter | Value |
|---|---|
| Code | 11135030 |
| Name | UNGUIA - AUT [11135030] |
| Latitude, ° | 8.03672222 |
| Longitude, ° | -77.08786111 |
| Elevation, m | 14 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-09-23 19:00:00 |
| Suspension date | NaT |
| State | Chocó |
| County | Unguía |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Atrato - Darién |
| SZH - Hydrographic subzone | Río Tanela y otros Directos al Caribe |

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

### (CNE index 298) Open Weather values for station 11135030 - UNGUIA - AUT [11135030]

JSON data from API OWM:

```
{'lat': 8.0367, 'lon': -77.0879, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813906, 'sunset': 1641855976, 'temp': 28.06, 'feels_like': 31.79, 'pressure': 1010, 'humidity': 77, 'dew_point': 23.65, 'uvi': 3.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 17, 'wind_gust': 2.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, 'hourly': [{'dt': 1641772800, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1011, 'humidity': 89, 'dew_point': 24.1, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 343, 'wind_gust': 3.84, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1012, 'humidity': 90, 'dew_point': 24.29, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 333, 'wind_gust': 3.52, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 23.78, 'feels_like': 24.59, 'pressure': 1012, 'humidity': 91, 'dew_point': 22.22, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 323, 'wind_gust': 3.43, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 23.58, 'feels_like': 24.4, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.2, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 322, 'wind_gust': 3.44, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 23.4, 'feels_like': 24.2, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.03, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 311, 'wind_gust': 3.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 23.11, 'feels_like': 23.9, 'pressure': 1012, 'humidity': 93, 'dew_point': 21.92, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 310, 'wind_gust': 2.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 22.78, 'feels_like': 23.57, 'pressure': 1012, 'humidity': 94, 'dew_point': 21.76, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 298, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641798000, 'temp': 22.59, 'feels_like': 23.39, 'pressure': 1011, 'humidity': 95, 'dew_point': 21.75, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 302, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641801600, 'temp': 22.43, 'feels_like': 23.21, 'pressure': 1011, 'humidity': 95, 'dew_point': 21.59, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 288, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641805200, 'temp': 22.28, 'feels_like': 23.04, 'pressure': 1011, 'humidity': 95, 'dew_point': 21.44, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 282, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 22.17, 'feels_like': 22.95, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.5, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 282, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641812400, 'temp': 25.06, 'feels_like': 26.15, 'pressure': 1012, 'humidity': 97, 'dew_point': 24.55, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 267, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641816000, 'temp': 25.06, 'feels_like': 26.1, 'pressure': 1013, 'humidity': 95, 'dew_point': 24.2, 'uvi': 0.25, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 278, 'wind_gust': 1.31, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 25.06, 'feels_like': 25.92, 'pressure': 1014, 'humidity': 88, 'dew_point': 22.93, 'uvi': 1.28, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 217, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1015, 'humidity': 78, 'dew_point': 21.92, 'uvi': 3.47, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 191, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.06, 'feels_like': 28.7, 'pressure': 1014, 'humidity': 67, 'dew_point': 20.41, 'uvi': 6.32, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 82, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 27.06, 'feels_like': 28.46, 'pressure': 1014, 'humidity': 64, 'dew_point': 19.67, 'uvi': 7.73, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 47, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.06, 'feels_like': 30.39, 'pressure': 1013, 'humidity': 67, 'dew_point': 21.36, 'uvi': 8.77, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 42, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641837600, 'temp': 28.06, 'feels_like': 31.49, 'pressure': 1012, 'humidity': 75, 'dew_point': 23.21, 'uvi': 8.23, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 29, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641841200, 'temp': 28.06, 'feels_like': 31.94, 'pressure': 1011, 'humidity': 78, 'dew_point': 23.86, 'uvi': 5.44, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 17, 'wind_gust': 2.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641844800, 'temp': 28.06, 'feels_like': 31.79, 'pressure': 1010, 'humidity': 77, 'dew_point': 23.65, 'uvi': 3.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 17, 'wind_gust': 2.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641848400, 'temp': 28.06, 'feels_like': 31.79, 'pressure': 1009, 'humidity': 77, 'dew_point': 23.65, 'uvi': 1.42, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 12, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641852000, 'temp': 27.06, 'feels_like': 30.38, 'pressure': 1010, 'humidity': 85, 'dew_point': 24.32, 'uvi': 0.46, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 19, 'wind_gust': 2.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641855600, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1011, 'humidity': 89, 'dew_point': 24.1, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 357, 'wind_gust': 3.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 00:00:00 | 7.000000 | 24.100000 | 26.060000 | 89.000000 | 1011.000000 |  | 26.060000 | 0.000000 | 10000.000000 | 343.000000 | 3.84 | 1.660000 | 800 | Clear | clear sky | 01n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 01:00:00 | 22.000000 | 24.290000 | 26.060000 | 90.000000 | 1012.000000 |  | 26.060000 | 0.000000 | 10000.000000 | 333.000000 | 3.52 | 1.660000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 02:00:00 | 19.000000 | 22.220000 | 24.590000 | 91.000000 | 1012.000000 |  | 23.780000 | 0.000000 | 10000.000000 | 323.000000 | 3.43 | 1.630000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 03:00:00 | 33.000000 | 22.200000 | 24.400000 | 92.000000 | 1012.000000 |  | 23.580000 | 0.000000 | 10000.000000 | 322.000000 | 3.44 | 1.670000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 04:00:00 | 47.000000 | 22.030000 | 24.200000 | 92.000000 | 1012.000000 |  | 23.400000 | 0.000000 | 10000.000000 | 311.000000 | 3.24 | 1.570000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 05:00:00 | 48.000000 | 21.920000 | 23.900000 | 93.000000 | 1012.000000 |  | 23.110000 | 0.000000 | 10000.000000 | 310.000000 | 2.99 | 1.550000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 21.760000 | 23.570000 | 94.000000 | 1012.000000 | 0.22 | 22.780000 | 0.000000 | 10000.000000 | 298.000000 | 2.38 | 1.550000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 07:00:00 | 36.000000 | 21.750000 | 23.390000 | 95.000000 | 1011.000000 | 0.32 | 22.590000 | 0.000000 | 10000.000000 | 302.000000 | 1.55 | 1.190000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 08:00:00 | 37.000000 | 21.590000 | 23.210000 | 95.000000 | 1011.000000 | 0.33 | 22.430000 | 0.000000 | 10000.000000 | 288.000000 | 1.72 | 1.190000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 09:00:00 | 37.000000 | 21.440000 | 23.040000 | 95.000000 | 1011.000000 | 0.23 | 22.280000 | 0.000000 | 10000.000000 | 282.000000 | 1.62 | 0.970000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 10:00:00 | 40.000000 | 21.500000 | 22.950000 | 96.000000 | 1012.000000 | 0.13 | 22.170000 | 0.000000 | 10000.000000 | 282.000000 | 1.45 | 0.760000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 11:00:00 | 51.000000 | 24.550000 | 26.150000 | 97.000000 | 1012.000000 | 0.11 | 25.060000 | 0.000000 | 10000.000000 | 267.000000 | 1.34 | 0.880000 | 500 | Rain | light rain | 10n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 12:00:00 | 50.000000 | 24.200000 | 26.100000 | 95.000000 | 1013.000000 |  | 25.060000 | 0.250000 | 10000.000000 | 278.000000 | 1.31 | 0.780000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 13:00:00 | 71.000000 | 22.930000 | 25.920000 | 88.000000 | 1014.000000 |  | 25.060000 | 1.280000 | 10000.000000 | 217.000000 | 1.27 | 0.590000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 21.920000 | 26.060000 | 78.000000 | 1015.000000 |  | 26.060000 | 3.470000 | 10000.000000 | 191.000000 | 1.03 | 0.550000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 15:00:00 | 90.000000 | 20.410000 | 28.700000 | 67.000000 | 1014.000000 |  | 27.060000 | 6.320000 | 10000.000000 | 82.000000 | 1.47 | 0.200000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 16:00:00 | 92.000000 | 19.670000 | 28.460000 | 64.000000 | 1014.000000 |  | 27.060000 | 7.730000 | 10000.000000 | 47.000000 | 1.84 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 17:00:00 | 94.000000 | 21.360000 | 30.390000 | 67.000000 | 1013.000000 | 0.21 | 28.060000 | 8.770000 | 10000.000000 | 42.000000 | 1.9 | 1.180000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 23.210000 | 31.490000 | 75.000000 | 1012.000000 | 0.53 | 28.060000 | 8.230000 | 10000.000000 | 29.000000 | 1.83 | 1.300000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 23.860000 | 31.940000 | 78.000000 | 1011.000000 | 0.47 | 28.060000 | 5.440000 | 10000.000000 | 17.000000 | 2.28 | 1.580000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 23.650000 | 31.790000 | 77.000000 | 1010.000000 | 0.46 | 28.060000 | 3.300000 | 10000.000000 | 17.000000 | 2.2 | 1.370000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 23.650000 | 31.790000 | 77.000000 | 1009.000000 | 0.36 | 28.060000 | 1.420000 | 10000.000000 | 12.000000 | 2.26 | 1.350000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 24.320000 | 30.380000 | 85.000000 | 1010.000000 | 0.29 | 27.060000 | 0.460000 | 10000.000000 | 19.000000 | 2.99 | 1.250000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 11135030 | "UNGUIA - AUT [11135030]" | 8.036722 | -77.087861 | 14.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 19:00:00 | NaT | Chocó | Unguía | 0 | Area Operativa 01 - Antioquia-Chocó | Caribe | Atrato - Darién | Río Tanela y otros Directos al Caribe | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 24.100000 | 26.060000 | 89.000000 | 1011.000000 | 0.12 | 26.060000 | 0.000000 | 10000.000000 | 357.000000 | 3.19 | 1.190000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station11135030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station11135030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station11135030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station11135030_OWM_Windspeed_20220111.png)
