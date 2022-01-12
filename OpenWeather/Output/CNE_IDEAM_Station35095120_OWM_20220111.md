
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AQUITANIA - AUT [35095120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35095120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.55663889,-72.88175) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.55663889&lon=-72.88175)


| Parameter | Value |
|---|---|
| Code | 35095120 |
| Name | AQUITANIA - AUT [35095120] |
| Latitude, ° | 5.55663889 |
| Longitude, ° | -72.88175 |
| Elevation, m | 321 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-12-06 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Aquitania |
| Stream | Tocaria |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Lago de Tota |

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

### (CNE index 148) Open Weather values for station 35095120 - AQUITANIA - AUT [35095120]

JSON data from API OWM:

```
{'lat': 5.5566, 'lon': -72.8818, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812654, 'sunset': 1641855208, 'temp': 13.24, 'feels_like': 12.53, 'pressure': 1013, 'humidity': 73, 'dew_point': 8.51, 'uvi': 4.8, 'clouds': 99, 'visibility': 7410, 'wind_speed': 0.77, 'wind_deg': 227, 'wind_gust': 2.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, 'hourly': [{'dt': 1641772800, 'temp': 9.85, 'feels_like': 9.85, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.09, 'uvi': 0, 'clouds': 95, 'visibility': 2914, 'wind_speed': 0.52, 'wind_deg': 205, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.75, 'feels_like': 9.75, 'pressure': 1018, 'humidity': 96, 'dew_point': 9.14, 'uvi': 0, 'clouds': 96, 'visibility': 2798, 'wind_speed': 0.41, 'wind_deg': 240, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 9.61, 'feels_like': 9.61, 'pressure': 1019, 'humidity': 96, 'dew_point': 9, 'uvi': 0, 'clouds': 96, 'visibility': 2797, 'wind_speed': 0.34, 'wind_deg': 221, 'wind_gust': 1.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641783600, 'temp': 8.96, 'feels_like': 8.96, 'pressure': 1019, 'humidity': 97, 'dew_point': 8.51, 'uvi': 0, 'clouds': 93, 'visibility': 2816, 'wind_speed': 0.31, 'wind_deg': 231, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.36, 'feels_like': 8.36, 'pressure': 1019, 'humidity': 96, 'dew_point': 7.76, 'uvi': 0, 'clouds': 95, 'visibility': 7620, 'wind_speed': 0.53, 'wind_deg': 252, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 8.14, 'feels_like': 8.14, 'pressure': 1019, 'humidity': 96, 'dew_point': 7.54, 'uvi': 0, 'clouds': 95, 'visibility': 5704, 'wind_speed': 0.81, 'wind_deg': 247, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 8.12, 'feels_like': 8.12, 'pressure': 1018, 'humidity': 95, 'dew_point': 7.37, 'uvi': 0, 'clouds': 76, 'visibility': 2579, 'wind_speed': 0.72, 'wind_deg': 254, 'wind_gust': 0.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 7.92, 'feels_like': 7.92, 'pressure': 1017, 'humidity': 95, 'dew_point': 7.17, 'uvi': 0, 'clouds': 84, 'visibility': 9706, 'wind_speed': 0.59, 'wind_deg': 267, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1017, 'humidity': 95, 'dew_point': 6.62, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 294, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.37, 'feels_like': 7.37, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.31, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 309, 'wind_gust': 1.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 7.09, 'feels_like': 7.09, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.19, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 319, 'wind_gust': 1.36, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 6.72, 'feels_like': 6.72, 'pressure': 1018, 'humidity': 93, 'dew_point': 5.67, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 319, 'wind_gust': 1.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 7.8, 'feels_like': 7.8, 'pressure': 1019, 'humidity': 89, 'dew_point': 6.1, 'uvi': 0.42, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 300, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 9.96, 'feels_like': 9.96, 'pressure': 1019, 'humidity': 79, 'dew_point': 6.49, 'uvi': 2.52, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 276, 'wind_gust': 1.41, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 11.73, 'feels_like': 10.81, 'pressure': 1019, 'humidity': 71, 'dew_point': 6.65, 'uvi': 5.81, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 266, 'wind_gust': 1.91, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 13.28, 'feels_like': 12.33, 'pressure': 1019, 'humidity': 64, 'dew_point': 6.62, 'uvi': 9.59, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 266, 'wind_gust': 2.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 14.38, 'feels_like': 13.41, 'pressure': 1017, 'humidity': 59, 'dew_point': 6.48, 'uvi': 12.58, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 274, 'wind_gust': 3.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 15.19, 'feels_like': 14.28, 'pressure': 1016, 'humidity': 58, 'dew_point': 6.99, 'uvi': 13.45, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 248, 'wind_gust': 3.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 15.31, 'feels_like': 14.49, 'pressure': 1015, 'humidity': 61, 'dew_point': 7.84, 'uvi': 11.95, 'clouds': 97, 'visibility': 9651, 'wind_speed': 0.68, 'wind_deg': 232, 'wind_gust': 3.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 14.07, 'feels_like': 13.28, 'pressure': 1014, 'humidity': 67, 'dew_point': 8.04, 'uvi': 8.57, 'clouds': 98, 'visibility': 7513, 'wind_speed': 0.85, 'wind_deg': 247, 'wind_gust': 3.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641844800, 'temp': 13.24, 'feels_like': 12.53, 'pressure': 1013, 'humidity': 73, 'dew_point': 8.51, 'uvi': 4.8, 'clouds': 99, 'visibility': 7410, 'wind_speed': 0.77, 'wind_deg': 227, 'wind_gust': 2.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641848400, 'temp': 12.14, 'feels_like': 11.5, 'pressure': 1014, 'humidity': 80, 'dew_point': 8.8, 'uvi': 1.85, 'clouds': 98, 'visibility': 5948, 'wind_speed': 1.03, 'wind_deg': 229, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641852000, 'temp': 10.99, 'feels_like': 10.47, 'pressure': 1015, 'humidity': 89, 'dew_point': 9.25, 'uvi': 0.34, 'clouds': 95, 'visibility': 2188, 'wind_speed': 0.86, 'wind_deg': 208, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641855600, 'temp': 9.7, 'feels_like': 9.7, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.94, 'uvi': 0, 'clouds': 95, 'visibility': 3229, 'wind_speed': 0.82, 'wind_deg': 195, 'wind_gust': 1.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 00:00:00 | 95.000000 | 9.090000 | 9.850000 | 95.000000 | 1017.000000 |  | 9.850000 | 0.000000 | 2914.000000 | 205.000000 | 1.12 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 9.140000 | 9.750000 | 96.000000 | 1018.000000 |  | 9.750000 | 0.000000 | 2798.000000 | 240.000000 | 1 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 02:00:00 | 96.000000 | 9.000000 | 9.610000 | 96.000000 | 1019.000000 | 0.1 | 9.610000 | 0.000000 | 2797.000000 | 221.000000 | 1.06 | 0.340000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 03:00:00 | 93.000000 | 8.510000 | 8.960000 | 97.000000 | 1019.000000 |  | 8.960000 | 0.000000 | 2816.000000 | 231.000000 | 0.9 | 0.310000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 7.760000 | 8.360000 | 96.000000 | 1019.000000 |  | 8.360000 | 0.000000 | 7620.000000 | 252.000000 | 0.8 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 7.540000 | 8.140000 | 96.000000 | 1019.000000 |  | 8.140000 | 0.000000 | 5704.000000 | 247.000000 | 1.15 | 0.810000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 06:00:00 | 76.000000 | 7.370000 | 8.120000 | 95.000000 | 1018.000000 |  | 8.120000 | 0.000000 | 2579.000000 | 254.000000 | 0.99 | 0.720000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 07:00:00 | 84.000000 | 7.170000 | 7.920000 | 95.000000 | 1017.000000 |  | 7.920000 | 0.000000 | 9706.000000 | 267.000000 | 1.02 | 0.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 08:00:00 | 78.000000 | 6.620000 | 7.370000 | 95.000000 | 1017.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 294.000000 | 1.08 | 0.920000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 09:00:00 | 77.000000 | 6.310000 | 7.370000 | 93.000000 | 1017.000000 |  | 7.370000 | 0.000000 | 10000.000000 | 309.000000 | 1.26 | 0.980000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 10:00:00 | 80.000000 | 6.190000 | 7.090000 | 94.000000 | 1018.000000 |  | 7.090000 | 0.000000 | 10000.000000 | 319.000000 | 1.36 | 1.010000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 11:00:00 | 77.000000 | 5.670000 | 6.720000 | 93.000000 | 1018.000000 |  | 6.720000 | 0.000000 | 10000.000000 | 319.000000 | 1.24 | 0.870000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 12:00:00 | 49.000000 | 6.100000 | 7.800000 | 89.000000 | 1019.000000 |  | 7.800000 | 0.420000 | 10000.000000 | 300.000000 | 1.11 | 0.650000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 13:00:00 | 64.000000 | 6.490000 | 9.960000 | 79.000000 | 1019.000000 |  | 9.960000 | 2.520000 | 10000.000000 | 276.000000 | 1.41 | 0.530000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 14:00:00 | 61.000000 | 6.650000 | 10.810000 | 71.000000 | 1019.000000 |  | 11.730000 | 5.810000 | 10000.000000 | 266.000000 | 1.91 | 0.650000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 6.620000 | 12.330000 | 64.000000 | 1019.000000 |  | 13.280000 | 9.590000 | 10000.000000 | 266.000000 | 2.62 | 0.480000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 16:00:00 | 64.000000 | 6.480000 | 13.410000 | 59.000000 | 1017.000000 |  | 14.380000 | 12.580000 | 10000.000000 | 274.000000 | 3.45 | 0.520000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 17:00:00 | 60.000000 | 6.990000 | 14.280000 | 58.000000 | 1016.000000 |  | 15.190000 | 13.450000 | 10000.000000 | 248.000000 | 3.54 | 0.520000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 18:00:00 | 97.000000 | 7.840000 | 14.490000 | 61.000000 | 1015.000000 |  | 15.310000 | 11.950000 | 9651.000000 | 232.000000 | 3.54 | 0.680000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 8.040000 | 13.280000 | 67.000000 | 1014.000000 | 0.11 | 14.070000 | 8.570000 | 7513.000000 | 247.000000 | 3.19 | 0.850000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 8.510000 | 12.530000 | 73.000000 | 1013.000000 | 0.1 | 13.240000 | 4.800000 | 7410.000000 | 227.000000 | 2.66 | 0.770000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 8.800000 | 11.500000 | 80.000000 | 1014.000000 | 0.16 | 12.140000 | 1.850000 | 5948.000000 | 229.000000 | 2.71 | 1.030000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 9.250000 | 10.470000 | 89.000000 | 1015.000000 | 0.14 | 10.990000 | 0.340000 | 2188.000000 | 208.000000 | 2.32 | 0.860000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095120 | "AQUITANIA - AUT [35095120]" | 5.556639 | -72.881750 | 321.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-12-06 00:00:00 | NaT | Boyacá | Aquitania | Tocaria | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Lago de Tota | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 8.940000 | 9.700000 | 95.000000 | 1016.000000 |  | 9.700000 | 0.000000 | 3229.000000 | 195.000000 | 1.65 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35095120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35095120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35095120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095120_OWM_Windspeed_20220111.png)
