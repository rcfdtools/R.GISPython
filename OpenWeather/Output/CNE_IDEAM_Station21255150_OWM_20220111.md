
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GARCIA HACIENDA [21255150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21255150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.85541667,-74.89155556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.85541667&lon=-74.89155556)


| Parameter | Value |
|---|---|
| Code | 21255150 |
| Name | GARCIA HACIENDA [21255150] |
| Latitude, ° | 4.85541667 |
| Longitude, ° | -74.89155556 |
| Elevation, m | 350 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1986-12-15 00:00:00 |
| Suspension date | 2014-08-28 00:00:00 |
| State | Tolima |
| County | Lérida |
| Stream | Rucio |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Lagunilla y Otros Directos al Magdalena |

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

### (CNE index 3941) Open Weather values for station 21255150 - GARCIA HACIENDA [21255150]

JSON data from API OWM:

```
{'lat': 4.8554, 'lon': -74.8916, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813068, 'sunset': 1641855759, 'temp': 28.72, 'feels_like': 29.77, 'pressure': 1009, 'humidity': 54, 'dew_point': 18.5, 'uvi': 5.05, 'clouds': 45, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 16, 'wind_gust': 3.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, 'hourly': [{'dt': 1641772800, 'temp': 26.72, 'feels_like': 29.53, 'pressure': 1012, 'humidity': 85, 'dew_point': 23.99, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 327, 'wind_gust': 3.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641776400, 'temp': 25.72, 'feels_like': 26.62, 'pressure': 1013, 'humidity': 87, 'dew_point': 23.39, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 323, 'wind_gust': 2.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641780000, 'temp': 25.72, 'feels_like': 26.62, 'pressure': 1014, 'humidity': 87, 'dew_point': 23.39, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 315, 'wind_gust': 2.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.72, 'feels_like': 26.65, 'pressure': 1014, 'humidity': 88, 'dew_point': 23.58, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 315, 'wind_gust': 1.87, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 22.79, 'feels_like': 23.42, 'pressure': 1014, 'humidity': 88, 'dew_point': 20.7, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 310, 'wind_gust': 1.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.62, 'feels_like': 23.24, 'pressure': 1013, 'humidity': 88, 'dew_point': 20.53, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 305, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.41, 'feels_like': 23.03, 'pressure': 1013, 'humidity': 89, 'dew_point': 20.51, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 308, 'wind_gust': 1.35, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 22.21, 'feels_like': 22.81, 'pressure': 1012, 'humidity': 89, 'dew_point': 20.31, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 299, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641801600, 'temp': 21.99, 'feels_like': 22.59, 'pressure': 1011, 'humidity': 90, 'dew_point': 20.27, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 299, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641805200, 'temp': 21.88, 'feels_like': 22.5, 'pressure': 1012, 'humidity': 91, 'dew_point': 20.34, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 307, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641808800, 'temp': 21.57, 'feels_like': 22.16, 'pressure': 1012, 'humidity': 91, 'dew_point': 20.04, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 305, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641812400, 'temp': 23.72, 'feels_like': 24.55, 'pressure': 1013, 'humidity': 92, 'dew_point': 22.34, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 301, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641816000, 'temp': 24.72, 'feels_like': 25.6, 'pressure': 1014, 'humidity': 90, 'dew_point': 22.97, 'uvi': 0.46, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 318, 'wind_gust': 1.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641819600, 'temp': 24.72, 'feels_like': 25.39, 'pressure': 1015, 'humidity': 82, 'dew_point': 21.44, 'uvi': 2.05, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 8, 'wind_gust': 2.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 24.72, 'feels_like': 25.26, 'pressure': 1016, 'humidity': 77, 'dew_point': 20.42, 'uvi': 5.01, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 22, 'wind_gust': 3.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641826800, 'temp': 26.72, 'feels_like': 28.39, 'pressure': 1015, 'humidity': 70, 'dew_point': 20.79, 'uvi': 8.54, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2, 'wind_deg': 18, 'wind_gust': 3.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641830400, 'temp': 27.72, 'feels_like': 29.25, 'pressure': 1014, 'humidity': 62, 'dew_point': 19.78, 'uvi': 11.83, 'clouds': 46, 'visibility': 10000, 'wind_speed': 2.21, 'wind_deg': 13, 'wind_gust': 3.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 28.72, 'feels_like': 29.9, 'pressure': 1012, 'humidity': 55, 'dew_point': 18.79, 'uvi': 12.96, 'clouds': 51, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 10, 'wind_gust': 3.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.72, 'feels_like': 31.26, 'pressure': 1011, 'humidity': 54, 'dew_point': 19.42, 'uvi': 11.83, 'clouds': 31, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 12, 'wind_gust': 3.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641841200, 'temp': 30.72, 'feels_like': 33.15, 'pressure': 1010, 'humidity': 55, 'dew_point': 20.64, 'uvi': 8.61, 'clouds': 45, 'visibility': 10000, 'wind_speed': 2.64, 'wind_deg': 12, 'wind_gust': 3.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641844800, 'temp': 28.72, 'feels_like': 29.77, 'pressure': 1009, 'humidity': 54, 'dew_point': 18.5, 'uvi': 5.05, 'clouds': 45, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 16, 'wind_gust': 3.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641848400, 'temp': 27.72, 'feels_like': 28.85, 'pressure': 1008, 'humidity': 58, 'dew_point': 18.71, 'uvi': 2.07, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 20, 'wind_gust': 3.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641852000, 'temp': 27.72, 'feels_like': 30.25, 'pressure': 1009, 'humidity': 71, 'dew_point': 21.98, 'uvi': 0.43, 'clouds': 48, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 20, 'wind_gust': 4.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641855600, 'temp': 26.72, 'feels_like': 29.29, 'pressure': 1010, 'humidity': 82, 'dew_point': 23.39, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 344, 'wind_gust': 3.83, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 70.000000 | 23.990000 | 29.530000 | 85.000000 | 1012.000000 | 0.37 | 26.720000 | 0.000000 | 10000.000000 | 327.000000 | 3.47 | 1.370000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 23.390000 | 26.620000 | 87.000000 | 1013.000000 | 0.19 | 25.720000 | 0.000000 | 10000.000000 | 323.000000 | 2.47 | 1.090000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 52.000000 | 23.390000 | 26.620000 | 87.000000 | 1014.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 315.000000 | 2.08 | 1.220000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 44.000000 | 23.580000 | 26.650000 | 88.000000 | 1014.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 315.000000 | 1.87 | 1.110000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 51.000000 | 20.700000 | 23.420000 | 88.000000 | 1014.000000 |  | 22.790000 | 0.000000 | 10000.000000 | 310.000000 | 1.51 | 1.060000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 57.000000 | 20.530000 | 23.240000 | 88.000000 | 1013.000000 |  | 22.620000 | 0.000000 | 10000.000000 | 305.000000 | 1.4 | 1.140000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 35.000000 | 20.510000 | 23.030000 | 89.000000 | 1013.000000 |  | 22.410000 | 0.000000 | 10000.000000 | 308.000000 | 1.35 | 0.990000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 34.000000 | 20.310000 | 22.810000 | 89.000000 | 1012.000000 | 0.15 | 22.210000 | 0.000000 | 10000.000000 | 299.000000 | 1.3 | 0.790000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 54.000000 | 20.270000 | 22.590000 | 90.000000 | 1011.000000 | 0.17 | 21.990000 | 0.000000 | 10000.000000 | 299.000000 | 1.26 | 0.880000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 51.000000 | 20.340000 | 22.500000 | 91.000000 | 1012.000000 | 0.16 | 21.880000 | 0.000000 | 10000.000000 | 307.000000 | 1.24 | 0.860000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 47.000000 | 20.040000 | 22.160000 | 91.000000 | 1012.000000 | 0.14 | 21.570000 | 0.000000 | 10000.000000 | 305.000000 | 1.19 | 0.820000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 50.000000 | 22.340000 | 24.550000 | 92.000000 | 1013.000000 | 0.21 | 23.720000 | 0.000000 | 10000.000000 | 301.000000 | 1.2 | 1.010000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 28.000000 | 22.970000 | 25.600000 | 90.000000 | 1014.000000 | 0.17 | 24.720000 | 0.460000 | 10000.000000 | 318.000000 | 1.91 | 0.970000 | 500 | Rain | light rain | 10d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 47.000000 | 21.440000 | 25.390000 | 82.000000 | 1015.000000 |  | 24.720000 | 2.050000 | 10000.000000 | 8.000000 | 2.59 | 1.200000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 41.000000 | 20.420000 | 25.260000 | 77.000000 | 1016.000000 | 0.29 | 24.720000 | 5.010000 | 10000.000000 | 22.000000 | 3.41 | 1.610000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 38.000000 | 20.790000 | 28.390000 | 70.000000 | 1015.000000 | 0.29 | 26.720000 | 8.540000 | 10000.000000 | 18.000000 | 3.85 | 2.000000 | 500 | Rain | light rain | 10d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 46.000000 | 19.780000 | 29.250000 | 62.000000 | 1014.000000 |  | 27.720000 | 11.830000 | 10000.000000 | 13.000000 | 3.57 | 2.210000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 51.000000 | 18.790000 | 29.900000 | 55.000000 | 1012.000000 |  | 28.720000 | 12.960000 | 10000.000000 | 10.000000 | 3.61 | 2.450000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 31.000000 | 19.420000 | 31.260000 | 54.000000 | 1011.000000 | 0.1 | 29.720000 | 11.830000 | 10000.000000 | 12.000000 | 3.31 | 2.440000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 45.000000 | 20.640000 | 33.150000 | 55.000000 | 1010.000000 | 0.13 | 30.720000 | 8.610000 | 10000.000000 | 12.000000 | 3.27 | 2.640000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 45.000000 | 18.500000 | 29.770000 | 54.000000 | 1009.000000 | 0.17 | 28.720000 | 5.050000 | 10000.000000 | 16.000000 | 3.2 | 2.560000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 49.000000 | 18.710000 | 28.850000 | 58.000000 | 1008.000000 | 0.22 | 27.720000 | 2.070000 | 10000.000000 | 20.000000 | 3.27 | 2.340000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 48.000000 | 21.980000 | 30.250000 | 71.000000 | 1009.000000 | 0.5 | 27.720000 | 0.430000 | 10000.000000 | 20.000000 | 4.27 | 2.220000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255150 | "GARCIA HACIENDA [21255150]" | 4.855417 | -74.891556 | 350.000000 | Climática Principal | Convencional | Suspendida | 1986-12-15 00:00:00 | 2014-08-28 00:00:00 | Tolima | Lérida | Rucio | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 49.000000 | 23.390000 | 29.290000 | 82.000000 | 1010.000000 | 1.12 | 26.720000 | 0.000000 | 10000.000000 | 344.000000 | 3.83 | 1.700000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21255150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21255150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21255150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255150_OWM_Windspeed_20220111.png)
