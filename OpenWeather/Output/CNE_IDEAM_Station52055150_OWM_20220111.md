
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CERRO PARAMO  - AUT [52055150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=0.84311111,-77.38880556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=0.84311111&lon=-77.38880556)


| Parameter | Value |
|---|---|
| Code | 52055150 |
| Name | CERRO PARAMO  - AUT [52055150] |
| Latitude, ° | 0.84311111 |
| Longitude, ° | -77.38880556 |
| Elevation, m | 3585 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-08 19:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Puerres |
| Stream | 0 |
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

### (CNE index 8) Open Weather values for station 52055150 - CERRO PARAMO  - AUT [52055150]

JSON data from API OWM:

```
{'lat': 0.8431, 'lon': -77.3888, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813280, 'sunset': 1641856746, 'temp': 10.56, 'feels_like': 9.84, 'pressure': 1013, 'humidity': 83, 'dew_point': 7.8, 'uvi': 5.78, 'clouds': 93, 'visibility': 8878, 'wind_speed': 0.56, 'wind_deg': 10, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, 'hourly': [{'dt': 1641772800, 'temp': 9.18, 'feels_like': 9.18, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.42, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 15, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641776400, 'temp': 6.28, 'feels_like': 6.28, 'pressure': 1018, 'humidity': 96, 'dew_point': 5.69, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 20, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641780000, 'temp': 6.18, 'feels_like': 6.18, 'pressure': 1019, 'humidity': 96, 'dew_point': 5.59, 'uvi': 0, 'clouds': 100, 'visibility': 5838, 'wind_speed': 0.56, 'wind_deg': 16, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 6.05, 'feels_like': 6.05, 'pressure': 1019, 'humidity': 97, 'dew_point': 5.61, 'uvi': 0, 'clouds': 100, 'visibility': 3045, 'wind_speed': 0.34, 'wind_deg': 31, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641787200, 'temp': 5.93, 'feels_like': 5.93, 'pressure': 1019, 'humidity': 97, 'dew_point': 5.49, 'uvi': 0, 'clouds': 100, 'visibility': 2476, 'wind_speed': 0.08, 'wind_deg': 58, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 5.83, 'feels_like': 5.83, 'pressure': 1018, 'humidity': 97, 'dew_point': 5.39, 'uvi': 0, 'clouds': 100, 'visibility': 2656, 'wind_speed': 0.25, 'wind_deg': 265, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 5.61, 'feels_like': 5.61, 'pressure': 1018, 'humidity': 97, 'dew_point': 5.17, 'uvi': 0, 'clouds': 100, 'visibility': 7912, 'wind_speed': 0.53, 'wind_deg': 272, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 5.5, 'feels_like': 5.5, 'pressure': 1017, 'humidity': 97, 'dew_point': 5.06, 'uvi': 0, 'clouds': 100, 'visibility': 5392, 'wind_speed': 0.56, 'wind_deg': 279, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641801600, 'temp': 5.45, 'feels_like': 5.45, 'pressure': 1017, 'humidity': 96, 'dew_point': 4.86, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 290, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 5.22, 'feels_like': 5.22, 'pressure': 1017, 'humidity': 96, 'dew_point': 4.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 290, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.6, 'feels_like': 4.6, 'pressure': 1018, 'humidity': 96, 'dew_point': 4.02, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 274, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.18, 'feels_like': 3.18, 'pressure': 1018, 'humidity': 96, 'dew_point': 2.6, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 277, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 4.18, 'feels_like': 4.18, 'pressure': 1019, 'humidity': 94, 'dew_point': 3.3, 'uvi': 0.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 273, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 5.99, 'feels_like': 5.99, 'pressure': 1019, 'humidity': 88, 'dew_point': 4.16, 'uvi': 2.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 262, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 8.56, 'feels_like': 8.56, 'pressure': 1018, 'humidity': 79, 'dew_point': 5.13, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 120, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 10.99, 'feels_like': 10.05, 'pressure': 1017, 'humidity': 73, 'dew_point': 6.34, 'uvi': 9.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 79, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641830400, 'temp': 12.56, 'feels_like': 11.8, 'pressure': 1016, 'humidity': 74, 'dew_point': 8.06, 'uvi': 11.08, 'clouds': 100, 'visibility': 5772, 'wind_speed': 0.83, 'wind_deg': 67, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641834000, 'temp': 12.85, 'feels_like': 12.33, 'pressure': 1016, 'humidity': 82, 'dew_point': 9.86, 'uvi': 12.49, 'clouds': 100, 'visibility': 3760, 'wind_speed': 0.78, 'wind_deg': 61, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641837600, 'temp': 13.85, 'feels_like': 13.51, 'pressure': 1016, 'humidity': 85, 'dew_point': 11.37, 'uvi': 11.78, 'clouds': 79, 'visibility': 4363, 'wind_speed': 0.53, 'wind_deg': 88, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641841200, 'temp': 13.56, 'feels_like': 13.14, 'pressure': 1014, 'humidity': 83, 'dew_point': 10.73, 'uvi': 9.25, 'clouds': 97, 'visibility': 8223, 'wind_speed': 0.17, 'wind_deg': 53, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641844800, 'temp': 10.56, 'feels_like': 9.84, 'pressure': 1013, 'humidity': 83, 'dew_point': 7.8, 'uvi': 5.78, 'clouds': 93, 'visibility': 8878, 'wind_speed': 0.56, 'wind_deg': 10, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}, {'dt': 1641848400, 'temp': 8.99, 'feels_like': 8.99, 'pressure': 1013, 'humidity': 88, 'dew_point': 7.11, 'uvi': 2.62, 'clouds': 95, 'visibility': 8636, 'wind_speed': 0.82, 'wind_deg': 15, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.79}}, {'dt': 1641852000, 'temp': 8.42, 'feels_like': 8.42, 'pressure': 1014, 'humidity': 92, 'dew_point': 7.2, 'uvi': 0.66, 'clouds': 96, 'visibility': 6945, 'wind_speed': 0.81, 'wind_deg': 8, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641855600, 'temp': 8.18, 'feels_like': 8.18, 'pressure': 1015, 'humidity': 95, 'dew_point': 7.43, 'uvi': 0, 'clouds': 97, 'visibility': 6864, 'wind_speed': 0.79, 'wind_deg': 346, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 8.420000 | 9.180000 | 95.000000 | 1016.000000 | 0.2 | 9.180000 | 0.000000 | 10000.000000 | 15.000000 | 1.12 | 0.870000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 5.690000 | 6.280000 | 96.000000 | 1018.000000 | 0.18 | 6.280000 | 0.000000 | 10000.000000 | 20.000000 | 1.09 | 0.770000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 5.590000 | 6.180000 | 96.000000 | 1019.000000 | 0.13 | 6.180000 | 0.000000 | 5838.000000 | 16.000000 | 0.97 | 0.560000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 5.610000 | 6.050000 | 97.000000 | 1019.000000 | 0.16 | 6.050000 | 0.000000 | 3045.000000 | 31.000000 | 0.83 | 0.340000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 5.490000 | 5.930000 | 97.000000 | 1019.000000 |  | 5.930000 | 0.000000 | 2476.000000 | 58.000000 | 0.52 | 0.080000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 5.390000 | 5.830000 | 97.000000 | 1018.000000 |  | 5.830000 | 0.000000 | 2656.000000 | 265.000000 | 0.44 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 5.170000 | 5.610000 | 97.000000 | 1018.000000 |  | 5.610000 | 0.000000 | 7912.000000 | 272.000000 | 0.74 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 5.060000 | 5.500000 | 97.000000 | 1017.000000 | 0.14 | 5.500000 | 0.000000 | 5392.000000 | 279.000000 | 0.85 | 0.560000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 4.860000 | 5.450000 | 96.000000 | 1017.000000 |  | 5.450000 | 0.000000 | 10000.000000 | 290.000000 | 0.92 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 4.640000 | 5.220000 | 96.000000 | 1017.000000 |  | 5.220000 | 0.000000 | 10000.000000 | 290.000000 | 1.16 | 0.830000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 4.020000 | 4.600000 | 96.000000 | 1018.000000 |  | 4.600000 | 0.000000 | 10000.000000 | 274.000000 | 0.92 | 0.830000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 2.600000 | 3.180000 | 96.000000 | 1018.000000 |  | 3.180000 | 0.000000 | 10000.000000 | 277.000000 | 1.03 | 0.930000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 3.300000 | 4.180000 | 94.000000 | 1019.000000 |  | 4.180000 | 0.450000 | 10000.000000 | 273.000000 | 1.14 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 4.160000 | 5.990000 | 88.000000 | 1019.000000 |  | 5.990000 | 2.070000 | 10000.000000 | 262.000000 | 0.68 | 0.380000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 5.130000 | 8.560000 | 79.000000 | 1018.000000 |  | 8.560000 | 5.270000 | 10000.000000 | 120.000000 | 0.82 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 6.340000 | 10.050000 | 73.000000 | 1017.000000 | 0.22 | 10.990000 | 9.260000 | 10000.000000 | 79.000000 | 1.37 | 0.630000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 8.060000 | 11.800000 | 74.000000 | 1016.000000 | 0.39 | 12.560000 | 11.080000 | 5772.000000 | 67.000000 | 1.72 | 0.830000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 9.860000 | 12.330000 | 82.000000 | 1016.000000 | 0.62 | 12.850000 | 12.490000 | 3760.000000 | 61.000000 | 1.73 | 0.780000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 18:00:00 | 79.000000 | 11.370000 | 13.510000 | 85.000000 | 1016.000000 | 0.81 | 13.850000 | 11.780000 | 4363.000000 | 88.000000 | 1.47 | 0.530000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 19:00:00 | 97.000000 | 10.730000 | 13.140000 | 83.000000 | 1014.000000 | 0.88 | 13.560000 | 9.250000 | 8223.000000 | 53.000000 | 1.5 | 0.170000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 20:00:00 | 93.000000 | 7.800000 | 9.840000 | 83.000000 | 1013.000000 | 0.88 | 10.560000 | 5.780000 | 8878.000000 | 10.000000 | 1.66 | 0.560000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 21:00:00 | 95.000000 | 7.110000 | 8.990000 | 88.000000 | 1013.000000 | 0.79 | 8.990000 | 2.620000 | 8636.000000 | 15.000000 | 1.88 | 0.820000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 22:00:00 | 96.000000 | 7.200000 | 8.420000 | 92.000000 | 1014.000000 | 0.65 | 8.420000 | 0.660000 | 6945.000000 | 8.000000 | 1.9 | 0.810000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055150 | "CERRO PARAMO  - AUT [52055150]" | 0.843111 | -77.388806 | 3585.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-08 19:00:00 | NaT | Nariño | Puerres | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 23:00:00 | 97.000000 | 7.430000 | 8.180000 | 95.000000 | 1015.000000 | 0.37 | 8.180000 | 0.000000 | 6864.000000 | 346.000000 | 1.6 | 0.790000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055150_OWM_Windspeed_20220111.png)
