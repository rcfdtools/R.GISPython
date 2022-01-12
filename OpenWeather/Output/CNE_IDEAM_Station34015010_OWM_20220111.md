
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LAS GAVIOTAS [34015010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station34015010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.55394444,-70.93011111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.55394444&lon=-70.93011111)


| Parameter | Value |
|---|---|
| Code | 34015010 |
| Name | LAS GAVIOTAS [34015010] |
| Latitude, ° | 4.55394444 |
| Longitude, ° | -70.93011111 |
| Elevation, m | 171 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1967-08-14 19:00:00 |
| Suspension date | NaT |
| State | Vichada |
| County | Cumaribo |
| Stream | 0 |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Tomo |
| SZH - Hydrographic subzone | Alto Río Tomo |

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

### (CNE index 1068) Open Weather values for station 34015010 - LAS GAVIOTAS [34015010]

JSON data from API OWM:

```
{'lat': 4.5539, 'lon': -70.9301, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812088, 'sunset': 1641854837, 'temp': 34.67, 'feels_like': 33.65, 'pressure': 1007, 'humidity': 27, 'dew_point': 12.94, 'uvi': 3.88, 'clouds': 63, 'visibility': 10000, 'wind_speed': 7.05, 'wind_deg': 40, 'wind_gust': 7.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 29.96, 'feels_like': 29.64, 'pressure': 1010, 'humidity': 40, 'dew_point': 14.9, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 5.7, 'wind_deg': 18, 'wind_gust': 9.58, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 28.27, 'feels_like': 28.22, 'pressure': 1011, 'humidity': 44, 'dew_point': 14.86, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 4.28, 'wind_deg': 11, 'wind_gust': 9.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 26.87, 'feels_like': 27.18, 'pressure': 1012, 'humidity': 48, 'dew_point': 14.94, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 3.7, 'wind_deg': 13, 'wind_gust': 8.51, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 25.99, 'feels_like': 25.99, 'pressure': 1012, 'humidity': 50, 'dew_point': 14.77, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 4.04, 'wind_deg': 5, 'wind_gust': 9.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 25.27, 'feels_like': 25.21, 'pressure': 1012, 'humidity': 52, 'dew_point': 14.72, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 3.82, 'wind_deg': 356, 'wind_gust': 9.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.54, 'feels_like': 24.43, 'pressure': 1011, 'humidity': 53, 'dew_point': 14.34, 'uvi': 0, 'clouds': 43, 'visibility': 10000, 'wind_speed': 3.8, 'wind_deg': 356, 'wind_gust': 9.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 23.6, 'feels_like': 23.45, 'pressure': 1011, 'humidity': 55, 'dew_point': 14.04, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3.34, 'wind_deg': 13, 'wind_gust': 9.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.9, 'feels_like': 22.68, 'pressure': 1010, 'humidity': 55, 'dew_point': 13.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 14, 'wind_gust': 7.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.65, 'feels_like': 22.38, 'pressure': 1010, 'humidity': 54, 'dew_point': 12.88, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.33, 'wind_deg': 23, 'wind_gust': 9.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 22.47, 'feels_like': 22.18, 'pressure': 1010, 'humidity': 54, 'dew_point': 12.71, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.31, 'wind_deg': 19, 'wind_gust': 9.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 22.23, 'feels_like': 21.94, 'pressure': 1011, 'humidity': 55, 'dew_point': 12.77, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 3.43, 'wind_deg': 16, 'wind_gust': 9.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 21.88, 'feels_like': 21.59, 'pressure': 1012, 'humidity': 56, 'dew_point': 12.72, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 3.92, 'wind_deg': 18, 'wind_gust': 11.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 23.64, 'feels_like': 23.47, 'pressure': 1013, 'humidity': 54, 'dew_point': 13.79, 'uvi': 0.71, 'clouds': 54, 'visibility': 10000, 'wind_speed': 5.24, 'wind_deg': 18, 'wind_gust': 13.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.6, 'feels_like': 26.6, 'pressure': 1014, 'humidity': 47, 'dew_point': 14.37, 'uvi': 2.59, 'clouds': 72, 'visibility': 10000, 'wind_speed': 7.56, 'wind_deg': 24, 'wind_gust': 12.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 29.11, 'feels_like': 28.72, 'pressure': 1014, 'humidity': 40, 'dew_point': 14.14, 'uvi': 5.62, 'clouds': 53, 'visibility': 10000, 'wind_speed': 8.14, 'wind_deg': 29, 'wind_gust': 11.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 30.99, 'feels_like': 30.25, 'pressure': 1014, 'humidity': 35, 'dew_point': 13.75, 'uvi': 8.91, 'clouds': 43, 'visibility': 10000, 'wind_speed': 8.34, 'wind_deg': 33, 'wind_gust': 10.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 32.42, 'feels_like': 31.71, 'pressure': 1013, 'humidity': 33, 'dew_point': 14.09, 'uvi': 11.16, 'clouds': 36, 'visibility': 10000, 'wind_speed': 8.15, 'wind_deg': 32, 'wind_gust': 9.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 33.4, 'feels_like': 32.66, 'pressure': 1012, 'humidity': 31, 'dew_point': 13.97, 'uvi': 11.64, 'clouds': 35, 'visibility': 10000, 'wind_speed': 8.02, 'wind_deg': 32, 'wind_gust': 9.15, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 34.29, 'feels_like': 33.5, 'pressure': 1010, 'humidity': 29, 'dew_point': 13.71, 'uvi': 10.11, 'clouds': 44, 'visibility': 10000, 'wind_speed': 7.44, 'wind_deg': 35, 'wind_gust': 8.21, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 34.7, 'feels_like': 33.87, 'pressure': 1008, 'humidity': 28, 'dew_point': 13.52, 'uvi': 7.19, 'clouds': 51, 'visibility': 10000, 'wind_speed': 7.24, 'wind_deg': 37, 'wind_gust': 7.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 34.67, 'feels_like': 33.65, 'pressure': 1007, 'humidity': 27, 'dew_point': 12.94, 'uvi': 3.88, 'clouds': 63, 'visibility': 10000, 'wind_speed': 7.05, 'wind_deg': 40, 'wind_gust': 7.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 34.42, 'feels_like': 33.5, 'pressure': 1006, 'humidity': 28, 'dew_point': 13.28, 'uvi': 1.42, 'clouds': 56, 'visibility': 10000, 'wind_speed': 6.48, 'wind_deg': 44, 'wind_gust': 7.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 33.39, 'feels_like': 32.49, 'pressure': 1007, 'humidity': 30, 'dew_point': 13.46, 'uvi': 0.25, 'clouds': 56, 'visibility': 10000, 'wind_speed': 5.27, 'wind_deg': 49, 'wind_gust': 7.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 30.28, 'feels_like': 29.56, 'pressure': 1008, 'humidity': 36, 'dew_point': 13.56, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 3.02, 'wind_deg': 51, 'wind_gust': 5.28, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 00:00:00 | 43.000000 | 14.900000 | 29.640000 | 40.000000 | 1010.000000 |  | 29.960000 | 0.000000 | 10000.000000 | 18.000000 | 9.58 | 5.700000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 01:00:00 | 47.000000 | 14.860000 | 28.220000 | 44.000000 | 1011.000000 |  | 28.270000 | 0.000000 | 10000.000000 | 11.000000 | 9.23 | 4.280000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 02:00:00 | 49.000000 | 14.940000 | 27.180000 | 48.000000 | 1012.000000 |  | 26.870000 | 0.000000 | 10000.000000 | 13.000000 | 8.51 | 3.700000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 03:00:00 | 46.000000 | 14.770000 | 25.990000 | 50.000000 | 1012.000000 |  | 25.990000 | 0.000000 | 10000.000000 | 5.000000 | 9.73 | 4.040000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 04:00:00 | 51.000000 | 14.720000 | 25.210000 | 52.000000 | 1012.000000 |  | 25.270000 | 0.000000 | 10000.000000 | 356.000000 | 9.54 | 3.820000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 05:00:00 | 43.000000 | 14.340000 | 24.430000 | 53.000000 | 1011.000000 |  | 24.540000 | 0.000000 | 10000.000000 | 356.000000 | 9.75 | 3.800000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 14.040000 | 23.450000 | 55.000000 | 1011.000000 |  | 23.600000 | 0.000000 | 10000.000000 | 13.000000 | 9.75 | 3.340000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 13.390000 | 22.680000 | 55.000000 | 1010.000000 |  | 22.900000 | 0.000000 | 10000.000000 | 14.000000 | 7.41 | 3.170000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 12.880000 | 22.380000 | 54.000000 | 1010.000000 |  | 22.650000 | 0.000000 | 10000.000000 | 23.000000 | 9.19 | 3.330000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 12.710000 | 22.180000 | 54.000000 | 1010.000000 |  | 22.470000 | 0.000000 | 10000.000000 | 19.000000 | 9.02 | 3.310000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 12.770000 | 21.940000 | 55.000000 | 1011.000000 |  | 22.230000 | 0.000000 | 10000.000000 | 16.000000 | 9.2 | 3.430000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 11:00:00 | 95.000000 | 12.720000 | 21.590000 | 56.000000 | 1012.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 18.000000 | 11.45 | 3.920000 | 804 | Clouds | overcast clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 12:00:00 | 54.000000 | 13.790000 | 23.470000 | 54.000000 | 1013.000000 |  | 23.640000 | 0.710000 | 10000.000000 | 18.000000 | 13.12 | 5.240000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 13:00:00 | 72.000000 | 14.370000 | 26.600000 | 47.000000 | 1014.000000 |  | 26.600000 | 2.590000 | 10000.000000 | 24.000000 | 12.54 | 7.560000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 14:00:00 | 53.000000 | 14.140000 | 28.720000 | 40.000000 | 1014.000000 |  | 29.110000 | 5.620000 | 10000.000000 | 29.000000 | 11.11 | 8.140000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 15:00:00 | 43.000000 | 13.750000 | 30.250000 | 35.000000 | 1014.000000 |  | 30.990000 | 8.910000 | 10000.000000 | 33.000000 | 10.45 | 8.340000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 16:00:00 | 36.000000 | 14.090000 | 31.710000 | 33.000000 | 1013.000000 |  | 32.420000 | 11.160000 | 10000.000000 | 32.000000 | 9.75 | 8.150000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 17:00:00 | 35.000000 | 13.970000 | 32.660000 | 31.000000 | 1012.000000 |  | 33.400000 | 11.640000 | 10000.000000 | 32.000000 | 9.15 | 8.020000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 18:00:00 | 44.000000 | 13.710000 | 33.500000 | 29.000000 | 1010.000000 |  | 34.290000 | 10.110000 | 10000.000000 | 35.000000 | 8.21 | 7.440000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 19:00:00 | 51.000000 | 13.520000 | 33.870000 | 28.000000 | 1008.000000 |  | 34.700000 | 7.190000 | 10000.000000 | 37.000000 | 7.79 | 7.240000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 20:00:00 | 63.000000 | 12.940000 | 33.650000 | 27.000000 | 1007.000000 |  | 34.670000 | 3.880000 | 10000.000000 | 40.000000 | 7.57 | 7.050000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 21:00:00 | 56.000000 | 13.280000 | 33.500000 | 28.000000 | 1006.000000 |  | 34.420000 | 1.420000 | 10000.000000 | 44.000000 | 7.15 | 6.480000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 22:00:00 | 56.000000 | 13.460000 | 32.490000 | 30.000000 | 1007.000000 |  | 33.390000 | 0.250000 | 10000.000000 | 49.000000 | 7.1 | 5.270000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 34015010 | "LAS GAVIOTAS [34015010]" | 4.553944 | -70.930111 | 171.000000 | Climática Principal | Convencional | Activa | 1967-08-14 19:00:00 | NaT | Vichada | Cumaribo | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Tomo | Alto Río Tomo | America/Bogota | 2022-01-10 23:00:00 | 59.000000 | 13.560000 | 29.560000 | 36.000000 | 1008.000000 |  | 30.280000 | 0.000000 | 10000.000000 | 51.000000 | 5.28 | 3.020000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station34015010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station34015010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station34015010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station34015010_OWM_Windspeed_20220111.png)
