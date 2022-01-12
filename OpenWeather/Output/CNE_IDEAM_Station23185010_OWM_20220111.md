
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA LEIVA [23185010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23185010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.45611111,-73.53722222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.45611111&lon=-73.53722222)


| Parameter | Value |
|---|---|
| Code | 23185010 |
| Name | VILLA LEIVA [23185010] |
| Latitude, ° | 7.45611111 |
| Longitude, ° | -73.53722222 |
| Elevation, m | 328 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1966-01-15 00:00:00 |
| Suspension date | NaT |
| State | Santander |
| County | Sabana De Torres |
| Stream | Atrato |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Lebrija y otros directos al Magdalena |

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

### (CNE index 2927) Open Weather values for station 23185010 - VILLA LEIVA [23185010]

JSON data from API OWM:

```
{'lat': 7.4561, 'lon': -73.5372, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812997, 'sunset': 1641855180, 'temp': 30.72, 'feels_like': 31.98, 'pressure': 1007, 'humidity': 49, 'dew_point': 18.78, 'uvi': 4.23, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 291, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.72, 'feels_like': 28.26, 'pressure': 1009, 'humidity': 68, 'dew_point': 20.32, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 144, 'wind_gust': 1.79, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.72, 'feels_like': 26.2, 'pressure': 1010, 'humidity': 71, 'dew_point': 20.07, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 143, 'wind_gust': 1.53, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 25.72, 'feels_like': 26.25, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.52, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 179, 'wind_gust': 0.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.72, 'feels_like': 26.28, 'pressure': 1011, 'humidity': 74, 'dew_point': 20.74, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 208, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 26.72, 'feels_like': 28.83, 'pressure': 1011, 'humidity': 76, 'dew_point': 22.14, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 90, 'wind_gust': 0.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 26.72, 'feels_like': 28.9, 'pressure': 1011, 'humidity': 77, 'dew_point': 22.35, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 120, 'wind_gust': 0.47, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.8, 'feels_like': 23.2, 'pressure': 1010, 'humidity': 79, 'dew_point': 18.97, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 150, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641798000, 'temp': 22.43, 'feels_like': 22.82, 'pressure': 1010, 'humidity': 80, 'dew_point': 18.81, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 138, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.14, 'feels_like': 22.5, 'pressure': 1010, 'humidity': 80, 'dew_point': 18.53, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 87, 'wind_gust': 0.37, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 21.94, 'feels_like': 22.25, 'pressure': 1010, 'humidity': 79, 'dew_point': 18.13, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 357, 'wind_gust': 0.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 21.75, 'feels_like': 22.04, 'pressure': 1011, 'humidity': 79, 'dew_point': 17.95, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 341, 'wind_gust': 0.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 25.72, 'feels_like': 26.41, 'pressure': 1012, 'humidity': 79, 'dew_point': 21.8, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 325, 'wind_gust': 0.82, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 25.72, 'feels_like': 26.36, 'pressure': 1013, 'humidity': 77, 'dew_point': 21.38, 'uvi': 0.44, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 354, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.72, 'feels_like': 28.46, 'pressure': 1014, 'humidity': 71, 'dew_point': 21.02, 'uvi': 1.89, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 10, 'wind_gust': 0.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.72, 'feels_like': 31.31, 'pressure': 1015, 'humidity': 65, 'dew_point': 21.49, 'uvi': 4.6, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 235, 'wind_gust': 0.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.72, 'feels_like': 32.69, 'pressure': 1014, 'humidity': 62, 'dew_point': 21.66, 'uvi': 7.77, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 253, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.72, 'feels_like': 31.94, 'pressure': 1013, 'humidity': 58, 'dew_point': 20.57, 'uvi': 10.49, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 260, 'wind_gust': 1.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 31.72, 'feels_like': 34.81, 'pressure': 1012, 'humidity': 54, 'dew_point': 21.27, 'uvi': 11.38, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 282, 'wind_gust': 1.09, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.72, 'feels_like': 33.86, 'pressure': 1010, 'humidity': 50, 'dew_point': 20.02, 'uvi': 10.22, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 295, 'wind_gust': 1.13, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 31.72, 'feels_like': 33.63, 'pressure': 1009, 'humidity': 49, 'dew_point': 19.69, 'uvi': 7.45, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 293, 'wind_gust': 1.48, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 30.72, 'feels_like': 31.98, 'pressure': 1007, 'humidity': 49, 'dew_point': 18.78, 'uvi': 4.23, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 291, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 30.72, 'feels_like': 32.16, 'pressure': 1007, 'humidity': 50, 'dew_point': 19.11, 'uvi': 1.66, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 277, 'wind_gust': 1.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 29.72, 'feels_like': 32.31, 'pressure': 1008, 'humidity': 60, 'dew_point': 21.13, 'uvi': 0.32, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 130, 'wind_gust': 0.66, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 27.72, 'feels_like': 29.46, 'pressure': 1008, 'humidity': 64, 'dew_point': 20.29, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 128, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 25.000000 | 20.320000 | 28.260000 | 68.000000 | 1009.000000 |  | 26.720000 | 0.000000 | 10000.000000 | 144.000000 | 1.79 | 1.790000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 28.000000 | 20.070000 | 26.200000 | 71.000000 | 1010.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 143.000000 | 1.53 | 1.500000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 59.000000 | 20.520000 | 26.250000 | 73.000000 | 1011.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 179.000000 | 0.59 | 0.420000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 58.000000 | 20.740000 | 26.280000 | 74.000000 | 1011.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 208.000000 | 0.7 | 0.570000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 68.000000 | 22.140000 | 28.830000 | 76.000000 | 1011.000000 |  | 26.720000 | 0.000000 | 10000.000000 | 90.000000 | 0.46 | 0.230000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 71.000000 | 22.350000 | 28.900000 | 77.000000 | 1011.000000 |  | 26.720000 | 0.000000 | 10000.000000 | 120.000000 | 0.47 | 0.440000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 60.000000 | 18.970000 | 23.200000 | 79.000000 | 1010.000000 | 0.11 | 22.800000 | 0.000000 | 10000.000000 | 150.000000 | 1.12 | 1.110000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 68.000000 | 18.810000 | 22.820000 | 80.000000 | 1010.000000 |  | 22.430000 | 0.000000 | 10000.000000 | 138.000000 | 0.7 | 0.660000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 43.000000 | 18.530000 | 22.500000 | 80.000000 | 1010.000000 |  | 22.140000 | 0.000000 | 10000.000000 | 87.000000 | 0.37 | 0.200000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 33.000000 | 18.130000 | 22.250000 | 79.000000 | 1010.000000 |  | 21.940000 | 0.000000 | 10000.000000 | 357.000000 | 0.6 | 0.480000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 29.000000 | 17.950000 | 22.040000 | 79.000000 | 1011.000000 |  | 21.750000 | 0.000000 | 10000.000000 | 341.000000 | 0.72 | 0.680000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 37.000000 | 21.800000 | 26.410000 | 79.000000 | 1012.000000 |  | 25.720000 | 0.000000 | 10000.000000 | 325.000000 | 0.82 | 0.770000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 89.000000 | 21.380000 | 26.360000 | 77.000000 | 1013.000000 |  | 25.720000 | 0.440000 | 10000.000000 | 354.000000 | 0.73 | 0.590000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 95.000000 | 21.020000 | 28.460000 | 71.000000 | 1014.000000 |  | 26.720000 | 1.890000 | 10000.000000 | 10.000000 | 0.6 | 0.190000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 91.000000 | 21.490000 | 31.310000 | 65.000000 | 1015.000000 |  | 28.720000 | 4.600000 | 10000.000000 | 235.000000 | 0.69 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 86.000000 | 21.660000 | 32.690000 | 62.000000 | 1014.000000 |  | 29.720000 | 7.770000 | 10000.000000 | 253.000000 | 1.05 | 0.890000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 73.000000 | 20.570000 | 31.940000 | 58.000000 | 1013.000000 |  | 29.720000 | 10.490000 | 10000.000000 | 260.000000 | 1.2 | 1.230000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 66.000000 | 21.270000 | 34.810000 | 54.000000 | 1012.000000 |  | 31.720000 | 11.380000 | 10000.000000 | 282.000000 | 1.09 | 1.460000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 19.000000 | 20.020000 | 33.860000 | 50.000000 | 1010.000000 |  | 31.720000 | 10.220000 | 10000.000000 | 295.000000 | 1.13 | 1.460000 | 801 | Clouds | few clouds | 02d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 24.000000 | 19.690000 | 33.630000 | 49.000000 | 1009.000000 |  | 31.720000 | 7.450000 | 10000.000000 | 293.000000 | 1.48 | 1.700000 | 801 | Clouds | few clouds | 02d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 38.000000 | 18.780000 | 31.980000 | 49.000000 | 1007.000000 |  | 30.720000 | 4.230000 | 10000.000000 | 291.000000 | 1.43 | 1.420000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 34.000000 | 19.110000 | 32.160000 | 50.000000 | 1007.000000 |  | 30.720000 | 1.660000 | 10000.000000 | 277.000000 | 1.06 | 0.790000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 46.000000 | 21.130000 | 32.310000 | 60.000000 | 1008.000000 |  | 29.720000 | 0.320000 | 10000.000000 | 130.000000 | 0.66 | 0.100000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23185010 | "VILLA LEIVA [23185010]" | 7.456111 | -73.537222 | 328.000000 | Climática Principal | Convencional | Activa | 1966-01-15 00:00:00 | NaT | Santander | Sabana De Torres | Atrato | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 57.000000 | 20.290000 | 29.460000 | 64.000000 | 1008.000000 |  | 27.720000 | 0.000000 | 10000.000000 | 128.000000 | 0.81 | 0.790000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station23185010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23185010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23185010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23185010_OWM_Windspeed_20220111.png)
