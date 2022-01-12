
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PARQUE ARQUEOLOGICO - AUT [21015030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21015030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.88847222,-76.29497222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.88847222&lon=-76.29497222)


| Parameter | Value |
|---|---|
| Code | 21015030 |
| Name | PARQUE ARQUEOLOGICO - AUT [21015030] |
| Latitude, ° | 1.88847222 |
| Longitude, ° | -76.29497222 |
| Elevation, m | 1800 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1971-06-14 19:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | San Agustín |
| Stream | 0 |
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

### (CNE index 312) Open Weather values for station 21015030 - PARQUE ARQUEOLOGICO - AUT [21015030]

JSON data from API OWM:

```
{'lat': 1.8885, 'lon': -76.295, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813118, 'sunset': 1641856383, 'temp': 19.28, 'feels_like': 19.64, 'pressure': 1012, 'humidity': 91, 'dew_point': 17.77, 'uvi': 3.54, 'clouds': 97, 'visibility': 6349, 'wind_speed': 1.07, 'wind_deg': 128, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.38}}, 'hourly': [{'dt': 1641772800, 'temp': 16.25, 'feels_like': 16.44, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 252, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641776400, 'temp': 16.32, 'feels_like': 16.51, 'pressure': 1016, 'humidity': 96, 'dew_point': 15.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 257, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641780000, 'temp': 16.39, 'feels_like': 16.59, 'pressure': 1017, 'humidity': 96, 'dew_point': 15.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 245, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 16.45, 'feels_like': 16.66, 'pressure': 1017, 'humidity': 96, 'dew_point': 15.81, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 233, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641787200, 'temp': 16.4, 'feels_like': 16.63, 'pressure': 1017, 'humidity': 97, 'dew_point': 15.92, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 235, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641790800, 'temp': 16.32, 'feels_like': 16.54, 'pressure': 1016, 'humidity': 97, 'dew_point': 15.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 211, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641794400, 'temp': 16, 'feels_like': 16.21, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.68, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 229, 'wind_gust': 0.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641798000, 'temp': 15.84, 'feels_like': 16.04, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.52, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 236, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.52}}, {'dt': 1641801600, 'temp': 15.67, 'feels_like': 15.85, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.36, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 255, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.36}}, {'dt': 1641805200, 'temp': 15.47, 'feels_like': 15.63, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.16, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 266, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641808800, 'temp': 15.46, 'feels_like': 15.62, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.15, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 268, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641812400, 'temp': 14.97, 'feels_like': 15.08, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 267, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 16.15, 'feels_like': 16.35, 'pressure': 1016, 'humidity': 97, 'dew_point': 15.67, 'uvi': 0.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 317, 'wind_gust': 0.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 17.22, 'feels_like': 17.48, 'pressure': 1017, 'humidity': 95, 'dew_point': 16.41, 'uvi': 0.98, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 124, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641823200, 'temp': 17.83, 'feels_like': 18.1, 'pressure': 1018, 'humidity': 93, 'dew_point': 16.68, 'uvi': 2.43, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 121, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641826800, 'temp': 18.47, 'feels_like': 18.75, 'pressure': 1017, 'humidity': 91, 'dew_point': 16.97, 'uvi': 4.2, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 126, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641830400, 'temp': 19.78, 'feels_like': 20.09, 'pressure': 1016, 'humidity': 87, 'dew_point': 17.55, 'uvi': 9.47, 'clouds': 98, 'visibility': 9209, 'wind_speed': 1.17, 'wind_deg': 125, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641834000, 'temp': 20.44, 'feels_like': 20.79, 'pressure': 1015, 'humidity': 86, 'dew_point': 18.02, 'uvi': 10.56, 'clouds': 98, 'visibility': 8455, 'wind_speed': 1.23, 'wind_deg': 118, 'wind_gust': 1.31, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.31}}, {'dt': 1641837600, 'temp': 20.26, 'feels_like': 20.61, 'pressure': 1014, 'humidity': 87, 'dew_point': 18.03, 'uvi': 9.82, 'clouds': 87, 'visibility': 8006, 'wind_speed': 1.25, 'wind_deg': 112, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.3}}, {'dt': 1641841200, 'temp': 19.73, 'feels_like': 20.08, 'pressure': 1013, 'humidity': 89, 'dew_point': 17.87, 'uvi': 5.79, 'clouds': 99, 'visibility': 6579, 'wind_speed': 1.13, 'wind_deg': 114, 'wind_gust': 1.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.41}}, {'dt': 1641844800, 'temp': 19.28, 'feels_like': 19.64, 'pressure': 1012, 'humidity': 91, 'dew_point': 17.77, 'uvi': 3.54, 'clouds': 97, 'visibility': 6349, 'wind_speed': 1.07, 'wind_deg': 128, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.38}}, {'dt': 1641848400, 'temp': 18.71, 'feels_like': 19.06, 'pressure': 1012, 'humidity': 93, 'dew_point': 17.56, 'uvi': 1.56, 'clouds': 98, 'visibility': 6467, 'wind_speed': 0.83, 'wind_deg': 140, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.46}}, {'dt': 1641852000, 'temp': 17.94, 'feels_like': 18.3, 'pressure': 1013, 'humidity': 96, 'dew_point': 17.29, 'uvi': 0.5, 'clouds': 97, 'visibility': 6834, 'wind_speed': 0.73, 'wind_deg': 152, 'wind_gust': 1.5, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641855600, 'temp': 16.83, 'feels_like': 17.1, 'pressure': 1014, 'humidity': 97, 'dew_point': 16.35, 'uvi': 0, 'clouds': 95, 'visibility': 7423, 'wind_speed': 0.64, 'wind_deg': 166, 'wind_gust': 1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 15.610000 | 16.440000 | 96.000000 | 1015.000000 | 0.2 | 16.250000 | 0.000000 | 10000.000000 | 252.000000 | 0.61 | 0.400000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 15.680000 | 16.510000 | 96.000000 | 1016.000000 | 0.14 | 16.320000 | 0.000000 | 10000.000000 | 257.000000 | 0.71 | 0.430000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 15.750000 | 16.590000 | 96.000000 | 1017.000000 | 0.13 | 16.390000 | 0.000000 | 10000.000000 | 245.000000 | 0.68 | 0.420000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 15.810000 | 16.660000 | 96.000000 | 1017.000000 | 0.15 | 16.450000 | 0.000000 | 10000.000000 | 233.000000 | 0.64 | 0.500000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 15.920000 | 16.630000 | 97.000000 | 1017.000000 | 0.22 | 16.400000 | 0.000000 | 10000.000000 | 235.000000 | 0.66 | 0.560000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 15.840000 | 16.540000 | 97.000000 | 1016.000000 | 0.23 | 16.320000 | 0.000000 | 10000.000000 | 211.000000 | 0.41 | 0.250000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 06:00:00 | 92.000000 | 15.680000 | 16.210000 | 98.000000 | 1016.000000 | 0.28 | 16.000000 | 0.000000 | 10000.000000 | 229.000000 | 0.58 | 0.380000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 15.520000 | 16.040000 | 98.000000 | 1015.000000 | 0.52 | 15.840000 | 0.000000 | 10000.000000 | 236.000000 | 0.56 | 0.380000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 15.360000 | 15.850000 | 98.000000 | 1015.000000 | 0.36 | 15.670000 | 0.000000 | 10000.000000 | 255.000000 | 0.68 | 0.640000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 15.160000 | 15.630000 | 98.000000 | 1015.000000 | 0.28 | 15.470000 | 0.000000 | 10000.000000 | 266.000000 | 0.72 | 0.670000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 15.150000 | 15.620000 | 98.000000 | 1015.000000 | 0.15 | 15.460000 | 0.000000 | 10000.000000 | 268.000000 | 0.65 | 0.580000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 14.660000 | 15.080000 | 98.000000 | 1016.000000 |  | 14.970000 | 0.000000 | 10000.000000 | 267.000000 | 0.95 | 0.910000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 15.670000 | 16.350000 | 97.000000 | 1016.000000 |  | 16.150000 | 0.370000 | 10000.000000 | 317.000000 | 0.58 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.410000 | 17.480000 | 95.000000 | 1017.000000 | 0.25 | 17.220000 | 0.980000 | 10000.000000 | 124.000000 | 0.77 | 0.340000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 16.680000 | 18.100000 | 93.000000 | 1018.000000 | 0.5 | 17.830000 | 2.430000 | 10000.000000 | 121.000000 | 1.14 | 0.720000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 16.970000 | 18.750000 | 91.000000 | 1017.000000 | 0.68 | 18.470000 | 4.200000 | 10000.000000 | 126.000000 | 1.04 | 0.780000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 17.550000 | 20.090000 | 87.000000 | 1016.000000 | 0.88 | 19.780000 | 9.470000 | 9209.000000 | 125.000000 | 1.21 | 1.170000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 18.020000 | 20.790000 | 86.000000 | 1015.000000 | 1.31 | 20.440000 | 10.560000 | 8455.000000 | 118.000000 | 1.31 | 1.230000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 18:00:00 | 87.000000 | 18.030000 | 20.610000 | 87.000000 | 1014.000000 | 1.3 | 20.260000 | 9.820000 | 8006.000000 | 112.000000 | 1.3 | 1.250000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 17.870000 | 20.080000 | 89.000000 | 1013.000000 | 1.41 | 19.730000 | 5.790000 | 6579.000000 | 114.000000 | 1.35 | 1.130000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 20:00:00 | 97.000000 | 17.770000 | 19.640000 | 91.000000 | 1012.000000 | 1.38 | 19.280000 | 3.540000 | 6349.000000 | 128.000000 | 1.54 | 1.070000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 17.560000 | 19.060000 | 93.000000 | 1012.000000 | 1.46 | 18.710000 | 1.560000 | 6467.000000 | 140.000000 | 1.45 | 0.830000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 22:00:00 | 97.000000 | 17.290000 | 18.300000 | 96.000000 | 1013.000000 | 1.18 | 17.940000 | 0.500000 | 6834.000000 | 152.000000 | 1.5 | 0.730000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015030 | "PARQUE ARQUEOLOGICO - AUT [21015030]" | 1.888472 | -76.294972 | 1800.000000 | Climática Principal | Automática con Telemetría | Activa | 1971-06-14 19:00:00 | NaT | Huila | San Agustín | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 16.350000 | 17.100000 | 97.000000 | 1014.000000 | 1.33 | 16.830000 | 0.000000 | 7423.000000 | 166.000000 | 1 | 0.640000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21015030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21015030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21015030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015030_OWM_Windspeed_20220111.png)
