
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NORMAL MANATI  - AUT [29035080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29035080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.45358333,-74.95463889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.45358333&lon=-74.95463889)


| Parameter | Value |
|---|---|
| Code | 29035080 |
| Name | NORMAL MANATI  - AUT [29035080] |
| Latitude, ° | 10.45358333 |
| Longitude, ° | -74.95463889 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1963-10-14 19:00:00 |
| Suspension date | NaT |
| State | Atlantico |
| County | Manatí |
| Stream | 0 |
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

### (CNE index 2844) Open Weather values for station 29035080 - NORMAL MANATI  - AUT [29035080]

JSON data from API OWM:

```
{'lat': 10.4536, 'lon': -74.9546, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813632, 'sunset': 1641855225, 'temp': 29.04, 'feels_like': 28.09, 'pressure': 1008, 'humidity': 33, 'dew_point': 11.15, 'uvi': 3.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.51, 'wind_deg': 309, 'wind_gust': 3.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1010, 'humidity': 68, 'dew_point': 19.68, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 2.83, 'wind_deg': 334, 'wind_gust': 4.93, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.82, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 335, 'wind_gust': 2.42, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1011, 'humidity': 76, 'dew_point': 21.48, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 335, 'wind_gust': 3.03, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.69, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 322, 'wind_gust': 3.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.11, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 317, 'wind_gust': 2.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 27.04, 'feels_like': 29.83, 'pressure': 1011, 'humidity': 80, 'dew_point': 23.29, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 314, 'wind_gust': 1.36, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1010, 'humidity': 81, 'dew_point': 22.52, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 335, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1010, 'humidity': 81, 'dew_point': 22.52, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 356, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 25.04, 'feels_like': 25.71, 'pressure': 1010, 'humidity': 81, 'dew_point': 21.55, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 359, 'wind_gust': 1.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 25.04, 'feels_like': 25.77, 'pressure': 1010, 'humidity': 83, 'dew_point': 21.95, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 60, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 25.04, 'feels_like': 25.79, 'pressure': 1011, 'humidity': 84, 'dew_point': 22.15, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 203, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 25.04, 'feels_like': 25.77, 'pressure': 1011, 'humidity': 83, 'dew_point': 21.95, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 190, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 25.04, 'feels_like': 25.61, 'pressure': 1012, 'humidity': 77, 'dew_point': 20.73, 'uvi': 0.27, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 99, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1014, 'humidity': 62, 'dew_point': 18.2, 'uvi': 1.5, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 130, 'wind_gust': 2.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.04, 'feels_like': 28.59, 'pressure': 1014, 'humidity': 51, 'dew_point': 16.96, 'uvi': 3.8, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 108, 'wind_gust': 2.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.04, 'feels_like': 28.83, 'pressure': 1014, 'humidity': 42, 'dew_point': 14.83, 'uvi': 6.66, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 124, 'wind_gust': 3.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.04, 'feels_like': 28.24, 'pressure': 1013, 'humidity': 35, 'dew_point': 12.04, 'uvi': 8.91, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 121, 'wind_gust': 3.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.04, 'feels_like': 28.79, 'pressure': 1011, 'humidity': 30, 'dew_point': 10.58, 'uvi': 9.79, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 128, 'wind_gust': 2.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.04, 'feels_like': 27.8, 'pressure': 1010, 'humidity': 28, 'dew_point': 8.7, 'uvi': 8.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 294, 'wind_gust': 2.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 29.04, 'feels_like': 27.75, 'pressure': 1009, 'humidity': 27, 'dew_point': 8.16, 'uvi': 6.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 305, 'wind_gust': 3.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.04, 'feels_like': 28.09, 'pressure': 1008, 'humidity': 33, 'dew_point': 11.15, 'uvi': 3.51, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.51, 'wind_deg': 309, 'wind_gust': 3.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.04, 'feels_like': 27.91, 'pressure': 1008, 'humidity': 43, 'dew_point': 14.3, 'uvi': 1.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.17, 'wind_deg': 317, 'wind_gust': 5.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.04, 'feels_like': 27.52, 'pressure': 1009, 'humidity': 51, 'dew_point': 16.04, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.69, 'wind_deg': 344, 'wind_gust': 5.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.04, 'feels_like': 26.04, 'pressure': 1010, 'humidity': 64, 'dew_point': 18.7, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.66, 'wind_deg': 354, 'wind_gust': 8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 00:00:00 | 4.000000 | 19.680000 | 26.040000 | 68.000000 | 1010.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 334.000000 | 4.93 | 2.830000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 20.820000 | 26.040000 | 73.000000 | 1011.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 335.000000 | 2.42 | 1.890000 | 800 | Clear | clear sky | 01n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 02:00:00 | 41.000000 | 21.480000 | 26.040000 | 76.000000 | 1011.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 335.000000 | 3.03 | 2.170000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 03:00:00 | 60.000000 | 21.690000 | 26.040000 | 77.000000 | 1011.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 322.000000 | 3.65 | 2.260000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 04:00:00 | 70.000000 | 22.110000 | 26.040000 | 79.000000 | 1011.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 317.000000 | 2.77 | 1.970000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 05:00:00 | 76.000000 | 23.290000 | 29.830000 | 80.000000 | 1011.000000 |  | 27.040000 | 0.000000 | 10000.000000 | 314.000000 | 1.36 | 1.270000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 06:00:00 | 99.000000 | 22.520000 | 26.040000 | 81.000000 | 1010.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 335.000000 | 0.84 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 22.520000 | 26.040000 | 81.000000 | 1010.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 356.000000 | 1.21 | 1.040000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 21.550000 | 25.710000 | 81.000000 | 1010.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 359.000000 | 1.54 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 09:00:00 | 88.000000 | 21.950000 | 25.770000 | 83.000000 | 1010.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 60.000000 | 1.16 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 22.150000 | 25.790000 | 84.000000 | 1011.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 203.000000 | 0.93 | 0.690000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 11:00:00 | 83.000000 | 21.950000 | 25.770000 | 83.000000 | 1011.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 190.000000 | 1.29 | 0.510000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 12:00:00 | 95.000000 | 20.730000 | 25.610000 | 77.000000 | 1012.000000 |  | 25.040000 | 0.270000 | 10000.000000 | 99.000000 | 1.84 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 13:00:00 | 97.000000 | 18.200000 | 26.040000 | 62.000000 | 1014.000000 |  | 26.040000 | 1.500000 | 10000.000000 | 130.000000 | 2.44 | 1.080000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 16.960000 | 28.590000 | 51.000000 | 1014.000000 |  | 28.040000 | 3.800000 | 10000.000000 | 108.000000 | 2.6 | 1.360000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 15:00:00 | 95.000000 | 14.830000 | 28.830000 | 42.000000 | 1014.000000 |  | 29.040000 | 6.660000 | 10000.000000 | 124.000000 | 3.23 | 1.940000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 16:00:00 | 94.000000 | 12.040000 | 28.240000 | 35.000000 | 1013.000000 |  | 29.040000 | 8.910000 | 10000.000000 | 121.000000 | 3.04 | 1.820000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 17:00:00 | 95.000000 | 10.580000 | 28.790000 | 30.000000 | 1011.000000 |  | 30.040000 | 9.790000 | 10000.000000 | 128.000000 | 2.13 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 8.700000 | 27.800000 | 28.000000 | 1010.000000 |  | 29.040000 | 8.910000 | 10000.000000 | 294.000000 | 2.14 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 8.160000 | 27.750000 | 27.000000 | 1009.000000 |  | 29.040000 | 6.160000 | 10000.000000 | 305.000000 | 3.09 | 2.500000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 11.150000 | 28.090000 | 33.000000 | 1008.000000 |  | 29.040000 | 3.510000 | 10000.000000 | 309.000000 | 3.76 | 4.510000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 14.300000 | 27.910000 | 43.000000 | 1008.000000 |  | 28.040000 | 1.390000 | 10000.000000 | 317.000000 | 5.11 | 5.170000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 16.040000 | 27.520000 | 51.000000 | 1009.000000 |  | 27.040000 | 0.260000 | 10000.000000 | 344.000000 | 5.76 | 4.690000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29035080 | "NORMAL MANATI  - AUT [29035080]" | 10.453583 | -74.954639 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 1963-10-14 19:00:00 | NaT | Atlantico | Manatí | 0 | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Canal del Dique margen derecho | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 18.700000 | 26.040000 | 64.000000 | 1010.000000 |  | 26.040000 | 0.000000 | 10000.000000 | 354.000000 | 8 | 4.660000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29035080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29035080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29035080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29035080_OWM_Windspeed_20220111.png)
