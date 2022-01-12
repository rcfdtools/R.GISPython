
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO A LLERAS C [24035340] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035340_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.67694444,-72.96791667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.67694444&lon=-72.96791667)


| Parameter | Value |
|---|---|
| Code | 24035340 |
| Name | AEROPUERTO A LLERAS C [24035340] |
| Latitude, ° | 5.67694444 |
| Longitude, ° | -72.96791667 |
| Elevation, m | 2500 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1974-01-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Sogamoso |
| Stream | Pauto |
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

### (CNE index 2029) Open Weather values for station 24035340 - AEROPUERTO A LLERAS C [24035340]

JSON data from API OWM:

```
{'lat': 5.6769, 'lon': -72.9679, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812686, 'sunset': 1641855217, 'temp': 19, 'feels_like': 18.47, 'pressure': 1011, 'humidity': 58, 'dew_point': 10.56, 'uvi': 4.8, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 300, 'wind_gust': 3.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 13.24, 'feels_like': 13.02, 'pressure': 1016, 'humidity': 92, 'dew_point': 11.97, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 292, 'wind_gust': 1.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 12.82, 'feels_like': 12.61, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.88, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 296, 'wind_gust': 1.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.42, 'feels_like': 12.2, 'pressure': 1018, 'humidity': 95, 'dew_point': 11.64, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 298, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 11.4, 'feels_like': 11.13, 'pressure': 1019, 'humidity': 97, 'dew_point': 10.94, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 297, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10.81, 'feels_like': 10.48, 'pressure': 1019, 'humidity': 97, 'dew_point': 10.35, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 285, 'wind_gust': 0.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.59, 'feels_like': 10.21, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.98, 'uvi': 0, 'clouds': 84, 'visibility': 4936, 'wind_speed': 0.76, 'wind_deg': 265, 'wind_gust': 0.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.58, 'feels_like': 10.17, 'pressure': 1018, 'humidity': 95, 'dew_point': 9.81, 'uvi': 0, 'clouds': 66, 'visibility': 2493, 'wind_speed': 0.6, 'wind_deg': 266, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 10.76, 'feels_like': 10.37, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.99, 'uvi': 0, 'clouds': 82, 'visibility': 6739, 'wind_speed': 0.46, 'wind_deg': 304, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 10.75, 'feels_like': 10.28, 'pressure': 1016, 'humidity': 92, 'dew_point': 9.5, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 307, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 10.87, 'feels_like': 10.39, 'pressure': 1016, 'humidity': 91, 'dew_point': 9.46, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 342, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 10.84, 'feels_like': 10.36, 'pressure': 1017, 'humidity': 91, 'dew_point': 9.43, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 22, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 10.69, 'feels_like': 10.16, 'pressure': 1018, 'humidity': 90, 'dew_point': 9.12, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 62, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 11.27, 'feels_like': 10.75, 'pressure': 1019, 'humidity': 88, 'dew_point': 9.36, 'uvi': 0.42, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 59, 'wind_gust': 0.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 13.59, 'feels_like': 12.96, 'pressure': 1019, 'humidity': 75, 'dew_point': 9.25, 'uvi': 2.52, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 319, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 15.49, 'feels_like': 14.84, 'pressure': 1019, 'humidity': 67, 'dew_point': 9.4, 'uvi': 5.81, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 290, 'wind_gust': 1.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.17, 'feels_like': 16.51, 'pressure': 1018, 'humidity': 60, 'dew_point': 9.35, 'uvi': 9.59, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 284, 'wind_gust': 2.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.36, 'feels_like': 17.69, 'pressure': 1016, 'humidity': 55, 'dew_point': 9.17, 'uvi': 12.58, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 275, 'wind_gust': 3.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.63, 'feels_like': 18.98, 'pressure': 1015, 'humidity': 51, 'dew_point': 9.23, 'uvi': 13.45, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 276, 'wind_gust': 3.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 20.33, 'feels_like': 19.72, 'pressure': 1013, 'humidity': 50, 'dew_point': 9.58, 'uvi': 11.95, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 289, 'wind_gust': 4.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 19.8, 'feels_like': 19.19, 'pressure': 1012, 'humidity': 52, 'dew_point': 9.67, 'uvi': 8.57, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 295, 'wind_gust': 4.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 19, 'feels_like': 18.47, 'pressure': 1011, 'humidity': 58, 'dew_point': 10.56, 'uvi': 4.8, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 300, 'wind_gust': 3.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 17.79, 'feels_like': 17.37, 'pressure': 1011, 'humidity': 67, 'dew_point': 11.59, 'uvi': 1.85, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 293, 'wind_gust': 3.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641852000, 'temp': 16.21, 'feels_like': 15.9, 'pressure': 1013, 'humidity': 77, 'dew_point': 12.18, 'uvi': 0.34, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 288, 'wind_gust': 3.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 13.57, 'feels_like': 13.33, 'pressure': 1015, 'humidity': 90, 'dew_point': 11.96, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 269, 'wind_gust': 1.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 79.000000 | 11.970000 | 13.020000 | 92.000000 | 1016.000000 |  | 13.240000 | 0.000000 | 10000.000000 | 292.000000 | 1.44 | 1.070000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 80.000000 | 11.880000 | 12.610000 | 94.000000 | 1017.000000 |  | 12.820000 | 0.000000 | 10000.000000 | 296.000000 | 1.43 | 1.140000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 81.000000 | 11.640000 | 12.200000 | 95.000000 | 1018.000000 | 0.12 | 12.420000 | 0.000000 | 10000.000000 | 298.000000 | 1.44 | 1.070000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 10.940000 | 11.130000 | 97.000000 | 1019.000000 |  | 11.400000 | 0.000000 | 10000.000000 | 297.000000 | 1.24 | 0.930000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 84.000000 | 10.350000 | 10.480000 | 97.000000 | 1019.000000 |  | 10.810000 | 0.000000 | 10000.000000 | 285.000000 | 0.98 | 0.790000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 84.000000 | 9.980000 | 10.210000 | 96.000000 | 1019.000000 |  | 10.590000 | 0.000000 | 4936.000000 | 265.000000 | 0.91 | 0.760000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 66.000000 | 9.810000 | 10.170000 | 95.000000 | 1018.000000 |  | 10.580000 | 0.000000 | 2493.000000 | 266.000000 | 0.7 | 0.600000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 82.000000 | 9.990000 | 10.370000 | 95.000000 | 1017.000000 |  | 10.760000 | 0.000000 | 6739.000000 | 304.000000 | 0.66 | 0.460000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 83.000000 | 9.500000 | 10.280000 | 92.000000 | 1016.000000 |  | 10.750000 | 0.000000 | 10000.000000 | 307.000000 | 0.86 | 0.730000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 85.000000 | 9.460000 | 10.390000 | 91.000000 | 1016.000000 |  | 10.870000 | 0.000000 | 10000.000000 | 342.000000 | 0.91 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 9.430000 | 10.360000 | 91.000000 | 1017.000000 |  | 10.840000 | 0.000000 | 10000.000000 | 22.000000 | 1.01 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 88.000000 | 9.120000 | 10.160000 | 90.000000 | 1018.000000 |  | 10.690000 | 0.000000 | 10000.000000 | 62.000000 | 1.02 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 40.000000 | 9.360000 | 10.750000 | 88.000000 | 1019.000000 |  | 11.270000 | 0.420000 | 10000.000000 | 59.000000 | 0.92 | 0.380000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 60.000000 | 9.250000 | 12.960000 | 75.000000 | 1019.000000 |  | 13.590000 | 2.520000 | 10000.000000 | 319.000000 | 1.29 | 0.740000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 73.000000 | 9.400000 | 14.840000 | 67.000000 | 1019.000000 |  | 15.490000 | 5.810000 | 10000.000000 | 290.000000 | 1.74 | 1.070000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 77.000000 | 9.350000 | 16.510000 | 60.000000 | 1018.000000 |  | 17.170000 | 9.590000 | 10000.000000 | 284.000000 | 2.61 | 1.160000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 9.170000 | 17.690000 | 55.000000 | 1016.000000 |  | 18.360000 | 12.580000 | 10000.000000 | 275.000000 | 3.45 | 1.510000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | 9.230000 | 18.980000 | 51.000000 | 1015.000000 |  | 19.630000 | 13.450000 | 10000.000000 | 276.000000 | 3.92 | 1.970000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 91.000000 | 9.580000 | 19.720000 | 50.000000 | 1013.000000 |  | 20.330000 | 11.950000 | 10000.000000 | 289.000000 | 4.23 | 2.470000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 9.670000 | 19.190000 | 52.000000 | 1012.000000 |  | 19.800000 | 8.570000 | 10000.000000 | 295.000000 | 4.31 | 3.010000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 95.000000 | 10.560000 | 18.470000 | 58.000000 | 1011.000000 |  | 19.000000 | 4.800000 | 10000.000000 | 300.000000 | 3.8 | 2.440000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 11.590000 | 17.370000 | 67.000000 | 1011.000000 | 0.11 | 17.790000 | 1.850000 | 10000.000000 | 293.000000 | 3.43 | 2.410000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 83.000000 | 12.180000 | 15.900000 | 77.000000 | 1013.000000 |  | 16.210000 | 0.340000 | 10000.000000 | 288.000000 | 3.14 | 1.810000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035340 | "AEROPUERTO A LLERAS C [24035340]" | 5.676944 | -72.967917 | 2500.000000 | Climática Principal | Convencional | Activa | 1974-01-15 00:00:00 | NaT | Boyacá | Sogamoso | Pauto | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 86.000000 | 11.960000 | 13.330000 | 90.000000 | 1015.000000 |  | 13.570000 | 0.000000 | 10000.000000 | 269.000000 | 1.78 | 1.060000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station24035340_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035340_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035340_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035340_OWM_Windspeed_20220111.png)
