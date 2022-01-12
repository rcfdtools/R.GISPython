
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SANTA LUCIA GRANJA [29035130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.31666667,-74.95) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.31666667&lon=-74.95)


| Parameter | Value |
|---|---|
| Code | 29035130 |
| Name | SANTA LUCIA GRANJA [29035130] |
| Latitude, ° | 10.31666667 |
| Longitude, ° | -74.95 |
| Elevation, m | 5 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-03-15 00:00:00 |
| Suspension date | 1987-11-15 00:00:00 |
| State | Atlantico |
| County | Santa Lucia |
| Stream | Canal Del Dique |
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

### (CNE index 3246) Open Weather values for station 29035130 - SANTA LUCIA GRANJA [29035130]

JSON data from API OWM:

```
{'lat': 10.3167, 'lon': -74.95, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813618, 'sunset': 1641855238, 'temp': 29.96, 'feels_like': 28.65, 'pressure': 1008, 'humidity': 29, 'dew_point': 10.01, 'uvi': 3.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.42, 'wind_deg': 265, 'wind_gust': 3.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1010, 'humidity': 63, 'dew_point': 18.38, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 2.94, 'wind_deg': 323, 'wind_gust': 4.91, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1011, 'humidity': 69, 'dew_point': 19.84, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 340, 'wind_gust': 2.37, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.75, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 329, 'wind_gust': 2.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 24.96, 'feels_like': 25.44, 'pressure': 1011, 'humidity': 74, 'dew_point': 20.01, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 306, 'wind_gust': 2.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.96, 'feels_like': 25.5, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.44, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 295, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.96, 'feels_like': 25.52, 'pressure': 1011, 'humidity': 77, 'dew_point': 20.65, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 290, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.96, 'feels_like': 24.47, 'pressure': 1010, 'humidity': 79, 'dew_point': 20.09, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 297, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.96, 'feels_like': 24.53, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.5, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 2, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.96, 'feels_like': 24.55, 'pressure': 1010, 'humidity': 82, 'dew_point': 20.7, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 36, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.96, 'feels_like': 24.58, 'pressure': 1010, 'humidity': 83, 'dew_point': 20.9, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 142, 'wind_gust': 1.23, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.96, 'feels_like': 24.55, 'pressure': 1011, 'humidity': 82, 'dew_point': 20.7, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 193, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.96, 'feels_like': 23.27, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.29, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 165, 'wind_gust': 3.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.96, 'feels_like': 23.11, 'pressure': 1012, 'humidity': 69, 'dew_point': 16.97, 'uvi': 0.27, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 129, 'wind_gust': 5.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.96, 'feels_like': 25.03, 'pressure': 1013, 'humidity': 58, 'dew_point': 16.13, 'uvi': 1.5, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.87, 'wind_deg': 123, 'wind_gust': 5.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.96, 'feels_like': 28.23, 'pressure': 1014, 'humidity': 48, 'dew_point': 15.94, 'uvi': 3.8, 'clouds': 93, 'visibility': 10000, 'wind_speed': 3.07, 'wind_deg': 113, 'wind_gust': 4.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.96, 'feels_like': 28.48, 'pressure': 1014, 'humidity': 39, 'dew_point': 13.62, 'uvi': 6.66, 'clouds': 93, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 112, 'wind_gust': 4.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.96, 'feels_like': 27.96, 'pressure': 1013, 'humidity': 32, 'dew_point': 10.62, 'uvi': 8.91, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.94, 'wind_deg': 119, 'wind_gust': 4.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.96, 'feels_like': 27.73, 'pressure': 1011, 'humidity': 28, 'dew_point': 8.63, 'uvi': 9.79, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 140, 'wind_gust': 2.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.96, 'feels_like': 28.52, 'pressure': 1010, 'humidity': 27, 'dew_point': 8.94, 'uvi': 8.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 190, 'wind_gust': 2.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.96, 'feels_like': 29.37, 'pressure': 1008, 'humidity': 26, 'dew_point': 9.23, 'uvi': 6.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 252, 'wind_gust': 2.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.96, 'feels_like': 28.65, 'pressure': 1008, 'humidity': 29, 'dew_point': 10.01, 'uvi': 3.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.42, 'wind_deg': 265, 'wind_gust': 3.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.96, 'feels_like': 28.09, 'pressure': 1008, 'humidity': 34, 'dew_point': 11.53, 'uvi': 1.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.6, 'wind_deg': 282, 'wind_gust': 4.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.96, 'feels_like': 28.15, 'pressure': 1008, 'humidity': 47, 'dew_point': 15.61, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.74, 'wind_deg': 322, 'wind_gust': 5.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.96, 'feels_like': 28.03, 'pressure': 1009, 'humidity': 60, 'dew_point': 18.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.36, 'wind_deg': 345, 'wind_gust': 7.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 00:00:00 | 6.000000 | 18.380000 | 25.960000 | 63.000000 | 1010.000000 |  | 25.960000 | 0.000000 | 10000.000000 | 323.000000 | 4.91 | 2.940000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 19.840000 | 25.960000 | 69.000000 | 1011.000000 |  | 25.960000 | 0.000000 | 10000.000000 | 340.000000 | 2.37 | 1.770000 | 800 | Clear | clear sky | 01n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 02:00:00 | 49.000000 | 20.750000 | 25.960000 | 73.000000 | 1011.000000 |  | 25.960000 | 0.000000 | 10000.000000 | 329.000000 | 2.56 | 1.880000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 03:00:00 | 66.000000 | 20.010000 | 25.440000 | 74.000000 | 1011.000000 |  | 24.960000 | 0.000000 | 10000.000000 | 306.000000 | 2.87 | 2.100000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 04:00:00 | 75.000000 | 20.440000 | 25.500000 | 76.000000 | 1011.000000 |  | 24.960000 | 0.000000 | 10000.000000 | 295.000000 | 2.3 | 1.840000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 05:00:00 | 80.000000 | 20.650000 | 25.520000 | 77.000000 | 1011.000000 |  | 24.960000 | 0.000000 | 10000.000000 | 290.000000 | 1.32 | 1.230000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 06:00:00 | 95.000000 | 20.090000 | 24.470000 | 79.000000 | 1010.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 297.000000 | 0.64 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 20.500000 | 24.530000 | 81.000000 | 1010.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 2.000000 | 0.95 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 20.700000 | 24.550000 | 82.000000 | 1010.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 36.000000 | 1.04 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 09:00:00 | 79.000000 | 20.900000 | 24.580000 | 83.000000 | 1010.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 142.000000 | 1.23 | 0.700000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 10:00:00 | 82.000000 | 20.700000 | 24.550000 | 82.000000 | 1011.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 193.000000 | 1.76 | 1.620000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 11:00:00 | 71.000000 | 18.290000 | 23.270000 | 75.000000 | 1011.000000 |  | 22.960000 | 0.000000 | 10000.000000 | 165.000000 | 3.32 | 1.970000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 12:00:00 | 97.000000 | 16.970000 | 23.110000 | 69.000000 | 1012.000000 |  | 22.960000 | 0.270000 | 10000.000000 | 129.000000 | 5.39 | 2.070000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 16.130000 | 25.030000 | 58.000000 | 1013.000000 |  | 24.960000 | 1.500000 | 10000.000000 | 123.000000 | 5.24 | 2.870000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 14:00:00 | 93.000000 | 15.940000 | 28.230000 | 48.000000 | 1014.000000 |  | 27.960000 | 3.800000 | 10000.000000 | 113.000000 | 4.79 | 3.070000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 15:00:00 | 93.000000 | 13.620000 | 28.480000 | 39.000000 | 1014.000000 |  | 28.960000 | 6.660000 | 10000.000000 | 112.000000 | 4.59 | 3.190000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 16:00:00 | 92.000000 | 10.620000 | 27.960000 | 32.000000 | 1013.000000 |  | 28.960000 | 8.910000 | 10000.000000 | 119.000000 | 4.01 | 2.940000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 17:00:00 | 93.000000 | 8.630000 | 27.730000 | 28.000000 | 1011.000000 |  | 28.960000 | 9.790000 | 10000.000000 | 140.000000 | 2.95 | 1.910000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 8.940000 | 28.520000 | 27.000000 | 1010.000000 |  | 29.960000 | 8.910000 | 10000.000000 | 190.000000 | 2.52 | 1.290000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 9.230000 | 29.370000 | 26.000000 | 1008.000000 |  | 30.960000 | 6.160000 | 10000.000000 | 252.000000 | 2.89 | 1.940000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 10.010000 | 28.650000 | 29.000000 | 1008.000000 |  | 29.960000 | 3.510000 | 10000.000000 | 265.000000 | 3.39 | 3.420000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 11.530000 | 28.090000 | 34.000000 | 1008.000000 |  | 28.960000 | 1.390000 | 10000.000000 | 282.000000 | 4.38 | 4.600000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 15.610000 | 28.150000 | 47.000000 | 1008.000000 |  | 27.960000 | 0.260000 | 10000.000000 | 322.000000 | 5.99 | 4.740000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035130 | "SANTA LUCIA GRANJA [29035130]" | 10.316667 | -74.950000 | 5.000000 | Climática Principal | Convencional | Suspendida | 1968-03-15 00:00:00 | 1987-11-15 00:00:00 | Atlantico | Santa Lucia | Canal Del Dique | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 18.540000 | 28.030000 | 60.000000 | 1009.000000 |  | 26.960000 | 0.000000 | 10000.000000 | 345.000000 | 7.43 | 4.360000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035130_OWM_Windspeed_20220111.png)
