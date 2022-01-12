
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO GUAPI - AUT [53045040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station53045040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.57441667,-77.89475) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.57441667&lon=-77.89475)


| Parameter | Value |
|---|---|
| Code | 53045040 |
| Name | AEROPUERTO GUAPI - AUT [53045040] |
| Latitude, ° | 2.57441667 |
| Longitude, ° | -77.89475 |
| Elevation, m | 42 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-03-01 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Guapi |
| Stream | Paez |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Tapaje - Dagua - Directos |
| SZH - Hydrographic subzone | Río Guapi |

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

### (CNE index 65) Open Weather values for station 53045040 - AEROPUERTO GUAPI - AUT [53045040]

JSON data from API OWM:

```
{'lat': 2.5744, 'lon': -77.8948, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813568, 'sunset': 1641856701, 'temp': 25.93, 'feels_like': 26.82, 'pressure': 1011, 'humidity': 86, 'dew_point': 23.41, 'uvi': 5.73, 'clouds': 82, 'visibility': 7402, 'wind_speed': 2.44, 'wind_deg': 276, 'wind_gust': 3.67, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, 'hourly': [{'dt': 1641772800, 'temp': 23.98, 'feels_like': 24.81, 'pressure': 1011, 'humidity': 91, 'dew_point': 22.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 248, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641776400, 'temp': 23.66, 'feels_like': 24.51, 'pressure': 1012, 'humidity': 93, 'dew_point': 22.46, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 221, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.8}}, {'dt': 1641780000, 'temp': 23.6, 'feels_like': 24.44, 'pressure': 1013, 'humidity': 93, 'dew_point': 22.4, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 196, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 23.46, 'feels_like': 24.32, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.44, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 180, 'wind_gust': 2.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.2, 'feels_like': 24.08, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.53, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 184, 'wind_gust': 2.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641790800, 'temp': 23, 'feels_like': 23.86, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.33, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 188, 'wind_gust': 2.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641794400, 'temp': 22.98, 'feels_like': 23.84, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.31, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 197, 'wind_gust': 3.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641798000, 'temp': 22.83, 'feels_like': 23.7, 'pressure': 1012, 'humidity': 97, 'dew_point': 22.33, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 203, 'wind_gust': 4.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641801600, 'temp': 22.69, 'feels_like': 23.55, 'pressure': 1011, 'humidity': 97, 'dew_point': 22.19, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 195, 'wind_gust': 5.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641805200, 'temp': 22.57, 'feels_like': 23.42, 'pressure': 1011, 'humidity': 97, 'dew_point': 22.07, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 193, 'wind_gust': 5.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641808800, 'temp': 22.48, 'feels_like': 23.32, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.98, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 196, 'wind_gust': 5.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641812400, 'temp': 22.43, 'feels_like': 23.24, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.76, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 193, 'wind_gust': 5.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1641816000, 'temp': 22.88, 'feels_like': 23.73, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.21, 'uvi': 0.32, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 196, 'wind_gust': 5.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641819600, 'temp': 24.21, 'feels_like': 25.09, 'pressure': 1014, 'humidity': 92, 'dew_point': 22.83, 'uvi': 1.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 201, 'wind_gust': 4.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641823200, 'temp': 25.43, 'feels_like': 26.33, 'pressure': 1014, 'humidity': 88, 'dew_point': 23.3, 'uvi': 4.41, 'clouds': 94, 'visibility': 7599, 'wind_speed': 2.65, 'wind_deg': 224, 'wind_gust': 5.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641826800, 'temp': 26.03, 'feels_like': 26.03, 'pressure': 1015, 'humidity': 86, 'dew_point': 23.5, 'uvi': 7.89, 'clouds': 94, 'visibility': 10000, 'wind_speed': 3.18, 'wind_deg': 238, 'wind_gust': 5.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.38}}, {'dt': 1641830400, 'temp': 26.41, 'feels_like': 26.41, 'pressure': 1014, 'humidity': 85, 'dew_point': 23.68, 'uvi': 11.02, 'clouds': 89, 'visibility': 9155, 'wind_speed': 3.44, 'wind_deg': 249, 'wind_gust': 5.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641834000, 'temp': 26.55, 'feels_like': 26.55, 'pressure': 1013, 'humidity': 85, 'dew_point': 23.82, 'uvi': 12.51, 'clouds': 90, 'visibility': 6342, 'wind_speed': 3.29, 'wind_deg': 258, 'wind_gust': 4.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.57}}, {'dt': 1641837600, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1013, 'humidity': 85, 'dew_point': 23.53, 'uvi': 11.84, 'clouds': 70, 'visibility': 9167, 'wind_speed': 2.85, 'wind_deg': 272, 'wind_gust': 4.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.56}}, {'dt': 1641841200, 'temp': 26.09, 'feels_like': 26.09, 'pressure': 1012, 'humidity': 85, 'dew_point': 23.37, 'uvi': 9.16, 'clouds': 88, 'visibility': 9565, 'wind_speed': 2.68, 'wind_deg': 275, 'wind_gust': 4.06, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.4}}, {'dt': 1641844800, 'temp': 25.93, 'feels_like': 26.82, 'pressure': 1011, 'humidity': 86, 'dew_point': 23.41, 'uvi': 5.73, 'clouds': 82, 'visibility': 7402, 'wind_speed': 2.44, 'wind_deg': 276, 'wind_gust': 3.67, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1641848400, 'temp': 25.58, 'feels_like': 26.49, 'pressure': 1010, 'humidity': 88, 'dew_point': 23.44, 'uvi': 2.6, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 274, 'wind_gust': 3.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.29}}, {'dt': 1641852000, 'temp': 25.17, 'feels_like': 26.09, 'pressure': 1011, 'humidity': 90, 'dew_point': 23.41, 'uvi': 0.65, 'clouds': 76, 'visibility': 9109, 'wind_speed': 1.63, 'wind_deg': 271, 'wind_gust': 3.17, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.27}}, {'dt': 1641855600, 'temp': 24.16, 'feels_like': 25.03, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.78, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 255, 'wind_gust': 2.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.49}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.420000 | 24.810000 | 91.000000 | 1011.000000 | 0.64 | 23.980000 | 0.000000 | 10000.000000 | 248.000000 | 1.62 | 1.330000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 22.460000 | 24.510000 | 93.000000 | 1012.000000 | 0.8 | 23.660000 | 0.000000 | 10000.000000 | 221.000000 | 1.56 | 1.280000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 02:00:00 | 93.000000 | 22.400000 | 24.440000 | 93.000000 | 1013.000000 | 0.15 | 23.600000 | 0.000000 | 10000.000000 | 196.000000 | 1.61 | 1.410000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 22.440000 | 24.320000 | 94.000000 | 1013.000000 |  | 23.460000 | 0.000000 | 10000.000000 | 180.000000 | 2.15 | 1.750000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 22.530000 | 24.080000 | 96.000000 | 1013.000000 | 0.1 | 23.200000 | 0.000000 | 10000.000000 | 184.000000 | 2.85 | 1.950000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 22.330000 | 23.860000 | 96.000000 | 1013.000000 | 0.18 | 23.000000 | 0.000000 | 10000.000000 | 188.000000 | 2.95 | 1.910000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 06:00:00 | 88.000000 | 22.310000 | 23.840000 | 96.000000 | 1012.000000 | 0.24 | 22.980000 | 0.000000 | 10000.000000 | 197.000000 | 3.81 | 1.960000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 22.330000 | 23.700000 | 97.000000 | 1012.000000 | 0.37 | 22.830000 | 0.000000 | 10000.000000 | 203.000000 | 4.9 | 2.130000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 22.190000 | 23.550000 | 97.000000 | 1011.000000 | 0.32 | 22.690000 | 0.000000 | 10000.000000 | 195.000000 | 5.3 | 2.220000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 09:00:00 | 92.000000 | 22.070000 | 23.420000 | 97.000000 | 1011.000000 | 0.39 | 22.570000 | 0.000000 | 10000.000000 | 193.000000 | 5.65 | 2.360000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 21.980000 | 23.320000 | 97.000000 | 1012.000000 | 0.53 | 22.480000 | 0.000000 | 10000.000000 | 196.000000 | 5.75 | 2.390000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 11:00:00 | 87.000000 | 21.760000 | 23.240000 | 96.000000 | 1012.000000 | 0.56 | 22.430000 | 0.000000 | 10000.000000 | 193.000000 | 5.76 | 2.410000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 12:00:00 | 92.000000 | 22.210000 | 23.730000 | 96.000000 | 1013.000000 | 0.38 | 22.880000 | 0.320000 | 10000.000000 | 196.000000 | 5.52 | 2.220000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 13:00:00 | 89.000000 | 22.830000 | 25.090000 | 92.000000 | 1014.000000 | 0.67 | 24.210000 | 1.690000 | 10000.000000 | 201.000000 | 4.74 | 2.410000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 23.300000 | 26.330000 | 88.000000 | 1014.000000 | 1.35 | 25.430000 | 4.410000 | 7599.000000 | 224.000000 | 5.25 | 2.650000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 15:00:00 | 94.000000 | 23.500000 | 26.030000 | 86.000000 | 1015.000000 | 1.38 | 26.030000 | 7.890000 | 10000.000000 | 238.000000 | 5.18 | 3.180000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 16:00:00 | 89.000000 | 23.680000 | 26.410000 | 85.000000 | 1014.000000 | 1.23 | 26.410000 | 11.020000 | 9155.000000 | 249.000000 | 5.01 | 3.440000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 23.820000 | 26.550000 | 85.000000 | 1013.000000 | 1.57 | 26.550000 | 12.510000 | 6342.000000 | 258.000000 | 4.57 | 3.290000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 18:00:00 | 70.000000 | 23.530000 | 26.250000 | 85.000000 | 1013.000000 | 1.56 | 26.250000 | 11.840000 | 9167.000000 | 272.000000 | 4.25 | 2.850000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 23.370000 | 26.090000 | 85.000000 | 1012.000000 | 1.4 | 26.090000 | 9.160000 | 9565.000000 | 275.000000 | 4.06 | 2.680000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 20:00:00 | 82.000000 | 23.410000 | 26.820000 | 86.000000 | 1011.000000 | 1.33 | 25.930000 | 5.730000 | 7402.000000 | 276.000000 | 3.67 | 2.440000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 21:00:00 | 77.000000 | 23.440000 | 26.490000 | 88.000000 | 1010.000000 | 1.29 | 25.580000 | 2.600000 | 10000.000000 | 274.000000 | 3.3 | 2.010000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 22:00:00 | 76.000000 | 23.410000 | 26.090000 | 90.000000 | 1011.000000 | 1.27 | 25.170000 | 0.650000 | 9109.000000 | 271.000000 | 3.17 | 1.630000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045040 | "AEROPUERTO GUAPI - AUT [53045040]" | 2.574417 | -77.894750 | 42.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Cauca | Guapi | Paez | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 23:00:00 | 80.000000 | 22.780000 | 25.030000 | 92.000000 | 1011.000000 | 1.49 | 24.160000 | 0.000000 | 10000.000000 | 255.000000 | 2.49 | 1.380000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station53045040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station53045040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station53045040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045040_OWM_Windspeed_20220111.png)
