
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLETA - AUT [23065180] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23065180_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.01686111,-74.47097222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.01686111&lon=-74.47097222)


| Parameter | Value |
|---|---|
| Code | 23065180 |
| Name | VILLETA - AUT [23065180] |
| Latitude, ° | 5.01686111 |
| Longitude, ° | -74.47097222 |
| Elevation, m | 878 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-10 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Villeta |
| Stream | San Juan |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Negro |

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

### (CNE index 129) Open Weather values for station 23065180 - VILLETA - AUT [23065180]

JSON data from API OWM:

```
{'lat': 5.0169, 'lon': -74.471, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812983, 'sunset': 1641855642, 'temp': 29.38, 'feels_like': 36.06, 'pressure': 1010, 'humidity': 81, 'dew_point': 25.78, 'uvi': 4.34, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 323, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, 'hourly': [{'dt': 1641772800, 'temp': 24.38, 'feels_like': 25.38, 'pressure': 1013, 'humidity': 96, 'dew_point': 23.7, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 104, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641776400, 'temp': 25.38, 'feels_like': 26.51, 'pressure': 1014, 'humidity': 97, 'dew_point': 24.87, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 107, 'wind_gust': 1.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.38, 'feels_like': 25.41, 'pressure': 1015, 'humidity': 97, 'dew_point': 23.87, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 104, 'wind_gust': 1.27, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 24.38, 'feels_like': 25.41, 'pressure': 1015, 'humidity': 97, 'dew_point': 23.87, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 109, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.38, 'feels_like': 25.38, 'pressure': 1015, 'humidity': 96, 'dew_point': 23.7, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 114, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.38, 'feels_like': 23.15, 'pressure': 1015, 'humidity': 95, 'dew_point': 21.54, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 116, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.38, 'feels_like': 20.95, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.55, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 121, 'wind_gust': 1.17, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 19.38, 'feels_like': 19.85, 'pressure': 1013, 'humidity': 95, 'dew_point': 18.56, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 125, 'wind_gust': 1.19, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 19.38, 'feels_like': 19.85, 'pressure': 1013, 'humidity': 95, 'dew_point': 18.56, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 122, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 19.38, 'feels_like': 19.85, 'pressure': 1013, 'humidity': 95, 'dew_point': 18.56, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 118, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.38, 'feels_like': 20.95, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.55, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 119, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.38, 'feels_like': 22.05, 'pressure': 1015, 'humidity': 95, 'dew_point': 20.55, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 120, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.38, 'feels_like': 21.95, 'pressure': 1015, 'humidity': 91, 'dew_point': 19.85, 'uvi': 0.32, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 118, 'wind_gust': 1.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 22.38, 'feels_like': 22.81, 'pressure': 1016, 'humidity': 82, 'dew_point': 19.16, 'uvi': 2.05, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 44, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 25.38, 'feels_like': 25.85, 'pressure': 1016, 'humidity': 72, 'dew_point': 19.97, 'uvi': 4.95, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 343, 'wind_gust': 1.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.38, 'feels_like': 28.75, 'pressure': 1016, 'humidity': 62, 'dew_point': 19.46, 'uvi': 8.38, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 341, 'wind_gust': 1.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.38, 'feels_like': 29.66, 'pressure': 1014, 'humidity': 57, 'dew_point': 19.05, 'uvi': 10.81, 'clouds': 78, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 325, 'wind_gust': 1.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 28.38, 'feels_like': 29.31, 'pressure': 1013, 'humidity': 54, 'dew_point': 18.18, 'uvi': 11.77, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 324, 'wind_gust': 1.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 29.38, 'feels_like': 30.88, 'pressure': 1011, 'humidity': 55, 'dew_point': 19.4, 'uvi': 10.67, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 313, 'wind_gust': 1.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 29.38, 'feels_like': 32.78, 'pressure': 1010, 'humidity': 66, 'dew_point': 22.36, 'uvi': 7.48, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.21, 'wind_deg': 311, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641844800, 'temp': 29.38, 'feels_like': 36.06, 'pressure': 1010, 'humidity': 81, 'dew_point': 25.78, 'uvi': 4.34, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 323, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641848400, 'temp': 29.38, 'feels_like': 36.38, 'pressure': 1010, 'humidity': 85, 'dew_point': 26.59, 'uvi': 1.74, 'clouds': 63, 'visibility': 9220, 'wind_speed': 1.38, 'wind_deg': 340, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641852000, 'temp': 28.38, 'feels_like': 35.18, 'pressure': 1011, 'humidity': 91, 'dew_point': 26.77, 'uvi': 0.39, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 357, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641855600, 'temp': 26.38, 'feels_like': 26.38, 'pressure': 1012, 'humidity': 97, 'dew_point': 25.86, 'uvi': 0, 'clouds': 67, 'visibility': 9765, 'wind_speed': 1.15, 'wind_deg': 60, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 00:00:00 | 43.000000 | 23.700000 | 25.380000 | 96.000000 | 1013.000000 | 0.25 | 24.380000 | 0.000000 | 10000.000000 | 104.000000 | 1.1 | 1.280000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 01:00:00 | 52.000000 | 24.870000 | 26.510000 | 97.000000 | 1014.000000 |  | 25.380000 | 0.000000 | 10000.000000 | 107.000000 | 1.25 | 1.540000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 02:00:00 | 36.000000 | 23.870000 | 25.410000 | 97.000000 | 1015.000000 |  | 24.380000 | 0.000000 | 10000.000000 | 104.000000 | 1.27 | 1.590000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 03:00:00 | 52.000000 | 23.870000 | 25.410000 | 97.000000 | 1015.000000 |  | 24.380000 | 0.000000 | 10000.000000 | 109.000000 | 1.32 | 1.540000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 04:00:00 | 57.000000 | 23.700000 | 25.380000 | 96.000000 | 1015.000000 |  | 24.380000 | 0.000000 | 10000.000000 | 114.000000 | 1.26 | 1.610000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 05:00:00 | 65.000000 | 21.540000 | 23.150000 | 95.000000 | 1015.000000 |  | 22.380000 | 0.000000 | 10000.000000 | 116.000000 | 1.26 | 1.660000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 06:00:00 | 21.000000 | 19.550000 | 20.950000 | 95.000000 | 1014.000000 |  | 20.380000 | 0.000000 | 10000.000000 | 121.000000 | 1.17 | 1.550000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 07:00:00 | 47.000000 | 18.560000 | 19.850000 | 95.000000 | 1013.000000 |  | 19.380000 | 0.000000 | 10000.000000 | 125.000000 | 1.19 | 1.560000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 08:00:00 | 67.000000 | 18.560000 | 19.850000 | 95.000000 | 1013.000000 |  | 19.380000 | 0.000000 | 10000.000000 | 122.000000 | 1.21 | 1.600000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 09:00:00 | 66.000000 | 18.560000 | 19.850000 | 95.000000 | 1013.000000 |  | 19.380000 | 0.000000 | 10000.000000 | 118.000000 | 1.19 | 1.660000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 10:00:00 | 53.000000 | 19.550000 | 20.950000 | 95.000000 | 1014.000000 |  | 20.380000 | 0.000000 | 10000.000000 | 119.000000 | 1.26 | 1.760000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 11:00:00 | 60.000000 | 20.550000 | 22.050000 | 95.000000 | 1015.000000 |  | 21.380000 | 0.000000 | 10000.000000 | 120.000000 | 1.29 | 1.760000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 12:00:00 | 34.000000 | 19.850000 | 21.950000 | 91.000000 | 1015.000000 |  | 21.380000 | 0.320000 | 10000.000000 | 118.000000 | 1.21 | 1.470000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 13:00:00 | 54.000000 | 19.160000 | 22.810000 | 82.000000 | 1016.000000 |  | 22.380000 | 2.050000 | 10000.000000 | 44.000000 | 1.33 | 0.770000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 14:00:00 | 64.000000 | 19.970000 | 25.850000 | 72.000000 | 1016.000000 |  | 25.380000 | 4.950000 | 10000.000000 | 343.000000 | 1.62 | 1.390000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 19.460000 | 28.750000 | 62.000000 | 1016.000000 |  | 27.380000 | 8.380000 | 10000.000000 | 341.000000 | 1.7 | 1.880000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 16:00:00 | 78.000000 | 19.050000 | 29.660000 | 57.000000 | 1014.000000 |  | 28.380000 | 10.810000 | 10000.000000 | 325.000000 | 1.65 | 2.220000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 17:00:00 | 76.000000 | 18.180000 | 29.310000 | 54.000000 | 1013.000000 |  | 28.380000 | 11.770000 | 10000.000000 | 324.000000 | 1.9 | 2.350000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 18:00:00 | 93.000000 | 19.400000 | 30.880000 | 55.000000 | 1011.000000 |  | 29.380000 | 10.670000 | 10000.000000 | 313.000000 | 1.93 | 2.420000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 19:00:00 | 96.000000 | 22.360000 | 32.780000 | 66.000000 | 1010.000000 | 0.29 | 29.380000 | 7.480000 | 10000.000000 | 311.000000 | 1.78 | 2.210000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 20:00:00 | 71.000000 | 25.780000 | 36.060000 | 81.000000 | 1010.000000 | 0.73 | 29.380000 | 4.340000 | 10000.000000 | 323.000000 | 1.87 | 1.560000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 21:00:00 | 63.000000 | 26.590000 | 36.380000 | 85.000000 | 1010.000000 | 0.86 | 29.380000 | 1.740000 | 9220.000000 | 340.000000 | 1.57 | 1.380000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 22:00:00 | 59.000000 | 26.770000 | 35.180000 | 91.000000 | 1011.000000 | 0.67 | 28.380000 | 0.390000 | 10000.000000 | 357.000000 | 1.53 | 1.010000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065180 | "VILLETA - AUT [23065180]" | 5.016861 | -74.470972 | 878.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-10 00:00:00 | NaT | Cundinamarca | Villeta | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 23:00:00 | 67.000000 | 25.860000 | 26.380000 | 97.000000 | 1012.000000 | 0.96 | 26.380000 | 0.000000 | 9765.000000 | 60.000000 | 1.1 | 1.150000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23065180_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23065180_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23065180_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065180_OWM_Windspeed_20220111.png)
