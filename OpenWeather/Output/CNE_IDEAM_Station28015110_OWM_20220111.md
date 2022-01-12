
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MANAURE - AUT [28015110] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28015110_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.36533333,-72.99763889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.36533333&lon=-72.99763889)


| Parameter | Value |
|---|---|
| Code | 28015110 |
| Name | MANAURE - AUT [28015110] |
| Latitude, ° | 10.36533333 |
| Longitude, ° | -72.99763889 |
| Elevation, m | 1918 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2005-08-17 00:00:00 |
| Suspension date | 2006-05-15 00:00:00 |
| State | Cesar |
| County | Manaure Balcón Del Cesar |
| Stream | Magdalena |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Medio Cesar |

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

### (CNE index 228) Open Weather values for station 28015110 - MANAURE - AUT [28015110]

JSON data from API OWM:

```
{'lat': 10.3653, 'lon': -72.9976, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813154, 'sunset': 1641854764, 'temp': 22.56, 'feels_like': 22.12, 'pressure': 1012, 'humidity': 48, 'dew_point': 11.01, 'uvi': 2.68, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 335, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 17.56, 'feels_like': 17.15, 'pressure': 1016, 'humidity': 68, 'dew_point': 11.59, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.9, 'wind_deg': 96, 'wind_gust': 5.32, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 16.56, 'feels_like': 16.07, 'pressure': 1017, 'humidity': 69, 'dew_point': 10.86, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 99, 'wind_gust': 4.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 15.56, 'feels_like': 14.89, 'pressure': 1018, 'humidity': 66, 'dew_point': 9.24, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 2.59, 'wind_deg': 98, 'wind_gust': 4.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 15.56, 'feels_like': 14.84, 'pressure': 1017, 'humidity': 64, 'dew_point': 8.78, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.64, 'wind_deg': 98, 'wind_gust': 4.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 15.56, 'feels_like': 14.84, 'pressure': 1017, 'humidity': 64, 'dew_point': 8.78, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.74, 'wind_deg': 100, 'wind_gust': 4.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 11.17, 'feels_like': 9.91, 'pressure': 1017, 'humidity': 60, 'dew_point': 3.7, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 101, 'wind_gust': 4.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 10.81, 'feels_like': 9.51, 'pressure': 1016, 'humidity': 60, 'dew_point': 3.36, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 2.83, 'wind_deg': 104, 'wind_gust': 4.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 10.62, 'feels_like': 9.41, 'pressure': 1016, 'humidity': 64, 'dew_point': 4.1, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 106, 'wind_gust': 3.95, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 10.71, 'feels_like': 9.53, 'pressure': 1015, 'humidity': 65, 'dew_point': 4.41, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 106, 'wind_gust': 3.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 10.71, 'feels_like': 9.56, 'pressure': 1016, 'humidity': 66, 'dew_point': 4.62, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.37, 'wind_deg': 106, 'wind_gust': 2.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 10.61, 'feels_like': 9.45, 'pressure': 1016, 'humidity': 66, 'dew_point': 4.53, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 106, 'wind_gust': 2.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 11.56, 'feels_like': 10.44, 'pressure': 1017, 'humidity': 64, 'dew_point': 4.99, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 107, 'wind_gust': 2.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 12.56, 'feels_like': 11.46, 'pressure': 1017, 'humidity': 61, 'dew_point': 5.25, 'uvi': 0.41, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 102, 'wind_gust': 3.84, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 14.56, 'feels_like': 13.35, 'pressure': 1017, 'humidity': 49, 'dew_point': 3.98, 'uvi': 1.91, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 340, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 16.56, 'feels_like': 15.45, 'pressure': 1018, 'humidity': 45, 'dew_point': 4.59, 'uvi': 4.61, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 328, 'wind_gust': 2.28, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 18.56, 'feels_like': 17.57, 'pressure': 1017, 'humidity': 42, 'dew_point': 5.42, 'uvi': 7.75, 'clouds': 45, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 326, 'wind_gust': 2.52, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 19.56, 'feels_like': 18.62, 'pressure': 1016, 'humidity': 40, 'dew_point': 5.61, 'uvi': 10.07, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.73, 'wind_deg': 318, 'wind_gust': 2.68, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 21.56, 'feels_like': 20.82, 'pressure': 1015, 'humidity': 40, 'dew_point': 7.4, 'uvi': 10.79, 'clouds': 33, 'visibility': 10000, 'wind_speed': 2.82, 'wind_deg': 313, 'wind_gust': 2.89, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 21.56, 'feels_like': 20.79, 'pressure': 1014, 'humidity': 39, 'dew_point': 7.03, 'uvi': 9.56, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 312, 'wind_gust': 2.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 22.56, 'feels_like': 21.97, 'pressure': 1013, 'humidity': 42, 'dew_point': 9.02, 'uvi': 4.87, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 320, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 22.56, 'feels_like': 22.12, 'pressure': 1012, 'humidity': 48, 'dew_point': 11.01, 'uvi': 2.68, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 335, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 22.56, 'feels_like': 22.33, 'pressure': 1013, 'humidity': 56, 'dew_point': 13.35, 'uvi': 0.98, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 5, 'wind_gust': 1.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 21.56, 'feels_like': 21.39, 'pressure': 1014, 'humidity': 62, 'dew_point': 13.98, 'uvi': 0.1, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 50, 'wind_gust': 2.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 19.56, 'feels_like': 19.29, 'pressure': 1014, 'humidity': 66, 'dew_point': 13.04, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 66, 'wind_gust': 2.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 00:00:00 | 33.000000 | 11.590000 | 17.150000 | 68.000000 | 1016.000000 |  | 17.560000 | 0.000000 | 10000.000000 | 96.000000 | 5.32 | 2.900000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 01:00:00 | 53.000000 | 10.860000 | 16.070000 | 69.000000 | 1017.000000 |  | 16.560000 | 0.000000 | 10000.000000 | 99.000000 | 4.98 | 2.860000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 02:00:00 | 72.000000 | 9.240000 | 14.890000 | 66.000000 | 1018.000000 |  | 15.560000 | 0.000000 | 10000.000000 | 98.000000 | 4.58 | 2.590000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 03:00:00 | 49.000000 | 8.780000 | 14.840000 | 64.000000 | 1017.000000 |  | 15.560000 | 0.000000 | 10000.000000 | 98.000000 | 4.63 | 2.640000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 04:00:00 | 38.000000 | 8.780000 | 14.840000 | 64.000000 | 1017.000000 |  | 15.560000 | 0.000000 | 10000.000000 | 100.000000 | 4.47 | 2.740000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 05:00:00 | 32.000000 | 3.700000 | 9.910000 | 60.000000 | 1017.000000 |  | 11.170000 | 0.000000 | 10000.000000 | 101.000000 | 4.37 | 2.840000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 06:00:00 | 7.000000 | 3.360000 | 9.510000 | 60.000000 | 1016.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 104.000000 | 4.28 | 2.830000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 07:00:00 | 5.000000 | 4.100000 | 9.410000 | 64.000000 | 1016.000000 |  | 10.620000 | 0.000000 | 10000.000000 | 106.000000 | 3.95 | 2.670000 | 800 | Clear | clear sky | 01n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 08:00:00 | 52.000000 | 4.410000 | 9.530000 | 65.000000 | 1015.000000 |  | 10.710000 | 0.000000 | 10000.000000 | 106.000000 | 3.03 | 2.440000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 09:00:00 | 68.000000 | 4.620000 | 9.560000 | 66.000000 | 1016.000000 |  | 10.710000 | 0.000000 | 10000.000000 | 106.000000 | 2.79 | 2.370000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 10:00:00 | 70.000000 | 4.530000 | 9.450000 | 66.000000 | 1016.000000 |  | 10.610000 | 0.000000 | 10000.000000 | 106.000000 | 2.7 | 2.490000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 11:00:00 | 62.000000 | 4.990000 | 10.440000 | 64.000000 | 1017.000000 |  | 11.560000 | 0.000000 | 10000.000000 | 107.000000 | 2.7 | 2.530000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 12:00:00 | 42.000000 | 5.250000 | 11.460000 | 61.000000 | 1017.000000 |  | 12.560000 | 0.410000 | 10000.000000 | 102.000000 | 3.84 | 2.220000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 13:00:00 | 57.000000 | 3.980000 | 13.350000 | 49.000000 | 1017.000000 |  | 14.560000 | 1.910000 | 10000.000000 | 340.000000 | 2.38 | 0.870000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 14:00:00 | 40.000000 | 4.590000 | 15.450000 | 45.000000 | 1018.000000 |  | 16.560000 | 4.610000 | 10000.000000 | 328.000000 | 2.28 | 1.850000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 15:00:00 | 45.000000 | 5.420000 | 17.570000 | 42.000000 | 1017.000000 |  | 18.560000 | 7.750000 | 10000.000000 | 326.000000 | 2.52 | 2.390000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 16:00:00 | 38.000000 | 5.610000 | 18.620000 | 40.000000 | 1016.000000 |  | 19.560000 | 10.070000 | 10000.000000 | 318.000000 | 2.68 | 2.730000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 17:00:00 | 33.000000 | 7.400000 | 20.820000 | 40.000000 | 1015.000000 |  | 21.560000 | 10.790000 | 10000.000000 | 313.000000 | 2.89 | 2.820000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 18:00:00 | 86.000000 | 7.030000 | 20.790000 | 39.000000 | 1014.000000 |  | 21.560000 | 9.560000 | 10000.000000 | 312.000000 | 2.83 | 2.650000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 19:00:00 | 97.000000 | 9.020000 | 21.970000 | 42.000000 | 1013.000000 |  | 22.560000 | 4.870000 | 10000.000000 | 320.000000 | 1.95 | 2.150000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 20:00:00 | 98.000000 | 11.010000 | 22.120000 | 48.000000 | 1012.000000 |  | 22.560000 | 2.680000 | 10000.000000 | 335.000000 | 1.82 | 1.470000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 13.350000 | 22.330000 | 56.000000 | 1013.000000 |  | 22.560000 | 0.980000 | 10000.000000 | 5.000000 | 1.91 | 1.010000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 13.980000 | 21.390000 | 62.000000 | 1014.000000 |  | 21.560000 | 0.100000 | 10000.000000 | 50.000000 | 2.37 | 0.950000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28015110 | "MANAURE - AUT [28015110]" | 10.365333 | -72.997639 | 1918.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2006-05-15 00:00:00 | Cesar | Manaure Balcón Del Cesar | Magdalena | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 13.040000 | 19.290000 | 66.000000 | 1014.000000 |  | 19.560000 | 0.000000 | 10000.000000 | 66.000000 | 2.95 | 1.420000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28015110_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28015110_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28015110_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28015110_OWM_Windspeed_20220111.png)
