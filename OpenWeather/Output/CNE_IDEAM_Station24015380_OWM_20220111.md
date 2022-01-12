
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CARMEN DE CARUPA  - AUT [24015380] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24015380_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.34722222,-73.89833333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.34722222&lon=-73.89833333)


| Parameter | Value |
|---|---|
| Code | 24015380 |
| Name | CARMEN DE CARUPA  - AUT [24015380] |
| Latitude, ° | 5.34722222 |
| Longitude, ° | -73.89833333 |
| Elevation, m | 2970 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2010-03-30 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Carmen De Carupa |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Suárez |

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

### (CNE index 1279) Open Weather values for station 24015380 - CARMEN DE CARUPA  - AUT [24015380]

JSON data from API OWM:

```
{'lat': 5.3472, 'lon': -73.8983, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812878, 'sunset': 1641855473, 'temp': 12.9, 'feels_like': 12.39, 'pressure': 1013, 'humidity': 82, 'dew_point': 9.91, 'uvi': 3.53, 'clouds': 87, 'visibility': 8892, 'wind_speed': 1.56, 'wind_deg': 320, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, 'hourly': [{'dt': 1641772800, 'temp': 9.56, 'feels_like': 9.56, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.8, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 24, 'wind_gust': 1.23, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.18, 'feels_like': 9.18, 'pressure': 1017, 'humidity': 95, 'dew_point': 8.42, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 32, 'wind_gust': 1.08, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.42, 'feels_like': 8.42, 'pressure': 1018, 'humidity': 95, 'dew_point': 7.67, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 36, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.04, 'feels_like': 8.04, 'pressure': 1018, 'humidity': 96, 'dew_point': 7.44, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 73, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 7.71, 'feels_like': 7.71, 'pressure': 1019, 'humidity': 96, 'dew_point': 7.11, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 118, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 7.27, 'feels_like': 7.27, 'pressure': 1018, 'humidity': 96, 'dew_point': 6.68, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 130, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 7.12, 'feels_like': 7.12, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.22, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 130, 'wind_gust': 0.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 6.33, 'feels_like': 6.33, 'pressure': 1017, 'humidity': 94, 'dew_point': 5.44, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 134, 'wind_gust': 0.88, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 5.93, 'feels_like': 5.93, 'pressure': 1016, 'humidity': 94, 'dew_point': 5.04, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 121, 'wind_gust': 0.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 5.66, 'feels_like': 5.66, 'pressure': 1016, 'humidity': 95, 'dew_point': 4.92, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 131, 'wind_gust': 0.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 5.45, 'feels_like': 5.45, 'pressure': 1017, 'humidity': 95, 'dew_point': 4.71, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 116, 'wind_gust': 0.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 5.58, 'feels_like': 5.58, 'pressure': 1018, 'humidity': 95, 'dew_point': 4.84, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 133, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 7.2, 'feels_like': 7.2, 'pressure': 1019, 'humidity': 91, 'dew_point': 5.83, 'uvi': 0.55, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 136, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 10.25, 'feels_like': 9.45, 'pressure': 1019, 'humidity': 81, 'dew_point': 7.14, 'uvi': 2.29, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 267, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 12.44, 'feels_like': 11.62, 'pressure': 1018, 'humidity': 72, 'dew_point': 7.54, 'uvi': 5.42, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 295, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 14.07, 'feels_like': 13.26, 'pressure': 1017, 'humidity': 66, 'dew_point': 7.82, 'uvi': 9.1, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 298, 'wind_gust': 1.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 14.87, 'feels_like': 14.06, 'pressure': 1016, 'humidity': 63, 'dew_point': 7.9, 'uvi': 11.35, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 309, 'wind_gust': 1.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 15.04, 'feels_like': 14.24, 'pressure': 1015, 'humidity': 63, 'dew_point': 8.06, 'uvi': 12.28, 'clouds': 60, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 310, 'wind_gust': 1.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641837600, 'temp': 14.77, 'feels_like': 14.05, 'pressure': 1014, 'humidity': 67, 'dew_point': 8.71, 'uvi': 11.06, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 309, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641841200, 'temp': 13.91, 'feels_like': 13.29, 'pressure': 1013, 'humidity': 74, 'dew_point': 9.36, 'uvi': 6.14, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 312, 'wind_gust': 1.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641844800, 'temp': 12.9, 'feels_like': 12.39, 'pressure': 1013, 'humidity': 82, 'dew_point': 9.91, 'uvi': 3.53, 'clouds': 87, 'visibility': 8892, 'wind_speed': 1.56, 'wind_deg': 320, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641848400, 'temp': 12.21, 'feels_like': 11.71, 'pressure': 1013, 'humidity': 85, 'dew_point': 9.77, 'uvi': 1.4, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 318, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641852000, 'temp': 11.39, 'feels_like': 10.88, 'pressure': 1014, 'humidity': 88, 'dew_point': 9.48, 'uvi': 0.33, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 335, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641855600, 'temp': 9.82, 'feels_like': 9.82, 'pressure': 1015, 'humidity': 93, 'dew_point': 8.74, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 354, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 00:00:00 | 68.000000 | 8.800000 | 9.560000 | 95.000000 | 1016.000000 |  | 9.560000 | 0.000000 | 10000.000000 | 24.000000 | 1.23 | 0.480000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 01:00:00 | 86.000000 | 8.420000 | 9.180000 | 95.000000 | 1017.000000 |  | 9.180000 | 0.000000 | 10000.000000 | 32.000000 | 1.08 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 02:00:00 | 88.000000 | 7.670000 | 8.420000 | 95.000000 | 1018.000000 |  | 8.420000 | 0.000000 | 10000.000000 | 36.000000 | 1.02 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 03:00:00 | 89.000000 | 7.440000 | 8.040000 | 96.000000 | 1018.000000 |  | 8.040000 | 0.000000 | 10000.000000 | 73.000000 | 0.96 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 04:00:00 | 84.000000 | 7.110000 | 7.710000 | 96.000000 | 1019.000000 |  | 7.710000 | 0.000000 | 10000.000000 | 118.000000 | 0.9 | 0.460000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 05:00:00 | 87.000000 | 6.680000 | 7.270000 | 96.000000 | 1018.000000 |  | 7.270000 | 0.000000 | 10000.000000 | 130.000000 | 0.82 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 06:00:00 | 28.000000 | 6.220000 | 7.120000 | 94.000000 | 1017.000000 |  | 7.120000 | 0.000000 | 10000.000000 | 130.000000 | 0.81 | 0.840000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 07:00:00 | 44.000000 | 5.440000 | 6.330000 | 94.000000 | 1017.000000 |  | 6.330000 | 0.000000 | 10000.000000 | 134.000000 | 0.88 | 0.770000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 08:00:00 | 52.000000 | 5.040000 | 5.930000 | 94.000000 | 1016.000000 |  | 5.930000 | 0.000000 | 10000.000000 | 121.000000 | 0.93 | 0.750000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 09:00:00 | 49.000000 | 4.920000 | 5.660000 | 95.000000 | 1016.000000 |  | 5.660000 | 0.000000 | 10000.000000 | 131.000000 | 0.92 | 0.520000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 10:00:00 | 51.000000 | 4.710000 | 5.450000 | 95.000000 | 1017.000000 |  | 5.450000 | 0.000000 | 10000.000000 | 116.000000 | 0.93 | 0.600000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 11:00:00 | 55.000000 | 4.840000 | 5.580000 | 95.000000 | 1018.000000 |  | 5.580000 | 0.000000 | 10000.000000 | 133.000000 | 0.9 | 0.630000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 12:00:00 | 68.000000 | 5.830000 | 7.200000 | 91.000000 | 1019.000000 |  | 7.200000 | 0.550000 | 10000.000000 | 136.000000 | 0.81 | 0.700000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 13:00:00 | 67.000000 | 7.140000 | 9.450000 | 81.000000 | 1019.000000 |  | 10.250000 | 2.290000 | 10000.000000 | 267.000000 | 0.75 | 0.450000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 14:00:00 | 64.000000 | 7.540000 | 11.620000 | 72.000000 | 1018.000000 |  | 12.440000 | 5.420000 | 10000.000000 | 295.000000 | 1.03 | 1.030000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 15:00:00 | 55.000000 | 7.820000 | 13.260000 | 66.000000 | 1017.000000 |  | 14.070000 | 9.100000 | 10000.000000 | 298.000000 | 1.78 | 1.750000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 16:00:00 | 56.000000 | 7.900000 | 14.060000 | 63.000000 | 1016.000000 | 0.11 | 14.870000 | 11.350000 | 10000.000000 | 309.000000 | 1.91 | 2.110000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 17:00:00 | 60.000000 | 8.060000 | 14.240000 | 63.000000 | 1015.000000 | 0.14 | 15.040000 | 12.280000 | 10000.000000 | 310.000000 | 1.85 | 2.340000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 18:00:00 | 71.000000 | 8.710000 | 14.050000 | 67.000000 | 1014.000000 | 0.12 | 14.770000 | 11.060000 | 10000.000000 | 309.000000 | 1.55 | 2.070000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 9.360000 | 13.290000 | 74.000000 | 1013.000000 | 0.41 | 13.910000 | 6.140000 | 10000.000000 | 312.000000 | 1.84 | 1.810000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 20:00:00 | 87.000000 | 9.910000 | 12.390000 | 82.000000 | 1013.000000 | 0.53 | 12.900000 | 3.530000 | 8892.000000 | 320.000000 | 1.74 | 1.560000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 21:00:00 | 88.000000 | 9.770000 | 11.710000 | 85.000000 | 1013.000000 | 0.4 | 12.210000 | 1.400000 | 10000.000000 | 318.000000 | 1.36 | 1.250000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 9.480000 | 10.880000 | 88.000000 | 1014.000000 | 0.25 | 11.390000 | 0.330000 | 10000.000000 | 335.000000 | 1.59 | 1.150000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24015380 | "CARMEN DE CARUPA  - AUT [24015380]" | 5.347222 | -73.898333 | 2970.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-30 19:00:00 | NaT | Cundinamarca | Carmen De Carupa | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 8.740000 | 9.820000 | 93.000000 | 1015.000000 | 0.19 | 9.820000 | 0.000000 | 10000.000000 | 354.000000 | 1.03 | 0.760000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24015380_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24015380_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24015380_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015380_OWM_Windspeed_20220111.png)
