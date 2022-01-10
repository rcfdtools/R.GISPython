
## Weather values for the IDEAM national station catalog - CNE from OWM https://openweathermap.org - AEROPUERTO RAFAEL BARVO [25025080]

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025080_OWM_20220110.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220110.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.33388889,-75.28305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.33388889&lon=-75.28305556)


| Parameter | Value |
|---|---|
| Code | 25025080 |
| Name | AEROPUERTO RAFAEL BARVO [25025080] |
| Latitude, ° | 9.33388889 |
| Longitude, ° | -75.28305556 |
| Elevation, m | 166 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1940-06-15 00:00:00 |
| Suspension date | NaT |
| State | Sucre |
| County | Corozal |
| Stream | Ay Libra Arriba |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena- Cauca -San Jorge |
| SZH - Hydrographic subzone | Bajo San Jorge - La Mojana |

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

### 2643 - Open Weather values for station 000025025080: AEROPUERTO RAFAEL BARVO [25025080]

JSON data from API OWM:

```
{'lat': 9.3339, 'lon': -75.2831, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641749250, 'sunrise': 1641727182, 'sunset': 1641768984, 'temp': 30.18, 'feels_like': 32.01, 'pressure': 1013, 'humidity': 54, 'dew_point': 19.85, 'uvi': 10.46, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.95, 'wind_deg': 130, 'wind_gust': 3.46, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641686400, 'temp': 24.13, 'feels_like': 24.87, 'pressure': 1012, 'humidity': 87, 'dew_point': 21.83, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 4.31, 'wind_deg': 310, 'wind_gust': 8.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641690000, 'temp': 24.29, 'feels_like': 25.02, 'pressure': 1013, 'humidity': 86, 'dew_point': 21.8, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 4.29, 'wind_deg': 312, 'wind_gust': 7.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641693600, 'temp': 23.94, 'feels_like': 24.69, 'pressure': 1013, 'humidity': 88, 'dew_point': 21.83, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 3.46, 'wind_deg': 315, 'wind_gust': 6.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641697200, 'temp': 23.71, 'feels_like': 24.46, 'pressure': 1014, 'humidity': 89, 'dew_point': 21.79, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 310, 'wind_gust': 4.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641700800, 'temp': 23.56, 'feels_like': 24.3, 'pressure': 1013, 'humidity': 89, 'dew_point': 21.64, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.9, 'wind_deg': 313, 'wind_gust': 2.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641704400, 'temp': 23.57, 'feels_like': 24.25, 'pressure': 1013, 'humidity': 87, 'dew_point': 21.28, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 306, 'wind_gust': 2.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641708000, 'temp': 23.25, 'feels_like': 23.9, 'pressure': 1013, 'humidity': 87, 'dew_point': 20.97, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 271, 'wind_gust': 1.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641711600, 'temp': 23.09, 'feels_like': 23.73, 'pressure': 1012, 'humidity': 87, 'dew_point': 20.81, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 275, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641715200, 'temp': 22.89, 'feels_like': 23.51, 'pressure': 1012, 'humidity': 87, 'dew_point': 20.61, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 237, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641718800, 'temp': 22.74, 'feels_like': 23.37, 'pressure': 1012, 'humidity': 88, 'dew_point': 20.65, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 135, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641722400, 'temp': 22.42, 'feels_like': 23.07, 'pressure': 1012, 'humidity': 90, 'dew_point': 20.7, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 106, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641726000, 'temp': 21.99, 'feels_like': 22.65, 'pressure': 1013, 'humidity': 92, 'dew_point': 20.63, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 2.43, 'wind_deg': 101, 'wind_gust': 3.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641729600, 'temp': 22.36, 'feels_like': 23.08, 'pressure': 1013, 'humidity': 93, 'dew_point': 21.17, 'uvi': 0.22, 'clouds': 11, 'visibility': 10000, 'wind_speed': 2.77, 'wind_deg': 102, 'wind_gust': 4.74, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641733200, 'temp': 24.29, 'feels_like': 24.97, 'pressure': 1014, 'humidity': 84, 'dew_point': 21.41, 'uvi': 1.54, 'clouds': 16, 'visibility': 10000, 'wind_speed': 3.15, 'wind_deg': 106, 'wind_gust': 4.34, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641736800, 'temp': 26.16, 'feels_like': 26.16, 'pressure': 1015, 'humidity': 75, 'dew_point': 21.38, 'uvi': 3.93, 'clouds': 17, 'visibility': 10000, 'wind_speed': 3.49, 'wind_deg': 120, 'wind_gust': 4.59, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641740400, 'temp': 27.76, 'feels_like': 30.09, 'pressure': 1014, 'humidity': 69, 'dew_point': 21.55, 'uvi': 6.92, 'clouds': 29, 'visibility': 10000, 'wind_speed': 3.53, 'wind_deg': 124, 'wind_gust': 4.27, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641744000, 'temp': 29.13, 'feels_like': 31.42, 'pressure': 1014, 'humidity': 61, 'dew_point': 20.84, 'uvi': 9.46, 'clouds': 44, 'visibility': 10000, 'wind_speed': 3.29, 'wind_deg': 125, 'wind_gust': 3.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641747600, 'temp': 30.18, 'feels_like': 32.01, 'pressure': 1013, 'humidity': 54, 'dew_point': 19.85, 'uvi': 10.46, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.95, 'wind_deg': 130, 'wind_gust': 3.46, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641751200, 'temp': 30.79, 'feels_like': 32.46, 'pressure': 1011, 'humidity': 51, 'dew_point': 19.49, 'uvi': 9.58, 'clouds': 14, 'visibility': 10000, 'wind_speed': 2.77, 'wind_deg': 125, 'wind_gust': 3.26, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641754800, 'temp': 31.15, 'feels_like': 32.47, 'pressure': 1010, 'humidity': 48, 'dew_point': 18.84, 'uvi': 6.74, 'clouds': 24, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 117, 'wind_gust': 2.94, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641758400, 'temp': 31.27, 'feels_like': 32.47, 'pressure': 1009, 'humidity': 47, 'dew_point': 18.62, 'uvi': 3.91, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 113, 'wind_gust': 2.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641762000, 'temp': 31.04, 'feels_like': 32.3, 'pressure': 1009, 'humidity': 48, 'dew_point': 18.74, 'uvi': 1.57, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 96, 'wind_gust': 2.32, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641765600, 'temp': 29.95, 'feels_like': 32.16, 'pressure': 1009, 'humidity': 57, 'dew_point': 20.51, 'uvi': 0.33, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 342, 'wind_gust': 1.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641769200, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1009, 'humidity': 71, 'dew_point': 20.57, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.5, 'wind_deg': 303, 'wind_gust': 4.95, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Julian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 00:00:00 | 81.000000 | 21.830000 | 24.870000 | 87.000000 | 1012.000000 |  | 24.130000 | 0.000000 | 10000.000000 | 310.000000 | 8.07 | 4.310000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 01:00:00 | 88.000000 | 21.800000 | 25.020000 | 86.000000 | 1013.000000 |  | 24.290000 | 0.000000 | 10000.000000 | 312.000000 | 7.34 | 4.290000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 02:00:00 | 94.000000 | 21.830000 | 24.690000 | 88.000000 | 1013.000000 |  | 23.940000 | 0.000000 | 10000.000000 | 315.000000 | 6.53 | 3.460000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 03:00:00 | 96.000000 | 21.790000 | 24.460000 | 89.000000 | 1014.000000 |  | 23.710000 | 0.000000 | 10000.000000 | 310.000000 | 4.62 | 2.530000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 04:00:00 | 97.000000 | 21.640000 | 24.300000 | 89.000000 | 1013.000000 | 0.12 | 23.560000 | 0.000000 | 10000.000000 | 313.000000 | 2.94 | 1.900000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 05:00:00 | 97.000000 | 21.280000 | 24.250000 | 87.000000 | 1013.000000 |  | 23.570000 | 0.000000 | 10000.000000 | 306.000000 | 2.58 | 1.810000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 06:00:00 | 78.000000 | 20.970000 | 23.900000 | 87.000000 | 1013.000000 |  | 23.250000 | 0.000000 | 10000.000000 | 271.000000 | 1.6 | 1.370000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 07:00:00 | 85.000000 | 20.810000 | 23.730000 | 87.000000 | 1012.000000 |  | 23.090000 | 0.000000 | 10000.000000 | 275.000000 | 1.38 | 1.300000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 08:00:00 | 92.000000 | 20.610000 | 23.510000 | 87.000000 | 1012.000000 |  | 22.890000 | 0.000000 | 10000.000000 | 237.000000 | 0.84 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 09:00:00 | 89.000000 | 20.650000 | 23.370000 | 88.000000 | 1012.000000 |  | 22.740000 | 0.000000 | 10000.000000 | 135.000000 | 1.07 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 10:00:00 | 80.000000 | 20.700000 | 23.070000 | 90.000000 | 1012.000000 |  | 22.420000 | 0.000000 | 10000.000000 | 106.000000 | 1.75 | 1.720000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 11:00:00 | 65.000000 | 20.630000 | 22.650000 | 92.000000 | 1013.000000 |  | 21.990000 | 0.000000 | 10000.000000 | 101.000000 | 3.15 | 2.430000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 12:00:00 | 11.000000 | 21.170000 | 23.080000 | 93.000000 | 1013.000000 |  | 22.360000 | 0.220000 | 10000.000000 | 102.000000 | 4.74 | 2.770000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 13:00:00 | 16.000000 | 21.410000 | 24.970000 | 84.000000 | 1014.000000 |  | 24.290000 | 1.540000 | 10000.000000 | 106.000000 | 4.34 | 3.150000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 14:00:00 | 17.000000 | 21.380000 | 26.160000 | 75.000000 | 1015.000000 |  | 26.160000 | 3.930000 | 10000.000000 | 120.000000 | 4.59 | 3.490000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 15:00:00 | 29.000000 | 21.550000 | 30.090000 | 69.000000 | 1014.000000 |  | 27.760000 | 6.920000 | 10000.000000 | 124.000000 | 4.27 | 3.530000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 16:00:00 | 44.000000 | 20.840000 | 31.420000 | 61.000000 | 1014.000000 |  | 29.130000 | 9.460000 | 10000.000000 | 125.000000 | 3.91 | 3.290000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 17:00:00 | 49.000000 | 19.850000 | 32.010000 | 54.000000 | 1013.000000 |  | 30.180000 | 10.460000 | 10000.000000 | 130.000000 | 3.46 | 2.950000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 18:00:00 | 14.000000 | 19.490000 | 32.460000 | 51.000000 | 1011.000000 |  | 30.790000 | 9.580000 | 10000.000000 | 125.000000 | 3.26 | 2.770000 | 801 | Clouds | few clouds | 02d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 19:00:00 | 24.000000 | 18.840000 | 32.470000 | 48.000000 | 1010.000000 |  | 31.150000 | 6.740000 | 10000.000000 | 117.000000 | 2.94 | 2.360000 | 801 | Clouds | few clouds | 02d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 20:00:00 | 26.000000 | 18.620000 | 32.470000 | 47.000000 | 1009.000000 |  | 31.270000 | 3.910000 | 10000.000000 | 113.000000 | 2.55 | 1.800000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 21:00:00 | 32.000000 | 18.740000 | 32.300000 | 48.000000 | 1009.000000 |  | 31.040000 | 1.570000 | 10000.000000 | 96.000000 | 2.32 | 1.080000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 22:00:00 | 38.000000 | 20.510000 | 32.160000 | 57.000000 | 1009.000000 |  | 29.950000 | 0.330000 | 10000.000000 | 342.000000 | 1.91 | 1.010000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025080 | "AEROPUERTO RAFAEL BARVO [25025080]" | 9.333889 | -75.283056 | 166.000000 | Sinóptica Secundaria | Convencional | Activa | 1940-06-15 00:00:00 | NaT | Sucre | Corozal | Ay Libra Arriba | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-09 23:00:00 | 40.000000 | 20.570000 | 26.250000 | 71.000000 | 1009.000000 |  | 26.250000 | 0.000000 | 10000.000000 | 303.000000 | 4.95 | 3.500000 | 802 | Clouds | scattered clouds | 03n | 23 |
