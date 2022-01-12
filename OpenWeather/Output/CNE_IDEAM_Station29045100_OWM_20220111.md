
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BASE NAVAL [29045100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station29045100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.0,-74.78333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.0&lon=-74.78333333)


| Parameter | Value |
|---|---|
| Code | 29045100 |
| Name | BASE NAVAL [29045100] |
| Latitude, ° | 11.0 |
| Longitude, ° | -74.78333333 |
| Elevation, m | 5 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1973-06-15 00:00:00 |
| Suspension date | 1992-09-15 00:00:00 |
| State | Atlantico |
| County | Barranquilla |
| Stream | Ay Pozo Hondo |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena |
| SZH - Hydrographic subzone | Directos al Bajo Magdalena entre Calamar y desembocadura |

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

### (CNE index 501) Open Weather values for station 29045100 - BASE NAVAL [29045100]

JSON data from API OWM:

```
{'lat': 11, 'lon': -74.7833, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813646, 'sunset': 1641855130, 'temp': 29.1, 'feels_like': 32.03, 'pressure': 1010, 'humidity': 65, 'dew_point': 21.85, 'uvi': 3.48, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1010, 'humidity': 78, 'dew_point': 21.96, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 9.26, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 78, 'dew_point': 21.96, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 78, 'dew_point': 21.96, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.88, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.88, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 27.1, 'feels_like': 28.28, 'pressure': 1011, 'humidity': 61, 'dew_point': 18.93, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1010, 'humidity': 65, 'dew_point': 19.01, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1010, 'humidity': 69, 'dew_point': 19.97, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 25.1, 'feels_like': 25.7, 'pressure': 1010, 'humidity': 78, 'dew_point': 20.99, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641805200, 'temp': 25.1, 'feels_like': 25.57, 'pressure': 1010, 'humidity': 73, 'dew_point': 19.92, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641808800, 'temp': 25.1, 'feels_like': 25.57, 'pressure': 1010, 'humidity': 73, 'dew_point': 19.92, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641812400, 'temp': 25.1, 'feels_like': 25.7, 'pressure': 1011, 'humidity': 78, 'dew_point': 20.99, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 25.09, 'feels_like': 25.56, 'pressure': 1011, 'humidity': 73, 'dew_point': 19.91, 'uvi': 0.26, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1013, 'humidity': 69, 'dew_point': 19.97, 'uvi': 1.5, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641823200, 'temp': 28.1, 'feels_like': 30.72, 'pressure': 1014, 'humidity': 69, 'dew_point': 21.88, 'uvi': 3.82, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 50, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641826800, 'temp': 29.1, 'feels_like': 30.89, 'pressure': 1014, 'humidity': 58, 'dew_point': 20, 'uvi': 6.71, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 60, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641830400, 'temp': 29.1, 'feels_like': 31.36, 'pressure': 1013, 'humidity': 61, 'dew_point': 20.81, 'uvi': 8.52, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641834000, 'temp': 30.1, 'feels_like': 33.44, 'pressure': 1012, 'humidity': 62, 'dew_point': 22.02, 'uvi': 9.37, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 50, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641837600, 'temp': 29.1, 'feels_like': 30.89, 'pressure': 1012, 'humidity': 58, 'dew_point': 20, 'uvi': 8.52, 'clouds': 0, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 30, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 29.1, 'feels_like': 31.36, 'pressure': 1010, 'humidity': 61, 'dew_point': 20.81, 'uvi': 6.12, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641844800, 'temp': 29.1, 'feels_like': 32.03, 'pressure': 1010, 'humidity': 65, 'dew_point': 21.85, 'uvi': 3.48, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641848400, 'temp': 28.1, 'feels_like': 30.72, 'pressure': 1010, 'humidity': 69, 'dew_point': 21.88, 'uvi': 1.37, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641852000, 'temp': 27.1, 'feels_like': 29.39, 'pressure': 1010, 'humidity': 74, 'dew_point': 22.07, 'uvi': 0.23, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641855600, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1010, 'humidity': 78, 'dew_point': 21.96, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 00:00:00 | 0.000000 | 21.960000 | 26.100000 | 78.000000 | 1010.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 20.000000 |  | 9.260000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 01:00:00 | 0.000000 | 21.960000 | 26.100000 | 78.000000 | 1011.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 20.000000 |  | 7.200000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 02:00:00 | 0.000000 | 21.960000 | 26.100000 | 78.000000 | 1011.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 20.000000 |  | 6.170000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 03:00:00 | 0.000000 | 20.880000 | 26.100000 | 73.000000 | 1011.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 4.630000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 04:00:00 | 0.000000 | 20.880000 | 26.100000 | 73.000000 | 1011.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 4.120000 | 800 | Clear | clear sky | 01n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 05:00:00 | 40.000000 | 18.930000 | 28.280000 | 61.000000 | 1011.000000 |  | 27.100000 | 0.000000 | 10000.000000 | 40.000000 |  | 6.170000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 19.010000 | 26.100000 | 65.000000 | 1010.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 40.000000 |  | 6.170000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 07:00:00 | 0.000000 | 19.970000 | 26.100000 | 69.000000 | 1010.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 4.120000 | 800 | Clear | clear sky | 01n | 07 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 08:00:00 | 0.000000 | 20.990000 | 25.700000 | 78.000000 | 1010.000000 |  | 25.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 3.600000 | 800 | Clear | clear sky | 01n | 08 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 09:00:00 | 0.000000 | 19.920000 | 25.570000 | 73.000000 | 1010.000000 |  | 25.100000 | 0.000000 | 10000.000000 | 40.000000 |  | 3.600000 | 800 | Clear | clear sky | 01n | 09 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 10:00:00 | 0.000000 | 19.920000 | 25.570000 | 73.000000 | 1010.000000 |  | 25.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 3.600000 | 800 | Clear | clear sky | 01n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 11:00:00 | 40.000000 | 20.990000 | 25.700000 | 78.000000 | 1011.000000 |  | 25.100000 | 0.000000 | 10000.000000 | 30.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 19.910000 | 25.560000 | 73.000000 | 1011.000000 |  | 25.090000 | 0.260000 | 10000.000000 | 30.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 13:00:00 | 0.000000 | 19.970000 | 26.100000 | 69.000000 | 1013.000000 |  | 26.100000 | 1.500000 | 10000.000000 | 40.000000 |  | 3.600000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 14:00:00 | 0.000000 | 21.880000 | 30.720000 | 69.000000 | 1014.000000 |  | 28.100000 | 3.820000 | 10000.000000 | 50.000000 |  | 4.630000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 15:00:00 | 0.000000 | 20.000000 | 30.890000 | 58.000000 | 1014.000000 |  | 29.100000 | 6.710000 | 10000.000000 | 60.000000 |  | 5.140000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 16:00:00 | 0.000000 | 20.810000 | 31.360000 | 61.000000 | 1013.000000 |  | 29.100000 | 8.520000 | 10000.000000 | 40.000000 |  | 3.600000 | 800 | Clear | clear sky | 01d | 16 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 17:00:00 | 0.000000 | 22.020000 | 33.440000 | 62.000000 | 1012.000000 |  | 30.100000 | 9.370000 | 10000.000000 | 50.000000 |  | 3.600000 | 800 | Clear | clear sky | 01d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 18:00:00 | 0.000000 | 20.000000 | 30.890000 | 58.000000 | 1012.000000 |  | 29.100000 | 8.520000 | 10000.000000 | 30.000000 |  | 6.170000 | 800 | Clear | clear sky | 01d | 18 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 19:00:00 | 0.000000 | 20.810000 | 31.360000 | 61.000000 | 1010.000000 |  | 29.100000 | 6.120000 | 10000.000000 | 20.000000 |  | 5.140000 | 800 | Clear | clear sky | 01d | 19 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 20:00:00 | 0.000000 | 21.850000 | 32.030000 | 65.000000 | 1010.000000 |  | 29.100000 | 3.480000 | 10000.000000 | 20.000000 |  | 5.660000 | 800 | Clear | clear sky | 01d | 20 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 21:00:00 | 0.000000 | 21.880000 | 30.720000 | 69.000000 | 1010.000000 |  | 28.100000 | 1.370000 | 10000.000000 | 20.000000 |  | 5.140000 | 800 | Clear | clear sky | 01d | 21 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 22:00:00 | 0.000000 | 22.070000 | 29.390000 | 74.000000 | 1010.000000 |  | 27.100000 | 0.230000 | 10000.000000 | 20.000000 |  | 5.660000 | 800 | Clear | clear sky | 01d | 22 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 29045100 | "BASE NAVAL [29045100]" | 11.000000 | -74.783333 | 5.000000 | Climática Principal | Convencional | Suspendida | 1973-06-15 00:00:00 | 1992-09-15 00:00:00 | Atlantico | Barranquilla | Ay Pozo Hondo | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena | Directos al Bajo Magdalena entre Calamar y desembocadura | America/Bogota | 2022-01-10 23:00:00 | 0.000000 | 21.960000 | 26.100000 | 78.000000 | 1010.000000 |  | 26.100000 | 0.000000 | 10000.000000 | 20.000000 |  | 5.140000 | 800 | Clear | clear sky | 01n | 23 |


### Weather plots

![CNE_IDEAM_Station29045100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station29045100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station29045100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station29045100_OWM_Windspeed_20220111.png)
