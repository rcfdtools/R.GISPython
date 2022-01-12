
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA PRIMAVERA - AUT [21015040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21015040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.02158333,-76.11433333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.02158333&lon=-76.11433333)


| Parameter | Value |
|---|---|
| Code | 21015040 |
| Name | LA PRIMAVERA - AUT [21015040] |
| Latitude, ° | 2.02158333 |
| Longitude, ° | -76.11433333 |
| Elevation, m | 1919 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-28 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | Saladoblanco |
| Stream | Sombrerillos |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Ríos Directos al Magdalena (mi) |

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

### (CNE index 26) Open Weather values for station 21015040 - LA PRIMAVERA - AUT [21015040]

JSON data from API OWM:

```
{'lat': 2.0216, 'lon': -76.1143, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813088, 'sunset': 1641856327, 'temp': 18.91, 'feels_like': 19.1, 'pressure': 1011, 'humidity': 86, 'dew_point': 16.52, 'uvi': 3.92, 'clouds': 74, 'visibility': 6217, 'wind_speed': 1.4, 'wind_deg': 127, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, 'hourly': [{'dt': 1641772800, 'temp': 15.37, 'feels_like': 15.42, 'pressure': 1014, 'humidity': 94, 'dew_point': 14.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 261, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641776400, 'temp': 15.36, 'feels_like': 15.41, 'pressure': 1015, 'humidity': 94, 'dew_point': 14.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 289, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641780000, 'temp': 15.5, 'feels_like': 15.56, 'pressure': 1016, 'humidity': 94, 'dew_point': 14.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 298, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 15.48, 'feels_like': 15.56, 'pressure': 1016, 'humidity': 95, 'dew_point': 14.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 277, 'wind_gust': 0.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641787200, 'temp': 15.27, 'feels_like': 15.33, 'pressure': 1016, 'humidity': 95, 'dew_point': 14.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 260, 'wind_gust': 0.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641790800, 'temp': 15.18, 'feels_like': 15.26, 'pressure': 1015, 'humidity': 96, 'dew_point': 14.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 302, 'wind_gust': 0.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641794400, 'temp': 14.89, 'feels_like': 14.97, 'pressure': 1015, 'humidity': 97, 'dew_point': 14.42, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 275, 'wind_gust': 0.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641798000, 'temp': 14.62, 'feels_like': 14.7, 'pressure': 1014, 'humidity': 98, 'dew_point': 14.31, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 267, 'wind_gust': 0.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1641801600, 'temp': 14.48, 'feels_like': 14.54, 'pressure': 1014, 'humidity': 98, 'dew_point': 14.17, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 273, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641805200, 'temp': 14.38, 'feels_like': 14.43, 'pressure': 1014, 'humidity': 98, 'dew_point': 14.07, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 274, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641808800, 'temp': 14.44, 'feels_like': 14.47, 'pressure': 1014, 'humidity': 97, 'dew_point': 13.97, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 270, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641812400, 'temp': 14.22, 'feels_like': 14.23, 'pressure': 1015, 'humidity': 97, 'dew_point': 13.75, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 283, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 14.79, 'feels_like': 14.83, 'pressure': 1016, 'humidity': 96, 'dew_point': 14.16, 'uvi': 0.26, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 349, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 15.71, 'feels_like': 15.82, 'pressure': 1016, 'humidity': 95, 'dew_point': 14.91, 'uvi': 1.55, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 104, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641823200, 'temp': 16.51, 'feels_like': 16.64, 'pressure': 1017, 'humidity': 93, 'dew_point': 15.37, 'uvi': 3.88, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 109, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641826800, 'temp': 17.47, 'feels_like': 17.6, 'pressure': 1017, 'humidity': 89, 'dew_point': 15.64, 'uvi': 6.73, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 122, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641830400, 'temp': 19.63, 'feels_like': 19.71, 'pressure': 1015, 'humidity': 79, 'dew_point': 15.89, 'uvi': 11.64, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 118, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641834000, 'temp': 20.07, 'feels_like': 20.17, 'pressure': 1014, 'humidity': 78, 'dew_point': 16.12, 'uvi': 12.98, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 113, 'wind_gust': 1.43, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.04}}, {'dt': 1641837600, 'temp': 19.85, 'feels_like': 19.98, 'pressure': 1013, 'humidity': 80, 'dew_point': 16.3, 'uvi': 12.07, 'clouds': 55, 'visibility': 9545, 'wind_speed': 1.5, 'wind_deg': 111, 'wind_gust': 1.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.27}}, {'dt': 1641841200, 'temp': 19.52, 'feels_like': 19.69, 'pressure': 1012, 'humidity': 83, 'dew_point': 16.56, 'uvi': 6.43, 'clouds': 75, 'visibility': 5659, 'wind_speed': 1.37, 'wind_deg': 120, 'wind_gust': 1.47, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.36}}, {'dt': 1641844800, 'temp': 18.91, 'feels_like': 19.1, 'pressure': 1011, 'humidity': 86, 'dew_point': 16.52, 'uvi': 3.92, 'clouds': 74, 'visibility': 6217, 'wind_speed': 1.4, 'wind_deg': 127, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641848400, 'temp': 18.26, 'feels_like': 18.44, 'pressure': 1011, 'humidity': 88, 'dew_point': 16.24, 'uvi': 1.72, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 137, 'wind_gust': 1.58, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.34}}, {'dt': 1641852000, 'temp': 17.33, 'feels_like': 17.55, 'pressure': 1012, 'humidity': 93, 'dew_point': 16.19, 'uvi': 0.54, 'clouds': 82, 'visibility': 8050, 'wind_speed': 0.91, 'wind_deg': 149, 'wind_gust': 1.5, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.36}}, {'dt': 1641855600, 'temp': 15.79, 'feels_like': 15.93, 'pressure': 1013, 'humidity': 96, 'dew_point': 15.15, 'uvi': 0, 'clouds': 84, 'visibility': 5530, 'wind_speed': 0.8, 'wind_deg': 160, 'wind_gust': 0.91, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.88}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 14.410000 | 15.420000 | 94.000000 | 1014.000000 | 0.24 | 15.370000 | 0.000000 | 10000.000000 | 261.000000 | 0.67 | 0.470000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 14.400000 | 15.410000 | 94.000000 | 1015.000000 | 0.22 | 15.360000 | 0.000000 | 10000.000000 | 289.000000 | 0.64 | 0.470000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 14.540000 | 15.560000 | 94.000000 | 1016.000000 | 0.15 | 15.500000 | 0.000000 | 10000.000000 | 298.000000 | 0.59 | 0.310000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 14.680000 | 15.560000 | 95.000000 | 1016.000000 | 0.16 | 15.480000 | 0.000000 | 10000.000000 | 277.000000 | 0.42 | 0.200000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 14.470000 | 15.330000 | 95.000000 | 1016.000000 | 0.28 | 15.270000 | 0.000000 | 10000.000000 | 260.000000 | 0.37 | 0.240000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 14.550000 | 15.260000 | 96.000000 | 1015.000000 | 0.31 | 15.180000 | 0.000000 | 10000.000000 | 302.000000 | 0.37 | 0.300000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 06:00:00 | 81.000000 | 14.420000 | 14.970000 | 97.000000 | 1015.000000 | 0.33 | 14.890000 | 0.000000 | 10000.000000 | 275.000000 | 0.35 | 0.190000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 14.310000 | 14.700000 | 98.000000 | 1014.000000 | 0.56 | 14.620000 | 0.000000 | 10000.000000 | 267.000000 | 0.49 | 0.370000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 14.170000 | 14.540000 | 98.000000 | 1014.000000 | 0.31 | 14.480000 | 0.000000 | 10000.000000 | 273.000000 | 0.59 | 0.620000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 09:00:00 | 97.000000 | 14.070000 | 14.430000 | 98.000000 | 1014.000000 | 0.21 | 14.380000 | 0.000000 | 10000.000000 | 274.000000 | 0.62 | 0.630000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 13.970000 | 14.470000 | 97.000000 | 1014.000000 | 0.24 | 14.440000 | 0.000000 | 10000.000000 | 270.000000 | 0.45 | 0.400000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 13.750000 | 14.230000 | 97.000000 | 1015.000000 |  | 14.220000 | 0.000000 | 10000.000000 | 283.000000 | 0.65 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 12:00:00 | 98.000000 | 14.160000 | 14.830000 | 96.000000 | 1016.000000 |  | 14.790000 | 0.260000 | 10000.000000 | 349.000000 | 0.44 | 0.210000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 14.910000 | 15.820000 | 95.000000 | 1016.000000 | 0.19 | 15.710000 | 1.550000 | 10000.000000 | 104.000000 | 0.85 | 0.460000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 15.370000 | 16.640000 | 93.000000 | 1017.000000 | 0.47 | 16.510000 | 3.880000 | 10000.000000 | 109.000000 | 1.27 | 0.800000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 15.640000 | 17.600000 | 89.000000 | 1017.000000 | 0.53 | 17.470000 | 6.730000 | 10000.000000 | 122.000000 | 1.18 | 0.870000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 15.890000 | 19.710000 | 79.000000 | 1015.000000 | 0.62 | 19.630000 | 11.640000 | 10000.000000 | 118.000000 | 1.27 | 1.280000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 17:00:00 | 96.000000 | 16.120000 | 20.170000 | 78.000000 | 1014.000000 | 1.04 | 20.070000 | 12.980000 | 10000.000000 | 113.000000 | 1.43 | 1.480000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 18:00:00 | 55.000000 | 16.300000 | 19.980000 | 80.000000 | 1013.000000 | 1.27 | 19.850000 | 12.070000 | 9545.000000 | 111.000000 | 1.48 | 1.500000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 16.560000 | 19.690000 | 83.000000 | 1012.000000 | 1.36 | 19.520000 | 6.430000 | 5659.000000 | 120.000000 | 1.47 | 1.370000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 20:00:00 | 74.000000 | 16.520000 | 19.100000 | 86.000000 | 1011.000000 | 1.25 | 18.910000 | 3.920000 | 6217.000000 | 127.000000 | 1.64 | 1.400000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 21:00:00 | 78.000000 | 16.240000 | 18.440000 | 88.000000 | 1011.000000 | 1.34 | 18.260000 | 1.720000 | 10000.000000 | 137.000000 | 1.58 | 1.180000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 22:00:00 | 82.000000 | 16.190000 | 17.550000 | 93.000000 | 1012.000000 | 1.36 | 17.330000 | 0.540000 | 8050.000000 | 149.000000 | 1.5 | 0.910000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015040 | "LA PRIMAVERA - AUT [21015040]" | 2.021583 | -76.114333 | 1919.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-28 00:00:00 | NaT | Huila | Saladoblanco | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos Directos al Magdalena (mi) | America/Bogota | 2022-01-10 23:00:00 | 84.000000 | 15.150000 | 15.930000 | 96.000000 | 1013.000000 | 1.88 | 15.790000 | 0.000000 | 5530.000000 | 160.000000 | 0.91 | 0.800000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21015040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21015040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21015040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015040_OWM_Windspeed_20220111.png)
