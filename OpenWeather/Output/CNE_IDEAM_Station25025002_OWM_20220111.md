
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LOS ALAMOS - AUT [25025002] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025002_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.30405556,-74.27363889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.30405556&lon=-74.27363889)


| Parameter | Value |
|---|---|
| Code | 25025002 |
| Name | LOS ALAMOS - AUT [25025002] |
| Latitude, ° | 9.30405556 |
| Longitude, ° | -74.27363889 |
| Elevation, m | 25 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-05 00:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | San Sebastián De Buenavista |
| Stream | Manzanares |
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

### (CNE index 206) Open Weather values for station 25025002 - LOS ALAMOS - AUT [25025002]

JSON data from API OWM:

```
{'lat': 9.3041, 'lon': -74.2736, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813355, 'sunset': 1641855175, 'temp': 32.98, 'feels_like': 32.6, 'pressure': 1008, 'humidity': 34, 'dew_point': 15.04, 'uvi': 3.75, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 236, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.09, 'feels_like': 26.09, 'pressure': 1009, 'humidity': 60, 'dew_point': 17.72, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 235, 'wind_gust': 1.34, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 25.34, 'feels_like': 25.55, 'pressure': 1010, 'humidity': 62, 'dew_point': 17.54, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 37, 'wind_gust': 1.03, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.66, 'feels_like': 24.88, 'pressure': 1011, 'humidity': 65, 'dew_point': 17.64, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 351, 'wind_gust': 2.39, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 24.01, 'feels_like': 24.22, 'pressure': 1011, 'humidity': 67, 'dew_point': 17.51, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 330, 'wind_gust': 1.81, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 23.4, 'feels_like': 23.65, 'pressure': 1011, 'humidity': 71, 'dew_point': 17.85, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 332, 'wind_gust': 1.42, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 22.8, 'feels_like': 23.07, 'pressure': 1011, 'humidity': 74, 'dew_point': 17.93, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 335, 'wind_gust': 1.19, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 22.24, 'feels_like': 22.48, 'pressure': 1011, 'humidity': 75, 'dew_point': 17.6, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 3, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.83, 'feels_like': 22, 'pressure': 1010, 'humidity': 74, 'dew_point': 16.99, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 86, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.26, 'feels_like': 21.37, 'pressure': 1010, 'humidity': 74, 'dew_point': 16.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 101, 'wind_gust': 1.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.68, 'feels_like': 20.71, 'pressure': 1010, 'humidity': 73, 'dew_point': 15.67, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 105, 'wind_gust': 2.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.19, 'feels_like': 20.14, 'pressure': 1011, 'humidity': 72, 'dew_point': 14.99, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 94, 'wind_gust': 1.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.79, 'feels_like': 19.7, 'pressure': 1012, 'humidity': 72, 'dew_point': 14.6, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 87, 'wind_gust': 1.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 20.6, 'feels_like': 20.6, 'pressure': 1013, 'humidity': 72, 'dew_point': 15.38, 'uvi': 0.34, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 90, 'wind_gust': 2.48, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 23.63, 'feels_like': 23.69, 'pressure': 1014, 'humidity': 63, 'dew_point': 16.18, 'uvi': 1.67, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 102, 'wind_gust': 3.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 26.52, 'feels_like': 26.52, 'pressure': 1014, 'humidity': 56, 'dew_point': 17.03, 'uvi': 4.16, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 124, 'wind_gust': 3.23, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.91, 'feels_like': 29.43, 'pressure': 1014, 'humidity': 49, 'dew_point': 17.13, 'uvi': 7.17, 'clouds': 47, 'visibility': 10000, 'wind_speed': 2, 'wind_deg': 123, 'wind_gust': 2.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 30.88, 'feels_like': 31.05, 'pressure': 1013, 'humidity': 42, 'dew_point': 16.48, 'uvi': 9.38, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 128, 'wind_gust': 2.29, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 32.28, 'feels_like': 32.15, 'pressure': 1012, 'humidity': 37, 'dew_point': 15.74, 'uvi': 10.24, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 135, 'wind_gust': 2.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 33.17, 'feels_like': 33.04, 'pressure': 1010, 'humidity': 35, 'dew_point': 15.66, 'uvi': 9.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 147, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 33.45, 'feels_like': 33.07, 'pressure': 1009, 'humidity': 33, 'dew_point': 14.98, 'uvi': 6.61, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 194, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 32.98, 'feels_like': 32.6, 'pressure': 1008, 'humidity': 34, 'dew_point': 15.04, 'uvi': 3.75, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 236, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 32.17, 'feels_like': 32, 'pressure': 1008, 'humidity': 37, 'dew_point': 15.65, 'uvi': 1.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 248, 'wind_gust': 1.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.56, 'feels_like': 30.14, 'pressure': 1008, 'humidity': 48, 'dew_point': 17.4, 'uvi': 0.3, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 252, 'wind_gust': 3.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.79, 'feels_like': 27.34, 'pressure': 1008, 'humidity': 52, 'dew_point': 16.12, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.51, 'wind_deg': 253, 'wind_gust': 3.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 00:00:00 | 5.000000 | 17.720000 | 26.090000 | 60.000000 | 1009.000000 |  | 26.090000 | 0.000000 | 10000.000000 | 235.000000 | 1.34 | 1.240000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 17.540000 | 25.550000 | 62.000000 | 1010.000000 |  | 25.340000 | 0.000000 | 10000.000000 | 37.000000 | 1.03 | 0.660000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 02:00:00 | 6.000000 | 17.640000 | 24.880000 | 65.000000 | 1011.000000 |  | 24.660000 | 0.000000 | 10000.000000 | 351.000000 | 2.39 | 2.100000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 03:00:00 | 6.000000 | 17.510000 | 24.220000 | 67.000000 | 1011.000000 |  | 24.010000 | 0.000000 | 10000.000000 | 330.000000 | 1.81 | 1.730000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 04:00:00 | 7.000000 | 17.850000 | 23.650000 | 71.000000 | 1011.000000 |  | 23.400000 | 0.000000 | 10000.000000 | 332.000000 | 1.42 | 1.280000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 05:00:00 | 8.000000 | 17.930000 | 23.070000 | 74.000000 | 1011.000000 |  | 22.800000 | 0.000000 | 10000.000000 | 335.000000 | 1.19 | 0.880000 | 800 | Clear | clear sky | 01n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 17.600000 | 22.480000 | 75.000000 | 1011.000000 |  | 22.240000 | 0.000000 | 10000.000000 | 3.000000 | 1.07 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 16.990000 | 22.000000 | 74.000000 | 1010.000000 |  | 21.830000 | 0.000000 | 10000.000000 | 86.000000 | 1.6 | 1.160000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 16.440000 | 21.370000 | 74.000000 | 1010.000000 |  | 21.260000 | 0.000000 | 10000.000000 | 101.000000 | 1.89 | 1.530000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 09:00:00 | 78.000000 | 15.670000 | 20.710000 | 73.000000 | 1010.000000 |  | 20.680000 | 0.000000 | 10000.000000 | 105.000000 | 2.05 | 1.790000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 10:00:00 | 65.000000 | 14.990000 | 20.140000 | 72.000000 | 1011.000000 |  | 20.190000 | 0.000000 | 10000.000000 | 94.000000 | 1.93 | 1.790000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 11:00:00 | 55.000000 | 14.600000 | 19.700000 | 72.000000 | 1012.000000 |  | 19.790000 | 0.000000 | 10000.000000 | 87.000000 | 1.64 | 1.590000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 12:00:00 | 33.000000 | 15.380000 | 20.600000 | 72.000000 | 1013.000000 |  | 20.600000 | 0.340000 | 10000.000000 | 90.000000 | 2.48 | 1.870000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 13:00:00 | 49.000000 | 16.180000 | 23.690000 | 63.000000 | 1014.000000 |  | 23.630000 | 1.670000 | 10000.000000 | 102.000000 | 3.56 | 2.200000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 14:00:00 | 60.000000 | 17.030000 | 26.520000 | 56.000000 | 1014.000000 |  | 26.520000 | 4.160000 | 10000.000000 | 124.000000 | 3.23 | 2.080000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 15:00:00 | 47.000000 | 17.130000 | 29.430000 | 49.000000 | 1014.000000 |  | 28.910000 | 7.170000 | 10000.000000 | 123.000000 | 2.73 | 2.000000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 16:00:00 | 46.000000 | 16.480000 | 31.050000 | 42.000000 | 1013.000000 |  | 30.880000 | 9.380000 | 10000.000000 | 128.000000 | 2.29 | 1.810000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 17:00:00 | 54.000000 | 15.740000 | 32.150000 | 37.000000 | 1012.000000 |  | 32.280000 | 10.240000 | 10000.000000 | 135.000000 | 2.16 | 1.650000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 15.660000 | 33.040000 | 35.000000 | 1010.000000 |  | 33.170000 | 9.260000 | 10000.000000 | 147.000000 | 1.95 | 1.350000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 14.980000 | 33.070000 | 33.000000 | 1009.000000 |  | 33.450000 | 6.610000 | 10000.000000 | 194.000000 | 1.49 | 0.950000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 15.040000 | 32.600000 | 34.000000 | 1008.000000 |  | 32.980000 | 3.750000 | 10000.000000 | 236.000000 | 1.59 | 1.350000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 15.650000 | 32.000000 | 37.000000 | 1008.000000 |  | 32.170000 | 1.470000 | 10000.000000 | 248.000000 | 1.87 | 1.990000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 17.400000 | 30.140000 | 48.000000 | 1008.000000 |  | 29.560000 | 0.300000 | 10000.000000 | 252.000000 | 3.57 | 2.360000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025002 | "LOS ALAMOS - AUT [25025002]" | 9.304056 | -74.273639 | 25.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | San Sebastián De Buenavista | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Directos Bajo Magdalena entre El Banco y El Plato | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 16.120000 | 27.340000 | 52.000000 | 1008.000000 |  | 26.790000 | 0.000000 | 10000.000000 | 253.000000 | 3.09 | 2.510000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025002_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025002_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025002_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025002_OWM_Windspeed_20220111.png)
