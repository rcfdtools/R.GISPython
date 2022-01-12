
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VALENCIA [44015030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44015030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.90041667,-76.66875) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.90041667&lon=-76.66875)


| Parameter | Value |
|---|---|
| Code | 44015030 |
| Name | VALENCIA [44015030] |
| Latitude, ° | 1.90041667 |
| Longitude, ° | -76.66875 |
| Elevation, m | 2900 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1971-04-15 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | San Sebastián |
| Stream | Caqueta |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Caquetá |
| SZH - Hydrographic subzone | Alto Caqueta |

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

### (CNE index 3629) Open Weather values for station 44015030 - VALENCIA [44015030]

JSON data from API OWM:

```
{'lat': 1.9004, 'lon': -76.6688, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813209, 'sunset': 1641856471, 'temp': 11.29, 'feels_like': 10.93, 'pressure': 1014, 'humidity': 94, 'dew_point': 10.36, 'uvi': 6.05, 'clouds': 100, 'visibility': 3940, 'wind_speed': 1.16, 'wind_deg': 279, 'wind_gust': 1.73, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.19}}, 'hourly': [{'dt': 1641772800, 'temp': 9.4, 'feels_like': 9.4, 'pressure': 1017, 'humidity': 98, 'dew_point': 9.1, 'uvi': 0, 'clouds': 100, 'visibility': 6625, 'wind_speed': 0.35, 'wind_deg': 262, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641776400, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 98, 'dew_point': 9.08, 'uvi': 0, 'clouds': 100, 'visibility': 6283, 'wind_speed': 0.58, 'wind_deg': 275, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641780000, 'temp': 9.25, 'feels_like': 9.25, 'pressure': 1019, 'humidity': 98, 'dew_point': 8.95, 'uvi': 0, 'clouds': 100, 'visibility': 6280, 'wind_speed': 0.57, 'wind_deg': 274, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641783600, 'temp': 9.31, 'feels_like': 9.31, 'pressure': 1019, 'humidity': 99, 'dew_point': 9.16, 'uvi': 0, 'clouds': 100, 'visibility': 6082, 'wind_speed': 0.55, 'wind_deg': 263, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 9.23, 'feels_like': 9.23, 'pressure': 1019, 'humidity': 99, 'dew_point': 9.08, 'uvi': 0, 'clouds': 100, 'visibility': 3537, 'wind_speed': 0.38, 'wind_deg': 246, 'wind_gust': 0.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 9.15, 'feels_like': 9.15, 'pressure': 1018, 'humidity': 99, 'dew_point': 9, 'uvi': 0, 'clouds': 100, 'visibility': 3624, 'wind_speed': 0.22, 'wind_deg': 232, 'wind_gust': 0.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 8.85, 'feels_like': 8.85, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.7, 'uvi': 0, 'clouds': 100, 'visibility': 4923, 'wind_speed': 0.35, 'wind_deg': 281, 'wind_gust': 0.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 8.7, 'feels_like': 8.7, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.55, 'uvi': 0, 'clouds': 100, 'visibility': 4304, 'wind_speed': 0.61, 'wind_deg': 289, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641801600, 'temp': 8.65, 'feels_like': 8.65, 'pressure': 1016, 'humidity': 99, 'dew_point': 8.5, 'uvi': 0, 'clouds': 100, 'visibility': 1738, 'wind_speed': 0.76, 'wind_deg': 295, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 8.66, 'feels_like': 8.66, 'pressure': 1016, 'humidity': 99, 'dew_point': 8.51, 'uvi': 0, 'clouds': 100, 'visibility': 1547, 'wind_speed': 0.72, 'wind_deg': 296, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 8.57, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.42, 'uvi': 0, 'clouds': 100, 'visibility': 1823, 'wind_speed': 0.75, 'wind_deg': 301, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641812400, 'temp': 8.26, 'feels_like': 8.26, 'pressure': 1018, 'humidity': 99, 'dew_point': 8.11, 'uvi': 0, 'clouds': 100, 'visibility': 3493, 'wind_speed': 0.86, 'wind_deg': 287, 'wind_gust': 1.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 9.03, 'feels_like': 9.03, 'pressure': 1018, 'humidity': 99, 'dew_point': 8.88, 'uvi': 0.42, 'clouds': 100, 'visibility': 3956, 'wind_speed': 0.76, 'wind_deg': 316, 'wind_gust': 1.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 9.88, 'feels_like': 9.88, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.27, 'uvi': 1.32, 'clouds': 100, 'visibility': 9286, 'wind_speed': 0.63, 'wind_deg': 294, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641823200, 'temp': 10.57, 'feels_like': 10.11, 'pressure': 1019, 'humidity': 93, 'dew_point': 9.49, 'uvi': 3.35, 'clouds': 98, 'visibility': 9825, 'wind_speed': 0.6, 'wind_deg': 305, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641826800, 'temp': 11.12, 'feels_like': 10.66, 'pressure': 1019, 'humidity': 91, 'dew_point': 9.71, 'uvi': 5.85, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 305, 'wind_gust': 1.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641830400, 'temp': 11.89, 'feels_like': 11.48, 'pressure': 1018, 'humidity': 90, 'dew_point': 10.3, 'uvi': 11.43, 'clouds': 99, 'visibility': 5962, 'wind_speed': 1.04, 'wind_deg': 284, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, {'dt': 1641834000, 'temp': 12.68, 'feels_like': 12.33, 'pressure': 1017, 'humidity': 89, 'dew_point': 10.92, 'uvi': 12.81, 'clouds': 99, 'visibility': 7264, 'wind_speed': 1.07, 'wind_deg': 283, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641837600, 'temp': 12.03, 'feels_like': 11.69, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.77, 'uvi': 11.99, 'clouds': 98, 'visibility': 7980, 'wind_speed': 0.95, 'wind_deg': 285, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641841200, 'temp': 11.61, 'feels_like': 11.25, 'pressure': 1015, 'humidity': 93, 'dew_point': 10.52, 'uvi': 9.82, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 290, 'wind_gust': 1.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.11}}, {'dt': 1641844800, 'temp': 11.29, 'feels_like': 10.93, 'pressure': 1014, 'humidity': 94, 'dew_point': 10.36, 'uvi': 6.05, 'clouds': 100, 'visibility': 3940, 'wind_speed': 1.16, 'wind_deg': 279, 'wind_gust': 1.73, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.19}}, {'dt': 1641848400, 'temp': 10.75, 'feels_like': 10.39, 'pressure': 1014, 'humidity': 96, 'dew_point': 10.14, 'uvi': 2.71, 'clouds': 98, 'visibility': 3169, 'wind_speed': 1.16, 'wind_deg': 274, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.97}}, {'dt': 1641852000, 'temp': 10.36, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 97, 'dew_point': 9.91, 'uvi': 0.7, 'clouds': 98, 'visibility': 3918, 'wind_speed': 0.99, 'wind_deg': 278, 'wind_gust': 1.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.64}}, {'dt': 1641855600, 'temp': 9.64, 'feels_like': 9.64, 'pressure': 1016, 'humidity': 98, 'dew_point': 9.34, 'uvi': 0, 'clouds': 96, 'visibility': 3801, 'wind_speed': 0.92, 'wind_deg': 281, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 9.100000 | 9.400000 | 98.000000 | 1017.000000 | 0.49 | 9.400000 | 0.000000 | 6625.000000 | 262.000000 | 0.94 | 0.350000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.080000 | 9.380000 | 98.000000 | 1018.000000 | 0.3 | 9.380000 | 0.000000 | 6283.000000 | 275.000000 | 1.07 | 0.580000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 8.950000 | 9.250000 | 98.000000 | 1019.000000 | 0.18 | 9.250000 | 0.000000 | 6280.000000 | 274.000000 | 1.02 | 0.570000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.160000 | 9.310000 | 99.000000 | 1019.000000 |  | 9.310000 | 0.000000 | 6082.000000 | 263.000000 | 1.05 | 0.550000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.080000 | 9.230000 | 99.000000 | 1019.000000 | 0.13 | 9.230000 | 0.000000 | 3537.000000 | 246.000000 | 0.78 | 0.380000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 9.000000 | 9.150000 | 99.000000 | 1018.000000 |  | 9.150000 | 0.000000 | 3624.000000 | 232.000000 | 0.43 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 8.700000 | 8.850000 | 99.000000 | 1017.000000 |  | 8.850000 | 0.000000 | 4923.000000 | 281.000000 | 0.53 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 8.550000 | 8.700000 | 99.000000 | 1017.000000 | 0.13 | 8.700000 | 0.000000 | 4304.000000 | 289.000000 | 0.9 | 0.610000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 8.500000 | 8.650000 | 99.000000 | 1016.000000 | 0.15 | 8.650000 | 0.000000 | 1738.000000 | 295.000000 | 1.13 | 0.760000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 8.510000 | 8.660000 | 99.000000 | 1016.000000 | 0.23 | 8.660000 | 0.000000 | 1547.000000 | 296.000000 | 1.16 | 0.720000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 8.420000 | 8.570000 | 99.000000 | 1017.000000 | 0.11 | 8.570000 | 0.000000 | 1823.000000 | 301.000000 | 1.2 | 0.750000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 8.110000 | 8.260000 | 99.000000 | 1018.000000 | 0.12 | 8.260000 | 0.000000 | 3493.000000 | 287.000000 | 1.28 | 0.860000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 8.880000 | 9.030000 | 99.000000 | 1018.000000 |  | 9.030000 | 0.420000 | 3956.000000 | 316.000000 | 1.3 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 9.270000 | 9.880000 | 96.000000 | 1019.000000 | 0.15 | 9.880000 | 1.320000 | 9286.000000 | 294.000000 | 0.98 | 0.630000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 9.490000 | 10.110000 | 93.000000 | 1019.000000 | 0.39 | 10.570000 | 3.350000 | 9825.000000 | 305.000000 | 0.99 | 0.600000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 15:00:00 | 99.000000 | 9.710000 | 10.660000 | 91.000000 | 1019.000000 | 0.56 | 11.120000 | 5.850000 | 10000.000000 | 305.000000 | 1.35 | 0.840000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 10.300000 | 11.480000 | 90.000000 | 1018.000000 | 0.71 | 11.890000 | 11.430000 | 5962.000000 | 284.000000 | 1.37 | 1.040000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 17:00:00 | 99.000000 | 10.920000 | 12.330000 | 89.000000 | 1017.000000 | 1.09 | 12.680000 | 12.810000 | 7264.000000 | 283.000000 | 1.39 | 1.070000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 10.770000 | 11.690000 | 92.000000 | 1016.000000 | 1.18 | 12.030000 | 11.990000 | 7980.000000 | 285.000000 | 1.39 | 0.950000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 10.520000 | 11.250000 | 93.000000 | 1015.000000 | 1.11 | 11.610000 | 9.820000 | 10000.000000 | 290.000000 | 1.34 | 0.980000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 10.360000 | 10.930000 | 94.000000 | 1014.000000 | 1.19 | 11.290000 | 6.050000 | 3940.000000 | 279.000000 | 1.73 | 1.160000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 10.140000 | 10.390000 | 96.000000 | 1014.000000 | 0.97 | 10.750000 | 2.710000 | 3169.000000 | 274.000000 | 1.69 | 1.160000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 9.910000 | 9.980000 | 97.000000 | 1015.000000 | 0.64 | 10.360000 | 0.700000 | 3918.000000 | 278.000000 | 1.59 | 0.990000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015030 | "VALENCIA [44015030]" | 1.900417 | -76.668750 | 2900.000000 | Climática Principal | Convencional | Activa | 1971-04-15 00:00:00 | NaT | Cauca | San Sebastián | Caqueta | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 9.340000 | 9.640000 | 98.000000 | 1016.000000 | 0.57 | 9.640000 | 0.000000 | 3801.000000 | 281.000000 | 1.53 | 0.920000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station44015030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44015030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44015030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015030_OWM_Windspeed_20220111.png)
