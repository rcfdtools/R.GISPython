
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CHIRIBIQUETE - AUT [44135030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44135030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=-0.07416667,-72.45138889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=-0.07416667&lon=-72.45138889)


| Parameter | Value |
|---|---|
| Code | 44135030 |
| Name | CHIRIBIQUETE - AUT [44135030] |
| Latitude, ° | -0.07416667 |
| Longitude, ° | -72.45138889 |
| Elevation, m | 256 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2006-02-04 00:00:00 |
| Suspension date | 2011-07-29 00:00:00 |
| State | Caquetá |
| County | Solano |
| Stream | Amazonas |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Yarí |
| SZH - Hydrographic subzone | Río Mesay |

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

### (CNE index 7) Open Weather values for station 44135030 - CHIRIBIQUETE - AUT [44135030]

JSON data from API OWM:

```
{'lat': -0.0742, 'lon': -72.4514, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812006, 'sunset': 1641855650, 'temp': 34.28, 'feels_like': 33.49, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.7, 'uvi': 4.87, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 30, 'wind_gust': 3.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.59, 'feels_like': 25.67, 'pressure': 1008, 'humidity': 56, 'dew_point': 16.17, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 63, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 24.67, 'feels_like': 24.73, 'pressure': 1009, 'humidity': 59, 'dew_point': 16.13, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 81, 'wind_gust': 1.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.77, 'feels_like': 23.85, 'pressure': 1010, 'humidity': 63, 'dew_point': 16.31, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 80, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.2, 'feels_like': 23.33, 'pressure': 1011, 'humidity': 67, 'dew_point': 16.74, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 72, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.71, 'feels_like': 22.86, 'pressure': 1011, 'humidity': 70, 'dew_point': 16.96, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 3, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.68, 'feels_like': 22.86, 'pressure': 1011, 'humidity': 71, 'dew_point': 17.16, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 24, 'wind_gust': 1.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.87, 'feels_like': 23.01, 'pressure': 1010, 'humidity': 69, 'dew_point': 16.89, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 43, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.88, 'feels_like': 22.03, 'pressure': 1010, 'humidity': 73, 'dew_point': 16.83, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 35, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.22, 'feels_like': 21.36, 'pressure': 1009, 'humidity': 75, 'dew_point': 16.61, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 33, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.7, 'feels_like': 20.84, 'pressure': 1010, 'humidity': 77, 'dew_point': 16.53, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 38, 'wind_gust': 3.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.29, 'feels_like': 20.44, 'pressure': 1010, 'humidity': 79, 'dew_point': 16.53, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 43, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.92, 'feels_like': 20.06, 'pressure': 1011, 'humidity': 80, 'dew_point': 16.37, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 49, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 22.01, 'feels_like': 22.2, 'pressure': 1012, 'humidity': 74, 'dew_point': 17.17, 'uvi': 0.77, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 32, 'wind_gust': 7.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.35, 'feels_like': 25.48, 'pressure': 1013, 'humidity': 59, 'dew_point': 16.76, 'uvi': 2.72, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 26, 'wind_gust': 7.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.23, 'feels_like': 28.62, 'pressure': 1014, 'humidity': 49, 'dew_point': 16.51, 'uvi': 5.95, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 28, 'wind_gust': 7.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 30.53, 'feels_like': 30.45, 'pressure': 1013, 'humidity': 41, 'dew_point': 15.79, 'uvi': 9.5, 'clouds': 74, 'visibility': 10000, 'wind_speed': 3.08, 'wind_deg': 30, 'wind_gust': 6.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 32.3, 'feels_like': 31.86, 'pressure': 1012, 'humidity': 35, 'dew_point': 14.89, 'uvi': 12.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.14, 'wind_deg': 27, 'wind_gust': 6.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.56, 'feels_like': 32.87, 'pressure': 1010, 'humidity': 31, 'dew_point': 14.11, 'uvi': 13.07, 'clouds': 77, 'visibility': 10000, 'wind_speed': 3.23, 'wind_deg': 26, 'wind_gust': 5.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 34.09, 'feels_like': 33.23, 'pressure': 1009, 'humidity': 29, 'dew_point': 13.54, 'uvi': 11.6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.94, 'wind_deg': 27, 'wind_gust': 4.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.41, 'feels_like': 33.66, 'pressure': 1008, 'humidity': 29, 'dew_point': 13.81, 'uvi': 8.51, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 29, 'wind_gust': 4.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 34.28, 'feels_like': 33.49, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.7, 'uvi': 4.87, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.29, 'wind_deg': 30, 'wind_gust': 3.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.66, 'feels_like': 33, 'pressure': 1006, 'humidity': 31, 'dew_point': 14.2, 'uvi': 1.94, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 38, 'wind_gust': 3.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 31.4, 'feels_like': 31.77, 'pressure': 1006, 'humidity': 42, 'dew_point': 16.95, 'uvi': 0.42, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 60, 'wind_gust': 3.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.18, 'feels_like': 27.72, 'pressure': 1007, 'humidity': 52, 'dew_point': 16.48, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 74, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 00:00:00 | 80.000000 | 16.170000 | 25.670000 | 56.000000 | 1008.000000 |  | 25.590000 | 0.000000 | 10000.000000 | 63.000000 | 1.21 | 1.170000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 01:00:00 | 89.000000 | 16.130000 | 24.730000 | 59.000000 | 1009.000000 |  | 24.670000 | 0.000000 | 10000.000000 | 81.000000 | 1.28 | 1.260000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 02:00:00 | 93.000000 | 16.310000 | 23.850000 | 63.000000 | 1010.000000 |  | 23.770000 | 0.000000 | 10000.000000 | 80.000000 | 1.38 | 1.130000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 03:00:00 | 92.000000 | 16.740000 | 23.330000 | 67.000000 | 1011.000000 |  | 23.200000 | 0.000000 | 10000.000000 | 72.000000 | 0.81 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 04:00:00 | 80.000000 | 16.960000 | 22.860000 | 70.000000 | 1011.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 3.000000 | 0.9 | 0.790000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 05:00:00 | 76.000000 | 17.160000 | 22.860000 | 71.000000 | 1011.000000 |  | 22.680000 | 0.000000 | 10000.000000 | 24.000000 | 1.57 | 0.950000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 06:00:00 | 73.000000 | 16.890000 | 23.010000 | 69.000000 | 1010.000000 |  | 22.870000 | 0.000000 | 10000.000000 | 43.000000 | 1.63 | 0.900000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 07:00:00 | 86.000000 | 16.830000 | 22.030000 | 73.000000 | 1010.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 35.000000 | 1.82 | 1.030000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 16.610000 | 21.360000 | 75.000000 | 1009.000000 |  | 21.220000 | 0.000000 | 10000.000000 | 33.000000 | 2.29 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 09:00:00 | 85.000000 | 16.530000 | 20.840000 | 77.000000 | 1010.000000 |  | 20.700000 | 0.000000 | 10000.000000 | 38.000000 | 3.18 | 1.200000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 16.530000 | 20.440000 | 79.000000 | 1010.000000 |  | 20.290000 | 0.000000 | 10000.000000 | 43.000000 | 1.66 | 1.120000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 11:00:00 | 89.000000 | 16.370000 | 20.060000 | 80.000000 | 1011.000000 |  | 19.920000 | 0.000000 | 10000.000000 | 49.000000 | 1.2 | 0.970000 | 804 | Clouds | overcast clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 12:00:00 | 87.000000 | 17.170000 | 22.200000 | 74.000000 | 1012.000000 |  | 22.010000 | 0.770000 | 10000.000000 | 32.000000 | 7.49 | 1.190000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 13:00:00 | 84.000000 | 16.760000 | 25.480000 | 59.000000 | 1013.000000 |  | 25.350000 | 2.720000 | 10000.000000 | 26.000000 | 7.75 | 2.390000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 14:00:00 | 71.000000 | 16.510000 | 28.620000 | 49.000000 | 1014.000000 |  | 28.230000 | 5.950000 | 10000.000000 | 28.000000 | 7.71 | 2.780000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 15:00:00 | 74.000000 | 15.790000 | 30.450000 | 41.000000 | 1013.000000 |  | 30.530000 | 9.500000 | 10000.000000 | 30.000000 | 6.83 | 3.080000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 14.890000 | 31.860000 | 35.000000 | 1012.000000 |  | 32.300000 | 12.330000 | 10000.000000 | 27.000000 | 6.39 | 3.140000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 17:00:00 | 77.000000 | 14.110000 | 32.870000 | 31.000000 | 1010.000000 |  | 33.560000 | 13.070000 | 10000.000000 | 26.000000 | 5.82 | 3.230000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 13.540000 | 33.230000 | 29.000000 | 1009.000000 |  | 34.090000 | 11.600000 | 10000.000000 | 27.000000 | 4.95 | 2.940000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 13.810000 | 33.660000 | 29.000000 | 1008.000000 |  | 34.410000 | 8.510000 | 10000.000000 | 29.000000 | 4.36 | 2.650000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 13.700000 | 33.490000 | 29.000000 | 1007.000000 |  | 34.280000 | 4.870000 | 10000.000000 | 30.000000 | 3.9 | 2.290000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 21:00:00 | 97.000000 | 14.200000 | 33.000000 | 31.000000 | 1006.000000 |  | 33.660000 | 1.940000 | 10000.000000 | 38.000000 | 3.8 | 2.200000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 16.950000 | 31.770000 | 42.000000 | 1006.000000 |  | 31.400000 | 0.420000 | 10000.000000 | 60.000000 | 3.54 | 1.470000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44135030 | "CHIRIBIQUETE - AUT [44135030]" | -0.074167 | -72.451389 | 256.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2006-02-04 00:00:00 | 2011-07-29 00:00:00 | Caquetá | Solano | Amazonas | Area Operativa 04 - Huila-Caquetá | Amazonas | Yarí | Río Mesay | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 16.480000 | 27.720000 | 52.000000 | 1007.000000 |  | 27.180000 | 0.000000 | 10000.000000 | 74.000000 | 1.25 | 1.220000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station44135030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44135030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44135030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44135030_OWM_Windspeed_20220111.png)
