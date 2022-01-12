
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL TABLAZO - AUT [26015010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26015010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.47483306,-76.58129361) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.47483306&lon=-76.58129361)


| Parameter | Value |
|---|---|
| Code | 26015010 |
| Name | EL TABLAZO - AUT [26015010] |
| Latitude, ° | 2.47483306 |
| Longitude, ° | -76.58129361 |
| Elevation, m | 1837 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-28 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Popayán |
| Stream | Vaupes |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Alto Río Cauca |

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

### (CNE index 23) Open Weather values for station 26015010 - EL TABLAZO - AUT [26015010]

JSON data from API OWM:

```
{'lat': 2.4748, 'lon': -76.5813, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813244, 'sunset': 1641856395, 'temp': 18.14, 'feels_like': 18.44, 'pressure': 1013, 'humidity': 93, 'dew_point': 16.99, 'uvi': 2.35, 'clouds': 99, 'visibility': 5031, 'wind_speed': 1.52, 'wind_deg': 272, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.45}}, 'hourly': [{'dt': 1641772800, 'temp': 15.4, 'feels_like': 15.55, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.09, 'uvi': 0, 'clouds': 95, 'visibility': 7441, 'wind_speed': 0.27, 'wind_deg': 170, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.69}}, {'dt': 1641776400, 'temp': 15.11, 'feels_like': 15.24, 'pressure': 1017, 'humidity': 98, 'dew_point': 14.8, 'uvi': 0, 'clouds': 96, 'visibility': 8387, 'wind_speed': 0.31, 'wind_deg': 151, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641780000, 'temp': 15.07, 'feels_like': 15.19, 'pressure': 1018, 'humidity': 98, 'dew_point': 14.76, 'uvi': 0, 'clouds': 95, 'visibility': 8811, 'wind_speed': 0.33, 'wind_deg': 109, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641783600, 'temp': 15.15, 'feels_like': 15.28, 'pressure': 1018, 'humidity': 98, 'dew_point': 14.84, 'uvi': 0, 'clouds': 94, 'visibility': 8494, 'wind_speed': 0.35, 'wind_deg': 129, 'wind_gust': 0.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.21, 'feels_like': 15.35, 'pressure': 1018, 'humidity': 98, 'dew_point': 14.9, 'uvi': 0, 'clouds': 95, 'visibility': 8932, 'wind_speed': 0.4, 'wind_deg': 174, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641790800, 'temp': 15.31, 'feels_like': 15.46, 'pressure': 1017, 'humidity': 98, 'dew_point': 15, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 138, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.34, 'feels_like': 15.49, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.03, 'uvi': 0, 'clouds': 90, 'visibility': 8426, 'wind_speed': 0.22, 'wind_deg': 241, 'wind_gust': 0.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 15.18, 'feels_like': 15.31, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.87, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 255, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641801600, 'temp': 15.08, 'feels_like': 15.23, 'pressure': 1015, 'humidity': 99, 'dew_point': 14.92, 'uvi': 0, 'clouds': 100, 'visibility': 8588, 'wind_speed': 0.36, 'wind_deg': 234, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641805200, 'temp': 15.15, 'feels_like': 15.31, 'pressure': 1015, 'humidity': 99, 'dew_point': 14.99, 'uvi': 0, 'clouds': 100, 'visibility': 8249, 'wind_speed': 0.28, 'wind_deg': 258, 'wind_gust': 0.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 15.1, 'feels_like': 15.25, 'pressure': 1016, 'humidity': 99, 'dew_point': 14.94, 'uvi': 0, 'clouds': 100, 'visibility': 7569, 'wind_speed': 0.37, 'wind_deg': 301, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641812400, 'temp': 15.05, 'feels_like': 15.2, 'pressure': 1017, 'humidity': 99, 'dew_point': 14.89, 'uvi': 0, 'clouds': 100, 'visibility': 6801, 'wind_speed': 0.45, 'wind_deg': 282, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641816000, 'temp': 15.58, 'feels_like': 15.78, 'pressure': 1017, 'humidity': 99, 'dew_point': 15.42, 'uvi': 0.28, 'clouds': 100, 'visibility': 7415, 'wind_speed': 0.23, 'wind_deg': 313, 'wind_gust': 0.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641819600, 'temp': 16.44, 'feels_like': 16.65, 'pressure': 1018, 'humidity': 96, 'dew_point': 15.8, 'uvi': 1.24, 'clouds': 100, 'visibility': 7515, 'wind_speed': 0.48, 'wind_deg': 299, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641823200, 'temp': 17.48, 'feels_like': 17.69, 'pressure': 1018, 'humidity': 92, 'dew_point': 16.17, 'uvi': 3.16, 'clouds': 100, 'visibility': 8235, 'wind_speed': 0.77, 'wind_deg': 288, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641826800, 'temp': 18.23, 'feels_like': 18.46, 'pressure': 1018, 'humidity': 90, 'dew_point': 16.56, 'uvi': 5.53, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 282, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641830400, 'temp': 19.38, 'feels_like': 19.67, 'pressure': 1017, 'humidity': 88, 'dew_point': 17.34, 'uvi': 9.04, 'clouds': 100, 'visibility': 6904, 'wind_speed': 1.4, 'wind_deg': 289, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.12}}, {'dt': 1641834000, 'temp': 19.53, 'feels_like': 19.86, 'pressure': 1016, 'humidity': 89, 'dew_point': 17.67, 'uvi': 10.14, 'clouds': 100, 'visibility': 6896, 'wind_speed': 1.78, 'wind_deg': 278, 'wind_gust': 1.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.47}}, {'dt': 1641837600, 'temp': 19.18, 'feels_like': 19.5, 'pressure': 1015, 'humidity': 90, 'dew_point': 17.5, 'uvi': 9.48, 'clouds': 92, 'visibility': 6151, 'wind_speed': 1.72, 'wind_deg': 271, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.56}}, {'dt': 1641841200, 'temp': 18.58, 'feels_like': 18.9, 'pressure': 1014, 'humidity': 92, 'dew_point': 17.26, 'uvi': 3.83, 'clouds': 99, 'visibility': 6651, 'wind_speed': 1.63, 'wind_deg': 272, 'wind_gust': 1.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.6}}, {'dt': 1641844800, 'temp': 18.14, 'feels_like': 18.44, 'pressure': 1013, 'humidity': 93, 'dew_point': 16.99, 'uvi': 2.35, 'clouds': 99, 'visibility': 5031, 'wind_speed': 1.52, 'wind_deg': 272, 'wind_gust': 1.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.45}}, {'dt': 1641848400, 'temp': 17.7, 'feels_like': 18.01, 'pressure': 1013, 'humidity': 95, 'dew_point': 16.89, 'uvi': 1.05, 'clouds': 99, 'visibility': 6630, 'wind_speed': 1.39, 'wind_deg': 256, 'wind_gust': 1.89, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.53}}, {'dt': 1641852000, 'temp': 17.16, 'feels_like': 17.44, 'pressure': 1014, 'humidity': 96, 'dew_point': 16.52, 'uvi': 0.24, 'clouds': 96, 'visibility': 7089, 'wind_speed': 1.11, 'wind_deg': 251, 'wind_gust': 1.93, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641855600, 'temp': 16.04, 'feels_like': 16.28, 'pressure': 1015, 'humidity': 99, 'dew_point': 15.88, 'uvi': 0, 'clouds': 91, 'visibility': 6360, 'wind_speed': 0.87, 'wind_deg': 246, 'wind_gust': 1.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 00:00:00 | 95.000000 | 15.090000 | 15.550000 | 98.000000 | 1016.000000 | 0.69 | 15.400000 | 0.000000 | 7441.000000 | 170.000000 | 0.98 | 0.270000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 14.800000 | 15.240000 | 98.000000 | 1017.000000 | 0.5 | 15.110000 | 0.000000 | 8387.000000 | 151.000000 | 0.66 | 0.310000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 02:00:00 | 95.000000 | 14.760000 | 15.190000 | 98.000000 | 1018.000000 | 0.11 | 15.070000 | 0.000000 | 8811.000000 | 109.000000 | 0.58 | 0.330000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 14.840000 | 15.280000 | 98.000000 | 1018.000000 |  | 15.150000 | 0.000000 | 8494.000000 | 129.000000 | 0.55 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 14.900000 | 15.350000 | 98.000000 | 1018.000000 | 0.15 | 15.210000 | 0.000000 | 8932.000000 | 174.000000 | 0.56 | 0.400000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 05:00:00 | 96.000000 | 15.000000 | 15.460000 | 98.000000 | 1017.000000 |  | 15.310000 | 0.000000 | 10000.000000 | 138.000000 | 0.51 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 06:00:00 | 90.000000 | 15.030000 | 15.490000 | 98.000000 | 1016.000000 |  | 15.340000 | 0.000000 | 8426.000000 | 241.000000 | 0.49 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 14.870000 | 15.310000 | 98.000000 | 1016.000000 | 0.17 | 15.180000 | 0.000000 | 10000.000000 | 255.000000 | 0.65 | 0.400000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 14.920000 | 15.230000 | 99.000000 | 1015.000000 | 0.24 | 15.080000 | 0.000000 | 8588.000000 | 234.000000 | 0.65 | 0.360000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 14.990000 | 15.310000 | 99.000000 | 1015.000000 | 0.18 | 15.150000 | 0.000000 | 8249.000000 | 258.000000 | 0.52 | 0.280000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 14.940000 | 15.250000 | 99.000000 | 1016.000000 | 0.26 | 15.100000 | 0.000000 | 7569.000000 | 301.000000 | 0.59 | 0.370000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 14.890000 | 15.200000 | 99.000000 | 1017.000000 | 0.16 | 15.050000 | 0.000000 | 6801.000000 | 282.000000 | 0.81 | 0.450000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 15.420000 | 15.780000 | 99.000000 | 1017.000000 | 0.24 | 15.580000 | 0.280000 | 7415.000000 | 313.000000 | 0.5 | 0.230000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 15.800000 | 16.650000 | 96.000000 | 1018.000000 | 0.19 | 16.440000 | 1.240000 | 7515.000000 | 299.000000 | 0.53 | 0.480000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 16.170000 | 17.690000 | 92.000000 | 1018.000000 | 0.41 | 17.480000 | 3.160000 | 8235.000000 | 288.000000 | 0.85 | 0.770000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 16.560000 | 18.460000 | 90.000000 | 1018.000000 | 0.77 | 18.230000 | 5.530000 | 10000.000000 | 282.000000 | 1.44 | 1.340000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 17.340000 | 19.670000 | 88.000000 | 1017.000000 | 1.12 | 19.380000 | 9.040000 | 6904.000000 | 289.000000 | 1.3 | 1.400000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 17.670000 | 19.860000 | 89.000000 | 1016.000000 | 1.47 | 19.530000 | 10.140000 | 6896.000000 | 278.000000 | 1.7 | 1.780000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 18:00:00 | 92.000000 | 17.500000 | 19.500000 | 90.000000 | 1015.000000 | 1.56 | 19.180000 | 9.480000 | 6151.000000 | 271.000000 | 1.66 | 1.720000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 17.260000 | 18.900000 | 92.000000 | 1014.000000 | 1.6 | 18.580000 | 3.830000 | 6651.000000 | 272.000000 | 1.88 | 1.630000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 16.990000 | 18.440000 | 93.000000 | 1013.000000 | 1.45 | 18.140000 | 2.350000 | 5031.000000 | 272.000000 | 1.86 | 1.520000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 16.890000 | 18.010000 | 95.000000 | 1013.000000 | 1.53 | 17.700000 | 1.050000 | 6630.000000 | 256.000000 | 1.89 | 1.390000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 16.520000 | 17.440000 | 96.000000 | 1014.000000 | 1.14 | 17.160000 | 0.240000 | 7089.000000 | 251.000000 | 1.93 | 1.110000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015010 | "EL TABLAZO - AUT [26015010]" | 2.474833 | -76.581294 | 1837.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Cauca | Popayán | Vaupes | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 15.880000 | 16.280000 | 99.000000 | 1015.000000 | 0.86 | 16.040000 | 0.000000 | 6360.000000 | 246.000000 | 1.41 | 0.870000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26015010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26015010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26015010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015010_OWM_Windspeed_20220111.png)
