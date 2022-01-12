
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CARMEN DE TONCHALA [16025010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16025010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.84888889,-72.56611111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.84888889&lon=-72.56611111)


| Parameter | Value |
|---|---|
| Code | 16025010 |
| Name | CARMEN DE TONCHALA [16025010] |
| Latitude, ° | 7.84888889 |
| Longitude, ° | -72.56611111 |
| Elevation, m | 285 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1968-10-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Cúcuta |
| Stream | Zulia |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Zulia |

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

### (CNE index 597) Open Weather values for station 16025010 - CARMEN DE TONCHALA [16025010]

JSON data from API OWM:

```
{'lat': 7.8489, 'lon': -72.5661, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812802, 'sunset': 1641854909, 'temp': 29.06, 'feels_like': 29.86, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.9, 'uvi': 1.52, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.06, 'feels_like': 24.56, 'pressure': 1016, 'humidity': 78, 'dew_point': 19.99, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 24.06, 'feels_like': 24.56, 'pressure': 1016, 'humidity': 78, 'dew_point': 19.99, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 23.06, 'feels_like': 23.72, 'pressure': 1017, 'humidity': 88, 'dew_point': 20.96, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 22.06, 'feels_like': 22.93, 'pressure': 1017, 'humidity': 100, 'dew_point': 22.06, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 120, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 21.06, 'feels_like': 21.83, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.06, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 140, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 21.06, 'feels_like': 21.83, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.06, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 21.06, 'feels_like': 21.83, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.06, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 19.77, 'feels_like': 19.79, 'pressure': 1015, 'humidity': 76, 'dew_point': 15.42, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 213, 'wind_gust': 1.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 19.82, 'feels_like': 19.79, 'pressure': 1015, 'humidity': 74, 'dew_point': 15.06, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 206, 'wind_gust': 1.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 19.71, 'feels_like': 19.64, 'pressure': 1015, 'humidity': 73, 'dew_point': 14.74, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 201, 'wind_gust': 1.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 19.06, 'feels_like': 19.32, 'pressure': 1015, 'humidity': 88, 'dew_point': 17.03, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641812400, 'temp': 18.06, 'feels_like': 18.38, 'pressure': 1016, 'humidity': 94, 'dew_point': 17.08, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 130, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 18.06, 'feels_like': 18.38, 'pressure': 1016, 'humidity': 94, 'dew_point': 17.08, 'uvi': 0.54, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 22.06, 'feels_like': 22.23, 'pressure': 1018, 'humidity': 73, 'dew_point': 17, 'uvi': 2.11, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 25.06, 'feels_like': 25.21, 'pressure': 1018, 'humidity': 61, 'dew_point': 17.02, 'uvi': 4.98, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 330, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 26.06, 'feels_like': 26.06, 'pressure': 1018, 'humidity': 57, 'dew_point': 16.88, 'uvi': 8.27, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 28.06, 'feels_like': 28.61, 'pressure': 1017, 'humidity': 51, 'dew_point': 16.98, 'uvi': 9.89, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 28.06, 'feels_like': 28.9, 'pressure': 1016, 'humidity': 54, 'dew_point': 17.89, 'uvi': 10.61, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 29.06, 'feels_like': 29.86, 'pressure': 1015, 'humidity': 51, 'dew_point': 17.9, 'uvi': 9.4, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 360, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 30.06, 'feels_like': 30.83, 'pressure': 1014, 'humidity': 48, 'dew_point': 17.85, 'uvi': 2.74, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 350, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 29.06, 'feels_like': 29.86, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.9, 'uvi': 1.52, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 28.06, 'feels_like': 28.9, 'pressure': 1013, 'humidity': 54, 'dew_point': 17.89, 'uvi': 0.58, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 360, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 27.06, 'feels_like': 27.94, 'pressure': 1014, 'humidity': 57, 'dew_point': 17.82, 'uvi': 0.18, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 27.06, 'feels_like': 27.94, 'pressure': 1014, 'humidity': 57, 'dew_point': 17.82, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 350, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 19.990000 | 24.560000 | 78.000000 | 1016.000000 |  | 24.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 01:00:00 | 40.000000 | 19.990000 | 24.560000 | 78.000000 | 1016.000000 |  | 24.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 02:00:00 | 40.000000 | 20.960000 | 23.720000 | 88.000000 | 1017.000000 |  | 23.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 03:00:00 | 40.000000 | 22.060000 | 22.930000 | 100.000000 | 1017.000000 |  | 22.060000 | 0.000000 | 10000.000000 | 120.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 04:00:00 | 40.000000 | 21.060000 | 21.830000 | 100.000000 | 1016.000000 |  | 21.060000 | 0.000000 | 10000.000000 | 140.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 05:00:00 | 40.000000 | 21.060000 | 21.830000 | 100.000000 | 1016.000000 |  | 21.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 21.060000 | 21.830000 | 100.000000 | 1016.000000 |  | 21.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 15.420000 | 19.790000 | 76.000000 | 1015.000000 |  | 19.770000 | 0.000000 | 10000.000000 | 213.000000 | 1.67 | 1.290000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 08:00:00 | 66.000000 | 15.060000 | 19.790000 | 74.000000 | 1015.000000 |  | 19.820000 | 0.000000 | 10000.000000 | 206.000000 | 1.48 | 1.220000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 09:00:00 | 59.000000 | 14.740000 | 19.640000 | 73.000000 | 1015.000000 |  | 19.710000 | 0.000000 | 10000.000000 | 201.000000 | 1.77 | 1.480000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 10:00:00 | 20.000000 | 17.030000 | 19.320000 | 88.000000 | 1015.000000 |  | 19.060000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 17.080000 | 18.380000 | 94.000000 | 1016.000000 |  | 18.060000 | 0.000000 | 10000.000000 | 130.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 17.080000 | 18.380000 | 94.000000 | 1016.000000 |  | 18.060000 | 0.540000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 17.000000 | 22.230000 | 73.000000 | 1018.000000 |  | 22.060000 | 2.110000 | 10000.000000 | 140.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 17.020000 | 25.210000 | 61.000000 | 1018.000000 |  | 25.060000 | 4.980000 | 10000.000000 | 330.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 15:00:00 | 40.000000 | 16.880000 | 26.060000 | 57.000000 | 1018.000000 |  | 26.060000 | 8.270000 | 10000.000000 | 0.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 16.980000 | 28.610000 | 51.000000 | 1017.000000 |  | 28.060000 | 9.890000 | 10000.000000 | 0.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 17.890000 | 28.900000 | 54.000000 | 1016.000000 |  | 28.060000 | 10.610000 | 10000.000000 | 20.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 17.900000 | 29.860000 | 51.000000 | 1015.000000 |  | 29.060000 | 9.400000 | 10000.000000 | 360.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 17.850000 | 30.830000 | 48.000000 | 1014.000000 |  | 30.060000 | 2.740000 | 10000.000000 | 350.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 20:00:00 | 40.000000 | 17.900000 | 29.860000 | 51.000000 | 1013.000000 |  | 29.060000 | 1.520000 | 10000.000000 | 20.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 21:00:00 | 40.000000 | 17.890000 | 28.900000 | 54.000000 | 1013.000000 |  | 28.060000 | 0.580000 | 10000.000000 | 360.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 22:00:00 | 40.000000 | 17.820000 | 27.940000 | 57.000000 | 1014.000000 |  | 27.060000 | 0.180000 | 10000.000000 | 10.000000 |  | 4.630000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025010 | "CARMEN DE TONCHALA [16025010]" | 7.848889 | -72.566111 | 285.000000 | Climática Principal | Convencional | Activa | 1968-10-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Zulia | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 17.820000 | 27.940000 | 57.000000 | 1014.000000 |  | 27.060000 | 0.000000 | 10000.000000 | 350.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station16025010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16025010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16025010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025010_OWM_Windspeed_20220111.png)
