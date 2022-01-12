
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CARMEN DE BOLIVAR  - AUT [29015040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29015040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.72,-75.11) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.72&lon=-75.11)


| Parameter | Value |
|---|---|
| Code | 29015040 |
| Name | CARMEN DE BOLIVAR  - AUT [29015040] |
| Latitude, ° | 9.72 |
| Longitude, ° | -75.11 |
| Elevation, m | 152 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-03-01 00:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | El Carmén De Bolívar |
| Stream | 0 |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Directos al Bajo Magdalena entre El Plato y Calamar |

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

### (CNE index 4401) Open Weather values for station 29015040 - CARMEN DE BOLIVAR  - AUT [29015040]

JSON data from API OWM:

```
{'lat': 9.72, 'lon': -75.11, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813597, 'sunset': 1641855335, 'temp': 31.25, 'feels_like': 30.68, 'pressure': 1009, 'humidity': 36, 'dew_point': 14.41, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 225, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 23.9, 'feels_like': 24.49, 'pressure': 1011, 'humidity': 82, 'dew_point': 20.64, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 310, 'wind_gust': 4.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 23.38, 'feels_like': 23.99, 'pressure': 1011, 'humidity': 85, 'dew_point': 20.71, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 311, 'wind_gust': 4.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.33, 'feels_like': 23.83, 'pressure': 1012, 'humidity': 81, 'dew_point': 19.89, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 300, 'wind_gust': 3.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.31, 'feels_like': 23.73, 'pressure': 1012, 'humidity': 78, 'dew_point': 19.26, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 297, 'wind_gust': 1.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.27, 'feels_like': 23.61, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.59, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 295, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.13, 'feels_like': 23.43, 'pressure': 1011, 'humidity': 74, 'dew_point': 18.24, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 276, 'wind_gust': 1.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.74, 'feels_like': 23, 'pressure': 1011, 'humidity': 74, 'dew_point': 17.87, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 236, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.44, 'feels_like': 22.7, 'pressure': 1010, 'humidity': 75, 'dew_point': 17.79, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 144, 'wind_gust': 0.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.87, 'feels_like': 22.12, 'pressure': 1010, 'humidity': 77, 'dew_point': 17.66, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 97, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.47, 'feels_like': 21.74, 'pressure': 1010, 'humidity': 79, 'dew_point': 17.68, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 88, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.23, 'feels_like': 21.47, 'pressure': 1011, 'humidity': 79, 'dew_point': 17.44, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 83, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.94, 'feels_like': 21.1, 'pressure': 1012, 'humidity': 77, 'dew_point': 16.76, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 87, 'wind_gust': 1.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.51, 'feels_like': 21.6, 'pressure': 1013, 'humidity': 72, 'dew_point': 16.25, 'uvi': 0.28, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 112, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.8, 'feels_like': 23.83, 'pressure': 1014, 'humidity': 61, 'dew_point': 15.83, 'uvi': 1.48, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 115, 'wind_gust': 3.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1014, 'humidity': 54, 'dew_point': 16.24, 'uvi': 3.78, 'clouds': 36, 'visibility': 10000, 'wind_speed': 2.48, 'wind_deg': 119, 'wind_gust': 4.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 28.38, 'feels_like': 28.6, 'pressure': 1014, 'humidity': 47, 'dew_point': 15.99, 'uvi': 6.69, 'clouds': 36, 'visibility': 10000, 'wind_speed': 3.21, 'wind_deg': 117, 'wind_gust': 4.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 29.96, 'feels_like': 29.76, 'pressure': 1013, 'humidity': 41, 'dew_point': 15.28, 'uvi': 8.76, 'clouds': 51, 'visibility': 10000, 'wind_speed': 3.36, 'wind_deg': 117, 'wind_gust': 3.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.97, 'feels_like': 30.6, 'pressure': 1012, 'humidity': 38, 'dew_point': 15, 'uvi': 9.7, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 120, 'wind_gust': 2.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.7, 'feels_like': 30.96, 'pressure': 1011, 'humidity': 34, 'dew_point': 13.92, 'uvi': 8.88, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 124, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.79, 'feels_like': 30.94, 'pressure': 1010, 'humidity': 33, 'dew_point': 13.54, 'uvi': 5.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 157, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.25, 'feels_like': 30.68, 'pressure': 1009, 'humidity': 36, 'dew_point': 14.41, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 225, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.6, 'feels_like': 29.81, 'pressure': 1009, 'humidity': 45, 'dew_point': 16.42, 'uvi': 1.38, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.51, 'wind_deg': 260, 'wind_gust': 2.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.49, 'feels_like': 28.55, 'pressure': 1009, 'humidity': 58, 'dew_point': 18.49, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 261, 'wind_gust': 3.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 24.72, 'feels_like': 25.1, 'pressure': 1010, 'humidity': 71, 'dew_point': 19.11, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 285, 'wind_gust': 3.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 00:00:00 | 63.000000 | 20.640000 | 24.490000 | 82.000000 | 1011.000000 |  | 23.900000 | 0.000000 | 10000.000000 | 310.000000 | 4.92 | 2.560000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 01:00:00 | 74.000000 | 20.710000 | 23.990000 | 85.000000 | 1011.000000 |  | 23.380000 | 0.000000 | 10000.000000 | 311.000000 | 4.19 | 2.200000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 02:00:00 | 85.000000 | 19.890000 | 23.830000 | 81.000000 | 1012.000000 |  | 23.330000 | 0.000000 | 10000.000000 | 300.000000 | 3.22 | 1.890000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 03:00:00 | 90.000000 | 19.260000 | 23.730000 | 78.000000 | 1012.000000 |  | 23.310000 | 0.000000 | 10000.000000 | 297.000000 | 1.99 | 1.670000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 18.590000 | 23.610000 | 75.000000 | 1011.000000 |  | 23.270000 | 0.000000 | 10000.000000 | 295.000000 | 1.47 | 1.440000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 18.240000 | 23.430000 | 74.000000 | 1011.000000 |  | 23.130000 | 0.000000 | 10000.000000 | 276.000000 | 1.08 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 17.870000 | 23.000000 | 74.000000 | 1011.000000 |  | 22.740000 | 0.000000 | 10000.000000 | 236.000000 | 0.7 | 0.570000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 07:00:00 | 87.000000 | 17.790000 | 22.700000 | 75.000000 | 1010.000000 |  | 22.440000 | 0.000000 | 10000.000000 | 144.000000 | 0.89 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 08:00:00 | 76.000000 | 17.660000 | 22.120000 | 77.000000 | 1010.000000 |  | 21.870000 | 0.000000 | 10000.000000 | 97.000000 | 1.07 | 0.980000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 09:00:00 | 56.000000 | 17.680000 | 21.740000 | 79.000000 | 1010.000000 |  | 21.470000 | 0.000000 | 10000.000000 | 88.000000 | 1.11 | 0.990000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 10:00:00 | 55.000000 | 17.440000 | 21.470000 | 79.000000 | 1011.000000 |  | 21.230000 | 0.000000 | 10000.000000 | 83.000000 | 1.07 | 0.820000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 11:00:00 | 57.000000 | 16.760000 | 21.100000 | 77.000000 | 1012.000000 |  | 20.940000 | 0.000000 | 10000.000000 | 87.000000 | 1.45 | 1.300000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 12:00:00 | 54.000000 | 16.250000 | 21.600000 | 72.000000 | 1013.000000 |  | 21.510000 | 0.280000 | 10000.000000 | 112.000000 | 1.43 | 1.200000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 13:00:00 | 57.000000 | 15.830000 | 23.830000 | 61.000000 | 1014.000000 |  | 23.800000 | 1.480000 | 10000.000000 | 115.000000 | 3.33 | 1.940000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 14:00:00 | 36.000000 | 16.240000 | 26.280000 | 54.000000 | 1014.000000 |  | 26.280000 | 3.780000 | 10000.000000 | 119.000000 | 4.45 | 2.480000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 15:00:00 | 36.000000 | 15.990000 | 28.600000 | 47.000000 | 1014.000000 |  | 28.380000 | 6.690000 | 10000.000000 | 117.000000 | 4.23 | 3.210000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 16:00:00 | 51.000000 | 15.280000 | 29.760000 | 41.000000 | 1013.000000 |  | 29.960000 | 8.760000 | 10000.000000 | 117.000000 | 3.69 | 3.360000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 15.000000 | 30.600000 | 38.000000 | 1012.000000 |  | 30.970000 | 9.700000 | 10000.000000 | 120.000000 | 2.97 | 2.810000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 13.920000 | 30.960000 | 34.000000 | 1011.000000 |  | 31.700000 | 8.880000 | 10000.000000 | 124.000000 | 2.25 | 2.070000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.540000 | 30.940000 | 33.000000 | 1010.000000 |  | 31.790000 | 5.940000 | 10000.000000 | 157.000000 | 1.58 | 1.430000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 14.410000 | 30.680000 | 36.000000 | 1009.000000 |  | 31.250000 | 3.430000 | 10000.000000 | 225.000000 | 1.51 | 1.570000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 16.420000 | 29.810000 | 45.000000 | 1009.000000 |  | 29.600000 | 1.380000 | 10000.000000 | 260.000000 | 2.96 | 2.510000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 18.490000 | 28.550000 | 58.000000 | 1009.000000 |  | 27.490000 | 0.270000 | 10000.000000 | 261.000000 | 3.92 | 2.170000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29015040 | "CARMEN DE BOLIVAR  - AUT [29015040]" | 9.720000 | -75.110000 | 152.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Bolívar | El Carmén De Bolívar | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre El Plato y Calamar | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 19.110000 | 25.100000 | 71.000000 | 1010.000000 |  | 24.720000 | 0.000000 | 10000.000000 | 285.000000 | 3.42 | 2.410000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29015040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29015040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29015040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29015040_OWM_Windspeed_20220111.png)
