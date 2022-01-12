
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO G L VALENCIA [26035030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26035030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.45288889,-76.60875) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.45288889&lon=-76.60875)


| Parameter | Value |
|---|---|
| Code | 26035030 |
| Name | AEROPUERTO G L VALENCIA [26035030] |
| Latitude, ° | 2.45288889 |
| Longitude, ° | -76.60875 |
| Elevation, m | 1752 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1941-06-15 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Popayán |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Alto Río Cauca |

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

### (CNE index 2071) Open Weather values for station 26035030 - AEROPUERTO G L VALENCIA [26035030]

JSON data from API OWM:

```
{'lat': 2.4529, 'lon': -76.6088, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813248, 'sunset': 1641856404, 'temp': 18.55, 'feels_like': 18.86, 'pressure': 1013, 'humidity': 92, 'dew_point': 17.23, 'uvi': 2.35, 'clouds': 99, 'visibility': 5023, 'wind_speed': 1.52, 'wind_deg': 270, 'wind_gust': 1.89, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.47}}, 'hourly': [{'dt': 1641772800, 'temp': 15.7, 'feels_like': 15.88, 'pressure': 1015, 'humidity': 98, 'dew_point': 15.39, 'uvi': 0, 'clouds': 94, 'visibility': 9136, 'wind_speed': 0.24, 'wind_deg': 200, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.7}}, {'dt': 1641776400, 'temp': 15.41, 'feels_like': 15.57, 'pressure': 1017, 'humidity': 98, 'dew_point': 15.1, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 159, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.46}}, {'dt': 1641780000, 'temp': 15.35, 'feels_like': 15.5, 'pressure': 1018, 'humidity': 98, 'dew_point': 15.04, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 101, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641783600, 'temp': 15.41, 'feels_like': 15.57, 'pressure': 1018, 'humidity': 98, 'dew_point': 15.1, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 124, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.46, 'feels_like': 15.62, 'pressure': 1018, 'humidity': 98, 'dew_point': 15.15, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 169, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641790800, 'temp': 15.56, 'feels_like': 15.73, 'pressure': 1017, 'humidity': 98, 'dew_point': 15.25, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 138, 'wind_gust': 0.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.56, 'feels_like': 15.73, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.25, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 257, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 15.41, 'feels_like': 15.57, 'pressure': 1016, 'humidity': 98, 'dew_point': 15.1, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 265, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641801600, 'temp': 15.36, 'feels_like': 15.54, 'pressure': 1015, 'humidity': 99, 'dew_point': 15.2, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 242, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641805200, 'temp': 15.42, 'feels_like': 15.6, 'pressure': 1015, 'humidity': 99, 'dew_point': 15.26, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 270, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641808800, 'temp': 15.36, 'feels_like': 15.54, 'pressure': 1016, 'humidity': 99, 'dew_point': 15.2, 'uvi': 0, 'clouds': 100, 'visibility': 8841, 'wind_speed': 0.36, 'wind_deg': 308, 'wind_gust': 0.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641812400, 'temp': 15.28, 'feels_like': 15.45, 'pressure': 1016, 'humidity': 99, 'dew_point': 15.12, 'uvi': 0, 'clouds': 100, 'visibility': 8180, 'wind_speed': 0.42, 'wind_deg': 285, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641816000, 'temp': 15.85, 'feels_like': 16.05, 'pressure': 1017, 'humidity': 98, 'dew_point': 15.53, 'uvi': 0.28, 'clouds': 100, 'visibility': 9640, 'wind_speed': 0.24, 'wind_deg': 322, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641819600, 'temp': 16.76, 'feels_like': 17, 'pressure': 1018, 'humidity': 96, 'dew_point': 16.12, 'uvi': 1.24, 'clouds': 100, 'visibility': 9531, 'wind_speed': 0.51, 'wind_deg': 297, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641823200, 'temp': 17.81, 'feels_like': 18.05, 'pressure': 1018, 'humidity': 92, 'dew_point': 16.49, 'uvi': 3.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 290, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641826800, 'temp': 18.63, 'feels_like': 18.9, 'pressure': 1018, 'humidity': 90, 'dew_point': 16.96, 'uvi': 5.53, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 281, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641830400, 'temp': 19.72, 'feels_like': 20.02, 'pressure': 1017, 'humidity': 87, 'dew_point': 17.5, 'uvi': 9.04, 'clouds': 100, 'visibility': 6751, 'wind_speed': 1.37, 'wind_deg': 285, 'wind_gust': 1.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641834000, 'temp': 19.82, 'feels_like': 20.18, 'pressure': 1016, 'humidity': 89, 'dew_point': 17.95, 'uvi': 10.14, 'clouds': 100, 'visibility': 6914, 'wind_speed': 1.68, 'wind_deg': 275, 'wind_gust': 1.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.49}}, {'dt': 1641837600, 'temp': 19.48, 'feels_like': 19.83, 'pressure': 1015, 'humidity': 90, 'dew_point': 17.8, 'uvi': 9.48, 'clouds': 92, 'visibility': 6181, 'wind_speed': 1.67, 'wind_deg': 269, 'wind_gust': 1.71, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.57}}, {'dt': 1641841200, 'temp': 18.97, 'feels_like': 19.3, 'pressure': 1014, 'humidity': 91, 'dew_point': 17.47, 'uvi': 3.83, 'clouds': 99, 'visibility': 6641, 'wind_speed': 1.61, 'wind_deg': 271, 'wind_gust': 1.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.59}}, {'dt': 1641844800, 'temp': 18.55, 'feels_like': 18.86, 'pressure': 1013, 'humidity': 92, 'dew_point': 17.23, 'uvi': 2.35, 'clouds': 99, 'visibility': 5023, 'wind_speed': 1.52, 'wind_deg': 270, 'wind_gust': 1.89, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.47}}, {'dt': 1641848400, 'temp': 18.09, 'feels_like': 18.41, 'pressure': 1013, 'humidity': 94, 'dew_point': 17.11, 'uvi': 1.05, 'clouds': 99, 'visibility': 7923, 'wind_speed': 1.4, 'wind_deg': 258, 'wind_gust': 1.9, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.54}}, {'dt': 1641852000, 'temp': 17.56, 'feels_like': 17.88, 'pressure': 1014, 'humidity': 96, 'dew_point': 16.92, 'uvi': 0.24, 'clouds': 94, 'visibility': 8409, 'wind_speed': 1.13, 'wind_deg': 255, 'wind_gust': 1.93, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641855600, 'temp': 16.36, 'feels_like': 16.61, 'pressure': 1015, 'humidity': 98, 'dew_point': 16.04, 'uvi': 0, 'clouds': 90, 'visibility': 7619, 'wind_speed': 0.91, 'wind_deg': 250, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 00:00:00 | 94.000000 | 15.390000 | 15.880000 | 98.000000 | 1015.000000 | 0.7 | 15.700000 | 0.000000 | 9136.000000 | 200.000000 | 1.01 | 0.240000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 01:00:00 | 95.000000 | 15.100000 | 15.570000 | 98.000000 | 1017.000000 | 0.46 | 15.410000 | 0.000000 | 10000.000000 | 159.000000 | 0.65 | 0.210000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 02:00:00 | 95.000000 | 15.040000 | 15.500000 | 98.000000 | 1018.000000 | 0.11 | 15.350000 | 0.000000 | 10000.000000 | 101.000000 | 0.59 | 0.240000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 03:00:00 | 93.000000 | 15.100000 | 15.570000 | 98.000000 | 1018.000000 |  | 15.410000 | 0.000000 | 10000.000000 | 124.000000 | 0.56 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 15.150000 | 15.620000 | 98.000000 | 1018.000000 | 0.14 | 15.460000 | 0.000000 | 10000.000000 | 169.000000 | 0.57 | 0.340000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 05:00:00 | 96.000000 | 15.250000 | 15.730000 | 98.000000 | 1017.000000 |  | 15.560000 | 0.000000 | 10000.000000 | 138.000000 | 0.49 | 0.310000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 06:00:00 | 92.000000 | 15.250000 | 15.730000 | 98.000000 | 1016.000000 |  | 15.560000 | 0.000000 | 10000.000000 | 257.000000 | 0.51 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 15.100000 | 15.570000 | 98.000000 | 1016.000000 | 0.16 | 15.410000 | 0.000000 | 10000.000000 | 265.000000 | 0.66 | 0.380000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 15.200000 | 15.540000 | 99.000000 | 1015.000000 | 0.21 | 15.360000 | 0.000000 | 10000.000000 | 242.000000 | 0.64 | 0.320000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 15.260000 | 15.600000 | 99.000000 | 1015.000000 | 0.17 | 15.420000 | 0.000000 | 10000.000000 | 270.000000 | 0.54 | 0.280000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 15.200000 | 15.540000 | 99.000000 | 1016.000000 | 0.23 | 15.360000 | 0.000000 | 8841.000000 | 308.000000 | 0.6 | 0.360000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 15.120000 | 15.450000 | 99.000000 | 1016.000000 | 0.13 | 15.280000 | 0.000000 | 8180.000000 | 285.000000 | 0.76 | 0.420000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 15.530000 | 16.050000 | 98.000000 | 1017.000000 | 0.21 | 15.850000 | 0.280000 | 9640.000000 | 322.000000 | 0.54 | 0.240000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.120000 | 17.000000 | 96.000000 | 1018.000000 | 0.17 | 16.760000 | 1.240000 | 9531.000000 | 297.000000 | 0.62 | 0.510000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 16.490000 | 18.050000 | 92.000000 | 1018.000000 | 0.39 | 17.810000 | 3.160000 | 10000.000000 | 290.000000 | 0.85 | 0.760000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 16.960000 | 18.900000 | 90.000000 | 1018.000000 | 0.73 | 18.630000 | 5.530000 | 10000.000000 | 281.000000 | 1.39 | 1.280000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 17.500000 | 20.020000 | 87.000000 | 1017.000000 | 1.13 | 19.720000 | 9.040000 | 6751.000000 | 285.000000 | 1.32 | 1.370000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 17.950000 | 20.180000 | 89.000000 | 1016.000000 | 1.49 | 19.820000 | 10.140000 | 6914.000000 | 275.000000 | 1.7 | 1.680000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 18:00:00 | 92.000000 | 17.800000 | 19.830000 | 90.000000 | 1015.000000 | 1.57 | 19.480000 | 9.480000 | 6181.000000 | 269.000000 | 1.71 | 1.670000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 17.470000 | 19.300000 | 91.000000 | 1014.000000 | 1.59 | 18.970000 | 3.830000 | 6641.000000 | 271.000000 | 1.87 | 1.610000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 17.230000 | 18.860000 | 92.000000 | 1013.000000 | 1.47 | 18.550000 | 2.350000 | 5023.000000 | 270.000000 | 1.89 | 1.520000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 17.110000 | 18.410000 | 94.000000 | 1013.000000 | 1.54 | 18.090000 | 1.050000 | 7923.000000 | 258.000000 | 1.9 | 1.400000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 16.920000 | 17.880000 | 96.000000 | 1014.000000 | 1.14 | 17.560000 | 0.240000 | 8409.000000 | 255.000000 | 1.93 | 1.130000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26035030 | "AEROPUERTO G L VALENCIA [26035030]" | 2.452889 | -76.608750 | 1752.000000 | Climática Principal | Convencional | Activa | 1941-06-15 00:00:00 | NaT | Cauca | Popayán | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 23:00:00 | 90.000000 | 16.040000 | 16.610000 | 98.000000 | 1015.000000 | 0.86 | 16.360000 | 0.000000 | 7619.000000 | 250.000000 | 1.47 | 0.910000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26035030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26035030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26035030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26035030_OWM_Windspeed_20220111.png)
