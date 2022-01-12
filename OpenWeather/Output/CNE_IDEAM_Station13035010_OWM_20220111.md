
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PUERTO NUEVO [13035010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13035010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.95,-76.28333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.95&lon=-76.28333333)


| Parameter | Value |
|---|---|
| Code | 13035010 |
| Name | PUERTO NUEVO [13035010] |
| Latitude, ° | 7.95 |
| Longitude, ° | -76.28333333 |
| Elevation, m | 145 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1965-09-15 00:00:00 |
| Suspension date | 1991-12-15 00:00:00 |
| State | Córdoba |
| County | Tierralta |
| Stream | El Zulia |
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

### (CNE index 703) Open Weather values for station 13035010 - PUERTO NUEVO [13035010]

JSON data from API OWM:

```
{'lat': 7.95, 'lon': -76.2833, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813704, 'sunset': 1641855791, 'temp': 27.35, 'feels_like': 30.88, 'pressure': 1010, 'humidity': 83, 'dew_point': 24.21, 'uvi': 3.66, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 317, 'wind_gust': 2.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, 'hourly': [{'dt': 1641772800, 'temp': 25.35, 'feels_like': 26.32, 'pressure': 1011, 'humidity': 91, 'dew_point': 23.77, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 325, 'wind_gust': 0.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.35, 'feels_like': 26.4, 'pressure': 1012, 'humidity': 94, 'dew_point': 24.31, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 315, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.15, 'feels_like': 24, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.3, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 311, 'wind_gust': 0.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.94, 'feels_like': 23.8, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.27, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 257, 'wind_gust': 0.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.7, 'feels_like': 23.56, 'pressure': 1012, 'humidity': 97, 'dew_point': 22.2, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 249, 'wind_gust': 0.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.45, 'feels_like': 23.28, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.95, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 291, 'wind_gust': 0.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.16, 'feels_like': 22.96, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.66, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 261, 'wind_gust': 0.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641798000, 'temp': 21.9, 'feels_like': 22.7, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.57, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 277, 'wind_gust': 0.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.73, 'feels_like': 22.52, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.4, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 219, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641805200, 'temp': 21.72, 'feels_like': 22.51, 'pressure': 1011, 'humidity': 98, 'dew_point': 21.39, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 201, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.67, 'feels_like': 22.45, 'pressure': 1012, 'humidity': 98, 'dew_point': 21.34, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 202, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641812400, 'temp': 24.35, 'feels_like': 25.4, 'pressure': 1012, 'humidity': 98, 'dew_point': 24.01, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 204, 'wind_gust': 0.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.35, 'feels_like': 25.35, 'pressure': 1013, 'humidity': 96, 'dew_point': 23.67, 'uvi': 0.28, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 196, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.35, 'feels_like': 25.19, 'pressure': 1014, 'humidity': 90, 'dew_point': 22.6, 'uvi': 1.48, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 195, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.35, 'feels_like': 26, 'pressure': 1015, 'humidity': 79, 'dew_point': 21.44, 'uvi': 3.83, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 226, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641826800, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1014, 'humidity': 71, 'dew_point': 20.67, 'uvi': 6.85, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 293, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641830400, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1014, 'humidity': 65, 'dew_point': 19.25, 'uvi': 8.66, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 324, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641834000, 'temp': 27.35, 'feels_like': 28.8, 'pressure': 1013, 'humidity': 63, 'dew_point': 19.69, 'uvi': 9.71, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 338, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641837600, 'temp': 27.35, 'feels_like': 29.26, 'pressure': 1012, 'humidity': 68, 'dew_point': 20.92, 'uvi': 8.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 327, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641841200, 'temp': 27.35, 'feels_like': 30.42, 'pressure': 1011, 'humidity': 79, 'dew_point': 23.38, 'uvi': 6.14, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 321, 'wind_gust': 2.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641844800, 'temp': 27.35, 'feels_like': 30.88, 'pressure': 1010, 'humidity': 83, 'dew_point': 24.21, 'uvi': 3.66, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 317, 'wind_gust': 2.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641848400, 'temp': 27.35, 'feels_like': 31, 'pressure': 1009, 'humidity': 84, 'dew_point': 24.41, 'uvi': 1.52, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 323, 'wind_gust': 2.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641852000, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1010, 'humidity': 90, 'dew_point': 24.58, 'uvi': 0.33, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 331, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641855600, 'temp': 25.35, 'feels_like': 26.34, 'pressure': 1011, 'humidity': 92, 'dew_point': 23.95, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 320, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 00:00:00 | 88.000000 | 23.770000 | 26.320000 | 91.000000 | 1011.000000 |  | 25.350000 | 0.000000 | 10000.000000 | 325.000000 | 0.49 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 01:00:00 | 89.000000 | 24.310000 | 26.400000 | 94.000000 | 1012.000000 |  | 25.350000 | 0.000000 | 10000.000000 | 315.000000 | 0.71 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 02:00:00 | 94.000000 | 22.300000 | 24.000000 | 95.000000 | 1013.000000 |  | 23.150000 | 0.000000 | 10000.000000 | 311.000000 | 0.41 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 22.270000 | 23.800000 | 96.000000 | 1013.000000 |  | 22.940000 | 0.000000 | 10000.000000 | 257.000000 | 0.38 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 22.200000 | 23.560000 | 97.000000 | 1012.000000 |  | 22.700000 | 0.000000 | 10000.000000 | 249.000000 | 0.45 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 21.950000 | 23.280000 | 97.000000 | 1012.000000 |  | 22.450000 | 0.000000 | 10000.000000 | 291.000000 | 0.42 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 06:00:00 | 80.000000 | 21.660000 | 22.960000 | 97.000000 | 1012.000000 | 0.24 | 22.160000 | 0.000000 | 10000.000000 | 261.000000 | 0.47 | 0.320000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 07:00:00 | 83.000000 | 21.570000 | 22.700000 | 98.000000 | 1011.000000 |  | 21.900000 | 0.000000 | 10000.000000 | 277.000000 | 0.31 | 0.230000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 08:00:00 | 62.000000 | 21.400000 | 22.520000 | 98.000000 | 1011.000000 | 0.14 | 21.730000 | 0.000000 | 10000.000000 | 219.000000 | 0.73 | 0.650000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 09:00:00 | 51.000000 | 21.390000 | 22.510000 | 98.000000 | 1011.000000 |  | 21.720000 | 0.000000 | 10000.000000 | 201.000000 | 1.02 | 1.030000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 10:00:00 | 62.000000 | 21.340000 | 22.450000 | 98.000000 | 1012.000000 | 0.13 | 21.670000 | 0.000000 | 10000.000000 | 202.000000 | 1.04 | 1.080000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 11:00:00 | 61.000000 | 24.010000 | 25.400000 | 98.000000 | 1012.000000 |  | 24.350000 | 0.000000 | 10000.000000 | 204.000000 | 0.99 | 1.020000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 12:00:00 | 84.000000 | 23.670000 | 25.350000 | 96.000000 | 1013.000000 |  | 24.350000 | 0.280000 | 10000.000000 | 196.000000 | 1.2 | 0.970000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 13:00:00 | 96.000000 | 22.600000 | 25.190000 | 90.000000 | 1014.000000 |  | 24.350000 | 1.480000 | 10000.000000 | 195.000000 | 1.26 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 21.440000 | 26.000000 | 79.000000 | 1015.000000 | 0.14 | 25.350000 | 3.830000 | 10000.000000 | 226.000000 | 1.07 | 0.650000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 20.670000 | 26.350000 | 71.000000 | 1014.000000 | 0.21 | 26.350000 | 6.850000 | 10000.000000 | 293.000000 | 0.97 | 0.520000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 19.250000 | 26.350000 | 65.000000 | 1014.000000 | 0.13 | 26.350000 | 8.660000 | 10000.000000 | 324.000000 | 0.92 | 0.850000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 19.690000 | 28.800000 | 63.000000 | 1013.000000 | 0.21 | 27.350000 | 9.710000 | 10000.000000 | 338.000000 | 1.23 | 1.490000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 20.920000 | 29.260000 | 68.000000 | 1012.000000 | 0.48 | 27.350000 | 8.990000 | 10000.000000 | 327.000000 | 1.75 | 1.850000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 23.380000 | 30.420000 | 79.000000 | 1011.000000 | 0.61 | 27.350000 | 6.140000 | 10000.000000 | 321.000000 | 2.73 | 1.790000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 24.210000 | 30.880000 | 83.000000 | 1010.000000 | 0.52 | 27.350000 | 3.660000 | 10000.000000 | 317.000000 | 2.91 | 1.380000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 21:00:00 | 95.000000 | 24.410000 | 31.000000 | 84.000000 | 1009.000000 | 0.54 | 27.350000 | 1.520000 | 10000.000000 | 323.000000 | 2.94 | 1.400000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 24.580000 | 26.350000 | 90.000000 | 1010.000000 | 0.33 | 26.350000 | 0.330000 | 10000.000000 | 331.000000 | 1.72 | 1.070000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13035010 | "PUERTO NUEVO [13035010]" | 7.950000 | -76.283333 | 145.000000 | Climática Principal | Convencional | Suspendida | 1965-09-15 00:00:00 | 1991-12-15 00:00:00 | Córdoba | Tierralta | El Zulia | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Alto Sinú - Urrá | America/Bogota | 2022-01-10 23:00:00 | 97.000000 | 23.950000 | 26.340000 | 92.000000 | 1011.000000 | 0.52 | 25.350000 | 0.000000 | 10000.000000 | 320.000000 | 0.97 | 0.930000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station13035010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13035010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13035010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13035010_OWM_Windspeed_20220111.png)
