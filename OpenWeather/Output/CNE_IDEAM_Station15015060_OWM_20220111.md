
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN LORENZO  - AUT [15015060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15015060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.11108333,-74.05469444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.11108333&lon=-74.05469444)


| Parameter | Value |
|---|---|
| Code | 15015060 |
| Name | SAN LORENZO  - AUT [15015060] |
| Latitude, ° | 11.11108333 |
| Longitude, ° | -74.05469444 |
| Elevation, m | 2200 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1969-01-14 19:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | Santa Marta |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río  Piedras - Río Manzanares |

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

### (CNE index 621) Open Weather values for station 15015060 - SAN LORENZO  - AUT [15015060]

JSON data from API OWM:

```
{'lat': 11.1111, 'lon': -74.0547, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813482, 'sunset': 1641854944, 'temp': 17.93, 'feels_like': 16.98, 'pressure': 1010, 'humidity': 46, 'dew_point': 6.16, 'uvi': 3.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 360, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 13.93, 'feels_like': 12.79, 'pressure': 1010, 'humidity': 54, 'dew_point': 4.78, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 30, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 12.93, 'feels_like': 11.77, 'pressure': 1011, 'humidity': 57, 'dew_point': 4.62, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 12.93, 'feels_like': 11.69, 'pressure': 1011, 'humidity': 54, 'dew_point': 3.85, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 12.93, 'feels_like': 11.61, 'pressure': 1012, 'humidity': 51, 'dew_point': 3.05, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 13.93, 'feels_like': 12.55, 'pressure': 1011, 'humidity': 45, 'dew_point': 2.2, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 12.93, 'feels_like': 11.51, 'pressure': 1012, 'humidity': 47, 'dew_point': 1.9, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 60, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 12.93, 'feels_like': 11.51, 'pressure': 1012, 'humidity': 47, 'dew_point': 1.9, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 60, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 11.52, 'feels_like': 10.79, 'pressure': 1013, 'humidity': 79, 'dew_point': 8.01, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.93, 'wind_deg': 94, 'wind_gust': 4.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 11.52, 'feels_like': 10.79, 'pressure': 1013, 'humidity': 79, 'dew_point': 8.01, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 95, 'wind_gust': 3.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.52, 'feels_like': 10.76, 'pressure': 1013, 'humidity': 78, 'dew_point': 7.82, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 89, 'wind_gust': 3.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.73, 'feels_like': 7.25, 'pressure': 1013, 'humidity': 78, 'dew_point': 5.11, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 90, 'wind_gust': 3.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 7.93, 'feels_like': 6.73, 'pressure': 1012, 'humidity': 73, 'dew_point': 3.39, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 90, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 7.93, 'feels_like': 7.93, 'pressure': 1013, 'humidity': 73, 'dew_point': 3.39, 'uvi': 0.28, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 11.93, 'feels_like': 10.67, 'pressure': 1014, 'humidity': 57, 'dew_point': 3.69, 'uvi': 1.51, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 11.93, 'feels_like': 10.98, 'pressure': 1015, 'humidity': 69, 'dew_point': 6.43, 'uvi': 3.79, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 12.93, 'feels_like': 12.21, 'pressure': 1015, 'humidity': 74, 'dew_point': 8.41, 'uvi': 6.62, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 230, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 15.93, 'feels_like': 15.3, 'pressure': 1014, 'humidity': 66, 'dew_point': 9.59, 'uvi': 8.69, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 240, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 14.93, 'feels_like': 14.2, 'pressure': 1013, 'humidity': 66, 'dew_point': 8.64, 'uvi': 9.5, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 250, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 15.93, 'feels_like': 15.2, 'pressure': 1012, 'humidity': 62, 'dew_point': 8.67, 'uvi': 8.58, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 240, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 15.93, 'feels_like': 15.09, 'pressure': 1011, 'humidity': 58, 'dew_point': 7.68, 'uvi': 5.91, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 230, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 17.93, 'feels_like': 16.98, 'pressure': 1010, 'humidity': 46, 'dew_point': 6.16, 'uvi': 3.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 360, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 16.93, 'feels_like': 15.93, 'pressure': 1010, 'humidity': 48, 'dew_point': 5.86, 'uvi': 1.28, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 10, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 14.93, 'feels_like': 13.89, 'pressure': 1010, 'humidity': 54, 'dew_point': 5.71, 'uvi': 0.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 20, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 12.93, 'feels_like': 11.87, 'pressure': 1010, 'humidity': 61, 'dew_point': 5.6, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 00:00:00 | 24.000000 | 4.780000 | 12.790000 | 54.000000 | 1010.000000 |  | 13.930000 | 0.000000 | 10000.000000 | 30.000000 |  | 5.660000 | 801 | Clouds | few clouds | 02n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 01:00:00 | 27.000000 | 4.620000 | 11.770000 | 57.000000 | 1011.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 30.000000 |  | 6.690000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 02:00:00 | 29.000000 | 3.850000 | 11.690000 | 54.000000 | 1011.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 30.000000 |  | 4.120000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 03:00:00 | 33.000000 | 3.050000 | 11.610000 | 51.000000 | 1012.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 30.000000 |  | 5.660000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 04:00:00 | 34.000000 | 2.200000 | 12.550000 | 45.000000 | 1011.000000 |  | 13.930000 | 0.000000 | 10000.000000 | 20.000000 |  | 6.690000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 05:00:00 | 47.000000 | 1.900000 | 11.510000 | 47.000000 | 1012.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 60.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 1.900000 | 11.510000 | 47.000000 | 1012.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 60.000000 |  | 1.540000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 8.010000 | 10.790000 | 79.000000 | 1013.000000 |  | 11.520000 | 0.000000 | 10000.000000 | 94.000000 | 4.35 | 2.930000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 8.010000 | 10.790000 | 79.000000 | 1013.000000 |  | 11.520000 | 0.000000 | 10000.000000 | 95.000000 | 3.99 | 2.610000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 7.820000 | 10.760000 | 78.000000 | 1013.000000 |  | 11.520000 | 0.000000 | 10000.000000 | 89.000000 | 3.72 | 2.600000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 5.110000 | 7.250000 | 78.000000 | 1013.000000 |  | 8.730000 | 0.000000 | 10000.000000 | 90.000000 | 3.66 | 2.600000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 3.390000 | 6.730000 | 73.000000 | 1012.000000 |  | 7.930000 | 0.000000 | 10000.000000 | 90.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 3.390000 | 7.930000 | 73.000000 | 1013.000000 |  | 7.930000 | 0.280000 | 10000.000000 | 0.000000 |  | 0.000000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 3.690000 | 10.670000 | 57.000000 | 1014.000000 |  | 11.930000 | 1.510000 | 10000.000000 | 0.000000 |  | 0.000000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 6.430000 | 10.980000 | 69.000000 | 1015.000000 |  | 11.930000 | 3.790000 | 10000.000000 | 230.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 15:00:00 | 20.000000 | 8.410000 | 12.210000 | 74.000000 | 1015.000000 |  | 12.930000 | 6.620000 | 10000.000000 | 230.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 9.590000 | 15.300000 | 66.000000 | 1014.000000 |  | 15.930000 | 8.690000 | 10000.000000 | 240.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 8.640000 | 14.200000 | 66.000000 | 1013.000000 |  | 14.930000 | 9.500000 | 10000.000000 | 250.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 8.670000 | 15.200000 | 62.000000 | 1012.000000 |  | 15.930000 | 8.580000 | 10000.000000 | 240.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 7.680000 | 15.090000 | 58.000000 | 1011.000000 |  | 15.930000 | 5.910000 | 10000.000000 | 230.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 6.160000 | 16.980000 | 46.000000 | 1010.000000 |  | 17.930000 | 3.330000 | 10000.000000 | 360.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 5.860000 | 15.930000 | 48.000000 | 1010.000000 |  | 16.930000 | 1.280000 | 10000.000000 | 10.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 5.710000 | 13.890000 | 54.000000 | 1010.000000 |  | 14.930000 | 0.240000 | 10000.000000 | 20.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15015060 | "SAN LORENZO  - AUT [15015060]" | 11.111083 | -74.054694 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 1969-01-14 19:00:00 | NaT | Magdalena | Santa Marta | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río  Piedras - Río Manzanares | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 5.600000 | 11.870000 | 61.000000 | 1010.000000 |  | 12.930000 | 0.000000 | 10000.000000 | 30.000000 |  | 5.140000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15015060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15015060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15015060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15015060_OWM_Windspeed_20220111.png)
