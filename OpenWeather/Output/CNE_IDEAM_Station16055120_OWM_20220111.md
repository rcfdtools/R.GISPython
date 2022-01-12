
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AGUAS DE LA VIRGEN  - AUT [16055120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16055120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.22769444,-73.3975) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.22769444&lon=-73.3975)


| Parameter | Value |
|---|---|
| Code | 16055120 |
| Name | AGUAS DE LA VIRGEN  - AUT [16055120] |
| Latitude, ° | 8.22769444 |
| Longitude, ° | -73.3975 |
| Elevation, m | 1700 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-08-08 19:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Ocaña |
| Stream | 0 |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Algodonal (Alto Catatumbo) |

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

### (CNE index 331) Open Weather values for station 16055120 - AGUAS DE LA VIRGEN  - AUT [16055120]

JSON data from API OWM:

```
{'lat': 8.2277, 'lon': -73.3975, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813039, 'sunset': 1641855071, 'temp': 23.01, 'feels_like': 22.46, 'pressure': 1010, 'humidity': 42, 'dew_point': 9.42, 'uvi': 3.96, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 306, 'wind_gust': 2.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 15.25, 'feels_like': 14.68, 'pressure': 1013, 'humidity': 71, 'dew_point': 10.03, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 3.3, 'wind_deg': 68, 'wind_gust': 4.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 14.51, 'feels_like': 13.92, 'pressure': 1014, 'humidity': 73, 'dew_point': 9.73, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 3.12, 'wind_deg': 69, 'wind_gust': 4.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 13.93, 'feels_like': 13.31, 'pressure': 1015, 'humidity': 74, 'dew_point': 9.38, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 70, 'wind_gust': 3.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 13.43, 'feels_like': 12.76, 'pressure': 1015, 'humidity': 74, 'dew_point': 8.89, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 3.12, 'wind_deg': 71, 'wind_gust': 3.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 13.04, 'feels_like': 12.31, 'pressure': 1015, 'humidity': 73, 'dew_point': 8.32, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 3.06, 'wind_deg': 75, 'wind_gust': 3.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 12.73, 'feels_like': 11.96, 'pressure': 1014, 'humidity': 73, 'dew_point': 8.02, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 3.06, 'wind_deg': 73, 'wind_gust': 3.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 12.3, 'feels_like': 11.54, 'pressure': 1014, 'humidity': 75, 'dew_point': 8, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 70, 'wind_gust': 3.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 11.93, 'feels_like': 11.19, 'pressure': 1014, 'humidity': 77, 'dew_point': 8.03, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 70, 'wind_gust': 2.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 11.64, 'feels_like': 10.95, 'pressure': 1013, 'humidity': 80, 'dew_point': 8.31, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 70, 'wind_gust': 2.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.49, 'feels_like': 10.84, 'pressure': 1013, 'humidity': 82, 'dew_point': 8.53, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.62, 'wind_deg': 70, 'wind_gust': 2.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 11.61, 'feels_like': 10.94, 'pressure': 1014, 'humidity': 81, 'dew_point': 8.46, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 70, 'wind_gust': 2.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 11.52, 'feels_like': 10.82, 'pressure': 1014, 'humidity': 80, 'dew_point': 8.19, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 71, 'wind_gust': 2.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 12.81, 'feels_like': 12.13, 'pressure': 1015, 'humidity': 76, 'dew_point': 8.69, 'uvi': 0.45, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 72, 'wind_gust': 2.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 16.24, 'feels_like': 15.54, 'pressure': 1016, 'humidity': 62, 'dew_point': 8.96, 'uvi': 1.93, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 75, 'wind_gust': 2.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 18.84, 'feels_like': 18.16, 'pressure': 1016, 'humidity': 53, 'dew_point': 9.07, 'uvi': 4.66, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 90, 'wind_gust': 1.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 20.55, 'feels_like': 19.86, 'pressure': 1016, 'humidity': 46, 'dew_point': 8.54, 'uvi': 7.83, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 269, 'wind_gust': 1.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 21.84, 'feels_like': 21.2, 'pressure': 1015, 'humidity': 43, 'dew_point': 8.72, 'uvi': 10.36, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 271, 'wind_gust': 2.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 22.72, 'feels_like': 22.12, 'pressure': 1013, 'humidity': 41, 'dew_point': 8.8, 'uvi': 11.18, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 272, 'wind_gust': 2.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 23.36, 'feels_like': 22.8, 'pressure': 1012, 'humidity': 40, 'dew_point': 9.01, 'uvi': 9.98, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 282, 'wind_gust': 2.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 23.54, 'feels_like': 23.02, 'pressure': 1010, 'humidity': 41, 'dew_point': 9.54, 'uvi': 7.09, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 291, 'wind_gust': 2.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 23.01, 'feels_like': 22.46, 'pressure': 1010, 'humidity': 42, 'dew_point': 9.42, 'uvi': 3.96, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 306, 'wind_gust': 2.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 21.8, 'feels_like': 21.29, 'pressure': 1010, 'humidity': 48, 'dew_point': 10.31, 'uvi': 1.52, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 3, 'wind_gust': 2.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 20.08, 'feels_like': 19.61, 'pressure': 1011, 'humidity': 56, 'dew_point': 11.04, 'uvi': 0.15, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 77, 'wind_gust': 1.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 18.08, 'feels_like': 17.54, 'pressure': 1012, 'humidity': 61, 'dew_point': 10.45, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 57, 'wind_gust': 1.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 00:00:00 | 53.000000 | 10.030000 | 14.680000 | 71.000000 | 1013.000000 |  | 15.250000 | 0.000000 | 10000.000000 | 68.000000 | 4.26 | 3.300000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 01:00:00 | 51.000000 | 9.730000 | 13.920000 | 73.000000 | 1014.000000 |  | 14.510000 | 0.000000 | 10000.000000 | 69.000000 | 4.03 | 3.120000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 02:00:00 | 60.000000 | 9.380000 | 13.310000 | 74.000000 | 1015.000000 |  | 13.930000 | 0.000000 | 10000.000000 | 70.000000 | 3.7 | 3.100000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 03:00:00 | 50.000000 | 8.890000 | 12.760000 | 74.000000 | 1015.000000 |  | 13.430000 | 0.000000 | 10000.000000 | 71.000000 | 3.69 | 3.120000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 04:00:00 | 39.000000 | 8.320000 | 12.310000 | 73.000000 | 1015.000000 |  | 13.040000 | 0.000000 | 10000.000000 | 75.000000 | 3.6 | 3.060000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 05:00:00 | 33.000000 | 8.020000 | 11.960000 | 73.000000 | 1014.000000 |  | 12.730000 | 0.000000 | 10000.000000 | 73.000000 | 3.45 | 3.060000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 8.000000 | 11.540000 | 75.000000 | 1014.000000 |  | 12.300000 | 0.000000 | 10000.000000 | 70.000000 | 3.08 | 2.840000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 07:00:00 | 90.000000 | 8.030000 | 11.190000 | 77.000000 | 1014.000000 |  | 11.930000 | 0.000000 | 10000.000000 | 70.000000 | 2.83 | 2.670000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 08:00:00 | 70.000000 | 8.310000 | 10.950000 | 80.000000 | 1013.000000 |  | 11.640000 | 0.000000 | 10000.000000 | 70.000000 | 2.99 | 2.690000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 09:00:00 | 76.000000 | 8.530000 | 10.840000 | 82.000000 | 1013.000000 |  | 11.490000 | 0.000000 | 10000.000000 | 70.000000 | 2.78 | 2.620000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 10:00:00 | 73.000000 | 8.460000 | 10.940000 | 81.000000 | 1014.000000 |  | 11.610000 | 0.000000 | 10000.000000 | 70.000000 | 2.9 | 2.530000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 11:00:00 | 78.000000 | 8.190000 | 10.820000 | 80.000000 | 1014.000000 |  | 11.520000 | 0.000000 | 10000.000000 | 71.000000 | 2.35 | 2.410000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 12:00:00 | 76.000000 | 8.690000 | 12.130000 | 76.000000 | 1015.000000 |  | 12.810000 | 0.450000 | 10000.000000 | 72.000000 | 2.74 | 2.220000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 13:00:00 | 80.000000 | 8.960000 | 15.540000 | 62.000000 | 1016.000000 |  | 16.240000 | 1.930000 | 10000.000000 | 75.000000 | 2.21 | 1.460000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 14:00:00 | 76.000000 | 9.070000 | 18.160000 | 53.000000 | 1016.000000 |  | 18.840000 | 4.660000 | 10000.000000 | 90.000000 | 1.8 | 0.550000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 15:00:00 | 80.000000 | 8.540000 | 19.860000 | 46.000000 | 1016.000000 |  | 20.550000 | 7.830000 | 10000.000000 | 269.000000 | 1.89 | 0.410000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 16:00:00 | 78.000000 | 8.720000 | 21.200000 | 43.000000 | 1015.000000 |  | 21.840000 | 10.360000 | 10000.000000 | 271.000000 | 2.15 | 0.990000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 17:00:00 | 68.000000 | 8.800000 | 22.120000 | 41.000000 | 1013.000000 |  | 22.720000 | 11.180000 | 10000.000000 | 272.000000 | 2.53 | 1.150000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 18:00:00 | 37.000000 | 9.010000 | 22.800000 | 40.000000 | 1012.000000 |  | 23.360000 | 9.980000 | 10000.000000 | 282.000000 | 2.72 | 1.060000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 19:00:00 | 53.000000 | 9.540000 | 23.020000 | 41.000000 | 1010.000000 |  | 23.540000 | 7.090000 | 10000.000000 | 291.000000 | 2.81 | 0.960000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 20:00:00 | 72.000000 | 9.420000 | 22.460000 | 42.000000 | 1010.000000 |  | 23.010000 | 3.960000 | 10000.000000 | 306.000000 | 2.69 | 0.750000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 21:00:00 | 66.000000 | 10.310000 | 21.290000 | 48.000000 | 1010.000000 |  | 21.800000 | 1.520000 | 10000.000000 | 3.000000 | 2.81 | 0.390000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 22:00:00 | 73.000000 | 11.040000 | 19.610000 | 56.000000 | 1011.000000 |  | 20.080000 | 0.150000 | 10000.000000 | 77.000000 | 1.87 | 0.790000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055120 | "AGUAS DE LA VIRGEN  - AUT [16055120]" | 8.227694 | -73.397500 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-08-08 19:00:00 | NaT | Norte de Santander | Ocaña | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 23:00:00 | 78.000000 | 10.450000 | 17.540000 | 61.000000 | 1012.000000 |  | 18.080000 | 0.000000 | 10000.000000 | 57.000000 | 1.96 | 1.730000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16055120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16055120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16055120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055120_OWM_Windspeed_20220111.png)
