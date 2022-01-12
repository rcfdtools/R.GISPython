
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ARBOLETES [12045010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station12045010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.84694444,-76.43194444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.84694444&lon=-76.43194444)


| Parameter | Value |
|---|---|
| Code | 12045010 |
| Name | ARBOLETES [12045010] |
| Latitude, ° | 8.84694444 |
| Longitude, ° | -76.43194444 |
| Elevation, m | 4 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1972-03-15 00:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Arboletes |
| Stream | Magdalena |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Litoral |
| SZH - Hydrographic subzone | Rio Canalete y otros Arroyos Directos al Caribe |

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

### (CNE index 3294) Open Weather values for station 12045010 - ARBOLETES [12045010]

JSON data from API OWM:

```
{'lat': 8.8469, 'lon': -76.4319, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813828, 'sunset': 1641855739, 'temp': 31.99, 'feels_like': 38.99, 'pressure': 1009, 'humidity': 72, 'dew_point': 26.3, 'uvi': 3.25, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 291, 'wind_gust': 2.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.99, 'feels_like': 29.81, 'pressure': 1010, 'humidity': 81, 'dew_point': 23.45, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 328, 'wind_gust': 3.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.99, 'feels_like': 25.99, 'pressure': 1011, 'humidity': 82, 'dew_point': 22.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.37, 'wind_deg': 334, 'wind_gust': 4.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.99, 'feels_like': 25.71, 'pressure': 1012, 'humidity': 83, 'dew_point': 21.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.56, 'wind_deg': 340, 'wind_gust': 4.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.99, 'feels_like': 25.99, 'pressure': 1012, 'humidity': 85, 'dew_point': 23.27, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 4.13, 'wind_deg': 339, 'wind_gust': 5.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.99, 'feels_like': 25.99, 'pressure': 1012, 'humidity': 84, 'dew_point': 23.08, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 4.17, 'wind_deg': 346, 'wind_gust': 5.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.99, 'feels_like': 25.99, 'pressure': 1011, 'humidity': 84, 'dew_point': 23.08, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 3.98, 'wind_deg': 348, 'wind_gust': 5.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.51, 'feels_like': 26.31, 'pressure': 1011, 'humidity': 84, 'dew_point': 22.61, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 4.37, 'wind_deg': 352, 'wind_gust': 6.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 25.39, 'feels_like': 26.18, 'pressure': 1010, 'humidity': 84, 'dew_point': 22.49, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 4.13, 'wind_deg': 346, 'wind_gust': 6.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 25.36, 'feels_like': 26.14, 'pressure': 1010, 'humidity': 84, 'dew_point': 22.46, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 4.11, 'wind_deg': 335, 'wind_gust': 5.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.38}}, {'dt': 1641805200, 'temp': 25.27, 'feels_like': 26.05, 'pressure': 1010, 'humidity': 84, 'dew_point': 22.37, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 3.8, 'wind_deg': 330, 'wind_gust': 5.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641808800, 'temp': 24.94, 'feels_like': 25.71, 'pressure': 1010, 'humidity': 85, 'dew_point': 22.24, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 3.31, 'wind_deg': 325, 'wind_gust': 4.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.85}}, {'dt': 1641812400, 'temp': 22.99, 'feels_like': 23.59, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.52, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 319, 'wind_gust': 3.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.2}}, {'dt': 1641816000, 'temp': 22.99, 'feels_like': 23.56, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.33, 'uvi': 0.28, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 306, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}, {'dt': 1641819600, 'temp': 24.99, 'feels_like': 25.66, 'pressure': 1013, 'humidity': 81, 'dew_point': 21.5, 'uvi': 1.37, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 297, 'wind_gust': 2.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641823200, 'temp': 27.99, 'feels_like': 31.48, 'pressure': 1014, 'humidity': 76, 'dew_point': 23.36, 'uvi': 3.58, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 311, 'wind_gust': 2.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641826800, 'temp': 28.99, 'feels_like': 33.27, 'pressure': 1014, 'humidity': 73, 'dew_point': 23.66, 'uvi': 6.44, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 311, 'wind_gust': 1.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641830400, 'temp': 29.99, 'feels_like': 35.5, 'pressure': 1013, 'humidity': 72, 'dew_point': 24.39, 'uvi': 8.29, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 309, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641834000, 'temp': 30.99, 'feels_like': 37.88, 'pressure': 1012, 'humidity': 71, 'dew_point': 25.11, 'uvi': 9.29, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 292, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 31.99, 'feels_like': 38.99, 'pressure': 1012, 'humidity': 69, 'dew_point': 25.59, 'uvi': 8.61, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.87, 'wind_deg': 286, 'wind_gust': 2.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.99, 'feels_like': 38.99, 'pressure': 1010, 'humidity': 70, 'dew_point': 25.83, 'uvi': 5.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.04, 'wind_deg': 288, 'wind_gust': 2.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.99, 'feels_like': 38.99, 'pressure': 1009, 'humidity': 72, 'dew_point': 26.3, 'uvi': 3.25, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 291, 'wind_gust': 2.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.99, 'feels_like': 37.99, 'pressure': 1009, 'humidity': 74, 'dew_point': 25.81, 'uvi': 1.34, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.06, 'wind_deg': 282, 'wind_gust': 3.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.99, 'feels_like': 36.99, 'pressure': 1009, 'humidity': 78, 'dew_point': 25.73, 'uvi': 0.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.92, 'wind_deg': 285, 'wind_gust': 3.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.99, 'feels_like': 32.23, 'pressure': 1010, 'humidity': 81, 'dew_point': 24.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.55, 'wind_deg': 287, 'wind_gust': 3.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 23.450000 | 29.810000 | 81.000000 | 1010.000000 |  | 26.990000 | 0.000000 | 10000.000000 | 328.000000 | 3.92 | 3.280000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 22.680000 | 25.990000 | 82.000000 | 1011.000000 |  | 25.990000 | 0.000000 | 10000.000000 | 334.000000 | 4.2 | 3.370000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 21.900000 | 25.710000 | 83.000000 | 1012.000000 |  | 24.990000 | 0.000000 | 10000.000000 | 340.000000 | 4.31 | 3.560000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 23.270000 | 25.990000 | 85.000000 | 1012.000000 |  | 25.990000 | 0.000000 | 10000.000000 | 339.000000 | 5.6 | 4.130000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 23.080000 | 25.990000 | 84.000000 | 1012.000000 |  | 25.990000 | 0.000000 | 10000.000000 | 346.000000 | 5.95 | 4.170000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 23.080000 | 25.990000 | 84.000000 | 1011.000000 |  | 25.990000 | 0.000000 | 10000.000000 | 348.000000 | 5.78 | 3.980000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 06:00:00 | 38.000000 | 22.610000 | 26.310000 | 84.000000 | 1011.000000 |  | 25.510000 | 0.000000 | 10000.000000 | 352.000000 | 6.43 | 4.370000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 07:00:00 | 47.000000 | 22.490000 | 26.180000 | 84.000000 | 1010.000000 | 0.19 | 25.390000 | 0.000000 | 10000.000000 | 346.000000 | 6.09 | 4.130000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 08:00:00 | 54.000000 | 22.460000 | 26.140000 | 84.000000 | 1010.000000 | 0.38 | 25.360000 | 0.000000 | 10000.000000 | 335.000000 | 5.74 | 4.110000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 09:00:00 | 48.000000 | 22.370000 | 26.050000 | 84.000000 | 1010.000000 | 0.32 | 25.270000 | 0.000000 | 10000.000000 | 330.000000 | 5.29 | 3.800000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 10:00:00 | 43.000000 | 22.240000 | 25.710000 | 85.000000 | 1010.000000 | 0.85 | 24.940000 | 0.000000 | 10000.000000 | 325.000000 | 4.52 | 3.310000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 11:00:00 | 42.000000 | 20.520000 | 23.590000 | 86.000000 | 1011.000000 | 1.2 | 22.990000 | 0.000000 | 10000.000000 | 319.000000 | 3.05 | 2.810000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 12:00:00 | 48.000000 | 20.330000 | 23.560000 | 85.000000 | 1012.000000 | 0.95 | 22.990000 | 0.280000 | 10000.000000 | 306.000000 | 2.23 | 1.720000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 13:00:00 | 69.000000 | 21.500000 | 25.660000 | 81.000000 | 1013.000000 | 0.58 | 24.990000 | 1.370000 | 10000.000000 | 297.000000 | 2.08 | 1.700000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 23.360000 | 31.480000 | 76.000000 | 1014.000000 | 0.47 | 27.990000 | 3.580000 | 10000.000000 | 311.000000 | 2.53 | 1.990000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 15:00:00 | 90.000000 | 23.660000 | 33.270000 | 73.000000 | 1014.000000 | 0.25 | 28.990000 | 6.440000 | 10000.000000 | 311.000000 | 1.98 | 1.810000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 16:00:00 | 92.000000 | 24.390000 | 35.500000 | 72.000000 | 1013.000000 | 0.19 | 29.990000 | 8.290000 | 10000.000000 | 309.000000 | 1.72 | 1.800000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 17:00:00 | 94.000000 | 25.110000 | 37.880000 | 71.000000 | 1012.000000 | 0.11 | 30.990000 | 9.290000 | 10000.000000 | 292.000000 | 1.93 | 2.360000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 25.590000 | 38.990000 | 69.000000 | 1012.000000 |  | 31.990000 | 8.610000 | 10000.000000 | 286.000000 | 2.27 | 2.870000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 25.830000 | 38.990000 | 70.000000 | 1010.000000 |  | 31.990000 | 5.480000 | 10000.000000 | 288.000000 | 2.49 | 3.040000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 26.300000 | 38.990000 | 72.000000 | 1009.000000 |  | 31.990000 | 3.250000 | 10000.000000 | 291.000000 | 2.65 | 2.960000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 25.810000 | 37.990000 | 74.000000 | 1009.000000 |  | 30.990000 | 1.340000 | 10000.000000 | 282.000000 | 3.06 | 3.060000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 25.730000 | 36.990000 | 78.000000 | 1009.000000 |  | 29.990000 | 0.300000 | 10000.000000 | 285.000000 | 3.64 | 2.920000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 12045010 | "ARBOLETES [12045010]" | 8.846944 | -76.431944 | 4.000000 | Climática Principal | Convencional | Activa | 1972-03-15 00:00:00 | NaT | Antioquia | Arboletes | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Rio Canalete y otros Arroyos Directos al Caribe | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 24.420000 | 32.230000 | 81.000000 | 1010.000000 |  | 27.990000 | 0.000000 | 10000.000000 | 287.000000 | 3.15 | 2.550000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station12045010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station12045010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station12045010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station12045010_OWM_Windspeed_20220111.png)
