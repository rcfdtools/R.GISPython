
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PRIMATES [13095020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13095020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.53013889,-75.35136111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.53013889&lon=-75.35136111)


| Parameter | Value |
|---|---|
| Code | 13095020 |
| Name | PRIMATES [13095020] |
| Latitude, ° | 9.53013889 |
| Longitude, ° | -75.35136111 |
| Elevation, m | 200 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1984-12-15 00:00:00 |
| Suspension date | NaT |
| State | Sucre |
| County | Colosó |
| Stream | Ay Pechelin |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Litoral |
| SZH - Hydrographic subzone | Directos Caribe Golfo de Morrosquillo |

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

### (CNE index 2703) Open Weather values for station 13095020 - PRIMATES [13095020]

JSON data from API OWM:

```
{'lat': 9.5301, 'lon': -75.3514, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813636, 'sunset': 1641855412, 'temp': 29.47, 'feels_like': 29.42, 'pressure': 1009, 'humidity': 43, 'dew_point': 15.59, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 273, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 23.36, 'feels_like': 23.97, 'pressure': 1010, 'humidity': 85, 'dew_point': 20.7, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 322, 'wind_gust': 4.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 22.94, 'feels_like': 23.54, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.04, 'wind_deg': 337, 'wind_gust': 5.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 22.8, 'feels_like': 23.36, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.15, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 340, 'wind_gust': 3.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.72, 'feels_like': 23.19, 'pressure': 1012, 'humidity': 82, 'dew_point': 19.49, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 336, 'wind_gust': 2.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.71, 'feels_like': 23.1, 'pressure': 1011, 'humidity': 79, 'dew_point': 18.88, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 335, 'wind_gust': 1.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.62, 'feels_like': 22.95, 'pressure': 1011, 'humidity': 77, 'dew_point': 18.38, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 331, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.44, 'feels_like': 22.7, 'pressure': 1011, 'humidity': 75, 'dew_point': 17.79, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 20, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.31, 'feels_like': 22.55, 'pressure': 1010, 'humidity': 75, 'dew_point': 17.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 132, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.98, 'feels_like': 22.22, 'pressure': 1010, 'humidity': 76, 'dew_point': 17.56, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 89, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.63, 'feels_like': 21.89, 'pressure': 1010, 'humidity': 78, 'dew_point': 17.63, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 97, 'wind_gust': 1.55, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.27, 'feels_like': 21.54, 'pressure': 1011, 'humidity': 80, 'dew_point': 17.68, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 89, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.97, 'feels_like': 21.21, 'pressure': 1011, 'humidity': 80, 'dew_point': 17.39, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 91, 'wind_gust': 2.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.44, 'feels_like': 21.62, 'pressure': 1012, 'humidity': 76, 'dew_point': 17.04, 'uvi': 0.28, 'clouds': 10, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 98, 'wind_gust': 3.15, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 23.65, 'feels_like': 23.74, 'pressure': 1013, 'humidity': 64, 'dew_point': 16.44, 'uvi': 1.48, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 97, 'wind_gust': 3.84, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 25.82, 'feels_like': 25.95, 'pressure': 1014, 'humidity': 57, 'dew_point': 16.66, 'uvi': 3.78, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.9, 'wind_deg': 105, 'wind_gust': 4.15, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 27.56, 'feels_like': 28.21, 'pressure': 1014, 'humidity': 53, 'dew_point': 17.13, 'uvi': 6.69, 'clouds': 41, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 108, 'wind_gust': 4.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 28.91, 'feels_like': 29.31, 'pressure': 1013, 'humidity': 48, 'dew_point': 16.8, 'uvi': 8.76, 'clouds': 53, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 114, 'wind_gust': 3.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.71, 'feels_like': 29.82, 'pressure': 1012, 'humidity': 44, 'dew_point': 16.16, 'uvi': 9.7, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.63, 'wind_deg': 120, 'wind_gust': 2.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.24, 'feels_like': 29.97, 'pressure': 1011, 'humidity': 40, 'dew_point': 15.15, 'uvi': 8.88, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 127, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30, 'feels_like': 29.69, 'pressure': 1010, 'humidity': 40, 'dew_point': 14.94, 'uvi': 5.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 204, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.47, 'feels_like': 29.42, 'pressure': 1009, 'humidity': 43, 'dew_point': 15.59, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 273, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.27, 'feels_like': 28.76, 'pressure': 1009, 'humidity': 50, 'dew_point': 16.86, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.73, 'wind_deg': 312, 'wind_gust': 2.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 26.23, 'feels_like': 26.23, 'pressure': 1009, 'humidity': 64, 'dew_point': 18.88, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.85, 'wind_deg': 322, 'wind_gust': 4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 24.05, 'feels_like': 24.44, 'pressure': 1010, 'humidity': 74, 'dew_point': 19.13, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 323, 'wind_gust': 3.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 00:00:00 | 97.000000 | 20.700000 | 23.970000 | 85.000000 | 1010.000000 |  | 23.360000 | 0.000000 | 10000.000000 | 322.000000 | 4.83 | 3.170000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 20.470000 | 23.540000 | 86.000000 | 1011.000000 |  | 22.940000 | 0.000000 | 10000.000000 | 337.000000 | 5.3 | 3.040000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 20.150000 | 23.360000 | 85.000000 | 1012.000000 |  | 22.800000 | 0.000000 | 10000.000000 | 340.000000 | 3.89 | 2.390000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 19.490000 | 23.190000 | 82.000000 | 1012.000000 |  | 22.720000 | 0.000000 | 10000.000000 | 336.000000 | 2.64 | 1.960000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 18.880000 | 23.100000 | 79.000000 | 1011.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 335.000000 | 1.91 | 1.600000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 18.380000 | 22.950000 | 77.000000 | 1011.000000 |  | 22.620000 | 0.000000 | 10000.000000 | 331.000000 | 1.22 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 17.790000 | 22.700000 | 75.000000 | 1011.000000 |  | 22.440000 | 0.000000 | 10000.000000 | 20.000000 | 0.77 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 17.670000 | 22.550000 | 75.000000 | 1010.000000 |  | 22.310000 | 0.000000 | 10000.000000 | 132.000000 | 0.54 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 08:00:00 | 63.000000 | 17.560000 | 22.220000 | 76.000000 | 1010.000000 |  | 21.980000 | 0.000000 | 10000.000000 | 89.000000 | 0.97 | 0.980000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 09:00:00 | 58.000000 | 17.630000 | 21.890000 | 78.000000 | 1010.000000 |  | 21.630000 | 0.000000 | 10000.000000 | 97.000000 | 1.55 | 1.550000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 10:00:00 | 54.000000 | 17.680000 | 21.540000 | 80.000000 | 1011.000000 |  | 21.270000 | 0.000000 | 10000.000000 | 89.000000 | 2.06 | 1.990000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 17.390000 | 21.210000 | 80.000000 | 1011.000000 |  | 20.970000 | 0.000000 | 10000.000000 | 91.000000 | 2.59 | 2.180000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 12:00:00 | 10.000000 | 17.040000 | 21.620000 | 76.000000 | 1012.000000 |  | 21.440000 | 0.280000 | 10000.000000 | 98.000000 | 3.15 | 2.250000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 13:00:00 | 18.000000 | 16.440000 | 23.740000 | 64.000000 | 1013.000000 |  | 23.650000 | 1.480000 | 10000.000000 | 97.000000 | 3.84 | 2.570000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 14:00:00 | 23.000000 | 16.660000 | 25.950000 | 57.000000 | 1014.000000 |  | 25.820000 | 3.780000 | 10000.000000 | 105.000000 | 4.15 | 2.900000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 15:00:00 | 41.000000 | 17.130000 | 28.210000 | 53.000000 | 1014.000000 |  | 27.560000 | 6.690000 | 10000.000000 | 108.000000 | 4.13 | 3.280000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 16:00:00 | 53.000000 | 16.800000 | 29.310000 | 48.000000 | 1013.000000 |  | 28.910000 | 8.760000 | 10000.000000 | 114.000000 | 3.54 | 3.270000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 17:00:00 | 63.000000 | 16.160000 | 29.820000 | 44.000000 | 1012.000000 |  | 29.710000 | 9.700000 | 10000.000000 | 120.000000 | 2.87 | 2.630000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 15.150000 | 29.970000 | 40.000000 | 1011.000000 |  | 30.240000 | 8.880000 | 10000.000000 | 127.000000 | 2.05 | 1.620000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 14.940000 | 29.690000 | 40.000000 | 1010.000000 |  | 30.000000 | 5.940000 | 10000.000000 | 204.000000 | 1.57 | 0.930000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 15.590000 | 29.420000 | 43.000000 | 1009.000000 |  | 29.470000 | 3.430000 | 10000.000000 | 273.000000 | 1.77 | 1.440000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 16.860000 | 28.760000 | 50.000000 | 1009.000000 |  | 28.270000 | 1.380000 | 10000.000000 | 312.000000 | 2.6 | 2.730000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 18.880000 | 26.230000 | 64.000000 | 1009.000000 |  | 26.230000 | 0.270000 | 10000.000000 | 322.000000 | 4 | 2.850000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13095020 | "PRIMATES [13095020]" | 9.530139 | -75.351361 | 200.000000 | Climática Principal | Convencional | Activa | 1984-12-15 00:00:00 | NaT | Sucre | Colosó | Ay Pechelin | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Caribe - Litoral | Directos Caribe Golfo de Morrosquillo | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 19.130000 | 24.440000 | 74.000000 | 1010.000000 |  | 24.050000 | 0.000000 | 10000.000000 | 323.000000 | 3.52 | 2.610000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station13095020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13095020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13095020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13095020_OWM_Windspeed_20220111.png)
