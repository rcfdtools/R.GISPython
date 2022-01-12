
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - RAGONVALIA [16015100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16015100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.57666667,-72.48388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.57666667&lon=-72.48388889)


| Parameter | Value |
|---|---|
| Code | 16015100 |
| Name | RAGONVALIA [16015100] |
| Latitude, ° | 7.57666667 |
| Longitude, ° | -72.48388889 |
| Elevation, m | 1550 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 2000-07-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Ragonvalia |
| Stream | Leon |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Pamplonita |

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

### (CNE index 3334) Open Weather values for station 16015100 - RAGONVALIA [16015100]

JSON data from API OWM:

```
{'lat': 7.5767, 'lon': -72.4839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812756, 'sunset': 1641854916, 'temp': 20.63, 'feels_like': 20.29, 'pressure': 1013, 'humidity': 59, 'dew_point': 12.34, 'uvi': 3.84, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 357, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.63, 'feels_like': 15.73, 'pressure': 1017, 'humidity': 95, 'dew_point': 14.83, 'uvi': 0, 'clouds': 71, 'visibility': 6427, 'wind_speed': 0.63, 'wind_deg': 310, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641776400, 'temp': 15.63, 'feels_like': 15.76, 'pressure': 1018, 'humidity': 96, 'dew_point': 14.99, 'uvi': 0, 'clouds': 78, 'visibility': 7957, 'wind_speed': 0.48, 'wind_deg': 273, 'wind_gust': 2.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 14.63, 'feels_like': 14.66, 'pressure': 1019, 'humidity': 96, 'dew_point': 14, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 247, 'wind_gust': 2.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 13.63, 'feels_like': 13.5, 'pressure': 1019, 'humidity': 94, 'dew_point': 12.68, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 224, 'wind_gust': 2.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 12.63, 'feels_like': 12.4, 'pressure': 1019, 'humidity': 94, 'dew_point': 11.69, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 212, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 12.63, 'feels_like': 12.35, 'pressure': 1019, 'humidity': 92, 'dew_point': 11.37, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 195, 'wind_gust': 1.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 12.63, 'feels_like': 12.32, 'pressure': 1018, 'humidity': 91, 'dew_point': 11.2, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 190, 'wind_gust': 1.79, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 11.61, 'feels_like': 11.18, 'pressure': 1017, 'humidity': 90, 'dew_point': 10.03, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 186, 'wind_gust': 2.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 11.49, 'feels_like': 10.99, 'pressure': 1017, 'humidity': 88, 'dew_point': 9.57, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 179, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.41, 'feels_like': 10.9, 'pressure': 1017, 'humidity': 88, 'dew_point': 9.5, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 175, 'wind_gust': 1.77, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 10.63, 'feels_like': 10.05, 'pressure': 1017, 'humidity': 88, 'dew_point': 8.73, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 172, 'wind_gust': 1.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 9.63, 'feels_like': 9.06, 'pressure': 1018, 'humidity': 88, 'dew_point': 7.74, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 169, 'wind_gust': 1.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 9.63, 'feels_like': 9.63, 'pressure': 1018, 'humidity': 84, 'dew_point': 7.06, 'uvi': 0.52, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 164, 'wind_gust': 1.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 13.63, 'feels_like': 12.95, 'pressure': 1019, 'humidity': 73, 'dew_point': 8.89, 'uvi': 2.11, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 99, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 16.63, 'feels_like': 16.1, 'pressure': 1019, 'humidity': 67, 'dew_point': 10.48, 'uvi': 4.88, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 43, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.63, 'feels_like': 17.04, 'pressure': 1018, 'humidity': 61, 'dew_point': 10.03, 'uvi': 8.05, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 24, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 19.63, 'feels_like': 19.16, 'pressure': 1017, 'humidity': 58, 'dew_point': 11.15, 'uvi': 10.48, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 17, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.63, 'feels_like': 19.22, 'pressure': 1017, 'humidity': 60, 'dew_point': 11.66, 'uvi': 11.16, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.77, 'wind_deg': 27, 'wind_gust': 1.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 20.63, 'feels_like': 20.32, 'pressure': 1016, 'humidity': 60, 'dew_point': 12.6, 'uvi': 9.84, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 33, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 21.63, 'feels_like': 21.36, 'pressure': 1014, 'humidity': 58, 'dew_point': 13.02, 'uvi': 7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 14, 'wind_gust': 1.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 20.63, 'feels_like': 20.29, 'pressure': 1013, 'humidity': 59, 'dew_point': 12.34, 'uvi': 3.84, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 357, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 19.63, 'feels_like': 19.35, 'pressure': 1013, 'humidity': 65, 'dew_point': 12.88, 'uvi': 1.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 356, 'wind_gust': 2.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 18.63, 'feels_like': 18.48, 'pressure': 1014, 'humidity': 74, 'dew_point': 13.91, 'uvi': 0.25, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 1, 'wind_gust': 3.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 18.63, 'feels_like': 18.77, 'pressure': 1015, 'humidity': 85, 'dew_point': 16.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 335, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 00:00:00 | 71.000000 | 14.830000 | 15.730000 | 95.000000 | 1017.000000 | 0.14 | 15.630000 | 0.000000 | 6427.000000 | 310.000000 | 2.18 | 0.630000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 01:00:00 | 78.000000 | 14.990000 | 15.760000 | 96.000000 | 1018.000000 | 0.12 | 15.630000 | 0.000000 | 7957.000000 | 273.000000 | 2.44 | 0.480000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 02:00:00 | 88.000000 | 14.000000 | 14.660000 | 96.000000 | 1019.000000 |  | 14.630000 | 0.000000 | 10000.000000 | 247.000000 | 2.17 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 03:00:00 | 81.000000 | 12.680000 | 13.500000 | 94.000000 | 1019.000000 |  | 13.630000 | 0.000000 | 10000.000000 | 224.000000 | 2.02 | 0.830000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 04:00:00 | 77.000000 | 11.690000 | 12.400000 | 94.000000 | 1019.000000 |  | 12.630000 | 0.000000 | 10000.000000 | 212.000000 | 2.06 | 1.050000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 05:00:00 | 75.000000 | 11.370000 | 12.350000 | 92.000000 | 1019.000000 |  | 12.630000 | 0.000000 | 10000.000000 | 195.000000 | 1.82 | 1.330000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 06:00:00 | 49.000000 | 11.200000 | 12.320000 | 91.000000 | 1018.000000 |  | 12.630000 | 0.000000 | 10000.000000 | 190.000000 | 1.79 | 1.590000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 07:00:00 | 59.000000 | 10.030000 | 11.180000 | 90.000000 | 1017.000000 |  | 11.610000 | 0.000000 | 10000.000000 | 186.000000 | 2.13 | 1.730000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 08:00:00 | 51.000000 | 9.570000 | 10.990000 | 88.000000 | 1017.000000 |  | 11.490000 | 0.000000 | 10000.000000 | 179.000000 | 1.98 | 1.640000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 09:00:00 | 47.000000 | 9.500000 | 10.900000 | 88.000000 | 1017.000000 |  | 11.410000 | 0.000000 | 10000.000000 | 175.000000 | 1.77 | 1.730000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 10:00:00 | 42.000000 | 8.730000 | 10.050000 | 88.000000 | 1017.000000 |  | 10.630000 | 0.000000 | 10000.000000 | 172.000000 | 1.55 | 1.690000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 11:00:00 | 49.000000 | 7.740000 | 9.060000 | 88.000000 | 1018.000000 |  | 9.630000 | 0.000000 | 10000.000000 | 169.000000 | 1.55 | 1.670000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 12:00:00 | 59.000000 | 7.060000 | 9.630000 | 84.000000 | 1018.000000 |  | 9.630000 | 0.520000 | 10000.000000 | 164.000000 | 1.97 | 1.310000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 13:00:00 | 77.000000 | 8.890000 | 12.950000 | 73.000000 | 1019.000000 |  | 13.630000 | 2.110000 | 10000.000000 | 99.000000 | 1.39 | 0.500000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 14:00:00 | 86.000000 | 10.480000 | 16.100000 | 67.000000 | 1019.000000 |  | 16.630000 | 4.880000 | 10000.000000 | 43.000000 | 1.51 | 0.780000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 15:00:00 | 90.000000 | 10.030000 | 17.040000 | 61.000000 | 1018.000000 |  | 17.630000 | 8.050000 | 10000.000000 | 24.000000 | 1.56 | 1.190000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 11.150000 | 19.160000 | 58.000000 | 1017.000000 |  | 19.630000 | 10.480000 | 10000.000000 | 17.000000 | 1.7 | 1.800000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 11.660000 | 19.220000 | 60.000000 | 1017.000000 |  | 19.630000 | 11.160000 | 10000.000000 | 27.000000 | 1.81 | 1.770000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 18:00:00 | 97.000000 | 12.600000 | 20.320000 | 60.000000 | 1016.000000 |  | 20.630000 | 9.840000 | 10000.000000 | 33.000000 | 1.67 | 1.430000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.020000 | 21.360000 | 58.000000 | 1014.000000 |  | 21.630000 | 7.000000 | 10000.000000 | 14.000000 | 1.57 | 1.480000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 12.340000 | 20.290000 | 59.000000 | 1013.000000 |  | 20.630000 | 3.840000 | 10000.000000 | 357.000000 | 1.74 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 12.880000 | 19.350000 | 65.000000 | 1013.000000 |  | 19.630000 | 1.430000 | 10000.000000 | 356.000000 | 2.34 | 1.840000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 13.910000 | 18.480000 | 74.000000 | 1014.000000 |  | 18.630000 | 0.250000 | 10000.000000 | 1.000000 | 3.18 | 1.680000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015100 | "RAGONVALIA [16015100]" | 7.576667 | -72.483889 | 1550.000000 | Climática Principal | Convencional | Activa | 2000-07-15 00:00:00 | NaT | Norte de Santander | Ragonvalia | Leon | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 16.060000 | 18.770000 | 85.000000 | 1015.000000 |  | 18.630000 | 0.000000 | 10000.000000 | 335.000000 | 2.1 | 0.880000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16015100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16015100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16015100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015100_OWM_Windspeed_20220111.png)
