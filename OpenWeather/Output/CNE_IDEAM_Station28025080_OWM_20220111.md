
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SOCOMBA [28025080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28025080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.68666667,-73.24055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.68666667&lon=-73.24055556)


| Parameter | Value |
|---|---|
| Code | 28025080 |
| Name | SOCOMBA [28025080] |
| Latitude, ° | 9.68666667 |
| Longitude, ° | -73.24055556 |
| Elevation, m | 170 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1976-12-14 19:00:00 |
| Suspension date | 2019-07-02 06:41:01 |
| State | Cesar |
| County | Becerrill |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Medio Cesar |

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

### (CNE index 2647) Open Weather values for station 28025080 - SOCOMBA [28025080]

JSON data from API OWM:

```
{'lat': 9.6867, 'lon': -73.2406, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813145, 'sunset': 1641854890, 'temp': 34.86, 'feels_like': 34.08, 'pressure': 1008, 'humidity': 28, 'dew_point': 13.66, 'uvi': 3.65, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 110, 'wind_gust': 1.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26, 'feels_like': 26, 'pressure': 1012, 'humidity': 50, 'dew_point': 14.78, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 3.74, 'wind_deg': 111, 'wind_gust': 6.88, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 24.98, 'feels_like': 24.97, 'pressure': 1013, 'humidity': 55, 'dew_point': 15.32, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 3.65, 'wind_deg': 112, 'wind_gust': 6.82, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.22, 'feels_like': 24.21, 'pressure': 1013, 'humidity': 58, 'dew_point': 15.44, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 3.24, 'wind_deg': 110, 'wind_gust': 6.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 23.52, 'feels_like': 23.49, 'pressure': 1013, 'humidity': 60, 'dew_point': 15.31, 'uvi': 0, 'clouds': 10, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 108, 'wind_gust': 6.26, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 22.71, 'feels_like': 22.68, 'pressure': 1013, 'humidity': 63, 'dew_point': 15.31, 'uvi': 0, 'clouds': 10, 'visibility': 10000, 'wind_speed': 3.16, 'wind_deg': 110, 'wind_gust': 4.9, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 22, 'feels_like': 21.98, 'pressure': 1013, 'humidity': 66, 'dew_point': 15.36, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 2.89, 'wind_deg': 109, 'wind_gust': 4.16, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 21.58, 'feels_like': 21.54, 'pressure': 1012, 'humidity': 67, 'dew_point': 15.2, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 109, 'wind_gust': 3.64, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 21.4, 'feels_like': 21.37, 'pressure': 1012, 'humidity': 68, 'dew_point': 15.25, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 109, 'wind_gust': 3.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.3, 'feels_like': 21.29, 'pressure': 1012, 'humidity': 69, 'dew_point': 15.39, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 108, 'wind_gust': 2.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.15, 'feels_like': 21.12, 'pressure': 1012, 'humidity': 69, 'dew_point': 15.24, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 104, 'wind_gust': 2.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.11, 'feels_like': 21.08, 'pressure': 1012, 'humidity': 69, 'dew_point': 15.21, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 104, 'wind_gust': 2.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.05, 'feels_like': 21.04, 'pressure': 1013, 'humidity': 70, 'dew_point': 15.37, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 108, 'wind_gust': 2.36, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 22.38, 'feels_like': 22.4, 'pressure': 1014, 'humidity': 66, 'dew_point': 15.72, 'uvi': 0.4, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 110, 'wind_gust': 2.51, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 26.56, 'feels_like': 26.56, 'pressure': 1015, 'humidity': 52, 'dew_point': 15.91, 'uvi': 1.79, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 102, 'wind_gust': 2.29, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 29.84, 'feels_like': 29.74, 'pressure': 1015, 'humidity': 42, 'dew_point': 15.55, 'uvi': 4.36, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 74, 'wind_gust': 2.01, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 32.04, 'feels_like': 31.52, 'pressure': 1014, 'humidity': 35, 'dew_point': 14.67, 'uvi': 7.37, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 20, 'wind_gust': 2.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 33.7, 'feels_like': 33.06, 'pressure': 1013, 'humidity': 31, 'dew_point': 14.23, 'uvi': 9.72, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 323, 'wind_gust': 1.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 34.84, 'feels_like': 34.06, 'pressure': 1012, 'humidity': 28, 'dew_point': 13.64, 'uvi': 10.49, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 350, 'wind_gust': 1.83, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 36.02, 'feels_like': 35.28, 'pressure': 1010, 'humidity': 26, 'dew_point': 13.5, 'uvi': 9.36, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 87, 'wind_gust': 1.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 36.03, 'feels_like': 35.29, 'pressure': 1009, 'humidity': 26, 'dew_point': 13.51, 'uvi': 6.58, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 101, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 34.86, 'feels_like': 34.08, 'pressure': 1008, 'humidity': 28, 'dew_point': 13.66, 'uvi': 3.65, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 110, 'wind_gust': 1.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.39, 'feels_like': 32.81, 'pressure': 1008, 'humidity': 32, 'dew_point': 14.46, 'uvi': 1.38, 'clouds': 95, 'visibility': 10000, 'wind_speed': 3.34, 'wind_deg': 111, 'wind_gust': 2.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.96, 'feels_like': 30.86, 'pressure': 1009, 'humidity': 40, 'dew_point': 15.79, 'uvi': 0.26, 'clouds': 79, 'visibility': 10000, 'wind_speed': 3.95, 'wind_deg': 111, 'wind_gust': 5.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.62, 'feels_like': 27.96, 'pressure': 1010, 'humidity': 49, 'dew_point': 15.95, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 3.4, 'wind_deg': 120, 'wind_gust': 6.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 00:00:00 | 13.000000 | 14.780000 | 26.000000 | 50.000000 | 1012.000000 |  | 26.000000 | 0.000000 | 10000.000000 | 111.000000 | 6.88 | 3.740000 | 801 | Clouds | few clouds | 02n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 01:00:00 | 8.000000 | 15.320000 | 24.970000 | 55.000000 | 1013.000000 |  | 24.980000 | 0.000000 | 10000.000000 | 112.000000 | 6.82 | 3.650000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 02:00:00 | 7.000000 | 15.440000 | 24.210000 | 58.000000 | 1013.000000 |  | 24.220000 | 0.000000 | 10000.000000 | 110.000000 | 6.28 | 3.240000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 03:00:00 | 10.000000 | 15.310000 | 23.490000 | 60.000000 | 1013.000000 |  | 23.520000 | 0.000000 | 10000.000000 | 108.000000 | 6.26 | 3.270000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 04:00:00 | 10.000000 | 15.310000 | 22.680000 | 63.000000 | 1013.000000 |  | 22.710000 | 0.000000 | 10000.000000 | 110.000000 | 4.9 | 3.160000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 05:00:00 | 9.000000 | 15.360000 | 21.980000 | 66.000000 | 1013.000000 |  | 22.000000 | 0.000000 | 10000.000000 | 109.000000 | 4.16 | 2.890000 | 800 | Clear | clear sky | 01n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 06:00:00 | 44.000000 | 15.200000 | 21.540000 | 67.000000 | 1012.000000 |  | 21.580000 | 0.000000 | 10000.000000 | 109.000000 | 3.64 | 2.600000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 07:00:00 | 62.000000 | 15.250000 | 21.370000 | 68.000000 | 1012.000000 |  | 21.400000 | 0.000000 | 10000.000000 | 109.000000 | 3.16 | 2.470000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 08:00:00 | 80.000000 | 15.390000 | 21.290000 | 69.000000 | 1012.000000 |  | 21.300000 | 0.000000 | 10000.000000 | 108.000000 | 2.45 | 2.250000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 15.240000 | 21.120000 | 69.000000 | 1012.000000 |  | 21.150000 | 0.000000 | 10000.000000 | 104.000000 | 2.44 | 2.250000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 10:00:00 | 54.000000 | 15.210000 | 21.080000 | 69.000000 | 1012.000000 |  | 21.110000 | 0.000000 | 10000.000000 | 104.000000 | 2.44 | 2.280000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 11:00:00 | 44.000000 | 15.370000 | 21.040000 | 70.000000 | 1013.000000 |  | 21.050000 | 0.000000 | 10000.000000 | 108.000000 | 2.36 | 2.150000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 12:00:00 | 45.000000 | 15.720000 | 22.400000 | 66.000000 | 1014.000000 |  | 22.380000 | 0.400000 | 10000.000000 | 110.000000 | 2.51 | 1.820000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 13:00:00 | 39.000000 | 15.910000 | 26.560000 | 52.000000 | 1015.000000 |  | 26.560000 | 1.790000 | 10000.000000 | 102.000000 | 2.29 | 1.250000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 14:00:00 | 44.000000 | 15.550000 | 29.740000 | 42.000000 | 1015.000000 |  | 29.840000 | 4.360000 | 10000.000000 | 74.000000 | 2.01 | 0.520000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 15:00:00 | 58.000000 | 14.670000 | 31.520000 | 35.000000 | 1014.000000 |  | 32.040000 | 7.370000 | 10000.000000 | 20.000000 | 2.33 | 0.340000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 16:00:00 | 57.000000 | 14.230000 | 33.060000 | 31.000000 | 1013.000000 |  | 33.700000 | 9.720000 | 10000.000000 | 323.000000 | 1.97 | 0.490000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 17:00:00 | 49.000000 | 13.640000 | 34.060000 | 28.000000 | 1012.000000 |  | 34.840000 | 10.490000 | 10000.000000 | 350.000000 | 1.83 | 0.450000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 18:00:00 | 84.000000 | 13.500000 | 35.280000 | 26.000000 | 1010.000000 |  | 36.020000 | 9.360000 | 10000.000000 | 87.000000 | 1.64 | 0.610000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 19:00:00 | 93.000000 | 13.510000 | 35.290000 | 26.000000 | 1009.000000 |  | 36.030000 | 6.580000 | 10000.000000 | 101.000000 | 1.49 | 1.060000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 20:00:00 | 96.000000 | 13.660000 | 34.080000 | 28.000000 | 1008.000000 |  | 34.860000 | 3.650000 | 10000.000000 | 110.000000 | 1.63 | 1.970000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 21:00:00 | 95.000000 | 14.460000 | 32.810000 | 32.000000 | 1008.000000 |  | 33.390000 | 1.380000 | 10000.000000 | 111.000000 | 2.58 | 3.340000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 22:00:00 | 79.000000 | 15.790000 | 30.860000 | 40.000000 | 1009.000000 |  | 30.960000 | 0.260000 | 10000.000000 | 111.000000 | 5.67 | 3.950000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025080 | "SOCOMBA [28025080]" | 9.686667 | -73.240556 | 170.000000 | Climática Principal | Convencional | Suspendida | 1976-12-14 19:00:00 | 2019-07-02 06:41:01 | Cesar | Becerrill | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 23:00:00 | 71.000000 | 15.950000 | 27.960000 | 49.000000 | 1010.000000 |  | 27.620000 | 0.000000 | 10000.000000 | 120.000000 | 6.48 | 3.400000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28025080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28025080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28025080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025080_OWM_Windspeed_20220111.png)
