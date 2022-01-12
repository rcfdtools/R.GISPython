
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MONTERREY FORESTAL [25025020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station25025020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.73166667,-74.83805556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.73166667&lon=-74.83805556)


| Parameter | Value |
|---|---|
| Code | 25025020 |
| Name | MONTERREY FORESTAL [25025020] |
| Latitude, ° | 9.73166667 |
| Longitude, ° | -74.83805556 |
| Elevation, m | 25 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1987-01-15 00:00:00 |
| Suspension date | NaT |
| State | Bolívar |
| County | Zambrano |
| Stream | Maracas |
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

### (CNE index 2796) Open Weather values for station 25025020 - MONTERREY FORESTAL [25025020]

JSON data from API OWM:

```
{'lat': 9.7317, 'lon': -74.8381, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813533, 'sunset': 1641855269, 'temp': 33.16, 'feels_like': 32.51, 'pressure': 1008, 'humidity': 32, 'dew_point': 14.26, 'uvi': 3.46, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 196, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.51, 'feels_like': 26.51, 'pressure': 1010, 'humidity': 65, 'dew_point': 19.4, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.23, 'wind_deg': 315, 'wind_gust': 6.82, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 25.44, 'feels_like': 25.95, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.25, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.88, 'wind_deg': 313, 'wind_gust': 7.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.89, 'feels_like': 25.37, 'pressure': 1011, 'humidity': 74, 'dew_point': 19.94, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 311, 'wind_gust': 5.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 24.38, 'feels_like': 24.81, 'pressure': 1011, 'humidity': 74, 'dew_point': 19.45, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 321, 'wind_gust': 3.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.03, 'feels_like': 24.42, 'pressure': 1011, 'humidity': 74, 'dew_point': 19.11, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 333, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.65, 'feels_like': 24.03, 'pressure': 1011, 'humidity': 75, 'dew_point': 18.96, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 334, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.21, 'feels_like': 23.57, 'pressure': 1011, 'humidity': 76, 'dew_point': 18.75, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 37, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.85, 'feels_like': 23.2, 'pressure': 1010, 'humidity': 77, 'dew_point': 18.61, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 85, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.48, 'feels_like': 22.79, 'pressure': 1010, 'humidity': 77, 'dew_point': 18.25, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 71, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.96, 'feels_like': 22.17, 'pressure': 1010, 'humidity': 75, 'dew_point': 17.33, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 87, 'wind_gust': 1.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 21.38, 'feels_like': 21.48, 'pressure': 1011, 'humidity': 73, 'dew_point': 16.34, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 109, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.87, 'feels_like': 20.87, 'pressure': 1012, 'humidity': 71, 'dew_point': 15.42, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 110, 'wind_gust': 1.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.63, 'feels_like': 21.65, 'pressure': 1013, 'humidity': 69, 'dew_point': 15.7, 'uvi': 0.29, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 127, 'wind_gust': 4.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 24.68, 'feels_like': 24.69, 'pressure': 1014, 'humidity': 57, 'dew_point': 15.6, 'uvi': 1.58, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.09, 'wind_deg': 128, 'wind_gust': 4.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.6, 'feels_like': 27.86, 'pressure': 1014, 'humidity': 48, 'dew_point': 15.61, 'uvi': 3.98, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 130, 'wind_gust': 4.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.83, 'feels_like': 29.72, 'pressure': 1014, 'humidity': 42, 'dew_point': 15.54, 'uvi': 6.95, 'clouds': 44, 'visibility': 10000, 'wind_speed': 2.9, 'wind_deg': 130, 'wind_gust': 3.82, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 31.49, 'feels_like': 31.11, 'pressure': 1013, 'humidity': 37, 'dew_point': 15.05, 'uvi': 8.91, 'clouds': 56, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 134, 'wind_gust': 3.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 32.85, 'feels_like': 32.26, 'pressure': 1012, 'humidity': 33, 'dew_point': 14.46, 'uvi': 9.79, 'clouds': 59, 'visibility': 10000, 'wind_speed': 2.73, 'wind_deg': 145, 'wind_gust': 3.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 33.48, 'feels_like': 32.76, 'pressure': 1010, 'humidity': 31, 'dew_point': 14.04, 'uvi': 8.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 152, 'wind_gust': 2.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 33.62, 'feels_like': 32.95, 'pressure': 1009, 'humidity': 31, 'dew_point': 14.16, 'uvi': 6.04, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 170, 'wind_gust': 2.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 33.16, 'feels_like': 32.51, 'pressure': 1008, 'humidity': 32, 'dew_point': 14.26, 'uvi': 3.46, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 196, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 32.32, 'feels_like': 31.73, 'pressure': 1008, 'humidity': 34, 'dew_point': 14.46, 'uvi': 1.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 210, 'wind_gust': 2.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.34, 'feels_like': 30.35, 'pressure': 1008, 'humidity': 42, 'dew_point': 16, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 226, 'wind_gust': 4.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.08, 'feels_like': 27.75, 'pressure': 1009, 'humidity': 54, 'dew_point': 16.98, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 268, 'wind_gust': 3.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 00:00:00 | 50.000000 | 19.400000 | 26.510000 | 65.000000 | 1010.000000 |  | 26.510000 | 0.000000 | 10000.000000 | 315.000000 | 6.82 | 3.230000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 01:00:00 | 58.000000 | 20.250000 | 25.950000 | 73.000000 | 1011.000000 |  | 25.440000 | 0.000000 | 10000.000000 | 313.000000 | 7.29 | 2.880000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 19.940000 | 25.370000 | 74.000000 | 1011.000000 |  | 24.890000 | 0.000000 | 10000.000000 | 311.000000 | 5.67 | 2.250000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 03:00:00 | 81.000000 | 19.450000 | 24.810000 | 74.000000 | 1011.000000 |  | 24.380000 | 0.000000 | 10000.000000 | 321.000000 | 3.25 | 1.810000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 04:00:00 | 81.000000 | 19.110000 | 24.420000 | 74.000000 | 1011.000000 |  | 24.030000 | 0.000000 | 10000.000000 | 333.000000 | 1.63 | 1.450000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 05:00:00 | 80.000000 | 18.960000 | 24.030000 | 75.000000 | 1011.000000 |  | 23.650000 | 0.000000 | 10000.000000 | 334.000000 | 1.11 | 0.820000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 18.750000 | 23.570000 | 76.000000 | 1011.000000 |  | 23.210000 | 0.000000 | 10000.000000 | 37.000000 | 1.01 | 0.540000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 07:00:00 | 83.000000 | 18.610000 | 23.200000 | 77.000000 | 1010.000000 |  | 22.850000 | 0.000000 | 10000.000000 | 85.000000 | 0.85 | 0.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 08:00:00 | 62.000000 | 18.250000 | 22.790000 | 77.000000 | 1010.000000 |  | 22.480000 | 0.000000 | 10000.000000 | 71.000000 | 1.05 | 0.870000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 09:00:00 | 50.000000 | 17.330000 | 22.170000 | 75.000000 | 1010.000000 |  | 21.960000 | 0.000000 | 10000.000000 | 87.000000 | 1.12 | 0.840000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 10:00:00 | 58.000000 | 16.340000 | 21.480000 | 73.000000 | 1011.000000 |  | 21.380000 | 0.000000 | 10000.000000 | 109.000000 | 1.3 | 0.770000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 11:00:00 | 55.000000 | 15.420000 | 20.870000 | 71.000000 | 1012.000000 |  | 20.870000 | 0.000000 | 10000.000000 | 110.000000 | 1.77 | 1.190000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 12:00:00 | 47.000000 | 15.700000 | 21.650000 | 69.000000 | 1013.000000 |  | 21.630000 | 0.290000 | 10000.000000 | 127.000000 | 4.81 | 1.360000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 13:00:00 | 52.000000 | 15.600000 | 24.690000 | 57.000000 | 1014.000000 |  | 24.680000 | 1.580000 | 10000.000000 | 128.000000 | 4.02 | 2.090000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 14:00:00 | 58.000000 | 15.610000 | 27.860000 | 48.000000 | 1014.000000 |  | 27.600000 | 3.980000 | 10000.000000 | 130.000000 | 4.14 | 2.450000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 15:00:00 | 44.000000 | 15.540000 | 29.720000 | 42.000000 | 1014.000000 |  | 29.830000 | 6.950000 | 10000.000000 | 130.000000 | 3.82 | 2.900000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 16:00:00 | 56.000000 | 15.050000 | 31.110000 | 37.000000 | 1013.000000 |  | 31.490000 | 8.910000 | 10000.000000 | 134.000000 | 3.62 | 3.010000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 17:00:00 | 59.000000 | 14.460000 | 32.260000 | 33.000000 | 1012.000000 |  | 32.850000 | 9.790000 | 10000.000000 | 145.000000 | 3.25 | 2.730000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 14.040000 | 32.760000 | 31.000000 | 1010.000000 |  | 33.480000 | 8.910000 | 10000.000000 | 152.000000 | 2.86 | 2.460000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 14.160000 | 32.950000 | 31.000000 | 1009.000000 |  | 33.620000 | 6.040000 | 10000.000000 | 170.000000 | 2.59 | 2.490000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 14.260000 | 32.510000 | 32.000000 | 1008.000000 |  | 33.160000 | 3.460000 | 10000.000000 | 196.000000 | 2.05 | 2.670000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 14.460000 | 31.730000 | 34.000000 | 1008.000000 |  | 32.320000 | 1.370000 | 10000.000000 | 210.000000 | 2.32 | 2.840000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 16.000000 | 30.350000 | 42.000000 | 1008.000000 |  | 30.340000 | 0.260000 | 10000.000000 | 226.000000 | 4.97 | 2.600000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 25025020 | "MONTERREY FORESTAL [25025020]" | 9.731667 | -74.838056 | 25.000000 | Climática Principal | Convencional | Activa | 1987-01-15 00:00:00 | NaT | Bolívar | Zambrano | Maracas | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena Cauca | Bajo Magdalena- Cauca -San Jorge | Bajo San Jorge - La Mojana | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 16.980000 | 27.750000 | 54.000000 | 1009.000000 |  | 27.080000 | 0.000000 | 10000.000000 | 268.000000 | 3.63 | 2.350000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station25025020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station25025020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station25025020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station25025020_OWM_Windspeed_20220111.png)
