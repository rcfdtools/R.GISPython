
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL PLACER - AUT [26105240] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26105240_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.87911111,-76.10055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.87911111&lon=-76.10055556)


| Parameter | Value |
|---|---|
| Code | 26105240 |
| Name | EL PLACER - AUT [26105240] |
| Latitude, ° | 3.87911111 |
| Longitude, ° | -76.10055556 |
| Elevation, m | 2200 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-30 00:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Buga |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Tulua y Morales |

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

### (CNE index 81) Open Weather values for station 26105240 - EL PLACER - AUT [26105240]

JSON data from API OWM:

```
{'lat': 3.8791, 'lon': -76.1006, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813264, 'sunset': 1641856144, 'temp': 19.85, 'feels_like': 20.19, 'pressure': 1013, 'humidity': 88, 'dew_point': 17.8, 'uvi': 3.14, 'clouds': 83, 'visibility': 7088, 'wind_speed': 1.27, 'wind_deg': 282, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, 'hourly': [{'dt': 1641772800, 'temp': 16.85, 'feels_like': 17.1, 'pressure': 1015, 'humidity': 96, 'dew_point': 16.21, 'uvi': 0, 'clouds': 62, 'visibility': 6711, 'wind_speed': 0.46, 'wind_deg': 73, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641776400, 'temp': 14.85, 'feels_like': 14.87, 'pressure': 1017, 'humidity': 95, 'dew_point': 14.06, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 86, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.55}}, {'dt': 1641780000, 'temp': 14.85, 'feels_like': 14.87, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.06, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 114, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.36}}, {'dt': 1641783600, 'temp': 14.85, 'feels_like': 14.87, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.06, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 125, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641787200, 'temp': 14.85, 'feels_like': 14.87, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.06, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 132, 'wind_gust': 0.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 13.85, 'feels_like': 13.77, 'pressure': 1017, 'humidity': 95, 'dew_point': 13.06, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 127, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.85, 'feels_like': 13.77, 'pressure': 1016, 'humidity': 95, 'dew_point': 13.06, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 152, 'wind_gust': 0.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 12.85, 'feels_like': 12.7, 'pressure': 1016, 'humidity': 96, 'dew_point': 12.23, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 153, 'wind_gust': 0.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 12.85, 'feels_like': 12.7, 'pressure': 1016, 'humidity': 96, 'dew_point': 12.23, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 157, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 12.85, 'feels_like': 12.72, 'pressure': 1016, 'humidity': 97, 'dew_point': 12.39, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 195, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641808800, 'temp': 11.85, 'feels_like': 11.62, 'pressure': 1016, 'humidity': 97, 'dew_point': 11.39, 'uvi': 0, 'clouds': 89, 'visibility': 9853, 'wind_speed': 0.31, 'wind_deg': 194, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641812400, 'temp': 11.85, 'feels_like': 11.62, 'pressure': 1017, 'humidity': 97, 'dew_point': 11.39, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 152, 'wind_gust': 0.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 12.85, 'feels_like': 12.72, 'pressure': 1018, 'humidity': 97, 'dew_point': 12.39, 'uvi': 0.2, 'clouds': 100, 'visibility': 7990, 'wind_speed': 0.3, 'wind_deg': 24, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641819600, 'temp': 13.85, 'feels_like': 13.77, 'pressure': 1018, 'humidity': 95, 'dew_point': 13.06, 'uvi': 1.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 345, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641823200, 'temp': 14.85, 'feels_like': 14.79, 'pressure': 1019, 'humidity': 92, 'dew_point': 13.56, 'uvi': 3.44, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 334, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}, {'dt': 1641826800, 'temp': 16.85, 'feels_like': 16.89, 'pressure': 1018, 'humidity': 88, 'dew_point': 14.85, 'uvi': 6.01, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 326, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641830400, 'temp': 17.85, 'feels_like': 17.88, 'pressure': 1017, 'humidity': 84, 'dew_point': 15.11, 'uvi': 7.7, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 296, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641834000, 'temp': 18.85, 'feels_like': 18.98, 'pressure': 1016, 'humidity': 84, 'dew_point': 16.09, 'uvi': 8.58, 'clouds': 99, 'visibility': 9314, 'wind_speed': 1.04, 'wind_deg': 286, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.82}}, {'dt': 1641837600, 'temp': 18.85, 'feels_like': 18.98, 'pressure': 1015, 'humidity': 84, 'dew_point': 16.09, 'uvi': 7.98, 'clouds': 72, 'visibility': 8766, 'wind_speed': 1.16, 'wind_deg': 286, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641841200, 'temp': 19.85, 'feels_like': 20.11, 'pressure': 1014, 'humidity': 85, 'dew_point': 17.26, 'uvi': 5.2, 'clouds': 77, 'visibility': 5351, 'wind_speed': 1.34, 'wind_deg': 281, 'wind_gust': 1.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641844800, 'temp': 19.85, 'feels_like': 20.19, 'pressure': 1013, 'humidity': 88, 'dew_point': 17.8, 'uvi': 3.14, 'clouds': 83, 'visibility': 7088, 'wind_speed': 1.27, 'wind_deg': 282, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641848400, 'temp': 15.85, 'feels_like': 15.81, 'pressure': 1013, 'humidity': 89, 'dew_point': 14.04, 'uvi': 1.37, 'clouds': 88, 'visibility': 8216, 'wind_speed': 1.04, 'wind_deg': 278, 'wind_gust': 1.29, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641852000, 'temp': 13.85, 'feels_like': 13.72, 'pressure': 1014, 'humidity': 93, 'dew_point': 12.74, 'uvi': 0.21, 'clouds': 91, 'visibility': 7110, 'wind_speed': 0.68, 'wind_deg': 296, 'wind_gust': 1.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.1}}, {'dt': 1641855600, 'temp': 11.85, 'feels_like': 11.57, 'pressure': 1015, 'humidity': 95, 'dew_point': 11.08, 'uvi': 0, 'clouds': 93, 'visibility': 6065, 'wind_speed': 0.26, 'wind_deg': 272, 'wind_gust': 0.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 00:00:00 | 62.000000 | 16.210000 | 17.100000 | 96.000000 | 1015.000000 | 0.15 | 16.850000 | 0.000000 | 6711.000000 | 73.000000 | 0.81 | 0.460000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 01:00:00 | 74.000000 | 14.060000 | 14.870000 | 95.000000 | 1017.000000 | 0.55 | 14.850000 | 0.000000 | 10000.000000 | 86.000000 | 0.77 | 0.450000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 14.060000 | 14.870000 | 95.000000 | 1018.000000 | 0.36 | 14.850000 | 0.000000 | 10000.000000 | 114.000000 | 0.76 | 0.420000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 03:00:00 | 63.000000 | 14.060000 | 14.870000 | 95.000000 | 1018.000000 | 0.14 | 14.850000 | 0.000000 | 10000.000000 | 125.000000 | 0.65 | 0.420000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 04:00:00 | 62.000000 | 14.060000 | 14.870000 | 95.000000 | 1018.000000 |  | 14.850000 | 0.000000 | 10000.000000 | 132.000000 | 0.63 | 0.550000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 05:00:00 | 64.000000 | 13.060000 | 13.770000 | 95.000000 | 1017.000000 |  | 13.850000 | 0.000000 | 10000.000000 | 127.000000 | 0.74 | 0.700000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 06:00:00 | 57.000000 | 13.060000 | 13.770000 | 95.000000 | 1016.000000 |  | 13.850000 | 0.000000 | 10000.000000 | 152.000000 | 0.5 | 0.380000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 12.230000 | 12.700000 | 96.000000 | 1016.000000 |  | 12.850000 | 0.000000 | 10000.000000 | 153.000000 | 0.53 | 0.370000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 08:00:00 | 81.000000 | 12.230000 | 12.700000 | 96.000000 | 1016.000000 | 0.13 | 12.850000 | 0.000000 | 10000.000000 | 157.000000 | 0.58 | 0.360000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 09:00:00 | 87.000000 | 12.390000 | 12.720000 | 97.000000 | 1016.000000 | 0.14 | 12.850000 | 0.000000 | 10000.000000 | 195.000000 | 0.61 | 0.380000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 10:00:00 | 89.000000 | 11.390000 | 11.620000 | 97.000000 | 1016.000000 | 0.2 | 11.850000 | 0.000000 | 9853.000000 | 194.000000 | 0.55 | 0.310000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 11:00:00 | 91.000000 | 11.390000 | 11.620000 | 97.000000 | 1017.000000 | 0.12 | 11.850000 | 0.000000 | 10000.000000 | 152.000000 | 0.49 | 0.100000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 12.390000 | 12.720000 | 97.000000 | 1018.000000 | 0.15 | 12.850000 | 0.200000 | 7990.000000 | 24.000000 | 0.72 | 0.300000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 13.060000 | 13.770000 | 95.000000 | 1018.000000 | 0.21 | 13.850000 | 1.360000 | 10000.000000 | 345.000000 | 0.89 | 0.550000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 13.560000 | 14.790000 | 92.000000 | 1019.000000 | 0.28 | 14.850000 | 3.440000 | 10000.000000 | 334.000000 | 1.05 | 0.860000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 14.850000 | 16.890000 | 88.000000 | 1018.000000 | 0.49 | 16.850000 | 6.010000 | 10000.000000 | 326.000000 | 1.09 | 1.080000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 15.110000 | 17.880000 | 84.000000 | 1017.000000 | 0.58 | 17.850000 | 7.700000 | 10000.000000 | 296.000000 | 1.09 | 1.280000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 16.090000 | 18.980000 | 84.000000 | 1016.000000 | 0.82 | 18.850000 | 8.580000 | 9314.000000 | 286.000000 | 1.03 | 1.040000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 18:00:00 | 72.000000 | 16.090000 | 18.980000 | 84.000000 | 1015.000000 | 0.92 | 18.850000 | 7.980000 | 8766.000000 | 286.000000 | 1 | 1.160000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 19:00:00 | 77.000000 | 17.260000 | 20.110000 | 85.000000 | 1014.000000 | 1.01 | 19.850000 | 5.200000 | 5351.000000 | 281.000000 | 1.35 | 1.340000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 20:00:00 | 83.000000 | 17.800000 | 20.190000 | 88.000000 | 1013.000000 | 1.25 | 19.850000 | 3.140000 | 7088.000000 | 282.000000 | 1.3 | 1.270000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 21:00:00 | 88.000000 | 14.040000 | 15.810000 | 89.000000 | 1013.000000 | 1.16 | 15.850000 | 1.370000 | 8216.000000 | 278.000000 | 1.29 | 1.040000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 22:00:00 | 91.000000 | 12.740000 | 13.720000 | 93.000000 | 1014.000000 | 1.1 | 13.850000 | 0.210000 | 7110.000000 | 296.000000 | 1.01 | 0.680000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26105240 | "EL PLACER - AUT [26105240]" | 3.879111 | -76.100556 | 2200.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 00:00:00 | NaT | Valle del Cauca | Buga | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Tulua y Morales | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 11.080000 | 11.570000 | 95.000000 | 1015.000000 | 1.11 | 11.850000 | 0.000000 | 6065.000000 | 272.000000 | 0.72 | 0.260000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26105240_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26105240_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26105240_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26105240_OWM_Windspeed_20220111.png)
