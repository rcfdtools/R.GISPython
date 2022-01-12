
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO BARACOA [25025100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.28194444,-74.84527778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.28194444&lon=-74.84527778)


| Parameter | Value |
|---|---|
| Code | 25025100 |
| Name | AEROPUERTO BARACOA [25025100] |
| Latitude, ° | 9.28194444 |
| Longitude, ° | -74.84527778 |
| Elevation, m | 18 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1954-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | Magangué |
| Stream | Lago La Pastora |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Bajo Magdalena- Cauca -San Jorge |
| SZH - Hydrographic subzone | Bajo San Jorge - La Mojana |

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

### (CNE index 2593) Open Weather values for station 25025100 - AEROPUERTO BARACOA [25025100]

JSON data from API OWM:

```
{'lat': 9.2819, 'lon': -74.8453, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813490, 'sunset': 1641855315, 'temp': 31.87, 'feels_like': 31.45, 'pressure': 1008, 'humidity': 36, 'dew_point': 14.95, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 282, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.01, 'feels_like': 27.95, 'pressure': 1009, 'humidity': 58, 'dew_point': 18.05, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.92, 'wind_deg': 252, 'wind_gust': 2.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.57, 'feels_like': 25.93, 'pressure': 1010, 'humidity': 67, 'dew_point': 18.99, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 3.23, 'wind_deg': 306, 'wind_gust': 5.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 24.27, 'feels_like': 24.76, 'pressure': 1011, 'humidity': 77, 'dew_point': 19.98, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 3.07, 'wind_deg': 330, 'wind_gust': 6.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 23.78, 'feels_like': 24.3, 'pressure': 1011, 'humidity': 80, 'dew_point': 20.12, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 316, 'wind_gust': 2.35, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 23.55, 'feels_like': 24.05, 'pressure': 1011, 'humidity': 80, 'dew_point': 19.9, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 289, 'wind_gust': 1.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 23.38, 'feels_like': 23.86, 'pressure': 1011, 'humidity': 80, 'dew_point': 19.73, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 248, 'wind_gust': 1.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 23.07, 'feels_like': 23.55, 'pressure': 1011, 'humidity': 81, 'dew_point': 19.63, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 231, 'wind_gust': 0.83, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 22.74, 'feels_like': 23.21, 'pressure': 1010, 'humidity': 82, 'dew_point': 19.51, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 330, 'wind_gust': 0.65, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 22.4, 'feels_like': 22.84, 'pressure': 1010, 'humidity': 82, 'dew_point': 19.18, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 47, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.85, 'feels_like': 22.26, 'pressure': 1010, 'humidity': 83, 'dew_point': 18.83, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 73, 'wind_gust': 1.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.47, 'feels_like': 21.87, 'pressure': 1011, 'humidity': 84, 'dew_point': 18.65, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 72, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.16, 'feels_like': 21.52, 'pressure': 1011, 'humidity': 84, 'dew_point': 18.35, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 60, 'wind_gust': 1.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.86, 'feels_like': 22.22, 'pressure': 1013, 'humidity': 81, 'dew_point': 18.45, 'uvi': 0.33, 'clouds': 13, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 85, 'wind_gust': 1.91, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 24.04, 'feels_like': 24.33, 'pressure': 1014, 'humidity': 70, 'dew_point': 18.23, 'uvi': 1.64, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 95, 'wind_gust': 2.1, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1014, 'humidity': 60, 'dew_point': 17.9, 'uvi': 4.11, 'clouds': 18, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 97, 'wind_gust': 2.56, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 28.22, 'feels_like': 28.9, 'pressure': 1014, 'humidity': 52, 'dew_point': 17.44, 'uvi': 7.16, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 94, 'wind_gust': 2.62, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 29.87, 'feels_like': 30.15, 'pressure': 1013, 'humidity': 45, 'dew_point': 16.66, 'uvi': 9.17, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 89, 'wind_gust': 2.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 31.12, 'feels_like': 31.07, 'pressure': 1012, 'humidity': 40, 'dew_point': 15.93, 'uvi': 10.08, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 94, 'wind_gust': 2.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 31.84, 'feels_like': 31.41, 'pressure': 1010, 'humidity': 36, 'dew_point': 14.93, 'uvi': 9.17, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 96, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 32.12, 'feels_like': 31.62, 'pressure': 1009, 'humidity': 35, 'dew_point': 14.74, 'uvi': 5.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 290, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.87, 'feels_like': 31.45, 'pressure': 1008, 'humidity': 36, 'dew_point': 14.95, 'uvi': 3.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 282, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 31.28, 'feels_like': 31.13, 'pressure': 1008, 'humidity': 39, 'dew_point': 15.68, 'uvi': 1.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 290, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.6, 'feels_like': 30.19, 'pressure': 1009, 'humidity': 48, 'dew_point': 17.43, 'uvi': 0.3, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 269, 'wind_gust': 2.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.31, 'feels_like': 27.65, 'pressure': 1009, 'humidity': 49, 'dew_point': 15.67, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 260, 'wind_gust': 3.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 00:00:00 | 32.000000 | 18.050000 | 27.950000 | 58.000000 | 1009.000000 |  | 27.010000 | 0.000000 | 10000.000000 | 252.000000 | 2.26 | 1.920000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 01:00:00 | 34.000000 | 18.990000 | 25.930000 | 67.000000 | 1010.000000 |  | 25.570000 | 0.000000 | 10000.000000 | 306.000000 | 5.2 | 3.230000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 02:00:00 | 44.000000 | 19.980000 | 24.760000 | 77.000000 | 1011.000000 |  | 24.270000 | 0.000000 | 10000.000000 | 330.000000 | 6.77 | 3.070000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 03:00:00 | 46.000000 | 20.120000 | 24.300000 | 80.000000 | 1011.000000 |  | 23.780000 | 0.000000 | 10000.000000 | 316.000000 | 2.35 | 1.810000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 04:00:00 | 41.000000 | 19.900000 | 24.050000 | 80.000000 | 1011.000000 |  | 23.550000 | 0.000000 | 10000.000000 | 289.000000 | 1.05 | 0.980000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 05:00:00 | 42.000000 | 19.730000 | 23.860000 | 80.000000 | 1011.000000 |  | 23.380000 | 0.000000 | 10000.000000 | 248.000000 | 1.15 | 1.100000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 06:00:00 | 34.000000 | 19.630000 | 23.550000 | 81.000000 | 1011.000000 |  | 23.070000 | 0.000000 | 10000.000000 | 231.000000 | 0.83 | 0.660000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 07:00:00 | 34.000000 | 19.510000 | 23.210000 | 82.000000 | 1010.000000 |  | 22.740000 | 0.000000 | 10000.000000 | 330.000000 | 0.65 | 0.350000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 08:00:00 | 61.000000 | 19.180000 | 22.840000 | 82.000000 | 1010.000000 |  | 22.400000 | 0.000000 | 10000.000000 | 47.000000 | 1.3 | 1.300000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 09:00:00 | 52.000000 | 18.830000 | 22.260000 | 83.000000 | 1010.000000 |  | 21.850000 | 0.000000 | 10000.000000 | 73.000000 | 1.44 | 1.320000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 10:00:00 | 59.000000 | 18.650000 | 21.870000 | 84.000000 | 1011.000000 |  | 21.470000 | 0.000000 | 10000.000000 | 72.000000 | 1.01 | 0.880000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 11:00:00 | 66.000000 | 18.350000 | 21.520000 | 84.000000 | 1011.000000 |  | 21.160000 | 0.000000 | 10000.000000 | 60.000000 | 1.35 | 1.310000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 12:00:00 | 13.000000 | 18.450000 | 22.220000 | 81.000000 | 1013.000000 |  | 21.860000 | 0.330000 | 10000.000000 | 85.000000 | 1.91 | 1.360000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 13:00:00 | 14.000000 | 18.230000 | 24.330000 | 70.000000 | 1014.000000 |  | 24.040000 | 1.640000 | 10000.000000 | 95.000000 | 2.1 | 1.660000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 14:00:00 | 18.000000 | 17.900000 | 26.280000 | 60.000000 | 1014.000000 |  | 26.280000 | 4.110000 | 10000.000000 | 97.000000 | 2.56 | 2.140000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 15:00:00 | 23.000000 | 17.440000 | 28.900000 | 52.000000 | 1014.000000 |  | 28.220000 | 7.160000 | 10000.000000 | 94.000000 | 2.62 | 2.320000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 16:00:00 | 23.000000 | 16.660000 | 30.150000 | 45.000000 | 1013.000000 |  | 29.870000 | 9.170000 | 10000.000000 | 89.000000 | 2.55 | 2.180000 | 801 | Clouds | few clouds | 02d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 17:00:00 | 36.000000 | 15.930000 | 31.070000 | 40.000000 | 1012.000000 |  | 31.120000 | 10.080000 | 10000.000000 | 94.000000 | 2.07 | 1.570000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 14.930000 | 31.410000 | 36.000000 | 1010.000000 |  | 31.840000 | 9.170000 | 10000.000000 | 96.000000 | 1.57 | 0.890000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 14.740000 | 31.620000 | 35.000000 | 1009.000000 |  | 32.120000 | 5.970000 | 10000.000000 | 290.000000 | 1.26 | 0.370000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 14.950000 | 31.450000 | 36.000000 | 1008.000000 |  | 31.870000 | 3.430000 | 10000.000000 | 282.000000 | 1.33 | 1.790000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 15.680000 | 31.130000 | 39.000000 | 1008.000000 |  | 31.280000 | 1.360000 | 10000.000000 | 290.000000 | 1.75 | 2.030000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 17.430000 | 30.190000 | 48.000000 | 1009.000000 |  | 29.600000 | 0.300000 | 10000.000000 | 269.000000 | 2.72 | 2.100000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025100 | "AEROPUERTO BARACOA [25025100]" | 9.281944 | -74.845278 | 18.000000 | Climática Principal | Convencional | Activa | 1954-01-15 00:00:00 | NaT | Bolívar | Magangué | Lago La Pastora | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 15.670000 | 27.650000 | 49.000000 | 1009.000000 |  | 27.310000 | 0.000000 | 10000.000000 | 260.000000 | 3.4 | 2.810000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025100_OWM_Windspeed_20220111.png)
