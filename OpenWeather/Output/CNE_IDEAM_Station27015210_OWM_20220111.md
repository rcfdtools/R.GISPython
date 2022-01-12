
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VIVERO EL [27015210] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station27015210_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.28333333,-75.5) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.28333333&lon=-75.5)


| Parameter | Value |
|---|---|
| Code | 27015210 |
| Name | VIVERO EL [27015210] |
| Latitude, ° | 6.28333333 |
| Longitude, ° | -75.5 |
| Elevation, m | 2400 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1982-07-15 00:00:00 |
| Suspension date | 1996-06-15 00:00:00 |
| State | Antioquia |
| County | Guarne |
| Stream | San Lope |
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

### (CNE index 823) Open Weather values for station 27015210 - VIVERO EL [27015210]

JSON data from API OWM:

```
{'lat': 6.2833, 'lon': -75.5, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813353, 'sunset': 1641855766, 'temp': 18.58, 'feels_like': 18.19, 'pressure': 1020, 'humidity': 65, 'dew_point': 11.88, 'uvi': 1.6, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.52}}, 'hourly': [{'dt': 1641772800, 'temp': 15.69, 'feels_like': 15.38, 'pressure': 1020, 'humidity': 79, 'dew_point': 12.06, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 360, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.48}}, {'dt': 1641776400, 'temp': 14.1, 'feels_like': 13.97, 'pressure': 1026, 'humidity': 92, 'dew_point': 12.82, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641780000, 'temp': 13.53, 'feels_like': 13.42, 'pressure': 1026, 'humidity': 95, 'dew_point': 12.75, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 13.53, 'feels_like': 13.42, 'pressure': 1026, 'humidity': 95, 'dew_point': 12.75, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 13.53, 'feels_like': 13.42, 'pressure': 1026, 'humidity': 95, 'dew_point': 12.75, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 160, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 12.25, 'feels_like': 12.09, 'pressure': 1026, 'humidity': 98, 'dew_point': 11.94, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 12.25, 'feels_like': 12.12, 'pressure': 1025, 'humidity': 99, 'dew_point': 12.1, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 1.54, 'wind_deg': 110, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641798000, 'temp': 12.25, 'feels_like': 12.12, 'pressure': 1025, 'humidity': 99, 'dew_point': 12.1, 'uvi': 0, 'clouds': 75, 'visibility': 5000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}]}, {'dt': 1641801600, 'temp': 12.01, 'feels_like': 11.85, 'pressure': 1024, 'humidity': 99, 'dew_point': 11.86, 'uvi': 0, 'clouds': 75, 'visibility': 4000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}]}, {'dt': 1641805200, 'temp': 11.44, 'feels_like': 11.22, 'pressure': 1024, 'humidity': 99, 'dew_point': 11.29, 'uvi': 0, 'clouds': 75, 'visibility': 6000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641808800, 'temp': 12.01, 'feels_like': 11.77, 'pressure': 1024, 'humidity': 96, 'dew_point': 11.39, 'uvi': 0, 'clouds': 75, 'visibility': 6000, 'wind_speed': 2.06, 'wind_deg': 50, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641812400, 'temp': 11.97, 'feels_like': 11.73, 'pressure': 1021, 'humidity': 96, 'dew_point': 11.35, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 20, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 12.18, 'feels_like': 11.86, 'pressure': 1022, 'humidity': 92, 'dew_point': 10.92, 'uvi': 0.35, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 20, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 13.93, 'feels_like': 13.57, 'pressure': 1022, 'humidity': 84, 'dew_point': 11.27, 'uvi': 1.93, 'clouds': 90, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641823200, 'temp': 14.95, 'feels_like': 14.54, 'pressure': 1024, 'humidity': 78, 'dew_point': 11.15, 'uvi': 4.84, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641826800, 'temp': 14.88, 'feels_like': 14.41, 'pressure': 1024, 'humidity': 76, 'dew_point': 10.69, 'uvi': 8.39, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641830400, 'temp': 14.41, 'feels_like': 13.97, 'pressure': 1024, 'humidity': 79, 'dew_point': 10.82, 'uvi': 6.44, 'clouds': 90, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 180, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641834000, 'temp': 14.35, 'feels_like': 13.96, 'pressure': 1023, 'humidity': 81, 'dew_point': 11.14, 'uvi': 7.1, 'clouds': 90, 'visibility': 8000, 'wind_speed': 2.57, 'wind_deg': 230, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.35}}, {'dt': 1641837600, 'temp': 15.6, 'feels_like': 15.25, 'pressure': 1023, 'humidity': 78, 'dew_point': 11.78, 'uvi': 6.51, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 210, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641841200, 'temp': 16.95, 'feels_like': 16.55, 'pressure': 1021, 'humidity': 71, 'dew_point': 11.66, 'uvi': 2.71, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, {'dt': 1641844800, 'temp': 18.58, 'feels_like': 18.19, 'pressure': 1020, 'humidity': 65, 'dew_point': 11.88, 'uvi': 1.6, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.52}}, {'dt': 1641848400, 'temp': 17.71, 'feels_like': 17.23, 'pressure': 1019, 'humidity': 65, 'dew_point': 11.05, 'uvi': 0.65, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.46}}, {'dt': 1641852000, 'temp': 16.76, 'feels_like': 16.35, 'pressure': 1020, 'humidity': 71, 'dew_point': 11.48, 'uvi': 0.21, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641855600, 'temp': 15.01, 'feels_like': 14.68, 'pressure': 1021, 'humidity': 81, 'dew_point': 11.78, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 00:00:00 | 75.000000 | 12.060000 | 15.380000 | 79.000000 | 1020.000000 | 0.48 | 15.690000 | 0.000000 | 10000.000000 | 360.000000 |  | 5.140000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 12.820000 | 13.970000 | 92.000000 | 1026.000000 | 0.18 | 14.100000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 02:00:00 | 75.000000 | 12.750000 | 13.420000 | 95.000000 | 1026.000000 |  | 13.530000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 03:00:00 | 75.000000 | 12.750000 | 13.420000 | 95.000000 | 1026.000000 |  | 13.530000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 04:00:00 | 75.000000 | 12.750000 | 13.420000 | 95.000000 | 1026.000000 |  | 13.530000 | 0.000000 | 10000.000000 | 160.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 05:00:00 | 75.000000 | 11.940000 | 12.090000 | 98.000000 | 1026.000000 |  | 12.250000 | 0.000000 | 10000.000000 | 300.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 12.100000 | 12.120000 | 99.000000 | 1025.000000 |  | 12.250000 | 0.000000 | 7000.000000 | 110.000000 |  | 1.540000 | 741 | Fog | fog | 50n | 06 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 07:00:00 | 75.000000 | 12.100000 | 12.120000 | 99.000000 | 1025.000000 |  | 12.250000 | 0.000000 | 5000.000000 | 0.000000 |  | 0.000000 | 701 | Mist | mist | 50n | 07 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 08:00:00 | 75.000000 | 11.860000 | 11.850000 | 99.000000 | 1024.000000 |  | 12.010000 | 0.000000 | 4000.000000 | 0.000000 |  | 0.000000 | 701 | Mist | mist | 50n | 08 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 09:00:00 | 75.000000 | 11.290000 | 11.220000 | 99.000000 | 1024.000000 |  | 11.440000 | 0.000000 | 6000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50n | 09 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 10:00:00 | 75.000000 | 11.390000 | 11.770000 | 96.000000 | 1024.000000 |  | 12.010000 | 0.000000 | 6000.000000 | 50.000000 |  | 2.060000 | 741 | Fog | fog | 50n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 11.350000 | 11.730000 | 96.000000 | 1021.000000 |  | 11.970000 | 0.000000 | 10000.000000 | 20.000000 |  | 3.090000 | 741 | Fog | fog | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 12:00:00 | 90.000000 | 10.920000 | 11.860000 | 92.000000 | 1022.000000 |  | 12.180000 | 0.350000 | 10000.000000 | 20.000000 |  | 2.570000 | 741 | Fog | fog | 50d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 13:00:00 | 90.000000 | 11.270000 | 13.570000 | 84.000000 | 1022.000000 | 0.11 | 13.930000 | 1.930000 | 10000.000000 | 20.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 14:00:00 | 90.000000 | 11.150000 | 14.540000 | 78.000000 | 1024.000000 | 0.17 | 14.950000 | 4.840000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 15:00:00 | 90.000000 | 10.690000 | 14.410000 | 76.000000 | 1024.000000 | 0.3 | 14.880000 | 8.390000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 16:00:00 | 90.000000 | 10.820000 | 13.970000 | 79.000000 | 1024.000000 | 0.41 | 14.410000 | 6.440000 | 10000.000000 | 180.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 11.140000 | 13.960000 | 81.000000 | 1023.000000 | 0.35 | 14.350000 | 7.100000 | 8000.000000 | 230.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 11.780000 | 15.250000 | 78.000000 | 1023.000000 | 0.66 | 15.600000 | 6.510000 | 10000.000000 | 210.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 11.660000 | 16.550000 | 71.000000 | 1021.000000 | 1.37 | 16.950000 | 2.710000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 11.880000 | 18.190000 | 65.000000 | 1020.000000 | 1.52 | 18.580000 | 1.600000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 11.050000 | 17.230000 | 65.000000 | 1019.000000 | 1.46 | 17.710000 | 0.650000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 11.480000 | 16.350000 | 71.000000 | 1020.000000 | 0.5 | 16.760000 | 0.210000 | 10000.000000 | 10.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015210 | "VIVERO EL [27015210]" | 6.283333 | -75.500000 | 2400.000000 | Climática Principal | Convencional | Suspendida | 1982-07-15 00:00:00 | 1996-06-15 00:00:00 | Antioquia | Guarne | San Lope | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 11.780000 | 14.680000 | 81.000000 | 1021.000000 | 0.31 | 15.010000 | 0.000000 | 10000.000000 | 10.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station27015210_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Rain_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Temp_20220111.png)
![CNE_IDEAM_Station27015210_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_UVI_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station27015210_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015210_OWM_Windspeed_20220111.png)
