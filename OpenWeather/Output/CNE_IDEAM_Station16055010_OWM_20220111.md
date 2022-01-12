
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO AGUAS CLARAS [16055010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16055010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.31527778,-73.3575) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.31527778&lon=-73.3575)


| Parameter | Value |
|---|---|
| Code | 16055010 |
| Name | AEROPUERTO AGUAS CLARAS [16055010] |
| Latitude, ° | 8.31527778 |
| Longitude, ° | -73.3575 |
| Elevation, m | 1435 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1973-03-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Ocaña |
| Stream | San Jorge |
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

### (CNE index 3376) Open Weather values for station 16055010 - AEROPUERTO AGUAS CLARAS [16055010]

JSON data from API OWM:

```
{'lat': 8.3153, 'lon': -73.3575, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813038, 'sunset': 1641855053, 'temp': 25.83, 'feels_like': 25.62, 'pressure': 1010, 'humidity': 44, 'dew_point': 12.66, 'uvi': 3.96, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 22, 'wind_gust': 2.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 17.48, 'feels_like': 17.27, 'pressure': 1014, 'humidity': 76, 'dew_point': 13.21, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 2.77, 'wind_deg': 75, 'wind_gust': 3.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 16.8, 'feels_like': 16.57, 'pressure': 1015, 'humidity': 78, 'dew_point': 12.95, 'uvi': 0, 'clouds': 53, 'visibility': 10000, 'wind_speed': 2.64, 'wind_deg': 79, 'wind_gust': 3.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 16.27, 'feels_like': 16.02, 'pressure': 1016, 'humidity': 79, 'dew_point': 12.63, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 80, 'wind_gust': 3.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 15.77, 'feels_like': 15.49, 'pressure': 1016, 'humidity': 80, 'dew_point': 12.33, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 2.68, 'wind_deg': 81, 'wind_gust': 3.25, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 15.4, 'feels_like': 15.08, 'pressure': 1016, 'humidity': 80, 'dew_point': 11.97, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 2.67, 'wind_deg': 84, 'wind_gust': 3.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 15.07, 'feels_like': 14.75, 'pressure': 1015, 'humidity': 81, 'dew_point': 11.84, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 2.72, 'wind_deg': 79, 'wind_gust': 3.04, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 14.72, 'feels_like': 14.41, 'pressure': 1015, 'humidity': 83, 'dew_point': 11.87, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 2.45, 'wind_deg': 78, 'wind_gust': 2.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.58, 'feels_like': 14.31, 'pressure': 1014, 'humidity': 85, 'dew_point': 12.09, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.31, 'wind_deg': 78, 'wind_gust': 2.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14.46, 'feels_like': 14.21, 'pressure': 1014, 'humidity': 86, 'dew_point': 12.15, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.4, 'wind_deg': 77, 'wind_gust': 2.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 14.26, 'feels_like': 14.04, 'pressure': 1014, 'humidity': 88, 'dew_point': 12.3, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 77, 'wind_gust': 2.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 14.39, 'feels_like': 14.16, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.26, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.22, 'wind_deg': 78, 'wind_gust': 2.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 14.27, 'feels_like': 14.02, 'pressure': 1015, 'humidity': 87, 'dew_point': 12.14, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 78, 'wind_gust': 2.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 15.55, 'feels_like': 15.3, 'pressure': 1016, 'humidity': 82, 'dew_point': 12.49, 'uvi': 0.45, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 78, 'wind_gust': 2.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 18.83, 'feels_like': 18.54, 'pressure': 1017, 'humidity': 68, 'dew_point': 12.8, 'uvi': 1.93, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 76, 'wind_gust': 2.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 21.38, 'feels_like': 21.06, 'pressure': 1017, 'humidity': 57, 'dew_point': 12.52, 'uvi': 4.66, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 75, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 23.28, 'feels_like': 22.97, 'pressure': 1016, 'humidity': 50, 'dew_point': 12.29, 'uvi': 7.83, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 47, 'wind_gust': 1.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 24.71, 'feels_like': 24.41, 'pressure': 1015, 'humidity': 45, 'dew_point': 11.99, 'uvi': 10.36, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 5, 'wind_gust': 1.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 25.67, 'feels_like': 25.42, 'pressure': 1014, 'humidity': 43, 'dew_point': 12.17, 'uvi': 11.18, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 356, 'wind_gust': 2.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1012, 'humidity': 42, 'dew_point': 12.35, 'uvi': 9.98, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 7, 'wind_gust': 2.24, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 26.39, 'feels_like': 26.39, 'pressure': 1011, 'humidity': 42, 'dew_point': 12.46, 'uvi': 7.09, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 14, 'wind_gust': 2.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 25.83, 'feels_like': 25.62, 'pressure': 1010, 'humidity': 44, 'dew_point': 12.66, 'uvi': 3.96, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 22, 'wind_gust': 2.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 24.42, 'feels_like': 24.22, 'pressure': 1010, 'humidity': 50, 'dew_point': 13.33, 'uvi': 1.52, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 42, 'wind_gust': 2.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 22.47, 'feels_like': 22.31, 'pressure': 1011, 'humidity': 59, 'dew_point': 14.07, 'uvi': 0.15, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 63, 'wind_gust': 2.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 20.6, 'feels_like': 20.41, 'pressure': 1012, 'humidity': 65, 'dew_point': 13.8, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 59, 'wind_gust': 1.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 00:00:00 | 54.000000 | 13.210000 | 17.270000 | 76.000000 | 1014.000000 |  | 17.480000 | 0.000000 | 10000.000000 | 75.000000 | 3.51 | 2.770000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 01:00:00 | 53.000000 | 12.950000 | 16.570000 | 78.000000 | 1015.000000 |  | 16.800000 | 0.000000 | 10000.000000 | 79.000000 | 3.38 | 2.640000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 02:00:00 | 58.000000 | 12.630000 | 16.020000 | 79.000000 | 1016.000000 |  | 16.270000 | 0.000000 | 10000.000000 | 80.000000 | 3.24 | 2.690000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 03:00:00 | 47.000000 | 12.330000 | 15.490000 | 80.000000 | 1016.000000 |  | 15.770000 | 0.000000 | 10000.000000 | 81.000000 | 3.25 | 2.680000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 04:00:00 | 37.000000 | 11.970000 | 15.080000 | 80.000000 | 1016.000000 |  | 15.400000 | 0.000000 | 10000.000000 | 84.000000 | 3.07 | 2.670000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 05:00:00 | 31.000000 | 11.840000 | 14.750000 | 81.000000 | 1015.000000 |  | 15.070000 | 0.000000 | 10000.000000 | 79.000000 | 3.04 | 2.720000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 11.870000 | 14.410000 | 83.000000 | 1015.000000 |  | 14.720000 | 0.000000 | 10000.000000 | 78.000000 | 2.72 | 2.450000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 12.090000 | 14.310000 | 85.000000 | 1014.000000 |  | 14.580000 | 0.000000 | 10000.000000 | 78.000000 | 2.56 | 2.310000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 08:00:00 | 77.000000 | 12.150000 | 14.210000 | 86.000000 | 1014.000000 |  | 14.460000 | 0.000000 | 10000.000000 | 77.000000 | 2.76 | 2.400000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 09:00:00 | 82.000000 | 12.300000 | 14.040000 | 88.000000 | 1014.000000 |  | 14.260000 | 0.000000 | 10000.000000 | 77.000000 | 2.48 | 2.300000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 10:00:00 | 74.000000 | 12.260000 | 14.160000 | 87.000000 | 1014.000000 |  | 14.390000 | 0.000000 | 10000.000000 | 78.000000 | 2.66 | 2.220000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 12.140000 | 14.020000 | 87.000000 | 1015.000000 |  | 14.270000 | 0.000000 | 10000.000000 | 78.000000 | 2.16 | 2.070000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 12:00:00 | 67.000000 | 12.490000 | 15.300000 | 82.000000 | 1016.000000 |  | 15.550000 | 0.450000 | 10000.000000 | 78.000000 | 2.61 | 1.950000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 13:00:00 | 72.000000 | 12.800000 | 18.540000 | 68.000000 | 1017.000000 |  | 18.830000 | 1.930000 | 10000.000000 | 76.000000 | 2.39 | 1.640000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 14:00:00 | 63.000000 | 12.520000 | 21.060000 | 57.000000 | 1017.000000 |  | 21.380000 | 4.660000 | 10000.000000 | 75.000000 | 2.06 | 1.180000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 15:00:00 | 67.000000 | 12.290000 | 22.970000 | 50.000000 | 1016.000000 |  | 23.280000 | 7.830000 | 10000.000000 | 47.000000 | 1.94 | 0.690000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 16:00:00 | 66.000000 | 11.990000 | 24.410000 | 45.000000 | 1015.000000 |  | 24.710000 | 10.360000 | 10000.000000 | 5.000000 | 1.93 | 0.700000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 12.170000 | 25.420000 | 43.000000 | 1014.000000 |  | 25.670000 | 11.180000 | 10000.000000 | 356.000000 | 2.13 | 0.850000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 18:00:00 | 47.000000 | 12.350000 | 26.270000 | 42.000000 | 1012.000000 |  | 26.270000 | 9.980000 | 10000.000000 | 7.000000 | 2.24 | 1.060000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 19:00:00 | 63.000000 | 12.460000 | 26.390000 | 42.000000 | 1011.000000 |  | 26.390000 | 7.090000 | 10000.000000 | 14.000000 | 2.43 | 1.180000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 20:00:00 | 74.000000 | 12.660000 | 25.620000 | 44.000000 | 1010.000000 |  | 25.830000 | 3.960000 | 10000.000000 | 22.000000 | 2.39 | 1.250000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 21:00:00 | 72.000000 | 13.330000 | 24.220000 | 50.000000 | 1010.000000 |  | 24.420000 | 1.520000 | 10000.000000 | 42.000000 | 2.83 | 1.290000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 22:00:00 | 78.000000 | 14.070000 | 22.310000 | 59.000000 | 1011.000000 |  | 22.470000 | 0.150000 | 10000.000000 | 63.000000 | 2.37 | 1.320000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16055010 | "AEROPUERTO AGUAS CLARAS [16055010]" | 8.315278 | -73.357500 | 1435.000000 | Climática Principal | Convencional | Activa | 1973-03-15 00:00:00 | NaT | Norte de Santander | Ocaña | San Jorge | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Algodonal (Alto Catatumbo) | America/Bogota | 2022-01-10 23:00:00 | 82.000000 | 13.800000 | 20.410000 | 65.000000 | 1012.000000 |  | 20.600000 | 0.000000 | 10000.000000 | 59.000000 | 1.92 | 1.710000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16055010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16055010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16055010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16055010_OWM_Windspeed_20220111.png)
