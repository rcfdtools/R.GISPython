
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - FARALLONES - AUT [26055100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26055100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.41605556,-76.6515) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.41605556&lon=-76.6515)


| Parameter | Value |
|---|---|
| Code | 26055100 |
| Name | FARALLONES - AUT [26055100] |
| Latitude, ° | 3.41605556 |
| Longitude, ° | -76.6515 |
| Elevation, m | 2275 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-28 00:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Cali |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Cali |

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

### (CNE index 2265) Open Weather values for station 26055100 - FARALLONES - AUT [26055100]

JSON data from API OWM:

```
{'lat': 3.4161, 'lon': -76.6515, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813351, 'sunset': 1641856321, 'temp': 19.39, 'feels_like': 19.68, 'pressure': 1012, 'humidity': 88, 'dew_point': 17.35, 'uvi': 3.72, 'clouds': 93, 'visibility': 6020, 'wind_speed': 1.58, 'wind_deg': 285, 'wind_gust': 2.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, 'hourly': [{'dt': 1641772800, 'temp': 16.39, 'feels_like': 16.54, 'pressure': 1014, 'humidity': 94, 'dew_point': 15.42, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 280, 'wind_gust': 2.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641776400, 'temp': 14.39, 'feels_like': 14.34, 'pressure': 1015, 'humidity': 94, 'dew_point': 13.44, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 274, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641780000, 'temp': 14.39, 'feels_like': 14.31, 'pressure': 1016, 'humidity': 93, 'dew_point': 13.27, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 247, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641783600, 'temp': 14.39, 'feels_like': 14.34, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.44, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 249, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641787200, 'temp': 14.39, 'feels_like': 14.34, 'pressure': 1016, 'humidity': 94, 'dew_point': 13.44, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 211, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641790800, 'temp': 13.39, 'feels_like': 13.24, 'pressure': 1016, 'humidity': 94, 'dew_point': 12.44, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 218, 'wind_gust': 0.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.39, 'feels_like': 13.24, 'pressure': 1015, 'humidity': 94, 'dew_point': 12.44, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 232, 'wind_gust': 0.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 12.39, 'feels_like': 12.17, 'pressure': 1014, 'humidity': 95, 'dew_point': 11.61, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 248, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641801600, 'temp': 12.39, 'feels_like': 12.17, 'pressure': 1014, 'humidity': 95, 'dew_point': 11.61, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 250, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 12.39, 'feels_like': 12.19, 'pressure': 1014, 'humidity': 96, 'dew_point': 11.77, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 231, 'wind_gust': 0.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 11.39, 'feels_like': 11.09, 'pressure': 1015, 'humidity': 96, 'dew_point': 10.78, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 262, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641812400, 'temp': 11.39, 'feels_like': 11.09, 'pressure': 1015, 'humidity': 96, 'dew_point': 10.78, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 270, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 12.39, 'feels_like': 12.19, 'pressure': 1016, 'humidity': 96, 'dew_point': 11.77, 'uvi': 0.37, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 266, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 13.39, 'feels_like': 13.21, 'pressure': 1017, 'humidity': 93, 'dew_point': 12.28, 'uvi': 1.66, 'clouds': 100, 'visibility': 5996, 'wind_speed': 0.55, 'wind_deg': 296, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641823200, 'temp': 14.39, 'feels_like': 14.23, 'pressure': 1017, 'humidity': 90, 'dew_point': 12.77, 'uvi': 4.22, 'clouds': 88, 'visibility': 9480, 'wind_speed': 0.69, 'wind_deg': 331, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641826800, 'temp': 16.39, 'feels_like': 16.36, 'pressure': 1017, 'humidity': 87, 'dew_point': 14.22, 'uvi': 7.42, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 319, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.82}}, {'dt': 1641830400, 'temp': 17.39, 'feels_like': 17.4, 'pressure': 1016, 'humidity': 85, 'dew_point': 14.84, 'uvi': 8.93, 'clouds': 88, 'visibility': 9197, 'wind_speed': 0.98, 'wind_deg': 300, 'wind_gust': 1.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641834000, 'temp': 18.39, 'feels_like': 18.5, 'pressure': 1015, 'humidity': 85, 'dew_point': 15.82, 'uvi': 10.02, 'clouds': 90, 'visibility': 8173, 'wind_speed': 1.2, 'wind_deg': 291, 'wind_gust': 1.72, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641837600, 'temp': 18.39, 'feels_like': 18.5, 'pressure': 1014, 'humidity': 85, 'dew_point': 15.82, 'uvi': 9.37, 'clouds': 71, 'visibility': 2475, 'wind_speed': 1.47, 'wind_deg': 283, 'wind_gust': 1.91, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641841200, 'temp': 19.39, 'feels_like': 19.63, 'pressure': 1013, 'humidity': 86, 'dew_point': 16.99, 'uvi': 6.08, 'clouds': 87, 'visibility': 3460, 'wind_speed': 1.63, 'wind_deg': 280, 'wind_gust': 2.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641844800, 'temp': 19.39, 'feels_like': 19.68, 'pressure': 1012, 'humidity': 88, 'dew_point': 17.35, 'uvi': 3.72, 'clouds': 93, 'visibility': 6020, 'wind_speed': 1.58, 'wind_deg': 285, 'wind_gust': 2.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641848400, 'temp': 15.39, 'feels_like': 15.33, 'pressure': 1012, 'humidity': 90, 'dew_point': 13.76, 'uvi': 1.65, 'clouds': 95, 'visibility': 6327, 'wind_speed': 1.53, 'wind_deg': 289, 'wind_gust': 2.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641852000, 'temp': 13.39, 'feels_like': 13.19, 'pressure': 1012, 'humidity': 92, 'dew_point': 12.12, 'uvi': 0.37, 'clouds': 96, 'visibility': 6637, 'wind_speed': 1.24, 'wind_deg': 297, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641855600, 'temp': 11.39, 'feels_like': 11.04, 'pressure': 1013, 'humidity': 94, 'dew_point': 10.46, 'uvi': 0, 'clouds': 97, 'visibility': 6346, 'wind_speed': 1.36, 'wind_deg': 292, 'wind_gust': 2.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 00:00:00 | 58.000000 | 15.420000 | 16.540000 | 94.000000 | 1014.000000 | 0.33 | 16.390000 | 0.000000 | 10000.000000 | 280.000000 | 2.07 | 1.320000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 01:00:00 | 73.000000 | 13.440000 | 14.340000 | 94.000000 | 1015.000000 | 0.31 | 14.390000 | 0.000000 | 10000.000000 | 274.000000 | 1.71 | 1.150000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 02:00:00 | 64.000000 | 13.270000 | 14.310000 | 93.000000 | 1016.000000 | 0.25 | 14.390000 | 0.000000 | 10000.000000 | 247.000000 | 1.06 | 0.760000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 03:00:00 | 64.000000 | 13.440000 | 14.340000 | 94.000000 | 1016.000000 | 0.16 | 14.390000 | 0.000000 | 10000.000000 | 249.000000 | 0.73 | 0.550000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 04:00:00 | 71.000000 | 13.440000 | 14.340000 | 94.000000 | 1016.000000 | 0.14 | 14.390000 | 0.000000 | 10000.000000 | 211.000000 | 0.73 | 0.550000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 05:00:00 | 76.000000 | 12.440000 | 13.240000 | 94.000000 | 1016.000000 |  | 13.390000 | 0.000000 | 10000.000000 | 218.000000 | 0.63 | 0.470000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 06:00:00 | 68.000000 | 12.440000 | 13.240000 | 94.000000 | 1015.000000 |  | 13.390000 | 0.000000 | 10000.000000 | 232.000000 | 0.68 | 0.540000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 11.610000 | 12.170000 | 95.000000 | 1014.000000 | 0.1 | 12.390000 | 0.000000 | 10000.000000 | 248.000000 | 1.03 | 0.700000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 11.610000 | 12.170000 | 95.000000 | 1014.000000 |  | 12.390000 | 0.000000 | 10000.000000 | 250.000000 | 1.15 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 11.770000 | 12.190000 | 96.000000 | 1014.000000 | 0.23 | 12.390000 | 0.000000 | 10000.000000 | 231.000000 | 0.78 | 0.410000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 10.780000 | 11.090000 | 96.000000 | 1015.000000 | 0.15 | 11.390000 | 0.000000 | 10000.000000 | 262.000000 | 0.53 | 0.280000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 10.780000 | 11.090000 | 96.000000 | 1015.000000 |  | 11.390000 | 0.000000 | 10000.000000 | 270.000000 | 0.56 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 12:00:00 | 95.000000 | 11.770000 | 12.190000 | 96.000000 | 1016.000000 |  | 12.390000 | 0.370000 | 10000.000000 | 266.000000 | 0.86 | 0.380000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 12.280000 | 13.210000 | 93.000000 | 1017.000000 | 0.4 | 13.390000 | 1.660000 | 5996.000000 | 296.000000 | 1.27 | 0.550000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 14:00:00 | 88.000000 | 12.770000 | 14.230000 | 90.000000 | 1017.000000 | 0.58 | 14.390000 | 4.220000 | 9480.000000 | 331.000000 | 1.19 | 0.690000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 15:00:00 | 85.000000 | 14.220000 | 16.360000 | 87.000000 | 1017.000000 | 0.82 | 16.390000 | 7.420000 | 10000.000000 | 319.000000 | 1.32 | 0.810000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 14.840000 | 17.400000 | 85.000000 | 1016.000000 | 1.23 | 17.390000 | 8.930000 | 9197.000000 | 300.000000 | 1.44 | 0.980000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 15.820000 | 18.500000 | 85.000000 | 1015.000000 | 1.09 | 18.390000 | 10.020000 | 8173.000000 | 291.000000 | 1.72 | 1.200000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 18:00:00 | 71.000000 | 15.820000 | 18.500000 | 85.000000 | 1014.000000 | 1.23 | 18.390000 | 9.370000 | 2475.000000 | 283.000000 | 1.91 | 1.470000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 16.990000 | 19.630000 | 86.000000 | 1013.000000 | 1.14 | 19.390000 | 6.080000 | 3460.000000 | 280.000000 | 2.19 | 1.630000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 20:00:00 | 93.000000 | 17.350000 | 19.680000 | 88.000000 | 1012.000000 | 1.08 | 19.390000 | 3.720000 | 6020.000000 | 285.000000 | 2.25 | 1.580000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 21:00:00 | 95.000000 | 13.760000 | 15.330000 | 90.000000 | 1012.000000 | 1.16 | 15.390000 | 1.650000 | 6327.000000 | 289.000000 | 2.18 | 1.530000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 12.120000 | 13.190000 | 92.000000 | 1012.000000 | 0.94 | 13.390000 | 0.370000 | 6637.000000 | 297.000000 | 1.89 | 1.240000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26055100 | "FARALLONES - AUT [26055100]" | 3.416056 | -76.651500 | 2275.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-28 00:00:00 | NaT | Valle del Cauca | Cali | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Cali | America/Bogota | 2022-01-10 23:00:00 | 97.000000 | 10.460000 | 11.040000 | 94.000000 | 1013.000000 | 1.01 | 11.390000 | 0.000000 | 6346.000000 | 292.000000 | 2.02 | 1.360000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26055100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26055100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26055100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26055100_OWM_Windspeed_20220111.png)
