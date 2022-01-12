
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - TOROMANA - AUT [15085050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15085050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=12.08352778,-71.21094444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=12.08352778&lon=-71.21094444)


| Parameter | Value |
|---|---|
| Code | 15085050 |
| Name | TOROMANA - AUT [15085050] |
| Latitude, ° | 12.08352778 |
| Longitude, ° | -71.21094444 |
| Elevation, m | 144 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-04-18 00:00:00 |
| Suspension date | NaT |
| State | La Guajira |
| County | Uribia |
| Stream | Manzanares |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo |

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

### (CNE index 210) Open Weather values for station 15085050 - TOROMANA - AUT [15085050]

JSON data from API OWM:

```
{'lat': 12.0835, 'lon': -71.2109, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812896, 'sunset': 1641854163, 'temp': 26.18, 'feels_like': 26.18, 'pressure': 1012, 'humidity': 66, 'dew_point': 19.33, 'uvi': 3.01, 'clouds': 42, 'visibility': 10000, 'wind_speed': 6.35, 'wind_deg': 62, 'wind_gust': 7.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.41, 'feels_like': 24.94, 'pressure': 1014, 'humidity': 78, 'dew_point': 20.33, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 9.26, 'wind_deg': 67, 'wind_gust': 12.49, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 24.34, 'feels_like': 24.87, 'pressure': 1015, 'humidity': 78, 'dew_point': 20.26, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 8.97, 'wind_deg': 70, 'wind_gust': 12.77, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.2, 'feels_like': 24.74, 'pressure': 1015, 'humidity': 79, 'dew_point': 20.33, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 8.35, 'wind_deg': 72, 'wind_gust': 12.58, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 24.13, 'feels_like': 24.69, 'pressure': 1015, 'humidity': 80, 'dew_point': 20.46, 'uvi': 0, 'clouds': 3, 'visibility': 10000, 'wind_speed': 8.08, 'wind_deg': 70, 'wind_gust': 12.26, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 24.06, 'feels_like': 24.61, 'pressure': 1015, 'humidity': 80, 'dew_point': 20.4, 'uvi': 0, 'clouds': 3, 'visibility': 10000, 'wind_speed': 7.69, 'wind_deg': 70, 'wind_gust': 11.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 23.93, 'feels_like': 24.49, 'pressure': 1014, 'humidity': 81, 'dew_point': 20.47, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 7.47, 'wind_deg': 72, 'wind_gust': 11.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 23.76, 'feels_like': 24.31, 'pressure': 1013, 'humidity': 81, 'dew_point': 20.3, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 7.28, 'wind_deg': 74, 'wind_gust': 10.83, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 23.65, 'feels_like': 24.16, 'pressure': 1013, 'humidity': 80, 'dew_point': 20, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 6.91, 'wind_deg': 76, 'wind_gust': 10.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 23.62, 'feels_like': 24.1, 'pressure': 1012, 'humidity': 79, 'dew_point': 19.76, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 7.13, 'wind_deg': 78, 'wind_gust': 10.42, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641805200, 'temp': 23.51, 'feels_like': 23.98, 'pressure': 1013, 'humidity': 79, 'dew_point': 19.66, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 7.03, 'wind_deg': 80, 'wind_gust': 9.93, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641808800, 'temp': 23.44, 'feels_like': 23.93, 'pressure': 1013, 'humidity': 80, 'dew_point': 19.79, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 6.55, 'wind_deg': 84, 'wind_gust': 9.6, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641812400, 'temp': 23.47, 'feels_like': 23.96, 'pressure': 1014, 'humidity': 80, 'dew_point': 19.82, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 6.43, 'wind_deg': 87, 'wind_gust': 9.26, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 23.81, 'feels_like': 24.31, 'pressure': 1015, 'humidity': 79, 'dew_point': 19.95, 'uvi': 0.43, 'clouds': 49, 'visibility': 10000, 'wind_speed': 6.09, 'wind_deg': 91, 'wind_gust': 9.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 24.52, 'feels_like': 25.01, 'pressure': 1016, 'humidity': 76, 'dew_point': 20.01, 'uvi': 1.79, 'clouds': 64, 'visibility': 10000, 'wind_speed': 6.77, 'wind_deg': 95, 'wind_gust': 8.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.04, 'feels_like': 25.53, 'pressure': 1017, 'humidity': 74, 'dew_point': 20.08, 'uvi': 4.21, 'clouds': 47, 'visibility': 10000, 'wind_speed': 7.17, 'wind_deg': 99, 'wind_gust': 8.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 25.41, 'feels_like': 25.86, 'pressure': 1017, 'humidity': 71, 'dew_point': 19.77, 'uvi': 6.93, 'clouds': 36, 'visibility': 10000, 'wind_speed': 6.9, 'wind_deg': 102, 'wind_gust': 8.56, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 25.86, 'feels_like': 26.28, 'pressure': 1016, 'humidity': 68, 'dew_point': 19.5, 'uvi': 9.06, 'clouds': 28, 'visibility': 10000, 'wind_speed': 6.32, 'wind_deg': 104, 'wind_gust': 8.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 26.23, 'feels_like': 26.23, 'pressure': 1015, 'humidity': 65, 'dew_point': 19.13, 'uvi': 9.54, 'clouds': 24, 'visibility': 10000, 'wind_speed': 6.09, 'wind_deg': 101, 'wind_gust': 8.23, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 26.33, 'feels_like': 26.33, 'pressure': 1014, 'humidity': 65, 'dew_point': 19.23, 'uvi': 8.26, 'clouds': 15, 'visibility': 10000, 'wind_speed': 6.08, 'wind_deg': 86, 'wind_gust': 8.12, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 26.33, 'feels_like': 26.33, 'pressure': 1013, 'humidity': 65, 'dew_point': 19.23, 'uvi': 5.74, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 71, 'wind_gust': 7.25, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 26.18, 'feels_like': 26.18, 'pressure': 1012, 'humidity': 66, 'dew_point': 19.33, 'uvi': 3.01, 'clouds': 42, 'visibility': 10000, 'wind_speed': 6.35, 'wind_deg': 62, 'wind_gust': 7.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 25.73, 'feels_like': 26.16, 'pressure': 1012, 'humidity': 69, 'dew_point': 19.62, 'uvi': 1.03, 'clouds': 41, 'visibility': 10000, 'wind_speed': 7.91, 'wind_deg': 58, 'wind_gust': 9.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 25.14, 'feels_like': 25.56, 'pressure': 1012, 'humidity': 71, 'dew_point': 19.51, 'uvi': 0.15, 'clouds': 49, 'visibility': 10000, 'wind_speed': 7.79, 'wind_deg': 54, 'wind_gust': 9.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 24.62, 'feels_like': 25.12, 'pressure': 1012, 'humidity': 76, 'dew_point': 20.11, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 7.38, 'wind_deg': 52, 'wind_gust': 10.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 00:00:00 | 5.000000 | 20.330000 | 24.940000 | 78.000000 | 1014.000000 |  | 24.410000 | 0.000000 | 10000.000000 | 67.000000 | 12.49 | 9.260000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 01:00:00 | 5.000000 | 20.260000 | 24.870000 | 78.000000 | 1015.000000 |  | 24.340000 | 0.000000 | 10000.000000 | 70.000000 | 12.77 | 8.970000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 02:00:00 | 4.000000 | 20.330000 | 24.740000 | 79.000000 | 1015.000000 |  | 24.200000 | 0.000000 | 10000.000000 | 72.000000 | 12.58 | 8.350000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 03:00:00 | 3.000000 | 20.460000 | 24.690000 | 80.000000 | 1015.000000 |  | 24.130000 | 0.000000 | 10000.000000 | 70.000000 | 12.26 | 8.080000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 04:00:00 | 3.000000 | 20.400000 | 24.610000 | 80.000000 | 1015.000000 |  | 24.060000 | 0.000000 | 10000.000000 | 70.000000 | 11.57 | 7.690000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 05:00:00 | 4.000000 | 20.470000 | 24.490000 | 81.000000 | 1014.000000 |  | 23.930000 | 0.000000 | 10000.000000 | 72.000000 | 11.17 | 7.470000 | 800 | Clear | clear sky | 01n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 06:00:00 | 5.000000 | 20.300000 | 24.310000 | 81.000000 | 1013.000000 |  | 23.760000 | 0.000000 | 10000.000000 | 74.000000 | 10.83 | 7.280000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 07:00:00 | 5.000000 | 20.000000 | 24.160000 | 80.000000 | 1013.000000 |  | 23.650000 | 0.000000 | 10000.000000 | 76.000000 | 10.57 | 6.910000 | 800 | Clear | clear sky | 01n | 07 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 08:00:00 | 6.000000 | 19.760000 | 24.100000 | 79.000000 | 1012.000000 |  | 23.620000 | 0.000000 | 10000.000000 | 78.000000 | 10.42 | 7.130000 | 800 | Clear | clear sky | 01n | 08 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 09:00:00 | 6.000000 | 19.660000 | 23.980000 | 79.000000 | 1013.000000 |  | 23.510000 | 0.000000 | 10000.000000 | 80.000000 | 9.93 | 7.030000 | 800 | Clear | clear sky | 01n | 09 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 10:00:00 | 9.000000 | 19.790000 | 23.930000 | 80.000000 | 1013.000000 |  | 23.440000 | 0.000000 | 10000.000000 | 84.000000 | 9.6 | 6.550000 | 800 | Clear | clear sky | 01n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 19.820000 | 23.960000 | 80.000000 | 1014.000000 |  | 23.470000 | 0.000000 | 10000.000000 | 87.000000 | 9.26 | 6.430000 | 801 | Clouds | few clouds | 02n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 12:00:00 | 49.000000 | 19.950000 | 24.310000 | 79.000000 | 1015.000000 |  | 23.810000 | 0.430000 | 10000.000000 | 91.000000 | 9.07 | 6.090000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 13:00:00 | 64.000000 | 20.010000 | 25.010000 | 76.000000 | 1016.000000 |  | 24.520000 | 1.790000 | 10000.000000 | 95.000000 | 8.88 | 6.770000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 14:00:00 | 47.000000 | 20.080000 | 25.530000 | 74.000000 | 1017.000000 |  | 25.040000 | 4.210000 | 10000.000000 | 99.000000 | 8.88 | 7.170000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 15:00:00 | 36.000000 | 19.770000 | 25.860000 | 71.000000 | 1017.000000 |  | 25.410000 | 6.930000 | 10000.000000 | 102.000000 | 8.56 | 6.900000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 16:00:00 | 28.000000 | 19.500000 | 26.280000 | 68.000000 | 1016.000000 |  | 25.860000 | 9.060000 | 10000.000000 | 104.000000 | 8.17 | 6.320000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 17:00:00 | 24.000000 | 19.130000 | 26.230000 | 65.000000 | 1015.000000 |  | 26.230000 | 9.540000 | 10000.000000 | 101.000000 | 8.23 | 6.090000 | 801 | Clouds | few clouds | 02d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 18:00:00 | 15.000000 | 19.230000 | 26.330000 | 65.000000 | 1014.000000 |  | 26.330000 | 8.260000 | 10000.000000 | 86.000000 | 8.12 | 6.080000 | 801 | Clouds | few clouds | 02d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 19:00:00 | 20.000000 | 19.230000 | 26.330000 | 65.000000 | 1013.000000 |  | 26.330000 | 5.740000 | 10000.000000 | 71.000000 | 7.25 | 5.660000 | 801 | Clouds | few clouds | 02d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 20:00:00 | 42.000000 | 19.330000 | 26.180000 | 66.000000 | 1012.000000 |  | 26.180000 | 3.010000 | 10000.000000 | 62.000000 | 7.67 | 6.350000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 21:00:00 | 41.000000 | 19.620000 | 26.160000 | 69.000000 | 1012.000000 |  | 25.730000 | 1.030000 | 10000.000000 | 58.000000 | 9.21 | 7.910000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 22:00:00 | 49.000000 | 19.510000 | 25.560000 | 71.000000 | 1012.000000 |  | 25.140000 | 0.150000 | 10000.000000 | 54.000000 | 9.92 | 7.790000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15085050 | "TOROMANA - AUT [15085050]" | 12.083528 | -71.210944 | 144.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-04-18 00:00:00 | NaT | La Guajira | Uribia | Manzanares | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 23:00:00 | 45.000000 | 20.110000 | 25.120000 | 76.000000 | 1012.000000 |  | 24.620000 | 0.000000 | 10000.000000 | 52.000000 | 10.67 | 7.380000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station15085050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15085050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15085050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085050_OWM_Windspeed_20220111.png)
