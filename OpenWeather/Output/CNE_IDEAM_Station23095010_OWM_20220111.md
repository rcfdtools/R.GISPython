
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO PUERTO BERRIO [23095010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23095010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.465,-74.41222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.465&lon=-74.41222222)


| Parameter | Value |
|---|---|
| Code | 23095010 |
| Name | AEROPUERTO PUERTO BERRIO [23095010] |
| Latitude, ° | 6.465 |
| Longitude, ° | -74.41222222 |
| Elevation, m | 150 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1975-04-15 00:00:00 |
| Suspension date | 2018-07-13 12:10:26 |
| State | Antioquia |
| County | Puerto Berrío |
| Stream | 0 |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Rió San Bartolo y otros directos al Magdalena Medio |

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

### (CNE index 885) Open Weather values for station 23095010 - AEROPUERTO PUERTO BERRIO [23095010]

JSON data from API OWM:

```
{'lat': 6.465, 'lon': -74.4122, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813110, 'sunset': 1641855487, 'temp': 31.97, 'feels_like': 33.84, 'pressure': 1007, 'humidity': 48, 'dew_point': 19.59, 'uvi': 4.5, 'clouds': 18, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 34, 'wind_gust': 2.38, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.99, 'feels_like': 25.69, 'pressure': 1010, 'humidity': 82, 'dew_point': 21.7, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 325, 'wind_gust': 0.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 24.39, 'feels_like': 25.1, 'pressure': 1011, 'humidity': 85, 'dew_point': 21.7, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 312, 'wind_gust': 0.87, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 23.96, 'feels_like': 24.66, 'pressure': 1011, 'humidity': 86, 'dew_point': 21.47, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 288, 'wind_gust': 0.76, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 23.54, 'feels_like': 24.22, 'pressure': 1011, 'humidity': 87, 'dew_point': 21.25, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 275, 'wind_gust': 0.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 23.1, 'feels_like': 23.79, 'pressure': 1011, 'humidity': 89, 'dew_point': 21.19, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 267, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.73, 'feels_like': 23.41, 'pressure': 1011, 'humidity': 90, 'dew_point': 21, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 267, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.38, 'feels_like': 23.02, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.66, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 257, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.1, 'feels_like': 22.74, 'pressure': 1010, 'humidity': 91, 'dew_point': 20.56, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 260, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.83, 'feels_like': 22.47, 'pressure': 1010, 'humidity': 92, 'dew_point': 20.47, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 250, 'wind_gust': 0.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 21.6, 'feels_like': 22.24, 'pressure': 1010, 'humidity': 93, 'dew_point': 20.42, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 271, 'wind_gust': 0.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 21.4, 'feels_like': 22.05, 'pressure': 1011, 'humidity': 94, 'dew_point': 20.39, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 296, 'wind_gust': 0.41, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 21.21, 'feels_like': 21.84, 'pressure': 1012, 'humidity': 94, 'dew_point': 20.21, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 279, 'wind_gust': 0.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 22.16, 'feels_like': 22.78, 'pressure': 1013, 'humidity': 90, 'dew_point': 20.44, 'uvi': 0.44, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 275, 'wind_gust': 0.33, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 24.63, 'feels_like': 25.21, 'pressure': 1014, 'humidity': 79, 'dew_point': 20.75, 'uvi': 1.92, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 89, 'wind_gust': 0.34, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 27.02, 'feels_like': 28.89, 'pressure': 1015, 'humidity': 70, 'dew_point': 21.08, 'uvi': 4.7, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 52, 'wind_gust': 1.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 28.94, 'feels_like': 31.4, 'pressure': 1014, 'humidity': 63, 'dew_point': 21.19, 'uvi': 7.99, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 50, 'wind_gust': 1.84, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 30.26, 'feels_like': 32.72, 'pressure': 1013, 'humidity': 57, 'dew_point': 20.8, 'uvi': 10.58, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 46, 'wind_gust': 2.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 31.26, 'feels_like': 33.7, 'pressure': 1012, 'humidity': 53, 'dew_point': 20.54, 'uvi': 11.52, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 44, 'wind_gust': 2.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 31.96, 'feels_like': 34.06, 'pressure': 1010, 'humidity': 49, 'dew_point': 19.91, 'uvi': 10.44, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 40, 'wind_gust': 2.41, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 32.27, 'feels_like': 34.14, 'pressure': 1009, 'humidity': 47, 'dew_point': 19.52, 'uvi': 7.79, 'clouds': 27, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 32, 'wind_gust': 2.31, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 31.97, 'feels_like': 33.84, 'pressure': 1007, 'humidity': 48, 'dew_point': 19.59, 'uvi': 4.5, 'clouds': 18, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 34, 'wind_gust': 2.38, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641848400, 'temp': 31.35, 'feels_like': 33.42, 'pressure': 1007, 'humidity': 51, 'dew_point': 20, 'uvi': 1.79, 'clouds': 18, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 26, 'wind_gust': 2.36, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641852000, 'temp': 29.34, 'feels_like': 32.51, 'pressure': 1008, 'humidity': 65, 'dew_point': 22.08, 'uvi': 0.38, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 24, 'wind_gust': 1.49, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 25.76, 'feels_like': 26.45, 'pressure': 1009, 'humidity': 79, 'dew_point': 21.84, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 340, 'wind_gust': 1.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 00:00:00 | 32.000000 | 21.700000 | 25.690000 | 82.000000 | 1010.000000 |  | 24.990000 | 0.000000 | 10000.000000 | 325.000000 | 0.97 | 0.890000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 01:00:00 | 47.000000 | 21.700000 | 25.100000 | 85.000000 | 1011.000000 |  | 24.390000 | 0.000000 | 10000.000000 | 312.000000 | 0.87 | 0.890000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 02:00:00 | 35.000000 | 21.470000 | 24.660000 | 86.000000 | 1011.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 288.000000 | 0.76 | 0.850000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 03:00:00 | 43.000000 | 21.250000 | 24.220000 | 87.000000 | 1011.000000 |  | 23.540000 | 0.000000 | 10000.000000 | 275.000000 | 0.73 | 0.790000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 04:00:00 | 55.000000 | 21.190000 | 23.790000 | 89.000000 | 1011.000000 |  | 23.100000 | 0.000000 | 10000.000000 | 267.000000 | 0.8 | 0.840000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 05:00:00 | 60.000000 | 21.000000 | 23.410000 | 90.000000 | 1011.000000 |  | 22.730000 | 0.000000 | 10000.000000 | 267.000000 | 0.75 | 0.680000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 06:00:00 | 67.000000 | 20.660000 | 23.020000 | 90.000000 | 1011.000000 |  | 22.380000 | 0.000000 | 10000.000000 | 257.000000 | 0.74 | 0.730000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 20.560000 | 22.740000 | 91.000000 | 1010.000000 |  | 22.100000 | 0.000000 | 10000.000000 | 260.000000 | 0.81 | 0.720000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 08:00:00 | 47.000000 | 20.470000 | 22.470000 | 92.000000 | 1010.000000 |  | 21.830000 | 0.000000 | 10000.000000 | 250.000000 | 0.67 | 0.530000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 09:00:00 | 38.000000 | 20.420000 | 22.240000 | 93.000000 | 1010.000000 |  | 21.600000 | 0.000000 | 10000.000000 | 271.000000 | 0.47 | 0.420000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 10:00:00 | 34.000000 | 20.390000 | 22.050000 | 94.000000 | 1011.000000 |  | 21.400000 | 0.000000 | 10000.000000 | 296.000000 | 0.41 | 0.400000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 11:00:00 | 36.000000 | 20.210000 | 21.840000 | 94.000000 | 1012.000000 |  | 21.210000 | 0.000000 | 10000.000000 | 279.000000 | 0.3 | 0.280000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 12:00:00 | 35.000000 | 20.440000 | 22.780000 | 90.000000 | 1013.000000 |  | 22.160000 | 0.440000 | 10000.000000 | 275.000000 | 0.33 | 0.230000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 13:00:00 | 45.000000 | 20.750000 | 25.210000 | 79.000000 | 1014.000000 |  | 24.630000 | 1.920000 | 10000.000000 | 89.000000 | 0.34 | 0.100000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 14:00:00 | 36.000000 | 21.080000 | 28.890000 | 70.000000 | 1015.000000 |  | 27.020000 | 4.700000 | 10000.000000 | 52.000000 | 1.26 | 0.440000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 15:00:00 | 28.000000 | 21.190000 | 31.400000 | 63.000000 | 1014.000000 |  | 28.940000 | 7.990000 | 10000.000000 | 50.000000 | 1.84 | 0.980000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 16:00:00 | 25.000000 | 20.800000 | 32.720000 | 57.000000 | 1013.000000 |  | 30.260000 | 10.580000 | 10000.000000 | 46.000000 | 2.21 | 1.500000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 17:00:00 | 26.000000 | 20.540000 | 33.700000 | 53.000000 | 1012.000000 |  | 31.260000 | 11.520000 | 10000.000000 | 44.000000 | 2.4 | 1.850000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 18:00:00 | 14.000000 | 19.910000 | 34.060000 | 49.000000 | 1010.000000 |  | 31.960000 | 10.440000 | 10000.000000 | 40.000000 | 2.41 | 1.810000 | 801 | Clouds | few clouds | 02d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 19:00:00 | 27.000000 | 19.520000 | 34.140000 | 47.000000 | 1009.000000 |  | 32.270000 | 7.790000 | 10000.000000 | 32.000000 | 2.31 | 1.680000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 20:00:00 | 18.000000 | 19.590000 | 33.840000 | 48.000000 | 1007.000000 |  | 31.970000 | 4.500000 | 10000.000000 | 34.000000 | 2.38 | 1.650000 | 801 | Clouds | few clouds | 02d | 20 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 21:00:00 | 18.000000 | 20.000000 | 33.420000 | 51.000000 | 1007.000000 |  | 31.350000 | 1.790000 | 10000.000000 | 26.000000 | 2.36 | 1.430000 | 801 | Clouds | few clouds | 02d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 22:00:00 | 28.000000 | 22.080000 | 32.510000 | 65.000000 | 1008.000000 |  | 29.340000 | 0.380000 | 10000.000000 | 24.000000 | 1.49 | 0.780000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23095010 | "AEROPUERTO PUERTO BERRIO [23095010]" | 6.465000 | -74.412222 | 150.000000 | Climática Principal | Convencional | Suspendida | 1975-04-15 00:00:00 | 2018-07-13 12:10:26 | Antioquia | Puerto Berrío | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 23:00:00 | 34.000000 | 21.840000 | 26.450000 | 79.000000 | 1009.000000 |  | 25.760000 | 0.000000 | 10000.000000 | 340.000000 | 1.02 | 0.760000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station23095010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23095010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23095010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23095010_OWM_Windspeed_20220111.png)
