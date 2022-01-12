
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ALTAQUER - AUT [51025080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station51025080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.24833333,-78.0925) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.24833333&lon=-78.0925)


| Parameter | Value |
|---|---|
| Code | 51025080 |
| Name | ALTAQUER - AUT [51025080] |
| Latitude, ° | 1.24833333 |
| Longitude, ° | -78.0925 |
| Elevation, m | 110 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-02-26 19:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Barbacoas |
| Stream | 0 |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Mira |
| SZH - Hydrographic subzone | Río Mira |

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

### (CNE index 279) Open Weather values for station 51025080 - ALTAQUER - AUT [51025080]

JSON data from API OWM:

```
{'lat': 1.2483, 'lon': -78.0925, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813488, 'sunset': 1641856876, 'temp': 26.34, 'feels_like': 26.34, 'pressure': 1013, 'humidity': 94, 'dew_point': 25.3, 'uvi': 4.68, 'clouds': 96, 'visibility': 2195, 'wind_speed': 1.58, 'wind_deg': 296, 'wind_gust': 1.89, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.08}}, 'hourly': [{'dt': 1641772800, 'temp': 24.34, 'feels_like': 25.39, 'pressure': 1014, 'humidity': 98, 'dew_point': 24, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 248, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641776400, 'temp': 18.78, 'feels_like': 19.25, 'pressure': 1015, 'humidity': 97, 'dew_point': 18.29, 'uvi': 0, 'clouds': 100, 'visibility': 6062, 'wind_speed': 0.33, 'wind_deg': 213, 'wind_gust': 0.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 18.68, 'feels_like': 19.14, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.19, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 211, 'wind_gust': 0.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 18.66, 'feels_like': 19.11, 'pressure': 1016, 'humidity': 97, 'dew_point': 18.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 107, 'wind_gust': 0.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.28, 'feels_like': 18.72, 'pressure': 1016, 'humidity': 98, 'dew_point': 17.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 289, 'wind_gust': 0.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 18.1, 'feels_like': 18.52, 'pressure': 1016, 'humidity': 98, 'dew_point': 17.78, 'uvi': 0, 'clouds': 100, 'visibility': 6129, 'wind_speed': 0.35, 'wind_deg': 192, 'wind_gust': 0.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.29, 'feels_like': 18.76, 'pressure': 1015, 'humidity': 99, 'dew_point': 18.13, 'uvi': 0, 'clouds': 100, 'visibility': 7855, 'wind_speed': 0.72, 'wind_deg': 242, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 18.16, 'feels_like': 18.62, 'pressure': 1014, 'humidity': 99, 'dew_point': 18, 'uvi': 0, 'clouds': 100, 'visibility': 7167, 'wind_speed': 0.5, 'wind_deg': 224, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641801600, 'temp': 18.19, 'feels_like': 18.62, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.87, 'uvi': 0, 'clouds': 100, 'visibility': 4106, 'wind_speed': 0.25, 'wind_deg': 139, 'wind_gust': 0.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641805200, 'temp': 18.1, 'feels_like': 18.52, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.78, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 205, 'wind_gust': 0.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.69}}, {'dt': 1641808800, 'temp': 18.17, 'feels_like': 18.6, 'pressure': 1014, 'humidity': 98, 'dew_point': 17.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 133, 'wind_gust': 0.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641812400, 'temp': 18.34, 'feels_like': 18.76, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.86, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 63, 'wind_gust': 0.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641816000, 'temp': 19.34, 'feels_like': 19.84, 'pressure': 1016, 'humidity': 96, 'dew_point': 18.69, 'uvi': 0.32, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 296, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641819600, 'temp': 21.34, 'feels_like': 21.96, 'pressure': 1016, 'humidity': 93, 'dew_point': 20.16, 'uvi': 1.7, 'clouds': 98, 'visibility': 7919, 'wind_speed': 0.71, 'wind_deg': 296, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641823200, 'temp': 24.34, 'feels_like': 25.15, 'pressure': 1017, 'humidity': 89, 'dew_point': 22.41, 'uvi': 4.46, 'clouds': 99, 'visibility': 3906, 'wind_speed': 1.11, 'wind_deg': 300, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641826800, 'temp': 26.34, 'feels_like': 26.34, 'pressure': 1017, 'humidity': 87, 'dew_point': 24, 'uvi': 7.99, 'clouds': 95, 'visibility': 5717, 'wind_speed': 1.72, 'wind_deg': 310, 'wind_gust': 1.67, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, {'dt': 1641830400, 'temp': 28.34, 'feels_like': 34.25, 'pressure': 1016, 'humidity': 87, 'dew_point': 25.97, 'uvi': 10.67, 'clouds': 96, 'visibility': 5145, 'wind_speed': 1.77, 'wind_deg': 315, 'wind_gust': 1.84, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.91}}, {'dt': 1641834000, 'temp': 27.34, 'feels_like': 31.1, 'pressure': 1015, 'humidity': 85, 'dew_point': 24.59, 'uvi': 12.18, 'clouds': 94, 'visibility': 5593, 'wind_speed': 1.72, 'wind_deg': 309, 'wind_gust': 1.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.96}}, {'dt': 1641837600, 'temp': 28.34, 'feels_like': 34.45, 'pressure': 1015, 'humidity': 88, 'dew_point': 26.16, 'uvi': 11.62, 'clouds': 85, 'visibility': 4020, 'wind_speed': 1.83, 'wind_deg': 307, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.2}}, {'dt': 1641841200, 'temp': 29.34, 'feels_like': 36.34, 'pressure': 1014, 'humidity': 91, 'dew_point': 27.72, 'uvi': 7.38, 'clouds': 93, 'visibility': 2364, 'wind_speed': 1.64, 'wind_deg': 295, 'wind_gust': 1.83, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.17}}, {'dt': 1641844800, 'temp': 26.34, 'feels_like': 26.34, 'pressure': 1013, 'humidity': 94, 'dew_point': 25.3, 'uvi': 4.68, 'clouds': 96, 'visibility': 2195, 'wind_speed': 1.58, 'wind_deg': 296, 'wind_gust': 1.89, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.08}}, {'dt': 1641848400, 'temp': 24.34, 'feels_like': 25.36, 'pressure': 1013, 'humidity': 97, 'dew_point': 23.83, 'uvi': 2.17, 'clouds': 97, 'visibility': 2899, 'wind_speed': 1.23, 'wind_deg': 293, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.66}}, {'dt': 1641852000, 'temp': 23.34, 'feels_like': 24.29, 'pressure': 1013, 'humidity': 98, 'dew_point': 23.01, 'uvi': 0.73, 'clouds': 98, 'visibility': 488, 'wind_speed': 0.97, 'wind_deg': 286, 'wind_gust': 1.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.26}}, {'dt': 1641855600, 'temp': 23.34, 'feels_like': 24.31, 'pressure': 1014, 'humidity': 99, 'dew_point': 23.17, 'uvi': 0, 'clouds': 98, 'visibility': 226, 'wind_speed': 0.62, 'wind_deg': 291, 'wind_gust': 1.17, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.56}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 24.000000 | 25.390000 | 98.000000 | 1014.000000 | 0.25 | 24.340000 | 0.000000 | 10000.000000 | 248.000000 | 0.63 | 0.520000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 18.290000 | 19.250000 | 97.000000 | 1015.000000 |  | 18.780000 | 0.000000 | 6062.000000 | 213.000000 | 0.39 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 18.190000 | 19.140000 | 97.000000 | 1016.000000 |  | 18.680000 | 0.000000 | 10000.000000 | 211.000000 | 0.29 | 0.190000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 18.170000 | 19.110000 | 97.000000 | 1016.000000 |  | 18.660000 | 0.000000 | 10000.000000 | 107.000000 | 0.5 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 17.960000 | 18.720000 | 98.000000 | 1016.000000 |  | 18.280000 | 0.000000 | 10000.000000 | 289.000000 | 0.34 | 0.100000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 17.780000 | 18.520000 | 98.000000 | 1016.000000 |  | 18.100000 | 0.000000 | 6129.000000 | 192.000000 | 0.44 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 18.130000 | 18.760000 | 99.000000 | 1015.000000 |  | 18.290000 | 0.000000 | 7855.000000 | 242.000000 | 0.87 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 18.000000 | 18.620000 | 99.000000 | 1014.000000 | 0.3 | 18.160000 | 0.000000 | 7167.000000 | 224.000000 | 0.64 | 0.500000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 17.870000 | 18.620000 | 98.000000 | 1014.000000 | 0.53 | 18.190000 | 0.000000 | 4106.000000 | 139.000000 | 0.42 | 0.250000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 17.780000 | 18.520000 | 98.000000 | 1014.000000 | 0.69 | 18.100000 | 0.000000 | 10000.000000 | 205.000000 | 0.28 | 0.220000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 17.850000 | 18.600000 | 98.000000 | 1014.000000 | 0.34 | 18.170000 | 0.000000 | 10000.000000 | 133.000000 | 0.26 | 0.190000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 17.860000 | 18.760000 | 97.000000 | 1015.000000 | 0.37 | 18.340000 | 0.000000 | 10000.000000 | 63.000000 | 0.29 | 0.260000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 12:00:00 | 92.000000 | 18.690000 | 19.840000 | 96.000000 | 1016.000000 | 0.44 | 19.340000 | 0.320000 | 10000.000000 | 296.000000 | 0.53 | 0.170000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 20.160000 | 21.960000 | 93.000000 | 1016.000000 | 0.4 | 21.340000 | 1.700000 | 7919.000000 | 296.000000 | 0.68 | 0.710000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 22.410000 | 25.150000 | 89.000000 | 1017.000000 | 0.62 | 24.340000 | 4.460000 | 3906.000000 | 300.000000 | 1.01 | 1.110000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 15:00:00 | 95.000000 | 24.000000 | 26.340000 | 87.000000 | 1017.000000 | 1.44 | 26.340000 | 7.990000 | 5717.000000 | 310.000000 | 1.67 | 1.720000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 16:00:00 | 96.000000 | 25.970000 | 34.250000 | 87.000000 | 1016.000000 | 1.91 | 28.340000 | 10.670000 | 5145.000000 | 315.000000 | 1.84 | 1.770000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 17:00:00 | 94.000000 | 24.590000 | 31.100000 | 85.000000 | 1015.000000 | 1.96 | 27.340000 | 12.180000 | 5593.000000 | 309.000000 | 1.57 | 1.720000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 18:00:00 | 85.000000 | 26.160000 | 34.450000 | 88.000000 | 1015.000000 | 2.2 | 28.340000 | 11.620000 | 4020.000000 | 307.000000 | 1.75 | 1.830000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 19:00:00 | 93.000000 | 27.720000 | 36.340000 | 91.000000 | 1014.000000 | 2.17 | 29.340000 | 7.380000 | 2364.000000 | 295.000000 | 1.83 | 1.640000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 20:00:00 | 96.000000 | 25.300000 | 26.340000 | 94.000000 | 1013.000000 | 2.08 | 26.340000 | 4.680000 | 2195.000000 | 296.000000 | 1.89 | 1.580000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 21:00:00 | 97.000000 | 23.830000 | 25.360000 | 97.000000 | 1013.000000 | 1.66 | 24.340000 | 2.170000 | 2899.000000 | 293.000000 | 1.66 | 1.230000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 23.010000 | 24.290000 | 98.000000 | 1013.000000 | 1.26 | 23.340000 | 0.730000 | 488.000000 | 286.000000 | 1.48 | 0.970000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025080 | "ALTAQUER - AUT [51025080]" | 1.248333 | -78.092500 | 110.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-02-26 19:00:00 | NaT | Nariño | Barbacoas | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 23.170000 | 24.310000 | 99.000000 | 1014.000000 | 1.56 | 23.340000 | 0.000000 | 226.000000 | 291.000000 | 1.17 | 0.620000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station51025080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station51025080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station51025080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025080_OWM_Windspeed_20220111.png)
