
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ARMERO GRANJA [21255090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21255090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.0,-74.89999167) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.0&lon=-74.89999167)


| Parameter | Value |
|---|---|
| Code | 21255090 |
| Name | ARMERO GRANJA [21255090] |
| Latitude, ° | 5.0 |
| Longitude, ° | -74.89999167 |
| Elevation, m | 321 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1986-10-14 19:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Armero (Guayabal) |
| Stream | 0 |
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

### (CNE index 3558) Open Weather values for station 21255090 - ARMERO GRANJA [21255090]

JSON data from API OWM:

```
{'lat': 5, 'lon': -74.9, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813084, 'sunset': 1641855747, 'temp': 25.69, 'feels_like': 25.75, 'pressure': 1009, 'humidity': 55, 'dew_point': 15.98, 'uvi': 5.05, 'clouds': 34, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 21, 'wind_gust': 3.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, 'hourly': [{'dt': 1641772800, 'temp': 27.01, 'feels_like': 30.66, 'pressure': 1012, 'humidity': 89, 'dew_point': 25.04, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 315, 'wind_gust': 2.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.44}}, {'dt': 1641776400, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1013, 'humidity': 89, 'dew_point': 24.05, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 309, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641780000, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1014, 'humidity': 89, 'dew_point': 24.05, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 313, 'wind_gust': 1.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1014, 'humidity': 90, 'dew_point': 24.24, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 314, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.91, 'feels_like': 23.63, 'pressure': 1014, 'humidity': 91, 'dew_point': 21.36, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 302, 'wind_gust': 1.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 22.75, 'feels_like': 23.46, 'pressure': 1014, 'humidity': 91, 'dew_point': 21.2, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 299, 'wind_gust': 1.36, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 22.45, 'feels_like': 23.18, 'pressure': 1013, 'humidity': 93, 'dew_point': 21.26, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 299, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.42, 'feels_like': 23.15, 'pressure': 1012, 'humidity': 93, 'dew_point': 21.23, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 298, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 22.47, 'feels_like': 23.2, 'pressure': 1011, 'humidity': 93, 'dew_point': 21.28, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 303, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641805200, 'temp': 22.47, 'feels_like': 23.17, 'pressure': 1012, 'humidity': 92, 'dew_point': 21.11, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 318, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641808800, 'temp': 22.09, 'feels_like': 22.76, 'pressure': 1012, 'humidity': 92, 'dew_point': 20.73, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 314, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 25.69, 'feels_like': 26.74, 'pressure': 1013, 'humidity': 93, 'dew_point': 24.47, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 301, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641816000, 'temp': 25.69, 'feels_like': 26.66, 'pressure': 1014, 'humidity': 90, 'dew_point': 23.93, 'uvi': 0.46, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 311, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641819600, 'temp': 25.69, 'feels_like': 26.46, 'pressure': 1015, 'humidity': 82, 'dew_point': 22.39, 'uvi': 2.05, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 10, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641823200, 'temp': 26.69, 'feels_like': 28.84, 'pressure': 1016, 'humidity': 77, 'dew_point': 22.32, 'uvi': 5.01, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 17, 'wind_gust': 3.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641826800, 'temp': 28.69, 'feels_like': 32.23, 'pressure': 1015, 'humidity': 71, 'dew_point': 22.91, 'uvi': 8.54, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 18, 'wind_gust': 3.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641830400, 'temp': 31.69, 'feels_like': 37.55, 'pressure': 1014, 'humidity': 64, 'dew_point': 24.04, 'uvi': 11.83, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 16, 'wind_gust': 3.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 28.69, 'feels_like': 30.25, 'pressure': 1013, 'humidity': 58, 'dew_point': 19.61, 'uvi': 12.96, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 14, 'wind_gust': 3.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 26.69, 'feels_like': 27.46, 'pressure': 1011, 'humidity': 56, 'dew_point': 17.19, 'uvi': 11.83, 'clouds': 25, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 12, 'wind_gust': 3.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641841200, 'temp': 26.69, 'feels_like': 27.52, 'pressure': 1010, 'humidity': 57, 'dew_point': 17.47, 'uvi': 8.61, 'clouds': 35, 'visibility': 10000, 'wind_speed': 2.77, 'wind_deg': 14, 'wind_gust': 3.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641844800, 'temp': 25.69, 'feels_like': 25.75, 'pressure': 1009, 'humidity': 55, 'dew_point': 15.98, 'uvi': 5.05, 'clouds': 34, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 21, 'wind_gust': 3.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641848400, 'temp': 26.69, 'feels_like': 27.64, 'pressure': 1008, 'humidity': 59, 'dew_point': 18.02, 'uvi': 2.07, 'clouds': 41, 'visibility': 10000, 'wind_speed': 2.58, 'wind_deg': 27, 'wind_gust': 3.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641852000, 'temp': 26.69, 'feels_like': 28.48, 'pressure': 1009, 'humidity': 72, 'dew_point': 21.22, 'uvi': 0.43, 'clouds': 43, 'visibility': 10000, 'wind_speed': 2.24, 'wind_deg': 29, 'wind_gust': 4.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641855600, 'temp': 25.69, 'feels_like': 26.51, 'pressure': 1010, 'humidity': 84, 'dew_point': 22.78, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 355, 'wind_gust': 3.46, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.06}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 89.000000 | 25.040000 | 30.660000 | 89.000000 | 1012.000000 | 0.44 | 27.010000 | 0.000000 | 10000.000000 | 315.000000 | 2.31 | 1.080000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 93.000000 | 24.050000 | 26.010000 | 89.000000 | 1013.000000 | 0.19 | 26.010000 | 0.000000 | 10000.000000 | 309.000000 | 1.72 | 0.940000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 59.000000 | 24.050000 | 26.010000 | 89.000000 | 1014.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 313.000000 | 1.76 | 0.990000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 52.000000 | 24.240000 | 26.010000 | 90.000000 | 1014.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 314.000000 | 1.34 | 0.910000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 49.000000 | 21.360000 | 23.630000 | 91.000000 | 1014.000000 |  | 22.910000 | 0.000000 | 10000.000000 | 302.000000 | 1.45 | 0.950000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 49.000000 | 21.200000 | 23.460000 | 91.000000 | 1014.000000 |  | 22.750000 | 0.000000 | 10000.000000 | 299.000000 | 1.36 | 1.140000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 63.000000 | 21.260000 | 23.180000 | 93.000000 | 1013.000000 |  | 22.450000 | 0.000000 | 10000.000000 | 299.000000 | 1.32 | 1.080000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 64.000000 | 21.230000 | 23.150000 | 93.000000 | 1012.000000 | 0.19 | 22.420000 | 0.000000 | 10000.000000 | 298.000000 | 1.27 | 0.800000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 82.000000 | 21.280000 | 23.200000 | 93.000000 | 1011.000000 | 0.21 | 22.470000 | 0.000000 | 10000.000000 | 303.000000 | 1.12 | 0.770000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 74.000000 | 21.110000 | 23.170000 | 92.000000 | 1012.000000 | 0.15 | 22.470000 | 0.000000 | 10000.000000 | 318.000000 | 1.09 | 0.670000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 66.000000 | 20.730000 | 22.760000 | 92.000000 | 1012.000000 |  | 22.090000 | 0.000000 | 10000.000000 | 314.000000 | 1.09 | 0.730000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 68.000000 | 24.470000 | 26.740000 | 93.000000 | 1013.000000 | 0.16 | 25.690000 | 0.000000 | 10000.000000 | 301.000000 | 1.27 | 1.010000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 38.000000 | 23.930000 | 26.660000 | 90.000000 | 1014.000000 | 0.14 | 25.690000 | 0.460000 | 10000.000000 | 311.000000 | 1.82 | 0.890000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 62.000000 | 22.390000 | 26.460000 | 82.000000 | 1015.000000 | 0.14 | 25.690000 | 2.050000 | 10000.000000 | 10.000000 | 2.32 | 1.120000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 54.000000 | 22.320000 | 28.840000 | 77.000000 | 1016.000000 | 0.26 | 26.690000 | 5.010000 | 10000.000000 | 17.000000 | 3.11 | 1.620000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 52.000000 | 22.910000 | 32.230000 | 71.000000 | 1015.000000 | 0.33 | 28.690000 | 8.540000 | 10000.000000 | 18.000000 | 3.59 | 2.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 60.000000 | 24.040000 | 37.550000 | 64.000000 | 1014.000000 | 0.11 | 31.690000 | 11.830000 | 10000.000000 | 16.000000 | 3.46 | 2.250000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 58.000000 | 19.610000 | 30.250000 | 58.000000 | 1013.000000 |  | 28.690000 | 12.960000 | 10000.000000 | 14.000000 | 3.41 | 2.530000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 25.000000 | 17.190000 | 27.460000 | 56.000000 | 1011.000000 | 0.11 | 26.690000 | 11.830000 | 10000.000000 | 12.000000 | 3.1 | 2.460000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 35.000000 | 17.470000 | 27.520000 | 57.000000 | 1010.000000 | 0.18 | 26.690000 | 8.610000 | 10000.000000 | 14.000000 | 3.29 | 2.770000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 34.000000 | 15.980000 | 25.750000 | 55.000000 | 1009.000000 | 0.1 | 25.690000 | 5.050000 | 10000.000000 | 21.000000 | 3.26 | 2.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 41.000000 | 18.020000 | 27.640000 | 59.000000 | 1008.000000 | 0.13 | 26.690000 | 2.070000 | 10000.000000 | 27.000000 | 3.36 | 2.580000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 43.000000 | 21.220000 | 28.480000 | 72.000000 | 1009.000000 | 0.36 | 26.690000 | 0.430000 | 10000.000000 | 29.000000 | 4.49 | 2.240000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21255090 | "ARMERO GRANJA [21255090]" | 5.000000 | -74.899992 | 321.000000 | Climática Principal | Convencional | Activa | 1986-10-14 19:00:00 | NaT | Tolima | Armero (Guayabal) | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Lagunilla y Otros Directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 49.000000 | 22.780000 | 26.510000 | 84.000000 | 1010.000000 | 1.06 | 25.690000 | 0.000000 | 10000.000000 | 355.000000 | 3.46 | 1.430000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21255090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21255090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21255090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21255090_OWM_Windspeed_20220111.png)
