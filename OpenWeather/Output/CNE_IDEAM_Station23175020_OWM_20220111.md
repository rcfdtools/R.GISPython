
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO OTU [23175020] - Historical

### General parameters

* Weather date time: 2022-01-11 19:01:08.491859
* Unix time to eval: 1641841268
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
* CNE IDEAM station code filter: ['All']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['All']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23175020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.01175,-74.71630556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.01175&lon=-74.71630556)


| Parameter | Value |
|---|---|
| Code | 23175020 |
| Name | AEROPUERTO OTU [23175020] |
| Latitude, ° | 7.01175 |
| Longitude, ° | -74.71630556 |
| Elevation, m | 643 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1940-05-15 00:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Remedios |
| Stream | Riosucio |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Cimitarra y otros directos al Magdalena |

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

### (CNE index 2831) Open Weather values for station 23175020 - AEROPUERTO OTU [23175020]

JSON data from API OWM:

```
{'lat': 7.0118, 'lon': -74.7163, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641841268, 'sunrise': 1641813236, 'sunset': 1641855507, 'temp': 27.63, 'feels_like': 28.64, 'pressure': 1010, 'humidity': 57, 'dew_point': 18.35, 'uvi': 7.55, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 354, 'wind_gust': 2.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, 'hourly': [{'dt': 1641772800, 'temp': 20.58, 'feels_like': 21.1, 'pressure': 1012, 'humidity': 92, 'dew_point': 19.23, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 278, 'wind_gust': 1.12, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 20.11, 'feels_like': 20.6, 'pressure': 1012, 'humidity': 93, 'dew_point': 18.94, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 263, 'wind_gust': 1.1, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 19.82, 'feels_like': 20.31, 'pressure': 1013, 'humidity': 94, 'dew_point': 18.83, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 259, 'wind_gust': 1.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 19.68, 'feels_like': 20.13, 'pressure': 1013, 'humidity': 93, 'dew_point': 18.52, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 265, 'wind_gust': 1.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 19.5, 'feels_like': 19.96, 'pressure': 1013, 'humidity': 94, 'dew_point': 18.51, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 270, 'wind_gust': 1.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 19.24, 'feels_like': 19.67, 'pressure': 1013, 'humidity': 94, 'dew_point': 18.25, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 266, 'wind_gust': 1.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.86, 'feels_like': 19.31, 'pressure': 1012, 'humidity': 96, 'dew_point': 18.21, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 274, 'wind_gust': 1.64, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 18.6, 'feels_like': 19.05, 'pressure': 1012, 'humidity': 97, 'dew_point': 18.11, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 288, 'wind_gust': 1.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 18.18, 'feels_like': 18.64, 'pressure': 1011, 'humidity': 99, 'dew_point': 18.02, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 299, 'wind_gust': 2.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 17.98, 'feels_like': 18.42, 'pressure': 1012, 'humidity': 99, 'dew_point': 17.82, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 296, 'wind_gust': 2.42, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 17.92, 'feels_like': 18.35, 'pressure': 1012, 'humidity': 99, 'dew_point': 17.76, 'uvi': 0, 'clouds': 35, 'visibility': 4401, 'wind_speed': 1.15, 'wind_deg': 289, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641812400, 'temp': 17.89, 'feels_like': 18.32, 'pressure': 1013, 'humidity': 99, 'dew_point': 17.73, 'uvi': 0, 'clouds': 39, 'visibility': 2221, 'wind_speed': 1.02, 'wind_deg': 288, 'wind_gust': 2.03, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 18.57, 'feels_like': 19.04, 'pressure': 1014, 'humidity': 98, 'dew_point': 18.25, 'uvi': 0.35, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 276, 'wind_gust': 1.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 20.59, 'feels_like': 21.13, 'pressure': 1015, 'humidity': 93, 'dew_point': 19.42, 'uvi': 1.75, 'clouds': 37, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 318, 'wind_gust': 1.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 22.2, 'feels_like': 22.83, 'pressure': 1015, 'humidity': 90, 'dew_point': 20.48, 'uvi': 4.36, 'clouds': 31, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 354, 'wind_gust': 2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641826800, 'temp': 23.26, 'feels_like': 23.91, 'pressure': 1015, 'humidity': 87, 'dew_point': 20.97, 'uvi': 7.51, 'clouds': 29, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 8, 'wind_gust': 2.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641830400, 'temp': 24.09, 'feels_like': 24.67, 'pressure': 1014, 'humidity': 81, 'dew_point': 20.63, 'uvi': 10.16, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 20, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641834000, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1013, 'humidity': 69, 'dew_point': 19.84, 'uvi': 11.16, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 36, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641837600, 'temp': 27.86, 'feels_like': 28.74, 'pressure': 1011, 'humidity': 55, 'dew_point': 17.99, 'uvi': 10.16, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 16, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641841200, 'temp': 27.63, 'feels_like': 28.64, 'pressure': 1010, 'humidity': 57, 'dew_point': 18.35, 'uvi': 7.55, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 354, 'wind_gust': 2.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641844800, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1009, 'humidity': 64, 'dew_point': 18.93, 'uvi': 4.38, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 328, 'wind_gust': 3.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641848400, 'temp': 26.31, 'feels_like': 26.31, 'pressure': 1009, 'humidity': 62, 'dew_point': 18.45, 'uvi': 1.76, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 325, 'wind_gust': 3.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641852000, 'temp': 24.14, 'feels_like': 24.59, 'pressure': 1010, 'humidity': 76, 'dew_point': 19.64, 'uvi': 0.31, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 317, 'wind_gust': 4.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641855600, 'temp': 21.38, 'feels_like': 21.85, 'pressure': 1011, 'humidity': 87, 'dew_point': 19.13, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 304, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 6.000000 | 19.230000 | 21.100000 | 92.000000 | 1012.000000 |  | 20.580000 | 0.000000 | 10000.000000 | 278.000000 | 1.12 | 1.190000 | 800 | Clear | clear sky | 01n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 11.000000 | 18.940000 | 20.600000 | 93.000000 | 1012.000000 |  | 20.110000 | 0.000000 | 10000.000000 | 263.000000 | 1.1 | 1.220000 | 801 | Clouds | few clouds | 02n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 26.000000 | 18.830000 | 20.310000 | 94.000000 | 1013.000000 |  | 19.820000 | 0.000000 | 10000.000000 | 259.000000 | 1.15 | 1.120000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 48.000000 | 18.520000 | 20.130000 | 93.000000 | 1013.000000 |  | 19.680000 | 0.000000 | 10000.000000 | 265.000000 | 1.26 | 1.190000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 61.000000 | 18.510000 | 19.960000 | 94.000000 | 1013.000000 |  | 19.500000 | 0.000000 | 10000.000000 | 270.000000 | 1.38 | 1.130000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 68.000000 | 18.250000 | 19.670000 | 94.000000 | 1013.000000 |  | 19.240000 | 0.000000 | 10000.000000 | 266.000000 | 1.37 | 1.180000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 28.000000 | 18.210000 | 19.310000 | 96.000000 | 1012.000000 |  | 18.860000 | 0.000000 | 10000.000000 | 274.000000 | 1.64 | 1.270000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 30.000000 | 18.110000 | 19.050000 | 97.000000 | 1012.000000 |  | 18.600000 | 0.000000 | 10000.000000 | 288.000000 | 1.86 | 1.340000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 25.000000 | 18.020000 | 18.640000 | 99.000000 | 1011.000000 |  | 18.180000 | 0.000000 | 10000.000000 | 299.000000 | 2.72 | 1.320000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 27.000000 | 17.820000 | 18.420000 | 99.000000 | 1012.000000 |  | 17.980000 | 0.000000 | 10000.000000 | 296.000000 | 2.42 | 1.230000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 35.000000 | 17.760000 | 18.350000 | 99.000000 | 1012.000000 | 0.11 | 17.920000 | 0.000000 | 4401.000000 | 289.000000 | 2.24 | 1.150000 | 500 | Rain | light rain | 10n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 39.000000 | 17.730000 | 18.320000 | 99.000000 | 1013.000000 |  | 17.890000 | 0.000000 | 2221.000000 | 288.000000 | 2.03 | 1.020000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 33.000000 | 18.250000 | 19.040000 | 98.000000 | 1014.000000 |  | 18.570000 | 0.350000 | 10000.000000 | 276.000000 | 1.77 | 0.860000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 37.000000 | 19.420000 | 21.130000 | 93.000000 | 1015.000000 |  | 20.590000 | 1.750000 | 10000.000000 | 318.000000 | 1.59 | 0.750000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 31.000000 | 20.480000 | 22.830000 | 90.000000 | 1015.000000 | 0.39 | 22.200000 | 4.360000 | 10000.000000 | 354.000000 | 2 | 1.130000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 29.000000 | 20.970000 | 23.910000 | 87.000000 | 1015.000000 | 0.61 | 23.260000 | 7.510000 | 10000.000000 | 8.000000 | 2.55 | 1.350000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 30.000000 | 20.630000 | 24.670000 | 81.000000 | 1014.000000 | 0.46 | 24.090000 | 10.160000 | 10000.000000 | 20.000000 | 2.19 | 1.230000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 30.000000 | 19.840000 | 25.960000 | 69.000000 | 1013.000000 | 0.35 | 25.960000 | 11.160000 | 10000.000000 | 36.000000 | 2.13 | 1.230000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 44.000000 | 17.990000 | 28.740000 | 55.000000 | 1011.000000 | 0.26 | 27.860000 | 10.160000 | 10000.000000 | 16.000000 | 2.1 | 1.870000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 56.000000 | 18.350000 | 28.640000 | 57.000000 | 1010.000000 | 0.21 | 27.630000 | 7.550000 | 10000.000000 | 354.000000 | 2.17 | 1.920000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 65.000000 | 18.930000 | 26.280000 | 64.000000 | 1009.000000 | 0.24 | 26.280000 | 4.380000 | 10000.000000 | 328.000000 | 3.05 | 1.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 51.000000 | 18.450000 | 26.310000 | 62.000000 | 1009.000000 | 0.17 | 26.310000 | 1.760000 | 10000.000000 | 325.000000 | 3.12 | 1.740000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 63.000000 | 19.640000 | 24.590000 | 76.000000 | 1010.000000 | 0.11 | 24.140000 | 0.310000 | 10000.000000 | 317.000000 | 4.16 | 1.520000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 70.000000 | 19.130000 | 21.850000 | 87.000000 | 1011.000000 |  | 21.380000 | 0.000000 | 10000.000000 | 304.000000 | 2.38 | 1.320000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station23175020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23175020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23175020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23175020_OWM_Windspeed_20220111.png)
