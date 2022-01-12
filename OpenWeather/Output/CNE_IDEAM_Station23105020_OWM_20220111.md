
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AMPARO EL [23105020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23105020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.73333333,-74.4) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.73333333&lon=-74.4)


| Parameter | Value |
|---|---|
| Code | 23105020 |
| Name | AMPARO EL [23105020] |
| Latitude, ° | 6.73333333 |
| Longitude, ° | -74.4 |
| Elevation, m | 150 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1984-09-15 00:00:00 |
| Suspension date | 1992-08-15 00:00:00 |
| State | Antioquia |
| County | Yondó (Casabe) |
| Stream | Regla |
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

### (CNE index 977) Open Weather values for station 23105020 - AMPARO EL [23105020]

JSON data from API OWM:

```
{'lat': 6.7333, 'lon': -74.4, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813133, 'sunset': 1641855458, 'temp': 31.54, 'feels_like': 33.32, 'pressure': 1008, 'humidity': 49, 'dew_point': 19.53, 'uvi': 4.05, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 26, 'wind_gust': 2.34, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.01, 'feels_like': 24.76, 'pressure': 1010, 'humidity': 88, 'dew_point': 21.9, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 300, 'wind_gust': 1.08, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 23.53, 'feels_like': 24.26, 'pressure': 1011, 'humidity': 89, 'dew_point': 21.61, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 295, 'wind_gust': 1.2, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 23.14, 'feels_like': 23.83, 'pressure': 1012, 'humidity': 89, 'dew_point': 21.23, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 281, 'wind_gust': 1.21, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 22.79, 'feels_like': 23.47, 'pressure': 1012, 'humidity': 90, 'dew_point': 21.06, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 285, 'wind_gust': 1.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 22.49, 'feels_like': 23.14, 'pressure': 1012, 'humidity': 90, 'dew_point': 20.77, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 284, 'wind_gust': 1.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 22.31, 'feels_like': 22.95, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.59, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 281, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.04, 'feels_like': 22.65, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.32, 'uvi': 0, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 274, 'wind_gust': 1.02, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 21.78, 'feels_like': 22.39, 'pressure': 1010, 'humidity': 91, 'dew_point': 20.25, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 271, 'wind_gust': 0.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 21.54, 'feels_like': 22.15, 'pressure': 1010, 'humidity': 92, 'dew_point': 20.18, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 289, 'wind_gust': 0.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 21.29, 'feels_like': 21.88, 'pressure': 1010, 'humidity': 92, 'dew_point': 19.94, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 306, 'wind_gust': 0.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 21.09, 'feels_like': 21.68, 'pressure': 1011, 'humidity': 93, 'dew_point': 19.91, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 305, 'wind_gust': 0.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 20.89, 'feels_like': 21.49, 'pressure': 1012, 'humidity': 94, 'dew_point': 19.89, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 306, 'wind_gust': 0.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 21.87, 'feels_like': 22.46, 'pressure': 1013, 'humidity': 90, 'dew_point': 20.16, 'uvi': 0.35, 'clouds': 6, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 306, 'wind_gust': 0.81, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 24.51, 'feels_like': 25.08, 'pressure': 1014, 'humidity': 79, 'dew_point': 20.63, 'uvi': 1.75, 'clouds': 10, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 359, 'wind_gust': 1.08, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641823200, 'temp': 26.76, 'feels_like': 28.6, 'pressure': 1015, 'humidity': 72, 'dew_point': 21.29, 'uvi': 4.3, 'clouds': 11, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 36, 'wind_gust': 1.66, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 27.9, 'feels_like': 30.35, 'pressure': 1014, 'humidity': 69, 'dew_point': 21.69, 'uvi': 7.32, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 51, 'wind_gust': 2.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641830400, 'temp': 28.78, 'feels_like': 31.58, 'pressure': 1013, 'humidity': 66, 'dew_point': 21.8, 'uvi': 10.21, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 36, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641834000, 'temp': 30.22, 'feels_like': 32.65, 'pressure': 1012, 'humidity': 57, 'dew_point': 20.76, 'uvi': 11.14, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 21, 'wind_gust': 2.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641837600, 'temp': 31.19, 'feels_like': 33.36, 'pressure': 1010, 'humidity': 52, 'dew_point': 20.17, 'uvi': 10.09, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 24, 'wind_gust': 2.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641841200, 'temp': 31.66, 'feels_like': 33.53, 'pressure': 1009, 'humidity': 49, 'dew_point': 19.64, 'uvi': 7.03, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 31, 'wind_gust': 2.12, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 31.54, 'feels_like': 33.32, 'pressure': 1008, 'humidity': 49, 'dew_point': 19.53, 'uvi': 4.05, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 26, 'wind_gust': 2.34, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641848400, 'temp': 30.94, 'feels_like': 32.71, 'pressure': 1007, 'humidity': 51, 'dew_point': 19.63, 'uvi': 1.61, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 18, 'wind_gust': 2.34, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641852000, 'temp': 28.79, 'feels_like': 31.93, 'pressure': 1008, 'humidity': 68, 'dew_point': 22.29, 'uvi': 0.34, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 23, 'wind_gust': 1.21, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641855600, 'temp': 25.47, 'feels_like': 26.14, 'pressure': 1009, 'humidity': 79, 'dew_point': 21.56, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 328, 'wind_gust': 1.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 00:00:00 | 7.000000 | 21.900000 | 24.760000 | 88.000000 | 1010.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 300.000000 | 1.08 | 1.140000 | 800 | Clear | clear sky | 01n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 01:00:00 | 13.000000 | 21.610000 | 24.260000 | 89.000000 | 1011.000000 |  | 23.530000 | 0.000000 | 10000.000000 | 295.000000 | 1.2 | 1.330000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 02:00:00 | 16.000000 | 21.230000 | 23.830000 | 89.000000 | 1012.000000 |  | 23.140000 | 0.000000 | 10000.000000 | 281.000000 | 1.21 | 1.330000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 03:00:00 | 27.000000 | 21.060000 | 23.470000 | 90.000000 | 1012.000000 |  | 22.790000 | 0.000000 | 10000.000000 | 285.000000 | 1.21 | 1.250000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 04:00:00 | 43.000000 | 20.770000 | 23.140000 | 90.000000 | 1012.000000 |  | 22.490000 | 0.000000 | 10000.000000 | 284.000000 | 1.12 | 1.200000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 05:00:00 | 54.000000 | 20.590000 | 22.950000 | 90.000000 | 1011.000000 |  | 22.310000 | 0.000000 | 10000.000000 | 281.000000 | 1.02 | 1.090000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 06:00:00 | 15.000000 | 20.320000 | 22.650000 | 90.000000 | 1011.000000 |  | 22.040000 | 0.000000 | 10000.000000 | 274.000000 | 1.02 | 1.070000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 07:00:00 | 31.000000 | 20.250000 | 22.390000 | 91.000000 | 1010.000000 |  | 21.780000 | 0.000000 | 10000.000000 | 271.000000 | 0.99 | 1.010000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 08:00:00 | 28.000000 | 20.180000 | 22.150000 | 92.000000 | 1010.000000 |  | 21.540000 | 0.000000 | 10000.000000 | 289.000000 | 0.88 | 0.840000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 09:00:00 | 31.000000 | 19.940000 | 21.880000 | 92.000000 | 1010.000000 |  | 21.290000 | 0.000000 | 10000.000000 | 306.000000 | 0.88 | 0.750000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 10:00:00 | 44.000000 | 19.910000 | 21.680000 | 93.000000 | 1011.000000 |  | 21.090000 | 0.000000 | 10000.000000 | 305.000000 | 0.91 | 0.830000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 11:00:00 | 43.000000 | 19.890000 | 21.490000 | 94.000000 | 1012.000000 |  | 20.890000 | 0.000000 | 10000.000000 | 306.000000 | 0.75 | 0.700000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 12:00:00 | 6.000000 | 20.160000 | 22.460000 | 90.000000 | 1013.000000 |  | 21.870000 | 0.350000 | 10000.000000 | 306.000000 | 0.81 | 0.440000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 13:00:00 | 10.000000 | 20.630000 | 25.080000 | 79.000000 | 1014.000000 |  | 24.510000 | 1.750000 | 10000.000000 | 359.000000 | 1.08 | 0.300000 | 800 | Clear | clear sky | 01d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 14:00:00 | 11.000000 | 21.290000 | 28.600000 | 72.000000 | 1015.000000 |  | 26.760000 | 4.300000 | 10000.000000 | 36.000000 | 1.66 | 0.580000 | 801 | Clouds | few clouds | 02d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 15:00:00 | 11.000000 | 21.690000 | 30.350000 | 69.000000 | 1014.000000 | 0.37 | 27.900000 | 7.320000 | 10000.000000 | 51.000000 | 2.02 | 1.220000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 16:00:00 | 12.000000 | 21.800000 | 31.580000 | 66.000000 | 1013.000000 | 0.31 | 28.780000 | 10.210000 | 10000.000000 | 36.000000 | 2.18 | 1.550000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 17:00:00 | 13.000000 | 20.760000 | 32.650000 | 57.000000 | 1012.000000 | 0.3 | 30.220000 | 11.140000 | 10000.000000 | 21.000000 | 2.22 | 1.650000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 18:00:00 | 7.000000 | 20.170000 | 33.360000 | 52.000000 | 1010.000000 | 0.14 | 31.190000 | 10.090000 | 10000.000000 | 24.000000 | 2.22 | 1.550000 | 500 | Rain | light rain | 10d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 19:00:00 | 12.000000 | 19.640000 | 33.530000 | 49.000000 | 1009.000000 |  | 31.660000 | 7.030000 | 10000.000000 | 31.000000 | 2.12 | 1.410000 | 801 | Clouds | few clouds | 02d | 19 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 20:00:00 | 10.000000 | 19.530000 | 33.320000 | 49.000000 | 1008.000000 |  | 31.540000 | 4.050000 | 10000.000000 | 26.000000 | 2.34 | 1.380000 | 800 | Clear | clear sky | 01d | 20 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 21:00:00 | 13.000000 | 19.630000 | 32.710000 | 51.000000 | 1007.000000 |  | 30.940000 | 1.610000 | 10000.000000 | 18.000000 | 2.34 | 1.120000 | 801 | Clouds | few clouds | 02d | 21 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 22:00:00 | 20.000000 | 22.290000 | 31.930000 | 68.000000 | 1008.000000 |  | 28.790000 | 0.340000 | 10000.000000 | 23.000000 | 1.21 | 0.750000 | 801 | Clouds | few clouds | 02d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105020 | "AMPARO EL [23105020]" | 6.733333 | -74.400000 | 150.000000 | Climática Principal | Convencional | Suspendida | 1984-09-15 00:00:00 | 1992-08-15 00:00:00 | Antioquia | Yondó (Casabe) | Regla | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 23:00:00 | 29.000000 | 21.560000 | 26.140000 | 79.000000 | 1009.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 328.000000 | 1.3 | 1.040000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station23105020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23105020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23105020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105020_OWM_Windspeed_20220111.png)
