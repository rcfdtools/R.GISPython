
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA LAGUNA DE CAJIBIO [26035090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26035090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.699175,-76.59544444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.699175&lon=-76.59544444)


| Parameter | Value |
|---|---|
| Code | 26035090 |
| Name | LA LAGUNA DE CAJIBIO [26035090] |
| Latitude, ° | 2.699175 |
| Longitude, ° | -76.59544444 |
| Elevation, m | 1872 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2004-10-04 00:00:00 |
| Suspension date | 2016-01-06 00:00:00 |
| State | Cauca |
| County | Cajibío |
| Stream | Magdalena |
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

### (CNE index 33) Open Weather values for station 26035090 - LA LAGUNA DE CAJIBIO [26035090]

JSON data from API OWM:

```
{'lat': 2.6992, 'lon': -76.5954, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813269, 'sunset': 1641856377, 'temp': 18.42, 'feels_like': 18.69, 'pressure': 1013, 'humidity': 91, 'dew_point': 16.92, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 281, 'wind_gust': 1.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.64}}, 'hourly': [{'dt': 1641772800, 'temp': 15.2, 'feels_like': 15.33, 'pressure': 1015, 'humidity': 98, 'dew_point': 14.89, 'uvi': 0, 'clouds': 75, 'visibility': 6448, 'wind_speed': 0.59, 'wind_deg': 177, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.67}}, {'dt': 1641776400, 'temp': 14.92, 'feels_like': 15.03, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.61, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 170, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1641780000, 'temp': 14.78, 'feels_like': 14.85, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.31, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 160, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641783600, 'temp': 14.87, 'feels_like': 14.95, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.4, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 173, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.02, 'feels_like': 15.11, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.55, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 181, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641790800, 'temp': 15.07, 'feels_like': 15.17, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.6, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 164, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.18, 'feels_like': 15.29, 'pressure': 1016, 'humidity': 97, 'dew_point': 14.71, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 213, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 15.08, 'feels_like': 15.2, 'pressure': 1015, 'humidity': 98, 'dew_point': 14.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 224, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641801600, 'temp': 15.06, 'feels_like': 15.18, 'pressure': 1015, 'humidity': 98, 'dew_point': 14.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 210, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 15.11, 'feels_like': 15.24, 'pressure': 1015, 'humidity': 98, 'dew_point': 14.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 205, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 15.14, 'feels_like': 15.27, 'pressure': 1015, 'humidity': 98, 'dew_point': 14.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 228, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641812400, 'temp': 15.02, 'feels_like': 15.14, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 239, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641816000, 'temp': 15.34, 'feels_like': 15.49, 'pressure': 1017, 'humidity': 98, 'dew_point': 15.03, 'uvi': 0.37, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 210, 'wind_gust': 0.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641819600, 'temp': 16.56, 'feels_like': 16.73, 'pressure': 1017, 'humidity': 94, 'dew_point': 15.59, 'uvi': 1.44, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 306, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641823200, 'temp': 17.74, 'feels_like': 17.92, 'pressure': 1017, 'humidity': 90, 'dew_point': 16.08, 'uvi': 3.66, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 309, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641826800, 'temp': 18.53, 'feels_like': 18.76, 'pressure': 1017, 'humidity': 89, 'dew_point': 16.68, 'uvi': 6.42, 'clouds': 100, 'visibility': 8885, 'wind_speed': 1.1, 'wind_deg': 291, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.87}}, {'dt': 1641830400, 'temp': 19.49, 'feels_like': 19.74, 'pressure': 1016, 'humidity': 86, 'dew_point': 17.09, 'uvi': 8.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 305, 'wind_gust': 1.16, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641834000, 'temp': 19.79, 'feels_like': 20.07, 'pressure': 1015, 'humidity': 86, 'dew_point': 17.38, 'uvi': 9.44, 'clouds': 100, 'visibility': 6288, 'wind_speed': 1.52, 'wind_deg': 295, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.52}}, {'dt': 1641837600, 'temp': 19.54, 'feels_like': 19.82, 'pressure': 1014, 'humidity': 87, 'dew_point': 17.32, 'uvi': 8.83, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 290, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.77}}, {'dt': 1641841200, 'temp': 19, 'feels_like': 19.28, 'pressure': 1013, 'humidity': 89, 'dew_point': 17.15, 'uvi': 5.41, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 287, 'wind_gust': 1.82, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.67}}, {'dt': 1641844800, 'temp': 18.42, 'feels_like': 18.69, 'pressure': 1013, 'humidity': 91, 'dew_point': 16.92, 'uvi': 3.32, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 281, 'wind_gust': 1.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.64}}, {'dt': 1641848400, 'temp': 17.99, 'feels_like': 18.25, 'pressure': 1012, 'humidity': 92, 'dew_point': 16.67, 'uvi': 1.47, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 263, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.77}}, {'dt': 1641852000, 'temp': 17.49, 'feels_like': 17.75, 'pressure': 1013, 'humidity': 94, 'dew_point': 16.51, 'uvi': 0.33, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 247, 'wind_gust': 1.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.59}}, {'dt': 1641855600, 'temp': 16.06, 'feels_like': 16.25, 'pressure': 1014, 'humidity': 97, 'dew_point': 15.58, 'uvi': 0, 'clouds': 87, 'visibility': 4716, 'wind_speed': 0.86, 'wind_deg': 249, 'wind_gust': 1.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.21}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 00:00:00 | 75.000000 | 14.890000 | 15.330000 | 98.000000 | 1015.000000 | 0.67 | 15.200000 | 0.000000 | 6448.000000 | 177.000000 | 1.47 | 0.590000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 01:00:00 | 77.000000 | 14.610000 | 15.030000 | 98.000000 | 1016.000000 | 0.47 | 14.920000 | 0.000000 | 10000.000000 | 170.000000 | 1.38 | 0.750000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 02:00:00 | 88.000000 | 14.310000 | 14.850000 | 97.000000 | 1017.000000 | 0.34 | 14.780000 | 0.000000 | 10000.000000 | 160.000000 | 0.97 | 0.660000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 03:00:00 | 92.000000 | 14.400000 | 14.950000 | 97.000000 | 1017.000000 |  | 14.870000 | 0.000000 | 10000.000000 | 173.000000 | 0.88 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 14.550000 | 15.110000 | 97.000000 | 1017.000000 | 0.16 | 15.020000 | 0.000000 | 10000.000000 | 181.000000 | 0.84 | 0.810000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 14.600000 | 15.170000 | 97.000000 | 1017.000000 |  | 15.070000 | 0.000000 | 10000.000000 | 164.000000 | 0.75 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 14.710000 | 15.290000 | 97.000000 | 1016.000000 |  | 15.180000 | 0.000000 | 10000.000000 | 213.000000 | 0.8 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 14.770000 | 15.200000 | 98.000000 | 1015.000000 | 0.16 | 15.080000 | 0.000000 | 10000.000000 | 224.000000 | 0.91 | 0.740000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 14.750000 | 15.180000 | 98.000000 | 1015.000000 | 0.13 | 15.060000 | 0.000000 | 10000.000000 | 210.000000 | 1.22 | 0.730000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 14.800000 | 15.240000 | 98.000000 | 1015.000000 | 0.23 | 15.110000 | 0.000000 | 10000.000000 | 205.000000 | 0.92 | 0.590000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 14.830000 | 15.270000 | 98.000000 | 1015.000000 | 0.19 | 15.140000 | 0.000000 | 10000.000000 | 228.000000 | 0.61 | 0.520000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 14.710000 | 15.140000 | 98.000000 | 1016.000000 | 0.17 | 15.020000 | 0.000000 | 10000.000000 | 239.000000 | 0.63 | 0.450000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 15.030000 | 15.490000 | 98.000000 | 1017.000000 | 0.16 | 15.340000 | 0.370000 | 10000.000000 | 210.000000 | 0.78 | 0.370000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 15.590000 | 16.730000 | 94.000000 | 1017.000000 | 0.17 | 16.560000 | 1.440000 | 10000.000000 | 306.000000 | 0.45 | 0.380000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 16.080000 | 17.920000 | 90.000000 | 1017.000000 | 0.51 | 17.740000 | 3.660000 | 10000.000000 | 309.000000 | 0.9 | 0.870000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 16.680000 | 18.760000 | 89.000000 | 1017.000000 | 0.87 | 18.530000 | 6.420000 | 8885.000000 | 291.000000 | 1.12 | 1.100000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 17.090000 | 19.740000 | 86.000000 | 1016.000000 | 1.13 | 19.490000 | 8.420000 | 10000.000000 | 305.000000 | 1.16 | 1.240000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 17.380000 | 20.070000 | 86.000000 | 1015.000000 | 1.52 | 19.790000 | 9.440000 | 6288.000000 | 295.000000 | 1.54 | 1.520000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 17.320000 | 19.820000 | 87.000000 | 1014.000000 | 1.77 | 19.540000 | 8.830000 | 10000.000000 | 290.000000 | 1.6 | 1.540000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 19:00:00 | 96.000000 | 17.150000 | 19.280000 | 89.000000 | 1013.000000 | 1.67 | 19.000000 | 5.410000 | 10000.000000 | 287.000000 | 1.82 | 1.640000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 20:00:00 | 94.000000 | 16.920000 | 18.690000 | 91.000000 | 1013.000000 | 1.64 | 18.420000 | 3.320000 | 10000.000000 | 281.000000 | 1.72 | 1.420000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 21:00:00 | 96.000000 | 16.670000 | 18.250000 | 92.000000 | 1012.000000 | 1.77 | 17.990000 | 1.470000 | 10000.000000 | 263.000000 | 1.75 | 1.340000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 16.510000 | 17.750000 | 94.000000 | 1013.000000 | 1.59 | 17.490000 | 0.330000 | 10000.000000 | 247.000000 | 1.7 | 1.070000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035090 | "LA LAGUNA DE CAJIBIO [26035090]" | 2.699175 | -76.595444 | 1872.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2004-10-04 00:00:00 | 2016-01-06 00:00:00 | Cauca | Cajibío | Magdalena | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Piendamo | America/Bogota | 2022-01-10 23:00:00 | 87.000000 | 15.580000 | 16.250000 | 97.000000 | 1014.000000 | 1.21 | 16.060000 | 0.000000 | 4716.000000 | 249.000000 | 1.32 | 0.860000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26035090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26035090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26035090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035090_OWM_Windspeed_20220111.png)
