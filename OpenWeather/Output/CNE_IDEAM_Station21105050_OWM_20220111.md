
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ROSALES LOS [21105050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21105050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.60305556,-75.41833333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.60305556&lon=-75.41833333)


| Parameter | Value |
|---|---|
| Code | 21105050 |
| Name | ROSALES LOS [21105050] |
| Latitude, ° | 2.60305556 |
| Longitude, ° | -75.41833333 |
| Elevation, m | 553 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1973-12-15 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | Campoalegre |
| Stream | Guayabero |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Rio Neiva |

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

### (CNE index 1217) Open Weather values for station 21105050 - ROSALES LOS [21105050]

JSON data from API OWM:

```
{'lat': 2.6031, 'lon': -75.4183, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812977, 'sunset': 1641856103, 'temp': 31.15, 'feels_like': 35.43, 'pressure': 1009, 'humidity': 61, 'dew_point': 22.74, 'uvi': 5.43, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 32, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, 'hourly': [{'dt': 1641772800, 'temp': 27.15, 'feels_like': 29.97, 'pressure': 1011, 'humidity': 79, 'dew_point': 23.19, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 97, 'wind_gust': 1.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 27.15, 'feels_like': 30.18, 'pressure': 1013, 'humidity': 81, 'dew_point': 23.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 120, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.15, 'feels_like': 26.15, 'pressure': 1014, 'humidity': 83, 'dew_point': 23.03, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 122, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 26.15, 'feels_like': 26.15, 'pressure': 1015, 'humidity': 85, 'dew_point': 23.43, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 149, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641787200, 'temp': 21.85, 'feels_like': 22.39, 'pressure': 1015, 'humidity': 88, 'dew_point': 19.77, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 171, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641790800, 'temp': 21.37, 'feels_like': 21.89, 'pressure': 1014, 'humidity': 89, 'dew_point': 19.48, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 172, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641794400, 'temp': 21.22, 'feels_like': 21.77, 'pressure': 1014, 'humidity': 91, 'dew_point': 19.69, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 167, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641798000, 'temp': 20.98, 'feels_like': 21.51, 'pressure': 1013, 'humidity': 91, 'dew_point': 19.45, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 152, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 20.74, 'feels_like': 21.25, 'pressure': 1013, 'humidity': 91, 'dew_point': 19.22, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 163, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 20.51, 'feels_like': 21.02, 'pressure': 1013, 'humidity': 92, 'dew_point': 19.17, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 173, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641808800, 'temp': 20.73, 'feels_like': 21.26, 'pressure': 1013, 'humidity': 92, 'dew_point': 19.38, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 176, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.15, 'feels_like': 23.9, 'pressure': 1014, 'humidity': 91, 'dew_point': 21.6, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 159, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.15, 'feels_like': 23.84, 'pressure': 1015, 'humidity': 89, 'dew_point': 21.24, 'uvi': 0.46, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 209, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.15, 'feels_like': 25.91, 'pressure': 1015, 'humidity': 84, 'dew_point': 22.25, 'uvi': 2.12, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 257, 'wind_gust': 0.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.15, 'feels_like': 29.87, 'pressure': 1015, 'humidity': 78, 'dew_point': 22.98, 'uvi': 5.16, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 13, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641826800, 'temp': 27.15, 'feels_like': 29.11, 'pressure': 1015, 'humidity': 70, 'dew_point': 21.21, 'uvi': 8.8, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 9, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641830400, 'temp': 28.15, 'feels_like': 30.55, 'pressure': 1014, 'humidity': 67, 'dew_point': 21.44, 'uvi': 11.34, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 11, 'wind_gust': 2.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641834000, 'temp': 29.15, 'feels_like': 31.96, 'pressure': 1013, 'humidity': 64, 'dew_point': 21.64, 'uvi': 12.5, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 14, 'wind_gust': 2.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641837600, 'temp': 31.15, 'feels_like': 35.69, 'pressure': 1012, 'humidity': 62, 'dew_point': 23.01, 'uvi': 11.47, 'clouds': 70, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 22, 'wind_gust': 2.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641841200, 'temp': 31.15, 'feels_like': 35.17, 'pressure': 1010, 'humidity': 60, 'dew_point': 22.46, 'uvi': 9.12, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 33, 'wind_gust': 2.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.64}}, {'dt': 1641844800, 'temp': 31.15, 'feels_like': 35.43, 'pressure': 1009, 'humidity': 61, 'dew_point': 22.74, 'uvi': 5.43, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 32, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641848400, 'temp': 30.15, 'feels_like': 33.98, 'pressure': 1009, 'humidity': 64, 'dew_point': 22.59, 'uvi': 2.32, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 42, 'wind_gust': 2.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641852000, 'temp': 29.15, 'feels_like': 33.06, 'pressure': 1009, 'humidity': 70, 'dew_point': 23.12, 'uvi': 0.56, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 55, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641855600, 'temp': 28.15, 'feels_like': 32.48, 'pressure': 1011, 'humidity': 80, 'dew_point': 24.37, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 101, 'wind_gust': 1.35, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 23.190000 | 29.970000 | 79.000000 | 1011.000000 |  | 27.150000 | 0.000000 | 10000.000000 | 97.000000 | 1.25 | 1.030000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 23.610000 | 30.180000 | 81.000000 | 1013.000000 |  | 27.150000 | 0.000000 | 10000.000000 | 120.000000 | 1.17 | 0.550000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 23.030000 | 26.150000 | 83.000000 | 1014.000000 |  | 26.150000 | 0.000000 | 10000.000000 | 122.000000 | 1.14 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 23.430000 | 26.150000 | 85.000000 | 1015.000000 | 0.15 | 26.150000 | 0.000000 | 10000.000000 | 149.000000 | 1.23 | 0.490000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 19.770000 | 22.390000 | 88.000000 | 1015.000000 | 0.21 | 21.850000 | 0.000000 | 10000.000000 | 171.000000 | 1.37 | 0.800000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 05:00:00 | 95.000000 | 19.480000 | 21.890000 | 89.000000 | 1014.000000 | 0.22 | 21.370000 | 0.000000 | 10000.000000 | 172.000000 | 1.39 | 0.840000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 06:00:00 | 38.000000 | 19.690000 | 21.770000 | 91.000000 | 1014.000000 | 0.23 | 21.220000 | 0.000000 | 10000.000000 | 167.000000 | 1.25 | 0.830000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 07:00:00 | 44.000000 | 19.450000 | 21.510000 | 91.000000 | 1013.000000 | 0.19 | 20.980000 | 0.000000 | 10000.000000 | 152.000000 | 1.17 | 0.650000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 08:00:00 | 71.000000 | 19.220000 | 21.250000 | 91.000000 | 1013.000000 | 0.15 | 20.740000 | 0.000000 | 10000.000000 | 163.000000 | 1.01 | 0.580000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 09:00:00 | 76.000000 | 19.170000 | 21.020000 | 92.000000 | 1013.000000 | 0.2 | 20.510000 | 0.000000 | 10000.000000 | 173.000000 | 1.11 | 0.740000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 10:00:00 | 73.000000 | 19.380000 | 21.260000 | 92.000000 | 1013.000000 |  | 20.730000 | 0.000000 | 10000.000000 | 176.000000 | 1.04 | 0.690000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 11:00:00 | 68.000000 | 21.600000 | 23.900000 | 91.000000 | 1014.000000 |  | 23.150000 | 0.000000 | 10000.000000 | 159.000000 | 0.87 | 0.380000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 12:00:00 | 95.000000 | 21.240000 | 23.840000 | 89.000000 | 1015.000000 |  | 23.150000 | 0.460000 | 10000.000000 | 209.000000 | 0.84 | 0.350000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 13:00:00 | 94.000000 | 22.250000 | 25.910000 | 84.000000 | 1015.000000 |  | 25.150000 | 2.120000 | 10000.000000 | 257.000000 | 0.59 | 0.320000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 14:00:00 | 84.000000 | 22.980000 | 29.870000 | 78.000000 | 1015.000000 | 0.15 | 27.150000 | 5.160000 | 10000.000000 | 13.000000 | 1.05 | 0.610000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 15:00:00 | 81.000000 | 21.210000 | 29.110000 | 70.000000 | 1015.000000 | 0.53 | 27.150000 | 8.800000 | 10000.000000 | 9.000000 | 2.18 | 1.600000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 16:00:00 | 86.000000 | 21.440000 | 30.550000 | 67.000000 | 1014.000000 | 0.55 | 28.150000 | 11.340000 | 10000.000000 | 11.000000 | 2.77 | 2.200000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 17:00:00 | 88.000000 | 21.640000 | 31.960000 | 64.000000 | 1013.000000 | 0.57 | 29.150000 | 12.500000 | 10000.000000 | 14.000000 | 2.78 | 2.300000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 18:00:00 | 70.000000 | 23.010000 | 35.690000 | 62.000000 | 1012.000000 | 0.7 | 31.150000 | 11.470000 | 10000.000000 | 22.000000 | 2.55 | 2.120000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 22.460000 | 35.170000 | 60.000000 | 1010.000000 | 0.64 | 31.150000 | 9.120000 | 10000.000000 | 33.000000 | 2.65 | 2.260000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 20:00:00 | 84.000000 | 22.740000 | 35.430000 | 61.000000 | 1009.000000 | 0.44 | 31.150000 | 5.430000 | 10000.000000 | 32.000000 | 2.34 | 1.940000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 21:00:00 | 80.000000 | 22.590000 | 33.980000 | 64.000000 | 1009.000000 | 0.48 | 30.150000 | 2.320000 | 10000.000000 | 42.000000 | 2.15 | 1.600000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 22:00:00 | 79.000000 | 23.120000 | 33.060000 | 70.000000 | 1009.000000 | 0.68 | 29.150000 | 0.560000 | 10000.000000 | 55.000000 | 2.26 | 1.290000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21105050 | "ROSALES LOS [21105050]" | 2.603056 | -75.418333 | 553.000000 | Climática Principal | Convencional | Activa | 1973-12-15 00:00:00 | NaT | Huila | Campoalegre | Guayabero | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Neiva | America/Bogota | 2022-01-10 23:00:00 | 77.000000 | 24.370000 | 32.480000 | 80.000000 | 1011.000000 | 0.81 | 28.150000 | 0.000000 | 10000.000000 | 101.000000 | 1.35 | 0.550000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21105050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21105050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21105050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21105050_OWM_Windspeed_20220111.png)
