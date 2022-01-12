
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA SALVAJINA [26035040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26035040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.95,-76.7) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.95&lon=-76.7)


| Parameter | Value |
|---|---|
| Code | 26035040 |
| Name | LA SALVAJINA [26035040] |
| Latitude, ° | 2.95 |
| Longitude, ° | -76.7 |
| Elevation, m | 1130 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2008-03-31 00:00:00 |
| Suspension date | 2018-06-19 10:39:44 |
| State | Cauca |
| County | Suárez (Cauca) |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Piendamo |

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

### (CNE index 3779) Open Weather values for station 26035040 - LA SALVAJINA [26035040]

JSON data from API OWM:

```
{'lat': 2.95, 'lon': -76.7, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813318, 'sunset': 1641856377, 'temp': 22.63, 'feels_like': 23.19, 'pressure': 1012, 'humidity': 86, 'dew_point': 20.17, 'uvi': 3.32, 'clouds': 92, 'visibility': 8523, 'wind_speed': 1.77, 'wind_deg': 282, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, 'hourly': [{'dt': 1641772800, 'temp': 19.33, 'feels_like': 19.85, 'pressure': 1014, 'humidity': 97, 'dew_point': 18.84, 'uvi': 0, 'clouds': 58, 'visibility': 5855, 'wind_speed': 1.48, 'wind_deg': 265, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.51}}, {'dt': 1641776400, 'temp': 19.14, 'feels_like': 19.64, 'pressure': 1015, 'humidity': 97, 'dew_point': 18.65, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 257, 'wind_gust': 2.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641780000, 'temp': 19.06, 'feels_like': 19.55, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.57, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 248, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641783600, 'temp': 18.74, 'feels_like': 19.2, 'pressure': 1017, 'humidity': 97, 'dew_point': 18.25, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 242, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.58, 'feels_like': 19, 'pressure': 1016, 'humidity': 96, 'dew_point': 17.93, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 233, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 18.44, 'feels_like': 18.85, 'pressure': 1016, 'humidity': 96, 'dew_point': 17.79, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 240, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.5, 'feels_like': 18.91, 'pressure': 1015, 'humidity': 96, 'dew_point': 17.85, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 252, 'wind_gust': 1.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 18.6, 'feels_like': 19.05, 'pressure': 1015, 'humidity': 97, 'dew_point': 18.11, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 251, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 18.42, 'feels_like': 18.85, 'pressure': 1014, 'humidity': 97, 'dew_point': 17.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 258, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 18.55, 'feels_like': 18.99, 'pressure': 1014, 'humidity': 97, 'dew_point': 18.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 258, 'wind_gust': 1.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 18.78, 'feels_like': 19.22, 'pressure': 1015, 'humidity': 96, 'dew_point': 18.13, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 255, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 18.8, 'feels_like': 19.24, 'pressure': 1015, 'humidity': 96, 'dew_point': 18.15, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 270, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 19.2, 'feels_like': 19.66, 'pressure': 1016, 'humidity': 95, 'dew_point': 18.38, 'uvi': 0.37, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 258, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 20.09, 'feels_like': 20.58, 'pressure': 1017, 'humidity': 93, 'dew_point': 18.92, 'uvi': 1.44, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 301, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641823200, 'temp': 21.51, 'feels_like': 22.01, 'pressure': 1017, 'humidity': 88, 'dew_point': 19.44, 'uvi': 3.66, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 313, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1641826800, 'temp': 22.8, 'feels_like': 23.33, 'pressure': 1017, 'humidity': 84, 'dew_point': 19.96, 'uvi': 6.42, 'clouds': 100, 'visibility': 8235, 'wind_speed': 0.81, 'wind_deg': 290, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641830400, 'temp': 23.52, 'feels_like': 24.07, 'pressure': 1016, 'humidity': 82, 'dew_point': 20.27, 'uvi': 8.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 310, 'wind_gust': 1.37, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641834000, 'temp': 23.61, 'feels_like': 24.19, 'pressure': 1015, 'humidity': 83, 'dew_point': 20.55, 'uvi': 9.44, 'clouds': 100, 'visibility': 8977, 'wind_speed': 1.54, 'wind_deg': 293, 'wind_gust': 1.99, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.27}}, {'dt': 1641837600, 'temp': 23.24, 'feels_like': 23.81, 'pressure': 1014, 'humidity': 84, 'dew_point': 20.39, 'uvi': 8.83, 'clouds': 64, 'visibility': 8590, 'wind_speed': 1.7, 'wind_deg': 288, 'wind_gust': 2.15, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, {'dt': 1641841200, 'temp': 22.8, 'feels_like': 23.38, 'pressure': 1013, 'humidity': 86, 'dew_point': 20.34, 'uvi': 5.41, 'clouds': 87, 'visibility': 5750, 'wind_speed': 1.8, 'wind_deg': 285, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.97}}, {'dt': 1641844800, 'temp': 22.63, 'feels_like': 23.19, 'pressure': 1012, 'humidity': 86, 'dew_point': 20.17, 'uvi': 3.32, 'clouds': 92, 'visibility': 8523, 'wind_speed': 1.77, 'wind_deg': 282, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641848400, 'temp': 22.31, 'feels_like': 22.87, 'pressure': 1012, 'humidity': 87, 'dew_point': 20.04, 'uvi': 1.47, 'clouds': 94, 'visibility': 7946, 'wind_speed': 1.76, 'wind_deg': 277, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641852000, 'temp': 21.72, 'feels_like': 22.3, 'pressure': 1012, 'humidity': 90, 'dew_point': 20.01, 'uvi': 0.33, 'clouds': 96, 'visibility': 7992, 'wind_speed': 1.41, 'wind_deg': 277, 'wind_gust': 1.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.87}}, {'dt': 1641855600, 'temp': 20.17, 'feels_like': 20.72, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.34, 'uvi': 0, 'clouds': 94, 'visibility': 2503, 'wind_speed': 1.34, 'wind_deg': 282, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 00:00:00 | 58.000000 | 18.840000 | 19.850000 | 97.000000 | 1014.000000 | 0.51 | 19.330000 | 0.000000 | 5855.000000 | 265.000000 | 2.19 | 1.480000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 01:00:00 | 88.000000 | 18.650000 | 19.640000 | 97.000000 | 1015.000000 | 0.26 | 19.140000 | 0.000000 | 10000.000000 | 257.000000 | 2.09 | 1.430000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 02:00:00 | 94.000000 | 18.570000 | 19.550000 | 97.000000 | 1016.000000 | 0.2 | 19.060000 | 0.000000 | 10000.000000 | 248.000000 | 1.62 | 1.210000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 03:00:00 | 95.000000 | 18.250000 | 19.200000 | 97.000000 | 1017.000000 |  | 18.740000 | 0.000000 | 10000.000000 | 242.000000 | 1.32 | 1.310000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 17.930000 | 19.000000 | 96.000000 | 1016.000000 |  | 18.580000 | 0.000000 | 10000.000000 | 233.000000 | 1.23 | 1.220000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 17.790000 | 18.850000 | 96.000000 | 1016.000000 |  | 18.440000 | 0.000000 | 10000.000000 | 240.000000 | 1.06 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 06:00:00 | 97.000000 | 17.850000 | 18.910000 | 96.000000 | 1015.000000 |  | 18.500000 | 0.000000 | 10000.000000 | 252.000000 | 1.5 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 18.110000 | 19.050000 | 97.000000 | 1015.000000 |  | 18.600000 | 0.000000 | 10000.000000 | 251.000000 | 1.67 | 1.270000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 17.940000 | 18.850000 | 97.000000 | 1014.000000 |  | 18.420000 | 0.000000 | 10000.000000 | 258.000000 | 1.58 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 18.060000 | 18.990000 | 97.000000 | 1014.000000 |  | 18.550000 | 0.000000 | 10000.000000 | 258.000000 | 1.27 | 1.000000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 18.130000 | 19.220000 | 96.000000 | 1015.000000 |  | 18.780000 | 0.000000 | 10000.000000 | 255.000000 | 0.82 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 18.150000 | 19.240000 | 96.000000 | 1015.000000 |  | 18.800000 | 0.000000 | 10000.000000 | 270.000000 | 0.74 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 12:00:00 | 98.000000 | 18.380000 | 19.660000 | 95.000000 | 1016.000000 |  | 19.200000 | 0.370000 | 10000.000000 | 258.000000 | 0.88 | 0.570000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 18.920000 | 20.580000 | 93.000000 | 1017.000000 | 0.14 | 20.090000 | 1.440000 | 10000.000000 | 301.000000 | 1 | 0.540000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 19.440000 | 22.010000 | 88.000000 | 1017.000000 | 0.42 | 21.510000 | 3.660000 | 10000.000000 | 313.000000 | 1.1 | 0.650000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 19.960000 | 23.330000 | 84.000000 | 1017.000000 | 0.86 | 22.800000 | 6.420000 | 8235.000000 | 290.000000 | 1.22 | 0.810000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 20.270000 | 24.070000 | 82.000000 | 1016.000000 | 1.25 | 23.520000 | 8.420000 | 10000.000000 | 310.000000 | 1.37 | 1.150000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 20.550000 | 24.190000 | 83.000000 | 1015.000000 | 1.27 | 23.610000 | 9.440000 | 8977.000000 | 293.000000 | 1.99 | 1.540000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 18:00:00 | 64.000000 | 20.390000 | 23.810000 | 84.000000 | 1014.000000 | 1.22 | 23.240000 | 8.830000 | 8590.000000 | 288.000000 | 2.15 | 1.700000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 20.340000 | 23.380000 | 86.000000 | 1013.000000 | 0.97 | 22.800000 | 5.410000 | 5750.000000 | 285.000000 | 2.26 | 1.800000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 20:00:00 | 92.000000 | 20.170000 | 23.190000 | 86.000000 | 1012.000000 | 0.85 | 22.630000 | 3.320000 | 8523.000000 | 282.000000 | 2.34 | 1.770000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 20.040000 | 22.870000 | 87.000000 | 1012.000000 | 0.91 | 22.310000 | 1.470000 | 7946.000000 | 277.000000 | 2.38 | 1.760000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 20.010000 | 22.300000 | 90.000000 | 1012.000000 | 0.87 | 21.720000 | 0.330000 | 7992.000000 | 277.000000 | 1.99 | 1.410000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035040 | "LA SALVAJINA [26035040]" | 2.950000 | -76.700000 | 1130.000000 | Climática Principal | Convencional | Suspendida | 2008-03-31 00:00:00 | 2018-06-19 10:39:44 | Cauca | Suárez (Cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 19.340000 | 20.720000 | 95.000000 | 1013.000000 | 0.73 | 20.170000 | 0.000000 | 2503.000000 | 282.000000 | 1.79 | 1.340000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26035040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26035040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26035040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035040_OWM_Windspeed_20220111.png)
