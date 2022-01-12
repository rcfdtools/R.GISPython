
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LAS BRISAS - AUT [26115090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26115090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.77558333,-76.14427778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.77558333&lon=-76.14427778)


| Parameter | Value |
|---|---|
| Code | 26115090 |
| Name | LAS BRISAS - AUT [26115090] |
| Latitude, ° | 4.77558333 |
| Longitude, ° | -76.14427778 |
| Elevation, m | 1971 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-30 00:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Argelia (Valle del cauca) |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | San Juán |
| SZH - Hydrographic subzone | Río Sipí |

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

### (CNE index 3483) Open Weather values for station 26115090 - LAS BRISAS - AUT [26115090]

JSON data from API OWM:

```
{'lat': 4.7756, 'lon': -76.1443, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813361, 'sunset': 1641856067, 'temp': 18.58, 'feels_like': 18.77, 'pressure': 1011, 'humidity': 87, 'dew_point': 16.38, 'uvi': 5.01, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 270, 'wind_gust': 2.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, 'hourly': [{'dt': 1641772800, 'temp': 18.58, 'feels_like': 19.03, 'pressure': 1013, 'humidity': 97, 'dew_point': 18.09, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 288, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641776400, 'temp': 18.58, 'feels_like': 19.03, 'pressure': 1014, 'humidity': 97, 'dew_point': 18.09, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 288, 'wind_gust': 1.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 17.58, 'feels_like': 17.93, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.1, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 279, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 17.58, 'feels_like': 17.93, 'pressure': 1016, 'humidity': 97, 'dew_point': 17.1, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 286, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 16.58, 'feels_like': 16.85, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.26, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 273, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 16.58, 'feels_like': 16.85, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.26, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 286, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 16.58, 'feels_like': 16.85, 'pressure': 1014, 'humidity': 98, 'dew_point': 16.26, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 282, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 16.58, 'feels_like': 16.85, 'pressure': 1014, 'humidity': 98, 'dew_point': 16.26, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 280, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 13.2, 'feels_like': 13.11, 'pressure': 1013, 'humidity': 97, 'dew_point': 12.73, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 256, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641805200, 'temp': 13.18, 'feels_like': 13.11, 'pressure': 1013, 'humidity': 98, 'dew_point': 12.87, 'uvi': 0, 'clouds': 91, 'visibility': 8133, 'wind_speed': 0.24, 'wind_deg': 272, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 15.58, 'feels_like': 15.75, 'pressure': 1014, 'humidity': 98, 'dew_point': 15.27, 'uvi': 0, 'clouds': 93, 'visibility': 7267, 'wind_speed': 0.26, 'wind_deg': 233, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1641812400, 'temp': 15.58, 'feels_like': 15.75, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.27, 'uvi': 0, 'clouds': 95, 'visibility': 9413, 'wind_speed': 0.22, 'wind_deg': 172, 'wind_gust': 0.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1641816000, 'temp': 16.58, 'feels_like': 16.85, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.26, 'uvi': 0.16, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 225, 'wind_gust': 0.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641819600, 'temp': 16.58, 'feels_like': 16.83, 'pressure': 1017, 'humidity': 97, 'dew_point': 16.1, 'uvi': 1.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 257, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641823200, 'temp': 18.58, 'feels_like': 19, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.93, 'uvi': 3.6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 245, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641826800, 'temp': 18.58, 'feels_like': 18.95, 'pressure': 1017, 'humidity': 94, 'dew_point': 17.6, 'uvi': 6.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 339, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641830400, 'temp': 18.58, 'feels_like': 18.77, 'pressure': 1016, 'humidity': 87, 'dew_point': 16.38, 'uvi': 9.61, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 279, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1641834000, 'temp': 18.58, 'feels_like': 18.66, 'pressure': 1014, 'humidity': 83, 'dew_point': 15.64, 'uvi': 10.72, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 267, 'wind_gust': 1.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.74}}, {'dt': 1641837600, 'temp': 18.58, 'feels_like': 18.63, 'pressure': 1013, 'humidity': 82, 'dew_point': 15.45, 'uvi': 9.98, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 266, 'wind_gust': 1.95, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.24}}, {'dt': 1641841200, 'temp': 18.58, 'feels_like': 18.74, 'pressure': 1012, 'humidity': 86, 'dew_point': 16.19, 'uvi': 8.32, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 273, 'wind_gust': 2.08, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641844800, 'temp': 18.58, 'feels_like': 18.77, 'pressure': 1011, 'humidity': 87, 'dew_point': 16.38, 'uvi': 5.01, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 270, 'wind_gust': 2.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, {'dt': 1641848400, 'temp': 19.58, 'feels_like': 19.89, 'pressure': 1011, 'humidity': 88, 'dew_point': 17.54, 'uvi': 2.16, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 269, 'wind_gust': 2.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.1}}, {'dt': 1641852000, 'temp': 16.58, 'feels_like': 16.72, 'pressure': 1012, 'humidity': 93, 'dew_point': 15.44, 'uvi': 0.44, 'clouds': 88, 'visibility': 7468, 'wind_speed': 1.35, 'wind_deg': 274, 'wind_gust': 2.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641855600, 'temp': 17.58, 'feels_like': 17.9, 'pressure': 1013, 'humidity': 96, 'dew_point': 16.94, 'uvi': 0, 'clouds': 91, 'visibility': 6890, 'wind_speed': 1.49, 'wind_deg': 278, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 00:00:00 | 85.000000 | 18.090000 | 19.030000 | 97.000000 | 1013.000000 | 0.23 | 18.580000 | 0.000000 | 10000.000000 | 288.000000 | 1.75 | 1.410000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 18.090000 | 19.030000 | 97.000000 | 1014.000000 |  | 18.580000 | 0.000000 | 10000.000000 | 288.000000 | 1.55 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 02:00:00 | 97.000000 | 17.100000 | 17.930000 | 97.000000 | 1015.000000 |  | 17.580000 | 0.000000 | 10000.000000 | 279.000000 | 1.56 | 1.230000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 03:00:00 | 93.000000 | 17.100000 | 17.930000 | 97.000000 | 1016.000000 |  | 17.580000 | 0.000000 | 10000.000000 | 286.000000 | 1.14 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 04:00:00 | 87.000000 | 16.260000 | 16.850000 | 98.000000 | 1015.000000 |  | 16.580000 | 0.000000 | 10000.000000 | 273.000000 | 1.17 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 05:00:00 | 84.000000 | 16.260000 | 16.850000 | 98.000000 | 1015.000000 |  | 16.580000 | 0.000000 | 10000.000000 | 286.000000 | 1.01 | 0.760000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 06:00:00 | 58.000000 | 16.260000 | 16.850000 | 98.000000 | 1014.000000 |  | 16.580000 | 0.000000 | 10000.000000 | 282.000000 | 0.76 | 0.540000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 07:00:00 | 77.000000 | 16.260000 | 16.850000 | 98.000000 | 1014.000000 | 0.19 | 16.580000 | 0.000000 | 10000.000000 | 280.000000 | 0.77 | 0.520000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 12.730000 | 13.110000 | 97.000000 | 1013.000000 | 0.22 | 13.200000 | 0.000000 | 10000.000000 | 256.000000 | 0.74 | 0.310000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 09:00:00 | 91.000000 | 12.870000 | 13.110000 | 98.000000 | 1013.000000 | 0.23 | 13.180000 | 0.000000 | 8133.000000 | 272.000000 | 0.65 | 0.240000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 15.270000 | 15.750000 | 98.000000 | 1014.000000 | 0.56 | 15.580000 | 0.000000 | 7267.000000 | 233.000000 | 0.6 | 0.260000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 11:00:00 | 95.000000 | 15.270000 | 15.750000 | 98.000000 | 1015.000000 | 0.47 | 15.580000 | 0.000000 | 9413.000000 | 172.000000 | 0.43 | 0.220000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 16.260000 | 16.850000 | 98.000000 | 1015.000000 | 0.36 | 16.580000 | 0.160000 | 10000.000000 | 225.000000 | 0.47 | 0.280000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.100000 | 16.830000 | 97.000000 | 1017.000000 | 0.38 | 16.580000 | 1.420000 | 10000.000000 | 257.000000 | 0.84 | 0.200000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 17.930000 | 19.000000 | 96.000000 | 1017.000000 | 0.49 | 18.580000 | 3.600000 | 10000.000000 | 245.000000 | 0.7 | 0.160000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 17.600000 | 18.950000 | 94.000000 | 1017.000000 | 0.2 | 18.580000 | 6.320000 | 10000.000000 | 339.000000 | 0.56 | 0.090000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 16:00:00 | 93.000000 | 16.380000 | 18.770000 | 87.000000 | 1016.000000 | 0.27 | 18.580000 | 9.610000 | 10000.000000 | 279.000000 | 1.11 | 0.610000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 15.640000 | 18.660000 | 83.000000 | 1014.000000 | 0.74 | 18.580000 | 10.720000 | 10000.000000 | 267.000000 | 1.8 | 1.300000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 18:00:00 | 58.000000 | 15.450000 | 18.630000 | 82.000000 | 1013.000000 | 1.24 | 18.580000 | 9.980000 | 10000.000000 | 266.000000 | 1.95 | 1.570000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 19:00:00 | 78.000000 | 16.190000 | 18.740000 | 86.000000 | 1012.000000 | 1.35 | 18.580000 | 8.320000 | 10000.000000 | 273.000000 | 2.08 | 1.710000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 20:00:00 | 77.000000 | 16.380000 | 18.770000 | 87.000000 | 1011.000000 | 1.26 | 18.580000 | 5.010000 | 10000.000000 | 270.000000 | 2.36 | 1.740000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 21:00:00 | 85.000000 | 17.540000 | 19.890000 | 88.000000 | 1011.000000 | 1.1 | 19.580000 | 2.160000 | 10000.000000 | 269.000000 | 2.18 | 1.550000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 22:00:00 | 88.000000 | 15.440000 | 16.720000 | 93.000000 | 1012.000000 | 1.01 | 16.580000 | 0.440000 | 7468.000000 | 274.000000 | 2.01 | 1.350000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26115090 | "LAS BRISAS - AUT [26115090]" | 4.775583 | -76.144278 | 1971.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Argelia (Valle del cauca) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | San Juán | Río Sipí | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 16.940000 | 17.900000 | 96.000000 | 1013.000000 | 1 | 17.580000 | 0.000000 | 6890.000000 | 278.000000 | 2.1 | 1.490000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26115090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26115090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26115090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26115090_OWM_Windspeed_20220111.png)
