
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA AGRICOLA MOGOTES [24025040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24025040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.47,-72.96888889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.47&lon=-72.96888889)


| Parameter | Value |
|---|---|
| Code | 24025040 |
| Name | ESCUELA AGRICOLA MOGOTES [24025040] |
| Latitude, ° | 6.47 |
| Longitude, ° | -72.96888889 |
| Elevation, m | 1673 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1973-11-15 00:00:00 |
| Suspension date | NaT |
| State | Santander |
| County | Mogotes |
| Stream | Nevado |
| Operator | Area Operativa 08 - Santanderes-Arauca |
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

### (CNE index 887) Open Weather values for station 24025040 - ESCUELA AGRICOLA MOGOTES [24025040]

JSON data from API OWM:

```
{'lat': 6.47, 'lon': -72.9689, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812764, 'sunset': 1641855140, 'temp': 22.23, 'feels_like': 22.08, 'pressure': 1010, 'humidity': 60, 'dew_point': 14.1, 'uvi': 4.37, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.58, 'wind_deg': 311, 'wind_gust': 2.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.64, 'feels_like': 15.79, 'pressure': 1015, 'humidity': 97, 'dew_point': 15.17, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 91, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641776400, 'temp': 15.23, 'feels_like': 15.34, 'pressure': 1016, 'humidity': 97, 'dew_point': 14.76, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 125, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641780000, 'temp': 14.86, 'feels_like': 14.93, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.39, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 137, 'wind_gust': 0.82, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 14.52, 'feels_like': 14.56, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.05, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 147, 'wind_gust': 0.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 14.18, 'feels_like': 14.19, 'pressure': 1017, 'humidity': 97, 'dew_point': 13.71, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 149, 'wind_gust': 0.96, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 13.9, 'feels_like': 13.85, 'pressure': 1016, 'humidity': 96, 'dew_point': 13.27, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 139, 'wind_gust': 0.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 13.94, 'feels_like': 13.9, 'pressure': 1016, 'humidity': 96, 'dew_point': 13.31, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 141, 'wind_gust': 0.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 13.86, 'feels_like': 13.81, 'pressure': 1015, 'humidity': 96, 'dew_point': 13.23, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 120, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14.33, 'feels_like': 14.3, 'pressure': 1014, 'humidity': 95, 'dew_point': 13.54, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 108, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 14.57, 'feels_like': 14.54, 'pressure': 1014, 'humidity': 94, 'dew_point': 13.62, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 98, 'wind_gust': 0.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 14.54, 'feels_like': 14.5, 'pressure': 1015, 'humidity': 94, 'dew_point': 13.59, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 65, 'wind_gust': 0.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 14.43, 'feels_like': 14.38, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.48, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 102, 'wind_gust': 0.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 15.14, 'feels_like': 15.14, 'pressure': 1017, 'humidity': 93, 'dew_point': 14.02, 'uvi': 0.58, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 349, 'wind_gust': 0.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 16.15, 'feels_like': 16.2, 'pressure': 1018, 'humidity': 91, 'dew_point': 14.68, 'uvi': 1.27, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 359, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 17.22, 'feels_like': 17.24, 'pressure': 1018, 'humidity': 86, 'dew_point': 14.86, 'uvi': 2.95, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 334, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641826800, 'temp': 19.52, 'feels_like': 19.46, 'pressure': 1017, 'humidity': 74, 'dew_point': 14.77, 'uvi': 4.88, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 300, 'wind_gust': 0.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 21.55, 'feels_like': 21.43, 'pressure': 1016, 'humidity': 64, 'dew_point': 14.46, 'uvi': 11.2, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 301, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 23.45, 'feels_like': 23.26, 'pressure': 1014, 'humidity': 54, 'dew_point': 13.62, 'uvi': 11.98, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 305, 'wind_gust': 1.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 24.14, 'feels_like': 23.97, 'pressure': 1012, 'humidity': 52, 'dew_point': 13.68, 'uvi': 10.65, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 314, 'wind_gust': 1.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 24, 'feels_like': 23.81, 'pressure': 1010, 'humidity': 52, 'dew_point': 13.55, 'uvi': 7.8, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.76, 'wind_deg': 313, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 22.23, 'feels_like': 22.08, 'pressure': 1010, 'humidity': 60, 'dew_point': 14.1, 'uvi': 4.37, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.58, 'wind_deg': 311, 'wind_gust': 2.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 20.86, 'feels_like': 20.88, 'pressure': 1011, 'humidity': 72, 'dew_point': 15.63, 'uvi': 1.67, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 313, 'wind_gust': 2.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1641852000, 'temp': 19.31, 'feels_like': 19.46, 'pressure': 1012, 'humidity': 83, 'dew_point': 16.35, 'uvi': 0.3, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 310, 'wind_gust': 2.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641855600, 'temp': 16.57, 'feels_like': 16.71, 'pressure': 1013, 'humidity': 93, 'dew_point': 15.43, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 306, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 15.170000 | 15.790000 | 97.000000 | 1015.000000 | 0.13 | 15.640000 | 0.000000 | 10000.000000 | 91.000000 | 0.73 | 0.260000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 01:00:00 | 23.000000 | 14.760000 | 15.340000 | 97.000000 | 1016.000000 | 0.17 | 15.230000 | 0.000000 | 10000.000000 | 125.000000 | 0.72 | 0.540000 | 500 | Rain | light rain | 10n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 02:00:00 | 24.000000 | 14.390000 | 14.930000 | 97.000000 | 1017.000000 |  | 14.860000 | 0.000000 | 10000.000000 | 137.000000 | 0.82 | 0.900000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 03:00:00 | 26.000000 | 14.050000 | 14.560000 | 97.000000 | 1017.000000 |  | 14.520000 | 0.000000 | 10000.000000 | 147.000000 | 0.92 | 1.120000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 04:00:00 | 31.000000 | 13.710000 | 14.190000 | 97.000000 | 1017.000000 |  | 14.180000 | 0.000000 | 10000.000000 | 149.000000 | 0.96 | 1.190000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 05:00:00 | 33.000000 | 13.270000 | 13.850000 | 96.000000 | 1016.000000 |  | 13.900000 | 0.000000 | 10000.000000 | 139.000000 | 0.86 | 1.060000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 06:00:00 | 44.000000 | 13.310000 | 13.900000 | 96.000000 | 1016.000000 |  | 13.940000 | 0.000000 | 10000.000000 | 141.000000 | 0.69 | 0.880000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 07:00:00 | 54.000000 | 13.230000 | 13.810000 | 96.000000 | 1015.000000 |  | 13.860000 | 0.000000 | 10000.000000 | 120.000000 | 0.75 | 0.880000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 08:00:00 | 66.000000 | 13.540000 | 14.300000 | 95.000000 | 1014.000000 |  | 14.330000 | 0.000000 | 10000.000000 | 108.000000 | 0.74 | 0.690000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 09:00:00 | 76.000000 | 13.620000 | 14.540000 | 94.000000 | 1014.000000 |  | 14.570000 | 0.000000 | 10000.000000 | 98.000000 | 0.68 | 0.540000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 10:00:00 | 81.000000 | 13.590000 | 14.500000 | 94.000000 | 1015.000000 |  | 14.540000 | 0.000000 | 10000.000000 | 65.000000 | 0.54 | 0.300000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 11:00:00 | 84.000000 | 13.480000 | 14.380000 | 94.000000 | 1016.000000 |  | 14.430000 | 0.000000 | 10000.000000 | 102.000000 | 0.61 | 0.460000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 12:00:00 | 82.000000 | 14.020000 | 15.140000 | 93.000000 | 1017.000000 |  | 15.140000 | 0.580000 | 10000.000000 | 349.000000 | 0.56 | 0.190000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 13:00:00 | 97.000000 | 14.680000 | 16.200000 | 91.000000 | 1018.000000 |  | 16.150000 | 1.270000 | 10000.000000 | 359.000000 | 0.61 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 14.860000 | 17.240000 | 86.000000 | 1018.000000 | 0.11 | 17.220000 | 2.950000 | 10000.000000 | 334.000000 | 0.59 | 0.510000 | 500 | Rain | light rain | 10d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 15:00:00 | 95.000000 | 14.770000 | 19.460000 | 74.000000 | 1017.000000 |  | 19.520000 | 4.880000 | 10000.000000 | 300.000000 | 0.72 | 1.160000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 16:00:00 | 95.000000 | 14.460000 | 21.430000 | 64.000000 | 1016.000000 |  | 21.550000 | 11.200000 | 10000.000000 | 301.000000 | 1.11 | 1.540000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 17:00:00 | 84.000000 | 13.620000 | 23.260000 | 54.000000 | 1014.000000 |  | 23.450000 | 11.980000 | 10000.000000 | 305.000000 | 1.57 | 2.050000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 18:00:00 | 73.000000 | 13.680000 | 23.970000 | 52.000000 | 1012.000000 |  | 24.140000 | 10.650000 | 10000.000000 | 314.000000 | 1.71 | 2.320000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 19:00:00 | 92.000000 | 13.550000 | 23.810000 | 52.000000 | 1010.000000 |  | 24.000000 | 7.800000 | 10000.000000 | 313.000000 | 1.88 | 2.760000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 20:00:00 | 95.000000 | 14.100000 | 22.080000 | 60.000000 | 1010.000000 |  | 22.230000 | 4.370000 | 10000.000000 | 311.000000 | 2.76 | 2.580000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 21:00:00 | 96.000000 | 15.630000 | 20.880000 | 72.000000 | 1011.000000 | 0.27 | 20.860000 | 1.670000 | 10000.000000 | 313.000000 | 2.87 | 2.200000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 22:00:00 | 97.000000 | 16.350000 | 19.460000 | 83.000000 | 1012.000000 | 0.23 | 19.310000 | 0.300000 | 10000.000000 | 310.000000 | 2.33 | 1.610000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24025040 | "ESCUELA AGRICOLA MOGOTES [24025040]" | 6.470000 | -72.968889 | 1673.000000 | Climática Principal | Convencional | Activa | 1973-11-15 00:00:00 | NaT | Santander | Mogotes | Nevado | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Fonce | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 15.430000 | 16.710000 | 93.000000 | 1013.000000 | 0.18 | 16.570000 | 0.000000 | 10000.000000 | 306.000000 | 0.94 | 0.870000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24025040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24025040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24025040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025040_OWM_Windspeed_20220111.png)
