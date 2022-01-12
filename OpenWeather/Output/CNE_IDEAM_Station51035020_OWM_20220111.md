
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CCCP DL PACIFICO [51035020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station51035020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.81916667,-78.73) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.81916667&lon=-78.73)


| Parameter | Value |
|---|---|
| Code | 51035020 |
| Name | CCCP DL PACIFICO [51035020] |
| Latitude, ° | 1.81916667 |
| Longitude, ° | -78.73 |
| Elevation, m | 1 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1991-09-15 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Tumaco |
| Stream | La Esmeralda |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Mira |
| SZH - Hydrographic subzone | Río Rosario |

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

### (CNE index 3598) Open Weather values for station 51035020 - CCCP DL PACIFICO [51035020]

JSON data from API OWM:

```
{'lat': 1.8192, 'lon': -78.73, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813696, 'sunset': 1641856974, 'temp': 26.88, 'feels_like': 29.05, 'pressure': 1011, 'humidity': 75, 'dew_point': 22.07, 'uvi': 6.17, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.11, 'wind_deg': 300, 'wind_gust': 4.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, 'hourly': [{'dt': 1641772800, 'temp': 24.66, 'feels_like': 25.48, 'pressure': 1011, 'humidity': 88, 'dew_point': 22.54, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 254, 'wind_gust': 2.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 24.41, 'feels_like': 25.23, 'pressure': 1012, 'humidity': 89, 'dew_point': 22.48, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 243, 'wind_gust': 2.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 24.06, 'feels_like': 24.9, 'pressure': 1013, 'humidity': 91, 'dew_point': 22.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 230, 'wind_gust': 2.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641783600, 'temp': 23.95, 'feels_like': 24.8, 'pressure': 1013, 'humidity': 92, 'dew_point': 22.57, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 224, 'wind_gust': 3.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.55}}, {'dt': 1641787200, 'temp': 23.82, 'feels_like': 24.66, 'pressure': 1013, 'humidity': 92, 'dew_point': 22.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 217, 'wind_gust': 3.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641790800, 'temp': 23.59, 'feels_like': 24.43, 'pressure': 1013, 'humidity': 93, 'dew_point': 22.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.51, 'wind_deg': 208, 'wind_gust': 3.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.8}}, {'dt': 1641794400, 'temp': 23.57, 'feels_like': 24.41, 'pressure': 1012, 'humidity': 93, 'dew_point': 22.37, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.74, 'wind_deg': 213, 'wind_gust': 4.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641798000, 'temp': 23.62, 'feels_like': 24.44, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.24, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 215, 'wind_gust': 3.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.33, 'feels_like': 24.15, 'pressure': 1011, 'humidity': 93, 'dew_point': 22.13, 'uvi': 0, 'clouds': 100, 'visibility': 6635, 'wind_speed': 2.55, 'wind_deg': 220, 'wind_gust': 3.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.92}}, {'dt': 1641805200, 'temp': 23.26, 'feels_like': 24.07, 'pressure': 1011, 'humidity': 93, 'dew_point': 22.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.66, 'wind_deg': 223, 'wind_gust': 4.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.45}}, {'dt': 1641808800, 'temp': 23.31, 'feels_like': 24.1, 'pressure': 1012, 'humidity': 92, 'dew_point': 21.94, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.87, 'wind_deg': 228, 'wind_gust': 4.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.88}}, {'dt': 1641812400, 'temp': 23.39, 'feels_like': 24.16, 'pressure': 1012, 'humidity': 91, 'dew_point': 21.84, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 227, 'wind_gust': 4.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641816000, 'temp': 23.55, 'feels_like': 24.36, 'pressure': 1013, 'humidity': 92, 'dew_point': 22.17, 'uvi': 0.29, 'clouds': 66, 'visibility': 8865, 'wind_speed': 2.41, 'wind_deg': 215, 'wind_gust': 4.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641819600, 'temp': 24.67, 'feels_like': 25.49, 'pressure': 1014, 'humidity': 88, 'dew_point': 22.55, 'uvi': 1.62, 'clouds': 91, 'visibility': 8604, 'wind_speed': 2.82, 'wind_deg': 222, 'wind_gust': 4.74, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641823200, 'temp': 25.65, 'feels_like': 26.46, 'pressure': 1015, 'humidity': 84, 'dew_point': 22.74, 'uvi': 4.3, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.49, 'wind_deg': 241, 'wind_gust': 5.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.78}}, {'dt': 1641826800, 'temp': 26.22, 'feels_like': 26.22, 'pressure': 1015, 'humidity': 82, 'dew_point': 22.9, 'uvi': 7.81, 'clouds': 93, 'visibility': 10000, 'wind_speed': 3.41, 'wind_deg': 254, 'wind_gust': 4.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641830400, 'temp': 26.59, 'feels_like': 26.59, 'pressure': 1014, 'humidity': 80, 'dew_point': 22.85, 'uvi': 11.14, 'clouds': 77, 'visibility': 7743, 'wind_speed': 3.31, 'wind_deg': 266, 'wind_gust': 4.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}, {'dt': 1641834000, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1013, 'humidity': 80, 'dew_point': 22.9, 'uvi': 12.79, 'clouds': 70, 'visibility': 10000, 'wind_speed': 3.49, 'wind_deg': 276, 'wind_gust': 4.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641837600, 'temp': 26.77, 'feels_like': 29.08, 'pressure': 1013, 'humidity': 78, 'dew_point': 22.61, 'uvi': 12.27, 'clouds': 34, 'visibility': 10000, 'wind_speed': 3.41, 'wind_deg': 292, 'wind_gust': 4.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641841200, 'temp': 26.87, 'feels_like': 29.2, 'pressure': 1012, 'humidity': 77, 'dew_point': 22.5, 'uvi': 9.67, 'clouds': 55, 'visibility': 10000, 'wind_speed': 3.45, 'wind_deg': 297, 'wind_gust': 4.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641844800, 'temp': 26.88, 'feels_like': 29.05, 'pressure': 1011, 'humidity': 75, 'dew_point': 22.07, 'uvi': 6.17, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.11, 'wind_deg': 300, 'wind_gust': 4.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641848400, 'temp': 26.89, 'feels_like': 28.99, 'pressure': 1010, 'humidity': 74, 'dew_point': 21.86, 'uvi': 2.89, 'clouds': 42, 'visibility': 10000, 'wind_speed': 3.05, 'wind_deg': 302, 'wind_gust': 3.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641852000, 'temp': 26.39, 'feels_like': 26.39, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.24, 'uvi': 0.83, 'clouds': 39, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 302, 'wind_gust': 3.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641855600, 'temp': 25.4, 'feels_like': 26.14, 'pressure': 1011, 'humidity': 82, 'dew_point': 22.1, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 298, 'wind_gust': 2.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 00:00:00 | 99.000000 | 22.540000 | 25.480000 | 88.000000 | 1011.000000 |  | 24.660000 | 0.000000 | 10000.000000 | 254.000000 | 2.83 | 2.420000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 22.480000 | 25.230000 | 89.000000 | 1012.000000 | 0.12 | 24.410000 | 0.000000 | 10000.000000 | 243.000000 | 2.72 | 2.290000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 22.500000 | 24.900000 | 91.000000 | 1013.000000 | 0.53 | 24.060000 | 0.000000 | 10000.000000 | 230.000000 | 2.68 | 2.200000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 22.570000 | 24.800000 | 92.000000 | 1013.000000 | 0.55 | 23.950000 | 0.000000 | 10000.000000 | 224.000000 | 3.15 | 2.460000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 22.440000 | 24.660000 | 92.000000 | 1013.000000 | 0.53 | 23.820000 | 0.000000 | 10000.000000 | 217.000000 | 3.02 | 2.350000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 22.390000 | 24.430000 | 93.000000 | 1013.000000 | 0.8 | 23.590000 | 0.000000 | 10000.000000 | 208.000000 | 3.74 | 2.510000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 22.370000 | 24.410000 | 93.000000 | 1012.000000 | 0.5 | 23.570000 | 0.000000 | 10000.000000 | 213.000000 | 4.75 | 2.740000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 22.240000 | 24.440000 | 92.000000 | 1012.000000 |  | 23.620000 | 0.000000 | 10000.000000 | 215.000000 | 3.78 | 2.500000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 22.130000 | 24.150000 | 93.000000 | 1011.000000 | 0.92 | 23.330000 | 0.000000 | 6635.000000 | 220.000000 | 3.93 | 2.550000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 22.060000 | 24.070000 | 93.000000 | 1011.000000 | 1.45 | 23.260000 | 0.000000 | 10000.000000 | 223.000000 | 4.02 | 2.660000 | 501 | Rain | moderate rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 10:00:00 | 97.000000 | 21.940000 | 24.100000 | 92.000000 | 1012.000000 | 0.88 | 23.310000 | 0.000000 | 10000.000000 | 228.000000 | 4.14 | 2.870000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 11:00:00 | 97.000000 | 21.840000 | 24.160000 | 91.000000 | 1012.000000 | 0.4 | 23.390000 | 0.000000 | 10000.000000 | 227.000000 | 4.05 | 2.780000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 12:00:00 | 66.000000 | 22.170000 | 24.360000 | 92.000000 | 1013.000000 | 0.72 | 23.550000 | 0.290000 | 8865.000000 | 215.000000 | 4.33 | 2.410000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 22.550000 | 25.490000 | 88.000000 | 1014.000000 | 1.18 | 24.670000 | 1.620000 | 8604.000000 | 222.000000 | 4.74 | 2.820000 | 501 | Rain | moderate rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 14:00:00 | 90.000000 | 22.740000 | 26.460000 | 84.000000 | 1015.000000 | 0.78 | 25.650000 | 4.300000 | 10000.000000 | 241.000000 | 5.3 | 3.490000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 15:00:00 | 93.000000 | 22.900000 | 26.220000 | 82.000000 | 1015.000000 | 0.86 | 26.220000 | 7.810000 | 10000.000000 | 254.000000 | 4.71 | 3.410000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 22.850000 | 26.590000 | 80.000000 | 1014.000000 | 0.99 | 26.590000 | 11.140000 | 7743.000000 | 266.000000 | 4.29 | 3.310000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | 22.900000 | 26.640000 | 80.000000 | 1013.000000 | 1.03 | 26.640000 | 12.790000 | 10000.000000 | 276.000000 | 4.4 | 3.490000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 18:00:00 | 34.000000 | 22.610000 | 29.080000 | 78.000000 | 1013.000000 | 0.68 | 26.770000 | 12.270000 | 10000.000000 | 292.000000 | 4.58 | 3.410000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 19:00:00 | 55.000000 | 22.500000 | 29.200000 | 77.000000 | 1012.000000 | 0.6 | 26.870000 | 9.670000 | 10000.000000 | 297.000000 | 4.72 | 3.450000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 20:00:00 | 50.000000 | 22.070000 | 29.050000 | 75.000000 | 1011.000000 | 0.31 | 26.880000 | 6.170000 | 10000.000000 | 300.000000 | 4.2 | 3.110000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 21:00:00 | 42.000000 | 21.860000 | 28.990000 | 74.000000 | 1010.000000 | 0.22 | 26.890000 | 2.890000 | 10000.000000 | 302.000000 | 3.9 | 3.050000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 22:00:00 | 39.000000 | 22.240000 | 26.390000 | 78.000000 | 1011.000000 | 0.22 | 26.390000 | 0.830000 | 10000.000000 | 302.000000 | 3.57 | 2.500000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51035020 | "CCCP DL PACIFICO [51035020]" | 1.819167 | -78.730000 | 1.000000 | Climática Principal | Convencional | Activa | 1991-09-15 00:00:00 | NaT | Nariño | Tumaco | La Esmeralda | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Rosario | America/Bogota | 2022-01-10 23:00:00 | 34.000000 | 22.100000 | 26.140000 | 82.000000 | 1011.000000 | 0.11 | 25.400000 | 0.000000 | 10000.000000 | 298.000000 | 2.87 | 2.320000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station51035020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station51035020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station51035020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51035020_OWM_Windspeed_20220111.png)
