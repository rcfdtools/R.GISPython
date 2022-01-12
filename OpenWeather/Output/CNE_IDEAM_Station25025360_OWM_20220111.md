
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO LAS FLORES  - AUT [25025360] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025360_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.04633333,-73.97083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.04633333&lon=-73.97083333)


| Parameter | Value |
|---|---|
| Code | 25025360 |
| Name | AEROPUERTO LAS FLORES  - AUT [25025360] |
| Latitude, ° | 9.04633333 |
| Longitude, ° | -73.97083333 |
| Elevation, m | 34 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-04 19:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | El Banco |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Directos Bajo Magdalena entre El Banco y El Plato |

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

### (CNE index 199) Open Weather values for station 25025360 - AEROPUERTO LAS FLORES  - AUT [25025360]

JSON data from API OWM:

```
{'lat': 9.0463, 'lon': -73.9708, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813257, 'sunset': 1641855128, 'temp': 33.94, 'feels_like': 33.56, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.93, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 291, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.78, 'feels_like': 25.95, 'pressure': 1009, 'humidity': 59, 'dew_point': 17.17, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 173, 'wind_gust': 0.84, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 24.94, 'feels_like': 25.08, 'pressure': 1010, 'humidity': 61, 'dew_point': 16.9, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 153, 'wind_gust': 0.93, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.22, 'feels_like': 24.32, 'pressure': 1011, 'humidity': 62, 'dew_point': 16.48, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 94, 'wind_gust': 0.89, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 23.43, 'feels_like': 23.47, 'pressure': 1011, 'humidity': 63, 'dew_point': 15.99, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 343, 'wind_gust': 0.76, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 22.69, 'feels_like': 22.74, 'pressure': 1011, 'humidity': 66, 'dew_point': 16.02, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 293, 'wind_gust': 1, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 22.11, 'feels_like': 22.2, 'pressure': 1011, 'humidity': 70, 'dew_point': 16.39, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 227, 'wind_gust': 0.86, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 21.5, 'feels_like': 21.59, 'pressure': 1011, 'humidity': 72, 'dew_point': 16.24, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 167, 'wind_gust': 0.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.11, 'feels_like': 21.21, 'pressure': 1011, 'humidity': 74, 'dew_point': 16.3, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 83, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.65, 'feels_like': 20.76, 'pressure': 1010, 'humidity': 76, 'dew_point': 16.27, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 86, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.28, 'feels_like': 20.37, 'pressure': 1010, 'humidity': 77, 'dew_point': 16.12, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 124, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.05, 'feels_like': 20.17, 'pressure': 1011, 'humidity': 79, 'dew_point': 16.3, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 130, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.88, 'feels_like': 20.04, 'pressure': 1012, 'humidity': 81, 'dew_point': 16.53, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 100, 'wind_gust': 0.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.03, 'feels_like': 21.2, 'pressure': 1013, 'humidity': 77, 'dew_point': 16.85, 'uvi': 0.38, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 80, 'wind_gust': 0.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 24.37, 'feels_like': 24.51, 'pressure': 1014, 'humidity': 63, 'dew_point': 16.88, 'uvi': 1.75, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 84, 'wind_gust': 1.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 27.73, 'feels_like': 28.24, 'pressure': 1014, 'humidity': 51, 'dew_point': 16.68, 'uvi': 4.3, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 104, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 30.51, 'feels_like': 30.71, 'pressure': 1014, 'humidity': 43, 'dew_point': 16.52, 'uvi': 7.33, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 92, 'wind_gust': 1.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 32.79, 'feels_like': 32.69, 'pressure': 1013, 'humidity': 36, 'dew_point': 15.76, 'uvi': 9.6, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 356, 'wind_gust': 1.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 34.29, 'feels_like': 34.06, 'pressure': 1011, 'humidity': 32, 'dew_point': 15.23, 'uvi': 10.42, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 289, 'wind_gust': 1.64, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 34.87, 'feels_like': 34.7, 'pressure': 1010, 'humidity': 31, 'dew_point': 15.24, 'uvi': 9.37, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 281, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.6, 'feels_like': 34.11, 'pressure': 1008, 'humidity': 30, 'dew_point': 14.5, 'uvi': 6.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 289, 'wind_gust': 2.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 33.94, 'feels_like': 33.56, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.93, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 291, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 32.77, 'feels_like': 32.66, 'pressure': 1007, 'humidity': 36, 'dew_point': 15.75, 'uvi': 1.43, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 294, 'wind_gust': 2.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.22, 'feels_like': 30.61, 'pressure': 1008, 'humidity': 45, 'dew_point': 16.98, 'uvi': 0.28, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 289, 'wind_gust': 5.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.6, 'feels_like': 26.6, 'pressure': 1008, 'humidity': 54, 'dew_point': 16.53, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 261, 'wind_gust': 1.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 00:00:00 | 7.000000 | 17.170000 | 25.950000 | 59.000000 | 1009.000000 |  | 25.780000 | 0.000000 | 10000.000000 | 173.000000 | 0.84 | 0.580000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 01:00:00 | 7.000000 | 16.900000 | 25.080000 | 61.000000 | 1010.000000 |  | 24.940000 | 0.000000 | 10000.000000 | 153.000000 | 0.93 | 0.790000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 02:00:00 | 7.000000 | 16.480000 | 24.320000 | 62.000000 | 1011.000000 |  | 24.220000 | 0.000000 | 10000.000000 | 94.000000 | 0.89 | 0.650000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 03:00:00 | 8.000000 | 15.990000 | 23.470000 | 63.000000 | 1011.000000 |  | 23.430000 | 0.000000 | 10000.000000 | 343.000000 | 0.76 | 0.630000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 04:00:00 | 7.000000 | 16.020000 | 22.740000 | 66.000000 | 1011.000000 |  | 22.690000 | 0.000000 | 10000.000000 | 293.000000 | 1 | 0.720000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 05:00:00 | 7.000000 | 16.390000 | 22.200000 | 70.000000 | 1011.000000 |  | 22.110000 | 0.000000 | 10000.000000 | 227.000000 | 0.86 | 0.420000 | 800 | Clear | clear sky | 01n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 06:00:00 | 80.000000 | 16.240000 | 21.590000 | 72.000000 | 1011.000000 |  | 21.500000 | 0.000000 | 10000.000000 | 167.000000 | 0.64 | 0.090000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 16.300000 | 21.210000 | 74.000000 | 1011.000000 |  | 21.110000 | 0.000000 | 10000.000000 | 83.000000 | 0.66 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 16.270000 | 20.760000 | 76.000000 | 1010.000000 |  | 20.650000 | 0.000000 | 10000.000000 | 86.000000 | 0.76 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 09:00:00 | 84.000000 | 16.120000 | 20.370000 | 77.000000 | 1010.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 124.000000 | 0.74 | 0.640000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 10:00:00 | 71.000000 | 16.300000 | 20.170000 | 79.000000 | 1011.000000 |  | 20.050000 | 0.000000 | 10000.000000 | 130.000000 | 0.66 | 0.530000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 16.530000 | 20.040000 | 81.000000 | 1012.000000 |  | 19.880000 | 0.000000 | 10000.000000 | 100.000000 | 0.51 | 0.450000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 12:00:00 | 35.000000 | 16.850000 | 21.200000 | 77.000000 | 1013.000000 |  | 21.030000 | 0.380000 | 10000.000000 | 80.000000 | 0.71 | 0.660000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 13:00:00 | 35.000000 | 16.880000 | 24.510000 | 63.000000 | 1014.000000 |  | 24.370000 | 1.750000 | 10000.000000 | 84.000000 | 1.57 | 0.950000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 14:00:00 | 38.000000 | 16.680000 | 28.240000 | 51.000000 | 1014.000000 |  | 27.730000 | 4.300000 | 10000.000000 | 104.000000 | 1.43 | 0.590000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 15:00:00 | 32.000000 | 16.520000 | 30.710000 | 43.000000 | 1014.000000 |  | 30.510000 | 7.330000 | 10000.000000 | 92.000000 | 1.37 | 0.310000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 16:00:00 | 29.000000 | 15.760000 | 32.690000 | 36.000000 | 1013.000000 |  | 32.790000 | 9.600000 | 10000.000000 | 356.000000 | 1.37 | 0.270000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 17:00:00 | 36.000000 | 15.230000 | 34.060000 | 32.000000 | 1011.000000 |  | 34.290000 | 10.420000 | 10000.000000 | 289.000000 | 1.64 | 0.320000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 18:00:00 | 95.000000 | 15.240000 | 34.700000 | 31.000000 | 1010.000000 |  | 34.870000 | 9.370000 | 10000.000000 | 281.000000 | 1.81 | 0.890000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 14.500000 | 34.110000 | 30.000000 | 1008.000000 |  | 34.600000 | 6.600000 | 10000.000000 | 289.000000 | 2.08 | 1.710000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 14.930000 | 33.560000 | 32.000000 | 1007.000000 |  | 33.940000 | 3.700000 | 10000.000000 | 291.000000 | 2.12 | 2.450000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 15.750000 | 32.660000 | 36.000000 | 1007.000000 |  | 32.770000 | 1.430000 | 10000.000000 | 294.000000 | 2.68 | 2.860000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 22:00:00 | 86.000000 | 16.980000 | 30.610000 | 45.000000 | 1008.000000 |  | 30.220000 | 0.280000 | 10000.000000 | 289.000000 | 5.25 | 2.230000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025360 | "AEROPUERTO LAS FLORES  - AUT [25025360]" | 9.046333 | -73.970833 | 34.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Magdalena | El Banco | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 16.530000 | 26.600000 | 54.000000 | 1008.000000 |  | 26.600000 | 0.000000 | 10000.000000 | 261.000000 | 1.91 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025360_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025360_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025360_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025360_OWM_Windspeed_20220111.png)
