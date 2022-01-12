
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - REPRESA URRA [13015040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13015040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.01416667,-76.20305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.01416667&lon=-76.20305556)


| Parameter | Value |
|---|---|
| Code | 13015040 |
| Name | REPRESA URRA [13015040] |
| Latitude, ° | 8.01416667 |
| Longitude, ° | -76.20305556 |
| Elevation, m | 300 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 2004-11-15 00:00:00 |
| Suspension date | NaT |
| State | Córdoba |
| County | Tierralta |
| Stream | Cauca |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Medio Sinú |

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

### (CNE index 2582) Open Weather values for station 13015040 - REPRESA URRA [13015040]

JSON data from API OWM:

```
{'lat': 8.0142, 'lon': -76.2031, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813691, 'sunset': 1641855766, 'temp': 27.49, 'feels_like': 31.5, 'pressure': 1010, 'humidity': 85, 'dew_point': 24.74, 'uvi': 3.34, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 313, 'wind_gust': 3.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, 'hourly': [{'dt': 1641772800, 'temp': 25.49, 'feels_like': 26.42, 'pressure': 1011, 'humidity': 89, 'dew_point': 23.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 325, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.49, 'feels_like': 26.47, 'pressure': 1012, 'humidity': 91, 'dew_point': 23.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 308, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.46, 'feels_like': 24.32, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.44, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 294, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.21, 'feels_like': 24.07, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.36, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 262, 'wind_gust': 0.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.97, 'feels_like': 23.83, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.3, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 259, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.71, 'feels_like': 23.54, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.04, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 287, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 22.4, 'feels_like': 23.23, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.9, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 271, 'wind_gust': 0.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641798000, 'temp': 22.13, 'feels_like': 22.93, 'pressure': 1011, 'humidity': 97, 'dew_point': 21.63, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 276, 'wind_gust': 0.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641801600, 'temp': 22, 'feels_like': 22.79, 'pressure': 1011, 'humidity': 97, 'dew_point': 21.5, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 220, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 21.96, 'feels_like': 22.74, 'pressure': 1011, 'humidity': 97, 'dew_point': 21.46, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 205, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.94, 'feels_like': 22.72, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.44, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 206, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641812400, 'temp': 24.49, 'feels_like': 25.53, 'pressure': 1012, 'humidity': 97, 'dew_point': 23.98, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 209, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.49, 'feels_like': 25.48, 'pressure': 1013, 'humidity': 95, 'dew_point': 23.64, 'uvi': 0.22, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 202, 'wind_gust': 1.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 24.49, 'feels_like': 25.32, 'pressure': 1014, 'humidity': 89, 'dew_point': 22.56, 'uvi': 1.13, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 203, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.49, 'feels_like': 26.13, 'pressure': 1015, 'humidity': 78, 'dew_point': 21.37, 'uvi': 2.94, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 226, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641826800, 'temp': 26.49, 'feels_like': 26.49, 'pressure': 1014, 'humidity': 70, 'dew_point': 20.57, 'uvi': 5.26, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 284, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641830400, 'temp': 26.49, 'feels_like': 26.49, 'pressure': 1014, 'humidity': 65, 'dew_point': 19.38, 'uvi': 7.71, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 321, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 27.49, 'feels_like': 29.1, 'pressure': 1013, 'humidity': 64, 'dew_point': 20.07, 'uvi': 8.63, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 341, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641837600, 'temp': 27.49, 'feels_like': 29.71, 'pressure': 1012, 'humidity': 70, 'dew_point': 21.53, 'uvi': 8, 'clouds': 100, 'visibility': 9586, 'wind_speed': 2.05, 'wind_deg': 330, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641841200, 'temp': 27.49, 'feels_like': 31.11, 'pressure': 1011, 'humidity': 82, 'dew_point': 24.14, 'uvi': 5.62, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 320, 'wind_gust': 2.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641844800, 'temp': 27.49, 'feels_like': 31.5, 'pressure': 1010, 'humidity': 85, 'dew_point': 24.74, 'uvi': 3.34, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 313, 'wind_gust': 3.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641848400, 'temp': 27.49, 'feels_like': 31.5, 'pressure': 1009, 'humidity': 85, 'dew_point': 24.74, 'uvi': 1.39, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 315, 'wind_gust': 3.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641852000, 'temp': 26.49, 'feels_like': 26.49, 'pressure': 1010, 'humidity': 90, 'dew_point': 24.71, 'uvi': 0.33, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 323, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641855600, 'temp': 25.49, 'feels_like': 26.5, 'pressure': 1011, 'humidity': 92, 'dew_point': 24.09, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 314, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 23.540000 | 26.420000 | 89.000000 | 1011.000000 |  | 25.490000 | 0.000000 | 10000.000000 | 325.000000 | 0.68 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 23.910000 | 26.470000 | 91.000000 | 1012.000000 |  | 25.490000 | 0.000000 | 10000.000000 | 308.000000 | 0.87 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 22.440000 | 24.320000 | 94.000000 | 1013.000000 |  | 23.460000 | 0.000000 | 10000.000000 | 294.000000 | 0.51 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 22.360000 | 24.070000 | 95.000000 | 1013.000000 |  | 23.210000 | 0.000000 | 10000.000000 | 262.000000 | 0.49 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 22.300000 | 23.830000 | 96.000000 | 1012.000000 |  | 22.970000 | 0.000000 | 10000.000000 | 259.000000 | 0.57 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 22.040000 | 23.540000 | 96.000000 | 1012.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 287.000000 | 0.56 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 21.900000 | 23.230000 | 97.000000 | 1012.000000 | 0.27 | 22.400000 | 0.000000 | 10000.000000 | 271.000000 | 0.55 | 0.480000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 07:00:00 | 91.000000 | 21.630000 | 22.930000 | 97.000000 | 1011.000000 | 0.1 | 22.130000 | 0.000000 | 10000.000000 | 276.000000 | 0.39 | 0.390000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 08:00:00 | 66.000000 | 21.500000 | 22.790000 | 97.000000 | 1011.000000 | 0.15 | 22.000000 | 0.000000 | 10000.000000 | 220.000000 | 0.91 | 0.890000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 09:00:00 | 55.000000 | 21.460000 | 22.740000 | 97.000000 | 1011.000000 |  | 21.960000 | 0.000000 | 10000.000000 | 205.000000 | 1.27 | 1.310000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 10:00:00 | 63.000000 | 21.440000 | 22.720000 | 97.000000 | 1012.000000 | 0.14 | 21.940000 | 0.000000 | 10000.000000 | 206.000000 | 1.31 | 1.330000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 23.980000 | 25.530000 | 97.000000 | 1012.000000 |  | 24.490000 | 0.000000 | 10000.000000 | 209.000000 | 1.27 | 1.280000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 12:00:00 | 76.000000 | 23.640000 | 25.480000 | 95.000000 | 1013.000000 |  | 24.490000 | 0.220000 | 10000.000000 | 202.000000 | 1.49 | 1.180000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 13:00:00 | 88.000000 | 22.560000 | 25.320000 | 89.000000 | 1014.000000 |  | 24.490000 | 1.130000 | 10000.000000 | 203.000000 | 1.49 | 1.020000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 21.370000 | 26.130000 | 78.000000 | 1015.000000 | 0.17 | 25.490000 | 2.940000 | 10000.000000 | 226.000000 | 1.09 | 0.830000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 15:00:00 | 96.000000 | 20.570000 | 26.490000 | 70.000000 | 1014.000000 | 0.19 | 26.490000 | 5.260000 | 10000.000000 | 284.000000 | 1.01 | 0.600000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 16:00:00 | 97.000000 | 19.380000 | 26.490000 | 65.000000 | 1014.000000 | 0.12 | 26.490000 | 7.710000 | 10000.000000 | 321.000000 | 0.89 | 0.860000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 20.070000 | 29.100000 | 64.000000 | 1013.000000 | 0.18 | 27.490000 | 8.630000 | 10000.000000 | 341.000000 | 1.26 | 1.610000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 21.530000 | 29.710000 | 70.000000 | 1012.000000 | 0.48 | 27.490000 | 8.000000 | 9586.000000 | 330.000000 | 1.92 | 2.050000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 24.140000 | 31.110000 | 82.000000 | 1011.000000 | 0.63 | 27.490000 | 5.620000 | 10000.000000 | 320.000000 | 2.99 | 1.930000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 24.740000 | 31.500000 | 85.000000 | 1010.000000 | 0.52 | 27.490000 | 3.340000 | 10000.000000 | 313.000000 | 3.04 | 1.550000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 21:00:00 | 92.000000 | 24.740000 | 31.500000 | 85.000000 | 1009.000000 | 0.56 | 27.490000 | 1.390000 | 10000.000000 | 315.000000 | 3.2 | 1.650000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 24.710000 | 26.490000 | 90.000000 | 1010.000000 | 0.35 | 26.490000 | 0.330000 | 10000.000000 | 323.000000 | 2.04 | 1.200000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 13015040 | "REPRESA URRA [13015040]" | 8.014167 | -76.203056 | 300.000000 | Climática Principal | Convencional | Activa | 2004-11-15 00:00:00 | NaT | Córdoba | Tierralta | Cauca | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Medio Sinú | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 24.090000 | 26.500000 | 92.000000 | 1011.000000 | 0.56 | 25.490000 | 0.000000 | 10000.000000 | 314.000000 | 1.19 | 1.090000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station13015040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13015040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13015040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13015040_OWM_Windspeed_20220111.png)
