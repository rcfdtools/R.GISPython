
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26085170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.36041667,-76.29972222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.36041667&lon=-76.29972222)


| Parameter | Value |
|---|---|
| Code | 26085170 |
| Name | BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170] |
| Latitude, ° | 3.36041667 |
| Longitude, ° | -76.29972222 |
| Elevation, m | 975 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-11-23 00:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Florida |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Guachal (Bolo - Fraile y Párraga) |

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

### (CNE index 2929) Open Weather values for station 26085170 - BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]

JSON data from API OWM:

```
{'lat': 3.3604, 'lon': -76.2997, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813262, 'sunset': 1641856242, 'temp': 27.74, 'feels_like': 30.92, 'pressure': 1012, 'humidity': 76, 'dew_point': 23.12, 'uvi': 4.75, 'clouds': 81, 'visibility': 6021, 'wind_speed': 1.11, 'wind_deg': 294, 'wind_gust': 1.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, 'hourly': [{'dt': 1641772800, 'temp': 24.74, 'feels_like': 25.67, 'pressure': 1013, 'humidity': 92, 'dew_point': 23.35, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 97, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.18}}, {'dt': 1641776400, 'temp': 22.74, 'feels_like': 23.5, 'pressure': 1015, 'humidity': 93, 'dew_point': 21.55, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 101, 'wind_gust': 1.5, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.23}}, {'dt': 1641780000, 'temp': 22.74, 'feels_like': 23.5, 'pressure': 1016, 'humidity': 93, 'dew_point': 21.55, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 113, 'wind_gust': 1.16, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.02}}, {'dt': 1641783600, 'temp': 22.74, 'feels_like': 23.52, 'pressure': 1016, 'humidity': 94, 'dew_point': 21.72, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 108, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.6}}, {'dt': 1641787200, 'temp': 22.74, 'feels_like': 23.55, 'pressure': 1016, 'humidity': 95, 'dew_point': 21.9, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 145, 'wind_gust': 0.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.52}}, {'dt': 1641790800, 'temp': 21.74, 'feels_like': 22.45, 'pressure': 1016, 'humidity': 95, 'dew_point': 20.9, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 126, 'wind_gust': 0.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641794400, 'temp': 21.74, 'feels_like': 22.5, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.24, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 285, 'wind_gust': 0.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641798000, 'temp': 20.74, 'feels_like': 21.4, 'pressure': 1015, 'humidity': 97, 'dew_point': 20.25, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 86, 'wind_gust': 0.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641801600, 'temp': 20.74, 'feels_like': 21.4, 'pressure': 1014, 'humidity': 97, 'dew_point': 20.25, 'uvi': 0, 'clouds': 94, 'visibility': 9069, 'wind_speed': 0.21, 'wind_deg': 101, 'wind_gust': 0.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641805200, 'temp': 20.74, 'feels_like': 21.43, 'pressure': 1014, 'humidity': 98, 'dew_point': 20.41, 'uvi': 0, 'clouds': 96, 'visibility': 7044, 'wind_speed': 0.07, 'wind_deg': 294, 'wind_gust': 0.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.46}}, {'dt': 1641808800, 'temp': 19.74, 'feels_like': 20.33, 'pressure': 1015, 'humidity': 98, 'dew_point': 19.41, 'uvi': 0, 'clouds': 96, 'visibility': 7218, 'wind_speed': 0.25, 'wind_deg': 60, 'wind_gust': 0.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641812400, 'temp': 19.74, 'feels_like': 20.3, 'pressure': 1016, 'humidity': 97, 'dew_point': 19.25, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.03, 'wind_deg': 16, 'wind_gust': 0.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641816000, 'temp': 20.74, 'feels_like': 21.38, 'pressure': 1016, 'humidity': 96, 'dew_point': 20.08, 'uvi': 0.32, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 82, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641819600, 'temp': 21.74, 'feels_like': 22.37, 'pressure': 1017, 'humidity': 92, 'dew_point': 20.38, 'uvi': 1.34, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 8, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641823200, 'temp': 22.74, 'feels_like': 23.32, 'pressure': 1017, 'humidity': 86, 'dew_point': 20.28, 'uvi': 3.39, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 332, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641826800, 'temp': 24.74, 'feels_like': 25.41, 'pressure': 1017, 'humidity': 82, 'dew_point': 21.46, 'uvi': 5.91, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 309, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641830400, 'temp': 25.74, 'feels_like': 26.33, 'pressure': 1016, 'humidity': 75, 'dew_point': 20.97, 'uvi': 11.68, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 294, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641834000, 'temp': 26.74, 'feels_like': 28.43, 'pressure': 1014, 'humidity': 70, 'dew_point': 20.81, 'uvi': 13.02, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 289, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641837600, 'temp': 26.74, 'feels_like': 28.29, 'pressure': 1013, 'humidity': 68, 'dew_point': 20.34, 'uvi': 12.1, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 279, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641841200, 'temp': 27.74, 'feels_like': 30.41, 'pressure': 1012, 'humidity': 72, 'dew_point': 22.23, 'uvi': 7.84, 'clouds': 78, 'visibility': 5824, 'wind_speed': 1.45, 'wind_deg': 283, 'wind_gust': 1.28, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.05}}, {'dt': 1641844800, 'temp': 27.74, 'feels_like': 30.92, 'pressure': 1012, 'humidity': 76, 'dew_point': 23.12, 'uvi': 4.75, 'clouds': 81, 'visibility': 6021, 'wind_speed': 1.11, 'wind_deg': 294, 'wind_gust': 1.05, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641848400, 'temp': 23.74, 'feels_like': 24.26, 'pressure': 1011, 'humidity': 80, 'dew_point': 20.08, 'uvi': 2.08, 'clouds': 87, 'visibility': 7858, 'wind_speed': 1.03, 'wind_deg': 311, 'wind_gust': 1.04, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.32}}, {'dt': 1641852000, 'temp': 21.74, 'feels_like': 22.24, 'pressure': 1012, 'humidity': 87, 'dew_point': 19.48, 'uvi': 0.5, 'clouds': 90, 'visibility': 6974, 'wind_speed': 0.84, 'wind_deg': 313, 'wind_gust': 1.31, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.28}}, {'dt': 1641855600, 'temp': 19.74, 'feels_like': 20.15, 'pressure': 1013, 'humidity': 91, 'dew_point': 18.23, 'uvi': 0, 'clouds': 92, 'visibility': 6940, 'wind_speed': 0.7, 'wind_deg': 53, 'wind_gust': 0.9, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 00:00:00 | 46.000000 | 23.350000 | 25.670000 | 92.000000 | 1013.000000 | 1.18 | 24.740000 | 0.000000 | 10000.000000 | 97.000000 | 1.49 | 0.780000 | 501 | Rain | moderate rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 01:00:00 | 67.000000 | 21.550000 | 23.500000 | 93.000000 | 1015.000000 | 1.23 | 22.740000 | 0.000000 | 10000.000000 | 101.000000 | 1.5 | 1.000000 | 501 | Rain | moderate rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 21.550000 | 23.500000 | 93.000000 | 1016.000000 | 1.02 | 22.740000 | 0.000000 | 10000.000000 | 113.000000 | 1.16 | 0.960000 | 501 | Rain | moderate rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 03:00:00 | 76.000000 | 21.720000 | 23.520000 | 94.000000 | 1016.000000 | 0.6 | 22.740000 | 0.000000 | 10000.000000 | 108.000000 | 0.62 | 0.460000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 21.900000 | 23.550000 | 95.000000 | 1016.000000 | 0.52 | 22.740000 | 0.000000 | 10000.000000 | 145.000000 | 0.5 | 0.310000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 05:00:00 | 85.000000 | 20.900000 | 22.450000 | 95.000000 | 1016.000000 | 0.32 | 21.740000 | 0.000000 | 10000.000000 | 126.000000 | 0.39 | 0.260000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 06:00:00 | 55.000000 | 21.240000 | 22.500000 | 97.000000 | 1015.000000 | 0.18 | 21.740000 | 0.000000 | 10000.000000 | 285.000000 | 0.34 | 0.090000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 07:00:00 | 88.000000 | 20.250000 | 21.400000 | 97.000000 | 1015.000000 | 0.23 | 20.740000 | 0.000000 | 10000.000000 | 86.000000 | 0.38 | 0.200000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 20.250000 | 21.400000 | 97.000000 | 1014.000000 | 0.42 | 20.740000 | 0.000000 | 9069.000000 | 101.000000 | 0.44 | 0.210000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 09:00:00 | 96.000000 | 20.410000 | 21.430000 | 98.000000 | 1014.000000 | 0.46 | 20.740000 | 0.000000 | 7044.000000 | 294.000000 | 0.38 | 0.070000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 10:00:00 | 96.000000 | 19.410000 | 20.330000 | 98.000000 | 1015.000000 | 0.49 | 19.740000 | 0.000000 | 7218.000000 | 60.000000 | 0.36 | 0.250000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 11:00:00 | 97.000000 | 19.250000 | 20.300000 | 97.000000 | 1016.000000 | 0.39 | 19.740000 | 0.000000 | 10000.000000 | 16.000000 | 0.35 | 0.030000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 20.080000 | 21.380000 | 96.000000 | 1016.000000 | 0.29 | 20.740000 | 0.320000 | 10000.000000 | 82.000000 | 0.56 | 0.270000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 20.380000 | 22.370000 | 92.000000 | 1017.000000 | 0.43 | 21.740000 | 1.340000 | 10000.000000 | 8.000000 | 0.68 | 0.120000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 14:00:00 | 95.000000 | 20.280000 | 23.320000 | 86.000000 | 1017.000000 | 0.58 | 22.740000 | 3.390000 | 10000.000000 | 332.000000 | 0.9 | 0.760000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 15:00:00 | 94.000000 | 21.460000 | 25.410000 | 82.000000 | 1017.000000 | 0.63 | 24.740000 | 5.910000 | 10000.000000 | 309.000000 | 1.08 | 1.230000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 16:00:00 | 95.000000 | 20.970000 | 26.330000 | 75.000000 | 1016.000000 | 0.5 | 25.740000 | 11.680000 | 10000.000000 | 294.000000 | 0.97 | 1.390000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 17:00:00 | 96.000000 | 20.810000 | 28.430000 | 70.000000 | 1014.000000 | 0.55 | 26.740000 | 13.020000 | 10000.000000 | 289.000000 | 1.25 | 1.460000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 18:00:00 | 77.000000 | 20.340000 | 28.290000 | 68.000000 | 1013.000000 | 0.88 | 26.740000 | 12.100000 | 10000.000000 | 279.000000 | 1.24 | 1.550000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 19:00:00 | 78.000000 | 22.230000 | 30.410000 | 72.000000 | 1012.000000 | 1.05 | 27.740000 | 7.840000 | 5824.000000 | 283.000000 | 1.28 | 1.450000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 20:00:00 | 81.000000 | 23.120000 | 30.920000 | 76.000000 | 1012.000000 | 1.23 | 27.740000 | 4.750000 | 6021.000000 | 294.000000 | 1.05 | 1.110000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 21:00:00 | 87.000000 | 20.080000 | 24.260000 | 80.000000 | 1011.000000 | 1.32 | 23.740000 | 2.080000 | 7858.000000 | 311.000000 | 1.04 | 1.030000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 22:00:00 | 90.000000 | 19.480000 | 22.240000 | 87.000000 | 1012.000000 | 1.28 | 21.740000 | 0.500000 | 6974.000000 | 313.000000 | 1.31 | 0.840000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26085170 | "BASE AEREA MARCO FIDEL SUAREZ  - AUT [26085170]" | 3.360417 | -76.299722 | 975.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-11-23 00:00:00 | NaT | Valle del Cauca | Florida | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 23:00:00 | 92.000000 | 18.230000 | 20.150000 | 91.000000 | 1013.000000 | 1.16 | 19.740000 | 0.000000 | 6940.000000 | 53.000000 | 0.9 | 0.700000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26085170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26085170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26085170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26085170_OWM_Windspeed_20220111.png)
