
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VIOLETAS LAS [23085210] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23085210_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.34888889,-75.00277778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.34888889&lon=-75.00277778)


| Parameter | Value |
|---|---|
| Code | 23085210 |
| Name | VIOLETAS LAS [23085210] |
| Latitude, ° | 6.34888889 |
| Longitude, ° | -75.00277778 |
| Elevation, m | 116 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1982-11-15 00:00:00 |
| Suspension date | 2011-09-30 00:00:00 |
| State | Antioquia |
| County | San Rafael |
| Stream | Penderisco |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Nare |

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

### (CNE index 839) Open Weather values for station 23085210 - VIOLETAS LAS [23085210]

JSON data from API OWM:

```
{'lat': 6.3489, 'lon': -75.0028, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813240, 'sunset': 1641855640, 'temp': 25.18, 'feels_like': 26.21, 'pressure': 1011, 'humidity': 94, 'dew_point': 24.14, 'uvi': 1.6, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 55, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, 'hourly': [{'dt': 1641772800, 'temp': 22.98, 'feels_like': 23.87, 'pressure': 1014, 'humidity': 97, 'dew_point': 22.48, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 293, 'wind_gust': 0.93, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 22.94, 'feels_like': 23.85, 'pressure': 1015, 'humidity': 98, 'dew_point': 22.61, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 275, 'wind_gust': 1.04, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 21.97, 'feels_like': 22.76, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.47, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 275, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 21.95, 'feels_like': 22.76, 'pressure': 1016, 'humidity': 98, 'dew_point': 21.62, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 266, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 21.95, 'feels_like': 22.76, 'pressure': 1015, 'humidity': 98, 'dew_point': 21.62, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 268, 'wind_gust': 1.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.95, 'feels_like': 21.66, 'pressure': 1015, 'humidity': 98, 'dew_point': 20.62, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 269, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.95, 'feels_like': 21.63, 'pressure': 1014, 'humidity': 97, 'dew_point': 20.46, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 272, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.95, 'feels_like': 21.63, 'pressure': 1014, 'humidity': 97, 'dew_point': 20.46, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 276, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.93, 'feels_like': 21.61, 'pressure': 1013, 'humidity': 97, 'dew_point': 20.44, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 277, 'wind_gust': 1.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 19.96, 'feels_like': 20.52, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.3, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 274, 'wind_gust': 1.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 20.93, 'feels_like': 21.59, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.27, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 277, 'wind_gust': 1.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 20.08, 'feels_like': 20.65, 'pressure': 1015, 'humidity': 96, 'dew_point': 19.42, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 277, 'wind_gust': 1.18, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 20.95, 'feels_like': 21.53, 'pressure': 1016, 'humidity': 93, 'dew_point': 19.78, 'uvi': 0.35, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 275, 'wind_gust': 1.33, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 21.84, 'feels_like': 22.27, 'pressure': 1016, 'humidity': 84, 'dew_point': 19.02, 'uvi': 1.93, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 282, 'wind_gust': 0.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 22.92, 'feels_like': 23.25, 'pressure': 1016, 'humidity': 76, 'dew_point': 18.47, 'uvi': 4.84, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 84, 'wind_gust': 1.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 22.96, 'feels_like': 23.09, 'pressure': 1016, 'humidity': 68, 'dew_point': 16.74, 'uvi': 8.39, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 85, 'wind_gust': 1.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641830400, 'temp': 23.85, 'feels_like': 23.96, 'pressure': 1015, 'humidity': 64, 'dew_point': 16.63, 'uvi': 6.44, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 86, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641834000, 'temp': 23.77, 'feels_like': 23.93, 'pressure': 1014, 'humidity': 66, 'dew_point': 17.04, 'uvi': 7.1, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 85, 'wind_gust': 1.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 22.22, 'feels_like': 22.51, 'pressure': 1013, 'humidity': 77, 'dew_point': 18, 'uvi': 6.51, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 82, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641841200, 'temp': 24.27, 'feels_like': 25, 'pressure': 1012, 'humidity': 86, 'dew_point': 21.78, 'uvi': 2.71, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 80, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641844800, 'temp': 25.18, 'feels_like': 26.21, 'pressure': 1011, 'humidity': 94, 'dew_point': 24.14, 'uvi': 1.6, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 55, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641848400, 'temp': 25.08, 'feels_like': 26.12, 'pressure': 1011, 'humidity': 95, 'dew_point': 24.22, 'uvi': 0.65, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 40, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641852000, 'temp': 24.08, 'feels_like': 25.02, 'pressure': 1012, 'humidity': 95, 'dew_point': 23.23, 'uvi': 0.21, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 26, 'wind_gust': 1.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}, {'dt': 1641855600, 'temp': 23.06, 'feels_like': 23.95, 'pressure': 1013, 'humidity': 97, 'dew_point': 22.56, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 313, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 00:00:00 | 33.000000 | 22.480000 | 23.870000 | 97.000000 | 1014.000000 |  | 22.980000 | 0.000000 | 10000.000000 | 293.000000 | 0.93 | 1.060000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 01:00:00 | 50.000000 | 22.610000 | 23.850000 | 98.000000 | 1015.000000 |  | 22.940000 | 0.000000 | 10000.000000 | 275.000000 | 1.04 | 1.220000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 02:00:00 | 64.000000 | 21.470000 | 22.760000 | 97.000000 | 1015.000000 |  | 21.970000 | 0.000000 | 10000.000000 | 275.000000 | 1.11 | 1.400000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 03:00:00 | 69.000000 | 21.620000 | 22.760000 | 98.000000 | 1016.000000 |  | 21.950000 | 0.000000 | 10000.000000 | 266.000000 | 1.24 | 1.530000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 04:00:00 | 72.000000 | 21.620000 | 22.760000 | 98.000000 | 1015.000000 |  | 21.950000 | 0.000000 | 10000.000000 | 268.000000 | 1.28 | 1.570000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 05:00:00 | 70.000000 | 20.620000 | 21.660000 | 98.000000 | 1015.000000 |  | 20.950000 | 0.000000 | 10000.000000 | 269.000000 | 1.33 | 1.640000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 06:00:00 | 73.000000 | 20.460000 | 21.630000 | 97.000000 | 1014.000000 |  | 20.950000 | 0.000000 | 10000.000000 | 272.000000 | 1.33 | 1.720000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 07:00:00 | 59.000000 | 20.460000 | 21.630000 | 97.000000 | 1014.000000 |  | 20.950000 | 0.000000 | 10000.000000 | 276.000000 | 1.34 | 1.690000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 08:00:00 | 53.000000 | 20.440000 | 21.610000 | 97.000000 | 1013.000000 |  | 20.930000 | 0.000000 | 10000.000000 | 277.000000 | 1.74 | 1.680000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 09:00:00 | 44.000000 | 19.300000 | 20.520000 | 96.000000 | 1013.000000 |  | 19.960000 | 0.000000 | 10000.000000 | 274.000000 | 1.24 | 1.640000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 10:00:00 | 39.000000 | 20.270000 | 21.590000 | 96.000000 | 1014.000000 |  | 20.930000 | 0.000000 | 10000.000000 | 277.000000 | 1.71 | 1.630000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 11:00:00 | 45.000000 | 19.420000 | 20.650000 | 96.000000 | 1015.000000 |  | 20.080000 | 0.000000 | 10000.000000 | 277.000000 | 1.18 | 1.430000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 12:00:00 | 30.000000 | 19.780000 | 21.530000 | 93.000000 | 1016.000000 |  | 20.950000 | 0.350000 | 10000.000000 | 275.000000 | 1.33 | 1.170000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 13:00:00 | 35.000000 | 19.020000 | 22.270000 | 84.000000 | 1016.000000 |  | 21.840000 | 1.930000 | 10000.000000 | 282.000000 | 0.55 | 0.210000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 14:00:00 | 39.000000 | 18.470000 | 23.250000 | 76.000000 | 1016.000000 |  | 22.920000 | 4.840000 | 10000.000000 | 84.000000 | 1.24 | 1.260000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 15:00:00 | 39.000000 | 16.740000 | 23.090000 | 68.000000 | 1016.000000 | 0.11 | 22.960000 | 8.390000 | 10000.000000 | 85.000000 | 1.29 | 1.770000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 16:00:00 | 53.000000 | 16.630000 | 23.960000 | 64.000000 | 1015.000000 | 0.1 | 23.850000 | 6.440000 | 10000.000000 | 86.000000 | 1.46 | 1.910000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 17:00:00 | 62.000000 | 17.040000 | 23.930000 | 66.000000 | 1014.000000 |  | 23.770000 | 7.100000 | 10000.000000 | 85.000000 | 1.84 | 1.660000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 18.000000 | 22.510000 | 77.000000 | 1013.000000 | 0.13 | 22.220000 | 6.510000 | 10000.000000 | 82.000000 | 2.1 | 1.440000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 19:00:00 | 94.000000 | 21.780000 | 25.000000 | 86.000000 | 1012.000000 | 0.37 | 24.270000 | 2.710000 | 10000.000000 | 80.000000 | 1.65 | 1.070000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 20:00:00 | 97.000000 | 24.140000 | 26.210000 | 94.000000 | 1011.000000 | 0.7 | 25.180000 | 1.600000 | 10000.000000 | 55.000000 | 1.02 | 0.530000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 24.220000 | 26.120000 | 95.000000 | 1011.000000 | 0.77 | 25.080000 | 0.650000 | 10000.000000 | 40.000000 | 1.22 | 0.560000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 23.230000 | 25.020000 | 95.000000 | 1012.000000 | 0.83 | 24.080000 | 0.210000 | 10000.000000 | 26.000000 | 1.33 | 0.630000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085210 | "VIOLETAS LAS [23085210]" | 6.348889 | -75.002778 | 116.000000 | Climática Principal | Convencional | Suspendida | 1982-11-15 00:00:00 | 2011-09-30 00:00:00 | Antioquia | San Rafael | Penderisco | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Río Nare | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 22.560000 | 23.950000 | 97.000000 | 1013.000000 | 0.33 | 23.060000 | 0.000000 | 10000.000000 | 313.000000 | 0.79 | 0.800000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23085210_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23085210_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23085210_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085210_OWM_Windspeed_20220111.png)
