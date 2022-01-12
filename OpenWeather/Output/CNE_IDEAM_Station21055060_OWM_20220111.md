
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ALPES LOS - AUT [21055060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21055060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.97113889,-76.11577778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.97113889&lon=-76.11577778)


| Parameter | Value |
|---|---|
| Code | 21055060 |
| Name | ALPES LOS - AUT [21055060] |
| Latitude, ° | 2.97113889 |
| Longitude, ° | -76.11577778 |
| Elevation, m | 4530 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2007-11-20 00:00:00 |
| Suspension date | 2010-09-29 00:00:00 |
| State | Cauca |
| County | Páez (Belalcázar) |
| Stream | Quebrada Don Abad |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Palo |

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

### (CNE index 2023) Open Weather values for station 21055060 - ALPES LOS - AUT [21055060]

JSON data from API OWM:

```
{'lat': 2.9711, 'lon': -76.1158, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813180, 'sunset': 1641856235, 'temp': 6.8, 'feels_like': 6.8, 'pressure': 1015, 'humidity': 91, 'dew_point': 5.44, 'uvi': 5.87, 'clouds': 97, 'visibility': 6066, 'wind_speed': 1.23, 'wind_deg': 293, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.21}}, 'hourly': [{'dt': 1641772800, 'temp': 4.78, 'feels_like': 4.78, 'pressure': 1017, 'humidity': 94, 'dew_point': 3.9, 'uvi': 0, 'clouds': 89, 'visibility': 7434, 'wind_speed': 0.11, 'wind_deg': 205, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.38}}, {'dt': 1641776400, 'temp': 4.7, 'feels_like': 4.7, 'pressure': 1018, 'humidity': 93, 'dew_point': 3.67, 'uvi': 0, 'clouds': 98, 'visibility': 6830, 'wind_speed': 0.09, 'wind_deg': 154, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641780000, 'temp': 4.55, 'feels_like': 4.55, 'pressure': 1019, 'humidity': 93, 'dew_point': 3.52, 'uvi': 0, 'clouds': 99, 'visibility': 5939, 'wind_speed': 0.02, 'wind_deg': 259, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641783600, 'temp': 4.4, 'feels_like': 4.4, 'pressure': 1019, 'humidity': 96, 'dew_point': 3.82, 'uvi': 0, 'clouds': 99, 'visibility': 5722, 'wind_speed': 0.18, 'wind_deg': 292, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641787200, 'temp': 3.81, 'feels_like': 3.81, 'pressure': 1019, 'humidity': 98, 'dew_point': 3.52, 'uvi': 0, 'clouds': 100, 'visibility': 5738, 'wind_speed': 0.28, 'wind_deg': 266, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641790800, 'temp': 3.66, 'feels_like': 3.66, 'pressure': 1019, 'humidity': 98, 'dew_point': 3.37, 'uvi': 0, 'clouds': 100, 'visibility': 5845, 'wind_speed': 0.15, 'wind_deg': 265, 'wind_gust': 0.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641794400, 'temp': 3.46, 'feels_like': 3.46, 'pressure': 1018, 'humidity': 99, 'dew_point': 3.32, 'uvi': 0, 'clouds': 96, 'visibility': 7289, 'wind_speed': 0.55, 'wind_deg': 272, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641798000, 'temp': 3.32, 'feels_like': 3.32, 'pressure': 1017, 'humidity': 99, 'dew_point': 3.18, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 275, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641801600, 'temp': 3.18, 'feels_like': 3.18, 'pressure': 1017, 'humidity': 99, 'dew_point': 3.04, 'uvi': 0, 'clouds': 100, 'visibility': 6609, 'wind_speed': 0.73, 'wind_deg': 279, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641805200, 'temp': 3.43, 'feels_like': 3.43, 'pressure': 1017, 'humidity': 97, 'dew_point': 3, 'uvi': 0, 'clouds': 100, 'visibility': 6463, 'wind_speed': 1.18, 'wind_deg': 282, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 3.58, 'feels_like': 3.58, 'pressure': 1017, 'humidity': 98, 'dew_point': 3.29, 'uvi': 0, 'clouds': 100, 'visibility': 6411, 'wind_speed': 0.89, 'wind_deg': 292, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641812400, 'temp': 3.65, 'feels_like': 3.65, 'pressure': 1018, 'humidity': 98, 'dew_point': 3.36, 'uvi': 0, 'clouds': 100, 'visibility': 6928, 'wind_speed': 0.87, 'wind_deg': 301, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641816000, 'temp': 4.02, 'feels_like': 4.02, 'pressure': 1018, 'humidity': 97, 'dew_point': 3.59, 'uvi': 0.37, 'clouds': 96, 'visibility': 6485, 'wind_speed': 0.78, 'wind_deg': 296, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641819600, 'temp': 4.51, 'feels_like': 4.51, 'pressure': 1019, 'humidity': 96, 'dew_point': 3.93, 'uvi': 1.49, 'clouds': 100, 'visibility': 6745, 'wind_speed': 0.47, 'wind_deg': 320, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641823200, 'temp': 5.13, 'feels_like': 5.13, 'pressure': 1020, 'humidity': 94, 'dew_point': 4.25, 'uvi': 3.77, 'clouds': 100, 'visibility': 6210, 'wind_speed': 0.42, 'wind_deg': 341, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641826800, 'temp': 6.43, 'feels_like': 6.43, 'pressure': 1019, 'humidity': 87, 'dew_point': 4.43, 'uvi': 6.55, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 310, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641830400, 'temp': 7.39, 'feels_like': 7.39, 'pressure': 1018, 'humidity': 85, 'dew_point': 5.04, 'uvi': 11.58, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 301, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.51}}, {'dt': 1641834000, 'temp': 7.64, 'feels_like': 7.64, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.45, 'uvi': 12.92, 'clouds': 99, 'visibility': 7358, 'wind_speed': 0.96, 'wind_deg': 295, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641837600, 'temp': 7.69, 'feels_like': 7.69, 'pressure': 1016, 'humidity': 88, 'dew_point': 5.83, 'uvi': 12.01, 'clouds': 81, 'visibility': 8708, 'wind_speed': 1.12, 'wind_deg': 291, 'wind_gust': 1.11, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.05}}, {'dt': 1641841200, 'temp': 7.4, 'feels_like': 7.4, 'pressure': 1015, 'humidity': 89, 'dew_point': 5.71, 'uvi': 9.66, 'clouds': 95, 'visibility': 5380, 'wind_speed': 1.14, 'wind_deg': 292, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641844800, 'temp': 6.8, 'feels_like': 6.8, 'pressure': 1015, 'humidity': 91, 'dew_point': 5.44, 'uvi': 5.87, 'clouds': 97, 'visibility': 6066, 'wind_speed': 1.23, 'wind_deg': 293, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.21}}, {'dt': 1641848400, 'temp': 6.22, 'feels_like': 6.22, 'pressure': 1014, 'humidity': 93, 'dew_point': 5.17, 'uvi': 2.57, 'clouds': 97, 'visibility': 6783, 'wind_speed': 0.99, 'wind_deg': 294, 'wind_gust': 1.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641852000, 'temp': 5.63, 'feels_like': 5.63, 'pressure': 1015, 'humidity': 95, 'dew_point': 4.89, 'uvi': 0.63, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 296, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641855600, 'temp': 4.37, 'feels_like': 4.37, 'pressure': 1016, 'humidity': 97, 'dew_point': 3.94, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 307, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.9}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 00:00:00 | 89.000000 | 3.900000 | 4.780000 | 94.000000 | 1017.000000 | 0.38 | 4.780000 | 0.000000 | 7434.000000 | 205.000000 | 0.84 | 0.110000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 01:00:00 | 98.000000 | 3.670000 | 4.700000 | 93.000000 | 1018.000000 | 0.31 | 4.700000 | 0.000000 | 6830.000000 | 154.000000 | 0.75 | 0.090000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 3.520000 | 4.550000 | 93.000000 | 1019.000000 | 0.3 | 4.550000 | 0.000000 | 5939.000000 | 259.000000 | 0.72 | 0.020000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 3.820000 | 4.400000 | 96.000000 | 1019.000000 | 0.19 | 4.400000 | 0.000000 | 5722.000000 | 292.000000 | 0.72 | 0.180000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 3.520000 | 3.810000 | 98.000000 | 1019.000000 | 0.26 | 3.810000 | 0.000000 | 5738.000000 | 266.000000 | 0.55 | 0.280000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 3.370000 | 3.660000 | 98.000000 | 1019.000000 | 0.17 | 3.660000 | 0.000000 | 5845.000000 | 265.000000 | 0.36 | 0.150000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 06:00:00 | 96.000000 | 3.320000 | 3.460000 | 99.000000 | 1018.000000 | 0.21 | 3.460000 | 0.000000 | 7289.000000 | 272.000000 | 0.73 | 0.550000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 3.180000 | 3.320000 | 99.000000 | 1017.000000 | 0.25 | 3.320000 | 0.000000 | 10000.000000 | 275.000000 | 0.94 | 0.730000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 3.040000 | 3.180000 | 99.000000 | 1017.000000 | 0.23 | 3.180000 | 0.000000 | 6609.000000 | 279.000000 | 1.18 | 0.730000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 3.000000 | 3.430000 | 97.000000 | 1017.000000 | 0.23 | 3.430000 | 0.000000 | 6463.000000 | 282.000000 | 1.51 | 1.180000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 3.290000 | 3.580000 | 98.000000 | 1017.000000 | 0.5 | 3.580000 | 0.000000 | 6411.000000 | 292.000000 | 1.53 | 0.890000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 3.360000 | 3.650000 | 98.000000 | 1018.000000 | 0.25 | 3.650000 | 0.000000 | 6928.000000 | 301.000000 | 1.38 | 0.870000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 3.590000 | 4.020000 | 97.000000 | 1018.000000 | 0.12 | 4.020000 | 0.370000 | 6485.000000 | 296.000000 | 1.27 | 0.780000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 3.930000 | 4.510000 | 96.000000 | 1019.000000 | 0.31 | 4.510000 | 1.490000 | 6745.000000 | 320.000000 | 0.99 | 0.470000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 4.250000 | 5.130000 | 94.000000 | 1020.000000 | 0.29 | 5.130000 | 3.770000 | 6210.000000 | 341.000000 | 0.97 | 0.420000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 4.430000 | 6.430000 | 87.000000 | 1019.000000 | 0.21 | 6.430000 | 6.550000 | 10000.000000 | 310.000000 | 0.84 | 0.830000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 5.040000 | 7.390000 | 85.000000 | 1018.000000 | 0.51 | 7.390000 | 11.580000 | 10000.000000 | 301.000000 | 1.1 | 1.050000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 5.450000 | 7.640000 | 86.000000 | 1017.000000 | 0.86 | 7.640000 | 12.920000 | 7358.000000 | 295.000000 | 1.07 | 0.960000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | 5.830000 | 7.690000 | 88.000000 | 1016.000000 | 1.05 | 7.690000 | 12.010000 | 8708.000000 | 291.000000 | 1.11 | 1.120000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 19:00:00 | 95.000000 | 5.710000 | 7.400000 | 89.000000 | 1015.000000 | 1.15 | 7.400000 | 9.660000 | 5380.000000 | 292.000000 | 1.26 | 1.140000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 20:00:00 | 97.000000 | 5.440000 | 6.800000 | 91.000000 | 1015.000000 | 1.21 | 6.800000 | 5.870000 | 6066.000000 | 293.000000 | 1.39 | 1.230000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 21:00:00 | 97.000000 | 5.170000 | 6.220000 | 93.000000 | 1014.000000 | 1.01 | 6.220000 | 2.570000 | 6783.000000 | 294.000000 | 1.25 | 0.990000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 4.890000 | 5.630000 | 95.000000 | 1015.000000 | 0.91 | 5.630000 | 0.630000 | 10000.000000 | 296.000000 | 1.25 | 0.910000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055060 | "ALPES LOS - AUT [21055060]" | 2.971139 | -76.115778 | 4530.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2007-11-20 00:00:00 | 2010-09-29 00:00:00 | Cauca | Páez (Belalcázar) | Quebrada Don Abad | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Palo | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 3.940000 | 4.370000 | 97.000000 | 1016.000000 | 0.9 | 4.370000 | 0.000000 | 10000.000000 | 307.000000 | 1.01 | 0.530000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21055060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21055060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21055060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055060_OWM_Windspeed_20220111.png)
