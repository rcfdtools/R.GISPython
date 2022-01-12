
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - FEDEARROZ - AUT [28035060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28035060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.46361111,-73.24805556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.46361111&lon=-73.24805556)


| Parameter | Value |
|---|---|
| Code | 28035060 |
| Name | FEDEARROZ - AUT [28035060] |
| Latitude, ° | 10.46361111 |
| Longitude, ° | -73.24805556 |
| Elevation, m | 184 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-08-16 00:00:00 |
| Suspension date | NaT |
| State | Cesar |
| County | Valledupar |
| Stream | Cauca |
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

### (CNE index 233) Open Weather values for station 28035060 - FEDEARROZ - AUT [28035060]

JSON data from API OWM:

```
{'lat': 10.4636, 'lon': -73.2481, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813224, 'sunset': 1641854814, 'temp': 33.85, 'feels_like': 33.26, 'pressure': 1011, 'humidity': 31, 'dew_point': 14.36, 'uvi': 2.97, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 60, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.85, 'feels_like': 28.92, 'pressure': 1012, 'humidity': 45, 'dew_point': 15.74, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 70, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 27.85, 'feels_like': 28.37, 'pressure': 1013, 'humidity': 51, 'dew_point': 16.79, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 26.85, 'feels_like': 27.51, 'pressure': 1014, 'humidity': 54, 'dew_point': 16.77, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 50, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 26.85, 'feels_like': 27.51, 'pressure': 1014, 'humidity': 54, 'dew_point': 16.77, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 26.85, 'feels_like': 27.51, 'pressure': 1014, 'humidity': 54, 'dew_point': 16.77, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 6.17, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 21.48, 'feels_like': 21.28, 'pressure': 1013, 'humidity': 61, 'dew_point': 13.65, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 4.14, 'wind_deg': 22, 'wind_gust': 8.12, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 21.06, 'feels_like': 20.71, 'pressure': 1012, 'humidity': 57, 'dew_point': 12.22, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 3.66, 'wind_deg': 23, 'wind_gust': 7.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 20.89, 'feels_like': 20.5, 'pressure': 1012, 'humidity': 56, 'dew_point': 11.79, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 21, 'wind_gust': 6.08, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 20.73, 'feels_like': 20.32, 'pressure': 1012, 'humidity': 56, 'dew_point': 11.65, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 2.89, 'wind_deg': 21, 'wind_gust': 5.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.57, 'feels_like': 20.2, 'pressure': 1012, 'humidity': 58, 'dew_point': 12.03, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 2.74, 'wind_deg': 17, 'wind_gust': 4.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.37, 'feels_like': 20.03, 'pressure': 1012, 'humidity': 60, 'dew_point': 12.36, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 16, 'wind_gust': 4.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.85, 'feels_like': 22.97, 'pressure': 1014, 'humidity': 68, 'dew_point': 16.64, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 23.85, 'feels_like': 23.96, 'pressure': 1015, 'humidity': 64, 'dew_point': 16.63, 'uvi': 0.4, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 25.85, 'feels_like': 26.08, 'pressure': 1016, 'humidity': 61, 'dew_point': 17.76, 'uvi': 1.95, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 27.85, 'feels_like': 28.04, 'pressure': 1016, 'humidity': 47, 'dew_point': 15.51, 'uvi': 4.76, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 29.85, 'feels_like': 29.75, 'pressure': 1016, 'humidity': 42, 'dew_point': 15.56, 'uvi': 8.08, 'clouds': 20, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 70, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 30.85, 'feels_like': 30.32, 'pressure': 1015, 'humidity': 37, 'dew_point': 14.48, 'uvi': 10.65, 'clouds': 20, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 32.85, 'feels_like': 32.26, 'pressure': 1014, 'humidity': 33, 'dew_point': 14.46, 'uvi': 11.48, 'clouds': 40, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 50, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 32.85, 'feels_like': 32.26, 'pressure': 1013, 'humidity': 33, 'dew_point': 14.46, 'uvi': 10.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 70, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 33.85, 'feels_like': 33.63, 'pressure': 1011, 'humidity': 33, 'dew_point': 15.33, 'uvi': 5.37, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 70, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 33.85, 'feels_like': 33.26, 'pressure': 1011, 'humidity': 31, 'dew_point': 14.36, 'uvi': 2.97, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 60, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.85, 'feels_like': 33.26, 'pressure': 1010, 'humidity': 31, 'dew_point': 14.36, 'uvi': 1.11, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 70, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 32.85, 'feels_like': 32.59, 'pressure': 1011, 'humidity': 35, 'dew_point': 15.38, 'uvi': 0.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 70, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 30.85, 'feels_like': 30.72, 'pressure': 1011, 'humidity': 40, 'dew_point': 15.69, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 70, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 15.740000 | 28.920000 | 45.000000 | 1012.000000 |  | 28.850000 | 0.000000 | 10000.000000 | 70.000000 |  | 5.140000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 16.790000 | 28.370000 | 51.000000 | 1013.000000 |  | 27.850000 | 0.000000 | 10000.000000 | 60.000000 |  | 7.200000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 16.770000 | 27.510000 | 54.000000 | 1014.000000 |  | 26.850000 | 0.000000 | 10000.000000 | 50.000000 |  | 6.170000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 16.770000 | 27.510000 | 54.000000 | 1014.000000 |  | 26.850000 | 0.000000 | 10000.000000 | 60.000000 |  | 6.170000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 04:00:00 | 20.000000 | 16.770000 | 27.510000 | 54.000000 | 1014.000000 |  | 26.850000 | 0.000000 | 10000.000000 | 60.000000 |  | 6.170000 | 801 | Clouds | few clouds | 02n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 05:00:00 | 31.000000 | 13.650000 | 21.280000 | 61.000000 | 1013.000000 |  | 21.480000 | 0.000000 | 10000.000000 | 22.000000 | 8.12 | 4.140000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 06:00:00 | 7.000000 | 12.220000 | 20.710000 | 57.000000 | 1012.000000 |  | 21.060000 | 0.000000 | 10000.000000 | 23.000000 | 7.28 | 3.660000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 07:00:00 | 6.000000 | 11.790000 | 20.500000 | 56.000000 | 1012.000000 |  | 20.890000 | 0.000000 | 10000.000000 | 21.000000 | 6.08 | 3.190000 | 800 | Clear | clear sky | 01n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 08:00:00 | 53.000000 | 11.650000 | 20.320000 | 56.000000 | 1012.000000 |  | 20.730000 | 0.000000 | 10000.000000 | 21.000000 | 5.49 | 2.890000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 09:00:00 | 69.000000 | 12.030000 | 20.200000 | 58.000000 | 1012.000000 |  | 20.570000 | 0.000000 | 10000.000000 | 17.000000 | 4.72 | 2.740000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 10:00:00 | 76.000000 | 12.360000 | 20.030000 | 60.000000 | 1012.000000 |  | 20.370000 | 0.000000 | 10000.000000 | 16.000000 | 4.28 | 2.670000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 16.640000 | 22.970000 | 68.000000 | 1014.000000 |  | 22.850000 | 0.000000 | 10000.000000 | 60.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 16.630000 | 23.960000 | 64.000000 | 1015.000000 |  | 23.850000 | 0.400000 | 10000.000000 | 40.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 17.760000 | 26.080000 | 61.000000 | 1016.000000 |  | 25.850000 | 1.950000 | 10000.000000 | 60.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 15.510000 | 28.040000 | 47.000000 | 1016.000000 |  | 27.850000 | 4.760000 | 10000.000000 | 60.000000 |  | 5.660000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 15:00:00 | 20.000000 | 15.560000 | 29.750000 | 42.000000 | 1016.000000 |  | 29.850000 | 8.080000 | 10000.000000 | 70.000000 |  | 6.690000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 16:00:00 | 20.000000 | 14.480000 | 30.320000 | 37.000000 | 1015.000000 |  | 30.850000 | 10.650000 | 10000.000000 | 60.000000 |  | 7.200000 | 801 | Clouds | few clouds | 02d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 14.460000 | 32.260000 | 33.000000 | 1014.000000 |  | 32.850000 | 11.480000 | 10000.000000 | 50.000000 |  | 6.690000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 14.460000 | 32.260000 | 33.000000 | 1013.000000 |  | 32.850000 | 10.240000 | 10000.000000 | 70.000000 |  | 4.630000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 15.330000 | 33.630000 | 33.000000 | 1011.000000 |  | 33.850000 | 5.370000 | 10000.000000 | 70.000000 |  | 5.140000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 14.360000 | 33.260000 | 31.000000 | 1011.000000 |  | 33.850000 | 2.970000 | 10000.000000 | 60.000000 |  | 4.630000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 21:00:00 | 40.000000 | 14.360000 | 33.260000 | 31.000000 | 1010.000000 |  | 33.850000 | 1.110000 | 10000.000000 | 70.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 22:00:00 | 40.000000 | 15.380000 | 32.590000 | 35.000000 | 1011.000000 |  | 32.850000 | 0.080000 | 10000.000000 | 70.000000 |  | 4.120000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28035060 | "FEDEARROZ - AUT [28035060]" | 10.463611 | -73.248056 | 184.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-16 00:00:00 | NaT | Cesar | Valledupar | Cauca | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Medio Cesar | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 15.690000 | 30.720000 | 40.000000 | 1011.000000 |  | 30.850000 | 0.000000 | 10000.000000 | 70.000000 |  | 4.630000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28035060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28035060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28035060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28035060_OWM_Windspeed_20220111.png)
