
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL PARAMO - AUT [24030680] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24030680_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.65333333,-72.59083333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.65333333&lon=-72.59083333)


| Parameter | Value |
|---|---|
| Code | 24030680 |
| Name | EL PARAMO - AUT [24030680] |
| Latitude, ° | 6.65333333 |
| Longitude, ° | -72.59083333 |
| Elevation, m | 2394 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1974-06-14 19:00:00 |
| Suspension date | NaT |
| State | Santander |
| County | Carcasí |
| Stream | 0 |
| Operator | Area Operativa 08 - Santanderes-Arauca |
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

### (CNE index 3564) Open Weather values for station 24030680 - EL PARAMO - AUT [24030680]

JSON data from API OWM:

```
{'lat': 6.6533, 'lon': -72.5908, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812691, 'sunset': 1641855032, 'temp': 18, 'feels_like': 17.55, 'pressure': 1013, 'humidity': 65, 'dew_point': 11.33, 'uvi': 3.69, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 276, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 13.18, 'feels_like': 13.09, 'pressure': 1017, 'humidity': 97, 'dew_point': 12.71, 'uvi': 0, 'clouds': 62, 'visibility': 5394, 'wind_speed': 0.66, 'wind_deg': 344, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641776400, 'temp': 12.89, 'feels_like': 12.77, 'pressure': 1018, 'humidity': 97, 'dew_point': 12.43, 'uvi': 0, 'clouds': 72, 'visibility': 7713, 'wind_speed': 0.38, 'wind_deg': 349, 'wind_gust': 1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.66, 'feels_like': 12.46, 'pressure': 1019, 'humidity': 95, 'dew_point': 11.88, 'uvi': 0, 'clouds': 73, 'visibility': 9479, 'wind_speed': 0.08, 'wind_deg': 318, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.26, 'feels_like': 12.02, 'pressure': 1019, 'humidity': 95, 'dew_point': 11.48, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 150, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 12.05, 'feels_like': 11.74, 'pressure': 1019, 'humidity': 93, 'dew_point': 10.95, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 88, 'wind_gust': 0.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 11.73, 'feels_like': 11.39, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.64, 'uvi': 0, 'clouds': 86, 'visibility': 9504, 'wind_speed': 0.2, 'wind_deg': 103, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.73, 'feels_like': 10.34, 'pressure': 1018, 'humidity': 95, 'dew_point': 9.96, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 105, 'wind_gust': 0.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 11.13, 'feels_like': 10.75, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.2, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 164, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 11.29, 'feels_like': 10.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.2, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 224, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.25, 'feels_like': 10.88, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.32, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 218, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 11.27, 'feels_like': 10.88, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.18, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 225, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 11.16, 'feels_like': 10.76, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.07, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 214, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 11.78, 'feels_like': 11.39, 'pressure': 1019, 'humidity': 91, 'dew_point': 10.36, 'uvi': 0.35, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 253, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 13.11, 'feels_like': 12.72, 'pressure': 1020, 'humidity': 86, 'dew_point': 10.82, 'uvi': 1.59, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 256, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 14.46, 'feels_like': 14.05, 'pressure': 1020, 'humidity': 80, 'dew_point': 11.06, 'uvi': 3.7, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 251, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 16.11, 'feels_like': 15.63, 'pressure': 1019, 'humidity': 71, 'dew_point': 10.86, 'uvi': 6.13, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 254, 'wind_gust': 1.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 17.5, 'feels_like': 17, 'pressure': 1018, 'humidity': 65, 'dew_point': 10.86, 'uvi': 9.67, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 259, 'wind_gust': 2.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 17.99, 'feels_like': 17.49, 'pressure': 1016, 'humidity': 63, 'dew_point': 10.85, 'uvi': 10.35, 'clouds': 83, 'visibility': 10000, 'wind_speed': 2.43, 'wind_deg': 262, 'wind_gust': 2.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 18.04, 'feels_like': 17.6, 'pressure': 1015, 'humidity': 65, 'dew_point': 11.37, 'uvi': 9.2, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.33, 'wind_deg': 265, 'wind_gust': 2.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 18.52, 'feels_like': 18.05, 'pressure': 1014, 'humidity': 62, 'dew_point': 11.11, 'uvi': 6.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.13, 'wind_deg': 269, 'wind_gust': 2.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 18, 'feels_like': 17.55, 'pressure': 1013, 'humidity': 65, 'dew_point': 11.33, 'uvi': 3.69, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 276, 'wind_gust': 2.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 16.73, 'feels_like': 16.34, 'pressure': 1013, 'humidity': 72, 'dew_point': 11.66, 'uvi': 1.41, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 279, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 15.43, 'feels_like': 15.17, 'pressure': 1014, 'humidity': 82, 'dew_point': 12.38, 'uvi': 0.19, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 277, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641855600, 'temp': 13.41, 'feels_like': 13.23, 'pressure': 1016, 'humidity': 93, 'dew_point': 12.3, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 281, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 62.000000 | 12.710000 | 13.090000 | 97.000000 | 1017.000000 | 0.16 | 13.180000 | 0.000000 | 5394.000000 | 344.000000 | 1.12 | 0.660000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 72.000000 | 12.430000 | 12.770000 | 97.000000 | 1018.000000 |  | 12.890000 | 0.000000 | 7713.000000 | 349.000000 | 1 | 0.380000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 11.880000 | 12.460000 | 95.000000 | 1019.000000 |  | 12.660000 | 0.000000 | 9479.000000 | 318.000000 | 0.75 | 0.080000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 79.000000 | 11.480000 | 12.020000 | 95.000000 | 1019.000000 |  | 12.260000 | 0.000000 | 10000.000000 | 150.000000 | 0.74 | 0.150000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 84.000000 | 10.950000 | 11.740000 | 93.000000 | 1019.000000 |  | 12.050000 | 0.000000 | 10000.000000 | 88.000000 | 0.88 | 0.350000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 86.000000 | 10.640000 | 11.390000 | 93.000000 | 1018.000000 |  | 11.730000 | 0.000000 | 9504.000000 | 103.000000 | 0.63 | 0.200000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 63.000000 | 9.960000 | 10.340000 | 95.000000 | 1018.000000 |  | 10.730000 | 0.000000 | 10000.000000 | 105.000000 | 0.67 | 0.230000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 76.000000 | 10.200000 | 10.750000 | 94.000000 | 1017.000000 |  | 11.130000 | 0.000000 | 10000.000000 | 164.000000 | 0.73 | 0.240000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 79.000000 | 10.200000 | 10.900000 | 93.000000 | 1017.000000 |  | 11.290000 | 0.000000 | 10000.000000 | 224.000000 | 0.83 | 0.440000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 84.000000 | 10.320000 | 10.880000 | 94.000000 | 1017.000000 |  | 11.250000 | 0.000000 | 10000.000000 | 218.000000 | 1.09 | 0.570000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 88.000000 | 10.180000 | 10.880000 | 93.000000 | 1017.000000 |  | 11.270000 | 0.000000 | 10000.000000 | 225.000000 | 1.07 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 89.000000 | 10.070000 | 10.760000 | 93.000000 | 1018.000000 |  | 11.160000 | 0.000000 | 10000.000000 | 214.000000 | 1.03 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 70.000000 | 10.360000 | 11.390000 | 91.000000 | 1019.000000 |  | 11.780000 | 0.350000 | 10000.000000 | 253.000000 | 1.05 | 0.350000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 82.000000 | 10.820000 | 12.720000 | 86.000000 | 1020.000000 |  | 13.110000 | 1.590000 | 10000.000000 | 256.000000 | 0.87 | 0.800000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 91.000000 | 11.060000 | 14.050000 | 80.000000 | 1020.000000 |  | 14.460000 | 3.700000 | 10000.000000 | 251.000000 | 0.95 | 1.050000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 87.000000 | 10.860000 | 15.630000 | 71.000000 | 1019.000000 |  | 16.110000 | 6.130000 | 10000.000000 | 254.000000 | 1.53 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 86.000000 | 10.860000 | 17.000000 | 65.000000 | 1018.000000 |  | 17.500000 | 9.670000 | 10000.000000 | 259.000000 | 2.12 | 2.350000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 83.000000 | 10.850000 | 17.490000 | 63.000000 | 1016.000000 |  | 17.990000 | 10.350000 | 10000.000000 | 262.000000 | 2.31 | 2.430000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 96.000000 | 11.370000 | 17.600000 | 65.000000 | 1015.000000 |  | 18.040000 | 9.200000 | 10000.000000 | 265.000000 | 2.36 | 2.330000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 11.110000 | 18.050000 | 62.000000 | 1014.000000 |  | 18.520000 | 6.610000 | 10000.000000 | 269.000000 | 2.26 | 2.130000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 11.330000 | 17.550000 | 65.000000 | 1013.000000 |  | 18.000000 | 3.690000 | 10000.000000 | 276.000000 | 2.29 | 2.140000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 11.660000 | 16.340000 | 72.000000 | 1013.000000 |  | 16.730000 | 1.410000 | 10000.000000 | 279.000000 | 2.1 | 1.910000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 12.380000 | 15.170000 | 82.000000 | 1014.000000 | 0.14 | 15.430000 | 0.190000 | 10000.000000 | 277.000000 | 1.89 | 1.550000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24030680 | "EL PARAMO - AUT [24030680]" | 6.653333 | -72.590833 | 2394.000000 | Climática Principal | Automática con Telemetría | Activa | 1974-06-14 19:00:00 | NaT | Santander | Carcasí | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 12.300000 | 13.230000 | 93.000000 | 1016.000000 |  | 13.410000 | 0.000000 | 10000.000000 | 281.000000 | 1.24 | 0.980000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station24030680_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24030680_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24030680_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24030680_OWM_Windspeed_20220111.png)
