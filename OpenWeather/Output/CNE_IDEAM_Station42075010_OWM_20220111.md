
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MITU [42075010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station42075010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.26,-70.24) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.26&lon=-70.24)


| Parameter | Value |
|---|---|
| Code | 42075010 |
| Name | MITU [42075010] |
| Latitude, ° | 1.26 |
| Longitude, ° | -70.24 |
| Elevation, m | 180 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-03-15 00:00:00 |
| Suspension date | NaT |
| State | Vaupes |
| County | Mitú |
| Stream | 0 |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Vaupes |
| SZH - Hydrographic subzone | Bajo Vaupés |

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

### (CNE index 3617) Open Weather values for station 42075010 - MITU [42075010]

JSON data from API OWM:

```
{'lat': 1.26, 'lon': -70.24, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641811604, 'sunset': 1641854990, 'temp': 33.81, 'feels_like': 32.87, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.3, 'uvi': 4.21, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 15, 'wind_gust': 3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.54, 'feels_like': 25.98, 'pressure': 1009, 'humidity': 70, 'dew_point': 19.67, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 68, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 24.69, 'feels_like': 25.12, 'pressure': 1010, 'humidity': 73, 'dew_point': 19.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 77, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.1, 'feels_like': 24.5, 'pressure': 1010, 'humidity': 74, 'dew_point': 19.18, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 82, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.54, 'feels_like': 23.91, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.85, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 69, 'wind_gust': 1.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 22.76, 'feels_like': 23.15, 'pressure': 1011, 'humidity': 79, 'dew_point': 18.93, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 353, 'wind_gust': 1.61, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 23.51, 'feels_like': 23.9, 'pressure': 1011, 'humidity': 76, 'dew_point': 19.04, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 61, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 21.72, 'feels_like': 22.06, 'pressure': 1011, 'humidity': 81, 'dew_point': 18.32, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 49, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.2, 'feels_like': 21.54, 'pressure': 1010, 'humidity': 83, 'dew_point': 18.2, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 41, 'wind_gust': 0.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.75, 'feels_like': 21.1, 'pressure': 1010, 'humidity': 85, 'dew_point': 18.14, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 52, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.47, 'feels_like': 20.79, 'pressure': 1010, 'humidity': 85, 'dew_point': 17.86, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 25, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.19, 'feels_like': 20.46, 'pressure': 1011, 'humidity': 84, 'dew_point': 17.4, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 13, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.92, 'feels_like': 20.13, 'pressure': 1011, 'humidity': 83, 'dew_point': 16.95, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 4, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 22.39, 'feels_like': 22.56, 'pressure': 1012, 'humidity': 72, 'dew_point': 17.1, 'uvi': 0.9, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 8, 'wind_gust': 5.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.73, 'feels_like': 25.82, 'pressure': 1013, 'humidity': 56, 'dew_point': 16.3, 'uvi': 2.99, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.9, 'wind_deg': 9, 'wind_gust': 5.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.46, 'feels_like': 28.5, 'pressure': 1014, 'humidity': 45, 'dew_point': 15.38, 'uvi': 6.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 1, 'wind_gust': 6.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 30.68, 'feels_like': 30.25, 'pressure': 1013, 'humidity': 38, 'dew_point': 14.74, 'uvi': 9.72, 'clouds': 85, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 5, 'wind_gust': 4.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 32.21, 'feels_like': 31.59, 'pressure': 1012, 'humidity': 34, 'dew_point': 14.37, 'uvi': 12.17, 'clouds': 83, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 3, 'wind_gust': 3.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.25, 'feels_like': 32.46, 'pressure': 1011, 'humidity': 31, 'dew_point': 13.84, 'uvi': 12.6, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 4, 'wind_gust': 3.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 33.85, 'feels_like': 33.09, 'pressure': 1009, 'humidity': 30, 'dew_point': 13.86, 'uvi': 10.92, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 3, 'wind_gust': 3.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 34.12, 'feels_like': 33.27, 'pressure': 1008, 'humidity': 29, 'dew_point': 13.57, 'uvi': 7.71, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 5, 'wind_gust': 3.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 33.81, 'feels_like': 32.87, 'pressure': 1007, 'humidity': 29, 'dew_point': 13.3, 'uvi': 4.21, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 15, 'wind_gust': 3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.06, 'feels_like': 32.22, 'pressure': 1007, 'humidity': 31, 'dew_point': 13.68, 'uvi': 1.57, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 26, 'wind_gust': 2.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.75, 'feels_like': 30.4, 'pressure': 1007, 'humidity': 48, 'dew_point': 17.57, 'uvi': 0.29, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 30, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1008, 'humidity': 54, 'dew_point': 16.24, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 50, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 00:00:00 | 83.000000 | 19.670000 | 25.980000 | 70.000000 | 1009.000000 |  | 25.540000 | 0.000000 | 10000.000000 | 68.000000 | 1.31 | 1.170000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 19.530000 | 25.120000 | 73.000000 | 1010.000000 |  | 24.690000 | 0.000000 | 10000.000000 | 77.000000 | 1.35 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 02:00:00 | 67.000000 | 19.180000 | 24.500000 | 74.000000 | 1010.000000 |  | 24.100000 | 0.000000 | 10000.000000 | 82.000000 | 1.12 | 1.040000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 03:00:00 | 49.000000 | 18.850000 | 23.910000 | 75.000000 | 1011.000000 |  | 23.540000 | 0.000000 | 10000.000000 | 69.000000 | 1.05 | 0.910000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 04:00:00 | 43.000000 | 18.930000 | 23.150000 | 79.000000 | 1011.000000 |  | 22.760000 | 0.000000 | 10000.000000 | 353.000000 | 1.61 | 1.080000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 05:00:00 | 54.000000 | 19.040000 | 23.900000 | 76.000000 | 1011.000000 |  | 23.510000 | 0.000000 | 10000.000000 | 61.000000 | 0.83 | 0.730000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 06:00:00 | 92.000000 | 18.320000 | 22.060000 | 81.000000 | 1011.000000 |  | 21.720000 | 0.000000 | 10000.000000 | 49.000000 | 0.52 | 0.470000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 07:00:00 | 82.000000 | 18.200000 | 21.540000 | 83.000000 | 1010.000000 |  | 21.200000 | 0.000000 | 10000.000000 | 41.000000 | 0.53 | 0.470000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 08:00:00 | 90.000000 | 18.140000 | 21.100000 | 85.000000 | 1010.000000 |  | 20.750000 | 0.000000 | 10000.000000 | 52.000000 | 0.63 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 09:00:00 | 93.000000 | 17.860000 | 20.790000 | 85.000000 | 1010.000000 |  | 20.470000 | 0.000000 | 10000.000000 | 25.000000 | 0.54 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 10:00:00 | 92.000000 | 17.400000 | 20.460000 | 84.000000 | 1011.000000 |  | 20.190000 | 0.000000 | 10000.000000 | 13.000000 | 1.02 | 0.970000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 11:00:00 | 94.000000 | 16.950000 | 20.130000 | 83.000000 | 1011.000000 |  | 19.920000 | 0.000000 | 10000.000000 | 4.000000 | 0.82 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 17.100000 | 22.560000 | 72.000000 | 1012.000000 |  | 22.390000 | 0.900000 | 10000.000000 | 8.000000 | 5.67 | 0.890000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.300000 | 25.820000 | 56.000000 | 1013.000000 |  | 25.730000 | 2.990000 | 10000.000000 | 9.000000 | 5.85 | 1.900000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 15.380000 | 28.500000 | 45.000000 | 1014.000000 |  | 28.460000 | 6.260000 | 10000.000000 | 1.000000 | 6.11 | 2.280000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 15:00:00 | 85.000000 | 14.740000 | 30.250000 | 38.000000 | 1013.000000 |  | 30.680000 | 9.720000 | 10000.000000 | 5.000000 | 4.81 | 2.530000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 16:00:00 | 83.000000 | 14.370000 | 31.590000 | 34.000000 | 1012.000000 |  | 32.210000 | 12.170000 | 10000.000000 | 3.000000 | 3.9 | 2.470000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 17:00:00 | 86.000000 | 13.840000 | 32.460000 | 31.000000 | 1011.000000 |  | 33.250000 | 12.600000 | 10000.000000 | 4.000000 | 3.69 | 2.440000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 13.860000 | 33.090000 | 30.000000 | 1009.000000 |  | 33.850000 | 10.920000 | 10000.000000 | 3.000000 | 3.49 | 2.270000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 19:00:00 | 76.000000 | 13.570000 | 33.270000 | 29.000000 | 1008.000000 |  | 34.120000 | 7.710000 | 10000.000000 | 5.000000 | 3.1 | 1.990000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 20:00:00 | 88.000000 | 13.300000 | 32.870000 | 29.000000 | 1007.000000 |  | 33.810000 | 4.210000 | 10000.000000 | 15.000000 | 3 | 1.820000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 21:00:00 | 91.000000 | 13.680000 | 32.220000 | 31.000000 | 1007.000000 |  | 33.060000 | 1.570000 | 10000.000000 | 26.000000 | 2.98 | 1.730000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 17.570000 | 30.400000 | 48.000000 | 1007.000000 |  | 29.750000 | 0.290000 | 10000.000000 | 30.000000 | 0.81 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 42075010 | "MITU [42075010]" | 1.260000 | -70.240000 | 180.000000 | Climática Principal | Convencional | Activa | 1985-03-15 00:00:00 | NaT | Vaupes | Mitú | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Amazonas | Vaupes | Bajo Vaupés | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 16.240000 | 26.280000 | 54.000000 | 1008.000000 |  | 26.280000 | 0.000000 | 10000.000000 | 50.000000 | 0.51 | 0.470000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station42075010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station42075010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station42075010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station42075010_OWM_Windspeed_20220111.png)
