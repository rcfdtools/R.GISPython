
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CEJALITO [35135010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35135010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.71666667,-72.35) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.71666667&lon=-72.35)


| Parameter | Value |
|---|---|
| Code | 35135010 |
| Name | CEJALITO [35135010] |
| Latitude, ° | 3.71666667 |
| Longitude, ° | -72.35 |
| Elevation, m | 200 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1976-05-15 00:00:00 |
| Suspension date | 1984-12-15 00:00:00 |
| State | Meta |
| County | San Martín (Meta) |
| Stream | Cno Camoa |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Manacacias |

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

### (CNE index 2220) Open Weather values for station 35135010 - CEJALITO [35135010]

JSON data from API OWM:

```
{'lat': 3.7167, 'lon': -72.35, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812348, 'sunset': 1641855259, 'temp': 33.12, 'feels_like': 32.45, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.22, 'uvi': 4.37, 'clouds': 7, 'visibility': 10000, 'wind_speed': 6.45, 'wind_deg': 30, 'wind_gust': 7.38, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 30.3, 'feels_like': 29.92, 'pressure': 1009, 'humidity': 39, 'dew_point': 14.81, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 6.13, 'wind_deg': 12, 'wind_gust': 10.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 29.23, 'feels_like': 28.94, 'pressure': 1010, 'humidity': 41, 'dew_point': 14.63, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 5.78, 'wind_deg': 11, 'wind_gust': 11.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 28.96, 'feels_like': 28.66, 'pressure': 1011, 'humidity': 41, 'dew_point': 14.39, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 5.43, 'wind_deg': 19, 'wind_gust': 11.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 28.9, 'feels_like': 28.69, 'pressure': 1011, 'humidity': 42, 'dew_point': 14.71, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 5.52, 'wind_deg': 33, 'wind_gust': 11.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 28.11, 'feels_like': 28.06, 'pressure': 1011, 'humidity': 44, 'dew_point': 14.72, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 4.55, 'wind_deg': 30, 'wind_gust': 10.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 27.61, 'feels_like': 27.66, 'pressure': 1011, 'humidity': 45, 'dew_point': 14.62, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 4.16, 'wind_deg': 24, 'wind_gust': 10.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.68, 'feels_like': 25.64, 'pressure': 1010, 'humidity': 51, 'dew_point': 14.79, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 29, 'wind_gust': 8.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 25.05, 'feels_like': 24.99, 'pressure': 1010, 'humidity': 53, 'dew_point': 14.81, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 3.25, 'wind_deg': 31, 'wind_gust': 9.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 25.23, 'feels_like': 25.17, 'pressure': 1009, 'humidity': 52, 'dew_point': 14.68, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 3.61, 'wind_deg': 33, 'wind_gust': 9.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 25.06, 'feels_like': 25.01, 'pressure': 1010, 'humidity': 53, 'dew_point': 14.82, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 4.17, 'wind_deg': 33, 'wind_gust': 10.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.68, 'feels_like': 24.59, 'pressure': 1010, 'humidity': 53, 'dew_point': 14.47, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 4.41, 'wind_deg': 35, 'wind_gust': 10.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 24.19, 'feels_like': 24.07, 'pressure': 1011, 'humidity': 54, 'dew_point': 14.3, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 4.08, 'wind_deg': 38, 'wind_gust': 10.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 24.64, 'feels_like': 24.54, 'pressure': 1013, 'humidity': 53, 'dew_point': 14.43, 'uvi': 0.3, 'clouds': 89, 'visibility': 10000, 'wind_speed': 4.26, 'wind_deg': 34, 'wind_gust': 10.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.26, 'feels_like': 26.26, 'pressure': 1014, 'humidity': 48, 'dew_point': 14.39, 'uvi': 1.21, 'clouds': 96, 'visibility': 10000, 'wind_speed': 5.33, 'wind_deg': 28, 'wind_gust': 10.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.03, 'feels_like': 27.98, 'pressure': 1015, 'humidity': 44, 'dew_point': 14.65, 'uvi': 2.7, 'clouds': 93, 'visibility': 10000, 'wind_speed': 6.61, 'wind_deg': 32, 'wind_gust': 10.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.65, 'feels_like': 28.43, 'pressure': 1014, 'humidity': 42, 'dew_point': 14.48, 'uvi': 4.38, 'clouds': 93, 'visibility': 10000, 'wind_speed': 7.18, 'wind_deg': 27, 'wind_gust': 10.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.27, 'feels_like': 28.98, 'pressure': 1014, 'humidity': 41, 'dew_point': 14.67, 'uvi': 11.07, 'clouds': 92, 'visibility': 10000, 'wind_speed': 7.15, 'wind_deg': 23, 'wind_gust': 9.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.07, 'feels_like': 29.66, 'pressure': 1012, 'humidity': 39, 'dew_point': 14.61, 'uvi': 11.77, 'clouds': 90, 'visibility': 10000, 'wind_speed': 7.29, 'wind_deg': 25, 'wind_gust': 9.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.71, 'feels_like': 30.28, 'pressure': 1011, 'humidity': 38, 'dew_point': 14.77, 'uvi': 10.42, 'clouds': 6, 'visibility': 10000, 'wind_speed': 7.14, 'wind_deg': 30, 'wind_gust': 9.02, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 32.71, 'feels_like': 32.08, 'pressure': 1009, 'humidity': 33, 'dew_point': 14.34, 'uvi': 7.77, 'clouds': 8, 'visibility': 10000, 'wind_speed': 6.93, 'wind_deg': 30, 'wind_gust': 8.23, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641844800, 'temp': 33.12, 'feels_like': 32.45, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.22, 'uvi': 4.37, 'clouds': 7, 'visibility': 10000, 'wind_speed': 6.45, 'wind_deg': 30, 'wind_gust': 7.38, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641848400, 'temp': 32.96, 'feels_like': 32.25, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.08, 'uvi': 1.68, 'clouds': 10, 'visibility': 10000, 'wind_speed': 5.86, 'wind_deg': 27, 'wind_gust': 6.76, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641852000, 'temp': 32.11, 'feels_like': 31.61, 'pressure': 1007, 'humidity': 35, 'dew_point': 14.73, 'uvi': 0.32, 'clouds': 22, 'visibility': 10000, 'wind_speed': 5.74, 'wind_deg': 17, 'wind_gust': 6.83, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641855600, 'temp': 29.71, 'feels_like': 29.36, 'pressure': 1008, 'humidity': 40, 'dew_point': 14.68, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 4.99, 'wind_deg': 4, 'wind_gust': 9.08, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 00:00:00 | 74.000000 | 14.810000 | 29.920000 | 39.000000 | 1009.000000 |  | 30.300000 | 0.000000 | 10000.000000 | 12.000000 | 10.07 | 6.130000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 01:00:00 | 83.000000 | 14.630000 | 28.940000 | 41.000000 | 1010.000000 |  | 29.230000 | 0.000000 | 10000.000000 | 11.000000 | 11.15 | 5.780000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 02:00:00 | 90.000000 | 14.390000 | 28.660000 | 41.000000 | 1011.000000 |  | 28.960000 | 0.000000 | 10000.000000 | 19.000000 | 11.38 | 5.430000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 03:00:00 | 93.000000 | 14.710000 | 28.690000 | 42.000000 | 1011.000000 |  | 28.900000 | 0.000000 | 10000.000000 | 33.000000 | 11.18 | 5.520000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 14.720000 | 28.060000 | 44.000000 | 1011.000000 |  | 28.110000 | 0.000000 | 10000.000000 | 30.000000 | 10.73 | 4.550000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 14.620000 | 27.660000 | 45.000000 | 1011.000000 |  | 27.610000 | 0.000000 | 10000.000000 | 24.000000 | 10.51 | 4.160000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 06:00:00 | 50.000000 | 14.790000 | 25.640000 | 51.000000 | 1010.000000 |  | 25.680000 | 0.000000 | 10000.000000 | 29.000000 | 8.55 | 3.280000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 07:00:00 | 67.000000 | 14.810000 | 24.990000 | 53.000000 | 1010.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 31.000000 | 9.03 | 3.250000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 08:00:00 | 81.000000 | 14.680000 | 25.170000 | 52.000000 | 1009.000000 |  | 25.230000 | 0.000000 | 10000.000000 | 33.000000 | 9.76 | 3.610000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 09:00:00 | 87.000000 | 14.820000 | 25.010000 | 53.000000 | 1010.000000 |  | 25.060000 | 0.000000 | 10000.000000 | 33.000000 | 10.52 | 4.170000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 14.470000 | 24.590000 | 53.000000 | 1010.000000 |  | 24.680000 | 0.000000 | 10000.000000 | 35.000000 | 10.88 | 4.410000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 11:00:00 | 91.000000 | 14.300000 | 24.070000 | 54.000000 | 1011.000000 |  | 24.190000 | 0.000000 | 10000.000000 | 38.000000 | 10.92 | 4.080000 | 804 | Clouds | overcast clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 12:00:00 | 89.000000 | 14.430000 | 24.540000 | 53.000000 | 1013.000000 |  | 24.640000 | 0.300000 | 10000.000000 | 34.000000 | 10.8 | 4.260000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 13:00:00 | 96.000000 | 14.390000 | 26.260000 | 48.000000 | 1014.000000 |  | 26.260000 | 1.210000 | 10000.000000 | 28.000000 | 10.87 | 5.330000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 14:00:00 | 93.000000 | 14.650000 | 27.980000 | 44.000000 | 1015.000000 |  | 28.030000 | 2.700000 | 10000.000000 | 32.000000 | 10.48 | 6.610000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 15:00:00 | 93.000000 | 14.480000 | 28.430000 | 42.000000 | 1014.000000 |  | 28.650000 | 4.380000 | 10000.000000 | 27.000000 | 10.14 | 7.180000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 16:00:00 | 92.000000 | 14.670000 | 28.980000 | 41.000000 | 1014.000000 |  | 29.270000 | 11.070000 | 10000.000000 | 23.000000 | 9.79 | 7.150000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 14.610000 | 29.660000 | 39.000000 | 1012.000000 |  | 30.070000 | 11.770000 | 10000.000000 | 25.000000 | 9.31 | 7.290000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 18:00:00 | 6.000000 | 14.770000 | 30.280000 | 38.000000 | 1011.000000 |  | 30.710000 | 10.420000 | 10000.000000 | 30.000000 | 9.02 | 7.140000 | 800 | Clear | clear sky | 01d | 18 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 19:00:00 | 8.000000 | 14.340000 | 32.080000 | 33.000000 | 1009.000000 |  | 32.710000 | 7.770000 | 10000.000000 | 30.000000 | 8.23 | 6.930000 | 800 | Clear | clear sky | 01d | 19 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 20:00:00 | 7.000000 | 14.220000 | 32.450000 | 32.000000 | 1007.000000 |  | 33.120000 | 4.370000 | 10000.000000 | 30.000000 | 7.38 | 6.450000 | 800 | Clear | clear sky | 01d | 20 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 21:00:00 | 10.000000 | 14.080000 | 32.250000 | 32.000000 | 1007.000000 |  | 32.960000 | 1.680000 | 10000.000000 | 27.000000 | 6.76 | 5.860000 | 800 | Clear | clear sky | 01d | 21 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 22:00:00 | 22.000000 | 14.730000 | 31.610000 | 35.000000 | 1007.000000 |  | 32.110000 | 0.320000 | 10000.000000 | 17.000000 | 6.83 | 5.740000 | 801 | Clouds | few clouds | 02d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35135010 | "CEJALITO [35135010]" | 3.716667 | -72.350000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1976-05-15 00:00:00 | 1984-12-15 00:00:00 | Meta | San Martín (Meta) | Cno Camoa | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 23:00:00 | 35.000000 | 14.680000 | 29.360000 | 40.000000 | 1008.000000 |  | 29.710000 | 0.000000 | 10000.000000 | 4.000000 | 9.08 | 4.990000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station35135010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35135010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35135010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35135010_OWM_Windspeed_20220111.png)
