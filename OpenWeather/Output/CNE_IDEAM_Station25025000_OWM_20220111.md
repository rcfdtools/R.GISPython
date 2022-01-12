
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL DIFICIL - AUT [25025000] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025000_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.91197222,-74.08580556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.91197222&lon=-74.08580556)


| Parameter | Value |
|---|---|
| Code | 25025000 |
| Name | EL DIFICIL - AUT [25025000] |
| Latitude, ° | 9.91197222 |
| Longitude, ° | -74.08580556 |
| Elevation, m | 120 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2013-05-05 00:00:00 |
| Suspension date | NaT |
| State | Magdalena |
| County | Ariguaní (El Dificil) |
| Stream | Vaupes |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Río Ariguaní |

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

### (CNE index 215) Open Weather values for station 25025000 - EL DIFICIL - AUT [25025000]

JSON data from API OWM:

```
{'lat': 9.912, 'lon': -74.0858, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813370, 'sunset': 1641855070, 'temp': 36.09, 'feels_like': 34.62, 'pressure': 1007, 'humidity': 22, 'dew_point': 11.02, 'uvi': 3.59, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 143, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.28, 'feels_like': 27.36, 'pressure': 1009, 'humidity': 45, 'dew_point': 14.32, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 230, 'wind_gust': 2.27, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1011, 'humidity': 51, 'dew_point': 15.07, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 256, 'wind_gust': 2.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 25.02, 'feels_like': 25.04, 'pressure': 1011, 'humidity': 56, 'dew_point': 15.64, 'uvi': 0, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 232, 'wind_gust': 1.56, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 24.3, 'feels_like': 24.33, 'pressure': 1011, 'humidity': 59, 'dew_point': 15.78, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 192, 'wind_gust': 1.31, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 23.74, 'feels_like': 23.71, 'pressure': 1011, 'humidity': 59, 'dew_point': 15.26, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 102, 'wind_gust': 1.53, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 23.05, 'feels_like': 22.93, 'pressure': 1011, 'humidity': 58, 'dew_point': 14.35, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 100, 'wind_gust': 3.08, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 22.18, 'feels_like': 21.97, 'pressure': 1011, 'humidity': 58, 'dew_point': 13.53, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 112, 'wind_gust': 5.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.7, 'feels_like': 21.49, 'pressure': 1010, 'humidity': 60, 'dew_point': 13.6, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 107, 'wind_gust': 7.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.48, 'feels_like': 21.3, 'pressure': 1010, 'humidity': 62, 'dew_point': 13.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.93, 'wind_deg': 97, 'wind_gust': 7.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.01, 'feels_like': 20.84, 'pressure': 1010, 'humidity': 64, 'dew_point': 13.95, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.99, 'wind_deg': 95, 'wind_gust': 7.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.6, 'feels_like': 20.41, 'pressure': 1011, 'humidity': 65, 'dew_point': 13.8, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 2.73, 'wind_deg': 105, 'wind_gust': 6.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.28, 'feels_like': 20.09, 'pressure': 1012, 'humidity': 66, 'dew_point': 13.73, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 113, 'wind_gust': 5.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.59, 'feels_like': 21.4, 'pressure': 1013, 'humidity': 61, 'dew_point': 13.75, 'uvi': 0.32, 'clouds': 9, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 111, 'wind_gust': 6.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 25.55, 'feels_like': 25.41, 'pressure': 1014, 'humidity': 48, 'dew_point': 13.74, 'uvi': 1.65, 'clouds': 6, 'visibility': 10000, 'wind_speed': 3.63, 'wind_deg': 97, 'wind_gust': 6.25, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641823200, 'temp': 29.02, 'feels_like': 28.54, 'pressure': 1014, 'humidity': 39, 'dew_point': 13.67, 'uvi': 4.09, 'clouds': 16, 'visibility': 10000, 'wind_speed': 3.96, 'wind_deg': 98, 'wind_gust': 5.94, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 31.55, 'feels_like': 30.65, 'pressure': 1014, 'humidity': 33, 'dew_point': 13.33, 'uvi': 7.08, 'clouds': 25, 'visibility': 10000, 'wind_speed': 3.88, 'wind_deg': 109, 'wind_gust': 4.42, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 33.34, 'feels_like': 32.28, 'pressure': 1013, 'humidity': 29, 'dew_point': 12.9, 'uvi': 9.41, 'clouds': 32, 'visibility': 10000, 'wind_speed': 3.55, 'wind_deg': 117, 'wind_gust': 3.7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 34.77, 'feels_like': 33.46, 'pressure': 1011, 'humidity': 25, 'dew_point': 11.85, 'uvi': 10.28, 'clouds': 34, 'visibility': 10000, 'wind_speed': 3.03, 'wind_deg': 120, 'wind_gust': 3.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 35.74, 'feels_like': 34.52, 'pressure': 1010, 'humidity': 24, 'dew_point': 12.05, 'uvi': 9.3, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 123, 'wind_gust': 2.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 36.26, 'feels_like': 34.83, 'pressure': 1008, 'humidity': 22, 'dew_point': 11.16, 'uvi': 6.35, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 132, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 36.09, 'feels_like': 34.62, 'pressure': 1007, 'humidity': 22, 'dew_point': 11.02, 'uvi': 3.59, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 143, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 35.46, 'feels_like': 34, 'pressure': 1007, 'humidity': 23, 'dew_point': 11.17, 'uvi': 1.41, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 298, 'wind_gust': 1.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 33.59, 'feels_like': 32.59, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.11, 'uvi': 0.24, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 303, 'wind_gust': 3.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 29.65, 'feels_like': 29.29, 'pressure': 1008, 'humidity': 40, 'dew_point': 14.62, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.95, 'wind_deg': 294, 'wind_gust': 6.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 00:00:00 | 7.000000 | 14.320000 | 27.360000 | 45.000000 | 1009.000000 |  | 27.280000 | 0.000000 | 10000.000000 | 230.000000 | 2.27 | 1.320000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 01:00:00 | 9.000000 | 15.070000 | 25.980000 | 51.000000 | 1011.000000 |  | 25.980000 | 0.000000 | 10000.000000 | 256.000000 | 2.11 | 1.600000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 02:00:00 | 10.000000 | 15.640000 | 25.040000 | 56.000000 | 1011.000000 |  | 25.020000 | 0.000000 | 10000.000000 | 232.000000 | 1.56 | 1.080000 | 800 | Clear | clear sky | 01n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 03:00:00 | 16.000000 | 15.780000 | 24.330000 | 59.000000 | 1011.000000 |  | 24.300000 | 0.000000 | 10000.000000 | 192.000000 | 1.31 | 0.580000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 04:00:00 | 23.000000 | 15.260000 | 23.710000 | 59.000000 | 1011.000000 |  | 23.740000 | 0.000000 | 10000.000000 | 102.000000 | 1.53 | 0.850000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 05:00:00 | 22.000000 | 14.350000 | 22.930000 | 58.000000 | 1011.000000 |  | 23.050000 | 0.000000 | 10000.000000 | 100.000000 | 3.08 | 1.670000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 06:00:00 | 99.000000 | 13.530000 | 21.970000 | 58.000000 | 1011.000000 |  | 22.180000 | 0.000000 | 10000.000000 | 112.000000 | 5.79 | 2.060000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 13.600000 | 21.490000 | 60.000000 | 1010.000000 |  | 21.700000 | 0.000000 | 10000.000000 | 107.000000 | 7.37 | 2.570000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 13.900000 | 21.300000 | 62.000000 | 1010.000000 |  | 21.480000 | 0.000000 | 10000.000000 | 97.000000 | 7.34 | 2.930000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 13.950000 | 20.840000 | 64.000000 | 1010.000000 |  | 21.010000 | 0.000000 | 10000.000000 | 95.000000 | 7.28 | 2.990000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 10:00:00 | 83.000000 | 13.800000 | 20.410000 | 65.000000 | 1011.000000 |  | 20.600000 | 0.000000 | 10000.000000 | 105.000000 | 6.54 | 2.730000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 11:00:00 | 74.000000 | 13.730000 | 20.090000 | 66.000000 | 1012.000000 |  | 20.280000 | 0.000000 | 10000.000000 | 113.000000 | 5.08 | 2.420000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 12:00:00 | 9.000000 | 13.750000 | 21.400000 | 61.000000 | 1013.000000 |  | 21.590000 | 0.320000 | 10000.000000 | 111.000000 | 6.17 | 2.450000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 13:00:00 | 6.000000 | 13.740000 | 25.410000 | 48.000000 | 1014.000000 |  | 25.550000 | 1.650000 | 10000.000000 | 97.000000 | 6.25 | 3.630000 | 800 | Clear | clear sky | 01d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 14:00:00 | 16.000000 | 13.670000 | 28.540000 | 39.000000 | 1014.000000 |  | 29.020000 | 4.090000 | 10000.000000 | 98.000000 | 5.94 | 3.960000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 15:00:00 | 25.000000 | 13.330000 | 30.650000 | 33.000000 | 1014.000000 |  | 31.550000 | 7.080000 | 10000.000000 | 109.000000 | 4.42 | 3.880000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 16:00:00 | 32.000000 | 12.900000 | 32.280000 | 29.000000 | 1013.000000 |  | 33.340000 | 9.410000 | 10000.000000 | 117.000000 | 3.7 | 3.550000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 17:00:00 | 34.000000 | 11.850000 | 33.460000 | 25.000000 | 1011.000000 |  | 34.770000 | 10.280000 | 10000.000000 | 120.000000 | 3.15 | 3.030000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 12.050000 | 34.520000 | 24.000000 | 1010.000000 |  | 35.740000 | 9.300000 | 10000.000000 | 123.000000 | 2.69 | 2.440000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 11.160000 | 34.830000 | 22.000000 | 1008.000000 |  | 36.260000 | 6.350000 | 10000.000000 | 132.000000 | 2.12 | 1.430000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 11.020000 | 34.620000 | 22.000000 | 1007.000000 |  | 36.090000 | 3.590000 | 10000.000000 | 143.000000 | 1.97 | 0.310000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 11.170000 | 34.000000 | 23.000000 | 1007.000000 |  | 35.460000 | 1.410000 | 10000.000000 | 298.000000 | 1.92 | 0.650000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 13.110000 | 32.590000 | 29.000000 | 1007.000000 |  | 33.590000 | 0.240000 | 10000.000000 | 303.000000 | 3.91 | 2.060000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025000 | "EL DIFICIL - AUT [25025000]" | 9.911972 | -74.085806 | 120.000000 | Climática Principal | Automática con Telemetría | Activa | 2013-05-05 00:00:00 | NaT | Magdalena | Ariguaní (El Dificil) | Vaupes | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 14.620000 | 29.290000 | 40.000000 | 1008.000000 |  | 29.650000 | 0.000000 | 10000.000000 | 294.000000 | 6.88 | 2.950000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025000_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025000_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025000_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025000_OWM_Windspeed_20220111.png)
