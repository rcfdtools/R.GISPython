
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SAN ANTONIO QUINTA [22065040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station22065040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.90691667,-75.48808333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.90691667&lon=-75.48808333)


| Parameter | Value |
|---|---|
| Code | 22065040 |
| Name | SAN ANTONIO QUINTA [22065040] |
| Latitude, ° | 3.90691667 |
| Longitude, ° | -75.48808333 |
| Elevation, m | 1448 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1971-12-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | San Antonio |
| Stream | Guayabero |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Saldaña |
| SZH - Hydrographic subzone | Río Tetuán, Río Ortega |

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

### (CNE index 1220) Open Weather values for station 22065040 - SAN ANTONIO QUINTA [22065040]

JSON data from API OWM:

```
{'lat': 3.9069, 'lon': -75.4881, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813120, 'sunset': 1641855994, 'temp': 21.89, 'feels_like': 22.25, 'pressure': 1012, 'humidity': 81, 'dew_point': 18.48, 'uvi': 3.24, 'clouds': 80, 'visibility': 8889, 'wind_speed': 1.05, 'wind_deg': 100, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, 'hourly': [{'dt': 1641772800, 'temp': 21.89, 'feels_like': 22.59, 'pressure': 1014, 'humidity': 94, 'dew_point': 20.88, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 319, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1641776400, 'temp': 20.89, 'feels_like': 21.49, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.89, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 307, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641780000, 'temp': 19.89, 'feels_like': 20.39, 'pressure': 1016, 'humidity': 94, 'dew_point': 18.9, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 297, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.7}}, {'dt': 1641783600, 'temp': 18.89, 'feels_like': 19.32, 'pressure': 1016, 'humidity': 95, 'dew_point': 18.07, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 292, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.72}}, {'dt': 1641787200, 'temp': 18.89, 'feels_like': 19.32, 'pressure': 1016, 'humidity': 95, 'dew_point': 18.07, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 285, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.54}}, {'dt': 1641790800, 'temp': 18.89, 'feels_like': 19.32, 'pressure': 1016, 'humidity': 95, 'dew_point': 18.07, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 277, 'wind_gust': 1.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641794400, 'temp': 17.63, 'feels_like': 17.9, 'pressure': 1015, 'humidity': 94, 'dew_point': 16.65, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 275, 'wind_gust': 1.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 17.68, 'feels_like': 17.96, 'pressure': 1014, 'humidity': 94, 'dew_point': 16.7, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 273, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 17.71, 'feels_like': 17.96, 'pressure': 1014, 'humidity': 93, 'dew_point': 16.56, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 274, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 17.38, 'feels_like': 17.6, 'pressure': 1014, 'humidity': 93, 'dew_point': 16.24, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 281, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 16.77, 'feels_like': 16.93, 'pressure': 1015, 'humidity': 93, 'dew_point': 15.63, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 296, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 17.89, 'feels_like': 18.19, 'pressure': 1016, 'humidity': 94, 'dew_point': 16.91, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 305, 'wind_gust': 1.53, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 17.89, 'feels_like': 18.14, 'pressure': 1016, 'humidity': 92, 'dew_point': 16.57, 'uvi': 0.47, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 308, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 18.89, 'feels_like': 19.08, 'pressure': 1017, 'humidity': 86, 'dew_point': 16.5, 'uvi': 1.98, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 80, 'wind_gust': 0.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 20.89, 'feels_like': 21.23, 'pressure': 1017, 'humidity': 84, 'dew_point': 18.09, 'uvi': 4.86, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 99, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641826800, 'temp': 22.89, 'feels_like': 23.43, 'pressure': 1017, 'humidity': 84, 'dew_point': 20.04, 'uvi': 8.33, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 106, 'wind_gust': 1.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641830400, 'temp': 21.89, 'feels_like': 22.41, 'pressure': 1016, 'humidity': 87, 'dew_point': 19.63, 'uvi': 7.71, 'clouds': 96, 'visibility': 6282, 'wind_speed': 1.89, 'wind_deg': 110, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641834000, 'temp': 22.89, 'feels_like': 23.51, 'pressure': 1015, 'humidity': 87, 'dew_point': 20.61, 'uvi': 8.49, 'clouds': 96, 'visibility': 5999, 'wind_speed': 1.59, 'wind_deg': 105, 'wind_gust': 1.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641837600, 'temp': 22.89, 'feels_like': 23.48, 'pressure': 1014, 'humidity': 86, 'dew_point': 20.42, 'uvi': 7.8, 'clouds': 63, 'visibility': 5529, 'wind_speed': 1.22, 'wind_deg': 111, 'wind_gust': 0.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641841200, 'temp': 22.89, 'feels_like': 23.4, 'pressure': 1013, 'humidity': 83, 'dew_point': 19.85, 'uvi': 5.46, 'clouds': 79, 'visibility': 7824, 'wind_speed': 1.18, 'wind_deg': 105, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641844800, 'temp': 21.89, 'feels_like': 22.25, 'pressure': 1012, 'humidity': 81, 'dew_point': 18.48, 'uvi': 3.24, 'clouds': 80, 'visibility': 8889, 'wind_speed': 1.05, 'wind_deg': 100, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641848400, 'temp': 20.89, 'feels_like': 21.18, 'pressure': 1011, 'humidity': 82, 'dew_point': 17.7, 'uvi': 1.37, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 88, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641852000, 'temp': 18.89, 'feels_like': 19.13, 'pressure': 1012, 'humidity': 88, 'dew_point': 16.86, 'uvi': 0.37, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 86, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641855600, 'temp': 16.89, 'feels_like': 17.06, 'pressure': 1013, 'humidity': 93, 'dew_point': 15.75, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 330, 'wind_gust': 0.82, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.87}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 00:00:00 | 54.000000 | 20.880000 | 22.590000 | 94.000000 | 1014.000000 | 0.65 | 21.890000 | 0.000000 | 10000.000000 | 319.000000 | 1.24 | 1.510000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 19.890000 | 21.490000 | 94.000000 | 1015.000000 | 0.25 | 20.890000 | 0.000000 | 10000.000000 | 307.000000 | 1.08 | 1.320000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 02:00:00 | 87.000000 | 18.900000 | 20.390000 | 94.000000 | 1016.000000 | 0.7 | 19.890000 | 0.000000 | 10000.000000 | 297.000000 | 1 | 1.340000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 03:00:00 | 92.000000 | 18.070000 | 19.320000 | 95.000000 | 1016.000000 | 0.72 | 18.890000 | 0.000000 | 10000.000000 | 292.000000 | 0.93 | 1.130000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 18.070000 | 19.320000 | 95.000000 | 1016.000000 | 0.54 | 18.890000 | 0.000000 | 10000.000000 | 285.000000 | 1.17 | 1.400000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | 18.070000 | 19.320000 | 95.000000 | 1016.000000 | 0.27 | 18.890000 | 0.000000 | 10000.000000 | 277.000000 | 1.28 | 1.420000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 06:00:00 | 59.000000 | 16.650000 | 17.900000 | 94.000000 | 1015.000000 |  | 17.630000 | 0.000000 | 10000.000000 | 275.000000 | 1.15 | 1.290000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 07:00:00 | 88.000000 | 16.700000 | 17.960000 | 94.000000 | 1014.000000 |  | 17.680000 | 0.000000 | 10000.000000 | 273.000000 | 1.12 | 1.270000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 16.560000 | 17.960000 | 93.000000 | 1014.000000 |  | 17.710000 | 0.000000 | 10000.000000 | 274.000000 | 1.2 | 1.370000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 09:00:00 | 91.000000 | 16.240000 | 17.600000 | 93.000000 | 1014.000000 |  | 17.380000 | 0.000000 | 10000.000000 | 281.000000 | 1.06 | 1.240000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 15.630000 | 16.930000 | 93.000000 | 1015.000000 |  | 16.770000 | 0.000000 | 10000.000000 | 296.000000 | 1.32 | 1.650000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 11:00:00 | 89.000000 | 16.910000 | 18.190000 | 94.000000 | 1016.000000 |  | 17.890000 | 0.000000 | 10000.000000 | 305.000000 | 1.53 | 1.790000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 12:00:00 | 93.000000 | 16.570000 | 18.140000 | 92.000000 | 1016.000000 |  | 17.890000 | 0.470000 | 10000.000000 | 308.000000 | 1.15 | 1.350000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 16.500000 | 19.080000 | 86.000000 | 1017.000000 |  | 18.890000 | 1.980000 | 10000.000000 | 80.000000 | 0.6 | 0.450000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 18.090000 | 21.230000 | 84.000000 | 1017.000000 | 0.5 | 20.890000 | 4.860000 | 10000.000000 | 99.000000 | 1.26 | 1.370000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 20.040000 | 23.430000 | 84.000000 | 1017.000000 | 0.73 | 22.890000 | 8.330000 | 10000.000000 | 106.000000 | 1.62 | 1.830000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 16:00:00 | 96.000000 | 19.630000 | 22.410000 | 87.000000 | 1016.000000 | 0.92 | 21.890000 | 7.710000 | 6282.000000 | 110.000000 | 1.58 | 1.890000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 17:00:00 | 96.000000 | 20.610000 | 23.510000 | 87.000000 | 1015.000000 | 0.81 | 22.890000 | 8.490000 | 5999.000000 | 105.000000 | 1.29 | 1.590000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 18:00:00 | 63.000000 | 20.420000 | 23.480000 | 86.000000 | 1014.000000 | 0.53 | 22.890000 | 7.800000 | 5529.000000 | 111.000000 | 0.95 | 1.220000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 19:00:00 | 79.000000 | 19.850000 | 23.400000 | 83.000000 | 1013.000000 | 0.52 | 22.890000 | 5.460000 | 7824.000000 | 105.000000 | 0.89 | 1.180000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 20:00:00 | 80.000000 | 18.480000 | 22.250000 | 81.000000 | 1012.000000 | 0.61 | 21.890000 | 3.240000 | 8889.000000 | 100.000000 | 0.98 | 1.050000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 21:00:00 | 82.000000 | 17.700000 | 21.180000 | 82.000000 | 1011.000000 | 0.55 | 20.890000 | 1.370000 | 10000.000000 | 88.000000 | 1.1 | 0.930000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 22:00:00 | 83.000000 | 16.860000 | 19.130000 | 88.000000 | 1012.000000 | 0.77 | 18.890000 | 0.370000 | 10000.000000 | 86.000000 | 1.27 | 0.700000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 22065040 | "SAN ANTONIO QUINTA [22065040]" | 3.906917 | -75.488083 | 1448.000000 | Climática Principal | Convencional | Activa | 1971-12-15 00:00:00 | NaT | Tolima | San Antonio | Guayabero | Area Operativa 10 - Tolima | Magdalena Cauca | Saldaña | Río Tetuán, Río Ortega | America/Bogota | 2022-01-10 23:00:00 | 86.000000 | 15.750000 | 17.060000 | 93.000000 | 1013.000000 | 1.87 | 16.890000 | 0.000000 | 10000.000000 | 330.000000 | 0.82 | 0.830000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station22065040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station22065040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station22065040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station22065040_OWM_Windspeed_20220111.png)
