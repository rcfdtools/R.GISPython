
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA CHORRERA [47075010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station47075010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=-1.44461111,-72.78958333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=-1.44461111&lon=-72.78958333)


| Parameter | Value |
|---|---|
| Code | 47075010 |
| Name | LA CHORRERA [47075010] |
| Latitude, ° | -1.44461111 |
| Longitude, ° | -72.78958333 |
| Elevation, m | 160 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-06-15 00:00:00 |
| Suspension date | NaT |
| State | Amazonas |
| County | La Chorrera |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Putumayo |
| SZH - Hydrographic subzone | Río Igará-Paraná |

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

### (CNE index 3797) Open Weather values for station 47075010 - LA CHORRERA [47075010]

JSON data from API OWM:

```
{'lat': -1.4446, 'lon': -72.7896, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641811954, 'sunset': 1641855863, 'temp': 34.13, 'feels_like': 33.83, 'pressure': 1007, 'humidity': 32, 'dew_point': 15.1, 'uvi': 5.14, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 36, 'wind_gust': 3.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.71, 'feels_like': 26.03, 'pressure': 1008, 'humidity': 65, 'dew_point': 18.64, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 78, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 24.88, 'feels_like': 25.17, 'pressure': 1009, 'humidity': 67, 'dew_point': 18.34, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 76, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.21, 'feels_like': 24.49, 'pressure': 1010, 'humidity': 69, 'dew_point': 18.17, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 61, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.58, 'feels_like': 23.85, 'pressure': 1011, 'humidity': 71, 'dew_point': 18.02, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 66, 'wind_gust': 2.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.06, 'feels_like': 23.35, 'pressure': 1011, 'humidity': 74, 'dew_point': 18.18, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 63, 'wind_gust': 2.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.76, 'feels_like': 23.05, 'pressure': 1010, 'humidity': 75, 'dew_point': 18.1, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 64, 'wind_gust': 1.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.13, 'feels_like': 22.41, 'pressure': 1010, 'humidity': 77, 'dew_point': 17.91, 'uvi': 0, 'clouds': 16, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 35, 'wind_gust': 1.35, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 21.59, 'feels_like': 21.87, 'pressure': 1009, 'humidity': 79, 'dew_point': 17.79, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 357, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 21.27, 'feels_like': 21.54, 'pressure': 1009, 'humidity': 80, 'dew_point': 17.68, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 35, 'wind_gust': 2.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.05, 'feels_like': 21.33, 'pressure': 1009, 'humidity': 81, 'dew_point': 17.67, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 56, 'wind_gust': 2.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.97, 'feels_like': 21.24, 'pressure': 1010, 'humidity': 81, 'dew_point': 17.59, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 51, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.78, 'feels_like': 21.03, 'pressure': 1011, 'humidity': 81, 'dew_point': 17.4, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 51, 'wind_gust': 3.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 22.88, 'feels_like': 23.18, 'pressure': 1012, 'humidity': 75, 'dew_point': 18.22, 'uvi': 0.76, 'clouds': 28, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 45, 'wind_gust': 8.68, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 25.94, 'feels_like': 26.18, 'pressure': 1013, 'humidity': 61, 'dew_point': 17.84, 'uvi': 2.76, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 38, 'wind_gust': 7.1, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 28.7, 'feels_like': 29.51, 'pressure': 1013, 'humidity': 52, 'dew_point': 17.88, 'uvi': 6.07, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 40, 'wind_gust': 6.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 30.92, 'feels_like': 31.42, 'pressure': 1013, 'humidity': 44, 'dew_point': 17.25, 'uvi': 9.74, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.8, 'wind_deg': 39, 'wind_gust': 5.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 32.39, 'feels_like': 32.48, 'pressure': 1011, 'humidity': 38, 'dew_point': 16.26, 'uvi': 12.51, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.93, 'wind_deg': 35, 'wind_gust': 5.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.45, 'feels_like': 33.44, 'pressure': 1010, 'humidity': 35, 'dew_point': 15.9, 'uvi': 13.33, 'clouds': 68, 'visibility': 10000, 'wind_speed': 2.7, 'wind_deg': 32, 'wind_gust': 4.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 34.05, 'feels_like': 34.12, 'pressure': 1009, 'humidity': 34, 'dew_point': 15.97, 'uvi': 11.92, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 32, 'wind_gust': 4.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.28, 'feels_like': 34.25, 'pressure': 1008, 'humidity': 33, 'dew_point': 15.7, 'uvi': 8.87, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 35, 'wind_gust': 3.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 34.13, 'feels_like': 33.83, 'pressure': 1007, 'humidity': 32, 'dew_point': 15.1, 'uvi': 5.14, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 36, 'wind_gust': 3.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.57, 'feels_like': 33.61, 'pressure': 1006, 'humidity': 35, 'dew_point': 16.01, 'uvi': 2.11, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.98, 'wind_deg': 45, 'wind_gust': 3.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.93, 'feels_like': 32.12, 'pressure': 1006, 'humidity': 48, 'dew_point': 18.64, 'uvi': 0.48, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 66, 'wind_gust': 3.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.57, 'feels_like': 26.57, 'pressure': 1007, 'humidity': 60, 'dew_point': 18.17, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 77, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 00:00:00 | 90.000000 | 18.640000 | 26.030000 | 65.000000 | 1008.000000 |  | 25.710000 | 0.000000 | 10000.000000 | 78.000000 | 1.41 | 1.350000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 01:00:00 | 93.000000 | 18.340000 | 25.170000 | 67.000000 | 1009.000000 |  | 24.880000 | 0.000000 | 10000.000000 | 76.000000 | 1.4 | 1.270000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 02:00:00 | 86.000000 | 18.170000 | 24.490000 | 69.000000 | 1010.000000 |  | 24.210000 | 0.000000 | 10000.000000 | 61.000000 | 1.25 | 1.150000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 03:00:00 | 73.000000 | 18.020000 | 23.850000 | 71.000000 | 1011.000000 |  | 23.580000 | 0.000000 | 10000.000000 | 66.000000 | 2.15 | 1.310000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 04:00:00 | 74.000000 | 18.180000 | 23.350000 | 74.000000 | 1011.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 63.000000 | 2.71 | 1.300000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 05:00:00 | 68.000000 | 18.100000 | 23.050000 | 75.000000 | 1010.000000 |  | 22.760000 | 0.000000 | 10000.000000 | 64.000000 | 1.42 | 1.140000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 06:00:00 | 16.000000 | 17.910000 | 22.410000 | 77.000000 | 1010.000000 |  | 22.130000 | 0.000000 | 10000.000000 | 35.000000 | 1.35 | 1.050000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 07:00:00 | 26.000000 | 17.790000 | 21.870000 | 79.000000 | 1009.000000 |  | 21.590000 | 0.000000 | 10000.000000 | 357.000000 | 1.11 | 1.040000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 08:00:00 | 60.000000 | 17.680000 | 21.540000 | 80.000000 | 1009.000000 |  | 21.270000 | 0.000000 | 10000.000000 | 35.000000 | 2.85 | 1.300000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 09:00:00 | 61.000000 | 17.670000 | 21.330000 | 81.000000 | 1009.000000 |  | 21.050000 | 0.000000 | 10000.000000 | 56.000000 | 2.45 | 1.180000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 10:00:00 | 51.000000 | 17.590000 | 21.240000 | 81.000000 | 1010.000000 |  | 20.970000 | 0.000000 | 10000.000000 | 51.000000 | 2.2 | 1.170000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 11:00:00 | 56.000000 | 17.400000 | 21.030000 | 81.000000 | 1011.000000 |  | 20.780000 | 0.000000 | 10000.000000 | 51.000000 | 3.63 | 1.110000 | 803 | Clouds | broken clouds | 04d | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 12:00:00 | 28.000000 | 18.220000 | 23.180000 | 75.000000 | 1012.000000 |  | 22.880000 | 0.760000 | 10000.000000 | 45.000000 | 8.68 | 1.140000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 13:00:00 | 38.000000 | 17.840000 | 26.180000 | 61.000000 | 1013.000000 |  | 25.940000 | 2.760000 | 10000.000000 | 38.000000 | 7.1 | 2.180000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 14:00:00 | 63.000000 | 17.880000 | 29.510000 | 52.000000 | 1013.000000 |  | 28.700000 | 6.070000 | 10000.000000 | 40.000000 | 6.8 | 2.450000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 15:00:00 | 54.000000 | 17.250000 | 31.420000 | 44.000000 | 1013.000000 |  | 30.920000 | 9.740000 | 10000.000000 | 39.000000 | 5.81 | 2.800000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 16:00:00 | 61.000000 | 16.260000 | 32.480000 | 38.000000 | 1011.000000 |  | 32.390000 | 12.510000 | 10000.000000 | 35.000000 | 5.24 | 2.930000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 17:00:00 | 68.000000 | 15.900000 | 33.440000 | 35.000000 | 1010.000000 |  | 33.450000 | 13.330000 | 10000.000000 | 32.000000 | 4.73 | 2.700000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 15.970000 | 34.120000 | 34.000000 | 1009.000000 |  | 34.050000 | 11.920000 | 10000.000000 | 32.000000 | 4.18 | 2.500000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 15.700000 | 34.250000 | 33.000000 | 1008.000000 |  | 34.280000 | 8.870000 | 10000.000000 | 35.000000 | 3.68 | 2.260000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 20:00:00 | 96.000000 | 15.100000 | 33.830000 | 32.000000 | 1007.000000 |  | 34.130000 | 5.140000 | 10000.000000 | 36.000000 | 3.5 | 2.160000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 16.010000 | 33.610000 | 35.000000 | 1006.000000 |  | 33.570000 | 2.110000 | 10000.000000 | 45.000000 | 3.51 | 1.980000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 22:00:00 | 61.000000 | 18.640000 | 32.120000 | 48.000000 | 1006.000000 |  | 30.930000 | 0.480000 | 10000.000000 | 66.000000 | 3.25 | 1.380000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47075010 | "LA CHORRERA [47075010]" | -1.444611 | -72.789583 | 160.000000 | Climática Principal | Convencional | Activa | 1986-06-15 00:00:00 | NaT | Amazonas | La Chorrera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Amazonas | Putumayo | Río Igará-Paraná | America/Bogota | 2022-01-10 23:00:00 | 54.000000 | 18.170000 | 26.570000 | 60.000000 | 1007.000000 |  | 26.570000 | 0.000000 | 10000.000000 | 77.000000 | 1.2 | 1.110000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station47075010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station47075010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station47075010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47075010_OWM_Windspeed_20220111.png)
