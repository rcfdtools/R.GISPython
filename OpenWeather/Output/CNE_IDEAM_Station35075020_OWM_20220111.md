
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SUTATENZA [35075020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35075020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.02227778,-73.44916667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.02227778&lon=-73.44916667)


| Parameter | Value |
|---|---|
| Code | 35075020 |
| Name | SUTATENZA [35075020] |
| Latitude, ° | 5.02227778 |
| Longitude, ° | -73.44916667 |
| Elevation, m | 1930 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1969-01-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Sutatenza |
| Stream | Sabandija |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Garagoa |

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

### (CNE index 2260) Open Weather values for station 35075020 - SUTATENZA [35075020]

JSON data from API OWM:

```
{'lat': 5.0223, 'lon': -73.4492, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812738, 'sunset': 1641855396, 'temp': 20.03, 'feels_like': 19.89, 'pressure': 1012, 'humidity': 69, 'dew_point': 14.17, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 122, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.24, 'feels_like': 15.33, 'pressure': 1016, 'humidity': 96, 'dew_point': 14.61, 'uvi': 0, 'clouds': 99, 'visibility': 4911, 'wind_speed': 0.44, 'wind_deg': 117, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 15.14, 'feels_like': 15.22, 'pressure': 1017, 'humidity': 96, 'dew_point': 14.51, 'uvi': 0, 'clouds': 100, 'visibility': 6349, 'wind_speed': 0.17, 'wind_deg': 152, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 15.13, 'feels_like': 15.18, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 160, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 15.14, 'feels_like': 15.16, 'pressure': 1018, 'humidity': 94, 'dew_point': 14.18, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 184, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 14.93, 'feels_like': 14.96, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.14, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 187, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 14.93, 'feels_like': 14.96, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.14, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 170, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.97, 'feels_like': 15, 'pressure': 1016, 'humidity': 95, 'dew_point': 14.18, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 151, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.55, 'feels_like': 14.57, 'pressure': 1015, 'humidity': 96, 'dew_point': 13.92, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 228, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14.21, 'feels_like': 14.14, 'pressure': 1015, 'humidity': 94, 'dew_point': 13.26, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 290, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 13.71, 'feels_like': 13.62, 'pressure': 1015, 'humidity': 95, 'dew_point': 12.92, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 293, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 13.19, 'feels_like': 13.05, 'pressure': 1016, 'humidity': 95, 'dew_point': 12.41, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 275, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 13.15, 'feels_like': 13, 'pressure': 1017, 'humidity': 95, 'dew_point': 12.37, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 274, 'wind_gust': 0.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 15.01, 'feels_like': 14.84, 'pressure': 1017, 'humidity': 87, 'dew_point': 12.87, 'uvi': 0.61, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 267, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.15, 'feels_like': 16.93, 'pressure': 1018, 'humidity': 77, 'dew_point': 13.09, 'uvi': 2.53, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 140, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 19.57, 'feels_like': 19.28, 'pressure': 1018, 'humidity': 65, 'dew_point': 12.82, 'uvi': 5.9, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 116, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.82, 'feels_like': 21.52, 'pressure': 1016, 'humidity': 56, 'dew_point': 12.66, 'uvi': 9.82, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 113, 'wind_gust': 2.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 22.28, 'feels_like': 21.97, 'pressure': 1015, 'humidity': 54, 'dew_point': 12.53, 'uvi': 12.42, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.88, 'wind_deg': 114, 'wind_gust': 2.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 20.85, 'feels_like': 20.61, 'pressure': 1015, 'humidity': 62, 'dew_point': 13.31, 'uvi': 13.35, 'clouds': 81, 'visibility': 10000, 'wind_speed': 3.07, 'wind_deg': 122, 'wind_gust': 2.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 20.56, 'feels_like': 20.37, 'pressure': 1014, 'humidity': 65, 'dew_point': 13.76, 'uvi': 11.96, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.43, 'wind_deg': 121, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 19.65, 'feels_like': 19.47, 'pressure': 1013, 'humidity': 69, 'dew_point': 13.81, 'uvi': 7.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 121, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 20.03, 'feels_like': 19.89, 'pressure': 1012, 'humidity': 69, 'dew_point': 14.17, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 122, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 18.33, 'feels_like': 18.28, 'pressure': 1013, 'humidity': 79, 'dew_point': 14.63, 'uvi': 1.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 121, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641852000, 'temp': 17.31, 'feels_like': 17.32, 'pressure': 1014, 'humidity': 85, 'dew_point': 14.77, 'uvi': 0.29, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 122, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641855600, 'temp': 15.92, 'feels_like': 16, 'pressure': 1015, 'humidity': 93, 'dew_point': 14.79, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 125, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 00:00:00 | 99.000000 | 14.610000 | 15.330000 | 96.000000 | 1016.000000 |  | 15.240000 | 0.000000 | 4911.000000 | 117.000000 | 0.96 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 14.510000 | 15.220000 | 96.000000 | 1017.000000 |  | 15.140000 | 0.000000 | 6349.000000 | 152.000000 | 0.68 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 14.340000 | 15.180000 | 95.000000 | 1018.000000 |  | 15.130000 | 0.000000 | 10000.000000 | 160.000000 | 1.04 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 14.180000 | 15.160000 | 94.000000 | 1018.000000 |  | 15.140000 | 0.000000 | 10000.000000 | 184.000000 | 0.76 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 14.140000 | 14.960000 | 95.000000 | 1018.000000 |  | 14.930000 | 0.000000 | 10000.000000 | 187.000000 | 0.81 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 14.140000 | 14.960000 | 95.000000 | 1018.000000 |  | 14.930000 | 0.000000 | 10000.000000 | 170.000000 | 0.88 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 14.180000 | 15.000000 | 95.000000 | 1016.000000 |  | 14.970000 | 0.000000 | 10000.000000 | 151.000000 | 0.73 | 0.240000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 13.920000 | 14.570000 | 96.000000 | 1015.000000 |  | 14.550000 | 0.000000 | 10000.000000 | 228.000000 | 0.63 | 0.470000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 13.260000 | 14.140000 | 94.000000 | 1015.000000 |  | 14.210000 | 0.000000 | 10000.000000 | 290.000000 | 0.56 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 09:00:00 | 93.000000 | 12.920000 | 13.620000 | 95.000000 | 1015.000000 |  | 13.710000 | 0.000000 | 10000.000000 | 293.000000 | 0.54 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 10:00:00 | 85.000000 | 12.410000 | 13.050000 | 95.000000 | 1016.000000 |  | 13.190000 | 0.000000 | 10000.000000 | 275.000000 | 0.71 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 11:00:00 | 79.000000 | 12.370000 | 13.000000 | 95.000000 | 1017.000000 |  | 13.150000 | 0.000000 | 10000.000000 | 274.000000 | 0.96 | 1.020000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 12:00:00 | 56.000000 | 12.870000 | 14.840000 | 87.000000 | 1017.000000 |  | 15.010000 | 0.610000 | 10000.000000 | 267.000000 | 0.76 | 0.420000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 13:00:00 | 90.000000 | 13.090000 | 16.930000 | 77.000000 | 1018.000000 |  | 17.150000 | 2.530000 | 10000.000000 | 140.000000 | 0.68 | 0.600000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 14:00:00 | 86.000000 | 12.820000 | 19.280000 | 65.000000 | 1018.000000 |  | 19.570000 | 5.900000 | 10000.000000 | 116.000000 | 1.04 | 1.450000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 15:00:00 | 74.000000 | 12.660000 | 21.520000 | 56.000000 | 1016.000000 |  | 21.820000 | 9.820000 | 10000.000000 | 113.000000 | 2.27 | 2.190000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 12.530000 | 21.970000 | 54.000000 | 1015.000000 |  | 22.280000 | 12.420000 | 10000.000000 | 114.000000 | 2.85 | 2.880000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 17:00:00 | 81.000000 | 13.310000 | 20.610000 | 62.000000 | 1015.000000 |  | 20.850000 | 13.350000 | 10000.000000 | 122.000000 | 2.67 | 3.070000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 18:00:00 | 94.000000 | 13.760000 | 20.370000 | 65.000000 | 1014.000000 |  | 20.560000 | 11.960000 | 10000.000000 | 121.000000 | 1.85 | 2.430000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.810000 | 19.470000 | 69.000000 | 1013.000000 |  | 19.650000 | 7.260000 | 10000.000000 | 121.000000 | 1.74 | 2.130000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 14.170000 | 19.890000 | 69.000000 | 1012.000000 |  | 20.030000 | 4.130000 | 10000.000000 | 122.000000 | 1.72 | 2.280000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 14.630000 | 18.280000 | 79.000000 | 1013.000000 | 0.15 | 18.330000 | 1.610000 | 10000.000000 | 121.000000 | 2.38 | 2.140000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 14.770000 | 17.320000 | 85.000000 | 1014.000000 | 0.13 | 17.310000 | 0.290000 | 10000.000000 | 122.000000 | 2.06 | 1.780000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075020 | "SUTATENZA [35075020]" | 5.022278 | -73.449167 | 1930.000000 | Climática Principal | Convencional | Activa | 1969-01-15 00:00:00 | NaT | Boyacá | Sutatenza | Sabandija | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 14.790000 | 16.000000 | 93.000000 | 1015.000000 |  | 15.920000 | 0.000000 | 10000.000000 | 125.000000 | 2.05 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35075020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35075020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35075020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075020_OWM_Windspeed_20220111.png)
