
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MANAURE [15075030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15075030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.78105556,-72.4635) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.78105556&lon=-72.4635)


| Parameter | Value |
|---|---|
| Code | 15075030 |
| Name | MANAURE [15075030] |
| Latitude, ° | 11.78105556 |
| Longitude, ° | -72.4635 |
| Elevation, m | 1 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1940-01-15 00:00:00 |
| Suspension date | NaT |
| State | La Guajira |
| County | Manaure |
| Stream | Cno Cicuco |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Directos Caribe - Ay.Sharimahana Alta Guajira |

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

### (CNE index 2632) Open Weather values for station 15075030 - MANAURE [15075030]

JSON data from API OWM:

```
{'lat': 11.7811, 'lon': -72.4635, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813167, 'sunset': 1641854495, 'temp': 28.08, 'feels_like': 28.92, 'pressure': 1010, 'humidity': 54, 'dew_point': 17.9, 'uvi': 3.27, 'clouds': 20, 'visibility': 10000, 'wind_speed': 7.25, 'wind_deg': 84, 'wind_gust': 9.22, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 29.08, 'feels_like': 32.53, 'pressure': 1014, 'humidity': 68, 'dew_point': 22.57, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 7.97, 'wind_deg': 69, 'wind_gust': 11.74, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 29.08, 'feels_like': 33.49, 'pressure': 1014, 'humidity': 73, 'dew_point': 23.74, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 7.45, 'wind_deg': 70, 'wind_gust': 11.16, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.72, 'feels_like': 25.23, 'pressure': 1015, 'humidity': 76, 'dew_point': 20.21, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 6.39, 'wind_deg': 76, 'wind_gust': 10.03, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 24.43, 'feels_like': 24.91, 'pressure': 1015, 'humidity': 76, 'dew_point': 19.92, 'uvi': 0, 'clouds': 3, 'visibility': 10000, 'wind_speed': 5.33, 'wind_deg': 81, 'wind_gust': 8.55, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 24.25, 'feels_like': 24.74, 'pressure': 1014, 'humidity': 77, 'dew_point': 19.96, 'uvi': 0, 'clouds': 3, 'visibility': 10000, 'wind_speed': 5, 'wind_deg': 82, 'wind_gust': 8.07, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 24.04, 'feels_like': 24.54, 'pressure': 1014, 'humidity': 78, 'dew_point': 19.97, 'uvi': 0, 'clouds': 2, 'visibility': 10000, 'wind_speed': 4.65, 'wind_deg': 86, 'wind_gust': 7.64, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 23.73, 'feels_like': 24.22, 'pressure': 1013, 'humidity': 79, 'dew_point': 19.87, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 86, 'wind_gust': 8.06, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 23.39, 'feels_like': 23.9, 'pressure': 1013, 'humidity': 81, 'dew_point': 19.94, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 4.42, 'wind_deg': 83, 'wind_gust': 7.75, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 23.13, 'feels_like': 23.67, 'pressure': 1012, 'humidity': 83, 'dew_point': 20.08, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 4.04, 'wind_deg': 84, 'wind_gust': 6.68, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641805200, 'temp': 23, 'feels_like': 23.55, 'pressure': 1013, 'humidity': 84, 'dew_point': 20.15, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 3.91, 'wind_deg': 77, 'wind_gust': 6.18, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641808800, 'temp': 23.04, 'feels_like': 23.59, 'pressure': 1013, 'humidity': 84, 'dew_point': 20.19, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 4.06, 'wind_deg': 74, 'wind_gust': 7.08, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 23.08, 'feels_like': 23.64, 'pressure': 1014, 'humidity': 84, 'dew_point': 20.23, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 4.18, 'wind_deg': 75, 'wind_gust': 7.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 23.08, 'feels_like': 23.56, 'pressure': 1014, 'humidity': 81, 'dew_point': 19.64, 'uvi': 0.38, 'clouds': 66, 'visibility': 10000, 'wind_speed': 4.43, 'wind_deg': 79, 'wind_gust': 8.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.08, 'feels_like': 25.65, 'pressure': 1016, 'humidity': 77, 'dew_point': 20.76, 'uvi': 1.7, 'clouds': 59, 'visibility': 10000, 'wind_speed': 5.59, 'wind_deg': 91, 'wind_gust': 8.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.08, 'feels_like': 28.91, 'pressure': 1016, 'humidity': 69, 'dew_point': 20.9, 'uvi': 4.06, 'clouds': 36, 'visibility': 10000, 'wind_speed': 7.09, 'wind_deg': 91, 'wind_gust': 9.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 29.08, 'feels_like': 31.17, 'pressure': 1016, 'humidity': 60, 'dew_point': 20.53, 'uvi': 6.81, 'clouds': 26, 'visibility': 10000, 'wind_speed': 7.96, 'wind_deg': 89, 'wind_gust': 10.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 32.08, 'feels_like': 35.54, 'pressure': 1015, 'humidity': 54, 'dew_point': 21.6, 'uvi': 9.08, 'clouds': 20, 'visibility': 10000, 'wind_speed': 8.02, 'wind_deg': 93, 'wind_gust': 9.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 31.08, 'feels_like': 33.16, 'pressure': 1014, 'humidity': 52, 'dew_point': 20.07, 'uvi': 9.69, 'clouds': 17, 'visibility': 10000, 'wind_speed': 7.42, 'wind_deg': 92, 'wind_gust': 9.45, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 32.08, 'feels_like': 35.54, 'pressure': 1012, 'humidity': 54, 'dew_point': 21.6, 'uvi': 8.52, 'clouds': 10, 'visibility': 10000, 'wind_speed': 6.88, 'wind_deg': 81, 'wind_gust': 8.91, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 33.08, 'feels_like': 38, 'pressure': 1011, 'humidity': 55, 'dew_point': 22.83, 'uvi': 6.06, 'clouds': 13, 'visibility': 10000, 'wind_speed': 7.06, 'wind_deg': 75, 'wind_gust': 8.93, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 28.08, 'feels_like': 28.92, 'pressure': 1010, 'humidity': 54, 'dew_point': 17.9, 'uvi': 3.27, 'clouds': 20, 'visibility': 10000, 'wind_speed': 7.25, 'wind_deg': 84, 'wind_gust': 9.22, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641848400, 'temp': 28.08, 'feels_like': 28.82, 'pressure': 1010, 'humidity': 53, 'dew_point': 17.61, 'uvi': 1.15, 'clouds': 36, 'visibility': 10000, 'wind_speed': 7.65, 'wind_deg': 85, 'wind_gust': 9.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 27.08, 'feels_like': 27.82, 'pressure': 1011, 'humidity': 55, 'dew_point': 17.27, 'uvi': 0.2, 'clouds': 45, 'visibility': 10000, 'wind_speed': 7.35, 'wind_deg': 81, 'wind_gust': 9.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 29.08, 'feels_like': 31.49, 'pressure': 1011, 'humidity': 62, 'dew_point': 21.06, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 5.78, 'wind_deg': 73, 'wind_gust': 8.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 00:00:00 | 5.000000 | 22.570000 | 32.530000 | 68.000000 | 1014.000000 |  | 29.080000 | 0.000000 | 10000.000000 | 69.000000 | 11.74 | 7.970000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 01:00:00 | 6.000000 | 23.740000 | 33.490000 | 73.000000 | 1014.000000 |  | 29.080000 | 0.000000 | 10000.000000 | 70.000000 | 11.16 | 7.450000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 02:00:00 | 5.000000 | 20.210000 | 25.230000 | 76.000000 | 1015.000000 |  | 24.720000 | 0.000000 | 10000.000000 | 76.000000 | 10.03 | 6.390000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 03:00:00 | 3.000000 | 19.920000 | 24.910000 | 76.000000 | 1015.000000 |  | 24.430000 | 0.000000 | 10000.000000 | 81.000000 | 8.55 | 5.330000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 04:00:00 | 3.000000 | 19.960000 | 24.740000 | 77.000000 | 1014.000000 |  | 24.250000 | 0.000000 | 10000.000000 | 82.000000 | 8.07 | 5.000000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 05:00:00 | 2.000000 | 19.970000 | 24.540000 | 78.000000 | 1014.000000 |  | 24.040000 | 0.000000 | 10000.000000 | 86.000000 | 7.64 | 4.650000 | 800 | Clear | clear sky | 01n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 06:00:00 | 5.000000 | 19.870000 | 24.220000 | 79.000000 | 1013.000000 |  | 23.730000 | 0.000000 | 10000.000000 | 86.000000 | 8.06 | 4.630000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 07:00:00 | 6.000000 | 19.940000 | 23.900000 | 81.000000 | 1013.000000 |  | 23.390000 | 0.000000 | 10000.000000 | 83.000000 | 7.75 | 4.420000 | 800 | Clear | clear sky | 01n | 07 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 08:00:00 | 8.000000 | 20.080000 | 23.670000 | 83.000000 | 1012.000000 |  | 23.130000 | 0.000000 | 10000.000000 | 84.000000 | 6.68 | 4.040000 | 800 | Clear | clear sky | 01n | 08 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 09:00:00 | 11.000000 | 20.150000 | 23.550000 | 84.000000 | 1013.000000 |  | 23.000000 | 0.000000 | 10000.000000 | 77.000000 | 6.18 | 3.910000 | 801 | Clouds | few clouds | 02n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 10:00:00 | 31.000000 | 20.190000 | 23.590000 | 84.000000 | 1013.000000 |  | 23.040000 | 0.000000 | 10000.000000 | 74.000000 | 7.08 | 4.060000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 11:00:00 | 45.000000 | 20.230000 | 23.640000 | 84.000000 | 1014.000000 |  | 23.080000 | 0.000000 | 10000.000000 | 75.000000 | 7.17 | 4.180000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 12:00:00 | 66.000000 | 19.640000 | 23.560000 | 81.000000 | 1014.000000 |  | 23.080000 | 0.380000 | 10000.000000 | 79.000000 | 8.56 | 4.430000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 13:00:00 | 59.000000 | 20.760000 | 25.650000 | 77.000000 | 1016.000000 |  | 25.080000 | 1.700000 | 10000.000000 | 91.000000 | 8.98 | 5.590000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 14:00:00 | 36.000000 | 20.900000 | 28.910000 | 69.000000 | 1016.000000 |  | 27.080000 | 4.060000 | 10000.000000 | 91.000000 | 9.4 | 7.090000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 15:00:00 | 26.000000 | 20.530000 | 31.170000 | 60.000000 | 1016.000000 |  | 29.080000 | 6.810000 | 10000.000000 | 89.000000 | 10.13 | 7.960000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 16:00:00 | 20.000000 | 21.600000 | 35.540000 | 54.000000 | 1015.000000 |  | 32.080000 | 9.080000 | 10000.000000 | 93.000000 | 9.89 | 8.020000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 17:00:00 | 17.000000 | 20.070000 | 33.160000 | 52.000000 | 1014.000000 |  | 31.080000 | 9.690000 | 10000.000000 | 92.000000 | 9.45 | 7.420000 | 801 | Clouds | few clouds | 02d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 18:00:00 | 10.000000 | 21.600000 | 35.540000 | 54.000000 | 1012.000000 |  | 32.080000 | 8.520000 | 10000.000000 | 81.000000 | 8.91 | 6.880000 | 800 | Clear | clear sky | 01d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 19:00:00 | 13.000000 | 22.830000 | 38.000000 | 55.000000 | 1011.000000 |  | 33.080000 | 6.060000 | 10000.000000 | 75.000000 | 8.93 | 7.060000 | 801 | Clouds | few clouds | 02d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 20:00:00 | 20.000000 | 17.900000 | 28.920000 | 54.000000 | 1010.000000 |  | 28.080000 | 3.270000 | 10000.000000 | 84.000000 | 9.22 | 7.250000 | 801 | Clouds | few clouds | 02d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 21:00:00 | 36.000000 | 17.610000 | 28.820000 | 53.000000 | 1010.000000 |  | 28.080000 | 1.150000 | 10000.000000 | 85.000000 | 9.81 | 7.650000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 22:00:00 | 45.000000 | 17.270000 | 27.820000 | 55.000000 | 1011.000000 |  | 27.080000 | 0.200000 | 10000.000000 | 81.000000 | 9.81 | 7.350000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15075030 | "MANAURE [15075030]" | 11.781056 | -72.463500 | 1.000000 | Climática Principal | Convencional | Activa | 1940-01-15 00:00:00 | NaT | La Guajira | Manaure | Cno Cicuco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Directos Caribe - Ay.Sharimahana Alta Guajira | America/Bogota | 2022-01-10 23:00:00 | 55.000000 | 21.060000 | 31.490000 | 62.000000 | 1011.000000 |  | 29.080000 | 0.000000 | 10000.000000 | 73.000000 | 8.84 | 5.780000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15075030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15075030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15075030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15075030_OWM_Windspeed_20220111.png)
