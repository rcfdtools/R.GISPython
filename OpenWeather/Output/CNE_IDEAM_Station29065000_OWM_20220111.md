
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MEDIA LUNA - AUT [29065000] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29065000_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.51002778,-74.50666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.51002778&lon=-74.50666667)


| Parameter | Value |
|---|---|
| Code | 29065000 |
| Name | MEDIA LUNA - AUT [29065000] |
| Latitude, ° | 10.51002778 |
| Longitude, ° | -74.50666667 |
| Elevation, m | 20 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-05 00:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | Pivijai |
| Stream | Cauca |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Cga Grande de Santa Marta |

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

### (CNE index 235) Open Weather values for station 29065000 - MEDIA LUNA - AUT [29065000]

JSON data from API OWM:

```
{'lat': 10.51, 'lon': -74.5067, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813530, 'sunset': 1641855112, 'temp': 29.05, 'feels_like': 27.97, 'pressure': 1008, 'humidity': 31, 'dew_point': 10.22, 'uvi': 3.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.08, 'wind_deg': 352, 'wind_gust': 3.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1009, 'humidity': 67, 'dew_point': 19.45, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 299, 'wind_gust': 2.73, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1010, 'humidity': 72, 'dew_point': 20.61, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 266, 'wind_gust': 3.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 75, 'dew_point': 21.27, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 2.09, 'wind_deg': 280, 'wind_gust': 2.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.7, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 278, 'wind_gust': 1.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 78, 'dew_point': 21.91, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 203, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 27.05, 'feels_like': 29.66, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.88, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 158, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1010, 'humidity': 81, 'dew_point': 22.53, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 180, 'wind_gust': 2.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1010, 'humidity': 82, 'dew_point': 22.74, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 195, 'wind_gust': 1.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 25.05, 'feels_like': 25.8, 'pressure': 1010, 'humidity': 84, 'dew_point': 22.16, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 193, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 25.05, 'feels_like': 25.83, 'pressure': 1010, 'humidity': 85, 'dew_point': 22.35, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 196, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 25.05, 'feels_like': 25.83, 'pressure': 1010, 'humidity': 85, 'dew_point': 22.35, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 195, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 25.05, 'feels_like': 25.8, 'pressure': 1011, 'humidity': 84, 'dew_point': 22.16, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 215, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 25.05, 'feels_like': 25.62, 'pressure': 1012, 'humidity': 77, 'dew_point': 20.74, 'uvi': 0.26, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 206, 'wind_gust': 0.63, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1013, 'humidity': 63, 'dew_point': 18.46, 'uvi': 1.5, 'clouds': 15, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 354, 'wind_gust': 0.93, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.05, 'feels_like': 28.69, 'pressure': 1014, 'humidity': 52, 'dew_point': 17.28, 'uvi': 3.82, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 354, 'wind_gust': 1.6, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 29.05, 'feels_like': 28.84, 'pressure': 1014, 'humidity': 42, 'dew_point': 14.84, 'uvi': 6.71, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 352, 'wind_gust': 1.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 29.05, 'feels_like': 28.32, 'pressure': 1013, 'humidity': 36, 'dew_point': 12.48, 'uvi': 8.52, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 360, 'wind_gust': 1.92, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 30.05, 'feels_like': 28.95, 'pressure': 1011, 'humidity': 32, 'dew_point': 11.56, 'uvi': 9.37, 'clouds': 31, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 352, 'wind_gust': 2.22, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 29.05, 'feels_like': 27.91, 'pressure': 1010, 'humidity': 30, 'dew_point': 9.73, 'uvi': 8.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.79, 'wind_deg': 343, 'wind_gust': 2.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 29.05, 'feels_like': 27.86, 'pressure': 1008, 'humidity': 29, 'dew_point': 9.23, 'uvi': 6.12, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.22, 'wind_deg': 343, 'wind_gust': 2.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.05, 'feels_like': 27.97, 'pressure': 1008, 'humidity': 31, 'dew_point': 10.22, 'uvi': 3.48, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.08, 'wind_deg': 352, 'wind_gust': 3.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 28.05, 'feels_like': 27.71, 'pressure': 1008, 'humidity': 40, 'dew_point': 13.2, 'uvi': 1.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 5.45, 'wind_deg': 359, 'wind_gust': 4.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.05, 'feels_like': 27.72, 'pressure': 1008, 'humidity': 54, 'dew_point': 16.95, 'uvi': 0.23, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.85, 'wind_deg': 354, 'wind_gust': 6.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1009, 'humidity': 65, 'dew_point': 18.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 326, 'wind_gust': 6.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 00:00:00 | 5.000000 | 19.450000 | 26.050000 | 67.000000 | 1009.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 299.000000 | 2.73 | 2.190000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 01:00:00 | 8.000000 | 20.610000 | 26.050000 | 72.000000 | 1010.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 266.000000 | 3.29 | 2.240000 | 800 | Clear | clear sky | 01n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 02:00:00 | 39.000000 | 21.270000 | 26.050000 | 75.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 280.000000 | 2.77 | 2.090000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 03:00:00 | 59.000000 | 21.700000 | 26.050000 | 77.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 278.000000 | 1.58 | 1.430000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 04:00:00 | 67.000000 | 21.910000 | 26.050000 | 78.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 203.000000 | 0.78 | 0.480000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 05:00:00 | 74.000000 | 22.880000 | 29.660000 | 78.000000 | 1011.000000 |  | 27.050000 | 0.000000 | 10000.000000 | 158.000000 | 1.7 | 1.580000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 06:00:00 | 78.000000 | 22.530000 | 26.050000 | 81.000000 | 1010.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 180.000000 | 2.25 | 1.960000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 22.740000 | 26.050000 | 82.000000 | 1010.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 195.000000 | 1.77 | 1.730000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 08:00:00 | 86.000000 | 22.160000 | 25.800000 | 84.000000 | 1010.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 193.000000 | 1.39 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 22.350000 | 25.830000 | 85.000000 | 1010.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 196.000000 | 1.39 | 1.280000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 10:00:00 | 72.000000 | 22.350000 | 25.830000 | 85.000000 | 1010.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 195.000000 | 1.12 | 1.030000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 11:00:00 | 61.000000 | 22.160000 | 25.800000 | 84.000000 | 1011.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 215.000000 | 1.09 | 1.040000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 12:00:00 | 7.000000 | 20.740000 | 25.620000 | 77.000000 | 1012.000000 |  | 25.050000 | 0.260000 | 10000.000000 | 206.000000 | 0.63 | 0.450000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 13:00:00 | 15.000000 | 18.460000 | 26.050000 | 63.000000 | 1013.000000 |  | 26.050000 | 1.500000 | 10000.000000 | 354.000000 | 0.93 | 0.620000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 14:00:00 | 12.000000 | 17.280000 | 28.690000 | 52.000000 | 1014.000000 |  | 28.050000 | 3.820000 | 10000.000000 | 354.000000 | 1.6 | 1.340000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 15:00:00 | 14.000000 | 14.840000 | 28.840000 | 42.000000 | 1014.000000 |  | 29.050000 | 6.710000 | 10000.000000 | 352.000000 | 1.55 | 1.100000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 16:00:00 | 14.000000 | 12.480000 | 28.320000 | 36.000000 | 1013.000000 |  | 29.050000 | 8.520000 | 10000.000000 | 360.000000 | 1.92 | 1.550000 | 801 | Clouds | few clouds | 02d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 17:00:00 | 31.000000 | 11.560000 | 28.950000 | 32.000000 | 1011.000000 |  | 30.050000 | 9.370000 | 10000.000000 | 352.000000 | 2.22 | 2.180000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 9.730000 | 27.910000 | 30.000000 | 1010.000000 |  | 29.050000 | 8.520000 | 10000.000000 | 343.000000 | 2.54 | 2.790000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 9.230000 | 27.860000 | 29.000000 | 1008.000000 |  | 29.050000 | 6.120000 | 10000.000000 | 343.000000 | 2.69 | 3.220000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 10.220000 | 27.970000 | 31.000000 | 1008.000000 |  | 29.050000 | 3.480000 | 10000.000000 | 352.000000 | 3.32 | 4.080000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 13.200000 | 27.710000 | 40.000000 | 1008.000000 |  | 28.050000 | 1.370000 | 10000.000000 | 359.000000 | 4.83 | 5.450000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 16.950000 | 27.720000 | 54.000000 | 1008.000000 |  | 27.050000 | 0.230000 | 10000.000000 | 354.000000 | 6.73 | 4.850000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 29065000 | "MEDIA LUNA - AUT [29065000]" | 10.510028 | -74.506667 | 20.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Pivijai | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Bajo Magdalena | Cga Grande de Santa Marta | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 18.960000 | 26.050000 | 65.000000 | 1009.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 326.000000 | 6.52 | 3.190000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station29065000_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29065000_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29065000_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29065000_OWM_Windspeed_20220111.png)
