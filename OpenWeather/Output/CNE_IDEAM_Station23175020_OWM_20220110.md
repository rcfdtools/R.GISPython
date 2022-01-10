
## Weather values for the IDEAM national station catalog - CNE from OWM https://openweathermap.org - AEROPUERTO OTU [23175020]

### General parameters

* Current date time: 2022-01-10 17:27:30.876955
* Unix time to eval: 1641749250
* Show historical: True
* Show yesterday: True
* Show OWM API detail: True
* Request OWM data: True
* Days before: 1
* Unit system: metric
* Icons from: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220110.xls
* CNE IDEAM stations: 4489
* CNE IDEAM attributes: 19
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23175020_OWM_20220110.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220110.csv)


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
| Julian | N/A | N/A | Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API

### 2868 - Open Weather values for station 000023175020: AEROPUERTO OTU [23175020]

JSON data from API OWM:

```
{'lat': 7.0118, 'lon': -74.7163, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641749250, 'sunrise': 1641726817, 'sunset': 1641769078, 'temp': 25.75, 'feels_like': 26.31, 'pressure': 1013, 'humidity': 74, 'dew_point': 20.77, 'uvi': 11.22, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 51, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, 'hourly': [{'dt': 1641686400, 'temp': 19.87, 'feels_like': 20.45, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.38, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 282, 'wind_gust': 1.66, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641690000, 'temp': 19.33, 'feels_like': 19.88, 'pressure': 1014, 'humidity': 98, 'dew_point': 19.01, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 264, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641693600, 'temp': 19.04, 'feels_like': 19.56, 'pressure': 1015, 'humidity': 98, 'dew_point': 18.72, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 263, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641697200, 'temp': 18.84, 'feels_like': 19.34, 'pressure': 1015, 'humidity': 98, 'dew_point': 18.52, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 269, 'wind_gust': 1.66, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641700800, 'temp': 18.66, 'feels_like': 19.14, 'pressure': 1015, 'humidity': 98, 'dew_point': 18.34, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 267, 'wind_gust': 1.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641704400, 'temp': 18.58, 'feels_like': 19.05, 'pressure': 1015, 'humidity': 98, 'dew_point': 18.26, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 265, 'wind_gust': 1.54, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641708000, 'temp': 18.51, 'feels_like': 18.92, 'pressure': 1014, 'humidity': 96, 'dew_point': 17.86, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 270, 'wind_gust': 1.44, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641711600, 'temp': 18.3, 'feels_like': 18.69, 'pressure': 1014, 'humidity': 96, 'dew_point': 17.65, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 282, 'wind_gust': 1.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641715200, 'temp': 18.06, 'feels_like': 18.48, 'pressure': 1013, 'humidity': 98, 'dew_point': 17.74, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 284, 'wind_gust': 1.42, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641718800, 'temp': 17.95, 'feels_like': 18.36, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.63, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 276, 'wind_gust': 1.16, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641722400, 'temp': 17.84, 'feels_like': 18.24, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.52, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 275, 'wind_gust': 0.87, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641726000, 'temp': 17.81, 'feels_like': 18.21, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.49, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 264, 'wind_gust': 0.94, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641729600, 'temp': 18.88, 'feels_like': 19.3, 'pressure': 1015, 'humidity': 95, 'dew_point': 18.06, 'uvi': 0.38, 'clouds': 12, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 248, 'wind_gust': 0.8, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641733200, 'temp': 21.47, 'feels_like': 21.94, 'pressure': 1016, 'humidity': 87, 'dew_point': 19.22, 'uvi': 1.75, 'clouds': 18, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 296, 'wind_gust': 1.02, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641736800, 'temp': 23.2, 'feels_like': 23.74, 'pressure': 1016, 'humidity': 83, 'dew_point': 20.15, 'uvi': 4.35, 'clouds': 13, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 3, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641740400, 'temp': 24.02, 'feels_like': 24.62, 'pressure': 1015, 'humidity': 82, 'dew_point': 20.76, 'uvi': 7.5, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 20, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, {'dt': 1641744000, 'temp': 24.84, 'feels_like': 25.47, 'pressure': 1014, 'humidity': 80, 'dew_point': 21.15, 'uvi': 10.21, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 43, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641747600, 'temp': 25.75, 'feels_like': 26.31, 'pressure': 1013, 'humidity': 74, 'dew_point': 20.77, 'uvi': 11.22, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 51, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641751200, 'temp': 28.88, 'feels_like': 29.51, 'pressure': 1011, 'humidity': 50, 'dew_point': 17.42, 'uvi': 10.21, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 28, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641754800, 'temp': 28.93, 'feels_like': 29.57, 'pressure': 1010, 'humidity': 50, 'dew_point': 17.47, 'uvi': 7.59, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 5, 'wind_gust': 2.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641758400, 'temp': 28.4, 'feels_like': 29.12, 'pressure': 1009, 'humidity': 52, 'dew_point': 17.6, 'uvi': 4.4, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 358, 'wind_gust': 2.56, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641762000, 'temp': 26.91, 'feels_like': 27.97, 'pressure': 1009, 'humidity': 60, 'dew_point': 18.49, 'uvi': 1.77, 'clouds': 27, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 359, 'wind_gust': 2.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641765600, 'temp': 24.77, 'feels_like': 25.21, 'pressure': 1010, 'humidity': 73, 'dew_point': 19.6, 'uvi': 0.36, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 360, 'wind_gust': 4.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641769200, 'temp': 21.6, 'feels_like': 22.11, 'pressure': 1011, 'humidity': 88, 'dew_point': 19.53, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 321, 'wind_gust': 1.25, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Julian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 00:00:00 | 8.000000 | 19.380000 | 20.450000 | 97.000000 | 1013.000000 |  | 19.870000 | 0.000000 | 10000.000000 | 282.000000 | 1.66 | 1.180000 | 800 | Clear | clear sky | 01n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 01:00:00 | 24.000000 | 19.010000 | 19.880000 | 98.000000 | 1014.000000 | 0.35 | 19.330000 | 0.000000 | 10000.000000 | 264.000000 | 1.6 | 1.290000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 02:00:00 | 24.000000 | 18.720000 | 19.560000 | 98.000000 | 1015.000000 | 0.24 | 19.040000 | 0.000000 | 10000.000000 | 263.000000 | 1.75 | 1.220000 | 500 | Rain | light rain | 10n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 03:00:00 | 25.000000 | 18.520000 | 19.340000 | 98.000000 | 1015.000000 |  | 18.840000 | 0.000000 | 10000.000000 | 269.000000 | 1.66 | 1.200000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 04:00:00 | 30.000000 | 18.340000 | 19.140000 | 98.000000 | 1015.000000 |  | 18.660000 | 0.000000 | 10000.000000 | 267.000000 | 1.57 | 1.240000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 05:00:00 | 44.000000 | 18.260000 | 19.050000 | 98.000000 | 1015.000000 |  | 18.580000 | 0.000000 | 10000.000000 | 265.000000 | 1.54 | 1.240000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 06:00:00 | 30.000000 | 17.860000 | 18.920000 | 96.000000 | 1014.000000 |  | 18.510000 | 0.000000 | 10000.000000 | 270.000000 | 1.44 | 1.110000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 07:00:00 | 36.000000 | 17.650000 | 18.690000 | 96.000000 | 1014.000000 |  | 18.300000 | 0.000000 | 10000.000000 | 282.000000 | 1.37 | 1.040000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 08:00:00 | 42.000000 | 17.740000 | 18.480000 | 98.000000 | 1013.000000 |  | 18.060000 | 0.000000 | 10000.000000 | 284.000000 | 1.42 | 1.150000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 09:00:00 | 37.000000 | 17.630000 | 18.360000 | 98.000000 | 1014.000000 |  | 17.950000 | 0.000000 | 10000.000000 | 276.000000 | 1.16 | 1.060000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 10:00:00 | 33.000000 | 17.520000 | 18.240000 | 98.000000 | 1014.000000 |  | 17.840000 | 0.000000 | 10000.000000 | 275.000000 | 0.87 | 0.800000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 11:00:00 | 44.000000 | 17.490000 | 18.210000 | 98.000000 | 1014.000000 |  | 17.810000 | 0.000000 | 10000.000000 | 264.000000 | 0.94 | 0.930000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 12:00:00 | 12.000000 | 18.060000 | 19.300000 | 95.000000 | 1015.000000 |  | 18.880000 | 0.380000 | 10000.000000 | 248.000000 | 0.8 | 0.670000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 13:00:00 | 18.000000 | 19.220000 | 21.940000 | 87.000000 | 1016.000000 |  | 21.470000 | 1.750000 | 10000.000000 | 296.000000 | 1.02 | 0.440000 | 801 | Clouds | few clouds | 02d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 14:00:00 | 13.000000 | 20.150000 | 23.740000 | 83.000000 | 1016.000000 | 0.35 | 23.200000 | 4.350000 | 10000.000000 | 3.000000 | 1.25 | 0.920000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 15:00:00 | 14.000000 | 20.760000 | 24.620000 | 82.000000 | 1015.000000 | 0.71 | 24.020000 | 7.500000 | 10000.000000 | 20.000000 | 1.4 | 1.020000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 16:00:00 | 20.000000 | 21.150000 | 25.470000 | 80.000000 | 1014.000000 | 0.81 | 24.840000 | 10.210000 | 10000.000000 | 43.000000 | 1.22 | 0.830000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 17:00:00 | 22.000000 | 20.770000 | 26.310000 | 74.000000 | 1013.000000 | 0.62 | 25.750000 | 11.220000 | 10000.000000 | 51.000000 | 1.25 | 0.540000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 18:00:00 | 19.000000 | 17.420000 | 29.510000 | 50.000000 | 1011.000000 | 0.32 | 28.880000 | 10.210000 | 10000.000000 | 28.000000 | 1.77 | 1.520000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 19:00:00 | 24.000000 | 17.470000 | 29.570000 | 50.000000 | 1010.000000 | 0.16 | 28.930000 | 7.590000 | 10000.000000 | 5.000000 | 2.33 | 1.760000 | 500 | Rain | light rain | 10d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 20:00:00 | 18.000000 | 17.600000 | 29.120000 | 52.000000 | 1009.000000 |  | 28.400000 | 4.400000 | 10000.000000 | 358.000000 | 2.56 | 2.010000 | 801 | Clouds | few clouds | 02d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 21:00:00 | 27.000000 | 18.490000 | 27.970000 | 60.000000 | 1009.000000 |  | 26.910000 | 1.770000 | 10000.000000 | 359.000000 | 2.92 | 2.100000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 22:00:00 | 32.000000 | 19.600000 | 25.210000 | 73.000000 | 1010.000000 | 0.15 | 24.770000 | 0.360000 | 10000.000000 | 360.000000 | 4.9 | 1.820000 | 500 | Rain | light rain | 10d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23175020 | "AEROPUERTO OTU [23175020]" | 7.011750 | -74.716306 | 643.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-05-15 00:00:00 | NaT | Antioquia | Remedios | Riosucio | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Cimitarra y otros directos al Magdalena | America/Bogota | 2022-01-09 23:00:00 | 30.000000 | 19.530000 | 22.110000 | 88.000000 | 1011.000000 |  | 21.600000 | 0.000000 | 10000.000000 | 321.000000 | 1.25 | 1.060000 | 802 | Clouds | scattered clouds | 03n | 23 |
