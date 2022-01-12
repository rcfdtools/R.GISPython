
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN PABLO DE BORBUR  - AUT [23125160] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23125160_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.64702778,-74.07130556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.64702778&lon=-74.07130556)


| Parameter | Value |
|---|---|
| Code | 23125160 |
| Name | SAN PABLO DE BORBUR  - AUT [23125160] |
| Latitude, ° | 5.64702778 |
| Longitude, ° | -74.07130556 |
| Elevation, m | 742 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-13 19:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | San Pablo De Borbur |
| Stream | 0 |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Carare (Minero) |

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

### (CNE index 143) Open Weather values for station 23125160 - SAN PABLO DE BORBUR  - AUT [23125160]

JSON data from API OWM:

```
{'lat': 5.647, 'lon': -74.0713, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812948, 'sunset': 1641855485, 'temp': 26.59, 'feels_like': 26.59, 'pressure': 1011, 'humidity': 80, 'dew_point': 22.85, 'uvi': 4.49, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 322, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, 'hourly': [{'dt': 1641772800, 'temp': 22.59, 'feels_like': 23.44, 'pressure': 1014, 'humidity': 97, 'dew_point': 22.09, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 95, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641776400, 'temp': 22.22, 'feels_like': 23, 'pressure': 1015, 'humidity': 96, 'dew_point': 21.55, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 103, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641780000, 'temp': 21.8, 'feels_like': 22.57, 'pressure': 1016, 'humidity': 97, 'dew_point': 21.3, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 111, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 21.5, 'feels_like': 22.24, 'pressure': 1016, 'humidity': 97, 'dew_point': 21, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 113, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 21.23, 'feels_like': 21.92, 'pressure': 1016, 'humidity': 96, 'dew_point': 20.57, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 120, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.96, 'feels_like': 21.62, 'pressure': 1015, 'humidity': 96, 'dew_point': 20.3, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 119, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.78, 'feels_like': 21.42, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.12, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 115, 'wind_gust': 1.21, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 20.32, 'feels_like': 20.91, 'pressure': 1014, 'humidity': 96, 'dew_point': 19.66, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 113, 'wind_gust': 1.23, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 20.02, 'feels_like': 20.56, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.19, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 109, 'wind_gust': 1.28, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 19.81, 'feels_like': 20.33, 'pressure': 1014, 'humidity': 95, 'dew_point': 18.99, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 113, 'wind_gust': 1.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 19.69, 'feels_like': 20.2, 'pressure': 1015, 'humidity': 95, 'dew_point': 18.87, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 112, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.75, 'feels_like': 20.26, 'pressure': 1015, 'humidity': 95, 'dew_point': 18.93, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 110, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 20.85, 'feels_like': 21.39, 'pressure': 1016, 'humidity': 92, 'dew_point': 19.5, 'uvi': 0.45, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 109, 'wind_gust': 1.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.82, 'feels_like': 24.42, 'pressure': 1017, 'humidity': 83, 'dew_point': 20.76, 'uvi': 1.57, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 20, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.81, 'feels_like': 26.4, 'pressure': 1017, 'humidity': 75, 'dew_point': 21.04, 'uvi': 3.81, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 316, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.38, 'feels_like': 29.41, 'pressure': 1016, 'humidity': 69, 'dew_point': 21.19, 'uvi': 6.46, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 309, 'wind_gust': 1.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.47, 'feels_like': 30.85, 'pressure': 1015, 'humidity': 65, 'dew_point': 21.25, 'uvi': 8.35, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 304, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641834000, 'temp': 29.18, 'feels_like': 31.84, 'pressure': 1014, 'humidity': 63, 'dew_point': 21.41, 'uvi': 9.09, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 303, 'wind_gust': 1.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 28.4, 'feels_like': 31.16, 'pressure': 1013, 'humidity': 68, 'dew_point': 21.92, 'uvi': 8.24, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 313, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641841200, 'temp': 27.36, 'feels_like': 30, 'pressure': 1012, 'humidity': 75, 'dew_point': 22.54, 'uvi': 7.76, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 316, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641844800, 'temp': 26.59, 'feels_like': 26.59, 'pressure': 1011, 'humidity': 80, 'dew_point': 22.85, 'uvi': 4.49, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 322, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641848400, 'temp': 26.19, 'feels_like': 26.19, 'pressure': 1011, 'humidity': 84, 'dew_point': 23.27, 'uvi': 1.8, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 330, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641852000, 'temp': 24.95, 'feels_like': 25.93, 'pressure': 1012, 'humidity': 93, 'dew_point': 23.74, 'uvi': 0.39, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 0, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641855600, 'temp': 23.1, 'feels_like': 23.97, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.43, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 61, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 00:00:00 | 24.000000 | 22.090000 | 23.440000 | 97.000000 | 1014.000000 | 0.49 | 22.590000 | 0.000000 | 10000.000000 | 95.000000 | 0.93 | 1.150000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 01:00:00 | 30.000000 | 21.550000 | 23.000000 | 96.000000 | 1015.000000 | 0.29 | 22.220000 | 0.000000 | 10000.000000 | 103.000000 | 0.94 | 1.110000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 02:00:00 | 38.000000 | 21.300000 | 22.570000 | 97.000000 | 1016.000000 | 0.12 | 21.800000 | 0.000000 | 10000.000000 | 111.000000 | 1.08 | 1.350000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 03:00:00 | 54.000000 | 21.000000 | 22.240000 | 97.000000 | 1016.000000 |  | 21.500000 | 0.000000 | 10000.000000 | 113.000000 | 1.18 | 1.510000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 04:00:00 | 59.000000 | 20.570000 | 21.920000 | 96.000000 | 1016.000000 |  | 21.230000 | 0.000000 | 10000.000000 | 120.000000 | 1.18 | 1.520000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 05:00:00 | 60.000000 | 20.300000 | 21.620000 | 96.000000 | 1015.000000 |  | 20.960000 | 0.000000 | 10000.000000 | 119.000000 | 1.21 | 1.610000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 06:00:00 | 13.000000 | 20.120000 | 21.420000 | 96.000000 | 1014.000000 |  | 20.780000 | 0.000000 | 10000.000000 | 115.000000 | 1.21 | 1.600000 | 801 | Clouds | few clouds | 02n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 07:00:00 | 24.000000 | 19.660000 | 20.910000 | 96.000000 | 1014.000000 |  | 20.320000 | 0.000000 | 10000.000000 | 113.000000 | 1.23 | 1.680000 | 801 | Clouds | few clouds | 02n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 08:00:00 | 44.000000 | 19.190000 | 20.560000 | 95.000000 | 1014.000000 |  | 20.020000 | 0.000000 | 10000.000000 | 109.000000 | 1.28 | 1.770000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 09:00:00 | 50.000000 | 18.990000 | 20.330000 | 95.000000 | 1014.000000 |  | 19.810000 | 0.000000 | 10000.000000 | 113.000000 | 1.3 | 1.720000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 18.870000 | 20.200000 | 95.000000 | 1015.000000 |  | 19.690000 | 0.000000 | 10000.000000 | 112.000000 | 1.29 | 1.810000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 11:00:00 | 55.000000 | 18.930000 | 20.260000 | 95.000000 | 1015.000000 |  | 19.750000 | 0.000000 | 10000.000000 | 110.000000 | 1.3 | 1.760000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 12:00:00 | 73.000000 | 19.500000 | 21.390000 | 92.000000 | 1016.000000 |  | 20.850000 | 0.450000 | 10000.000000 | 109.000000 | 1.42 | 1.480000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 13:00:00 | 79.000000 | 20.760000 | 24.420000 | 83.000000 | 1017.000000 |  | 23.820000 | 1.570000 | 10000.000000 | 20.000000 | 0.9 | 0.240000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 14:00:00 | 77.000000 | 21.040000 | 26.400000 | 75.000000 | 1017.000000 |  | 25.810000 | 3.810000 | 10000.000000 | 316.000000 | 1.21 | 1.150000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 15:00:00 | 61.000000 | 21.190000 | 29.410000 | 69.000000 | 1016.000000 |  | 27.380000 | 6.460000 | 10000.000000 | 309.000000 | 1.48 | 1.790000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 16:00:00 | 56.000000 | 21.250000 | 30.850000 | 65.000000 | 1015.000000 | 0.1 | 28.470000 | 8.350000 | 10000.000000 | 304.000000 | 1.66 | 2.100000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 17:00:00 | 54.000000 | 21.410000 | 31.840000 | 63.000000 | 1014.000000 |  | 29.180000 | 9.090000 | 10000.000000 | 303.000000 | 1.56 | 2.180000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 18:00:00 | 77.000000 | 21.920000 | 31.160000 | 68.000000 | 1013.000000 | 0.12 | 28.400000 | 8.240000 | 10000.000000 | 313.000000 | 1.56 | 1.930000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 22.540000 | 30.000000 | 75.000000 | 1012.000000 | 0.34 | 27.360000 | 7.760000 | 10000.000000 | 316.000000 | 1.59 | 1.560000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 20:00:00 | 91.000000 | 22.850000 | 26.590000 | 80.000000 | 1011.000000 | 0.33 | 26.590000 | 4.490000 | 10000.000000 | 322.000000 | 1.45 | 1.210000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 21:00:00 | 91.000000 | 23.270000 | 26.190000 | 84.000000 | 1011.000000 | 0.37 | 26.190000 | 1.800000 | 10000.000000 | 330.000000 | 1.27 | 1.000000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 23.740000 | 25.930000 | 93.000000 | 1012.000000 | 0.55 | 24.950000 | 0.390000 | 10000.000000 | 0.000000 | 1.32 | 0.820000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125160 | "SAN PABLO DE BORBUR  - AUT [23125160]" | 5.647028 | -74.071306 | 742.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-13 19:00:00 | NaT | Boyacá | San Pablo De Borbur | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 22.430000 | 23.970000 | 96.000000 | 1013.000000 | 0.33 | 23.100000 | 0.000000 | 10000.000000 | 61.000000 | 0.73 | 0.740000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station23125160_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23125160_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23125160_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125160_OWM_Windspeed_20220111.png)
