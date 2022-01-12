
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNIVERSIDAD INDUSTRIAL SANTANDER [23195040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23195040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.14472222,-73.12222222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.14472222&lon=-73.12222222)


| Parameter | Value |
|---|---|
| Code | 23195040 |
| Name | UNIVERSIDAD INDUSTRIAL SANTANDER [23195040] |
| Latitude, ° | 7.14472222 |
| Longitude, ° | -73.12222222 |
| Elevation, m | 118 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1957-01-14 19:00:00 |
| Suspension date | 2019-01-21 03:32:04 |
| State | Santander |
| County | Bucaramanga |
| Stream | 0 |
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

### (CNE index 4169) Open Weather values for station 23195040 - UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]

JSON data from API OWM:

```
{'lat': 7.1447, 'lon': -73.1222, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812866, 'sunset': 1641855111, 'temp': 25.88, 'feels_like': 26.43, 'pressure': 1015, 'humidity': 73, 'dew_point': 20.67, 'uvi': 4.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 21.88, 'feels_like': 22.73, 'pressure': 1015, 'humidity': 100, 'dew_point': 21.88, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 320, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 20.88, 'feels_like': 21.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 20.88, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 320, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 20.88, 'feels_like': 21.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 20.88, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 300, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 20.88, 'feels_like': 21.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 20.88, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 21.88, 'feels_like': 22.58, 'pressure': 1016, 'humidity': 94, 'dew_point': 20.87, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 21.88, 'feels_like': 22.58, 'pressure': 1016, 'humidity': 94, 'dew_point': 20.87, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 20.01, 'feels_like': 20.31, 'pressure': 1014, 'humidity': 86, 'dew_point': 17.6, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 105, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.19, 'feels_like': 20.48, 'pressure': 1014, 'humidity': 85, 'dew_point': 17.59, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 109, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.26, 'feels_like': 20.56, 'pressure': 1013, 'humidity': 85, 'dew_point': 17.66, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 119, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.17, 'feels_like': 20.49, 'pressure': 1013, 'humidity': 86, 'dew_point': 17.75, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 120, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.19, 'feels_like': 20.54, 'pressure': 1014, 'humidity': 87, 'dew_point': 17.96, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 113, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.88, 'feels_like': 21.32, 'pressure': 1015, 'humidity': 88, 'dew_point': 18.82, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 20.88, 'feels_like': 21.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 20.88, 'uvi': 0.42, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 21.88, 'feels_like': 22.58, 'pressure': 1017, 'humidity': 94, 'dew_point': 20.87, 'uvi': 1.34, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 170, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 23.88, 'feels_like': 24.49, 'pressure': 1018, 'humidity': 83, 'dew_point': 20.82, 'uvi': 3.18, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 24.88, 'feels_like': 25.33, 'pressure': 1018, 'humidity': 73, 'dew_point': 19.71, 'uvi': 5.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 24.88, 'feels_like': 25.33, 'pressure': 1018, 'humidity': 73, 'dew_point': 19.71, 'uvi': 10.38, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 350, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 26.88, 'feels_like': 28.58, 'pressure': 1017, 'humidity': 69, 'dew_point': 20.71, 'uvi': 11.19, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 340, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 26.88, 'feels_like': 28.58, 'pressure': 1016, 'humidity': 69, 'dew_point': 20.71, 'uvi': 10, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 26.88, 'feels_like': 28.58, 'pressure': 1015, 'humidity': 69, 'dew_point': 20.71, 'uvi': 7.27, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 330, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 25.88, 'feels_like': 26.43, 'pressure': 1015, 'humidity': 73, 'dew_point': 20.67, 'uvi': 4.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 25.88, 'feels_like': 26.43, 'pressure': 1014, 'humidity': 73, 'dew_point': 20.67, 'uvi': 1.58, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641852000, 'temp': 24.88, 'feels_like': 25.33, 'pressure': 1014, 'humidity': 73, 'dew_point': 19.71, 'uvi': 0.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641855600, 'temp': 22.88, 'feels_like': 23.39, 'pressure': 1015, 'humidity': 83, 'dew_point': 19.84, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 21.880000 | 22.730000 | 100.000000 | 1015.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 20.880000 | 21.630000 | 100.000000 | 1016.000000 |  | 20.880000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 20.880000 | 21.630000 | 100.000000 | 1016.000000 |  | 20.880000 | 0.000000 | 10000.000000 | 300.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 40.000000 | 20.880000 | 21.630000 | 100.000000 | 1016.000000 |  | 20.880000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 20.000000 | 20.870000 | 22.580000 | 94.000000 | 1016.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 20.000000 | 20.870000 | 22.580000 | 94.000000 | 1016.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 84.000000 | 17.600000 | 20.310000 | 86.000000 | 1014.000000 |  | 20.010000 | 0.000000 | 10000.000000 | 105.000000 | 1.26 | 1.260000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 17.590000 | 20.480000 | 85.000000 | 1014.000000 |  | 20.190000 | 0.000000 | 10000.000000 | 109.000000 | 1.09 | 1.140000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 17.660000 | 20.560000 | 85.000000 | 1013.000000 |  | 20.260000 | 0.000000 | 10000.000000 | 119.000000 | 0.88 | 0.710000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 17.750000 | 20.490000 | 86.000000 | 1013.000000 |  | 20.170000 | 0.000000 | 10000.000000 | 120.000000 | 0.68 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 92.000000 | 17.960000 | 20.540000 | 87.000000 | 1014.000000 |  | 20.190000 | 0.000000 | 10000.000000 | 113.000000 | 0.61 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 18.820000 | 21.320000 | 88.000000 | 1015.000000 |  | 20.880000 | 0.000000 | 10000.000000 | 40.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 20.880000 | 21.630000 | 100.000000 | 1016.000000 |  | 20.880000 | 0.420000 | 10000.000000 | 140.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 20.870000 | 22.580000 | 94.000000 | 1017.000000 |  | 21.880000 | 1.340000 | 10000.000000 | 170.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 20.820000 | 24.490000 | 83.000000 | 1018.000000 |  | 23.880000 | 3.180000 | 10000.000000 | 140.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 19.710000 | 25.330000 | 73.000000 | 1018.000000 |  | 24.880000 | 5.330000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 19.710000 | 25.330000 | 73.000000 | 1018.000000 |  | 24.880000 | 10.380000 | 10000.000000 | 350.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 20.710000 | 28.580000 | 69.000000 | 1017.000000 |  | 26.880000 | 11.190000 | 10000.000000 | 340.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 20.710000 | 28.580000 | 69.000000 | 1016.000000 |  | 26.880000 | 10.000000 | 10000.000000 | 310.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 20.710000 | 28.580000 | 69.000000 | 1015.000000 |  | 26.880000 | 7.270000 | 10000.000000 | 330.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 40.000000 | 20.670000 | 26.430000 | 73.000000 | 1015.000000 |  | 25.880000 | 4.080000 | 10000.000000 | 320.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 20.670000 | 26.430000 | 73.000000 | 1014.000000 | 0.12 | 25.880000 | 1.580000 | 10000.000000 | 310.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 19.710000 | 25.330000 | 73.000000 | 1014.000000 | 0.16 | 24.880000 | 0.300000 | 10000.000000 | 300.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23195040 | "UNIVERSIDAD INDUSTRIAL SANTANDER [23195040]" | 7.144722 | -73.122222 | 118.000000 | Climática Principal | Convencional | Suspendida | 1957-01-14 19:00:00 | 2019-01-21 03:32:04 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 19.840000 | 23.390000 | 83.000000 | 1015.000000 |  | 22.880000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station23195040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23195040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23195040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195040_OWM_Windspeed_20220111.png)
