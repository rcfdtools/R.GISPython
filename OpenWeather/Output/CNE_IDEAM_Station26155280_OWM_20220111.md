
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NEV SANTA ISABEL [26155280] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26155280_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.81758333,-75.37405556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.81758333&lon=-75.37405556)


| Parameter | Value |
|---|---|
| Code | 26155280 |
| Name | NEV SANTA ISABEL [26155280] |
| Latitude, ° | 4.81758333 |
| Longitude, ° | -75.37405556 |
| Elevation, m | 4685 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2010-04-23 00:00:00 |
| Suspension date | NaT |
| State | Caldas |
| County | Villamaria |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Chinchiná |

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

### (CNE index 3635) Open Weather values for station 26155280 - NEV SANTA ISABEL [26155280]

JSON data from API OWM:

```
{'lat': 4.8176, 'lon': -75.3741, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813181, 'sunset': 1641855878, 'temp': -2.75, 'feels_like': -2.75, 'pressure': 1016, 'humidity': 92, 'dew_point': -3.74, 'uvi': 3, 'clouds': 93, 'visibility': 5217, 'wind_speed': 0.94, 'wind_deg': 278, 'wind_gust': 1.1, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.65}}, 'hourly': [{'dt': 1641772800, 'temp': -0.78, 'feels_like': -0.78, 'pressure': 1018, 'humidity': 96, 'dew_point': -1.27, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 19, 'wind_gust': 1.09, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'snow': {'1h': 0.24}}, {'dt': 1641776400, 'temp': -0.93, 'feels_like': -0.93, 'pressure': 1019, 'humidity': 93, 'dew_point': -1.8, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 356, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': -1.78, 'feels_like': -1.78, 'pressure': 1020, 'humidity': 94, 'dew_point': -2.52, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 329, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': -1.78, 'feels_like': -1.78, 'pressure': 1020, 'humidity': 94, 'dew_point': -2.52, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 289, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': -2.51, 'feels_like': -2.51, 'pressure': 1020, 'humidity': 94, 'dew_point': -3.25, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 292, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': -2.51, 'feels_like': -2.51, 'pressure': 1020, 'humidity': 95, 'dew_point': -3.12, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 259, 'wind_gust': 0.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': -2.51, 'feels_like': -2.51, 'pressure': 1019, 'humidity': 94, 'dew_point': -3.25, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 275, 'wind_gust': 0.8, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': -2.51, 'feels_like': -2.51, 'pressure': 1018, 'humidity': 94, 'dew_point': -3.25, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 255, 'wind_gust': 0.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': -4.06, 'feels_like': -4.06, 'pressure': 1018, 'humidity': 94, 'dew_point': -4.79, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 274, 'wind_gust': 0.98, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'snow': {'1h': 0.12}}, {'dt': 1641805200, 'temp': -4.02, 'feels_like': -4.02, 'pressure': 1018, 'humidity': 95, 'dew_point': -4.62, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 279, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': -3.51, 'feels_like': -3.51, 'pressure': 1019, 'humidity': 95, 'dew_point': -4.12, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 280, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': -3.64, 'feels_like': -3.64, 'pressure': 1020, 'humidity': 96, 'dew_point': -4.12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 277, 'wind_gust': 1.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': -3.37, 'feels_like': -3.37, 'pressure': 1020, 'humidity': 94, 'dew_point': -4.1, 'uvi': 0.14, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 281, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': -3.37, 'feels_like': -3.37, 'pressure': 1020, 'humidity': 91, 'dew_point': -4.48, 'uvi': 1.92, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 287, 'wind_gust': 1.16, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.13}}, {'dt': 1641823200, 'temp': -2.18, 'feels_like': -2.18, 'pressure': 1020, 'humidity': 86, 'dew_point': -3.97, 'uvi': 4.8, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 315, 'wind_gust': 1.17, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.23}}, {'dt': 1641826800, 'temp': -0.64, 'feels_like': -0.64, 'pressure': 1020, 'humidity': 81, 'dew_point': -3.16, 'uvi': 8.25, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 306, 'wind_gust': 1.42, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.34}}, {'dt': 1641830400, 'temp': 1.59, 'feels_like': 1.59, 'pressure': 1019, 'humidity': 85, 'dew_point': -0.58, 'uvi': 9.29, 'clouds': 64, 'visibility': 5079, 'wind_speed': 0.47, 'wind_deg': 310, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641834000, 'temp': -0.56, 'feels_like': -0.56, 'pressure': 1018, 'humidity': 89, 'dew_point': -1.96, 'uvi': 10.23, 'clouds': 70, 'visibility': 9276, 'wind_speed': 0.74, 'wind_deg': 293, 'wind_gust': 1.33, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.44}}, {'dt': 1641837600, 'temp': -1.98, 'feels_like': -1.98, 'pressure': 1018, 'humidity': 92, 'dew_point': -2.97, 'uvi': 9.4, 'clouds': 81, 'visibility': 2846, 'wind_speed': 0.78, 'wind_deg': 276, 'wind_gust': 0.97, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.7}}, {'dt': 1641841200, 'temp': -1.94, 'feels_like': -1.94, 'pressure': 1016, 'humidity': 92, 'dew_point': -2.93, 'uvi': 5.06, 'clouds': 92, 'visibility': 2483, 'wind_speed': 0.9, 'wind_deg': 273, 'wind_gust': 1.07, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.68}}, {'dt': 1641844800, 'temp': -2.75, 'feels_like': -2.75, 'pressure': 1016, 'humidity': 92, 'dew_point': -3.74, 'uvi': 3, 'clouds': 93, 'visibility': 5217, 'wind_speed': 0.94, 'wind_deg': 278, 'wind_gust': 1.1, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.65}}, {'dt': 1641848400, 'temp': -1.83, 'feels_like': -1.83, 'pressure': 1016, 'humidity': 93, 'dew_point': -2.7, 'uvi': 1.25, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 276, 'wind_gust': 0.89, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.62}}, {'dt': 1641852000, 'temp': -2.52, 'feels_like': -2.52, 'pressure': 1016, 'humidity': 96, 'dew_point': -3.01, 'uvi': 0.4, 'clouds': 96, 'visibility': 8033, 'wind_speed': 0.68, 'wind_deg': 292, 'wind_gust': 1.07, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'snow': {'1h': 0.46}}, {'dt': 1641855600, 'temp': -3.06, 'feels_like': -3.06, 'pressure': 1017, 'humidity': 98, 'dew_point': -3.3, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 292, 'wind_gust': 0.72, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'snow': {'1h': 0.52}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![13n.png](http://openweathermap.org/img/w/13n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 00:00:00 | 68.000000 | -1.270000 | -0.780000 | 96.000000 | 1018.000000 |  | -0.780000 | 0.000000 | 10000.000000 | 19.000000 | 1.09 | 0.580000 | 600 | Snow | light snow | 13n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 01:00:00 | 98.000000 | -1.800000 | -0.930000 | 93.000000 | 1019.000000 |  | -0.930000 | 0.000000 | 10000.000000 | 356.000000 | 0.95 | 0.560000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 02:00:00 | 97.000000 | -2.520000 | -1.780000 | 94.000000 | 1020.000000 |  | -1.780000 | 0.000000 | 10000.000000 | 329.000000 | 0.91 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | -2.520000 | -1.780000 | 94.000000 | 1020.000000 |  | -1.780000 | 0.000000 | 10000.000000 | 289.000000 | 0.78 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 04:00:00 | 96.000000 | -3.250000 | -2.510000 | 94.000000 | 1020.000000 |  | -2.510000 | 0.000000 | 10000.000000 | 292.000000 | 0.73 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | -3.120000 | -2.510000 | 95.000000 | 1020.000000 |  | -2.510000 | 0.000000 | 10000.000000 | 259.000000 | 0.69 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 06:00:00 | 34.000000 | -3.250000 | -2.510000 | 94.000000 | 1019.000000 |  | -2.510000 | 0.000000 | 10000.000000 | 275.000000 | 0.8 | 0.390000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 07:00:00 | 49.000000 | -3.250000 | -2.510000 | 94.000000 | 1018.000000 |  | -2.510000 | 0.000000 | 10000.000000 | 255.000000 | 0.92 | 0.200000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![13n.png](http://openweathermap.org/img/w/13n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 08:00:00 | 58.000000 | -4.790000 | -4.060000 | 94.000000 | 1018.000000 |  | -4.060000 | 0.000000 | 10000.000000 | 274.000000 | 0.98 | 0.350000 | 600 | Snow | light snow | 13n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 09:00:00 | 60.000000 | -4.620000 | -4.020000 | 95.000000 | 1018.000000 |  | -4.020000 | 0.000000 | 10000.000000 | 279.000000 | 0.95 | 0.690000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 10:00:00 | 69.000000 | -4.120000 | -3.510000 | 95.000000 | 1019.000000 |  | -3.510000 | 0.000000 | 10000.000000 | 280.000000 | 1.15 | 0.830000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | -4.120000 | -3.640000 | 96.000000 | 1020.000000 |  | -3.640000 | 0.000000 | 10000.000000 | 277.000000 | 1.1 | 0.890000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 12:00:00 | 53.000000 | -4.100000 | -3.370000 | 94.000000 | 1020.000000 |  | -3.370000 | 0.140000 | 10000.000000 | 281.000000 | 1.08 | 0.520000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 13:00:00 | 55.000000 | -4.480000 | -3.370000 | 91.000000 | 1020.000000 |  | -3.370000 | 1.920000 | 10000.000000 | 287.000000 | 1.16 | 0.630000 | 600 | Snow | light snow | 13d | 13 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 14:00:00 | 53.000000 | -3.970000 | -2.180000 | 86.000000 | 1020.000000 |  | -2.180000 | 4.800000 | 10000.000000 | 315.000000 | 1.17 | 0.310000 | 600 | Snow | light snow | 13d | 14 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 15:00:00 | 57.000000 | -3.160000 | -0.640000 | 81.000000 | 1020.000000 |  | -0.640000 | 8.250000 | 10000.000000 | 306.000000 | 1.42 | 0.400000 | 600 | Snow | light snow | 13d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 16:00:00 | 64.000000 | -0.580000 | 1.590000 | 85.000000 | 1019.000000 | 0.31 | 1.590000 | 9.290000 | 5079.000000 | 310.000000 | 1.15 | 0.470000 | 500 | Rain | light rain | 10d | 16 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | -1.960000 | -0.560000 | 89.000000 | 1018.000000 |  | -0.560000 | 10.230000 | 9276.000000 | 293.000000 | 1.33 | 0.740000 | 600 | Snow | light snow | 13d | 17 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | -2.970000 | -1.980000 | 92.000000 | 1018.000000 |  | -1.980000 | 9.400000 | 2846.000000 | 276.000000 | 0.97 | 0.780000 | 601 | Snow | snow | 13d | 18 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 19:00:00 | 92.000000 | -2.930000 | -1.940000 | 92.000000 | 1016.000000 |  | -1.940000 | 5.060000 | 2483.000000 | 273.000000 | 1.07 | 0.900000 | 601 | Snow | snow | 13d | 19 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 20:00:00 | 93.000000 | -3.740000 | -2.750000 | 92.000000 | 1016.000000 |  | -2.750000 | 3.000000 | 5217.000000 | 278.000000 | 1.1 | 0.940000 | 601 | Snow | snow | 13d | 20 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 21:00:00 | 95.000000 | -2.700000 | -1.830000 | 93.000000 | 1016.000000 |  | -1.830000 | 1.250000 | 10000.000000 | 276.000000 | 0.89 | 0.720000 | 601 | Snow | snow | 13d | 21 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | -3.010000 | -2.520000 | 96.000000 | 1016.000000 |  | -2.520000 | 0.400000 | 8033.000000 | 292.000000 | 1.07 | 0.680000 | 600 | Snow | light snow | 13d | 22 |
| ![13d.png](http://openweathermap.org/img/w/13d.png) | 26155280 | "NEV SANTA ISABEL [26155280]" | 4.817583 | -75.374056 | 4685.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-04-23 00:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | -3.300000 | -3.060000 | 98.000000 | 1017.000000 |  | -3.060000 | 0.000000 | 10000.000000 | 292.000000 | 0.72 | 0.450000 | 601 | Snow | snow | 13d | 23 |


### Weather plots

![CNE_IDEAM_Station26155280_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26155280_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26155280_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155280_OWM_Windspeed_20220111.png)
