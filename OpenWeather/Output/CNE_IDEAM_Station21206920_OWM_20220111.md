
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA TERESA - AUT [21206920] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.35,-74.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.35&lon=-74.15)


| Parameter | Value |
|---|---|
| Code | 21206920 |
| Name | VILLA TERESA - AUT [21206920] |
| Latitude, ° | 4.35 |
| Longitude, ° | -74.15 |
| Elevation, m | 3624 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-19 00:00:00 |
| Suspension date | NaT |
| State | Bogotá |
| County | Bogota, D.C |
| Stream | Guatiquia |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 86) Open Weather values for station 21206920 - VILLA TERESA - AUT [21206920]

JSON data from API OWM:

```
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812841, 'sunset': 1641855630, 'temp': 12.9, 'feels_like': 12.47, 'pressure': 1014, 'humidity': 85, 'dew_point': 10.44, 'uvi': 4.94, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 276, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, 'hourly': [{'dt': 1641772800, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 95, 'dew_point': 7.15, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 54, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.99, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 95, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 94, 'dew_point': 7, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 108, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 94, 'dew_point': 7, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 133, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 94, 'dew_point': 7, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 146, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.86, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 127, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 2.72, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 144, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1017, 'humidity': 91, 'dew_point': 1.58, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 233, 'wind_gust': 0.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1016, 'humidity': 91, 'dew_point': 1.58, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 233, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 2.9, 'feels_like': 2.9, 'pressure': 1016, 'humidity': 91, 'dew_point': 1.58, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 259, 'wind_gust': 0.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 3.9, 'feels_like': 3.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.87, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 266, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1018, 'humidity': 95, 'dew_point': 4.17, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 250, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1019, 'humidity': 91, 'dew_point': 3.56, 'uvi': 0.52, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 236, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1019, 'humidity': 84, 'dew_point': 3.41, 'uvi': 2.18, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 345, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 76, 'dew_point': 4.91, 'uvi': 5.19, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 326, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641826800, 'temp': 10.9, 'feels_like': 9.87, 'pressure': 1018, 'humidity': 70, 'dew_point': 5.65, 'uvi': 8.75, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 325, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641830400, 'temp': 11.9, 'feels_like': 10.9, 'pressure': 1017, 'humidity': 67, 'dew_point': 5.97, 'uvi': 11.72, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 308, 'wind_gust': 1.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641834000, 'temp': 11.9, 'feels_like': 10.92, 'pressure': 1015, 'humidity': 68, 'dew_point': 6.19, 'uvi': 12.75, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 310, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641837600, 'temp': 12.9, 'feels_like': 12.2, 'pressure': 1015, 'humidity': 75, 'dew_point': 8.58, 'uvi': 11.57, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 303, 'wind_gust': 2.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641841200, 'temp': 12.9, 'feels_like': 12.26, 'pressure': 1014, 'humidity': 77, 'dew_point': 8.97, 'uvi': 8.48, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 295, 'wind_gust': 2.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641844800, 'temp': 12.9, 'feels_like': 12.47, 'pressure': 1014, 'humidity': 85, 'dew_point': 10.44, 'uvi': 4.94, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 276, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641848400, 'temp': 12.9, 'feels_like': 12.57, 'pressure': 1014, 'humidity': 89, 'dew_point': 11.13, 'uvi': 2, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 264, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641852000, 'temp': 11.9, 'feels_like': 11.55, 'pressure': 1015, 'humidity': 92, 'dew_point': 10.64, 'uvi': 0.45, 'clouds': 92, 'visibility': 9013, 'wind_speed': 0.34, 'wind_deg': 264, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641855600, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1016, 'humidity': 93, 'dew_point': 8.82, 'uvi': 0, 'clouds': 93, 'visibility': 9937, 'wind_speed': 0.13, 'wind_deg': 234, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 00:00:00 | 95.000000 | 7.150000 | 7.900000 | 95.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 54.000000 | 0.91 | 0.170000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 7.990000 | 8.900000 | 94.000000 | 1018.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 95.000000 | 1 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 02:00:00 | 94.000000 | 7.000000 | 7.900000 | 94.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 108.000000 | 1.03 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 7.000000 | 7.900000 | 94.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 133.000000 | 1.21 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 7.000000 | 7.900000 | 94.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 146.000000 | 1.25 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 4.860000 | 5.900000 | 93.000000 | 1018.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 127.000000 | 0.96 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 2.720000 | 3.900000 | 92.000000 | 1017.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 144.000000 | 0.86 | 0.280000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 07:00:00 | 84.000000 | 1.580000 | 2.900000 | 91.000000 | 1017.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 233.000000 | 0.69 | 0.210000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 08:00:00 | 82.000000 | 1.580000 | 2.900000 | 91.000000 | 1016.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 233.000000 | 0.8 | 0.230000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 09:00:00 | 83.000000 | 1.580000 | 2.900000 | 91.000000 | 1016.000000 |  | 2.900000 | 0.000000 | 10000.000000 | 259.000000 | 0.88 | 0.550000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 10:00:00 | 81.000000 | 2.870000 | 3.900000 | 93.000000 | 1017.000000 |  | 3.900000 | 0.000000 | 10000.000000 | 266.000000 | 0.86 | 0.630000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 11:00:00 | 80.000000 | 4.170000 | 4.900000 | 95.000000 | 1018.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 250.000000 | 0.89 | 0.390000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 12:00:00 | 78.000000 | 3.560000 | 4.900000 | 91.000000 | 1019.000000 |  | 4.900000 | 0.520000 | 10000.000000 | 236.000000 | 1.03 | 0.120000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 13:00:00 | 82.000000 | 3.410000 | 5.900000 | 84.000000 | 1019.000000 |  | 5.900000 | 2.180000 | 10000.000000 | 345.000000 | 0.8 | 0.410000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 14:00:00 | 80.000000 | 4.910000 | 8.900000 | 76.000000 | 1019.000000 | 0.13 | 8.900000 | 5.190000 | 10000.000000 | 326.000000 | 1.21 | 0.620000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 5.650000 | 9.870000 | 70.000000 | 1018.000000 | 0.12 | 10.900000 | 8.750000 | 10000.000000 | 325.000000 | 1.73 | 0.860000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 16:00:00 | 80.000000 | 5.970000 | 10.900000 | 67.000000 | 1017.000000 | 0.17 | 11.900000 | 11.720000 | 10000.000000 | 308.000000 | 1.95 | 0.990000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 17:00:00 | 82.000000 | 6.190000 | 10.920000 | 68.000000 | 1015.000000 | 0.12 | 11.900000 | 12.750000 | 10000.000000 | 310.000000 | 2.23 | 0.910000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 18:00:00 | 65.000000 | 8.580000 | 12.200000 | 75.000000 | 1015.000000 | 0.22 | 12.900000 | 11.570000 | 10000.000000 | 303.000000 | 2.09 | 0.890000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 19:00:00 | 86.000000 | 8.970000 | 12.260000 | 77.000000 | 1014.000000 | 0.53 | 12.900000 | 8.480000 | 10000.000000 | 295.000000 | 2.15 | 0.850000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 20:00:00 | 92.000000 | 10.440000 | 12.470000 | 85.000000 | 1014.000000 | 0.53 | 12.900000 | 4.940000 | 10000.000000 | 276.000000 | 1.9 | 0.700000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 11.130000 | 12.570000 | 89.000000 | 1014.000000 | 0.43 | 12.900000 | 2.000000 | 10000.000000 | 264.000000 | 1.5 | 0.330000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 22:00:00 | 92.000000 | 10.640000 | 11.550000 | 92.000000 | 1015.000000 | 0.23 | 11.900000 | 0.450000 | 9013.000000 | 264.000000 | 1.52 | 0.340000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-19 00:00:00 | NaT | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 23:00:00 | 93.000000 | 8.820000 | 9.900000 | 93.000000 | 1016.000000 | 0.22 | 9.900000 | 0.000000 | 9937.000000 | 234.000000 | 1.06 | 0.130000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220111.png)
