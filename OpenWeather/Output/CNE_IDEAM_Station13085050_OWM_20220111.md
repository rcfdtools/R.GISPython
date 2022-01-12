
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LORICA  ITA - AUT [13085050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station13085050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.25272222,-75.84441667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.25272222&lon=-75.84441667)


| Parameter | Value |
|---|---|
| Code | 13085050 |
| Name | LORICA  ITA - AUT [13085050] |
| Latitude, ° | 9.25272222 |
| Longitude, ° | -75.84441667 |
| Elevation, m | 30 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2005-05-13 00:00:00 |
| Suspension date | 2010-10-02 00:00:00 |
| State | Córdoba |
| County | Lorica |
| Stream | Barroblanco |
| Operator | Area Operativa 02 - Atlántico-Bolivar-Sucre |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Sinú |
| SZH - Hydrographic subzone | Bajo Sinú |

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

### (CNE index 204) Open Weather values for station 13085050 - LORICA  ITA - AUT [13085050]

JSON data from API OWM:

```
{'lat': 9.2527, 'lon': -75.8444, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813727, 'sunset': 1641855558, 'temp': 31.94, 'feels_like': 35.52, 'pressure': 1009, 'humidity': 55, 'dew_point': 21.77, 'uvi': 3.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 255, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.94, 'feels_like': 30.17, 'pressure': 1010, 'humidity': 86, 'dew_point': 24.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.37, 'wind_deg': 316, 'wind_gust': 6.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.94, 'feels_like': 26.81, 'pressure': 1011, 'humidity': 85, 'dew_point': 23.22, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.7, 'wind_deg': 322, 'wind_gust': 7.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.94, 'feels_like': 25.66, 'pressure': 1012, 'humidity': 83, 'dew_point': 21.85, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3.86, 'wind_deg': 330, 'wind_gust': 7.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.94, 'feels_like': 26.7, 'pressure': 1012, 'humidity': 81, 'dew_point': 22.43, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.65, 'wind_deg': 341, 'wind_gust': 7.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.94, 'feels_like': 26.73, 'pressure': 1011, 'humidity': 82, 'dew_point': 22.63, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 342, 'wind_gust': 5.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.94, 'feels_like': 26.76, 'pressure': 1011, 'humidity': 83, 'dew_point': 22.83, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.63, 'wind_deg': 340, 'wind_gust': 4.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.67, 'feels_like': 25.36, 'pressure': 1011, 'humidity': 83, 'dew_point': 21.59, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 326, 'wind_gust': 2.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 24.49, 'feels_like': 25.16, 'pressure': 1010, 'humidity': 83, 'dew_point': 21.41, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 317, 'wind_gust': 2.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.29, 'feels_like': 24.97, 'pressure': 1009, 'humidity': 84, 'dew_point': 21.41, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 314, 'wind_gust': 2.18, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 24.02, 'feels_like': 24.72, 'pressure': 1010, 'humidity': 86, 'dew_point': 21.53, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 316, 'wind_gust': 1.68, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 23.71, 'feels_like': 24.41, 'pressure': 1010, 'humidity': 87, 'dew_point': 21.42, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 50, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641812400, 'temp': 22.94, 'feels_like': 23.59, 'pressure': 1011, 'humidity': 88, 'dew_point': 20.85, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 120, 'wind_gust': 1.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 22.94, 'feels_like': 23.56, 'pressure': 1012, 'humidity': 87, 'dew_point': 20.66, 'uvi': 0.29, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 115, 'wind_gust': 2.54, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 24.94, 'feels_like': 25.58, 'pressure': 1013, 'humidity': 80, 'dew_point': 21.25, 'uvi': 1.43, 'clouds': 15, 'visibility': 10000, 'wind_speed': 2.95, 'wind_deg': 128, 'wind_gust': 4.05, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 27.94, 'feels_like': 30.95, 'pressure': 1014, 'humidity': 73, 'dew_point': 22.65, 'uvi': 3.69, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.4, 'wind_deg': 128, 'wind_gust': 4.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 28.94, 'feels_like': 31.89, 'pressure': 1014, 'humidity': 66, 'dew_point': 21.95, 'uvi': 6.57, 'clouds': 66, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 129, 'wind_gust': 3.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.94, 'feels_like': 32.92, 'pressure': 1013, 'humidity': 61, 'dew_point': 21.6, 'uvi': 8.01, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.83, 'wind_deg': 136, 'wind_gust': 3.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.94, 'feels_like': 34.24, 'pressure': 1012, 'humidity': 58, 'dew_point': 21.71, 'uvi': 8.92, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 134, 'wind_gust': 2.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.94, 'feels_like': 35.52, 'pressure': 1011, 'humidity': 55, 'dew_point': 21.77, 'uvi': 8.21, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 158, 'wind_gust': 1.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.94, 'feels_like': 35.25, 'pressure': 1010, 'humidity': 54, 'dew_point': 21.47, 'uvi': 6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 198, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.94, 'feels_like': 35.52, 'pressure': 1009, 'humidity': 55, 'dew_point': 21.77, 'uvi': 3.52, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 255, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.94, 'feels_like': 35.48, 'pressure': 1009, 'humidity': 63, 'dew_point': 23.07, 'uvi': 1.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 289, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.94, 'feels_like': 35.38, 'pressure': 1009, 'humidity': 72, 'dew_point': 24.34, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.86, 'wind_deg': 313, 'wind_gust': 4.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.94, 'feels_like': 31.8, 'pressure': 1010, 'humidity': 79, 'dew_point': 23.96, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.8, 'wind_deg': 322, 'wind_gust': 5.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 24.400000 | 30.170000 | 86.000000 | 1010.000000 |  | 26.940000 | 0.000000 | 10000.000000 | 316.000000 | 6.87 | 3.370000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 23.220000 | 26.810000 | 85.000000 | 1011.000000 |  | 25.940000 | 0.000000 | 10000.000000 | 322.000000 | 7.4 | 3.700000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | 21.850000 | 25.660000 | 83.000000 | 1012.000000 |  | 24.940000 | 0.000000 | 10000.000000 | 330.000000 | 7.95 | 3.860000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 22.430000 | 26.700000 | 81.000000 | 1012.000000 |  | 25.940000 | 0.000000 | 10000.000000 | 341.000000 | 7.7 | 3.650000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 22.630000 | 26.730000 | 82.000000 | 1011.000000 |  | 25.940000 | 0.000000 | 10000.000000 | 342.000000 | 5.96 | 2.960000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 22.830000 | 26.760000 | 83.000000 | 1011.000000 |  | 25.940000 | 0.000000 | 10000.000000 | 340.000000 | 4.44 | 2.630000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 06:00:00 | 43.000000 | 21.590000 | 25.360000 | 83.000000 | 1011.000000 |  | 24.670000 | 0.000000 | 10000.000000 | 326.000000 | 2.92 | 2.150000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 07:00:00 | 60.000000 | 21.410000 | 25.160000 | 83.000000 | 1010.000000 |  | 24.490000 | 0.000000 | 10000.000000 | 317.000000 | 2.62 | 1.840000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 08:00:00 | 43.000000 | 21.410000 | 24.970000 | 84.000000 | 1009.000000 |  | 24.290000 | 0.000000 | 10000.000000 | 314.000000 | 2.18 | 1.560000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 09:00:00 | 41.000000 | 21.530000 | 24.720000 | 86.000000 | 1010.000000 |  | 24.020000 | 0.000000 | 10000.000000 | 316.000000 | 1.68 | 1.110000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 10:00:00 | 44.000000 | 21.420000 | 24.410000 | 87.000000 | 1010.000000 | 0.13 | 23.710000 | 0.000000 | 10000.000000 | 50.000000 | 0.92 | 0.240000 | 500 | Rain | light rain | 10n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 11:00:00 | 40.000000 | 20.850000 | 23.590000 | 88.000000 | 1011.000000 |  | 22.940000 | 0.000000 | 10000.000000 | 120.000000 | 1.23 | 0.930000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 12:00:00 | 9.000000 | 20.660000 | 23.560000 | 87.000000 | 1012.000000 |  | 22.940000 | 0.290000 | 10000.000000 | 115.000000 | 2.54 | 1.820000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 13:00:00 | 15.000000 | 21.250000 | 25.580000 | 80.000000 | 1013.000000 |  | 24.940000 | 1.430000 | 10000.000000 | 128.000000 | 4.05 | 2.950000 | 801 | Clouds | few clouds | 02d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 14:00:00 | 50.000000 | 22.650000 | 30.950000 | 73.000000 | 1014.000000 |  | 27.940000 | 3.690000 | 10000.000000 | 128.000000 | 4.13 | 3.400000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 15:00:00 | 66.000000 | 21.950000 | 31.890000 | 66.000000 | 1014.000000 |  | 28.940000 | 6.570000 | 10000.000000 | 129.000000 | 3.67 | 3.170000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 21.600000 | 32.920000 | 61.000000 | 1013.000000 |  | 29.940000 | 8.010000 | 10000.000000 | 136.000000 | 3.13 | 2.830000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 17:00:00 | 80.000000 | 21.710000 | 34.240000 | 58.000000 | 1012.000000 |  | 30.940000 | 8.920000 | 10000.000000 | 134.000000 | 2.57 | 2.230000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 21.770000 | 35.520000 | 55.000000 | 1011.000000 |  | 31.940000 | 8.210000 | 10000.000000 | 158.000000 | 1.86 | 1.630000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 21.470000 | 35.250000 | 54.000000 | 1010.000000 |  | 31.940000 | 6.000000 | 10000.000000 | 198.000000 | 1.2 | 1.180000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 21.770000 | 35.520000 | 55.000000 | 1009.000000 |  | 31.940000 | 3.520000 | 10000.000000 | 255.000000 | 1.01 | 1.280000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 23.070000 | 35.480000 | 63.000000 | 1009.000000 |  | 30.940000 | 1.430000 | 10000.000000 | 289.000000 | 1.6 | 1.890000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 24.340000 | 35.380000 | 72.000000 | 1009.000000 |  | 29.940000 | 0.270000 | 10000.000000 | 313.000000 | 4.14 | 2.860000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 13085050 | "LORICA  ITA - AUT [13085050]" | 9.252722 | -75.844417 | 30.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-05-13 00:00:00 | 2010-10-02 00:00:00 | Córdoba | Lorica | Barroblanco | Area Operativa 02 - Atlántico-Bolivar-Sucre | Caribe | Sinú | Bajo Sinú | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 23.960000 | 31.800000 | 79.000000 | 1010.000000 |  | 27.940000 | 0.000000 | 10000.000000 | 322.000000 | 5.3 | 2.800000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station13085050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station13085050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station13085050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station13085050_OWM_Windspeed_20220111.png)
