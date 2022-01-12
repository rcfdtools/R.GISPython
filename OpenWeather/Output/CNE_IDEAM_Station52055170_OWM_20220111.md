
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA JOSEFINA - AUT [52055170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=0.93030556,-77.49119444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=0.93030556&lon=-77.49119444)


| Parameter | Value |
|---|---|
| Code | 52055170 |
| Name | LA JOSEFINA - AUT [52055170] |
| Latitude, ° | 0.93030556 |
| Longitude, ° | -77.49119444 |
| Elevation, m | 2450 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-10 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Contadero |
| Stream | Guaitara |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Guáitara |

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

### (CNE index 2) Open Weather values for station 52055170 - LA JOSEFINA - AUT [52055170]

JSON data from API OWM:

```
{'lat': 0.9303, 'lon': -77.4912, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813313, 'sunset': 1641856763, 'temp': 17.43, 'feels_like': 17.29, 'pressure': 1013, 'humidity': 79, 'dew_point': 13.75, 'uvi': 5.78, 'clouds': 86, 'visibility': 7272, 'wind_speed': 2.6, 'wind_deg': 342, 'wind_gust': 2.69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, 'hourly': [{'dt': 1641772800, 'temp': 16.02, 'feels_like': 16.08, 'pressure': 1016, 'humidity': 92, 'dew_point': 14.72, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 6, 'wind_gust': 1.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 13.13, 'feels_like': 12.95, 'pressure': 1018, 'humidity': 94, 'dew_point': 12.19, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 20, 'wind_gust': 1.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.81, 'feels_like': 12.63, 'pressure': 1019, 'humidity': 95, 'dew_point': 12.03, 'uvi': 0, 'clouds': 100, 'visibility': 2094, 'wind_speed': 0.94, 'wind_deg': 20, 'wind_gust': 1.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.65, 'feels_like': 12.48, 'pressure': 1020, 'humidity': 96, 'dew_point': 12.03, 'uvi': 0, 'clouds': 100, 'visibility': 2372, 'wind_speed': 0.58, 'wind_deg': 30, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 12.53, 'feels_like': 12.35, 'pressure': 1020, 'humidity': 96, 'dew_point': 11.91, 'uvi': 0, 'clouds': 100, 'visibility': 1430, 'wind_speed': 0.11, 'wind_deg': 113, 'wind_gust': 0.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 12.49, 'feels_like': 12.28, 'pressure': 1019, 'humidity': 95, 'dew_point': 11.71, 'uvi': 0, 'clouds': 100, 'visibility': 1682, 'wind_speed': 0.48, 'wind_deg': 245, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 12.22, 'feels_like': 11.95, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.28, 'uvi': 0, 'clouds': 100, 'visibility': 1418, 'wind_speed': 0.92, 'wind_deg': 262, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 12.07, 'feels_like': 11.79, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.13, 'uvi': 0, 'clouds': 100, 'visibility': 4388, 'wind_speed': 0.68, 'wind_deg': 255, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 12.01, 'feels_like': 11.72, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.08, 'uvi': 0, 'clouds': 100, 'visibility': 6865, 'wind_speed': 0.79, 'wind_deg': 261, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.89, 'feels_like': 11.56, 'pressure': 1017, 'humidity': 93, 'dew_point': 10.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 285, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 11.42, 'feels_like': 11.05, 'pressure': 1018, 'humidity': 93, 'dew_point': 10.33, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 232, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 10.02, 'feels_like': 9.51, 'pressure': 1018, 'humidity': 93, 'dew_point': 8.94, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 263, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 11.02, 'feels_like': 10.58, 'pressure': 1019, 'humidity': 92, 'dew_point': 9.77, 'uvi': 0.45, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 213, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 12.83, 'feels_like': 12.39, 'pressure': 1019, 'humidity': 85, 'dew_point': 10.37, 'uvi': 2.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 249, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 15.43, 'feels_like': 15.01, 'pressure': 1018, 'humidity': 76, 'dew_point': 11.22, 'uvi': 5.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 15, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.83, 'feels_like': 17.47, 'pressure': 1017, 'humidity': 69, 'dew_point': 12.07, 'uvi': 9.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 8, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641830400, 'temp': 19.43, 'feels_like': 19.2, 'pressure': 1016, 'humidity': 68, 'dew_point': 13.38, 'uvi': 11.08, 'clouds': 100, 'visibility': 9656, 'wind_speed': 2.33, 'wind_deg': 1, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641834000, 'temp': 19.64, 'feels_like': 19.62, 'pressure': 1016, 'humidity': 75, 'dew_point': 15.09, 'uvi': 12.49, 'clouds': 100, 'visibility': 6908, 'wind_speed': 2.45, 'wind_deg': 360, 'wind_gust': 2.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.79}}, {'dt': 1641837600, 'temp': 20.64, 'feels_like': 20.82, 'pressure': 1015, 'humidity': 79, 'dew_point': 16.87, 'uvi': 11.78, 'clouds': 80, 'visibility': 7564, 'wind_speed': 2.03, 'wind_deg': 356, 'wind_gust': 2.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641841200, 'temp': 20.43, 'feels_like': 20.62, 'pressure': 1014, 'humidity': 80, 'dew_point': 16.87, 'uvi': 9.25, 'clouds': 100, 'visibility': 5919, 'wind_speed': 2.1, 'wind_deg': 342, 'wind_gust': 2.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.1}}, {'dt': 1641844800, 'temp': 17.43, 'feels_like': 17.29, 'pressure': 1013, 'humidity': 79, 'dew_point': 13.75, 'uvi': 5.78, 'clouds': 86, 'visibility': 7272, 'wind_speed': 2.6, 'wind_deg': 342, 'wind_gust': 2.69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641848400, 'temp': 15.83, 'feels_like': 15.61, 'pressure': 1013, 'humidity': 82, 'dew_point': 12.77, 'uvi': 2.62, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.62, 'wind_deg': 346, 'wind_gust': 2.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}, {'dt': 1641852000, 'temp': 15.24, 'feels_like': 15.09, 'pressure': 1014, 'humidity': 87, 'dew_point': 13.09, 'uvi': 0.66, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.33, 'wind_deg': 346, 'wind_gust': 2.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641855600, 'temp': 15.02, 'feels_like': 14.98, 'pressure': 1016, 'humidity': 92, 'dew_point': 13.73, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 340, 'wind_gust': 2.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 14.720000 | 16.080000 | 92.000000 | 1016.000000 |  | 16.020000 | 0.000000 | 10000.000000 | 6.000000 | 1.8 | 1.540000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 12.190000 | 12.950000 | 94.000000 | 1018.000000 |  | 13.130000 | 0.000000 | 10000.000000 | 20.000000 | 1.54 | 1.250000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 12.030000 | 12.630000 | 95.000000 | 1019.000000 |  | 12.810000 | 0.000000 | 2094.000000 | 20.000000 | 1.24 | 0.940000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 12.030000 | 12.480000 | 96.000000 | 1020.000000 |  | 12.650000 | 0.000000 | 2372.000000 | 30.000000 | 0.95 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 11.910000 | 12.350000 | 96.000000 | 1020.000000 |  | 12.530000 | 0.000000 | 1430.000000 | 113.000000 | 0.4 | 0.110000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 11.710000 | 12.280000 | 95.000000 | 1019.000000 |  | 12.490000 | 0.000000 | 1682.000000 | 245.000000 | 0.54 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 11.280000 | 11.950000 | 94.000000 | 1018.000000 |  | 12.220000 | 0.000000 | 1418.000000 | 262.000000 | 0.97 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 11.130000 | 11.790000 | 94.000000 | 1018.000000 |  | 12.070000 | 0.000000 | 4388.000000 | 255.000000 | 0.82 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 11.080000 | 11.720000 | 94.000000 | 1017.000000 |  | 12.010000 | 0.000000 | 6865.000000 | 261.000000 | 0.97 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 10.800000 | 11.560000 | 93.000000 | 1017.000000 |  | 11.890000 | 0.000000 | 10000.000000 | 285.000000 | 1.33 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 10.330000 | 11.050000 | 93.000000 | 1018.000000 |  | 11.420000 | 0.000000 | 10000.000000 | 232.000000 | 0.86 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 8.940000 | 9.510000 | 93.000000 | 1018.000000 |  | 10.020000 | 0.000000 | 10000.000000 | 263.000000 | 0.97 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 9.770000 | 10.580000 | 92.000000 | 1019.000000 |  | 11.020000 | 0.450000 | 10000.000000 | 213.000000 | 1.17 | 0.840000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 10.370000 | 12.390000 | 85.000000 | 1019.000000 |  | 12.830000 | 2.070000 | 10000.000000 | 249.000000 | 0.74 | 0.540000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 11.220000 | 15.010000 | 76.000000 | 1018.000000 |  | 15.430000 | 5.270000 | 10000.000000 | 15.000000 | 0.8 | 0.560000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 12.070000 | 17.470000 | 69.000000 | 1017.000000 | 0.13 | 17.830000 | 9.260000 | 10000.000000 | 8.000000 | 1.61 | 1.610000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 13.380000 | 19.200000 | 68.000000 | 1016.000000 | 0.46 | 19.430000 | 11.080000 | 9656.000000 | 1.000000 | 2.19 | 2.330000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 15.090000 | 19.620000 | 75.000000 | 1016.000000 | 0.79 | 19.640000 | 12.490000 | 6908.000000 | 360.000000 | 2.47 | 2.450000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 18:00:00 | 80.000000 | 16.870000 | 20.820000 | 79.000000 | 1015.000000 | 0.92 | 20.640000 | 11.780000 | 7564.000000 | 356.000000 | 2.28 | 2.030000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 16.870000 | 20.620000 | 80.000000 | 1014.000000 | 1.1 | 20.430000 | 9.250000 | 5919.000000 | 342.000000 | 2.34 | 2.100000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 20:00:00 | 86.000000 | 13.750000 | 17.290000 | 79.000000 | 1013.000000 | 1.01 | 17.430000 | 5.780000 | 7272.000000 | 342.000000 | 2.69 | 2.600000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 12.770000 | 15.610000 | 82.000000 | 1013.000000 | 0.83 | 15.830000 | 2.620000 | 10000.000000 | 346.000000 | 2.74 | 2.620000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 22:00:00 | 93.000000 | 13.090000 | 15.090000 | 87.000000 | 1014.000000 | 0.53 | 15.240000 | 0.660000 | 10000.000000 | 346.000000 | 2.71 | 2.330000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055170 | "LA JOSEFINA - AUT [52055170]" | 0.930306 | -77.491194 | 2450.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-10 00:00:00 | NaT | Nariño | Contadero | Guaitara | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guáitara | America/Bogota | 2022-01-10 23:00:00 | 94.000000 | 13.730000 | 14.980000 | 92.000000 | 1016.000000 | 0.29 | 15.020000 | 0.000000 | 10000.000000 | 340.000000 | 2.41 | 1.930000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055170_OWM_Windspeed_20220111.png)
