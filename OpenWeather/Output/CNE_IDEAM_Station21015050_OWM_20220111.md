
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PURACE  - AUT [21015050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21015050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.92591667,-76.42755556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.92591667&lon=-76.42755556)


| Parameter | Value |
|---|---|
| Code | 21015050 |
| Name | PURACE  - AUT [21015050] |
| Latitude, ° | 1.92591667 |
| Longitude, ° | -76.42755556 |
| Elevation, m | 1900 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-17 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | San Agustín |
| Stream | Sombrerillos |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Alto Magdalena |

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

### (CNE index 25) Open Weather values for station 21015050 - PURACE  - AUT [21015050]

JSON data from API OWM:

```
{'lat': 1.9259, 'lon': -76.4276, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813154, 'sunset': 1641856411, 'temp': 18.95, 'feels_like': 19.33, 'pressure': 1013, 'humidity': 93, 'dew_point': 17.79, 'uvi': 3.54, 'clouds': 99, 'visibility': 5154, 'wind_speed': 0.48, 'wind_deg': 166, 'wind_gust': 1.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, 'hourly': [{'dt': 1641772800, 'temp': 16.48, 'feels_like': 16.69, 'pressure': 1016, 'humidity': 96, 'dew_point': 15.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 275, 'wind_gust': 0.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641776400, 'temp': 16.56, 'feels_like': 16.8, 'pressure': 1017, 'humidity': 97, 'dew_point': 16.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 287, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641780000, 'temp': 16.58, 'feels_like': 16.83, 'pressure': 1018, 'humidity': 97, 'dew_point': 16.1, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 280, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 16.56, 'feels_like': 16.8, 'pressure': 1018, 'humidity': 97, 'dew_point': 16.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 257, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641787200, 'temp': 16.49, 'feels_like': 16.75, 'pressure': 1018, 'humidity': 98, 'dew_point': 16.17, 'uvi': 0, 'clouds': 100, 'visibility': 9834, 'wind_speed': 0.53, 'wind_deg': 247, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641790800, 'temp': 16.48, 'feels_like': 16.74, 'pressure': 1017, 'humidity': 98, 'dew_point': 16.16, 'uvi': 0, 'clouds': 100, 'visibility': 8756, 'wind_speed': 0.26, 'wind_deg': 246, 'wind_gust': 0.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641794400, 'temp': 16.13, 'feels_like': 16.36, 'pressure': 1017, 'humidity': 98, 'dew_point': 15.81, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 275, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641798000, 'temp': 15.89, 'feels_like': 16.09, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.57, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 279, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641801600, 'temp': 15.74, 'feels_like': 15.93, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.42, 'uvi': 0, 'clouds': 100, 'visibility': 8780, 'wind_speed': 0.86, 'wind_deg': 284, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641805200, 'temp': 15.7, 'feels_like': 15.88, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.39, 'uvi': 0, 'clouds': 100, 'visibility': 8000, 'wind_speed': 0.83, 'wind_deg': 288, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641808800, 'temp': 15.63, 'feels_like': 15.81, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.32, 'uvi': 0, 'clouds': 100, 'visibility': 8573, 'wind_speed': 0.81, 'wind_deg': 293, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641812400, 'temp': 15.17, 'feels_like': 15.3, 'pressure': 1017, 'humidity': 98, 'dew_point': 14.86, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 285, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 16.26, 'feels_like': 16.47, 'pressure': 1017, 'humidity': 97, 'dew_point': 15.78, 'uvi': 0.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 304, 'wind_gust': 1.04, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.44, 'feels_like': 17.72, 'pressure': 1018, 'humidity': 95, 'dew_point': 16.63, 'uvi': 0.98, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 201, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641823200, 'temp': 18.08, 'feels_like': 18.37, 'pressure': 1018, 'humidity': 93, 'dew_point': 16.93, 'uvi': 2.43, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 146, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641826800, 'temp': 18.7, 'feels_like': 18.98, 'pressure': 1018, 'humidity': 90, 'dew_point': 17.03, 'uvi': 4.2, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 161, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641830400, 'temp': 19.7, 'feels_like': 20.02, 'pressure': 1017, 'humidity': 88, 'dew_point': 17.66, 'uvi': 9.47, 'clouds': 98, 'visibility': 9546, 'wind_speed': 0.65, 'wind_deg': 156, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641834000, 'temp': 20.35, 'feels_like': 20.71, 'pressure': 1016, 'humidity': 87, 'dew_point': 18.12, 'uvi': 10.56, 'clouds': 98, 'visibility': 8164, 'wind_speed': 0.84, 'wind_deg': 143, 'wind_gust': 1.22, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641837600, 'temp': 20.04, 'feels_like': 20.42, 'pressure': 1015, 'humidity': 89, 'dew_point': 18.17, 'uvi': 9.82, 'clouds': 91, 'visibility': 8179, 'wind_speed': 0.72, 'wind_deg': 129, 'wind_gust': 1.09, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.32}}, {'dt': 1641841200, 'temp': 19.52, 'feels_like': 19.9, 'pressure': 1014, 'humidity': 91, 'dew_point': 18.01, 'uvi': 5.79, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 141, 'wind_gust': 1.12, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1641844800, 'temp': 18.95, 'feels_like': 19.33, 'pressure': 1013, 'humidity': 93, 'dew_point': 17.79, 'uvi': 3.54, 'clouds': 99, 'visibility': 5154, 'wind_speed': 0.48, 'wind_deg': 166, 'wind_gust': 1.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1641848400, 'temp': 18.45, 'feels_like': 18.81, 'pressure': 1013, 'humidity': 94, 'dew_point': 17.47, 'uvi': 1.56, 'clouds': 99, 'visibility': 7252, 'wind_speed': 0.43, 'wind_deg': 207, 'wind_gust': 1.41, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.24}}, {'dt': 1641852000, 'temp': 17.96, 'feels_like': 18.32, 'pressure': 1014, 'humidity': 96, 'dew_point': 17.31, 'uvi': 0.5, 'clouds': 98, 'visibility': 9099, 'wind_speed': 0.38, 'wind_deg': 220, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641855600, 'temp': 16.91, 'feels_like': 17.22, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.59, 'uvi': 0, 'clouds': 94, 'visibility': 9890, 'wind_speed': 0.48, 'wind_deg': 246, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 15.840000 | 16.690000 | 96.000000 | 1016.000000 | 0.21 | 16.480000 | 0.000000 | 10000.000000 | 275.000000 | 0.48 | 0.340000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 16.080000 | 16.800000 | 97.000000 | 1017.000000 | 0.16 | 16.560000 | 0.000000 | 10000.000000 | 287.000000 | 0.66 | 0.510000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 16.100000 | 16.830000 | 97.000000 | 1018.000000 | 0.13 | 16.580000 | 0.000000 | 10000.000000 | 280.000000 | 0.68 | 0.540000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 16.080000 | 16.800000 | 97.000000 | 1018.000000 | 0.11 | 16.560000 | 0.000000 | 10000.000000 | 257.000000 | 0.55 | 0.410000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 16.170000 | 16.750000 | 98.000000 | 1018.000000 | 0.18 | 16.490000 | 0.000000 | 9834.000000 | 247.000000 | 0.6 | 0.530000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 16.160000 | 16.740000 | 98.000000 | 1017.000000 | 0.2 | 16.480000 | 0.000000 | 8756.000000 | 246.000000 | 0.34 | 0.260000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 15.810000 | 16.360000 | 98.000000 | 1017.000000 | 0.23 | 16.130000 | 0.000000 | 10000.000000 | 275.000000 | 0.79 | 0.590000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 15.570000 | 16.090000 | 98.000000 | 1016.000000 | 0.43 | 15.890000 | 0.000000 | 10000.000000 | 279.000000 | 0.94 | 0.720000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 15.420000 | 15.930000 | 98.000000 | 1016.000000 | 0.27 | 15.740000 | 0.000000 | 8780.000000 | 284.000000 | 0.99 | 0.860000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 15.390000 | 15.880000 | 98.000000 | 1016.000000 | 0.2 | 15.700000 | 0.000000 | 8000.000000 | 288.000000 | 1.06 | 0.830000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 15.320000 | 15.810000 | 98.000000 | 1016.000000 | 0.1 | 15.630000 | 0.000000 | 8573.000000 | 293.000000 | 1.06 | 0.810000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 14.860000 | 15.300000 | 98.000000 | 1017.000000 |  | 15.170000 | 0.000000 | 10000.000000 | 285.000000 | 1.35 | 1.100000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 15.780000 | 16.470000 | 97.000000 | 1017.000000 |  | 16.260000 | 0.370000 | 10000.000000 | 304.000000 | 1.04 | 0.640000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.630000 | 17.720000 | 95.000000 | 1018.000000 | 0.15 | 17.440000 | 0.980000 | 10000.000000 | 201.000000 | 0.9 | 0.250000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 16.930000 | 18.370000 | 93.000000 | 1018.000000 | 0.41 | 18.080000 | 2.430000 | 10000.000000 | 146.000000 | 1.03 | 0.300000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 17.030000 | 18.980000 | 90.000000 | 1018.000000 | 0.6 | 18.700000 | 4.200000 | 10000.000000 | 161.000000 | 1.25 | 0.270000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 17.660000 | 20.020000 | 88.000000 | 1017.000000 | 0.76 | 19.700000 | 9.470000 | 9546.000000 | 156.000000 | 1.22 | 0.650000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 18.120000 | 20.710000 | 87.000000 | 1016.000000 | 1.25 | 20.350000 | 10.560000 | 8164.000000 | 143.000000 | 1.22 | 0.840000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 18:00:00 | 91.000000 | 18.170000 | 20.420000 | 89.000000 | 1015.000000 | 1.32 | 20.040000 | 9.820000 | 8179.000000 | 129.000000 | 1.09 | 0.720000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 18.010000 | 19.900000 | 91.000000 | 1014.000000 | 1.33 | 19.520000 | 5.790000 | 10000.000000 | 141.000000 | 1.12 | 0.490000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 17.790000 | 19.330000 | 93.000000 | 1013.000000 | 1.33 | 18.950000 | 3.540000 | 5154.000000 | 166.000000 | 1.4 | 0.480000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 17.470000 | 18.810000 | 94.000000 | 1013.000000 | 1.24 | 18.450000 | 1.560000 | 7252.000000 | 207.000000 | 1.41 | 0.430000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 17.310000 | 18.320000 | 96.000000 | 1014.000000 | 0.92 | 17.960000 | 0.500000 | 9099.000000 | 220.000000 | 1.51 | 0.380000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015050 | "PURACE  - AUT [21015050]" | 1.925917 | -76.427556 | 1900.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-17 00:00:00 | NaT | Huila | San Agustín | Sombrerillos | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 16.590000 | 17.220000 | 98.000000 | 1015.000000 | 0.89 | 16.910000 | 0.000000 | 9890.000000 | 246.000000 | 1.19 | 0.480000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21015050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21015050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21015050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015050_OWM_Windspeed_20220111.png)
