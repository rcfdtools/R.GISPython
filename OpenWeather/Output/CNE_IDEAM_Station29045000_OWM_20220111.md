
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SABANALARGA - AUT [29045000] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29045000_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.63672222,-74.91888889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.63672222&lon=-74.91888889)


| Parameter | Value |
|---|---|
| Code | 29045000 |
| Name | SABANALARGA - AUT [29045000] |
| Latitude, ° | 10.63672222 |
| Longitude, ° | -74.91888889 |
| Elevation, m | 100 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-05 00:00:00 |
| Suspension date | NaT |
| State | Atlantico |
| County | Sabanalarga (Atlántico) |
| Stream | Magdalena |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Canal del Dique margen derecho |

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

### (CNE index 238) Open Weather values for station 29045000 - SABANALARGA - AUT [29045000]

JSON data from API OWM:

```
{'lat': 10.6367, 'lon': -74.9189, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813642, 'sunset': 1641855198, 'temp': 28.47, 'feels_like': 28.01, 'pressure': 1008, 'humidity': 39, 'dew_point': 13.18, 'uvi': 3.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.96, 'wind_deg': 337, 'wind_gust': 3.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.47, 'feels_like': 25.98, 'pressure': 1010, 'humidity': 73, 'dew_point': 20.28, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 3.2, 'wind_deg': 360, 'wind_gust': 6.51, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 25.47, 'feels_like': 26.03, 'pressure': 1011, 'humidity': 75, 'dew_point': 20.71, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 2, 'wind_gust': 4.63, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 25.47, 'feels_like': 26.06, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.93, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 8, 'wind_gust': 5.19, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 25.47, 'feels_like': 26.08, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.14, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 360, 'wind_gust': 5.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.47, 'feels_like': 26.08, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.14, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 354, 'wind_gust': 4.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 26.47, 'feels_like': 26.47, 'pressure': 1011, 'humidity': 77, 'dew_point': 22.11, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 9, 'wind_gust': 3.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.47, 'feels_like': 26.11, 'pressure': 1010, 'humidity': 78, 'dew_point': 21.35, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 36, 'wind_gust': 3.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 25.47, 'feels_like': 26.16, 'pressure': 1010, 'humidity': 80, 'dew_point': 21.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 40, 'wind_gust': 2.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.47, 'feels_like': 25.11, 'pressure': 1010, 'humidity': 82, 'dew_point': 21.2, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 32, 'wind_gust': 2.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.47, 'feels_like': 25.17, 'pressure': 1010, 'humidity': 84, 'dew_point': 21.59, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 52, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.47, 'feels_like': 25.24, 'pressure': 1011, 'humidity': 87, 'dew_point': 22.16, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 67, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 24.47, 'feels_like': 25.27, 'pressure': 1011, 'humidity': 88, 'dew_point': 22.35, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 65, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.47, 'feels_like': 25.14, 'pressure': 1012, 'humidity': 83, 'dew_point': 21.39, 'uvi': 0.26, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 38, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.47, 'feels_like': 25.85, 'pressure': 1014, 'humidity': 68, 'dew_point': 19.13, 'uvi': 1.5, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 26, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.47, 'feels_like': 28.27, 'pressure': 1014, 'humidity': 55, 'dew_point': 17.63, 'uvi': 3.82, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 360, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.47, 'feels_like': 28.6, 'pressure': 1014, 'humidity': 46, 'dew_point': 15.74, 'uvi': 6.71, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 228, 'wind_gust': 1.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.47, 'feels_like': 28.01, 'pressure': 1013, 'humidity': 39, 'dew_point': 13.18, 'uvi': 8.52, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 230, 'wind_gust': 2.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.47, 'feels_like': 28.64, 'pressure': 1012, 'humidity': 35, 'dew_point': 12.42, 'uvi': 9.37, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 276, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 28.47, 'feels_like': 27.61, 'pressure': 1010, 'humidity': 33, 'dew_point': 10.65, 'uvi': 8.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 299, 'wind_gust': 2.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 28.47, 'feels_like': 27.67, 'pressure': 1009, 'humidity': 34, 'dew_point': 11.1, 'uvi': 6.12, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.76, 'wind_deg': 320, 'wind_gust': 3.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 28.47, 'feels_like': 28.01, 'pressure': 1008, 'humidity': 39, 'dew_point': 13.18, 'uvi': 3.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.96, 'wind_deg': 337, 'wind_gust': 3.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 27.47, 'feels_like': 27.81, 'pressure': 1008, 'humidity': 49, 'dew_point': 15.81, 'uvi': 1.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.61, 'wind_deg': 352, 'wind_gust': 5.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 26.47, 'feels_like': 26.47, 'pressure': 1009, 'humidity': 59, 'dew_point': 17.81, 'uvi': 0.23, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.62, 'wind_deg': 6, 'wind_gust': 7.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 25.47, 'feels_like': 25.93, 'pressure': 1010, 'humidity': 71, 'dew_point': 19.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.18, 'wind_deg': 9, 'wind_gust': 9.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 00:00:00 | 4.000000 | 20.280000 | 25.980000 | 73.000000 | 1010.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 360.000000 | 6.51 | 3.200000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 20.710000 | 26.030000 | 75.000000 | 1011.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 2.000000 | 4.63 | 2.250000 | 800 | Clear | clear sky | 01n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 02:00:00 | 35.000000 | 20.930000 | 26.060000 | 76.000000 | 1011.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 8.000000 | 5.19 | 2.570000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 03:00:00 | 57.000000 | 21.140000 | 26.080000 | 77.000000 | 1011.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 360.000000 | 5.07 | 2.490000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 04:00:00 | 68.000000 | 21.140000 | 26.080000 | 77.000000 | 1011.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 354.000000 | 4.06 | 2.220000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 05:00:00 | 74.000000 | 22.110000 | 26.470000 | 77.000000 | 1011.000000 |  | 26.470000 | 0.000000 | 10000.000000 | 9.000000 | 3.01 | 1.730000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 21.350000 | 26.110000 | 78.000000 | 1010.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 36.000000 | 3.03 | 1.620000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 21.770000 | 26.160000 | 80.000000 | 1010.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 40.000000 | 2.82 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 21.200000 | 25.110000 | 82.000000 | 1010.000000 |  | 24.470000 | 0.000000 | 10000.000000 | 32.000000 | 2.24 | 1.460000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 09:00:00 | 94.000000 | 21.590000 | 25.170000 | 84.000000 | 1010.000000 |  | 24.470000 | 0.000000 | 10000.000000 | 52.000000 | 1.76 | 1.230000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 10:00:00 | 92.000000 | 22.160000 | 25.240000 | 87.000000 | 1011.000000 |  | 24.470000 | 0.000000 | 10000.000000 | 67.000000 | 1.23 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 11:00:00 | 88.000000 | 22.350000 | 25.270000 | 88.000000 | 1011.000000 |  | 24.470000 | 0.000000 | 10000.000000 | 65.000000 | 1 | 0.470000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 12:00:00 | 68.000000 | 21.390000 | 25.140000 | 83.000000 | 1012.000000 |  | 24.470000 | 0.260000 | 10000.000000 | 38.000000 | 1.15 | 0.670000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 13:00:00 | 78.000000 | 19.130000 | 25.850000 | 68.000000 | 1014.000000 |  | 25.470000 | 1.500000 | 10000.000000 | 26.000000 | 1.63 | 0.630000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 14:00:00 | 81.000000 | 17.630000 | 28.270000 | 55.000000 | 1014.000000 |  | 27.470000 | 3.820000 | 10000.000000 | 360.000000 | 1.4 | 0.620000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 15:00:00 | 87.000000 | 15.740000 | 28.600000 | 46.000000 | 1014.000000 |  | 28.470000 | 6.710000 | 10000.000000 | 228.000000 | 1.99 | 0.330000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 16:00:00 | 89.000000 | 13.180000 | 28.010000 | 39.000000 | 1013.000000 |  | 28.470000 | 8.520000 | 10000.000000 | 230.000000 | 2.38 | 0.730000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 17:00:00 | 91.000000 | 12.420000 | 28.640000 | 35.000000 | 1012.000000 |  | 29.470000 | 9.370000 | 10000.000000 | 276.000000 | 2.3 | 1.460000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 10.650000 | 27.610000 | 33.000000 | 1010.000000 |  | 28.470000 | 8.520000 | 10000.000000 | 299.000000 | 2.6 | 2.290000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 11.100000 | 27.670000 | 34.000000 | 1009.000000 |  | 28.470000 | 6.120000 | 10000.000000 | 320.000000 | 3.28 | 3.760000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 13.180000 | 28.010000 | 39.000000 | 1008.000000 |  | 28.470000 | 3.480000 | 10000.000000 | 337.000000 | 3.72 | 4.960000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 15.810000 | 27.810000 | 49.000000 | 1008.000000 |  | 27.470000 | 1.370000 | 10000.000000 | 352.000000 | 5.33 | 5.610000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 17.810000 | 26.470000 | 59.000000 | 1009.000000 |  | 26.470000 | 0.230000 | 10000.000000 | 6.000000 | 7.04 | 5.620000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29045000 | "SABANALARGA - AUT [29045000]" | 10.636722 | -74.918889 | 100.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Atlantico | Sabanalarga (Atlántico) | Magdalena | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 19.830000 | 25.930000 | 71.000000 | 1010.000000 |  | 25.470000 | 0.000000 | 10000.000000 | 9.000000 | 9.6 | 5.180000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29045000_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29045000_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29045000_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045000_OWM_Windspeed_20220111.png)
