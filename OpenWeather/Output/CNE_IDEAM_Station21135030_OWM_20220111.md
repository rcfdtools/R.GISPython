
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ANCHIQUE [21135030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21135030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.57383333,-75.109) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.57383333&lon=-75.109)


| Parameter | Value |
|---|---|
| Code | 21135030 |
| Name | ANCHIQUE [21135030] |
| Latitude, ° | 3.57383333 |
| Longitude, ° | -75.109 |
| Elevation, m | 415 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1963-12-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Natagaima |
| Stream | Guaviare |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Aipe, Río Chenche y otros directos al Magdalena |

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

### (CNE index 2289) Open Weather values for station 21135030 - ANCHIQUE [21135030]

JSON data from API OWM:

```
{'lat': 3.5738, 'lon': -75.109, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812996, 'sunset': 1641855935, 'temp': 29.85, 'feels_like': 32.74, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.52, 'uvi': 3.24, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 356, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, 'hourly': [{'dt': 1641772800, 'temp': 25.58, 'feels_like': 26.18, 'pressure': 1010, 'humidity': 76, 'dew_point': 21.04, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 10, 'wind_gust': 1.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 24.76, 'feels_like': 25.35, 'pressure': 1011, 'humidity': 79, 'dew_point': 20.87, 'uvi': 0, 'clouds': 18, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 92, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641780000, 'temp': 24.06, 'feels_like': 24.66, 'pressure': 1012, 'humidity': 82, 'dew_point': 20.8, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 118, 'wind_gust': 1.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641783600, 'temp': 23.35, 'feels_like': 23.96, 'pressure': 1013, 'humidity': 85, 'dew_point': 20.69, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 69, 'wind_gust': 1.73, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.21}}, {'dt': 1641787200, 'temp': 23.03, 'feels_like': 23.63, 'pressure': 1013, 'humidity': 86, 'dew_point': 20.56, 'uvi': 0, 'clouds': 80, 'visibility': 8210, 'wind_speed': 0.28, 'wind_deg': 64, 'wind_gust': 1.83, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.16}}, {'dt': 1641790800, 'temp': 23.11, 'feels_like': 23.7, 'pressure': 1012, 'humidity': 85, 'dew_point': 20.45, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 35, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641794400, 'temp': 23.14, 'feels_like': 23.76, 'pressure': 1012, 'humidity': 86, 'dew_point': 20.67, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 109, 'wind_gust': 1.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641798000, 'temp': 23.01, 'feels_like': 23.61, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.54, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 129, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641801600, 'temp': 22.88, 'feels_like': 23.47, 'pressure': 1010, 'humidity': 86, 'dew_point': 20.41, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 135, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641805200, 'temp': 22.76, 'feels_like': 23.34, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.3, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 131, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641808800, 'temp': 22.26, 'feels_like': 22.87, 'pressure': 1011, 'humidity': 89, 'dew_point': 20.36, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 129, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641812400, 'temp': 22.29, 'feels_like': 22.9, 'pressure': 1012, 'humidity': 89, 'dew_point': 20.39, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 129, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1641816000, 'temp': 23.01, 'feels_like': 23.69, 'pressure': 1013, 'humidity': 89, 'dew_point': 21.1, 'uvi': 0.47, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 76, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641819600, 'temp': 23.88, 'feels_like': 24.57, 'pressure': 1014, 'humidity': 86, 'dew_point': 21.4, 'uvi': 1.98, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 38, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641823200, 'temp': 25.24, 'feels_like': 25.96, 'pressure': 1015, 'humidity': 82, 'dew_point': 21.95, 'uvi': 4.86, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 51, 'wind_gust': 1.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.79}}, {'dt': 1641826800, 'temp': 25.83, 'feels_like': 26.56, 'pressure': 1014, 'humidity': 80, 'dew_point': 22.12, 'uvi': 8.33, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.09, 'wind_deg': 48, 'wind_gust': 2.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641830400, 'temp': 27.22, 'feels_like': 29.62, 'pressure': 1013, 'humidity': 74, 'dew_point': 22.18, 'uvi': 7.71, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 20, 'wind_gust': 2.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641834000, 'temp': 28.68, 'feels_like': 31.71, 'pressure': 1012, 'humidity': 68, 'dew_point': 22.19, 'uvi': 8.49, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.73, 'wind_deg': 355, 'wind_gust': 2.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641837600, 'temp': 29.6, 'feels_like': 32.65, 'pressure': 1011, 'humidity': 63, 'dew_point': 21.81, 'uvi': 7.8, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.74, 'wind_deg': 350, 'wind_gust': 2.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 29.77, 'feels_like': 32.78, 'pressure': 1009, 'humidity': 62, 'dew_point': 21.71, 'uvi': 5.46, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 347, 'wind_gust': 2.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 29.85, 'feels_like': 32.74, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.52, 'uvi': 3.24, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 356, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641848400, 'temp': 29.66, 'feels_like': 32.38, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.34, 'uvi': 1.37, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 5, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641852000, 'temp': 29.29, 'feels_like': 32.41, 'pressure': 1008, 'humidity': 65, 'dew_point': 22.03, 'uvi': 0.37, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 11, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641855600, 'temp': 26.29, 'feels_like': 26.29, 'pressure': 1009, 'humidity': 75, 'dew_point': 21.5, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 22, 'wind_gust': 1.41, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 23.000000 | 21.040000 | 26.180000 | 76.000000 | 1010.000000 |  | 25.580000 | 0.000000 | 10000.000000 | 10.000000 | 1.55 | 0.820000 | 801 | Clouds | few clouds | 02n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 18.000000 | 20.870000 | 25.350000 | 79.000000 | 1011.000000 | 0.29 | 24.760000 | 0.000000 | 10000.000000 | 92.000000 | 1.71 | 0.490000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 59.000000 | 20.800000 | 24.660000 | 82.000000 | 1012.000000 | 0.64 | 24.060000 | 0.000000 | 10000.000000 | 118.000000 | 1.8 | 0.640000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 73.000000 | 20.690000 | 23.960000 | 85.000000 | 1013.000000 | 1.21 | 23.350000 | 0.000000 | 10000.000000 | 69.000000 | 1.73 | 0.400000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 80.000000 | 20.560000 | 23.630000 | 86.000000 | 1013.000000 | 1.16 | 23.030000 | 0.000000 | 8210.000000 | 64.000000 | 1.83 | 0.280000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 75.000000 | 20.450000 | 23.700000 | 85.000000 | 1012.000000 | 0.32 | 23.110000 | 0.000000 | 10000.000000 | 35.000000 | 1.67 | 0.140000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 53.000000 | 20.670000 | 23.760000 | 86.000000 | 1012.000000 | 0.3 | 23.140000 | 0.000000 | 10000.000000 | 109.000000 | 1.35 | 0.150000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 69.000000 | 20.540000 | 23.610000 | 86.000000 | 1011.000000 | 0.28 | 23.010000 | 0.000000 | 10000.000000 | 129.000000 | 1.26 | 0.700000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 82.000000 | 20.410000 | 23.470000 | 86.000000 | 1010.000000 | 0.16 | 22.880000 | 0.000000 | 10000.000000 | 135.000000 | 1.1 | 0.820000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 80.000000 | 20.300000 | 23.340000 | 86.000000 | 1011.000000 | 0.22 | 22.760000 | 0.000000 | 10000.000000 | 131.000000 | 1.03 | 0.850000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 84.000000 | 20.360000 | 22.870000 | 89.000000 | 1011.000000 | 0.39 | 22.260000 | 0.000000 | 10000.000000 | 129.000000 | 1.05 | 1.000000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 85.000000 | 20.390000 | 22.900000 | 89.000000 | 1012.000000 | 0.56 | 22.290000 | 0.000000 | 10000.000000 | 129.000000 | 1.07 | 0.960000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 76.000000 | 21.100000 | 23.690000 | 89.000000 | 1013.000000 | 0.26 | 23.010000 | 0.470000 | 10000.000000 | 76.000000 | 0.72 | 0.500000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 21.400000 | 24.570000 | 86.000000 | 1014.000000 | 0.57 | 23.880000 | 1.980000 | 10000.000000 | 38.000000 | 1.05 | 1.070000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 91.000000 | 21.950000 | 25.960000 | 82.000000 | 1015.000000 | 0.79 | 25.240000 | 4.860000 | 10000.000000 | 51.000000 | 1.86 | 1.650000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 92.000000 | 22.120000 | 26.560000 | 80.000000 | 1014.000000 | 0.92 | 25.830000 | 8.330000 | 10000.000000 | 48.000000 | 2.41 | 2.090000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 89.000000 | 22.180000 | 29.620000 | 74.000000 | 1013.000000 | 0.54 | 27.220000 | 7.710000 | 10000.000000 | 20.000000 | 2.93 | 2.470000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 86.000000 | 22.190000 | 31.710000 | 68.000000 | 1012.000000 | 0.19 | 28.680000 | 8.490000 | 10000.000000 | 355.000000 | 2.99 | 2.730000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 74.000000 | 21.810000 | 32.650000 | 63.000000 | 1011.000000 |  | 29.600000 | 7.800000 | 10000.000000 | 350.000000 | 2.61 | 2.740000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 21.710000 | 32.780000 | 62.000000 | 1009.000000 |  | 29.770000 | 5.460000 | 10000.000000 | 347.000000 | 2.16 | 2.260000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 84.000000 | 21.520000 | 32.740000 | 61.000000 | 1008.000000 | 0.18 | 29.850000 | 3.240000 | 10000.000000 | 356.000000 | 1.82 | 1.780000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 65.000000 | 21.340000 | 32.380000 | 61.000000 | 1008.000000 | 0.32 | 29.660000 | 1.370000 | 10000.000000 | 5.000000 | 1.6 | 1.360000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 62.000000 | 22.030000 | 32.410000 | 65.000000 | 1008.000000 | 0.38 | 29.290000 | 0.370000 | 10000.000000 | 11.000000 | 1.42 | 1.070000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21135030 | "ANCHIQUE [21135030]" | 3.573833 | -75.109000 | 415.000000 | Climática Principal | Convencional | Activa | 1963-12-15 00:00:00 | NaT | Tolima | Natagaima | Guaviare | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Aipe, Río Chenche y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 54.000000 | 21.500000 | 26.290000 | 75.000000 | 1009.000000 | 1.01 | 26.290000 | 0.000000 | 10000.000000 | 22.000000 | 1.41 | 0.970000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21135030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21135030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21135030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21135030_OWM_Windspeed_20220111.png)
