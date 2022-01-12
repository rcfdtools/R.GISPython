
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - U P T C [24035130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.5430775,-73.36081306) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.5430775&lon=-73.36081306)


| Parameter | Value |
|---|---|
| Code | 24035130 |
| Name | U P T C [24035130] |
| Latitude, ° | 5.5430775 |
| Longitude, ° | -73.36081306 |
| Elevation, m | 2690 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1962-02-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Tunja |
| Stream | Meta |
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

### (CNE index 1963) Open Weather values for station 24035130 - U P T C [24035130]

JSON data from API OWM:

```
{'lat': 5.5431, 'lon': -73.3608, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812768, 'sunset': 1641855324, 'temp': 16.11, 'feels_like': 15.55, 'pressure': 1011, 'humidity': 68, 'dew_point': 10.21, 'uvi': 3.84, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 266, 'wind_gust': 2.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, 'hourly': [{'dt': 1641772800, 'temp': 11.15, 'feels_like': 10.85, 'pressure': 1016, 'humidity': 97, 'dew_point': 10.69, 'uvi': 0, 'clouds': 81, 'visibility': 4167, 'wind_speed': 0.7, 'wind_deg': 305, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641776400, 'temp': 10.94, 'feels_like': 10.62, 'pressure': 1018, 'humidity': 97, 'dew_point': 10.48, 'uvi': 0, 'clouds': 92, 'visibility': 2996, 'wind_speed': 0.64, 'wind_deg': 317, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 10.56, 'feels_like': 10.2, 'pressure': 1018, 'humidity': 97, 'dew_point': 10.1, 'uvi': 0, 'clouds': 87, 'visibility': 9624, 'wind_speed': 0.82, 'wind_deg': 307, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 10.67, 'feels_like': 10.3, 'pressure': 1018, 'humidity': 96, 'dew_point': 10.06, 'uvi': 0, 'clouds': 91, 'visibility': 9590, 'wind_speed': 0.82, 'wind_deg': 317, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10.77, 'feels_like': 10.33, 'pressure': 1018, 'humidity': 93, 'dew_point': 9.68, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 316, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.75, 'feels_like': 10.26, 'pressure': 1018, 'humidity': 91, 'dew_point': 9.34, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 230, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.68, 'feels_like': 10.13, 'pressure': 1017, 'humidity': 89, 'dew_point': 8.94, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 260, 'wind_gust': 0.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 10, 'feels_like': 10, 'pressure': 1016, 'humidity': 90, 'dew_point': 8.44, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.04, 'wind_deg': 292, 'wind_gust': 0.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.49, 'feels_like': 9.49, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.93, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 288, 'wind_gust': 0.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.29, 'feels_like': 9.29, 'pressure': 1016, 'humidity': 89, 'dew_point': 7.57, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 337, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.58, 'feels_like': 8.58, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.03, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 344, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 8.08, 'feels_like': 8.08, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.7, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 353, 'wind_gust': 0.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 9.54, 'feels_like': 9.54, 'pressure': 1019, 'humidity': 88, 'dew_point': 7.65, 'uvi': 0.57, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 330, 'wind_gust': 0.52, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 12.13, 'feels_like': 11.41, 'pressure': 1019, 'humidity': 77, 'dew_point': 8.22, 'uvi': 2.33, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 295, 'wind_gust': 0.49, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 14.51, 'feels_like': 13.74, 'pressure': 1018, 'humidity': 66, 'dew_point': 8.24, 'uvi': 5.47, 'clouds': 39, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 262, 'wind_gust': 1.1, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 16.54, 'feels_like': 15.74, 'pressure': 1017, 'humidity': 57, 'dew_point': 8, 'uvi': 9.11, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 290, 'wind_gust': 2.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 17.78, 'feels_like': 16.95, 'pressure': 1016, 'humidity': 51, 'dew_point': 7.52, 'uvi': 11.79, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 308, 'wind_gust': 3.18, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 18.65, 'feels_like': 17.85, 'pressure': 1014, 'humidity': 49, 'dew_point': 7.74, 'uvi': 12.68, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 314, 'wind_gust': 3.35, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 18.9, 'feels_like': 18.15, 'pressure': 1013, 'humidity': 50, 'dew_point': 8.26, 'uvi': 11.35, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 308, 'wind_gust': 3.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 17.54, 'feels_like': 16.84, 'pressure': 1012, 'humidity': 57, 'dew_point': 8.93, 'uvi': 6.78, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 286, 'wind_gust': 2.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 16.11, 'feels_like': 15.55, 'pressure': 1011, 'humidity': 68, 'dew_point': 10.21, 'uvi': 3.84, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 266, 'wind_gust': 2.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641848400, 'temp': 14.71, 'feels_like': 14.27, 'pressure': 1012, 'humidity': 78, 'dew_point': 10.92, 'uvi': 1.5, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 271, 'wind_gust': 2.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641852000, 'temp': 13.53, 'feels_like': 13.16, 'pressure': 1014, 'humidity': 85, 'dew_point': 11.06, 'uvi': 0.36, 'clouds': 86, 'visibility': 7941, 'wind_speed': 0.66, 'wind_deg': 274, 'wind_gust': 1.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641855600, 'temp': 11.69, 'feels_like': 11.4, 'pressure': 1015, 'humidity': 95, 'dew_point': 10.92, 'uvi': 0, 'clouds': 85, 'visibility': 6156, 'wind_speed': 0.65, 'wind_deg': 272, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 81.000000 | 10.690000 | 10.850000 | 97.000000 | 1016.000000 | 0.12 | 11.150000 | 0.000000 | 4167.000000 | 305.000000 | 1.21 | 0.700000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 92.000000 | 10.480000 | 10.620000 | 97.000000 | 1018.000000 |  | 10.940000 | 0.000000 | 2996.000000 | 317.000000 | 1.1 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 87.000000 | 10.100000 | 10.200000 | 97.000000 | 1018.000000 |  | 10.560000 | 0.000000 | 9624.000000 | 307.000000 | 1.24 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 91.000000 | 10.060000 | 10.300000 | 96.000000 | 1018.000000 |  | 10.670000 | 0.000000 | 9590.000000 | 317.000000 | 1.09 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 92.000000 | 9.680000 | 10.330000 | 93.000000 | 1018.000000 |  | 10.770000 | 0.000000 | 10000.000000 | 316.000000 | 0.95 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 92.000000 | 9.340000 | 10.260000 | 91.000000 | 1018.000000 |  | 10.750000 | 0.000000 | 10000.000000 | 230.000000 | 0.73 | 0.290000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 74.000000 | 8.940000 | 10.130000 | 89.000000 | 1017.000000 |  | 10.680000 | 0.000000 | 10000.000000 | 260.000000 | 0.59 | 0.140000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 87.000000 | 8.440000 | 10.000000 | 90.000000 | 1016.000000 |  | 10.000000 | 0.000000 | 10000.000000 | 292.000000 | 0.53 | 0.040000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 85.000000 | 7.930000 | 9.490000 | 90.000000 | 1016.000000 |  | 9.490000 | 0.000000 | 10000.000000 | 288.000000 | 0.72 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 82.000000 | 7.570000 | 9.290000 | 89.000000 | 1016.000000 |  | 9.290000 | 0.000000 | 10000.000000 | 337.000000 | 0.84 | 0.600000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 79.000000 | 7.030000 | 8.580000 | 90.000000 | 1017.000000 |  | 8.580000 | 0.000000 | 10000.000000 | 344.000000 | 0.83 | 0.630000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 6.700000 | 8.080000 | 91.000000 | 1018.000000 |  | 8.080000 | 0.000000 | 10000.000000 | 353.000000 | 0.69 | 0.400000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 29.000000 | 7.650000 | 9.540000 | 88.000000 | 1019.000000 |  | 9.540000 | 0.570000 | 10000.000000 | 330.000000 | 0.52 | 0.240000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 41.000000 | 8.220000 | 11.410000 | 77.000000 | 1019.000000 |  | 12.130000 | 2.330000 | 10000.000000 | 295.000000 | 0.49 | 0.340000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 39.000000 | 8.240000 | 13.740000 | 66.000000 | 1018.000000 |  | 14.510000 | 5.470000 | 10000.000000 | 262.000000 | 1.1 | 0.720000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 36.000000 | 8.000000 | 15.740000 | 57.000000 | 1017.000000 |  | 16.540000 | 9.110000 | 10000.000000 | 290.000000 | 2.37 | 1.250000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 7.520000 | 16.950000 | 51.000000 | 1016.000000 |  | 17.780000 | 11.790000 | 10000.000000 | 308.000000 | 3.18 | 1.760000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 46.000000 | 7.740000 | 17.850000 | 49.000000 | 1014.000000 |  | 18.650000 | 12.680000 | 10000.000000 | 314.000000 | 3.35 | 1.960000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 66.000000 | 8.260000 | 18.150000 | 50.000000 | 1013.000000 |  | 18.900000 | 11.350000 | 10000.000000 | 308.000000 | 3.19 | 1.800000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 76.000000 | 8.930000 | 16.840000 | 57.000000 | 1012.000000 |  | 17.540000 | 6.780000 | 10000.000000 | 286.000000 | 2.4 | 1.320000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 86.000000 | 10.210000 | 15.550000 | 68.000000 | 1011.000000 | 0.16 | 16.110000 | 3.840000 | 10000.000000 | 266.000000 | 2.51 | 1.210000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 87.000000 | 10.920000 | 14.270000 | 78.000000 | 1012.000000 | 0.54 | 14.710000 | 1.500000 | 10000.000000 | 271.000000 | 2.31 | 1.040000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 86.000000 | 11.060000 | 13.160000 | 85.000000 | 1014.000000 | 0.46 | 13.530000 | 0.360000 | 7941.000000 | 274.000000 | 1.96 | 0.660000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035130 | "U P T C [24035130]" | 5.543077 | -73.360813 | 2690.000000 | Climática Principal | Convencional | Activa | 1962-02-15 00:00:00 | NaT | Boyacá | Tunja | Meta | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 10.920000 | 11.400000 | 95.000000 | 1015.000000 | 0.28 | 11.690000 | 0.000000 | 6156.000000 | 272.000000 | 1.6 | 0.650000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24035130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035130_OWM_Windspeed_20220111.png)
