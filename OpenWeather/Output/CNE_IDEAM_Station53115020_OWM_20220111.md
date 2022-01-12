
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - COLPUERTOS [53115020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station53115020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.88333333,-77.06666667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.88333333&lon=-77.06666667)


| Parameter | Value |
|---|---|
| Code | 53115020 |
| Name | COLPUERTOS [53115020] |
| Latitude, ° | 3.88333333 |
| Longitude, ° | -77.06666667 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1969-04-15 00:00:00 |
| Suspension date | 2002-03-15 00:00:00 |
| State | Valle del Cauca |
| County | Buenaventura |
| Stream | Inirida |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Tapaje - Dagua - Directos |
| SZH - Hydrographic subzone | Dagua - Buenaventura - Bahia Málaga |

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

### (CNE index 1143) Open Weather values for station 53115020 - COLPUERTOS [53115020]

JSON data from API OWM:

```
{'lat': 3.8833, 'lon': -77.0667, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813496, 'sunset': 1641856375, 'temp': 26.15, 'feels_like': 26.15, 'pressure': 1010, 'humidity': 86, 'dew_point': 23.62, 'uvi': 5.1, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.16, 'wind_deg': 226, 'wind_gust': 5.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, 'hourly': [{'dt': 1641772800, 'temp': 24.1, 'feels_like': 24.97, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.72, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 187, 'wind_gust': 1.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 23.79, 'feels_like': 24.65, 'pressure': 1012, 'humidity': 93, 'dew_point': 22.59, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 184, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641780000, 'temp': 23.59, 'feels_like': 24.46, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.57, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 173, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641783600, 'temp': 23.42, 'feels_like': 24.27, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.4, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 167, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 23.27, 'feels_like': 24.11, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.25, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 172, 'wind_gust': 1.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 23.1, 'feels_like': 23.92, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.08, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 161, 'wind_gust': 1.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.06, 'feels_like': 23.88, 'pressure': 1012, 'humidity': 94, 'dew_point': 22.04, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 174, 'wind_gust': 2.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.87, 'feels_like': 23.69, 'pressure': 1011, 'humidity': 95, 'dew_point': 22.03, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 173, 'wind_gust': 2.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641801600, 'temp': 22.7, 'feels_like': 23.51, 'pressure': 1011, 'humidity': 95, 'dew_point': 21.86, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 171, 'wind_gust': 2.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.8}}, {'dt': 1641805200, 'temp': 22.75, 'feels_like': 23.56, 'pressure': 1011, 'humidity': 95, 'dew_point': 21.91, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 166, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.94}}, {'dt': 1641808800, 'temp': 22.9, 'feels_like': 23.7, 'pressure': 1012, 'humidity': 94, 'dew_point': 21.88, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 167, 'wind_gust': 2.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641812400, 'temp': 22.97, 'feels_like': 23.78, 'pressure': 1012, 'humidity': 94, 'dew_point': 21.95, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 178, 'wind_gust': 2.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.89}}, {'dt': 1641816000, 'temp': 23.23, 'feels_like': 24.06, 'pressure': 1013, 'humidity': 94, 'dew_point': 22.21, 'uvi': 0.31, 'clouds': 88, 'visibility': 9288, 'wind_speed': 1.37, 'wind_deg': 172, 'wind_gust': 2.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641819600, 'temp': 23.87, 'feels_like': 24.74, 'pressure': 1014, 'humidity': 93, 'dew_point': 22.67, 'uvi': 1.53, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 184, 'wind_gust': 2.24, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641823200, 'temp': 24.41, 'feels_like': 25.31, 'pressure': 1014, 'humidity': 92, 'dew_point': 23.02, 'uvi': 3.98, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 209, 'wind_gust': 2.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641826800, 'temp': 25.19, 'feels_like': 26.11, 'pressure': 1015, 'humidity': 90, 'dew_point': 23.43, 'uvi': 7.08, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 227, 'wind_gust': 4.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641830400, 'temp': 25.88, 'feels_like': 26.82, 'pressure': 1014, 'humidity': 88, 'dew_point': 23.74, 'uvi': 10.69, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3, 'wind_deg': 223, 'wind_gust': 5.5, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.11}}, {'dt': 1641834000, 'temp': 26.38, 'feels_like': 26.38, 'pressure': 1013, 'humidity': 85, 'dew_point': 23.65, 'uvi': 12.08, 'clouds': 89, 'visibility': 9320, 'wind_speed': 3.49, 'wind_deg': 226, 'wind_gust': 5.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641837600, 'temp': 26.39, 'feels_like': 26.39, 'pressure': 1012, 'humidity': 86, 'dew_point': 23.86, 'uvi': 11.37, 'clouds': 92, 'visibility': 10000, 'wind_speed': 3.41, 'wind_deg': 223, 'wind_gust': 5.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641841200, 'temp': 26.21, 'feels_like': 26.21, 'pressure': 1011, 'humidity': 87, 'dew_point': 23.87, 'uvi': 8.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.25, 'wind_deg': 223, 'wind_gust': 5.13, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641844800, 'temp': 26.15, 'feels_like': 26.15, 'pressure': 1010, 'humidity': 86, 'dew_point': 23.62, 'uvi': 5.1, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.16, 'wind_deg': 226, 'wind_gust': 5.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, {'dt': 1641848400, 'temp': 25.92, 'feels_like': 26.81, 'pressure': 1010, 'humidity': 86, 'dew_point': 23.4, 'uvi': 2.28, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.59, 'wind_deg': 220, 'wind_gust': 4.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641852000, 'temp': 25.24, 'feels_like': 26.14, 'pressure': 1011, 'humidity': 89, 'dew_point': 23.3, 'uvi': 0.56, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 218, 'wind_gust': 4.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641855600, 'temp': 24.09, 'feels_like': 24.96, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.71, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 199, 'wind_gust': 3.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 00:00:00 | 89.000000 | 22.720000 | 24.970000 | 92.000000 | 1011.000000 |  | 24.100000 | 0.000000 | 10000.000000 | 187.000000 | 1.68 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 22.590000 | 24.650000 | 93.000000 | 1012.000000 | 0.16 | 23.790000 | 0.000000 | 10000.000000 | 184.000000 | 1.48 | 1.230000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 02:00:00 | 81.000000 | 22.570000 | 24.460000 | 94.000000 | 1013.000000 | 0.24 | 23.590000 | 0.000000 | 10000.000000 | 173.000000 | 1.61 | 1.300000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 03:00:00 | 76.000000 | 22.400000 | 24.270000 | 94.000000 | 1013.000000 | 0.12 | 23.420000 | 0.000000 | 10000.000000 | 167.000000 | 1.61 | 1.360000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 04:00:00 | 66.000000 | 22.250000 | 24.110000 | 94.000000 | 1013.000000 | 0.13 | 23.270000 | 0.000000 | 10000.000000 | 172.000000 | 1.68 | 1.400000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 05:00:00 | 73.000000 | 22.080000 | 23.920000 | 94.000000 | 1013.000000 |  | 23.100000 | 0.000000 | 10000.000000 | 161.000000 | 1.88 | 1.550000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 06:00:00 | 70.000000 | 22.040000 | 23.880000 | 94.000000 | 1012.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 174.000000 | 2.16 | 1.690000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 07:00:00 | 70.000000 | 22.030000 | 23.690000 | 95.000000 | 1011.000000 | 0.42 | 22.870000 | 0.000000 | 10000.000000 | 173.000000 | 2.5 | 1.850000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 08:00:00 | 77.000000 | 21.860000 | 23.510000 | 95.000000 | 1011.000000 | 0.8 | 22.700000 | 0.000000 | 10000.000000 | 171.000000 | 2.44 | 1.770000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 09:00:00 | 80.000000 | 21.910000 | 23.560000 | 95.000000 | 1011.000000 | 0.94 | 22.750000 | 0.000000 | 10000.000000 | 166.000000 | 2.26 | 1.530000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 10:00:00 | 85.000000 | 21.880000 | 23.700000 | 94.000000 | 1012.000000 | 0.53 | 22.900000 | 0.000000 | 10000.000000 | 167.000000 | 2.11 | 1.480000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 11:00:00 | 88.000000 | 21.950000 | 23.780000 | 94.000000 | 1012.000000 | 0.89 | 22.970000 | 0.000000 | 10000.000000 | 178.000000 | 2.11 | 1.430000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 12:00:00 | 88.000000 | 22.210000 | 24.060000 | 94.000000 | 1013.000000 | 0.91 | 23.230000 | 0.310000 | 9288.000000 | 172.000000 | 2.29 | 1.370000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 13:00:00 | 94.000000 | 22.670000 | 24.740000 | 93.000000 | 1014.000000 | 1.08 | 23.870000 | 1.530000 | 10000.000000 | 184.000000 | 2.24 | 1.360000 | 501 | Rain | moderate rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 23.020000 | 25.310000 | 92.000000 | 1014.000000 | 0.73 | 24.410000 | 3.980000 | 10000.000000 | 209.000000 | 2.15 | 1.110000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 15:00:00 | 97.000000 | 23.430000 | 26.110000 | 90.000000 | 1015.000000 | 0.96 | 25.190000 | 7.080000 | 10000.000000 | 227.000000 | 4.26 | 2.110000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 23.740000 | 26.820000 | 88.000000 | 1014.000000 | 1.11 | 25.880000 | 10.690000 | 10000.000000 | 223.000000 | 5.5 | 3.000000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 17:00:00 | 89.000000 | 23.650000 | 26.380000 | 85.000000 | 1013.000000 | 0.91 | 26.380000 | 12.080000 | 9320.000000 | 226.000000 | 5.44 | 3.490000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 18:00:00 | 92.000000 | 23.860000 | 26.390000 | 86.000000 | 1012.000000 | 1.25 | 26.390000 | 11.370000 | 10000.000000 | 223.000000 | 5.19 | 3.410000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 23.870000 | 26.210000 | 87.000000 | 1011.000000 | 1.15 | 26.210000 | 8.270000 | 10000.000000 | 223.000000 | 5.13 | 3.250000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 23.620000 | 26.150000 | 86.000000 | 1010.000000 | 0.89 | 26.150000 | 5.100000 | 10000.000000 | 226.000000 | 5.16 | 3.160000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 21:00:00 | 97.000000 | 23.400000 | 26.810000 | 86.000000 | 1010.000000 | 0.81 | 25.920000 | 2.280000 | 10000.000000 | 220.000000 | 4.41 | 2.590000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 22:00:00 | 94.000000 | 23.300000 | 26.140000 | 89.000000 | 1011.000000 | 0.81 | 25.240000 | 0.560000 | 10000.000000 | 218.000000 | 4.47 | 2.250000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 53115020 | "COLPUERTOS [53115020]" | 3.883333 | -77.066667 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-04-15 00:00:00 | 2002-03-15 00:00:00 | Valle del Cauca | Buenaventura | Inirida | Area Operativa 09 - Cauca-Valle-Caldas | Pacifico | Tapaje - Dagua - Directos | Dagua - Buenaventura - Bahia Málaga | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 22.710000 | 24.960000 | 92.000000 | 1011.000000 | 0.95 | 24.090000 | 0.000000 | 10000.000000 | 199.000000 | 3.9 | 1.670000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station53115020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station53115020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station53115020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station53115020_OWM_Windspeed_20220111.png)
