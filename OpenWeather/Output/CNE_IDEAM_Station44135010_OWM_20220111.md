
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ARARACUARA [44135010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44135010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=-0.61636111,-72.38191667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=-0.61636111&lon=-72.38191667)


| Parameter | Value |
|---|---|
| Code | 44135010 |
| Name | ARARACUARA [44135010] |
| Latitude, ° | -0.61636111 |
| Longitude, ° | -72.38191667 |
| Elevation, m | 150 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1979-03-15 00:00:00 |
| Suspension date | NaT |
| State | Caquetá |
| County | Solano |
| Stream | Caqueta |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Caquetá |
| SZH - Hydrographic subzone | Río Caqueta Bajo |

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

### (CNE index 2480) Open Weather values for station 44135010 - ARARACUARA [44135010]

JSON data from API OWM:

```
{'lat': -0.6164, 'lon': -72.3819, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641811937, 'sunset': 1641855685, 'temp': 34.4, 'feels_like': 33.65, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.81, 'uvi': 4.93, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 28, 'wind_gust': 3.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.94, 'feels_like': 26.1, 'pressure': 1008, 'humidity': 58, 'dew_point': 17.05, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 52, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.07, 'feels_like': 25.25, 'pressure': 1009, 'humidity': 62, 'dew_point': 17.28, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 65, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.28, 'feels_like': 24.49, 'pressure': 1010, 'humidity': 66, 'dew_point': 17.53, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 67, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.78, 'feels_like': 24.04, 'pressure': 1011, 'humidity': 70, 'dew_point': 17.98, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 57, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.48, 'feels_like': 23.74, 'pressure': 1011, 'humidity': 71, 'dew_point': 17.92, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 51, 'wind_gust': 0.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 23.15, 'feels_like': 23.4, 'pressure': 1010, 'humidity': 72, 'dew_point': 17.83, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 35, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 22.35, 'feels_like': 22.6, 'pressure': 1010, 'humidity': 75, 'dew_point': 17.71, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 359, 'wind_gust': 4.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 21.86, 'feels_like': 22.11, 'pressure': 1010, 'humidity': 77, 'dew_point': 17.65, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 18, 'wind_gust': 3.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 21.59, 'feels_like': 21.82, 'pressure': 1009, 'humidity': 77, 'dew_point': 17.39, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 24, 'wind_gust': 2.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.33, 'feels_like': 21.56, 'pressure': 1010, 'humidity': 78, 'dew_point': 17.34, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 24, 'wind_gust': 3.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.11, 'feels_like': 21.31, 'pressure': 1010, 'humidity': 78, 'dew_point': 17.13, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 33, 'wind_gust': 7.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.81, 'feels_like': 21.01, 'pressure': 1011, 'humidity': 79, 'dew_point': 17.04, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 27, 'wind_gust': 6.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 22.78, 'feels_like': 23.02, 'pressure': 1012, 'humidity': 73, 'dew_point': 17.69, 'uvi': 0.79, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 26, 'wind_gust': 8.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.13, 'feels_like': 26.13, 'pressure': 1013, 'humidity': 59, 'dew_point': 17.49, 'uvi': 2.77, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 31, 'wind_gust': 7.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.93, 'feels_like': 29.45, 'pressure': 1014, 'humidity': 49, 'dew_point': 17.15, 'uvi': 6.04, 'clouds': 69, 'visibility': 10000, 'wind_speed': 2.75, 'wind_deg': 28, 'wind_gust': 7.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 31.04, 'feels_like': 31.11, 'pressure': 1013, 'humidity': 41, 'dew_point': 16.25, 'uvi': 9.62, 'clouds': 69, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 29, 'wind_gust': 6.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 32.64, 'feels_like': 32.48, 'pressure': 1012, 'humidity': 36, 'dew_point': 15.63, 'uvi': 12.32, 'clouds': 65, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 29, 'wind_gust': 5.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.84, 'feels_like': 33.43, 'pressure': 1010, 'humidity': 32, 'dew_point': 14.84, 'uvi': 13.06, 'clouds': 66, 'visibility': 10000, 'wind_speed': 3.16, 'wind_deg': 29, 'wind_gust': 5.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 34.38, 'feels_like': 33.8, 'pressure': 1009, 'humidity': 30, 'dew_point': 14.31, 'uvi': 11.6, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.9, 'wind_deg': 27, 'wind_gust': 4.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.62, 'feels_like': 33.94, 'pressure': 1008, 'humidity': 29, 'dew_point': 13.99, 'uvi': 8.58, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 27, 'wind_gust': 4.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 34.4, 'feels_like': 33.65, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.81, 'uvi': 4.93, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 28, 'wind_gust': 3.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.76, 'feels_like': 33.14, 'pressure': 1007, 'humidity': 31, 'dew_point': 14.28, 'uvi': 1.97, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 36, 'wind_gust': 3.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 31.41, 'feels_like': 31.78, 'pressure': 1007, 'humidity': 42, 'dew_point': 16.96, 'uvi': 0.43, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 51, 'wind_gust': 3.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27, 'feels_like': 27.6, 'pressure': 1007, 'humidity': 53, 'dew_point': 16.61, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 70, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 00:00:00 | 58.000000 | 17.050000 | 26.100000 | 58.000000 | 1008.000000 |  | 25.940000 | 0.000000 | 10000.000000 | 52.000000 | 1.24 | 1.180000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 01:00:00 | 65.000000 | 17.280000 | 25.250000 | 62.000000 | 1009.000000 |  | 25.070000 | 0.000000 | 10000.000000 | 65.000000 | 1.43 | 1.260000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 02:00:00 | 70.000000 | 17.530000 | 24.490000 | 66.000000 | 1010.000000 |  | 24.280000 | 0.000000 | 10000.000000 | 67.000000 | 1.18 | 1.080000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 03:00:00 | 61.000000 | 17.980000 | 24.040000 | 70.000000 | 1011.000000 |  | 23.780000 | 0.000000 | 10000.000000 | 57.000000 | 0.9 | 0.820000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 04:00:00 | 50.000000 | 17.920000 | 23.740000 | 71.000000 | 1011.000000 |  | 23.480000 | 0.000000 | 10000.000000 | 51.000000 | 0.86 | 0.830000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 05:00:00 | 48.000000 | 17.830000 | 23.400000 | 72.000000 | 1010.000000 |  | 23.150000 | 0.000000 | 10000.000000 | 35.000000 | 1.11 | 0.880000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 06:00:00 | 41.000000 | 17.710000 | 22.600000 | 75.000000 | 1010.000000 |  | 22.350000 | 0.000000 | 10000.000000 | 359.000000 | 4.63 | 1.550000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 07:00:00 | 40.000000 | 17.650000 | 22.110000 | 77.000000 | 1010.000000 |  | 21.860000 | 0.000000 | 10000.000000 | 18.000000 | 3.99 | 1.270000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 08:00:00 | 62.000000 | 17.390000 | 21.820000 | 77.000000 | 1009.000000 |  | 21.590000 | 0.000000 | 10000.000000 | 24.000000 | 2.94 | 1.130000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 17.340000 | 21.560000 | 78.000000 | 1010.000000 |  | 21.330000 | 0.000000 | 10000.000000 | 24.000000 | 3.69 | 1.190000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 10:00:00 | 70.000000 | 17.130000 | 21.310000 | 78.000000 | 1010.000000 |  | 21.110000 | 0.000000 | 10000.000000 | 33.000000 | 7.33 | 1.420000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 11:00:00 | 76.000000 | 17.040000 | 21.010000 | 79.000000 | 1011.000000 |  | 20.810000 | 0.000000 | 10000.000000 | 27.000000 | 6.34 | 1.330000 | 803 | Clouds | broken clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 12:00:00 | 86.000000 | 17.690000 | 23.020000 | 73.000000 | 1012.000000 |  | 22.780000 | 0.790000 | 10000.000000 | 26.000000 | 8.42 | 1.450000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 17.490000 | 26.130000 | 59.000000 | 1013.000000 |  | 26.130000 | 2.770000 | 10000.000000 | 31.000000 | 7.35 | 2.190000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 14:00:00 | 69.000000 | 17.150000 | 29.450000 | 49.000000 | 1014.000000 |  | 28.930000 | 6.040000 | 10000.000000 | 28.000000 | 7.41 | 2.750000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 15:00:00 | 69.000000 | 16.250000 | 31.110000 | 41.000000 | 1013.000000 |  | 31.040000 | 9.620000 | 10000.000000 | 29.000000 | 6.18 | 2.960000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 16:00:00 | 65.000000 | 15.630000 | 32.480000 | 36.000000 | 1012.000000 |  | 32.640000 | 12.320000 | 10000.000000 | 29.000000 | 5.99 | 3.100000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 17:00:00 | 66.000000 | 14.840000 | 33.430000 | 32.000000 | 1010.000000 |  | 33.840000 | 13.060000 | 10000.000000 | 29.000000 | 5.72 | 3.160000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 14.310000 | 33.800000 | 30.000000 | 1009.000000 |  | 34.380000 | 11.600000 | 10000.000000 | 27.000000 | 4.81 | 2.900000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.990000 | 33.940000 | 29.000000 | 1008.000000 |  | 34.620000 | 8.580000 | 10000.000000 | 27.000000 | 4.14 | 2.600000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 13.810000 | 33.650000 | 29.000000 | 1007.000000 |  | 34.400000 | 4.930000 | 10000.000000 | 28.000000 | 3.79 | 2.450000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 14.280000 | 33.140000 | 31.000000 | 1007.000000 |  | 33.760000 | 1.970000 | 10000.000000 | 36.000000 | 3.65 | 2.310000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 22:00:00 | 60.000000 | 16.960000 | 31.780000 | 42.000000 | 1007.000000 |  | 31.410000 | 0.430000 | 10000.000000 | 51.000000 | 3.76 | 1.530000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135010 | "ARARACUARA [44135010]" | -0.616361 | -72.381917 | 150.000000 | Climática Principal | Convencional | Activa | 1979-03-15 00:00:00 | NaT | Caquetá | Solano | Caqueta | Area Operativa 04 - Huila-Caquetá | Amazonas | Caquetá | Río Caqueta Bajo | America/Bogota | 2022-01-10 23:00:00 | 58.000000 | 16.610000 | 27.600000 | 53.000000 | 1007.000000 |  | 27.000000 | 0.000000 | 10000.000000 | 70.000000 | 1.18 | 1.150000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station44135010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44135010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44135010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135010_OWM_Windspeed_20220111.png)
