
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SINDAGUA [52055090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.10758333,-77.38936111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.10758333&lon=-77.38936111)


| Parameter | Value |
|---|---|
| Code | 52055090 |
| Name | SINDAGUA [52055090] |
| Latitude, ° | 1.10758333 |
| Longitude, ° | -77.38936111 |
| Elevation, m | 2800 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1987-07-15 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Tangua |
| Stream | Putumayo |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Guáitara |

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

### (CNE index 3703) Open Weather values for station 52055090 - SINDAGUA [52055090]

JSON data from API OWM:

```
{'lat': 1.1076, 'lon': -77.3894, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813305, 'sunset': 1641856721, 'temp': 12.57, 'feels_like': 12.13, 'pressure': 1014, 'humidity': 86, 'dew_point': 10.29, 'uvi': 4.56, 'clouds': 94, 'visibility': 6885, 'wind_speed': 2.3, 'wind_deg': 330, 'wind_gust': 2.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, 'hourly': [{'dt': 1641772800, 'temp': 11.89, 'feels_like': 11.59, 'pressure': 1016, 'humidity': 94, 'dew_point': 10.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 341, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 10.71, 'feels_like': 10.29, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 351, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 10.5, 'feels_like': 10.09, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.73, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 352, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 10.46, 'feels_like': 10.04, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.69, 'uvi': 0, 'clouds': 100, 'visibility': 8902, 'wind_speed': 0.14, 'wind_deg': 307, 'wind_gust': 0.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10.41, 'feels_like': 9.99, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 180, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.39, 'feels_like': 9.94, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 228, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.33, 'feels_like': 9.85, 'pressure': 1018, 'humidity': 93, 'dew_point': 9.25, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 266, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 10.15, 'feels_like': 9.68, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.23, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 256, 'wind_gust': 0.89, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.82, 'feels_like': 9.82, 'pressure': 1017, 'humidity': 94, 'dew_point': 8.9, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 260, 'wind_gust': 0.93, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.65, 'feels_like': 9.65, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.89, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 299, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1018, 'humidity': 95, 'dew_point': 8.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 233, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 8.89, 'feels_like': 8.89, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 261, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.89, 'feels_like': 8.89, 'pressure': 1019, 'humidity': 93, 'dew_point': 7.82, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 209, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 10.02, 'feels_like': 9.38, 'pressure': 1019, 'humidity': 88, 'dew_point': 8.13, 'uvi': 1.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 276, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 11.39, 'feels_like': 10.67, 'pressure': 1018, 'humidity': 80, 'dew_point': 8.07, 'uvi': 2.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 330, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 13.39, 'feels_like': 12.77, 'pressure': 1018, 'humidity': 76, 'dew_point': 9.25, 'uvi': 5.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 340, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641830400, 'temp': 13.75, 'feels_like': 13.24, 'pressure': 1017, 'humidity': 79, 'dew_point': 10.18, 'uvi': 8.9, 'clouds': 100, 'visibility': 7351, 'wind_speed': 2.27, 'wind_deg': 346, 'wind_gust': 2.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641834000, 'temp': 14.39, 'feels_like': 14.05, 'pressure': 1016, 'humidity': 83, 'dew_point': 11.54, 'uvi': 10.03, 'clouds': 100, 'visibility': 6141, 'wind_speed': 2.22, 'wind_deg': 345, 'wind_gust': 2.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}, {'dt': 1641837600, 'temp': 14.57, 'feels_like': 14.28, 'pressure': 1016, 'humidity': 84, 'dew_point': 11.9, 'uvi': 9.45, 'clouds': 86, 'visibility': 6896, 'wind_speed': 2.12, 'wind_deg': 342, 'wind_gust': 2.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.97}}, {'dt': 1641841200, 'temp': 13.93, 'feels_like': 13.57, 'pressure': 1014, 'humidity': 84, 'dew_point': 11.27, 'uvi': 7.32, 'clouds': 100, 'visibility': 5818, 'wind_speed': 2.23, 'wind_deg': 331, 'wind_gust': 2.42, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641844800, 'temp': 12.57, 'feels_like': 12.13, 'pressure': 1014, 'humidity': 86, 'dew_point': 10.29, 'uvi': 4.56, 'clouds': 94, 'visibility': 6885, 'wind_speed': 2.3, 'wind_deg': 330, 'wind_gust': 2.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641848400, 'temp': 12.2, 'feels_like': 11.8, 'pressure': 1014, 'humidity': 89, 'dew_point': 10.44, 'uvi': 2.07, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 331, 'wind_gust': 2.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.82}}, {'dt': 1641852000, 'temp': 12.02, 'feels_like': 11.68, 'pressure': 1015, 'humidity': 92, 'dew_point': 10.76, 'uvi': 0.62, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 328, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641855600, 'temp': 10.89, 'feels_like': 10.52, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.12, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 325, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 10.960000 | 11.590000 | 94.000000 | 1016.000000 |  | 11.890000 | 0.000000 | 10000.000000 | 341.000000 | 1.34 | 1.130000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.780000 | 10.290000 | 94.000000 | 1018.000000 |  | 10.710000 | 0.000000 | 10000.000000 | 351.000000 | 1.11 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 9.730000 | 10.090000 | 95.000000 | 1019.000000 |  | 10.500000 | 0.000000 | 10000.000000 | 352.000000 | 0.76 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.690000 | 10.040000 | 95.000000 | 1019.000000 |  | 10.460000 | 0.000000 | 8902.000000 | 307.000000 | 0.6 | 0.140000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.640000 | 9.990000 | 95.000000 | 1019.000000 |  | 10.410000 | 0.000000 | 10000.000000 | 180.000000 | 0.44 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 9.470000 | 9.940000 | 94.000000 | 1018.000000 |  | 10.390000 | 0.000000 | 10000.000000 | 228.000000 | 0.56 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 9.250000 | 9.850000 | 93.000000 | 1018.000000 |  | 10.330000 | 0.000000 | 10000.000000 | 266.000000 | 0.74 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 9.230000 | 9.680000 | 94.000000 | 1017.000000 |  | 10.150000 | 0.000000 | 10000.000000 | 256.000000 | 0.89 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 8.900000 | 9.820000 | 94.000000 | 1017.000000 |  | 9.820000 | 0.000000 | 10000.000000 | 260.000000 | 0.93 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 8.890000 | 9.650000 | 95.000000 | 1016.000000 |  | 9.650000 | 0.000000 | 10000.000000 | 299.000000 | 1.05 | 0.770000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 8.610000 | 9.370000 | 95.000000 | 1018.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 233.000000 | 0.73 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 7.980000 | 8.890000 | 94.000000 | 1018.000000 |  | 8.890000 | 0.000000 | 10000.000000 | 261.000000 | 0.86 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 7.820000 | 8.890000 | 93.000000 | 1019.000000 |  | 8.890000 | 0.260000 | 10000.000000 | 209.000000 | 1.03 | 0.800000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 8.130000 | 9.380000 | 88.000000 | 1019.000000 |  | 10.020000 | 1.160000 | 10000.000000 | 276.000000 | 0.77 | 0.580000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 8.070000 | 10.670000 | 80.000000 | 1018.000000 |  | 11.390000 | 2.970000 | 10000.000000 | 330.000000 | 1 | 0.980000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 9.250000 | 12.770000 | 76.000000 | 1018.000000 | 0.3 | 13.390000 | 5.220000 | 10000.000000 | 340.000000 | 1.69 | 1.840000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 10.180000 | 13.240000 | 79.000000 | 1017.000000 | 0.72 | 13.750000 | 8.900000 | 7351.000000 | 346.000000 | 2.12 | 2.270000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 11.540000 | 14.050000 | 83.000000 | 1016.000000 | 0.95 | 14.390000 | 10.030000 | 6141.000000 | 345.000000 | 2.12 | 2.220000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 18:00:00 | 86.000000 | 11.900000 | 14.280000 | 84.000000 | 1016.000000 | 0.97 | 14.570000 | 9.450000 | 6896.000000 | 342.000000 | 2.08 | 2.120000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 11.270000 | 13.570000 | 84.000000 | 1014.000000 | 1.08 | 13.930000 | 7.320000 | 5818.000000 | 331.000000 | 2.42 | 2.230000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 20:00:00 | 94.000000 | 10.290000 | 12.130000 | 86.000000 | 1014.000000 | 1.02 | 12.570000 | 4.560000 | 6885.000000 | 330.000000 | 2.48 | 2.300000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 21:00:00 | 96.000000 | 10.440000 | 11.800000 | 89.000000 | 1014.000000 | 0.82 | 12.200000 | 2.070000 | 10000.000000 | 331.000000 | 2.45 | 2.170000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 22:00:00 | 97.000000 | 10.760000 | 11.680000 | 92.000000 | 1015.000000 | 0.52 | 12.020000 | 0.620000 | 10000.000000 | 328.000000 | 2.32 | 1.920000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055090 | "SINDAGUA [52055090]" | 1.107583 | -77.389361 | 2800.000000 | Climática Principal | Convencional | Activa | 1987-07-15 00:00:00 | NaT | Nariño | Tangua | Putumayo | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 23:00:00 | 97.000000 | 10.120000 | 10.520000 | 95.000000 | 1016.000000 | 0.34 | 10.890000 | 0.000000 | 10000.000000 | 325.000000 | 2.24 | 1.710000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055090_OWM_Windspeed_20220111.png)
