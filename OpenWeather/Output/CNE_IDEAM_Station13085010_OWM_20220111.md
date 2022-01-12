
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - DOCTRINA LA [13085010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13085010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.29722222,-75.89277778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.29722222&lon=-75.89277778)


| Parameter | Value |
|---|---|
| Code | 13085010 |
| Name | DOCTRINA LA [13085010] |
| Latitude, ° | 9.29722222 |
| Longitude, ° | -75.89277778 |
| Elevation, m | 20 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1968-01-15 00:00:00 |
| Suspension date | NaT |
| State | Córdoba |
| County | Lorica |
| Stream | Lago La Pastora |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Bajo Sinú |

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

### (CNE index 2595) Open Weather values for station 13085010 - DOCTRINA LA [13085010]

JSON data from API OWM:

```
{'lat': 9.2972, 'lon': -75.8928, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813743, 'sunset': 1641855565, 'temp': 32.05, 'feels_like': 36.59, 'pressure': 1009, 'humidity': 58, 'dew_point': 22.75, 'uvi': 3.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 279, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.05, 'feels_like': 30.25, 'pressure': 1010, 'humidity': 84, 'dew_point': 24.11, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.87, 'wind_deg': 319, 'wind_gust': 6.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 83, 'dew_point': 22.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.3, 'wind_deg': 326, 'wind_gust': 7.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.05, 'feels_like': 25.73, 'pressure': 1012, 'humidity': 81, 'dew_point': 21.56, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 4.51, 'wind_deg': 337, 'wind_gust': 7.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1012, 'humidity': 79, 'dew_point': 22.12, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 4.4, 'wind_deg': 347, 'wind_gust': 7.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 80, 'dew_point': 22.33, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.78, 'wind_deg': 348, 'wind_gust': 6.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 26.05, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 81, 'dew_point': 22.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.24, 'wind_deg': 346, 'wind_gust': 4.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.34, 'feels_like': 26.04, 'pressure': 1010, 'humidity': 81, 'dew_point': 21.84, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.71, 'wind_deg': 335, 'wind_gust': 3.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 25.21, 'feels_like': 25.9, 'pressure': 1010, 'humidity': 81, 'dew_point': 21.72, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 329, 'wind_gust': 3.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 25.04, 'feels_like': 25.74, 'pressure': 1009, 'humidity': 82, 'dew_point': 21.75, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 328, 'wind_gust': 2.76, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 24.77, 'feels_like': 25.47, 'pressure': 1010, 'humidity': 83, 'dew_point': 21.69, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 334, 'wind_gust': 2.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 24.48, 'feels_like': 25.18, 'pressure': 1010, 'humidity': 84, 'dew_point': 21.6, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 19, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641812400, 'temp': 23.05, 'feels_like': 23.63, 'pressure': 1011, 'humidity': 85, 'dew_point': 20.39, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 102, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641816000, 'temp': 23.05, 'feels_like': 23.6, 'pressure': 1012, 'humidity': 84, 'dew_point': 20.2, 'uvi': 0.29, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 116, 'wind_gust': 2.46, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 25.05, 'feels_like': 25.7, 'pressure': 1013, 'humidity': 80, 'dew_point': 21.36, 'uvi': 1.43, 'clouds': 17, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 129, 'wind_gust': 4.08, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.05, 'feels_like': 31.32, 'pressure': 1014, 'humidity': 74, 'dew_point': 22.98, 'uvi': 3.69, 'clouds': 54, 'visibility': 10000, 'wind_speed': 3.77, 'wind_deg': 130, 'wind_gust': 4.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.05, 'feels_like': 32.29, 'pressure': 1014, 'humidity': 67, 'dew_point': 22.3, 'uvi': 6.57, 'clouds': 69, 'visibility': 10000, 'wind_speed': 3.45, 'wind_deg': 131, 'wind_gust': 3.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 30.05, 'feels_like': 33.55, 'pressure': 1013, 'humidity': 63, 'dew_point': 22.23, 'uvi': 8.01, 'clouds': 77, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 137, 'wind_gust': 3.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 31.05, 'feels_like': 34.95, 'pressure': 1012, 'humidity': 60, 'dew_point': 22.37, 'uvi': 8.92, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 136, 'wind_gust': 2.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 32.05, 'feels_like': 36.3, 'pressure': 1011, 'humidity': 57, 'dew_point': 22.46, 'uvi': 8.21, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 163, 'wind_gust': 1.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 32.05, 'feels_like': 36.02, 'pressure': 1010, 'humidity': 56, 'dew_point': 22.17, 'uvi': 6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 228, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 32.05, 'feels_like': 36.59, 'pressure': 1009, 'humidity': 58, 'dew_point': 22.75, 'uvi': 3.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 279, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 31.05, 'feels_like': 36.28, 'pressure': 1009, 'humidity': 65, 'dew_point': 23.69, 'uvi': 1.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 298, 'wind_gust': 2.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.05, 'feels_like': 35.66, 'pressure': 1009, 'humidity': 72, 'dew_point': 24.45, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.11, 'wind_deg': 314, 'wind_gust': 4.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.05, 'feels_like': 31.76, 'pressure': 1010, 'humidity': 77, 'dew_point': 23.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.14, 'wind_deg': 323, 'wind_gust': 4.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 00:00:00 | 99.000000 | 24.110000 | 30.250000 | 84.000000 | 1010.000000 |  | 27.050000 | 0.000000 | 10000.000000 | 319.000000 | 6.46 | 3.870000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 22.940000 | 26.050000 | 83.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 326.000000 | 7.06 | 4.300000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 21.560000 | 25.730000 | 81.000000 | 1012.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 337.000000 | 7.63 | 4.510000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 22.120000 | 26.050000 | 79.000000 | 1012.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 347.000000 | 7.46 | 4.400000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 22.330000 | 26.050000 | 80.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 348.000000 | 6.25 | 3.780000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 22.530000 | 26.050000 | 81.000000 | 1011.000000 |  | 26.050000 | 0.000000 | 10000.000000 | 346.000000 | 4.95 | 3.240000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 21.840000 | 26.040000 | 81.000000 | 1010.000000 |  | 25.340000 | 0.000000 | 10000.000000 | 335.000000 | 3.71 | 2.710000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 07:00:00 | 52.000000 | 21.720000 | 25.900000 | 81.000000 | 1010.000000 |  | 25.210000 | 0.000000 | 10000.000000 | 329.000000 | 3.29 | 2.340000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 08:00:00 | 40.000000 | 21.750000 | 25.740000 | 82.000000 | 1009.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 328.000000 | 2.76 | 2.020000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 09:00:00 | 43.000000 | 21.690000 | 25.470000 | 83.000000 | 1010.000000 |  | 24.770000 | 0.000000 | 10000.000000 | 334.000000 | 2.24 | 1.630000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 10:00:00 | 46.000000 | 21.600000 | 25.180000 | 84.000000 | 1010.000000 | 0.15 | 24.480000 | 0.000000 | 10000.000000 | 19.000000 | 1.26 | 0.690000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 11:00:00 | 44.000000 | 20.390000 | 23.630000 | 85.000000 | 1011.000000 | 0.1 | 23.050000 | 0.000000 | 10000.000000 | 102.000000 | 1.34 | 0.870000 | 500 | Rain | light rain | 10n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 12:00:00 | 9.000000 | 20.200000 | 23.600000 | 84.000000 | 1012.000000 |  | 23.050000 | 0.290000 | 10000.000000 | 116.000000 | 2.46 | 1.960000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 13:00:00 | 17.000000 | 21.360000 | 25.700000 | 80.000000 | 1013.000000 |  | 25.050000 | 1.430000 | 10000.000000 | 129.000000 | 4.08 | 3.270000 | 801 | Clouds | few clouds | 02d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 14:00:00 | 54.000000 | 22.980000 | 31.320000 | 74.000000 | 1014.000000 |  | 28.050000 | 3.690000 | 10000.000000 | 130.000000 | 4.33 | 3.770000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 15:00:00 | 69.000000 | 22.300000 | 32.290000 | 67.000000 | 1014.000000 |  | 29.050000 | 6.570000 | 10000.000000 | 131.000000 | 3.89 | 3.450000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 22.230000 | 33.550000 | 63.000000 | 1013.000000 |  | 30.050000 | 8.010000 | 10000.000000 | 137.000000 | 3.37 | 3.010000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 17:00:00 | 82.000000 | 22.370000 | 34.950000 | 60.000000 | 1012.000000 |  | 31.050000 | 8.920000 | 10000.000000 | 136.000000 | 2.72 | 2.230000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 22.460000 | 36.300000 | 57.000000 | 1011.000000 |  | 32.050000 | 8.210000 | 10000.000000 | 163.000000 | 1.8 | 1.350000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 22.170000 | 36.020000 | 56.000000 | 1010.000000 |  | 32.050000 | 6.000000 | 10000.000000 | 228.000000 | 1.3 | 0.960000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 22.750000 | 36.590000 | 58.000000 | 1009.000000 |  | 32.050000 | 3.520000 | 10000.000000 | 279.000000 | 1.45 | 1.720000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 23.690000 | 36.280000 | 65.000000 | 1009.000000 |  | 31.050000 | 1.430000 | 10000.000000 | 298.000000 | 2.13 | 2.420000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 24.450000 | 35.660000 | 72.000000 | 1009.000000 |  | 30.050000 | 0.270000 | 10000.000000 | 314.000000 | 4.01 | 3.110000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085010 | "DOCTRINA LA [13085010]" | 9.297222 | -75.892778 | 20.000000 | Climática Principal | Convencional | Activa | 1968-01-15 00:00:00 | NaT | Córdoba | Lorica | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 23.640000 | 31.760000 | 77.000000 | 1010.000000 |  | 28.050000 | 0.000000 | 10000.000000 | 323.000000 | 4.99 | 3.140000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station13085010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13085010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13085010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085010_OWM_Windspeed_20220111.png)
