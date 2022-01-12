
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - HIMAT R 4 [24035090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.78333333,-73.05) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.78333333&lon=-73.05)


| Parameter | Value |
|---|---|
| Code | 24035090 |
| Name | HIMAT R 4 [24035090] |
| Latitude, ° | 5.78333333 |
| Longitude, ° | -73.05 |
| Elevation, m | 2500 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1994-07-15 00:00:00 |
| Suspension date | 1996-08-15 00:00:00 |
| State | Boyacá |
| County | Duitama |
| Stream | Chicamocha |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Chicamocha |

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

### (CNE index 2062) Open Weather values for station 24035090 - HIMAT R 4 [24035090]

JSON data from API OWM:

```
{'lat': 5.7833, 'lon': -73.05, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812716, 'sunset': 1641855227, 'temp': 19.93, 'feels_like': 19.34, 'pressure': 1010, 'humidity': 52, 'dew_point': 9.79, 'uvi': 3.84, 'clouds': 87, 'visibility': 10000, 'wind_speed': 3.76, 'wind_deg': 314, 'wind_gust': 4.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 12.65, 'feels_like': 12.4, 'pressure': 1016, 'humidity': 93, 'dew_point': 11.55, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 310, 'wind_gust': 1.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 12.03, 'feels_like': 11.77, 'pressure': 1018, 'humidity': 95, 'dew_point': 11.25, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 309, 'wind_gust': 1.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 11.58, 'feels_like': 11.27, 'pressure': 1019, 'humidity': 95, 'dew_point': 10.81, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 310, 'wind_gust': 1.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 10.8, 'feels_like': 10.44, 'pressure': 1019, 'humidity': 96, 'dew_point': 10.19, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 311, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10.45, 'feels_like': 10.06, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.84, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 300, 'wind_gust': 0.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.22, 'feels_like': 9.78, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.46, 'uvi': 0, 'clouds': 79, 'visibility': 8294, 'wind_speed': 0.52, 'wind_deg': 268, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.26, 'feels_like': 9.8, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.34, 'uvi': 0, 'clouds': 64, 'visibility': 7146, 'wind_speed': 0.37, 'wind_deg': 254, 'wind_gust': 0.55, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 10.55, 'feels_like': 10.09, 'pressure': 1017, 'humidity': 93, 'dew_point': 9.47, 'uvi': 0, 'clouds': 81, 'visibility': 6391, 'wind_speed': 0.26, 'wind_deg': 330, 'wind_gust': 0.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 10.69, 'feels_like': 10.14, 'pressure': 1016, 'humidity': 89, 'dew_point': 8.95, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 313, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 10.86, 'feels_like': 10.33, 'pressure': 1016, 'humidity': 89, 'dew_point': 9.12, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 8, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 10.82, 'feels_like': 10.28, 'pressure': 1017, 'humidity': 89, 'dew_point': 9.08, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 69, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 10.68, 'feels_like': 10.1, 'pressure': 1017, 'humidity': 88, 'dew_point': 8.78, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 93, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 11.07, 'feels_like': 10.53, 'pressure': 1019, 'humidity': 88, 'dew_point': 9.16, 'uvi': 0.57, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 78, 'wind_gust': 0.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 13.65, 'feels_like': 13.03, 'pressure': 1019, 'humidity': 75, 'dew_point': 9.31, 'uvi': 2.33, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 340, 'wind_gust': 0.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 15.74, 'feels_like': 15.09, 'pressure': 1019, 'humidity': 66, 'dew_point': 9.41, 'uvi': 5.47, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 301, 'wind_gust': 1.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.49, 'feels_like': 16.84, 'pressure': 1018, 'humidity': 59, 'dew_point': 9.4, 'uvi': 9.11, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 294, 'wind_gust': 2.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.64, 'feels_like': 17.97, 'pressure': 1016, 'humidity': 54, 'dew_point': 9.16, 'uvi': 11.79, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 285, 'wind_gust': 3.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.85, 'feels_like': 19.17, 'pressure': 1014, 'humidity': 49, 'dew_point': 8.84, 'uvi': 12.68, 'clouds': 65, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 290, 'wind_gust': 3.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 20.68, 'feels_like': 20, 'pressure': 1012, 'humidity': 46, 'dew_point': 8.66, 'uvi': 11.35, 'clouds': 74, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 302, 'wind_gust': 4.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 20.63, 'feels_like': 19.98, 'pressure': 1011, 'humidity': 47, 'dew_point': 8.93, 'uvi': 6.78, 'clouds': 76, 'visibility': 10000, 'wind_speed': 4.04, 'wind_deg': 308, 'wind_gust': 4.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 19.93, 'feels_like': 19.34, 'pressure': 1010, 'humidity': 52, 'dew_point': 9.79, 'uvi': 3.84, 'clouds': 87, 'visibility': 10000, 'wind_speed': 3.76, 'wind_deg': 314, 'wind_gust': 4.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 18.57, 'feels_like': 18.08, 'pressure': 1011, 'humidity': 61, 'dew_point': 10.91, 'uvi': 1.5, 'clouds': 89, 'visibility': 10000, 'wind_speed': 3.46, 'wind_deg': 311, 'wind_gust': 3.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641852000, 'temp': 16.68, 'feels_like': 16.31, 'pressure': 1012, 'humidity': 73, 'dew_point': 11.82, 'uvi': 0.36, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 309, 'wind_gust': 3.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641855600, 'temp': 13.36, 'feels_like': 13.1, 'pressure': 1015, 'humidity': 90, 'dew_point': 11.76, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 305, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 68.000000 | 11.550000 | 12.400000 | 93.000000 | 1016.000000 |  | 12.650000 | 0.000000 | 10000.000000 | 310.000000 | 1.52 | 1.600000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 73.000000 | 11.250000 | 11.770000 | 95.000000 | 1018.000000 |  | 12.030000 | 0.000000 | 10000.000000 | 309.000000 | 1.47 | 1.500000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 74.000000 | 10.810000 | 11.270000 | 95.000000 | 1019.000000 |  | 11.580000 | 0.000000 | 10000.000000 | 310.000000 | 1.49 | 1.420000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 75.000000 | 10.190000 | 10.440000 | 96.000000 | 1019.000000 |  | 10.800000 | 0.000000 | 10000.000000 | 311.000000 | 1.26 | 1.120000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 81.000000 | 9.840000 | 10.060000 | 96.000000 | 1019.000000 |  | 10.450000 | 0.000000 | 10000.000000 | 300.000000 | 0.98 | 0.750000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 79.000000 | 9.460000 | 9.780000 | 95.000000 | 1019.000000 |  | 10.220000 | 0.000000 | 8294.000000 | 268.000000 | 0.73 | 0.520000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 64.000000 | 9.340000 | 9.800000 | 94.000000 | 1018.000000 |  | 10.260000 | 0.000000 | 7146.000000 | 254.000000 | 0.55 | 0.370000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 81.000000 | 9.470000 | 10.090000 | 93.000000 | 1017.000000 |  | 10.550000 | 0.000000 | 6391.000000 | 330.000000 | 0.42 | 0.260000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 86.000000 | 8.950000 | 10.140000 | 89.000000 | 1016.000000 |  | 10.690000 | 0.000000 | 10000.000000 | 313.000000 | 0.64 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 89.000000 | 9.120000 | 10.330000 | 89.000000 | 1016.000000 |  | 10.860000 | 0.000000 | 10000.000000 | 8.000000 | 0.64 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 9.080000 | 10.280000 | 89.000000 | 1017.000000 |  | 10.820000 | 0.000000 | 10000.000000 | 69.000000 | 0.67 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 90.000000 | 8.780000 | 10.100000 | 88.000000 | 1017.000000 |  | 10.680000 | 0.000000 | 10000.000000 | 93.000000 | 0.74 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 30.000000 | 9.160000 | 10.530000 | 88.000000 | 1019.000000 |  | 11.070000 | 0.570000 | 10000.000000 | 78.000000 | 0.75 | 0.610000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 49.000000 | 9.310000 | 13.030000 | 75.000000 | 1019.000000 |  | 13.650000 | 2.330000 | 10000.000000 | 340.000000 | 0.97 | 0.720000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 9.410000 | 15.090000 | 66.000000 | 1019.000000 |  | 15.740000 | 5.470000 | 10000.000000 | 301.000000 | 1.52 | 0.990000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 71.000000 | 9.400000 | 16.840000 | 59.000000 | 1018.000000 |  | 17.490000 | 9.110000 | 10000.000000 | 294.000000 | 2.51 | 1.280000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 70.000000 | 9.160000 | 17.970000 | 54.000000 | 1016.000000 |  | 18.640000 | 11.790000 | 10000.000000 | 285.000000 | 3.35 | 1.710000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 65.000000 | 8.840000 | 19.170000 | 49.000000 | 1014.000000 |  | 19.850000 | 12.680000 | 10000.000000 | 290.000000 | 3.83 | 2.450000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 74.000000 | 8.660000 | 20.000000 | 46.000000 | 1012.000000 |  | 20.680000 | 11.350000 | 10000.000000 | 302.000000 | 4.19 | 3.280000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 76.000000 | 8.930000 | 19.980000 | 47.000000 | 1011.000000 |  | 20.630000 | 6.780000 | 10000.000000 | 308.000000 | 4.34 | 4.040000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 87.000000 | 9.790000 | 19.340000 | 52.000000 | 1010.000000 |  | 19.930000 | 3.840000 | 10000.000000 | 314.000000 | 4.09 | 3.760000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 10.910000 | 18.080000 | 61.000000 | 1011.000000 | 0.11 | 18.570000 | 1.500000 | 10000.000000 | 311.000000 | 3.5 | 3.460000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 11.820000 | 16.310000 | 73.000000 | 1012.000000 | 0.12 | 16.680000 | 0.360000 | 10000.000000 | 309.000000 | 3.18 | 2.780000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035090 | "HIMAT R 4 [24035090]" | 5.783333 | -73.050000 | 2500.000000 | Climática Principal | Convencional | Suspendida | 1994-07-15 00:00:00 | 1996-08-15 00:00:00 | Boyacá | Duitama | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 80.000000 | 11.760000 | 13.100000 | 90.000000 | 1015.000000 |  | 13.360000 | 0.000000 | 10000.000000 | 305.000000 | 1.76 | 1.690000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station24035090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035090_OWM_Windspeed_20220111.png)
