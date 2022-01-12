
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - METROMEDELLIN - AUT [27015310] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station27015310_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.32975,-75.55211111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.32975&lon=-75.55211111)


| Parameter | Value |
|---|---|
| Code | 27015310 |
| Name | METROMEDELLIN - AUT [27015310] |
| Latitude, ° | 6.32975 |
| Longitude, ° | -75.55211111 |
| Elevation, m | 1440 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-30 19:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Bello |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Nechí |
| SZH - Hydrographic subzone | Río Porce |

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

### (CNE index 296) Open Weather values for station 27015310 - METROMEDELLIN - AUT [27015310]

JSON data from API OWM:

```
{'lat': 6.3298, 'lon': -75.5521, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813370, 'sunset': 1641855774, 'temp': 25.31, 'feels_like': 25.28, 'pressure': 1018, 'humidity': 53, 'dew_point': 15.05, 'uvi': 3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, 'hourly': [{'dt': 1641772800, 'temp': 22.29, 'feels_like': 22.35, 'pressure': 1018, 'humidity': 68, 'dew_point': 16.1, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 360, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641776400, 'temp': 20.28, 'feels_like': 20.9, 'pressure': 1016, 'humidity': 97, 'dew_point': 19.79, 'uvi': 0, 'clouds': 90, 'visibility': 5421, 'wind_speed': 1.11, 'wind_deg': 61, 'wind_gust': 2.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641780000, 'temp': 20.19, 'feels_like': 20.8, 'pressure': 1017, 'humidity': 97, 'dew_point': 19.7, 'uvi': 0, 'clouds': 90, 'visibility': 5497, 'wind_speed': 0.9, 'wind_deg': 71, 'wind_gust': 1.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 20.19, 'feels_like': 20.82, 'pressure': 1017, 'humidity': 98, 'dew_point': 19.86, 'uvi': 0, 'clouds': 93, 'visibility': 5401, 'wind_speed': 0.84, 'wind_deg': 75, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 20.19, 'feels_like': 20.82, 'pressure': 1017, 'humidity': 98, 'dew_point': 19.86, 'uvi': 0, 'clouds': 94, 'visibility': 5377, 'wind_speed': 0.53, 'wind_deg': 86, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 18.59, 'feels_like': 19.06, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.27, 'uvi': 0, 'clouds': 93, 'visibility': 5403, 'wind_speed': 0.68, 'wind_deg': 86, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.59, 'feels_like': 19.06, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.27, 'uvi': 0, 'clouds': 87, 'visibility': 7870, 'wind_speed': 0.54, 'wind_deg': 71, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 18.59, 'feels_like': 19.06, 'pressure': 1015, 'humidity': 98, 'dew_point': 18.27, 'uvi': 0, 'clouds': 96, 'visibility': 8255, 'wind_speed': 0.42, 'wind_deg': 60, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 18.07, 'feels_like': 18.49, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.75, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 52, 'wind_gust': 0.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 17.99, 'feels_like': 18.4, 'pressure': 1015, 'humidity': 98, 'dew_point': 17.67, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 22, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641808800, 'temp': 18.07, 'feels_like': 18.49, 'pressure': 1015, 'humidity': 98, 'dew_point': 17.75, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 342, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641812400, 'temp': 18.4, 'feels_like': 18.75, 'pressure': 1019, 'humidity': 94, 'dew_point': 17.42, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641816000, 'temp': 18.45, 'feels_like': 18.65, 'pressure': 1021, 'humidity': 88, 'dew_point': 16.43, 'uvi': 0.27, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 20, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 20.37, 'feels_like': 20.47, 'pressure': 1022, 'humidity': 77, 'dew_point': 16.21, 'uvi': 1.52, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 20, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 21.38, 'feels_like': 21.48, 'pressure': 1022, 'humidity': 73, 'dew_point': 16.34, 'uvi': 3.85, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641826800, 'temp': 21.33, 'feels_like': 21.29, 'pressure': 1022, 'humidity': 68, 'dew_point': 15.19, 'uvi': 6.75, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641830400, 'temp': 20.53, 'feels_like': 20.65, 'pressure': 1022, 'humidity': 77, 'dew_point': 16.36, 'uvi': 6.84, 'clouds': 90, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 180, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641834000, 'temp': 20.48, 'feels_like': 20.59, 'pressure': 1022, 'humidity': 77, 'dew_point': 16.31, 'uvi': 7.6, 'clouds': 90, 'visibility': 8000, 'wind_speed': 2.57, 'wind_deg': 230, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641837600, 'temp': 22.33, 'feels_like': 22.39, 'pressure': 1021, 'humidity': 68, 'dew_point': 16.14, 'uvi': 7.01, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 210, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641841200, 'temp': 23.48, 'feels_like': 23.45, 'pressure': 1019, 'humidity': 60, 'dew_point': 15.27, 'uvi': 5.06, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.06}}, {'dt': 1641844800, 'temp': 25.31, 'feels_like': 25.28, 'pressure': 1018, 'humidity': 53, 'dew_point': 15.05, 'uvi': 3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641848400, 'temp': 24.31, 'feels_like': 24.18, 'pressure': 1017, 'humidity': 53, 'dew_point': 14.13, 'uvi': 1.25, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641852000, 'temp': 23.35, 'feels_like': 23.31, 'pressure': 1018, 'humidity': 60, 'dew_point': 15.15, 'uvi': 0.14, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641855600, 'temp': 21.43, 'feels_like': 21.53, 'pressure': 1019, 'humidity': 73, 'dew_point': 16.39, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 00:00:00 | 75.000000 | 16.100000 | 22.350000 | 68.000000 | 1018.000000 | 0.42 | 22.290000 | 0.000000 | 10000.000000 | 360.000000 |  | 5.140000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 01:00:00 | 90.000000 | 19.790000 | 20.900000 | 97.000000 | 1016.000000 | 0.15 | 20.280000 | 0.000000 | 5421.000000 | 61.000000 | 2.25 | 1.110000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 02:00:00 | 90.000000 | 19.700000 | 20.800000 | 97.000000 | 1017.000000 |  | 20.190000 | 0.000000 | 5497.000000 | 71.000000 | 1.55 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 03:00:00 | 93.000000 | 19.860000 | 20.820000 | 98.000000 | 1017.000000 |  | 20.190000 | 0.000000 | 5401.000000 | 75.000000 | 1.24 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 19.860000 | 20.820000 | 98.000000 | 1017.000000 |  | 20.190000 | 0.000000 | 5377.000000 | 86.000000 | 0.76 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 18.270000 | 19.060000 | 98.000000 | 1016.000000 |  | 18.590000 | 0.000000 | 5403.000000 | 86.000000 | 0.9 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 06:00:00 | 87.000000 | 18.270000 | 19.060000 | 98.000000 | 1016.000000 |  | 18.590000 | 0.000000 | 7870.000000 | 71.000000 | 0.83 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 18.270000 | 19.060000 | 98.000000 | 1015.000000 |  | 18.590000 | 0.000000 | 8255.000000 | 60.000000 | 0.66 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 17.750000 | 18.490000 | 98.000000 | 1014.000000 |  | 18.070000 | 0.000000 | 10000.000000 | 52.000000 | 0.85 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 09:00:00 | 93.000000 | 17.670000 | 18.400000 | 98.000000 | 1015.000000 | 0.11 | 17.990000 | 0.000000 | 10000.000000 | 22.000000 | 0.86 | 0.570000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 10:00:00 | 92.000000 | 17.750000 | 18.490000 | 98.000000 | 1015.000000 | 0.16 | 18.070000 | 0.000000 | 10000.000000 | 342.000000 | 0.65 | 0.380000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 17.420000 | 18.750000 | 94.000000 | 1019.000000 | 0.1 | 18.400000 | 0.000000 | 10000.000000 | 20.000000 |  | 3.090000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 12:00:00 | 90.000000 | 16.430000 | 18.650000 | 88.000000 | 1021.000000 |  | 18.450000 | 0.270000 | 10000.000000 | 20.000000 |  | 2.570000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 13:00:00 | 90.000000 | 16.210000 | 20.470000 | 77.000000 | 1022.000000 |  | 20.370000 | 1.520000 | 10000.000000 | 20.000000 |  | 3.090000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 14:00:00 | 90.000000 | 16.340000 | 21.480000 | 73.000000 | 1022.000000 | 0.13 | 21.380000 | 3.850000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 15:00:00 | 90.000000 | 15.190000 | 21.290000 | 68.000000 | 1022.000000 | 0.25 | 21.330000 | 6.750000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 16:00:00 | 90.000000 | 16.360000 | 20.650000 | 77.000000 | 1022.000000 | 0.33 | 20.530000 | 6.840000 | 10000.000000 | 180.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 16.310000 | 20.590000 | 77.000000 | 1022.000000 | 0.29 | 20.480000 | 7.600000 | 8000.000000 | 230.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 16.140000 | 22.390000 | 68.000000 | 1021.000000 | 0.57 | 22.330000 | 7.010000 | 10000.000000 | 210.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 15.270000 | 23.450000 | 60.000000 | 1019.000000 | 1.06 | 23.480000 | 5.060000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 15.050000 | 25.280000 | 53.000000 | 1018.000000 | 1.13 | 25.310000 | 3.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 14.130000 | 24.180000 | 53.000000 | 1017.000000 | 1.14 | 24.310000 | 1.250000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 15.150000 | 23.310000 | 60.000000 | 1018.000000 | 0.52 | 23.350000 | 0.140000 | 10000.000000 | 10.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015310 | "METROMEDELLIN - AUT [27015310]" | 6.329750 | -75.552111 | 1440.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-30 19:00:00 | NaT | Antioquia | Bello | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 16.390000 | 21.530000 | 73.000000 | 1019.000000 | 0.3 | 21.430000 | 0.000000 | 10000.000000 | 10.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station27015310_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Rain_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Temp_20220111.png)
![CNE_IDEAM_Station27015310_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_UVI_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station27015310_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015310_OWM_Windspeed_20220111.png)
