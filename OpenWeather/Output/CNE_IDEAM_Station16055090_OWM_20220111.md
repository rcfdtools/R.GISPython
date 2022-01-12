
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - INSTITUCION AGRICOLA CONVENCION [16055090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16055090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.47055556,-73.34388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.47055556&lon=-73.34388889)


| Parameter | Value |
|---|---|
| Code | 16055090 |
| Name | INSTITUCION AGRICOLA CONVENCION [16055090] |
| Latitude, ° | 8.47055556 |
| Longitude, ° | -73.34388889 |
| Elevation, m | 176 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1990-08-14 19:00:00 |
| Suspension date | 2019-08-20 10:38:32 |
| State | Norte de Santander |
| County | Convención |
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

### (CNE index 3568) Open Weather values for station 16055090 - INSTITUCION AGRICOLA CONVENCION [16055090]

JSON data from API OWM:

```
{'lat': 8.4706, 'lon': -73.3439, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813050, 'sunset': 1641855034, 'temp': 26.32, 'feels_like': 26.32, 'pressure': 1010, 'humidity': 42, 'dew_point': 12.39, 'uvi': 3.96, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 52, 'wind_gust': 1.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 17.21, 'feels_like': 17.05, 'pressure': 1015, 'humidity': 79, 'dew_point': 13.54, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 95, 'wind_gust': 2.44, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 16.61, 'feels_like': 16.42, 'pressure': 1016, 'humidity': 80, 'dew_point': 13.15, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 103, 'wind_gust': 2.44, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 16.09, 'feels_like': 15.9, 'pressure': 1016, 'humidity': 82, 'dew_point': 13.02, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.93, 'wind_deg': 102, 'wind_gust': 2.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 15.57, 'feels_like': 15.35, 'pressure': 1016, 'humidity': 83, 'dew_point': 12.7, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 105, 'wind_gust': 2.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 15.17, 'feels_like': 14.96, 'pressure': 1016, 'humidity': 85, 'dew_point': 12.67, 'uvi': 0, 'clouds': 27, 'visibility': 10000, 'wind_speed': 1.89, 'wind_deg': 95, 'wind_gust': 2.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 14.77, 'feels_like': 14.63, 'pressure': 1016, 'humidity': 89, 'dew_point': 12.98, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 2, 'wind_deg': 87, 'wind_gust': 2.5, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 14.57, 'feels_like': 14.48, 'pressure': 1015, 'humidity': 92, 'dew_point': 13.29, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 100, 'wind_gust': 2.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.92, 'feels_like': 14.87, 'pressure': 1015, 'humidity': 92, 'dew_point': 13.63, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 95, 'wind_gust': 2.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 15.14, 'feels_like': 15.09, 'pressure': 1014, 'humidity': 91, 'dew_point': 13.68, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 90, 'wind_gust': 2.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 14.63, 'feels_like': 14.6, 'pressure': 1014, 'humidity': 94, 'dew_point': 13.68, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 96, 'wind_gust': 2.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 14.47, 'feels_like': 14.4, 'pressure': 1015, 'humidity': 93, 'dew_point': 13.35, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 100, 'wind_gust': 2.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 14.22, 'feels_like': 14.13, 'pressure': 1015, 'humidity': 93, 'dew_point': 13.11, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 100, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 15.47, 'feels_like': 15.37, 'pressure': 1016, 'humidity': 88, 'dew_point': 13.49, 'uvi': 0.45, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 97, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 19.03, 'feels_like': 18.84, 'pressure': 1017, 'humidity': 71, 'dew_point': 13.66, 'uvi': 1.93, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 86, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 21.6, 'feels_like': 21.36, 'pressure': 1017, 'humidity': 59, 'dew_point': 13.25, 'uvi': 4.66, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 77, 'wind_gust': 2.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 23.68, 'feels_like': 23.46, 'pressure': 1016, 'humidity': 52, 'dew_point': 13.25, 'uvi': 7.83, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 62, 'wind_gust': 1.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 25.2, 'feels_like': 24.98, 'pressure': 1015, 'humidity': 46, 'dew_point': 12.77, 'uvi': 10.36, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 48, 'wind_gust': 1.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 26.19, 'feels_like': 26.19, 'pressure': 1014, 'humidity': 43, 'dew_point': 12.64, 'uvi': 11.18, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 46, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 26.71, 'feels_like': 26.7, 'pressure': 1012, 'humidity': 41, 'dew_point': 12.38, 'uvi': 9.98, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 46, 'wind_gust': 1.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 26.74, 'feels_like': 26.72, 'pressure': 1011, 'humidity': 41, 'dew_point': 12.4, 'uvi': 7.09, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 48, 'wind_gust': 1.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 26.32, 'feels_like': 26.32, 'pressure': 1010, 'humidity': 42, 'dew_point': 12.39, 'uvi': 3.96, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 52, 'wind_gust': 1.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 25.05, 'feels_like': 24.84, 'pressure': 1010, 'humidity': 47, 'dew_point': 12.96, 'uvi': 1.52, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 56, 'wind_gust': 2.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 22.68, 'feels_like': 22.54, 'pressure': 1011, 'humidity': 59, 'dew_point': 14.26, 'uvi': 0.15, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 60, 'wind_gust': 2.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 20.38, 'feels_like': 20.28, 'pressure': 1013, 'humidity': 69, 'dew_point': 14.51, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 64, 'wind_gust': 1.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 00:00:00 | 38.000000 | 13.540000 | 17.050000 | 79.000000 | 1015.000000 |  | 17.210000 | 0.000000 | 10000.000000 | 95.000000 | 2.44 | 1.820000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 01:00:00 | 39.000000 | 13.150000 | 16.420000 | 80.000000 | 1016.000000 |  | 16.610000 | 0.000000 | 10000.000000 | 103.000000 | 2.44 | 1.790000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 02:00:00 | 40.000000 | 13.020000 | 15.900000 | 82.000000 | 1016.000000 |  | 16.090000 | 0.000000 | 10000.000000 | 102.000000 | 2.55 | 1.930000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 03:00:00 | 35.000000 | 12.700000 | 15.350000 | 83.000000 | 1016.000000 |  | 15.570000 | 0.000000 | 10000.000000 | 105.000000 | 2.57 | 1.840000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 04:00:00 | 27.000000 | 12.670000 | 14.960000 | 85.000000 | 1016.000000 |  | 15.170000 | 0.000000 | 10000.000000 | 95.000000 | 2.24 | 1.890000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 05:00:00 | 23.000000 | 12.980000 | 14.630000 | 89.000000 | 1016.000000 |  | 14.770000 | 0.000000 | 10000.000000 | 87.000000 | 2.5 | 2.000000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 06:00:00 | 94.000000 | 13.290000 | 14.480000 | 92.000000 | 1015.000000 |  | 14.570000 | 0.000000 | 10000.000000 | 100.000000 | 2.2 | 1.720000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 13.630000 | 14.870000 | 92.000000 | 1015.000000 |  | 14.920000 | 0.000000 | 10000.000000 | 95.000000 | 2.21 | 1.610000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 13.680000 | 15.090000 | 91.000000 | 1014.000000 |  | 15.140000 | 0.000000 | 10000.000000 | 90.000000 | 2.52 | 1.720000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 09:00:00 | 86.000000 | 13.680000 | 14.600000 | 94.000000 | 1014.000000 |  | 14.630000 | 0.000000 | 10000.000000 | 96.000000 | 2.01 | 1.590000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 10:00:00 | 74.000000 | 13.350000 | 14.400000 | 93.000000 | 1015.000000 |  | 14.470000 | 0.000000 | 10000.000000 | 100.000000 | 2.01 | 1.540000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 11:00:00 | 65.000000 | 13.110000 | 14.130000 | 93.000000 | 1015.000000 |  | 14.220000 | 0.000000 | 10000.000000 | 100.000000 | 1.79 | 1.360000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 12:00:00 | 71.000000 | 13.490000 | 15.370000 | 88.000000 | 1016.000000 |  | 15.470000 | 0.450000 | 10000.000000 | 97.000000 | 2.06 | 1.320000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 13.660000 | 18.840000 | 71.000000 | 1017.000000 |  | 19.030000 | 1.930000 | 10000.000000 | 86.000000 | 2.3 | 1.420000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 14:00:00 | 61.000000 | 13.250000 | 21.360000 | 59.000000 | 1017.000000 |  | 21.600000 | 4.660000 | 10000.000000 | 77.000000 | 2.13 | 1.430000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 15:00:00 | 57.000000 | 13.250000 | 23.460000 | 52.000000 | 1016.000000 |  | 23.680000 | 7.830000 | 10000.000000 | 62.000000 | 1.87 | 1.280000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 16:00:00 | 57.000000 | 12.770000 | 24.980000 | 46.000000 | 1015.000000 |  | 25.200000 | 10.360000 | 10000.000000 | 48.000000 | 1.71 | 1.300000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 12.640000 | 26.190000 | 43.000000 | 1014.000000 |  | 26.190000 | 11.180000 | 10000.000000 | 46.000000 | 1.61 | 1.450000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 18:00:00 | 61.000000 | 12.380000 | 26.700000 | 41.000000 | 1012.000000 |  | 26.710000 | 9.980000 | 10000.000000 | 46.000000 | 1.52 | 1.720000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 19:00:00 | 68.000000 | 12.400000 | 26.720000 | 41.000000 | 1011.000000 |  | 26.740000 | 7.090000 | 10000.000000 | 48.000000 | 1.84 | 1.810000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 20:00:00 | 69.000000 | 12.390000 | 26.320000 | 42.000000 | 1010.000000 |  | 26.320000 | 3.960000 | 10000.000000 | 52.000000 | 1.85 | 1.680000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 21:00:00 | 72.000000 | 12.960000 | 24.840000 | 47.000000 | 1010.000000 |  | 25.050000 | 1.520000 | 10000.000000 | 56.000000 | 2.25 | 1.680000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 22:00:00 | 76.000000 | 14.260000 | 22.540000 | 59.000000 | 1011.000000 |  | 22.680000 | 0.150000 | 10000.000000 | 60.000000 | 2.99 | 1.640000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055090 | "INSTITUCION AGRICOLA CONVENCION [16055090]" | 8.470556 | -73.343889 | 176.000000 | Climática Principal | Convencional | Suspendida | 1990-08-14 19:00:00 | 2019-08-20 10:38:32 | Norte de Santander | Convención | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 23:00:00 | 81.000000 | 14.510000 | 20.280000 | 69.000000 | 1013.000000 |  | 20.380000 | 0.000000 | 10000.000000 | 64.000000 | 1.58 | 1.400000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16055090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16055090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16055090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055090_OWM_Windspeed_20220111.png)
