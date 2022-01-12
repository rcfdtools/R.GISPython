
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SALTO EL [21255080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21255080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.78375,-74.76794444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.78375&lon=-74.76794444)


| Parameter | Value |
|---|---|
| Code | 21255080 |
| Name | SALTO EL [21255080] |
| Latitude, ° | 4.78375 |
| Longitude, ° | -74.76794444 |
| Elevation, m | 1139 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1968-11-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Ambalema |
| Stream | Guavio |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Coello |

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

### (CNE index 1708) Open Weather values for station 21255080 - SALTO EL [21255080]

JSON data from API OWM:

```
{'lat': 4.7838, 'lon': -74.7679, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813032, 'sunset': 1641855736, 'temp': 29.35, 'feels_like': 29.99, 'pressure': 1007, 'humidity': 49, 'dew_point': 17.53, 'uvi': 5.05, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 350, 'wind_gust': 3.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, 'hourly': [{'dt': 1641772800, 'temp': 27.35, 'feels_like': 30.42, 'pressure': 1010, 'humidity': 79, 'dew_point': 23.38, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 20, 'wind_gust': 5.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641776400, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1011, 'humidity': 84, 'dew_point': 23.43, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 41, 'wind_gust': 4.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641780000, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1012, 'humidity': 85, 'dew_point': 23.62, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 24, 'wind_gust': 2.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 26.35, 'feels_like': 26.35, 'pressure': 1013, 'humidity': 87, 'dew_point': 24.01, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 32, 'wind_gust': 2.78, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 28.06, 'feels_like': 33.58, 'pressure': 1013, 'humidity': 88, 'dew_point': 25.88, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 45, 'wind_gust': 1.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1012, 'humidity': 88, 'dew_point': 23.92, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 39, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.06, 'feels_like': 24.85, 'pressure': 1012, 'humidity': 89, 'dew_point': 22.13, 'uvi': 0, 'clouds': 15, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 51, 'wind_gust': 1.22, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 23.06, 'feels_like': 23.75, 'pressure': 1011, 'humidity': 89, 'dew_point': 21.15, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 70, 'wind_gust': 1.15, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 23.06, 'feels_like': 23.75, 'pressure': 1011, 'humidity': 89, 'dew_point': 21.15, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 64, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.06, 'feels_like': 23.77, 'pressure': 1011, 'humidity': 90, 'dew_point': 21.33, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 51, 'wind_gust': 1.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 24.06, 'feels_like': 24.92, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.68, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 54, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641812400, 'temp': 24.35, 'feels_like': 25.24, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.97, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 42, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641816000, 'temp': 25.35, 'feels_like': 26.29, 'pressure': 1014, 'humidity': 90, 'dew_point': 23.59, 'uvi': 0.46, 'clouds': 16, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 24, 'wind_gust': 2.18, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 25.35, 'feels_like': 26.06, 'pressure': 1015, 'humidity': 81, 'dew_point': 21.85, 'uvi': 2.05, 'clouds': 23, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 338, 'wind_gust': 2.96, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 25.35, 'feels_like': 25.79, 'pressure': 1015, 'humidity': 71, 'dew_point': 19.71, 'uvi': 5.01, 'clouds': 17, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 334, 'wind_gust': 3.5, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 27.35, 'feels_like': 28.45, 'pressure': 1014, 'humidity': 59, 'dew_point': 18.64, 'uvi': 8.54, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 326, 'wind_gust': 3.74, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 28.35, 'feels_like': 29.06, 'pressure': 1013, 'humidity': 52, 'dew_point': 17.55, 'uvi': 11.83, 'clouds': 37, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 328, 'wind_gust': 3.61, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 29.35, 'feels_like': 29.87, 'pressure': 1011, 'humidity': 48, 'dew_point': 17.2, 'uvi': 12.96, 'clouds': 43, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 328, 'wind_gust': 3.7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 30.35, 'feels_like': 31.25, 'pressure': 1010, 'humidity': 48, 'dew_point': 18.12, 'uvi': 11.83, 'clouds': 17, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 335, 'wind_gust': 3.32, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 31.35, 'feels_like': 32.8, 'pressure': 1008, 'humidity': 48, 'dew_point': 19.03, 'uvi': 8.61, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.9, 'wind_deg': 344, 'wind_gust': 3.34, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 29.35, 'feels_like': 29.99, 'pressure': 1007, 'humidity': 49, 'dew_point': 17.53, 'uvi': 5.05, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 350, 'wind_gust': 3.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641848400, 'temp': 28.35, 'feels_like': 29.38, 'pressure': 1007, 'humidity': 55, 'dew_point': 18.45, 'uvi': 2.07, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 355, 'wind_gust': 3.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641852000, 'temp': 28.35, 'feels_like': 30.37, 'pressure': 1008, 'humidity': 63, 'dew_point': 20.63, 'uvi': 0.43, 'clouds': 27, 'visibility': 10000, 'wind_speed': 2.63, 'wind_deg': 3, 'wind_gust': 4.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641855600, 'temp': 27.35, 'feels_like': 29.87, 'pressure': 1009, 'humidity': 74, 'dew_point': 22.31, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 353, 'wind_gust': 5.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 00:00:00 | 81.000000 | 23.380000 | 30.420000 | 79.000000 | 1010.000000 | 0.19 | 27.350000 | 0.000000 | 10000.000000 | 20.000000 | 5.8 | 1.950000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 01:00:00 | 83.000000 | 23.430000 | 26.350000 | 84.000000 | 1011.000000 | 0.31 | 26.350000 | 0.000000 | 10000.000000 | 41.000000 | 4.24 | 1.650000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 02:00:00 | 61.000000 | 23.620000 | 26.350000 | 85.000000 | 1012.000000 |  | 26.350000 | 0.000000 | 10000.000000 | 24.000000 | 2.97 | 1.410000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 03:00:00 | 50.000000 | 24.010000 | 26.350000 | 87.000000 | 1013.000000 |  | 26.350000 | 0.000000 | 10000.000000 | 32.000000 | 2.78 | 1.360000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 04:00:00 | 62.000000 | 25.880000 | 33.580000 | 88.000000 | 1013.000000 |  | 28.060000 | 0.000000 | 10000.000000 | 45.000000 | 1.51 | 1.280000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 05:00:00 | 69.000000 | 23.920000 | 26.060000 | 88.000000 | 1012.000000 |  | 26.060000 | 0.000000 | 10000.000000 | 39.000000 | 1.24 | 1.130000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 06:00:00 | 15.000000 | 22.130000 | 24.850000 | 89.000000 | 1012.000000 |  | 24.060000 | 0.000000 | 10000.000000 | 51.000000 | 1.22 | 1.150000 | 801 | Clouds | few clouds | 02n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 07:00:00 | 14.000000 | 21.150000 | 23.750000 | 89.000000 | 1011.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 70.000000 | 1.15 | 1.090000 | 801 | Clouds | few clouds | 02n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 08:00:00 | 51.000000 | 21.150000 | 23.750000 | 89.000000 | 1011.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 64.000000 | 1.07 | 0.890000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 09:00:00 | 39.000000 | 21.330000 | 23.770000 | 90.000000 | 1011.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 51.000000 | 1.07 | 0.950000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 10:00:00 | 34.000000 | 22.680000 | 24.920000 | 92.000000 | 1012.000000 | 0.22 | 24.060000 | 0.000000 | 10000.000000 | 54.000000 | 0.99 | 0.820000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 11:00:00 | 43.000000 | 22.970000 | 25.240000 | 92.000000 | 1012.000000 | 0.23 | 24.350000 | 0.000000 | 10000.000000 | 42.000000 | 0.83 | 0.690000 | 500 | Rain | light rain | 10n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 12:00:00 | 16.000000 | 23.590000 | 26.290000 | 90.000000 | 1014.000000 |  | 25.350000 | 0.460000 | 10000.000000 | 24.000000 | 2.18 | 1.000000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 13:00:00 | 23.000000 | 21.850000 | 26.060000 | 81.000000 | 1015.000000 |  | 25.350000 | 2.050000 | 10000.000000 | 338.000000 | 2.96 | 1.320000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 14:00:00 | 17.000000 | 19.710000 | 25.790000 | 71.000000 | 1015.000000 |  | 25.350000 | 5.010000 | 10000.000000 | 334.000000 | 3.5 | 1.550000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 15:00:00 | 25.000000 | 18.640000 | 28.450000 | 59.000000 | 1014.000000 |  | 27.350000 | 8.540000 | 10000.000000 | 326.000000 | 3.74 | 1.920000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 16:00:00 | 37.000000 | 17.550000 | 29.060000 | 52.000000 | 1013.000000 |  | 28.350000 | 11.830000 | 10000.000000 | 328.000000 | 3.61 | 2.250000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 17:00:00 | 43.000000 | 17.200000 | 29.870000 | 48.000000 | 1011.000000 |  | 29.350000 | 12.960000 | 10000.000000 | 328.000000 | 3.7 | 2.690000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 18:00:00 | 17.000000 | 18.120000 | 31.250000 | 48.000000 | 1010.000000 |  | 30.350000 | 11.830000 | 10000.000000 | 335.000000 | 3.32 | 2.560000 | 801 | Clouds | few clouds | 02d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 19:00:00 | 23.000000 | 19.030000 | 32.800000 | 48.000000 | 1008.000000 |  | 31.350000 | 8.610000 | 10000.000000 | 344.000000 | 3.34 | 2.900000 | 801 | Clouds | few clouds | 02d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 20:00:00 | 26.000000 | 17.530000 | 29.990000 | 49.000000 | 1007.000000 | 0.18 | 29.350000 | 5.050000 | 10000.000000 | 350.000000 | 3.36 | 2.960000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 21:00:00 | 26.000000 | 18.450000 | 29.380000 | 55.000000 | 1007.000000 | 0.24 | 28.350000 | 2.070000 | 10000.000000 | 355.000000 | 3.8 | 2.670000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 22:00:00 | 27.000000 | 20.630000 | 30.370000 | 63.000000 | 1008.000000 | 0.41 | 28.350000 | 0.430000 | 10000.000000 | 3.000000 | 4.72 | 2.630000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255080 | "SALTO EL [21255080]" | 4.783750 | -74.767944 | 1139.000000 | Climática Principal | Convencional | Activa | 1968-11-15 00:00:00 | NaT | Tolima | Ambalema | Guavio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 23:00:00 | 25.000000 | 22.310000 | 29.870000 | 74.000000 | 1009.000000 | 0.66 | 27.350000 | 0.000000 | 10000.000000 | 353.000000 | 5.38 | 2.180000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21255080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21255080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21255080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255080_OWM_Windspeed_20220111.png)
