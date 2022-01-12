
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ITA VALSALICE  - AUT [21195120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21195120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.39577778,-74.39613889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.39577778&lon=-74.39613889)


| Parameter | Value |
|---|---|
| Code | 21195120 |
| Name | ITA VALSALICE  - AUT [21195120] |
| Latitude, ° | 4.39577778 |
| Longitude, ° | -74.39613889 |
| Elevation, m | 1460 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1989-02-14 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Silvania |
| Stream | 0 |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Sumapaz |

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

### (CNE index 1522) Open Weather values for station 21195120 - ITA VALSALICE  - AUT [21195120]

JSON data from API OWM:

```
{'lat': 4.3958, 'lon': -74.3961, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812905, 'sunset': 1641855684, 'temp': 25.22, 'feels_like': 25.78, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.69, 'uvi': 4.94, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 271, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, 'hourly': [{'dt': 1641772800, 'temp': 20.22, 'feels_like': 20.6, 'pressure': 1014, 'humidity': 88, 'dew_point': 18.17, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 94, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641776400, 'temp': 21.22, 'feels_like': 21.75, 'pressure': 1015, 'humidity': 90, 'dew_point': 19.51, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 91, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.57}}, {'dt': 1641780000, 'temp': 20.22, 'feels_like': 20.62, 'pressure': 1016, 'humidity': 89, 'dew_point': 18.35, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 94, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641783600, 'temp': 20.22, 'feels_like': 20.6, 'pressure': 1016, 'humidity': 88, 'dew_point': 18.17, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 99, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 20.22, 'feels_like': 20.57, 'pressure': 1016, 'humidity': 87, 'dew_point': 17.99, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 97, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641790800, 'temp': 18.22, 'feels_like': 18.37, 'pressure': 1016, 'humidity': 87, 'dew_point': 16.02, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 98, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 16.22, 'feels_like': 16.17, 'pressure': 1015, 'humidity': 87, 'dew_point': 14.06, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 100, 'wind_gust': 1.3, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 15.22, 'feels_like': 15.04, 'pressure': 1014, 'humidity': 86, 'dew_point': 12.9, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 97, 'wind_gust': 0.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 15.22, 'feels_like': 15.07, 'pressure': 1013, 'humidity': 87, 'dew_point': 13.07, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 88, 'wind_gust': 1.14, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 15.22, 'feels_like': 15.07, 'pressure': 1014, 'humidity': 87, 'dew_point': 13.07, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 95, 'wind_gust': 1.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 16.22, 'feels_like': 16.22, 'pressure': 1014, 'humidity': 89, 'dew_point': 14.41, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 86, 'wind_gust': 0.99, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 17.22, 'feels_like': 17.35, 'pressure': 1015, 'humidity': 90, 'dew_point': 15.57, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 98, 'wind_gust': 1.19, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 17.22, 'feels_like': 17.27, 'pressure': 1016, 'humidity': 87, 'dew_point': 15.04, 'uvi': 0.52, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 84, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 18.22, 'feels_like': 18.21, 'pressure': 1017, 'humidity': 81, 'dew_point': 14.91, 'uvi': 2.18, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 299, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 21.22, 'feels_like': 21.46, 'pressure': 1017, 'humidity': 79, 'dew_point': 17.43, 'uvi': 5.19, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 283, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641826800, 'temp': 23.22, 'feels_like': 23.53, 'pressure': 1017, 'humidity': 74, 'dew_point': 18.33, 'uvi': 8.75, 'clouds': 79, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 284, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641830400, 'temp': 24.22, 'feels_like': 24.53, 'pressure': 1015, 'humidity': 70, 'dew_point': 18.4, 'uvi': 11.72, 'clouds': 72, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 284, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641834000, 'temp': 24.22, 'feels_like': 24.47, 'pressure': 1014, 'humidity': 68, 'dew_point': 17.94, 'uvi': 12.75, 'clouds': 67, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 287, 'wind_gust': 1.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 25.22, 'feels_like': 25.63, 'pressure': 1013, 'humidity': 70, 'dew_point': 19.36, 'uvi': 11.57, 'clouds': 36, 'visibility': 10000, 'wind_speed': 2.85, 'wind_deg': 280, 'wind_gust': 2.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641841200, 'temp': 25.22, 'feels_like': 25.7, 'pressure': 1012, 'humidity': 73, 'dew_point': 20.04, 'uvi': 8.48, 'clouds': 51, 'visibility': 10000, 'wind_speed': 2.37, 'wind_deg': 277, 'wind_gust': 1.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641844800, 'temp': 25.22, 'feels_like': 25.78, 'pressure': 1011, 'humidity': 76, 'dew_point': 20.69, 'uvi': 4.94, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 271, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641848400, 'temp': 25.22, 'feels_like': 25.83, 'pressure': 1011, 'humidity': 78, 'dew_point': 21.11, 'uvi': 2, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 276, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641852000, 'temp': 24.22, 'feels_like': 24.86, 'pressure': 1012, 'humidity': 83, 'dew_point': 21.15, 'uvi': 0.45, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 289, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641855600, 'temp': 22.22, 'feels_like': 22.77, 'pressure': 1013, 'humidity': 87, 'dew_point': 19.95, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 82, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 00:00:00 | 93.000000 | 18.170000 | 20.600000 | 88.000000 | 1014.000000 | 0.19 | 20.220000 | 0.000000 | 10000.000000 | 94.000000 | 1.24 | 1.030000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 01:00:00 | 91.000000 | 19.510000 | 21.750000 | 90.000000 | 1015.000000 | 0.57 | 21.220000 | 0.000000 | 10000.000000 | 91.000000 | 1.65 | 1.590000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 18.350000 | 20.620000 | 89.000000 | 1016.000000 | 0.19 | 20.220000 | 0.000000 | 10000.000000 | 94.000000 | 1.66 | 1.670000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 03:00:00 | 82.000000 | 18.170000 | 20.600000 | 88.000000 | 1016.000000 | 0.12 | 20.220000 | 0.000000 | 10000.000000 | 99.000000 | 1.63 | 1.520000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 04:00:00 | 86.000000 | 17.990000 | 20.570000 | 87.000000 | 1016.000000 | 0.24 | 20.220000 | 0.000000 | 10000.000000 | 97.000000 | 1.79 | 1.570000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 05:00:00 | 85.000000 | 16.020000 | 18.370000 | 87.000000 | 1016.000000 |  | 18.220000 | 0.000000 | 10000.000000 | 98.000000 | 1.56 | 1.620000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 06:00:00 | 44.000000 | 14.060000 | 16.170000 | 87.000000 | 1015.000000 |  | 16.220000 | 0.000000 | 10000.000000 | 100.000000 | 1.3 | 1.190000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 07:00:00 | 47.000000 | 12.900000 | 15.040000 | 86.000000 | 1014.000000 |  | 15.220000 | 0.000000 | 10000.000000 | 97.000000 | 0.98 | 0.850000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 08:00:00 | 44.000000 | 13.070000 | 15.070000 | 87.000000 | 1013.000000 |  | 15.220000 | 0.000000 | 10000.000000 | 88.000000 | 1.14 | 1.020000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 09:00:00 | 45.000000 | 13.070000 | 15.070000 | 87.000000 | 1014.000000 |  | 15.220000 | 0.000000 | 10000.000000 | 95.000000 | 1.07 | 0.760000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 10:00:00 | 47.000000 | 14.410000 | 16.220000 | 89.000000 | 1014.000000 |  | 16.220000 | 0.000000 | 10000.000000 | 86.000000 | 0.99 | 0.610000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 11:00:00 | 48.000000 | 15.570000 | 17.350000 | 90.000000 | 1015.000000 |  | 17.220000 | 0.000000 | 10000.000000 | 98.000000 | 1.19 | 1.140000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 12:00:00 | 82.000000 | 15.040000 | 17.270000 | 87.000000 | 1016.000000 |  | 17.220000 | 0.520000 | 10000.000000 | 84.000000 | 1.11 | 0.860000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 13:00:00 | 96.000000 | 14.910000 | 18.210000 | 81.000000 | 1017.000000 |  | 18.220000 | 2.180000 | 10000.000000 | 299.000000 | 0.91 | 0.960000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 14:00:00 | 87.000000 | 17.430000 | 21.460000 | 79.000000 | 1017.000000 | 0.16 | 21.220000 | 5.190000 | 10000.000000 | 283.000000 | 1.07 | 1.600000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 18.330000 | 23.530000 | 74.000000 | 1017.000000 | 0.15 | 23.220000 | 8.750000 | 10000.000000 | 284.000000 | 1.3 | 2.110000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 16:00:00 | 72.000000 | 18.400000 | 24.530000 | 70.000000 | 1015.000000 | 0.16 | 24.220000 | 11.720000 | 10000.000000 | 284.000000 | 1.57 | 2.560000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 17:00:00 | 67.000000 | 17.940000 | 24.470000 | 68.000000 | 1014.000000 |  | 24.220000 | 12.750000 | 10000.000000 | 287.000000 | 1.86 | 2.570000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 18:00:00 | 36.000000 | 19.360000 | 25.630000 | 70.000000 | 1013.000000 | 0.18 | 25.220000 | 11.570000 | 10000.000000 | 280.000000 | 2.05 | 2.850000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 19:00:00 | 51.000000 | 20.040000 | 25.700000 | 73.000000 | 1012.000000 | 0.63 | 25.220000 | 8.480000 | 10000.000000 | 277.000000 | 1.95 | 2.370000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 20:00:00 | 57.000000 | 20.690000 | 25.780000 | 76.000000 | 1011.000000 | 0.68 | 25.220000 | 4.940000 | 10000.000000 | 271.000000 | 1.44 | 1.470000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 21:00:00 | 61.000000 | 21.110000 | 25.830000 | 78.000000 | 1011.000000 | 0.65 | 25.220000 | 2.000000 | 10000.000000 | 276.000000 | 0.88 | 0.970000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 22:00:00 | 65.000000 | 21.150000 | 24.860000 | 83.000000 | 1012.000000 | 0.66 | 24.220000 | 0.450000 | 10000.000000 | 289.000000 | 0.97 | 0.850000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21195120 | "ITA VALSALICE  - AUT [21195120]" | 4.395778 | -74.396139 | 1460.000000 | Climática Principal | Automática con Telemetría | Activa | 1989-02-14 19:00:00 | NaT | Cundinamarca | Silvania | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz | America/Bogota | 2022-01-10 23:00:00 | 63.000000 | 19.950000 | 22.770000 | 87.000000 | 1013.000000 | 0.53 | 22.220000 | 0.000000 | 10000.000000 | 82.000000 | 1.1 | 0.470000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21195120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21195120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21195120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21195120_OWM_Windspeed_20220111.png)
