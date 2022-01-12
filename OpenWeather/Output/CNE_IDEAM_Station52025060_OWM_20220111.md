
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52025060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.91,-77.19) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.91&lon=-77.19)


| Parameter | Value |
|---|---|
| Code | 52025060 |
| Name | GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060] |
| Latitude, ° | 1.91 |
| Longitude, ° | -77.19 |
| Elevation, m | 580 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1992-08-15 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Mercaderes |
| Stream | 0 |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Patia Alto |

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

### (CNE index 4456) Open Weather values for station 52025060 - GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]

JSON data from API OWM:

```
{'lat': 1.91, 'lon': -77.19, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813335, 'sunset': 1641856596, 'temp': 25.64, 'feels_like': 26.4, 'pressure': 1012, 'humidity': 82, 'dew_point': 22.34, 'uvi': 4.44, 'clouds': 85, 'visibility': 8015, 'wind_speed': 1.96, 'wind_deg': 262, 'wind_gust': 2.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, 'hourly': [{'dt': 1641772800, 'temp': 25.64, 'feels_like': 26.77, 'pressure': 1013, 'humidity': 96, 'dew_point': 24.95, 'uvi': 0, 'clouds': 100, 'visibility': 5562, 'wind_speed': 1.22, 'wind_deg': 259, 'wind_gust': 2.13, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.17}}, {'dt': 1641776400, 'temp': 21.71, 'feels_like': 22.44, 'pressure': 1015, 'humidity': 96, 'dew_point': 21.04, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 263, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.61}}, {'dt': 1641780000, 'temp': 21.77, 'feels_like': 22.48, 'pressure': 1016, 'humidity': 95, 'dew_point': 20.93, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 266, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641783600, 'temp': 21.63, 'feels_like': 22.36, 'pressure': 1016, 'humidity': 96, 'dew_point': 20.96, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 265, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641787200, 'temp': 21.51, 'feels_like': 22.22, 'pressure': 1016, 'humidity': 96, 'dew_point': 20.85, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 251, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 21.34, 'feels_like': 22.04, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.68, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 279, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641794400, 'temp': 21.68, 'feels_like': 22.44, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.18, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 285, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641798000, 'temp': 21.6, 'feels_like': 22.35, 'pressure': 1014, 'humidity': 97, 'dew_point': 21.1, 'uvi': 0, 'clouds': 100, 'visibility': 8008, 'wind_speed': 0.29, 'wind_deg': 308, 'wind_gust': 0.68, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.02}}, {'dt': 1641801600, 'temp': 21.44, 'feels_like': 22.17, 'pressure': 1014, 'humidity': 97, 'dew_point': 20.94, 'uvi': 0, 'clouds': 100, 'visibility': 9306, 'wind_speed': 0.4, 'wind_deg': 267, 'wind_gust': 0.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.22}}, {'dt': 1641805200, 'temp': 21.43, 'feels_like': 22.19, 'pressure': 1014, 'humidity': 98, 'dew_point': 21.1, 'uvi': 0, 'clouds': 100, 'visibility': 7974, 'wind_speed': 0.48, 'wind_deg': 249, 'wind_gust': 0.74, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.12}}, {'dt': 1641808800, 'temp': 21.49, 'feels_like': 22.25, 'pressure': 1014, 'humidity': 98, 'dew_point': 21.16, 'uvi': 0, 'clouds': 100, 'visibility': 8821, 'wind_speed': 0.39, 'wind_deg': 240, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.91}}, {'dt': 1641812400, 'temp': 22.64, 'feels_like': 23.52, 'pressure': 1015, 'humidity': 98, 'dew_point': 22.31, 'uvi': 0, 'clouds': 100, 'visibility': 8720, 'wind_speed': 0.59, 'wind_deg': 234, 'wind_gust': 0.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.16}}, {'dt': 1641816000, 'temp': 22.64, 'feels_like': 23.52, 'pressure': 1015, 'humidity': 98, 'dew_point': 22.31, 'uvi': 0.28, 'clouds': 97, 'visibility': 7758, 'wind_speed': 0.54, 'wind_deg': 257, 'wind_gust': 0.84, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.8}}, {'dt': 1641819600, 'temp': 23.64, 'feels_like': 24.57, 'pressure': 1016, 'humidity': 96, 'dew_point': 22.96, 'uvi': 1.32, 'clouds': 100, 'visibility': 6541, 'wind_speed': 0.67, 'wind_deg': 260, 'wind_gust': 1.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.67}}, {'dt': 1641823200, 'temp': 24.64, 'feels_like': 25.64, 'pressure': 1017, 'humidity': 95, 'dew_point': 23.78, 'uvi': 3.38, 'clouds': 100, 'visibility': 5558, 'wind_speed': 0.98, 'wind_deg': 266, 'wind_gust': 1.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.12}}, {'dt': 1641826800, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1017, 'humidity': 94, 'dew_point': 25.59, 'uvi': 5.96, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 258, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.51}}, {'dt': 1641830400, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1016, 'humidity': 89, 'dew_point': 24.68, 'uvi': 9.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 230, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641834000, 'temp': 27.64, 'feels_like': 31.62, 'pressure': 1015, 'humidity': 83, 'dew_point': 24.49, 'uvi': 10.69, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 250, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641837600, 'temp': 27.64, 'feels_like': 31.09, 'pressure': 1013, 'humidity': 79, 'dew_point': 23.67, 'uvi': 10.07, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 265, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.84}}, {'dt': 1641841200, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1012, 'humidity': 80, 'dew_point': 22.9, 'uvi': 7.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 263, 'wind_gust': 2.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641844800, 'temp': 25.64, 'feels_like': 26.4, 'pressure': 1012, 'humidity': 82, 'dew_point': 22.34, 'uvi': 4.44, 'clouds': 85, 'visibility': 8015, 'wind_speed': 1.96, 'wind_deg': 262, 'wind_gust': 2.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, {'dt': 1641848400, 'temp': 25.64, 'feels_like': 26.4, 'pressure': 1011, 'humidity': 82, 'dew_point': 22.34, 'uvi': 2.01, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 261, 'wind_gust': 2.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641852000, 'temp': 25.64, 'feels_like': 26.51, 'pressure': 1012, 'humidity': 86, 'dew_point': 23.12, 'uvi': 0.42, 'clouds': 70, 'visibility': 8579, 'wind_speed': 1.69, 'wind_deg': 261, 'wind_gust': 2.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}, {'dt': 1641855600, 'temp': 24.64, 'feels_like': 25.59, 'pressure': 1013, 'humidity': 93, 'dew_point': 23.43, 'uvi': 0, 'clouds': 67, 'visibility': 6408, 'wind_speed': 1.5, 'wind_deg': 255, 'wind_gust': 2.1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.05}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 24.950000 | 26.770000 | 96.000000 | 1013.000000 | 1.17 | 25.640000 | 0.000000 | 5562.000000 | 259.000000 | 2.13 | 1.220000 | 501 | Rain | moderate rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 21.040000 | 22.440000 | 96.000000 | 1015.000000 | 0.61 | 21.710000 | 0.000000 | 10000.000000 | 263.000000 | 1.57 | 0.860000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 20.930000 | 22.480000 | 95.000000 | 1016.000000 | 0.3 | 21.770000 | 0.000000 | 10000.000000 | 266.000000 | 1.15 | 0.630000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 03:00:00 | 98.000000 | 20.960000 | 22.360000 | 96.000000 | 1016.000000 | 0.39 | 21.630000 | 0.000000 | 10000.000000 | 265.000000 | 0.99 | 0.610000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 20.850000 | 22.220000 | 96.000000 | 1016.000000 | 0.13 | 21.510000 | 0.000000 | 10000.000000 | 251.000000 | 0.67 | 0.250000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 20.680000 | 22.040000 | 96.000000 | 1015.000000 | 0.19 | 21.340000 | 0.000000 | 10000.000000 | 279.000000 | 0.69 | 0.470000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 21.180000 | 22.440000 | 97.000000 | 1015.000000 | 0.49 | 21.680000 | 0.000000 | 10000.000000 | 285.000000 | 0.53 | 0.320000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 21.100000 | 22.350000 | 97.000000 | 1014.000000 | 1.02 | 21.600000 | 0.000000 | 8008.000000 | 308.000000 | 0.68 | 0.290000 | 501 | Rain | moderate rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 20.940000 | 22.170000 | 97.000000 | 1014.000000 | 1.22 | 21.440000 | 0.000000 | 9306.000000 | 267.000000 | 0.62 | 0.400000 | 501 | Rain | moderate rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 21.100000 | 22.190000 | 98.000000 | 1014.000000 | 1.12 | 21.430000 | 0.000000 | 7974.000000 | 249.000000 | 0.74 | 0.480000 | 501 | Rain | moderate rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 21.160000 | 22.250000 | 98.000000 | 1014.000000 | 0.91 | 21.490000 | 0.000000 | 8821.000000 | 240.000000 | 0.66 | 0.390000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 22.310000 | 23.520000 | 98.000000 | 1015.000000 | 1.16 | 22.640000 | 0.000000 | 8720.000000 | 234.000000 | 0.86 | 0.590000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 12:00:00 | 97.000000 | 22.310000 | 23.520000 | 98.000000 | 1015.000000 | 1.8 | 22.640000 | 0.280000 | 7758.000000 | 257.000000 | 0.84 | 0.540000 | 501 | Rain | moderate rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 22.960000 | 24.570000 | 96.000000 | 1016.000000 | 2.67 | 23.640000 | 1.320000 | 6541.000000 | 260.000000 | 1.02 | 0.670000 | 501 | Rain | moderate rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 23.780000 | 25.640000 | 95.000000 | 1017.000000 | 3.12 | 24.640000 | 3.380000 | 5558.000000 | 266.000000 | 1.51 | 0.980000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 25.590000 | 26.640000 | 94.000000 | 1017.000000 | 1.51 | 26.640000 | 5.960000 | 10000.000000 | 258.000000 | 1.26 | 0.610000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 24.680000 | 26.640000 | 89.000000 | 1016.000000 | 0.62 | 26.640000 | 9.480000 | 10000.000000 | 230.000000 | 1.66 | 1.090000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 24.490000 | 31.620000 | 83.000000 | 1015.000000 | 0.81 | 27.640000 | 10.690000 | 10000.000000 | 250.000000 | 2.1 | 1.620000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 18:00:00 | 97.000000 | 23.670000 | 31.090000 | 79.000000 | 1013.000000 | 0.84 | 27.640000 | 10.070000 | 10000.000000 | 265.000000 | 1.93 | 1.590000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 22.900000 | 26.640000 | 80.000000 | 1012.000000 | 1.15 | 26.640000 | 7.140000 | 10000.000000 | 263.000000 | 2.18 | 1.790000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 20:00:00 | 85.000000 | 22.340000 | 26.400000 | 82.000000 | 1012.000000 | 1.26 | 25.640000 | 4.440000 | 8015.000000 | 262.000000 | 2.4 | 1.960000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 21:00:00 | 72.000000 | 22.340000 | 26.400000 | 82.000000 | 1011.000000 | 1.03 | 25.640000 | 2.010000 | 10000.000000 | 261.000000 | 2.44 | 1.920000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 22:00:00 | 70.000000 | 23.120000 | 26.510000 | 86.000000 | 1012.000000 | 0.95 | 25.640000 | 0.420000 | 8579.000000 | 261.000000 | 2.35 | 1.690000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025060 | "GRANJA EXPERIMENTAL UNIVERSIDAD DE NARIÑO [52025060]" | 1.910000 | -77.190000 | 580.000000 | Climática Principal | Convencional | Activa | 1992-08-15 00:00:00 | NaT | Cauca | Mercaderes | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 23:00:00 | 67.000000 | 23.430000 | 25.590000 | 93.000000 | 1013.000000 | 1.05 | 24.640000 | 0.000000 | 6408.000000 | 255.000000 | 2.1 | 1.500000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52025060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52025060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52025060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025060_OWM_Windspeed_20220111.png)
