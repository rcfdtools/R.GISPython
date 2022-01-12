
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BONANZA [53045010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station53045010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.56666667,-77.88333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.56666667&lon=-77.88333333)


| Parameter | Value |
|---|---|
| Code | 53045010 |
| Name | BONANZA [53045010] |
| Latitude, ° | 2.56666667 |
| Longitude, ° | -77.88333333 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1966-10-15 00:00:00 |
| Suspension date | 2008-03-31 00:00:00 |
| State | Cauca |
| County | Guapi |
| Stream | Neiva |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Tapaje - Dagua - Directos |
| SZH - Hydrographic subzone | Río Guapi |

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

### (CNE index 3910) Open Weather values for station 53045010 - BONANZA [53045010]

JSON data from API OWM:

```
{'lat': 2.5667, 'lon': -77.8833, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813565, 'sunset': 1641856699, 'temp': 25.93, 'feels_like': 26.85, 'pressure': 1011, 'humidity': 87, 'dew_point': 23.6, 'uvi': 5.73, 'clouds': 83, 'visibility': 7096, 'wind_speed': 2.36, 'wind_deg': 275, 'wind_gust': 3.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.41}}, 'hourly': [{'dt': 1641772800, 'temp': 23.89, 'feels_like': 24.74, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.51, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 246, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.66}}, {'dt': 1641776400, 'temp': 23.57, 'feels_like': 24.44, 'pressure': 1012, 'humidity': 94, 'dew_point': 22.55, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 219, 'wind_gust': 1.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.79}}, {'dt': 1641780000, 'temp': 23.5, 'feels_like': 24.36, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.48, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 194, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 23.38, 'feels_like': 24.25, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.53, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 179, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 23.13, 'feels_like': 24.01, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.46, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 184, 'wind_gust': 2.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.94, 'feels_like': 23.8, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.27, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 188, 'wind_gust': 2.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641794400, 'temp': 22.93, 'feels_like': 23.79, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.26, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 197, 'wind_gust': 3.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641798000, 'temp': 22.78, 'feels_like': 23.65, 'pressure': 1012, 'humidity': 97, 'dew_point': 22.28, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 202, 'wind_gust': 4.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641801600, 'temp': 22.63, 'feels_like': 23.48, 'pressure': 1011, 'humidity': 97, 'dew_point': 22.13, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 194, 'wind_gust': 5.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641805200, 'temp': 22.5, 'feels_like': 23.34, 'pressure': 1011, 'humidity': 97, 'dew_point': 22, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 193, 'wind_gust': 5.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641808800, 'temp': 22.4, 'feels_like': 23.23, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.9, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 196, 'wind_gust': 5.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1641812400, 'temp': 22.35, 'feels_like': 23.17, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.85, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 193, 'wind_gust': 5.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641816000, 'temp': 22.82, 'feels_like': 23.66, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.15, 'uvi': 0.32, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 195, 'wind_gust': 5.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641819600, 'temp': 24.19, 'feels_like': 25.07, 'pressure': 1014, 'humidity': 92, 'dew_point': 22.81, 'uvi': 1.69, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 201, 'wind_gust': 4.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641823200, 'temp': 25.44, 'feels_like': 26.34, 'pressure': 1014, 'humidity': 88, 'dew_point': 23.31, 'uvi': 4.41, 'clouds': 94, 'visibility': 7616, 'wind_speed': 2.55, 'wind_deg': 223, 'wind_gust': 5.17, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641826800, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1015, 'humidity': 86, 'dew_point': 23.53, 'uvi': 7.89, 'clouds': 95, 'visibility': 10000, 'wind_speed': 3.08, 'wind_deg': 238, 'wind_gust': 5.1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.38}}, {'dt': 1641830400, 'temp': 26.44, 'feels_like': 26.44, 'pressure': 1014, 'humidity': 85, 'dew_point': 23.71, 'uvi': 11.02, 'clouds': 90, 'visibility': 8815, 'wind_speed': 3.32, 'wind_deg': 248, 'wind_gust': 4.9, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.24}}, {'dt': 1641834000, 'temp': 26.58, 'feels_like': 26.58, 'pressure': 1013, 'humidity': 85, 'dew_point': 23.85, 'uvi': 12.51, 'clouds': 91, 'visibility': 6163, 'wind_speed': 3.15, 'wind_deg': 258, 'wind_gust': 4.44, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.6}}, {'dt': 1641837600, 'temp': 26.26, 'feels_like': 26.26, 'pressure': 1013, 'humidity': 86, 'dew_point': 23.73, 'uvi': 11.84, 'clouds': 70, 'visibility': 8540, 'wind_speed': 2.76, 'wind_deg': 272, 'wind_gust': 4.18, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.64}}, {'dt': 1641841200, 'temp': 26.08, 'feels_like': 26.08, 'pressure': 1012, 'humidity': 86, 'dew_point': 23.55, 'uvi': 9.16, 'clouds': 89, 'visibility': 8914, 'wind_speed': 2.59, 'wind_deg': 275, 'wind_gust': 4.01, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.49}}, {'dt': 1641844800, 'temp': 25.93, 'feels_like': 26.85, 'pressure': 1011, 'humidity': 87, 'dew_point': 23.6, 'uvi': 5.73, 'clouds': 83, 'visibility': 7096, 'wind_speed': 2.36, 'wind_deg': 275, 'wind_gust': 3.62, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.41}}, {'dt': 1641848400, 'temp': 25.56, 'feels_like': 26.47, 'pressure': 1010, 'humidity': 88, 'dew_point': 23.42, 'uvi': 2.6, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 273, 'wind_gust': 3.27, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1641852000, 'temp': 25.12, 'feels_like': 26.06, 'pressure': 1011, 'humidity': 91, 'dew_point': 23.55, 'uvi': 0.65, 'clouds': 78, 'visibility': 9293, 'wind_speed': 1.54, 'wind_deg': 269, 'wind_gust': 3.1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.31}}, {'dt': 1641855600, 'temp': 24.09, 'feels_like': 24.96, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.71, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 252, 'wind_gust': 2.42, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.52}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.510000 | 24.740000 | 92.000000 | 1011.000000 | 0.66 | 23.890000 | 0.000000 | 10000.000000 | 246.000000 | 1.5 | 1.190000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 22.550000 | 24.440000 | 94.000000 | 1012.000000 | 0.79 | 23.570000 | 0.000000 | 10000.000000 | 219.000000 | 1.47 | 1.190000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 02:00:00 | 94.000000 | 22.480000 | 24.360000 | 94.000000 | 1013.000000 | 0.13 | 23.500000 | 0.000000 | 10000.000000 | 194.000000 | 1.53 | 1.340000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 03:00:00 | 96.000000 | 22.530000 | 24.250000 | 95.000000 | 1013.000000 |  | 23.380000 | 0.000000 | 10000.000000 | 179.000000 | 2.06 | 1.680000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 04:00:00 | 97.000000 | 22.460000 | 24.010000 | 96.000000 | 1013.000000 |  | 23.130000 | 0.000000 | 10000.000000 | 184.000000 | 2.74 | 1.860000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 22.270000 | 23.800000 | 96.000000 | 1013.000000 | 0.16 | 22.940000 | 0.000000 | 10000.000000 | 188.000000 | 2.84 | 1.820000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 06:00:00 | 88.000000 | 22.260000 | 23.790000 | 96.000000 | 1012.000000 | 0.22 | 22.930000 | 0.000000 | 10000.000000 | 197.000000 | 3.74 | 1.870000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 22.280000 | 23.650000 | 97.000000 | 1012.000000 | 0.34 | 22.780000 | 0.000000 | 10000.000000 | 202.000000 | 4.82 | 2.020000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 08:00:00 | 90.000000 | 22.130000 | 23.480000 | 97.000000 | 1011.000000 | 0.28 | 22.630000 | 0.000000 | 10000.000000 | 194.000000 | 5.22 | 2.100000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 09:00:00 | 92.000000 | 22.000000 | 23.340000 | 97.000000 | 1011.000000 | 0.34 | 22.500000 | 0.000000 | 10000.000000 | 193.000000 | 5.57 | 2.230000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 10:00:00 | 88.000000 | 21.900000 | 23.230000 | 97.000000 | 1012.000000 | 0.47 | 22.400000 | 0.000000 | 10000.000000 | 196.000000 | 5.64 | 2.260000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 11:00:00 | 87.000000 | 21.850000 | 23.170000 | 97.000000 | 1012.000000 | 0.5 | 22.350000 | 0.000000 | 10000.000000 | 193.000000 | 5.62 | 2.280000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 12:00:00 | 92.000000 | 22.150000 | 23.660000 | 96.000000 | 1013.000000 | 0.33 | 22.820000 | 0.320000 | 10000.000000 | 195.000000 | 5.43 | 2.080000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 13:00:00 | 89.000000 | 22.810000 | 25.070000 | 92.000000 | 1014.000000 | 0.63 | 24.190000 | 1.690000 | 10000.000000 | 201.000000 | 4.67 | 2.300000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 23.310000 | 26.340000 | 88.000000 | 1014.000000 | 1.35 | 25.440000 | 4.410000 | 7616.000000 | 223.000000 | 5.17 | 2.550000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 15:00:00 | 95.000000 | 23.530000 | 26.060000 | 86.000000 | 1015.000000 | 1.38 | 26.060000 | 7.890000 | 10000.000000 | 238.000000 | 5.1 | 3.080000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 16:00:00 | 90.000000 | 23.710000 | 26.440000 | 85.000000 | 1014.000000 | 1.24 | 26.440000 | 11.020000 | 8815.000000 | 248.000000 | 4.9 | 3.320000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 17:00:00 | 91.000000 | 23.850000 | 26.580000 | 85.000000 | 1013.000000 | 1.6 | 26.580000 | 12.510000 | 6163.000000 | 258.000000 | 4.44 | 3.150000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 18:00:00 | 70.000000 | 23.730000 | 26.260000 | 86.000000 | 1013.000000 | 1.64 | 26.260000 | 11.840000 | 8540.000000 | 272.000000 | 4.18 | 2.760000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 19:00:00 | 89.000000 | 23.550000 | 26.080000 | 86.000000 | 1012.000000 | 1.49 | 26.080000 | 9.160000 | 8914.000000 | 275.000000 | 4.01 | 2.590000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 20:00:00 | 83.000000 | 23.600000 | 26.850000 | 87.000000 | 1011.000000 | 1.41 | 25.930000 | 5.730000 | 7096.000000 | 275.000000 | 3.62 | 2.360000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 21:00:00 | 79.000000 | 23.420000 | 26.470000 | 88.000000 | 1010.000000 | 1.33 | 25.560000 | 2.600000 | 10000.000000 | 273.000000 | 3.27 | 1.940000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 22:00:00 | 78.000000 | 23.550000 | 26.060000 | 91.000000 | 1011.000000 | 1.31 | 25.120000 | 0.650000 | 9293.000000 | 269.000000 | 3.1 | 1.540000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53045010 | "BONANZA [53045010]" | 2.566667 | -77.883333 | 10.000000 | Climática Principal | Convencional | Suspendida | 1966-10-15 00:00:00 | 2008-03-31 00:00:00 | Cauca | Guapi | Neiva | Area Operativa 07 - Nariño-Putumayo | Pacifico | Tapaje - Dagua - Directos | Río Guapi | America/Bogota | 2022-01-10 23:00:00 | 82.000000 | 22.710000 | 24.960000 | 92.000000 | 1011.000000 | 1.52 | 24.090000 | 0.000000 | 10000.000000 | 252.000000 | 2.42 | 1.300000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station53045010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station53045010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station53045010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53045010_OWM_Windspeed_20220111.png)
