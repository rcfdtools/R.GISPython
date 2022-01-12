
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GUAIRA LA HACIENDA [28045040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28045040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.61666667,-73.8) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.61666667&lon=-73.8)


| Parameter | Value |
|---|---|
| Code | 28045040 |
| Name | GUAIRA LA HACIENDA [28045040] |
| Latitude, ° | 9.61666667 |
| Longitude, ° | -73.8 |
| Elevation, m | 50 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1987-09-15 00:00:00 |
| Suspension date | 1994-07-15 00:00:00 |
| State | Cesar |
| County | El Paso |
| Stream | Lago La Divisa |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Río Ariguaní |

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

### (CNE index 2715) Open Weather values for station 28045040 - GUAIRA LA HACIENDA [28045040]

JSON data from API OWM:

```
{'lat': 9.6167, 'lon': -73.8, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813272, 'sunset': 1641855031, 'temp': 36.37, 'feels_like': 35.15, 'pressure': 1007, 'humidity': 23, 'dew_point': 11.93, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 219, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.74, 'feels_like': 26.92, 'pressure': 1009, 'humidity': 45, 'dew_point': 13.83, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 117, 'wind_gust': 3.57, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 25.61, 'feels_like': 25.48, 'pressure': 1010, 'humidity': 48, 'dew_point': 13.79, 'uvi': 0, 'clouds': 17, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 96, 'wind_gust': 2.95, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 24.61, 'feels_like': 24.46, 'pressure': 1011, 'humidity': 51, 'dew_point': 13.81, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 74, 'wind_gust': 2.41, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 23.75, 'feels_like': 23.59, 'pressure': 1011, 'humidity': 54, 'dew_point': 13.9, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 28, 'wind_gust': 2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 23.21, 'feels_like': 23.05, 'pressure': 1011, 'humidity': 56, 'dew_point': 13.95, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 26, 'wind_gust': 2.47, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 22.77, 'feels_like': 22.62, 'pressure': 1011, 'humidity': 58, 'dew_point': 14.08, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 46, 'wind_gust': 4.08, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 22.1, 'feels_like': 21.93, 'pressure': 1011, 'humidity': 60, 'dew_point': 13.98, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 69, 'wind_gust': 4.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.52, 'feels_like': 21.37, 'pressure': 1010, 'humidity': 63, 'dew_point': 14.19, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 84, 'wind_gust': 4.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.96, 'feels_like': 20.81, 'pressure': 1010, 'humidity': 65, 'dew_point': 14.14, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 82, 'wind_gust': 3.62, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.39, 'feels_like': 20.26, 'pressure': 1010, 'humidity': 68, 'dew_point': 14.29, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 71, 'wind_gust': 3.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.05, 'feels_like': 19.91, 'pressure': 1011, 'humidity': 69, 'dew_point': 14.19, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 68, 'wind_gust': 2.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.83, 'feels_like': 19.67, 'pressure': 1012, 'humidity': 69, 'dew_point': 13.98, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 61, 'wind_gust': 1.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 21.25, 'feels_like': 21.15, 'pressure': 1013, 'humidity': 66, 'dew_point': 14.65, 'uvi': 0.37, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 73, 'wind_gust': 2.74, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 25.04, 'feels_like': 24.98, 'pressure': 1014, 'humidity': 53, 'dew_point': 14.8, 'uvi': 1.71, 'clouds': 12, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 75, 'wind_gust': 3.79, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 28.29, 'feels_like': 28.24, 'pressure': 1014, 'humidity': 44, 'dew_point': 14.88, 'uvi': 4.22, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 75, 'wind_gust': 3.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 31.29, 'feels_like': 30.86, 'pressure': 1014, 'humidity': 37, 'dew_point': 14.87, 'uvi': 7.22, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 91, 'wind_gust': 2.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 33.67, 'feels_like': 33.02, 'pressure': 1013, 'humidity': 31, 'dew_point': 14.21, 'uvi': 9.68, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 114, 'wind_gust': 2.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 35.31, 'feels_like': 34.51, 'pressure': 1011, 'humidity': 27, 'dew_point': 13.48, 'uvi': 10.5, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 130, 'wind_gust': 2.38, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 36.47, 'feels_like': 35.69, 'pressure': 1009, 'humidity': 25, 'dew_point': 13.28, 'uvi': 9.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 148, 'wind_gust': 2.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 36.78, 'feels_like': 35.69, 'pressure': 1008, 'humidity': 23, 'dew_point': 12.27, 'uvi': 6.6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 176, 'wind_gust': 2.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 36.37, 'feels_like': 35.15, 'pressure': 1007, 'humidity': 23, 'dew_point': 11.93, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 219, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 35.41, 'feels_like': 34.1, 'pressure': 1007, 'humidity': 24, 'dew_point': 11.77, 'uvi': 1.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 240, 'wind_gust': 1.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 33.01, 'feels_like': 32.01, 'pressure': 1007, 'humidity': 30, 'dew_point': 13.14, 'uvi': 0.28, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 227, 'wind_gust': 2.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.44, 'feels_like': 28.14, 'pressure': 1008, 'humidity': 41, 'dew_point': 13.93, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 228, 'wind_gust': 4.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 13.830000 | 26.920000 | 45.000000 | 1009.000000 |  | 26.740000 | 0.000000 | 10000.000000 | 117.000000 | 3.57 | 1.620000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 01:00:00 | 17.000000 | 13.790000 | 25.480000 | 48.000000 | 1010.000000 |  | 25.610000 | 0.000000 | 10000.000000 | 96.000000 | 2.95 | 1.110000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 02:00:00 | 24.000000 | 13.810000 | 24.460000 | 51.000000 | 1011.000000 |  | 24.610000 | 0.000000 | 10000.000000 | 74.000000 | 2.41 | 0.840000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 03:00:00 | 30.000000 | 13.900000 | 23.590000 | 54.000000 | 1011.000000 |  | 23.750000 | 0.000000 | 10000.000000 | 28.000000 | 2 | 0.910000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 04:00:00 | 29.000000 | 13.950000 | 23.050000 | 56.000000 | 1011.000000 |  | 23.210000 | 0.000000 | 10000.000000 | 26.000000 | 2.47 | 1.270000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 05:00:00 | 24.000000 | 14.080000 | 22.620000 | 58.000000 | 1011.000000 |  | 22.770000 | 0.000000 | 10000.000000 | 46.000000 | 4.08 | 1.630000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 06:00:00 | 80.000000 | 13.980000 | 21.930000 | 60.000000 | 1011.000000 |  | 22.100000 | 0.000000 | 10000.000000 | 69.000000 | 4.62 | 1.690000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 07:00:00 | 88.000000 | 14.190000 | 21.370000 | 63.000000 | 1010.000000 |  | 21.520000 | 0.000000 | 10000.000000 | 84.000000 | 4.19 | 1.690000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 14.140000 | 20.810000 | 65.000000 | 1010.000000 |  | 20.960000 | 0.000000 | 10000.000000 | 82.000000 | 3.62 | 1.640000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 09:00:00 | 86.000000 | 14.290000 | 20.260000 | 68.000000 | 1010.000000 |  | 20.390000 | 0.000000 | 10000.000000 | 71.000000 | 3.15 | 1.590000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 10:00:00 | 73.000000 | 14.190000 | 19.910000 | 69.000000 | 1011.000000 |  | 20.050000 | 0.000000 | 10000.000000 | 68.000000 | 2.64 | 1.230000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 11:00:00 | 59.000000 | 13.980000 | 19.670000 | 69.000000 | 1012.000000 |  | 19.830000 | 0.000000 | 10000.000000 | 61.000000 | 1.48 | 1.020000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 12:00:00 | 11.000000 | 14.650000 | 21.150000 | 66.000000 | 1013.000000 |  | 21.250000 | 0.370000 | 10000.000000 | 73.000000 | 2.74 | 1.040000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 13:00:00 | 12.000000 | 14.800000 | 24.980000 | 53.000000 | 1014.000000 |  | 25.040000 | 1.710000 | 10000.000000 | 75.000000 | 3.79 | 2.040000 | 801 | Clouds | few clouds | 02d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 14:00:00 | 38.000000 | 14.880000 | 28.240000 | 44.000000 | 1014.000000 |  | 28.290000 | 4.220000 | 10000.000000 | 75.000000 | 3.75 | 2.340000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 15:00:00 | 54.000000 | 14.870000 | 30.860000 | 37.000000 | 1014.000000 |  | 31.290000 | 7.220000 | 10000.000000 | 91.000000 | 2.49 | 1.620000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 16:00:00 | 59.000000 | 14.210000 | 33.020000 | 31.000000 | 1013.000000 |  | 33.670000 | 9.680000 | 10000.000000 | 114.000000 | 2.26 | 1.340000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 17:00:00 | 50.000000 | 13.480000 | 34.510000 | 27.000000 | 1011.000000 |  | 35.310000 | 10.500000 | 10000.000000 | 130.000000 | 2.38 | 1.350000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 13.280000 | 35.690000 | 25.000000 | 1009.000000 |  | 36.470000 | 9.430000 | 10000.000000 | 148.000000 | 2.22 | 1.020000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 12.270000 | 35.690000 | 23.000000 | 1008.000000 |  | 36.780000 | 6.600000 | 10000.000000 | 176.000000 | 2.13 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 11.930000 | 35.150000 | 23.000000 | 1007.000000 |  | 36.370000 | 3.700000 | 10000.000000 | 219.000000 | 2.03 | 0.550000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 11.770000 | 34.100000 | 24.000000 | 1007.000000 |  | 35.410000 | 1.420000 | 10000.000000 | 240.000000 | 1.85 | 0.850000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 13.140000 | 32.010000 | 30.000000 | 1007.000000 |  | 33.010000 | 0.280000 | 10000.000000 | 227.000000 | 2.84 | 1.510000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28045040 | "GUAIRA LA HACIENDA [28045040]" | 9.616667 | -73.800000 | 50.000000 | Climática Principal | Convencional | Suspendida | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | Cesar | El Paso | Lago La Divisa | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Río Ariguaní | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 13.930000 | 28.140000 | 41.000000 | 1008.000000 |  | 28.440000 | 0.000000 | 10000.000000 | 228.000000 | 4.97 | 1.990000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28045040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28045040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28045040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28045040_OWM_Windspeed_20220111.png)
