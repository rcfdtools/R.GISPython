
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO YOPAL - AUT [35215020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35215020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.32044444,-72.3875) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.32044444&lon=-72.3875)


| Parameter | Value |
|---|---|
| Code | 35215020 |
| Name | AEROPUERTO YOPAL - AUT [35215020] |
| Latitude, ° | 5.32044444 |
| Longitude, ° | -72.3875 |
| Elevation, m | 325 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-11-17 00:00:00 |
| Suspension date | NaT |
| State | Casanare |
| County | Yopal |
| Stream | Bogota |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Cravo Sur |

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

### (CNE index 121) Open Weather values for station 35215020 - AEROPUERTO YOPAL - AUT [35215020]

JSON data from API OWM:

```
{'lat': 5.3204, 'lon': -72.3875, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812512, 'sunset': 1641855112, 'temp': 31.22, 'feels_like': 31.05, 'pressure': 1008, 'humidity': 39, 'dew_point': 15.63, 'uvi': 2.08, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.91, 'wind_deg': 50, 'wind_gust': 4.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.76, 'feels_like': 27.31, 'pressure': 1011, 'humidity': 52, 'dew_point': 16.09, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 35, 'wind_gust': 5.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.26, 'feels_like': 26.26, 'pressure': 1012, 'humidity': 54, 'dew_point': 16.22, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 30, 'wind_gust': 5.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.67, 'feels_like': 25.73, 'pressure': 1013, 'humidity': 55, 'dew_point': 15.96, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 19, 'wind_gust': 4.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.25, 'feels_like': 25.29, 'pressure': 1013, 'humidity': 56, 'dew_point': 15.85, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 0, 'wind_gust': 3.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.24, 'feels_like': 25.31, 'pressure': 1013, 'humidity': 57, 'dew_point': 16.12, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 343, 'wind_gust': 2.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.92, 'feels_like': 24.98, 'pressure': 1012, 'humidity': 58, 'dew_point': 16.09, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 340, 'wind_gust': 2.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.3, 'feels_like': 24.35, 'pressure': 1012, 'humidity': 60, 'dew_point': 16.04, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 358, 'wind_gust': 1.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.04, 'feels_like': 24.09, 'pressure': 1011, 'humidity': 61, 'dew_point': 16.06, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 12, 'wind_gust': 2.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.95, 'feels_like': 23.99, 'pressure': 1011, 'humidity': 61, 'dew_point': 15.97, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 17, 'wind_gust': 2.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.95, 'feels_like': 23.99, 'pressure': 1011, 'humidity': 61, 'dew_point': 15.97, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 27, 'wind_gust': 3.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.9, 'feels_like': 23.94, 'pressure': 1011, 'humidity': 61, 'dew_point': 15.93, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 29, 'wind_gust': 3.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.71, 'feels_like': 23.73, 'pressure': 1012, 'humidity': 61, 'dew_point': 15.75, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 36, 'wind_gust': 3.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.34, 'feels_like': 24.37, 'pressure': 1014, 'humidity': 59, 'dew_point': 15.82, 'uvi': 0.29, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 55, 'wind_gust': 4.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.44, 'feels_like': 25.48, 'pressure': 1015, 'humidity': 55, 'dew_point': 15.75, 'uvi': 1.55, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 52, 'wind_gust': 5.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.1, 'feels_like': 27.45, 'pressure': 1016, 'humidity': 49, 'dew_point': 15.47, 'uvi': 3.51, 'clouds': 95, 'visibility': 10000, 'wind_speed': 3.33, 'wind_deg': 54, 'wind_gust': 6.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.77, 'feels_like': 28.74, 'pressure': 1015, 'humidity': 44, 'dew_point': 15.31, 'uvi': 5.74, 'clouds': 91, 'visibility': 10000, 'wind_speed': 4.04, 'wind_deg': 60, 'wind_gust': 5.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 30.66, 'feels_like': 30.35, 'pressure': 1014, 'humidity': 39, 'dew_point': 15.13, 'uvi': 8.04, 'clouds': 88, 'visibility': 10000, 'wind_speed': 4.07, 'wind_deg': 63, 'wind_gust': 4.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 32.09, 'feels_like': 31.74, 'pressure': 1013, 'humidity': 36, 'dew_point': 15.15, 'uvi': 8.53, 'clouds': 83, 'visibility': 10000, 'wind_speed': 4.07, 'wind_deg': 70, 'wind_gust': 4.36, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.68, 'feels_like': 31.5, 'pressure': 1011, 'humidity': 38, 'dew_point': 15.63, 'uvi': 7.54, 'clouds': 96, 'visibility': 10000, 'wind_speed': 3.89, 'wind_deg': 65, 'wind_gust': 4.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.79, 'feels_like': 31.65, 'pressure': 1010, 'humidity': 38, 'dew_point': 15.73, 'uvi': 3.75, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.89, 'wind_deg': 60, 'wind_gust': 4.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.22, 'feels_like': 31.05, 'pressure': 1008, 'humidity': 39, 'dew_point': 15.63, 'uvi': 2.08, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.91, 'wind_deg': 50, 'wind_gust': 4.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.55, 'feels_like': 30.48, 'pressure': 1008, 'humidity': 41, 'dew_point': 15.81, 'uvi': 0.8, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.64, 'wind_deg': 41, 'wind_gust': 4.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.84, 'feels_like': 29.86, 'pressure': 1009, 'humidity': 43, 'dew_point': 15.92, 'uvi': 0.2, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 35, 'wind_gust': 4.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.78, 'feels_like': 28.05, 'pressure': 1010, 'humidity': 48, 'dew_point': 15.77, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 21, 'wind_gust': 4.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 00:00:00 | 90.000000 | 16.090000 | 27.310000 | 52.000000 | 1011.000000 |  | 26.760000 | 0.000000 | 10000.000000 | 35.000000 | 5.35 | 2.100000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 16.220000 | 26.260000 | 54.000000 | 1012.000000 |  | 26.260000 | 0.000000 | 10000.000000 | 30.000000 | 5.53 | 2.080000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 02:00:00 | 97.000000 | 15.960000 | 25.730000 | 55.000000 | 1013.000000 |  | 25.670000 | 0.000000 | 10000.000000 | 19.000000 | 4.91 | 1.830000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 03:00:00 | 97.000000 | 15.850000 | 25.290000 | 56.000000 | 1013.000000 |  | 25.250000 | 0.000000 | 10000.000000 | 0.000000 | 3.72 | 1.600000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 16.120000 | 25.310000 | 57.000000 | 1013.000000 |  | 25.240000 | 0.000000 | 10000.000000 | 343.000000 | 2.89 | 1.420000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 05:00:00 | 96.000000 | 16.090000 | 24.980000 | 58.000000 | 1012.000000 |  | 24.920000 | 0.000000 | 10000.000000 | 340.000000 | 2.02 | 1.280000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 06:00:00 | 84.000000 | 16.040000 | 24.350000 | 60.000000 | 1012.000000 |  | 24.300000 | 0.000000 | 10000.000000 | 358.000000 | 1.58 | 1.120000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 07:00:00 | 93.000000 | 16.060000 | 24.090000 | 61.000000 | 1011.000000 |  | 24.040000 | 0.000000 | 10000.000000 | 12.000000 | 2.25 | 1.250000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 08:00:00 | 93.000000 | 15.970000 | 23.990000 | 61.000000 | 1011.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 17.000000 | 2.68 | 1.310000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 09:00:00 | 94.000000 | 15.970000 | 23.990000 | 61.000000 | 1011.000000 |  | 23.950000 | 0.000000 | 10000.000000 | 27.000000 | 3.01 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 10:00:00 | 94.000000 | 15.930000 | 23.940000 | 61.000000 | 1011.000000 |  | 23.900000 | 0.000000 | 10000.000000 | 29.000000 | 3.04 | 1.070000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 11:00:00 | 94.000000 | 15.750000 | 23.730000 | 61.000000 | 1012.000000 |  | 23.710000 | 0.000000 | 10000.000000 | 36.000000 | 3.29 | 1.130000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 12:00:00 | 84.000000 | 15.820000 | 24.370000 | 59.000000 | 1014.000000 |  | 24.340000 | 0.290000 | 10000.000000 | 55.000000 | 4.37 | 1.510000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 13:00:00 | 92.000000 | 15.750000 | 25.480000 | 55.000000 | 1015.000000 |  | 25.440000 | 1.550000 | 10000.000000 | 52.000000 | 5.84 | 2.110000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 14:00:00 | 95.000000 | 15.470000 | 27.450000 | 49.000000 | 1016.000000 |  | 27.100000 | 3.510000 | 10000.000000 | 54.000000 | 6.43 | 3.330000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 15:00:00 | 91.000000 | 15.310000 | 28.740000 | 44.000000 | 1015.000000 |  | 28.770000 | 5.740000 | 10000.000000 | 60.000000 | 5.84 | 4.040000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 15.130000 | 30.350000 | 39.000000 | 1014.000000 |  | 30.660000 | 8.040000 | 10000.000000 | 63.000000 | 4.95 | 4.070000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 17:00:00 | 83.000000 | 15.150000 | 31.740000 | 36.000000 | 1013.000000 |  | 32.090000 | 8.530000 | 10000.000000 | 70.000000 | 4.36 | 4.070000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 18:00:00 | 96.000000 | 15.630000 | 31.500000 | 38.000000 | 1011.000000 |  | 31.680000 | 7.540000 | 10000.000000 | 65.000000 | 4.23 | 3.890000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 15.730000 | 31.650000 | 38.000000 | 1010.000000 |  | 31.790000 | 3.750000 | 10000.000000 | 60.000000 | 4.16 | 3.890000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 15.630000 | 31.050000 | 39.000000 | 1008.000000 |  | 31.220000 | 2.080000 | 10000.000000 | 50.000000 | 4.39 | 3.910000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 15.810000 | 30.480000 | 41.000000 | 1008.000000 |  | 30.550000 | 0.800000 | 10000.000000 | 41.000000 | 4.36 | 3.640000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 15.920000 | 29.860000 | 43.000000 | 1009.000000 |  | 29.840000 | 0.200000 | 10000.000000 | 35.000000 | 4.17 | 2.860000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35215020 | "AEROPUERTO YOPAL - AUT [35215020]" | 5.320444 | -72.387500 | 325.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-17 00:00:00 | NaT | Casanare | Yopal | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Cravo Sur | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 15.770000 | 28.050000 | 48.000000 | 1010.000000 |  | 27.780000 | 0.000000 | 10000.000000 | 21.000000 | 4.29 | 1.950000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35215020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35215020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35215020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35215020_OWM_Windspeed_20220111.png)
