
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SINCERIN  - AUT [29035000] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035000_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.14258333,-75.27827778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.14258333&lon=-75.27827778)


| Parameter | Value |
|---|---|
| Code | 29035000 |
| Name | SINCERIN  - AUT [29035000] |
| Latitude, ° | 10.14258333 |
| Longitude, ° | -75.27827778 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-04 19:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | Arjona |
| Stream | 0 |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Canal del Dique margen izquierda |

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

### (CNE index 223) Open Weather values for station 29035000 - SINCERIN  - AUT [29035000]

JSON data from API OWM:

```
{'lat': 10.1426, 'lon': -75.2783, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813679, 'sunset': 1641855334, 'temp': 29.97, 'feels_like': 29.65, 'pressure': 1009, 'humidity': 40, 'dew_point': 14.91, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.69, 'wind_deg': 258, 'wind_gust': 3.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1010, 'humidity': 74, 'dew_point': 20.98, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 317, 'wind_gust': 2.46, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1011, 'humidity': 76, 'dew_point': 21.41, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 311, 'wind_gust': 1.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1012, 'humidity': 76, 'dew_point': 21.41, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 48, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.97, 'feels_like': 25.51, 'pressure': 1012, 'humidity': 76, 'dew_point': 20.45, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 359, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.97, 'feels_like': 25.53, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.66, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 33, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.97, 'feels_like': 25.53, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.66, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 139, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.97, 'feels_like': 24.46, 'pressure': 1010, 'humidity': 78, 'dew_point': 19.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 145, 'wind_gust': 0.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.97, 'feels_like': 24.46, 'pressure': 1010, 'humidity': 78, 'dew_point': 19.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 116, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.97, 'feels_like': 24.46, 'pressure': 1010, 'humidity': 78, 'dew_point': 19.9, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 91, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.97, 'feels_like': 24.51, 'pressure': 1010, 'humidity': 80, 'dew_point': 20.31, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 90, 'wind_gust': 2.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.97, 'feels_like': 24.51, 'pressure': 1011, 'humidity': 80, 'dew_point': 20.31, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 101, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.97, 'feels_like': 23.33, 'pressure': 1011, 'humidity': 77, 'dew_point': 18.72, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 106, 'wind_gust': 3.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.97, 'feels_like': 23.12, 'pressure': 1012, 'humidity': 69, 'dew_point': 16.98, 'uvi': 0.27, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.68, 'wind_deg': 110, 'wind_gust': 8.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.97, 'feels_like': 25.06, 'pressure': 1013, 'humidity': 59, 'dew_point': 16.41, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.37, 'wind_deg': 109, 'wind_gust': 9.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.97, 'feels_like': 28.5, 'pressure': 1014, 'humidity': 51, 'dew_point': 16.9, 'uvi': 3.61, 'clouds': 98, 'visibility': 10000, 'wind_speed': 4.93, 'wind_deg': 110, 'wind_gust': 7.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.97, 'feels_like': 29.16, 'pressure': 1014, 'humidity': 46, 'dew_point': 16.19, 'uvi': 6.4, 'clouds': 98, 'visibility': 10000, 'wind_speed': 4.6, 'wind_deg': 111, 'wind_gust': 5.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.97, 'feels_like': 28.67, 'pressure': 1013, 'humidity': 41, 'dew_point': 14.4, 'uvi': 8.59, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.78, 'wind_deg': 120, 'wind_gust': 4.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.97, 'feels_like': 28.32, 'pressure': 1012, 'humidity': 37, 'dew_point': 12.82, 'uvi': 9.51, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 136, 'wind_gust': 2.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.97, 'feels_like': 29.14, 'pressure': 1011, 'humidity': 35, 'dew_point': 12.85, 'uvi': 8.71, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 181, 'wind_gust': 2.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.97, 'feels_like': 30.22, 'pressure': 1009, 'humidity': 35, 'dew_point': 13.73, 'uvi': 5.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 240, 'wind_gust': 2.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.97, 'feels_like': 29.65, 'pressure': 1009, 'humidity': 40, 'dew_point': 14.91, 'uvi': 3.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.69, 'wind_deg': 258, 'wind_gust': 3.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.97, 'feels_like': 29.87, 'pressure': 1008, 'humidity': 52, 'dew_point': 18.13, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.73, 'wind_deg': 282, 'wind_gust': 4.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.97, 'feels_like': 30.1, 'pressure': 1009, 'humidity': 66, 'dew_point': 21.03, 'uvi': 0.24, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.09, 'wind_deg': 309, 'wind_gust': 6.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.97, 'feels_like': 29.14, 'pressure': 1010, 'humidity': 74, 'dew_point': 21.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.35, 'wind_deg': 335, 'wind_gust': 6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 00:00:00 | 46.000000 | 20.980000 | 25.970000 | 74.000000 | 1010.000000 |  | 25.970000 | 0.000000 | 10000.000000 | 317.000000 | 2.46 | 1.430000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 01:00:00 | 52.000000 | 21.410000 | 25.970000 | 76.000000 | 1011.000000 |  | 25.970000 | 0.000000 | 10000.000000 | 311.000000 | 1.56 | 0.630000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 02:00:00 | 76.000000 | 21.410000 | 25.970000 | 76.000000 | 1012.000000 |  | 25.970000 | 0.000000 | 10000.000000 | 48.000000 | 1.15 | 0.200000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 03:00:00 | 84.000000 | 20.450000 | 25.510000 | 76.000000 | 1012.000000 |  | 24.970000 | 0.000000 | 10000.000000 | 359.000000 | 1.02 | 0.320000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 04:00:00 | 88.000000 | 20.660000 | 25.530000 | 77.000000 | 1011.000000 |  | 24.970000 | 0.000000 | 10000.000000 | 33.000000 | 0.91 | 0.200000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 05:00:00 | 90.000000 | 20.660000 | 25.530000 | 77.000000 | 1011.000000 |  | 24.970000 | 0.000000 | 10000.000000 | 139.000000 | 0.76 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 19.900000 | 24.460000 | 78.000000 | 1010.000000 |  | 23.970000 | 0.000000 | 10000.000000 | 145.000000 | 0.72 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.900000 | 24.460000 | 78.000000 | 1010.000000 |  | 23.970000 | 0.000000 | 10000.000000 | 116.000000 | 0.88 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 19.900000 | 24.460000 | 78.000000 | 1010.000000 |  | 23.970000 | 0.000000 | 10000.000000 | 91.000000 | 1.37 | 1.330000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 09:00:00 | 69.000000 | 20.310000 | 24.510000 | 80.000000 | 1010.000000 |  | 23.970000 | 0.000000 | 10000.000000 | 90.000000 | 2.15 | 2.140000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 10:00:00 | 55.000000 | 20.310000 | 24.510000 | 80.000000 | 1011.000000 |  | 23.970000 | 0.000000 | 10000.000000 | 101.000000 | 2.38 | 2.240000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 11:00:00 | 56.000000 | 18.720000 | 23.330000 | 77.000000 | 1011.000000 |  | 22.970000 | 0.000000 | 10000.000000 | 106.000000 | 3.18 | 2.420000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 12:00:00 | 95.000000 | 16.980000 | 23.120000 | 69.000000 | 1012.000000 |  | 22.970000 | 0.270000 | 10000.000000 | 110.000000 | 8.59 | 2.680000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.410000 | 25.060000 | 59.000000 | 1013.000000 |  | 24.970000 | 1.410000 | 10000.000000 | 109.000000 | 9.54 | 4.370000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 16.900000 | 28.500000 | 51.000000 | 1014.000000 |  | 27.970000 | 3.610000 | 10000.000000 | 110.000000 | 7.51 | 4.930000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 16.190000 | 29.160000 | 46.000000 | 1014.000000 |  | 28.970000 | 6.400000 | 10000.000000 | 111.000000 | 5.92 | 4.600000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 14.400000 | 28.670000 | 41.000000 | 1013.000000 |  | 28.970000 | 8.590000 | 10000.000000 | 120.000000 | 4.22 | 3.780000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 12.820000 | 28.320000 | 37.000000 | 1012.000000 |  | 28.970000 | 9.510000 | 10000.000000 | 136.000000 | 2.97 | 2.610000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 12.850000 | 29.140000 | 35.000000 | 1011.000000 |  | 29.970000 | 8.710000 | 10000.000000 | 181.000000 | 2.33 | 1.730000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.730000 | 30.220000 | 35.000000 | 1009.000000 |  | 30.970000 | 5.990000 | 10000.000000 | 240.000000 | 2.22 | 2.070000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 14.910000 | 29.650000 | 40.000000 | 1009.000000 |  | 29.970000 | 3.450000 | 10000.000000 | 258.000000 | 3.07 | 3.690000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 18.130000 | 29.870000 | 52.000000 | 1008.000000 |  | 28.970000 | 1.380000 | 10000.000000 | 282.000000 | 4.43 | 4.730000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 21.030000 | 30.100000 | 66.000000 | 1009.000000 |  | 27.970000 | 0.240000 | 10000.000000 | 309.000000 | 6.52 | 4.090000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035000 | "SINCERIN  - AUT [29035000]" | 10.142583 | -75.278278 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-04 19:00:00 | NaT | Bolívar | Arjona | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen izquierda | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 21.940000 | 29.140000 | 74.000000 | 1010.000000 |  | 26.970000 | 0.000000 | 10000.000000 | 335.000000 | 6 | 3.350000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035000_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035000_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035000_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035000_OWM_Windspeed_20220111.png)
