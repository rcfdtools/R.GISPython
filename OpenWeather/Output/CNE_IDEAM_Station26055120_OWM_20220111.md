
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNIVERSIDAD DEL VALLE  - AUT [26055120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26055120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.378,-76.53388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.378&lon=-76.53388889)


| Parameter | Value |
|---|---|
| Code | 26055120 |
| Name | UNIVERSIDAD DEL VALLE  - AUT [26055120] |
| Latitude, ° | 3.378 |
| Longitude, ° | -76.53388889 |
| Elevation, m | 996 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-11-25 19:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Cali |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Lilí, Melendez y Canaveralejo |

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

### (CNE index 69) Open Weather values for station 26055120 - UNIVERSIDAD DEL VALLE  - AUT [26055120]

JSON data from API OWM:

```
{'lat': 3.378, 'lon': -76.5339, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813319, 'sunset': 1641856296, 'temp': 27.93, 'feels_like': 31.34, 'pressure': 1011, 'humidity': 76, 'dew_point': 23.31, 'uvi': 3.72, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 295, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.55}}, 'hourly': [{'dt': 1641772800, 'temp': 24.93, 'feels_like': 25.8, 'pressure': 1012, 'humidity': 89, 'dew_point': 22.99, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 286, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.88}}, {'dt': 1641776400, 'temp': 22.93, 'feels_like': 23.63, 'pressure': 1014, 'humidity': 90, 'dew_point': 21.2, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 274, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.85}}, {'dt': 1641780000, 'temp': 22.93, 'feels_like': 23.65, 'pressure': 1015, 'humidity': 91, 'dew_point': 21.38, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 234, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.67}}, {'dt': 1641783600, 'temp': 22.93, 'feels_like': 23.68, 'pressure': 1015, 'humidity': 92, 'dew_point': 21.56, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 256, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641787200, 'temp': 22.93, 'feels_like': 23.71, 'pressure': 1015, 'humidity': 93, 'dew_point': 21.74, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 235, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641790800, 'temp': 21.93, 'feels_like': 22.61, 'pressure': 1015, 'humidity': 93, 'dew_point': 20.75, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 232, 'wind_gust': 0.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641794400, 'temp': 21.93, 'feels_like': 22.61, 'pressure': 1014, 'humidity': 93, 'dew_point': 20.75, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 265, 'wind_gust': 0.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.93, 'feels_like': 21.51, 'pressure': 1013, 'humidity': 93, 'dew_point': 19.76, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 242, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641801600, 'temp': 20.93, 'feels_like': 21.53, 'pressure': 1013, 'humidity': 94, 'dew_point': 19.93, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 132, 'wind_gust': 0.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641805200, 'temp': 20.93, 'feels_like': 21.56, 'pressure': 1013, 'humidity': 95, 'dew_point': 20.1, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 163, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641808800, 'temp': 19.93, 'feels_like': 20.46, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.11, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 354, 'wind_gust': 0.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641812400, 'temp': 19.93, 'feels_like': 20.46, 'pressure': 1015, 'humidity': 95, 'dew_point': 19.11, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 304, 'wind_gust': 0.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 20.93, 'feels_like': 21.53, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.93, 'uvi': 0.37, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.06, 'wind_deg': 52, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641819600, 'temp': 21.93, 'feels_like': 22.58, 'pressure': 1016, 'humidity': 92, 'dew_point': 20.57, 'uvi': 1.66, 'clouds': 100, 'visibility': 9794, 'wind_speed': 0.27, 'wind_deg': 58, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641823200, 'temp': 22.93, 'feels_like': 23.58, 'pressure': 1016, 'humidity': 88, 'dew_point': 20.84, 'uvi': 4.22, 'clouds': 76, 'visibility': 9417, 'wind_speed': 0.66, 'wind_deg': 36, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.74}}, {'dt': 1641826800, 'temp': 24.93, 'feels_like': 25.67, 'pressure': 1016, 'humidity': 84, 'dew_point': 22.04, 'uvi': 7.42, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 34, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641830400, 'temp': 25.93, 'feels_like': 26.62, 'pressure': 1015, 'humidity': 78, 'dew_point': 21.8, 'uvi': 8.93, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 20, 'wind_gust': 1.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641834000, 'temp': 26.93, 'feels_like': 29.15, 'pressure': 1014, 'humidity': 75, 'dew_point': 22.12, 'uvi': 10.02, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 7, 'wind_gust': 1.2, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.17}}, {'dt': 1641837600, 'temp': 26.93, 'feels_like': 29.06, 'pressure': 1013, 'humidity': 74, 'dew_point': 21.9, 'uvi': 9.37, 'clouds': 48, 'visibility': 4767, 'wind_speed': 0.66, 'wind_deg': 299, 'wind_gust': 1.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.31}}, {'dt': 1641841200, 'temp': 27.93, 'feels_like': 31.06, 'pressure': 1011, 'humidity': 74, 'dew_point': 22.86, 'uvi': 6.08, 'clouds': 68, 'visibility': 6368, 'wind_speed': 1.22, 'wind_deg': 286, 'wind_gust': 1.74, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, {'dt': 1641844800, 'temp': 27.93, 'feels_like': 31.34, 'pressure': 1011, 'humidity': 76, 'dew_point': 23.31, 'uvi': 3.72, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 295, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.55}}, {'dt': 1641848400, 'temp': 23.93, 'feels_like': 24.49, 'pressure': 1010, 'humidity': 81, 'dew_point': 20.47, 'uvi': 1.65, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 302, 'wind_gust': 1.61, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.76}}, {'dt': 1641852000, 'temp': 21.93, 'feels_like': 22.4, 'pressure': 1011, 'humidity': 85, 'dew_point': 19.29, 'uvi': 0.37, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 318, 'wind_gust': 1.23, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.38}}, {'dt': 1641855600, 'temp': 19.93, 'feels_like': 20.3, 'pressure': 1012, 'humidity': 89, 'dew_point': 18.06, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 305, 'wind_gust': 1.41, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 22.990000 | 25.800000 | 89.000000 | 1012.000000 | 0.88 | 24.930000 | 0.000000 | 10000.000000 | 286.000000 | 2.26 | 1.250000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 01:00:00 | 60.000000 | 21.200000 | 23.630000 | 90.000000 | 1014.000000 | 0.85 | 22.930000 | 0.000000 | 10000.000000 | 274.000000 | 1.94 | 1.170000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 02:00:00 | 59.000000 | 21.380000 | 23.650000 | 91.000000 | 1015.000000 | 0.67 | 22.930000 | 0.000000 | 10000.000000 | 234.000000 | 1.17 | 0.690000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 03:00:00 | 60.000000 | 21.560000 | 23.680000 | 92.000000 | 1015.000000 | 0.35 | 22.930000 | 0.000000 | 10000.000000 | 256.000000 | 0.7 | 0.540000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 04:00:00 | 68.000000 | 21.740000 | 23.710000 | 93.000000 | 1015.000000 | 0.33 | 22.930000 | 0.000000 | 10000.000000 | 235.000000 | 0.66 | 0.520000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 05:00:00 | 72.000000 | 20.750000 | 22.610000 | 93.000000 | 1015.000000 | 0.11 | 21.930000 | 0.000000 | 10000.000000 | 232.000000 | 0.48 | 0.300000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 06:00:00 | 67.000000 | 20.750000 | 22.610000 | 93.000000 | 1014.000000 |  | 21.930000 | 0.000000 | 10000.000000 | 265.000000 | 0.54 | 0.430000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 19.760000 | 21.510000 | 93.000000 | 1013.000000 | 0.17 | 20.930000 | 0.000000 | 10000.000000 | 242.000000 | 0.63 | 0.190000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 19.930000 | 21.530000 | 94.000000 | 1013.000000 | 0.17 | 20.930000 | 0.000000 | 10000.000000 | 132.000000 | 0.78 | 0.110000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 20.100000 | 21.560000 | 95.000000 | 1013.000000 | 0.27 | 20.930000 | 0.000000 | 10000.000000 | 163.000000 | 0.54 | 0.070000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 19.110000 | 20.460000 | 95.000000 | 1014.000000 | 0.2 | 19.930000 | 0.000000 | 10000.000000 | 354.000000 | 0.4 | 0.120000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 19.110000 | 20.460000 | 95.000000 | 1015.000000 |  | 19.930000 | 0.000000 | 10000.000000 | 304.000000 | 0.41 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 19.930000 | 21.530000 | 94.000000 | 1015.000000 | 0.12 | 20.930000 | 0.370000 | 10000.000000 | 52.000000 | 0.59 | 0.060000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 20.570000 | 22.580000 | 92.000000 | 1016.000000 | 0.46 | 21.930000 | 1.660000 | 9794.000000 | 58.000000 | 0.96 | 0.270000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 14:00:00 | 76.000000 | 20.840000 | 23.580000 | 88.000000 | 1016.000000 | 0.74 | 22.930000 | 4.220000 | 9417.000000 | 36.000000 | 1.2 | 0.660000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 15:00:00 | 71.000000 | 22.040000 | 25.670000 | 84.000000 | 1016.000000 | 0.72 | 24.930000 | 7.420000 | 10000.000000 | 34.000000 | 1.23 | 0.780000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 21.800000 | 26.620000 | 78.000000 | 1015.000000 | 1.15 | 25.930000 | 8.930000 | 10000.000000 | 20.000000 | 1.05 | 0.590000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 17:00:00 | 82.000000 | 22.120000 | 29.150000 | 75.000000 | 1014.000000 | 1.17 | 26.930000 | 10.020000 | 10000.000000 | 7.000000 | 1.2 | 0.470000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 18:00:00 | 48.000000 | 21.900000 | 29.060000 | 74.000000 | 1013.000000 | 1.31 | 26.930000 | 9.370000 | 4767.000000 | 299.000000 | 1.32 | 0.660000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 19:00:00 | 68.000000 | 22.860000 | 31.060000 | 74.000000 | 1011.000000 | 1.44 | 27.930000 | 6.080000 | 6368.000000 | 286.000000 | 1.74 | 1.220000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 20:00:00 | 84.000000 | 23.310000 | 31.340000 | 76.000000 | 1011.000000 | 1.55 | 27.930000 | 3.720000 | 10000.000000 | 295.000000 | 1.6 | 1.020000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 20.470000 | 24.490000 | 81.000000 | 1010.000000 | 1.76 | 23.930000 | 1.650000 | 10000.000000 | 302.000000 | 1.61 | 1.080000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 22:00:00 | 92.000000 | 19.290000 | 22.400000 | 85.000000 | 1011.000000 | 1.38 | 21.930000 | 0.370000 | 10000.000000 | 318.000000 | 1.23 | 0.750000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055120 | "UNIVERSIDAD DEL VALLE  - AUT [26055120]" | 3.378000 | -76.533889 | 996.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-25 19:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 18.060000 | 20.300000 | 89.000000 | 1012.000000 | 1.22 | 19.930000 | 0.000000 | 10000.000000 | 305.000000 | 1.41 | 1.010000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26055120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26055120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26055120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055120_OWM_Windspeed_20220111.png)
