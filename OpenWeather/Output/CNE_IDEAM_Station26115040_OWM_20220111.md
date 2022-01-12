
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CENT ADMO LA UNION [26115040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26115040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.53,-76.06) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.53&lon=-76.06)


| Parameter | Value |
|---|---|
| Code | 26115040 |
| Name | CENT ADMO LA UNION [26115040] |
| Latitude, ° | 4.53 |
| Longitude, ° | -76.06 |
| Elevation, m | 934 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1967-02-15 00:00:00 |
| Suspension date | 2020-10-20 12:18:23 |
| State | Valle del Cauca |
| County | La Unión (Valle del cauca) |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Rios Pescador - RUT - Chanco - Catarina y Cañaveral |

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

### (CNE index 4465) Open Weather values for station 26115040 - CENT ADMO LA UNION [26115040]

JSON data from API OWM:

```
{'lat': 4.53, 'lon': -76.06, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813317, 'sunset': 1641856071, 'temp': 24.93, 'feels_like': 25.54, 'pressure': 1010, 'humidity': 79, 'dew_point': 21.04, 'uvi': 5.01, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 268, 'wind_gust': 2.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, 'hourly': [{'dt': 1641772800, 'temp': 24.93, 'feels_like': 25.96, 'pressure': 1012, 'humidity': 95, 'dew_point': 24.07, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 283, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.67}}, {'dt': 1641776400, 'temp': 23.93, 'feels_like': 24.89, 'pressure': 1014, 'humidity': 96, 'dew_point': 23.25, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 283, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641780000, 'temp': 22.93, 'feels_like': 23.79, 'pressure': 1015, 'humidity': 96, 'dew_point': 22.26, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 267, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 21.93, 'feels_like': 22.71, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.43, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 273, 'wind_gust': 1.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 21.93, 'feels_like': 22.71, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.43, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 260, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 21.93, 'feels_like': 22.71, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.43, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 272, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.71, 'feels_like': 23.54, 'pressure': 1014, 'humidity': 96, 'dew_point': 22.04, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 262, 'wind_gust': 0.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 22.71, 'feels_like': 23.57, 'pressure': 1013, 'humidity': 97, 'dew_point': 22.21, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 237, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 18.26, 'feels_like': 18.67, 'pressure': 1013, 'humidity': 97, 'dew_point': 17.78, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 182, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641805200, 'temp': 18.51, 'feels_like': 18.98, 'pressure': 1013, 'humidity': 98, 'dew_point': 18.19, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 203, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641808800, 'temp': 21.71, 'feels_like': 22.5, 'pressure': 1014, 'humidity': 98, 'dew_point': 21.38, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 241, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641812400, 'temp': 20.93, 'feels_like': 21.64, 'pressure': 1015, 'humidity': 98, 'dew_point': 20.6, 'uvi': 0, 'clouds': 90, 'visibility': 9774, 'wind_speed': 0.1, 'wind_deg': 208, 'wind_gust': 0.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.41}}, {'dt': 1641816000, 'temp': 20.93, 'feels_like': 21.61, 'pressure': 1015, 'humidity': 97, 'dew_point': 20.44, 'uvi': 0.16, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 259, 'wind_gust': 0.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641819600, 'temp': 21.93, 'feels_like': 22.69, 'pressure': 1016, 'humidity': 96, 'dew_point': 21.26, 'uvi': 1.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 195, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641823200, 'temp': 23.93, 'feels_like': 24.83, 'pressure': 1017, 'humidity': 94, 'dew_point': 22.9, 'uvi': 3.6, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 345, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641826800, 'temp': 25.93, 'feels_like': 27.01, 'pressure': 1016, 'humidity': 93, 'dew_point': 24.71, 'uvi': 6.32, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 22, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641830400, 'temp': 24.93, 'feels_like': 25.67, 'pressure': 1015, 'humidity': 84, 'dew_point': 22.04, 'uvi': 9.61, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 3, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641834000, 'temp': 25.93, 'feels_like': 26.59, 'pressure': 1014, 'humidity': 77, 'dew_point': 21.59, 'uvi': 10.72, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 291, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.59}}, {'dt': 1641837600, 'temp': 25.93, 'feels_like': 26.51, 'pressure': 1012, 'humidity': 74, 'dew_point': 20.94, 'uvi': 9.98, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 273, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641841200, 'temp': 25.93, 'feels_like': 26.59, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.59, 'uvi': 8.32, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 276, 'wind_gust': 1.92, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641844800, 'temp': 24.93, 'feels_like': 25.54, 'pressure': 1010, 'humidity': 79, 'dew_point': 21.04, 'uvi': 5.01, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 268, 'wind_gust': 2.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641848400, 'temp': 23.93, 'feels_like': 24.49, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.47, 'uvi': 2.16, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 270, 'wind_gust': 2.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, {'dt': 1641852000, 'temp': 21.93, 'feels_like': 22.53, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.21, 'uvi': 0.44, 'clouds': 88, 'visibility': 4985, 'wind_speed': 1.42, 'wind_deg': 272, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641855600, 'temp': 19.93, 'feels_like': 20.41, 'pressure': 1012, 'humidity': 93, 'dew_point': 18.76, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 272, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.59}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 00:00:00 | 98.000000 | 24.070000 | 25.960000 | 95.000000 | 1012.000000 | 0.67 | 24.930000 | 0.000000 | 10000.000000 | 283.000000 | 1.5 | 1.420000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 23.250000 | 24.890000 | 96.000000 | 1014.000000 | 0.35 | 23.930000 | 0.000000 | 10000.000000 | 283.000000 | 1.31 | 1.230000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 02:00:00 | 96.000000 | 22.260000 | 23.790000 | 96.000000 | 1015.000000 |  | 22.930000 | 0.000000 | 10000.000000 | 267.000000 | 1.44 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 03:00:00 | 76.000000 | 21.430000 | 22.710000 | 97.000000 | 1015.000000 |  | 21.930000 | 0.000000 | 10000.000000 | 273.000000 | 1.17 | 0.920000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 04:00:00 | 65.000000 | 21.430000 | 22.710000 | 97.000000 | 1015.000000 |  | 21.930000 | 0.000000 | 10000.000000 | 260.000000 | 1.08 | 0.880000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 05:00:00 | 59.000000 | 21.430000 | 22.710000 | 97.000000 | 1015.000000 |  | 21.930000 | 0.000000 | 10000.000000 | 272.000000 | 0.95 | 0.740000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 06:00:00 | 34.000000 | 22.040000 | 23.540000 | 96.000000 | 1014.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 262.000000 | 0.67 | 0.490000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 07:00:00 | 58.000000 | 22.210000 | 23.570000 | 97.000000 | 1013.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 237.000000 | 0.76 | 0.510000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 08:00:00 | 76.000000 | 17.780000 | 18.670000 | 97.000000 | 1013.000000 | 0.2 | 18.260000 | 0.000000 | 10000.000000 | 182.000000 | 0.62 | 0.160000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 09:00:00 | 83.000000 | 18.190000 | 18.980000 | 98.000000 | 1013.000000 | 0.32 | 18.510000 | 0.000000 | 10000.000000 | 203.000000 | 0.55 | 0.260000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 10:00:00 | 87.000000 | 21.380000 | 22.500000 | 98.000000 | 1014.000000 | 0.53 | 21.710000 | 0.000000 | 10000.000000 | 241.000000 | 0.58 | 0.440000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 11:00:00 | 90.000000 | 20.600000 | 21.640000 | 98.000000 | 1015.000000 | 0.41 | 20.930000 | 0.000000 | 9774.000000 | 208.000000 | 0.29 | 0.100000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 20.440000 | 21.610000 | 97.000000 | 1015.000000 | 0.41 | 20.930000 | 0.160000 | 10000.000000 | 259.000000 | 0.28 | 0.200000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 21.260000 | 22.690000 | 96.000000 | 1016.000000 | 0.31 | 21.930000 | 1.420000 | 10000.000000 | 195.000000 | 0.61 | 0.170000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 22.900000 | 24.830000 | 94.000000 | 1017.000000 | 0.37 | 23.930000 | 3.600000 | 10000.000000 | 345.000000 | 0.64 | 0.230000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 24.710000 | 27.010000 | 93.000000 | 1016.000000 | 0.28 | 25.930000 | 6.320000 | 10000.000000 | 22.000000 | 0.94 | 0.580000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 16:00:00 | 91.000000 | 22.040000 | 25.670000 | 84.000000 | 1015.000000 | 0.32 | 24.930000 | 9.610000 | 10000.000000 | 3.000000 | 1.2 | 0.610000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 17:00:00 | 84.000000 | 21.590000 | 26.590000 | 77.000000 | 1014.000000 | 0.59 | 25.930000 | 10.720000 | 10000.000000 | 291.000000 | 1.31 | 0.610000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 18:00:00 | 55.000000 | 20.940000 | 26.510000 | 74.000000 | 1012.000000 | 0.76 | 25.930000 | 9.980000 | 10000.000000 | 273.000000 | 1.54 | 1.000000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 19:00:00 | 58.000000 | 21.590000 | 26.590000 | 77.000000 | 1011.000000 | 1.02 | 25.930000 | 8.320000 | 10000.000000 | 276.000000 | 1.92 | 1.440000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 20:00:00 | 76.000000 | 21.040000 | 25.540000 | 79.000000 | 1010.000000 | 1.09 | 24.930000 | 5.010000 | 10000.000000 | 268.000000 | 2.18 | 1.580000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 21:00:00 | 84.000000 | 20.470000 | 24.490000 | 81.000000 | 1010.000000 | 0.89 | 23.930000 | 2.160000 | 10000.000000 | 270.000000 | 2.08 | 1.480000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 22:00:00 | 88.000000 | 20.210000 | 22.530000 | 90.000000 | 1011.000000 | 1.35 | 21.930000 | 0.440000 | 4985.000000 | 272.000000 | 1.86 | 1.420000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115040 | "CENT ADMO LA UNION [26115040]" | 4.530000 | -76.060000 | 934.000000 | Climática Principal | Convencional | Suspendida | 1967-02-15 00:00:00 | 2020-10-20 12:18:23 | Valle del Cauca | La Unión (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Rios Pescador - RUT - Chanco - Catarina y Cañaveral | America/Bogota | 2022-01-10 23:00:00 | 90.000000 | 18.760000 | 20.410000 | 93.000000 | 1012.000000 | 1.59 | 19.930000 | 0.000000 | 10000.000000 | 272.000000 | 1.86 | 1.660000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26115040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26115040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26115040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115040_OWM_Windspeed_20220111.png)
