
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ZETAQUIRA - AUT [35085060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35085060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.29494444,-73.16994444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.29494444&lon=-73.16994444)


| Parameter | Value |
|---|---|
| Code | 35085060 |
| Name | ZETAQUIRA - AUT [35085060] |
| Latitude, ° | 5.29494444 |
| Longitude, ° | -73.16994444 |
| Elevation, m | 1436 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-12 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Zetaquirá |
| Stream | San Juan |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Lengupá |

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

### (CNE index 128) Open Weather values for station 35085060 - ZETAQUIRA - AUT [35085060]

JSON data from API OWM:

```
{'lat': 5.2949, 'lon': -73.1699, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812698, 'sunset': 1641855303, 'temp': 21.17, 'feels_like': 21.51, 'pressure': 1013, 'humidity': 83, 'dew_point': 18.17, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 151, 'wind_gust': 2.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, 'hourly': [{'dt': 1641772800, 'temp': 18.9, 'feels_like': 19.38, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.41, 'uvi': 0, 'clouds': 100, 'visibility': 900, 'wind_speed': 0.59, 'wind_deg': 166, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 18.82, 'feels_like': 19.29, 'pressure': 1017, 'humidity': 97, 'dew_point': 18.33, 'uvi': 0, 'clouds': 100, 'visibility': 1155, 'wind_speed': 0.48, 'wind_deg': 176, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 18.71, 'feels_like': 19.17, 'pressure': 1018, 'humidity': 97, 'dew_point': 18.22, 'uvi': 0, 'clouds': 99, 'visibility': 2584, 'wind_speed': 0.57, 'wind_deg': 179, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 18.52, 'feels_like': 18.96, 'pressure': 1018, 'humidity': 97, 'dew_point': 18.03, 'uvi': 0, 'clouds': 99, 'visibility': 2418, 'wind_speed': 0.45, 'wind_deg': 188, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.45, 'feels_like': 18.86, 'pressure': 1018, 'humidity': 96, 'dew_point': 17.8, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 192, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 18.31, 'feels_like': 18.7, 'pressure': 1018, 'humidity': 96, 'dew_point': 17.66, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 209, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.29, 'feels_like': 18.68, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.64, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 216, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 18.17, 'feels_like': 18.55, 'pressure': 1015, 'humidity': 96, 'dew_point': 17.52, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 213, 'wind_gust': 0.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 17.74, 'feels_like': 18.08, 'pressure': 1015, 'humidity': 96, 'dew_point': 17.09, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 260, 'wind_gust': 0.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 17.23, 'feels_like': 17.49, 'pressure': 1015, 'humidity': 95, 'dew_point': 16.42, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 255, 'wind_gust': 0.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 16.82, 'feels_like': 17.06, 'pressure': 1016, 'humidity': 96, 'dew_point': 16.18, 'uvi': 0, 'clouds': 91, 'visibility': 8229, 'wind_speed': 0.22, 'wind_deg': 346, 'wind_gust': 0.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 16.69, 'feels_like': 16.92, 'pressure': 1017, 'humidity': 96, 'dew_point': 16.05, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 359, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 17.88, 'feels_like': 18.15, 'pressure': 1018, 'humidity': 93, 'dew_point': 16.73, 'uvi': 0.61, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 219, 'wind_gust': 0.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 19.45, 'feels_like': 19.67, 'pressure': 1019, 'humidity': 85, 'dew_point': 16.86, 'uvi': 2.53, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 192, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 20.57, 'feels_like': 20.72, 'pressure': 1019, 'humidity': 78, 'dew_point': 16.6, 'uvi': 5.9, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 183, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.6, 'feels_like': 21.72, 'pressure': 1018, 'humidity': 73, 'dew_point': 16.56, 'uvi': 9.82, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 168, 'wind_gust': 1.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 22.33, 'feels_like': 22.47, 'pressure': 1017, 'humidity': 71, 'dew_point': 16.82, 'uvi': 12.42, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 164, 'wind_gust': 2.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 24.58, 'feels_like': 24.69, 'pressure': 1015, 'humidity': 61, 'dew_point': 16.57, 'uvi': 13.35, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 153, 'wind_gust': 1.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 24.02, 'feels_like': 24.2, 'pressure': 1014, 'humidity': 66, 'dew_point': 17.28, 'uvi': 11.96, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 155, 'wind_gust': 2.28, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 22.32, 'feels_like': 22.59, 'pressure': 1014, 'humidity': 76, 'dew_point': 17.89, 'uvi': 7.26, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 155, 'wind_gust': 2.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641844800, 'temp': 21.17, 'feels_like': 21.51, 'pressure': 1013, 'humidity': 83, 'dew_point': 18.17, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 151, 'wind_gust': 2.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641848400, 'temp': 20.38, 'feels_like': 20.8, 'pressure': 1014, 'humidity': 89, 'dew_point': 18.51, 'uvi': 1.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 149, 'wind_gust': 2.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641852000, 'temp': 19.56, 'feels_like': 20, 'pressure': 1015, 'humidity': 93, 'dew_point': 18.4, 'uvi': 0.29, 'clouds': 99, 'visibility': 5472, 'wind_speed': 0.95, 'wind_deg': 142, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641855600, 'temp': 18.92, 'feels_like': 19.37, 'pressure': 1015, 'humidity': 96, 'dew_point': 18.27, 'uvi': 0, 'clouds': 99, 'visibility': 4817, 'wind_speed': 0.64, 'wind_deg': 157, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 18.410000 | 19.380000 | 97.000000 | 1016.000000 |  | 18.900000 | 0.000000 | 900.000000 | 166.000000 | 1.07 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 18.330000 | 19.290000 | 97.000000 | 1017.000000 |  | 18.820000 | 0.000000 | 1155.000000 | 176.000000 | 0.85 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 18.220000 | 19.170000 | 97.000000 | 1018.000000 |  | 18.710000 | 0.000000 | 2584.000000 | 179.000000 | 1.09 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 18.030000 | 18.960000 | 97.000000 | 1018.000000 |  | 18.520000 | 0.000000 | 2418.000000 | 188.000000 | 0.9 | 0.450000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 17.800000 | 18.860000 | 96.000000 | 1018.000000 |  | 18.450000 | 0.000000 | 10000.000000 | 192.000000 | 0.87 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 17.660000 | 18.700000 | 96.000000 | 1018.000000 |  | 18.310000 | 0.000000 | 10000.000000 | 209.000000 | 1.12 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 06:00:00 | 92.000000 | 17.640000 | 18.680000 | 96.000000 | 1017.000000 |  | 18.290000 | 0.000000 | 10000.000000 | 216.000000 | 0.68 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 17.520000 | 18.550000 | 96.000000 | 1015.000000 |  | 18.170000 | 0.000000 | 10000.000000 | 213.000000 | 0.34 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 17.090000 | 18.080000 | 96.000000 | 1015.000000 |  | 17.740000 | 0.000000 | 10000.000000 | 260.000000 | 0.46 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 16.420000 | 17.490000 | 95.000000 | 1015.000000 |  | 17.230000 | 0.000000 | 10000.000000 | 255.000000 | 0.36 | 0.140000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 16.180000 | 17.060000 | 96.000000 | 1016.000000 |  | 16.820000 | 0.000000 | 8229.000000 | 346.000000 | 0.4 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 11:00:00 | 88.000000 | 16.050000 | 16.920000 | 96.000000 | 1017.000000 |  | 16.690000 | 0.000000 | 10000.000000 | 359.000000 | 0.51 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 12:00:00 | 66.000000 | 16.730000 | 18.150000 | 93.000000 | 1018.000000 |  | 17.880000 | 0.610000 | 10000.000000 | 219.000000 | 0.79 | 0.330000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 13:00:00 | 65.000000 | 16.860000 | 19.670000 | 85.000000 | 1019.000000 |  | 19.450000 | 2.530000 | 10000.000000 | 192.000000 | 0.85 | 0.740000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 16.600000 | 20.720000 | 78.000000 | 1019.000000 |  | 20.570000 | 5.900000 | 10000.000000 | 183.000000 | 1.14 | 0.990000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 16.560000 | 21.720000 | 73.000000 | 1018.000000 |  | 21.600000 | 9.820000 | 10000.000000 | 168.000000 | 1.78 | 1.320000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 16.820000 | 22.470000 | 71.000000 | 1017.000000 |  | 22.330000 | 12.420000 | 10000.000000 | 164.000000 | 2.32 | 1.560000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 17:00:00 | 71.000000 | 16.570000 | 24.690000 | 61.000000 | 1015.000000 |  | 24.580000 | 13.350000 | 10000.000000 | 153.000000 | 1.91 | 1.780000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 18:00:00 | 88.000000 | 17.280000 | 24.200000 | 66.000000 | 1014.000000 |  | 24.020000 | 11.960000 | 10000.000000 | 155.000000 | 2.28 | 2.080000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 19:00:00 | 97.000000 | 17.890000 | 22.590000 | 76.000000 | 1014.000000 | 0.13 | 22.320000 | 7.260000 | 10000.000000 | 155.000000 | 2.44 | 1.940000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 18.170000 | 21.510000 | 83.000000 | 1013.000000 | 0.13 | 21.170000 | 4.130000 | 10000.000000 | 151.000000 | 2.3 | 1.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 18.510000 | 20.800000 | 89.000000 | 1014.000000 | 0.23 | 20.380000 | 1.610000 | 10000.000000 | 149.000000 | 2.14 | 1.280000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 18.400000 | 20.000000 | 93.000000 | 1015.000000 | 0.12 | 19.560000 | 0.290000 | 5472.000000 | 142.000000 | 1.88 | 0.950000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085060 | "ZETAQUIRA - AUT [35085060]" | 5.294944 | -73.169944 | 1436.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-12 00:00:00 | NaT | Boyacá | Zetaquirá | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Lengupá | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 18.270000 | 19.370000 | 96.000000 | 1015.000000 |  | 18.920000 | 0.000000 | 4817.000000 | 157.000000 | 1.59 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35085060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35085060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35085060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085060_OWM_Windspeed_20220111.png)
