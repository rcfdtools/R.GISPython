
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CAMPO BELLO [13015030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13015030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.98333333,-76.23333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.98333333&lon=-76.23333333)


| Parameter | Value |
|---|---|
| Code | 13015030 |
| Name | CAMPO BELLO [13015030] |
| Latitude, ° | 7.98333333 |
| Longitude, ° | -76.23333333 |
| Elevation, m | 78 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1996-12-15 00:00:00 |
| Suspension date | 2008-03-31 00:00:00 |
| State | Córdoba |
| County | Tierralta |
| Stream | Magdalena |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Alto Sinú - Urrá |

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

### (CNE index 345) Open Weather values for station 13015030 - CAMPO BELLO [13015030]

JSON data from API OWM:

```
{'lat': 7.9833, 'lon': -76.2333, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813695, 'sunset': 1641855776, 'temp': 27.25, 'feels_like': 30.98, 'pressure': 1010, 'humidity': 86, 'dew_point': 24.7, 'uvi': 3.66, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 318, 'wind_gust': 3.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, 'hourly': [{'dt': 1641772800, 'temp': 25.25, 'feels_like': 26.18, 'pressure': 1011, 'humidity': 90, 'dew_point': 23.49, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 326, 'wind_gust': 0.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.25, 'feels_like': 26.26, 'pressure': 1012, 'humidity': 93, 'dew_point': 24.04, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 311, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.11, 'feels_like': 23.96, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.26, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 298, 'wind_gust': 0.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.89, 'feels_like': 23.74, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.22, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 256, 'wind_gust': 0.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.65, 'feels_like': 23.5, 'pressure': 1012, 'humidity': 97, 'dew_point': 22.15, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 251, 'wind_gust': 0.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.41, 'feels_like': 23.24, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.91, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 291, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.1, 'feels_like': 22.9, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.6, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 268, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641798000, 'temp': 21.82, 'feels_like': 22.62, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.49, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 282, 'wind_gust': 0.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.67, 'feels_like': 22.45, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.34, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 219, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 21.64, 'feels_like': 22.42, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.31, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 202, 'wind_gust': 1.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.6, 'feels_like': 22.35, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.1, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 202, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641812400, 'temp': 24.25, 'feels_like': 25.29, 'pressure': 1012, 'humidity': 98, 'dew_point': 23.91, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 205, 'wind_gust': 1.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.25, 'feels_like': 25.24, 'pressure': 1013, 'humidity': 96, 'dew_point': 23.57, 'uvi': 0.28, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 197, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.25, 'feels_like': 25.05, 'pressure': 1014, 'humidity': 89, 'dew_point': 22.32, 'uvi': 1.48, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 197, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.25, 'feels_like': 25.87, 'pressure': 1015, 'humidity': 78, 'dew_point': 21.14, 'uvi': 3.83, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 223, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641826800, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1014, 'humidity': 70, 'dew_point': 20.34, 'uvi': 6.85, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 287, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641830400, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1014, 'humidity': 64, 'dew_point': 18.9, 'uvi': 8.66, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 323, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 27.25, 'feels_like': 28.65, 'pressure': 1012, 'humidity': 63, 'dew_point': 19.59, 'uvi': 9.71, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 342, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641837600, 'temp': 27.25, 'feels_like': 29.19, 'pressure': 1012, 'humidity': 69, 'dew_point': 21.07, 'uvi': 8.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 332, 'wind_gust': 1.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641841200, 'temp': 27.25, 'feels_like': 30.52, 'pressure': 1011, 'humidity': 82, 'dew_point': 23.91, 'uvi': 6.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 324, 'wind_gust': 2.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641844800, 'temp': 27.25, 'feels_like': 30.98, 'pressure': 1010, 'humidity': 86, 'dew_point': 24.7, 'uvi': 3.66, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 318, 'wind_gust': 3.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641848400, 'temp': 27.25, 'feels_like': 30.98, 'pressure': 1009, 'humidity': 86, 'dew_point': 24.7, 'uvi': 1.52, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 323, 'wind_gust': 3.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641852000, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1010, 'humidity': 91, 'dew_point': 24.66, 'uvi': 0.33, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 333, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641855600, 'temp': 25.25, 'feels_like': 26.23, 'pressure': 1011, 'humidity': 92, 'dew_point': 23.86, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 322, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 00:00:00 | 98.000000 | 23.490000 | 26.180000 | 90.000000 | 1011.000000 |  | 25.250000 | 0.000000 | 10000.000000 | 326.000000 | 0.42 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 24.040000 | 26.260000 | 93.000000 | 1012.000000 |  | 25.250000 | 0.000000 | 10000.000000 | 311.000000 | 0.71 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 22.260000 | 23.960000 | 95.000000 | 1013.000000 |  | 23.110000 | 0.000000 | 10000.000000 | 298.000000 | 0.36 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 22.220000 | 23.740000 | 96.000000 | 1013.000000 |  | 22.890000 | 0.000000 | 10000.000000 | 256.000000 | 0.36 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 22.150000 | 23.500000 | 97.000000 | 1012.000000 |  | 22.650000 | 0.000000 | 10000.000000 | 251.000000 | 0.45 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 21.910000 | 23.240000 | 97.000000 | 1012.000000 |  | 22.410000 | 0.000000 | 10000.000000 | 291.000000 | 0.44 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 06:00:00 | 90.000000 | 21.600000 | 22.900000 | 97.000000 | 1012.000000 | 0.25 | 22.100000 | 0.000000 | 10000.000000 | 268.000000 | 0.45 | 0.410000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 07:00:00 | 92.000000 | 21.490000 | 22.620000 | 98.000000 | 1011.000000 |  | 21.820000 | 0.000000 | 10000.000000 | 282.000000 | 0.27 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 08:00:00 | 63.000000 | 21.340000 | 22.450000 | 98.000000 | 1011.000000 | 0.13 | 21.670000 | 0.000000 | 10000.000000 | 219.000000 | 0.81 | 0.790000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 09:00:00 | 53.000000 | 21.310000 | 22.420000 | 98.000000 | 1011.000000 |  | 21.640000 | 0.000000 | 10000.000000 | 202.000000 | 1.16 | 1.200000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 10:00:00 | 63.000000 | 21.100000 | 22.350000 | 97.000000 | 1012.000000 | 0.13 | 21.600000 | 0.000000 | 10000.000000 | 202.000000 | 1.19 | 1.250000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 11:00:00 | 62.000000 | 23.910000 | 25.290000 | 98.000000 | 1012.000000 |  | 24.250000 | 0.000000 | 10000.000000 | 205.000000 | 1.17 | 1.200000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 12:00:00 | 83.000000 | 23.570000 | 25.240000 | 96.000000 | 1013.000000 |  | 24.250000 | 0.280000 | 10000.000000 | 197.000000 | 1.43 | 1.130000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 13:00:00 | 94.000000 | 22.320000 | 25.050000 | 89.000000 | 1014.000000 |  | 24.250000 | 1.480000 | 10000.000000 | 197.000000 | 1.44 | 0.970000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 21.140000 | 25.870000 | 78.000000 | 1015.000000 | 0.14 | 25.250000 | 3.830000 | 10000.000000 | 223.000000 | 1.04 | 0.770000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 20.340000 | 26.250000 | 70.000000 | 1014.000000 | 0.19 | 26.250000 | 6.850000 | 10000.000000 | 287.000000 | 0.96 | 0.540000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 18.900000 | 26.250000 | 64.000000 | 1014.000000 | 0.12 | 26.250000 | 8.660000 | 10000.000000 | 323.000000 | 0.83 | 0.790000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 19.590000 | 28.650000 | 63.000000 | 1012.000000 | 0.18 | 27.250000 | 9.710000 | 10000.000000 | 342.000000 | 1.2 | 1.570000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 21.070000 | 29.190000 | 69.000000 | 1012.000000 | 0.48 | 27.250000 | 8.990000 | 10000.000000 | 332.000000 | 1.84 | 2.020000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 23.910000 | 30.520000 | 82.000000 | 1011.000000 | 0.66 | 27.250000 | 6.140000 | 10000.000000 | 324.000000 | 2.97 | 1.840000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 24.700000 | 30.980000 | 86.000000 | 1010.000000 | 0.56 | 27.250000 | 3.660000 | 10000.000000 | 318.000000 | 3.01 | 1.350000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 24.700000 | 30.980000 | 86.000000 | 1009.000000 | 0.56 | 27.250000 | 1.520000 | 10000.000000 | 323.000000 | 3.15 | 1.490000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 24.660000 | 26.250000 | 91.000000 | 1010.000000 | 0.33 | 26.250000 | 0.330000 | 10000.000000 | 333.000000 | 1.85 | 1.140000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015030 | "CAMPO BELLO [13015030]" | 7.983333 | -76.233333 | 78.000000 | Climática Principal | Convencional | Suspendida | 1996-12-15 00:00:00 | 2008-03-31 00:00:00 | Córdoba | Tierralta | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 23.860000 | 26.230000 | 92.000000 | 1011.000000 | 0.6 | 25.250000 | 0.000000 | 10000.000000 | 322.000000 | 1.07 | 1.030000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station13015030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13015030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13015030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015030_OWM_Windspeed_20220111.png)
