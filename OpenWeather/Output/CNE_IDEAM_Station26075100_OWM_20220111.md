
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GRANJA EXP HOESCHST [26075100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26075100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.63333333,-76.43333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.63333333&lon=-76.43333333)


| Parameter | Value |
|---|---|
| Code | 26075100 |
| Name | GRANJA EXP HOESCHST [26075100] |
| Latitude, ° | 3.63333333 |
| Longitude, ° | -76.43333333 |
| Elevation, m | 950 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1990-06-15 00:00:00 |
| Suspension date | 2002-10-15 00:00:00 |
| State | Valle del Cauca |
| County | Palmira |
| Stream | Guaviare |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Amaime y Cerrito |

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

### (CNE index 2379) Open Weather values for station 26075100 - GRANJA EXP HOESCHST [26075100]

JSON data from API OWM:

```
{'lat': 3.6333, 'lon': -76.4333, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813320, 'sunset': 1641856247, 'temp': 28.1, 'feels_like': 28.66, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.02, 'uvi': 3.14, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 170, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, 'hourly': [{'dt': 1641772800, 'temp': 25.1, 'feels_like': 25.36, 'pressure': 1014, 'humidity': 65, 'dew_point': 18.06, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 330, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641776400, 'temp': 23.1, 'feels_like': 23.37, 'pressure': 1015, 'humidity': 73, 'dew_point': 18, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 350, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641780000, 'temp': 23.1, 'feels_like': 23.37, 'pressure': 1015, 'humidity': 73, 'dew_point': 18, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 350, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641783600, 'temp': 23.1, 'feels_like': 23.37, 'pressure': 1016, 'humidity': 73, 'dew_point': 18, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 350, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641787200, 'temp': 23.1, 'feels_like': 23.37, 'pressure': 1016, 'humidity': 73, 'dew_point': 18, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 360, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 22.1, 'feels_like': 22.4, 'pressure': 1016, 'humidity': 78, 'dew_point': 18.09, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 10, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.1, 'feels_like': 22.4, 'pressure': 1016, 'humidity': 78, 'dew_point': 18.09, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.1, 'feels_like': 21.43, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.1, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 50, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.1, 'feels_like': 21.43, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.1, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641805200, 'temp': 21.1, 'feels_like': 21.43, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.1, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 70, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 20.1, 'feels_like': 20.46, 'pressure': 1015, 'humidity': 88, 'dew_point': 18.05, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641812400, 'temp': 20.1, 'feels_like': 20.46, 'pressure': 1016, 'humidity': 88, 'dew_point': 18.05, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 80, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641816000, 'temp': 21.1, 'feels_like': 21.43, 'pressure': 1017, 'humidity': 83, 'dew_point': 18.1, 'uvi': 0.2, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641819600, 'temp': 22.1, 'feels_like': 22.53, 'pressure': 1018, 'humidity': 83, 'dew_point': 19.08, 'uvi': 1.36, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641823200, 'temp': 23.1, 'feels_like': 23.5, 'pressure': 1019, 'humidity': 78, 'dew_point': 19.06, 'uvi': 3.44, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641826800, 'temp': 25.1, 'feels_like': 25.47, 'pressure': 1018, 'humidity': 69, 'dew_point': 19.01, 'uvi': 6.01, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 170, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641830400, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1018, 'humidity': 65, 'dew_point': 19.01, 'uvi': 7.7, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 200, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641834000, 'temp': 27.1, 'feels_like': 27.99, 'pressure': 1017, 'humidity': 57, 'dew_point': 17.85, 'uvi': 8.58, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641837600, 'temp': 27.1, 'feels_like': 27.99, 'pressure': 1016, 'humidity': 57, 'dew_point': 17.85, 'uvi': 7.98, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 190, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641841200, 'temp': 28.1, 'feels_like': 29.26, 'pressure': 1015, 'humidity': 57, 'dew_point': 18.78, 'uvi': 5.2, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 180, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641844800, 'temp': 28.1, 'feels_like': 28.66, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.02, 'uvi': 3.14, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 170, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641848400, 'temp': 24.1, 'feels_like': 24.47, 'pressure': 1013, 'humidity': 73, 'dew_point': 18.96, 'uvi': 1.37, 'clouds': 75, 'visibility': 8000, 'wind_speed': 5.14, 'wind_deg': 300, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641852000, 'temp': 22.1, 'feels_like': 22.4, 'pressure': 1014, 'humidity': 78, 'dew_point': 18.09, 'uvi': 0.21, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641855600, 'temp': 20.1, 'feels_like': 20.46, 'pressure': 1016, 'humidity': 88, 'dew_point': 18.05, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 5.14, 'wind_deg': 330, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 00:00:00 | 75.000000 | 18.060000 | 25.360000 | 65.000000 | 1014.000000 | 0.21 | 25.100000 | 0.000000 | 10000.000000 | 330.000000 |  | 4.120000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 18.000000 | 23.370000 | 73.000000 | 1015.000000 | 0.34 | 23.100000 | 0.000000 | 10000.000000 | 350.000000 |  | 5.660000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 02:00:00 | 75.000000 | 18.000000 | 23.370000 | 73.000000 | 1015.000000 | 0.27 | 23.100000 | 0.000000 | 10000.000000 | 350.000000 |  | 5.140000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 03:00:00 | 75.000000 | 18.000000 | 23.370000 | 73.000000 | 1016.000000 | 0.18 | 23.100000 | 0.000000 | 10000.000000 | 350.000000 |  | 4.120000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 04:00:00 | 75.000000 | 18.000000 | 23.370000 | 73.000000 | 1016.000000 | 0.13 | 23.100000 | 0.000000 | 10000.000000 | 360.000000 |  | 5.140000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 05:00:00 | 75.000000 | 18.090000 | 22.400000 | 78.000000 | 1016.000000 |  | 22.100000 | 0.000000 | 10000.000000 | 10.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 18.090000 | 22.400000 | 78.000000 | 1016.000000 |  | 22.100000 | 0.000000 | 10000.000000 | 40.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 07:00:00 | 75.000000 | 18.100000 | 21.430000 | 83.000000 | 1015.000000 |  | 21.100000 | 0.000000 | 10000.000000 | 50.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 08:00:00 | 75.000000 | 18.100000 | 21.430000 | 83.000000 | 1015.000000 | 0.14 | 21.100000 | 0.000000 | 10000.000000 | 60.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 09:00:00 | 40.000000 | 18.100000 | 21.430000 | 83.000000 | 1015.000000 | 0.18 | 21.100000 | 0.000000 | 10000.000000 | 70.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 10:00:00 | 40.000000 | 18.050000 | 20.460000 | 88.000000 | 1015.000000 | 0.21 | 20.100000 | 0.000000 | 10000.000000 | 20.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 18.050000 | 20.460000 | 88.000000 | 1016.000000 | 0.15 | 20.100000 | 0.000000 | 10000.000000 | 80.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 18.100000 | 21.430000 | 83.000000 | 1017.000000 | 0.15 | 21.100000 | 0.200000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 19.080000 | 22.530000 | 83.000000 | 1018.000000 | 0.38 | 22.100000 | 1.360000 | 10000.000000 | 310.000000 |  | 1.540000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 19.060000 | 23.500000 | 78.000000 | 1019.000000 | 0.47 | 23.100000 | 3.440000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 15:00:00 | 40.000000 | 19.010000 | 25.470000 | 69.000000 | 1018.000000 | 0.44 | 25.100000 | 6.010000 | 10000.000000 | 170.000000 |  | 1.540000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 19.010000 | 26.100000 | 65.000000 | 1018.000000 | 0.88 | 26.100000 | 7.700000 | 10000.000000 | 200.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 17.850000 | 27.990000 | 57.000000 | 1017.000000 | 0.81 | 27.100000 | 8.580000 | 10000.000000 | 0.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 17.850000 | 27.990000 | 57.000000 | 1016.000000 | 1.02 | 27.100000 | 7.980000 | 10000.000000 | 190.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 18.780000 | 29.260000 | 57.000000 | 1015.000000 | 1.08 | 28.100000 | 5.200000 | 10000.000000 | 180.000000 |  | 3.090000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 20:00:00 | 40.000000 | 17.020000 | 28.660000 | 51.000000 | 1013.000000 | 1.01 | 28.100000 | 3.140000 | 10000.000000 | 170.000000 |  | 3.090000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 18.960000 | 24.470000 | 73.000000 | 1013.000000 | 1.01 | 24.100000 | 1.370000 | 8000.000000 | 300.000000 |  | 5.140000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 18.090000 | 22.400000 | 78.000000 | 1014.000000 | 0.88 | 22.100000 | 0.210000 | 10000.000000 | 290.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075100 | "GRANJA EXP HOESCHST [26075100]" | 3.633333 | -76.433333 | 950.000000 | Climática Principal | Convencional | Suspendida | 1990-06-15 00:00:00 | 2002-10-15 00:00:00 | Valle del Cauca | Palmira | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Amaime y Cerrito | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 18.050000 | 20.460000 | 88.000000 | 1016.000000 | 1.12 | 20.100000 | 0.000000 | 7000.000000 | 330.000000 |  | 5.140000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26075100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26075100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26075100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075100_OWM_Windspeed_20220111.png)
