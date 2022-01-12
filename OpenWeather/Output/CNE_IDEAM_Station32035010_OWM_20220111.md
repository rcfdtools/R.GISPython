
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA MACARENA [32035010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station32035010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.17611111,-73.79333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.17611111&lon=-73.79333333)


| Parameter | Value |
|---|---|
| Code | 32035010 |
| Name | LA MACARENA [32035010] |
| Latitude, ° | 2.17611111 |
| Longitude, ° | -73.79333333 |
| Elevation, m | 248 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1967-10-14 19:00:00 |
| Suspension date | NaT |
| State | Meta |
| County | La Macarena |
| Stream | 0 |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Guaviare |
| SZH - Hydrographic subzone | Alto Guaviare |

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

### (CNE index 2424) Open Weather values for station 32035010 - LA MACARENA [32035010]

JSON data from API OWM:

```
{'lat': 2.1761, 'lon': -73.7933, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812545, 'sunset': 1641855754, 'temp': 33.22, 'feels_like': 32.75, 'pressure': 1007, 'humidity': 33, 'dew_point': 14.78, 'uvi': 3.38, 'clouds': 35, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 52, 'wind_gust': 4.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.58, 'feels_like': 28.15, 'pressure': 1009, 'humidity': 52, 'dew_point': 16.85, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 23, 'wind_gust': 9.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.83, 'feels_like': 27.55, 'pressure': 1010, 'humidity': 55, 'dew_point': 17.04, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.99, 'wind_deg': 21, 'wind_gust': 9.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1011, 'humidity': 58, 'dew_point': 17.07, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 20, 'wind_gust': 8.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.04, 'feels_like': 25.22, 'pressure': 1012, 'humidity': 62, 'dew_point': 17.26, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 23, 'wind_gust': 8.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.34, 'feels_like': 24.5, 'pressure': 1012, 'humidity': 64, 'dew_point': 17.1, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 25, 'wind_gust': 9.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.13, 'feels_like': 24.3, 'pressure': 1011, 'humidity': 65, 'dew_point': 17.14, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 35, 'wind_gust': 9.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.04, 'feels_like': 25.19, 'pressure': 1011, 'humidity': 61, 'dew_point': 17, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 33, 'wind_gust': 9.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.3, 'feels_like': 24.43, 'pressure': 1010, 'humidity': 63, 'dew_point': 16.81, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.75, 'wind_deg': 28, 'wind_gust': 8.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.37, 'feels_like': 23.49, 'pressure': 1009, 'humidity': 66, 'dew_point': 16.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 26, 'wind_gust': 8.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 22.92, 'feels_like': 23.02, 'pressure': 1010, 'humidity': 67, 'dew_point': 16.47, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.78, 'wind_deg': 27, 'wind_gust': 8.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 22.74, 'feels_like': 22.79, 'pressure': 1010, 'humidity': 66, 'dew_point': 16.06, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 33, 'wind_gust': 9.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.43, 'feels_like': 22.48, 'pressure': 1011, 'humidity': 67, 'dew_point': 16, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 36, 'wind_gust': 9.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.39, 'feels_like': 23.48, 'pressure': 1012, 'humidity': 65, 'dew_point': 16.44, 'uvi': 0.21, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 38, 'wind_gust': 10.34, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 26.96, 'feels_like': 27.5, 'pressure': 1013, 'humidity': 52, 'dew_point': 16.27, 'uvi': 2.39, 'clouds': 31, 'visibility': 10000, 'wind_speed': 3.29, 'wind_deg': 40, 'wind_gust': 9.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 29.65, 'feels_like': 29.4, 'pressure': 1014, 'humidity': 41, 'dew_point': 15.01, 'uvi': 5.49, 'clouds': 32, 'visibility': 10000, 'wind_speed': 4.09, 'wind_deg': 41, 'wind_gust': 8.41, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 31.38, 'feels_like': 30.83, 'pressure': 1013, 'humidity': 36, 'dew_point': 14.52, 'uvi': 9.11, 'clouds': 50, 'visibility': 10000, 'wind_speed': 4.31, 'wind_deg': 39, 'wind_gust': 7.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 32.43, 'feels_like': 31.72, 'pressure': 1012, 'humidity': 33, 'dew_point': 14.1, 'uvi': 11.3, 'clouds': 56, 'visibility': 10000, 'wind_speed': 4.28, 'wind_deg': 44, 'wind_gust': 6.58, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 33.07, 'feels_like': 32.39, 'pressure': 1011, 'humidity': 32, 'dew_point': 14.18, 'uvi': 12.22, 'clouds': 52, 'visibility': 10000, 'wind_speed': 4.3, 'wind_deg': 48, 'wind_gust': 6.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 33.09, 'feels_like': 32.42, 'pressure': 1010, 'humidity': 32, 'dew_point': 14.2, 'uvi': 11.03, 'clouds': 23, 'visibility': 10000, 'wind_speed': 4.06, 'wind_deg': 48, 'wind_gust': 5.75, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 33.33, 'feels_like': 32.73, 'pressure': 1008, 'humidity': 32, 'dew_point': 14.4, 'uvi': 5.82, 'clouds': 29, 'visibility': 10000, 'wind_speed': 3.46, 'wind_deg': 48, 'wind_gust': 5.06, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 33.22, 'feels_like': 32.75, 'pressure': 1007, 'humidity': 33, 'dew_point': 14.78, 'uvi': 3.38, 'clouds': 35, 'visibility': 10000, 'wind_speed': 3.1, 'wind_deg': 52, 'wind_gust': 4.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 32.65, 'feels_like': 32.16, 'pressure': 1007, 'humidity': 34, 'dew_point': 14.75, 'uvi': 1.38, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.08, 'wind_deg': 54, 'wind_gust': 4.36, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 31.58, 'feels_like': 31.37, 'pressure': 1007, 'humidity': 38, 'dew_point': 15.54, 'uvi': 0.37, 'clouds': 41, 'visibility': 10000, 'wind_speed': 2.75, 'wind_deg': 60, 'wind_gust': 4.53, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 28.92, 'feels_like': 28.8, 'pressure': 1008, 'humidity': 43, 'dew_point': 15.09, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 67, 'wind_gust': 7.5, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 00:00:00 | 84.000000 | 16.850000 | 28.150000 | 52.000000 | 1009.000000 |  | 27.580000 | 0.000000 | 10000.000000 | 23.000000 | 9.68 | 2.320000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 01:00:00 | 96.000000 | 17.040000 | 27.550000 | 55.000000 | 1010.000000 |  | 26.830000 | 0.000000 | 10000.000000 | 21.000000 | 9.66 | 1.990000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 02:00:00 | 97.000000 | 17.070000 | 25.970000 | 58.000000 | 1011.000000 |  | 25.970000 | 0.000000 | 10000.000000 | 20.000000 | 8.33 | 1.700000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 03:00:00 | 98.000000 | 17.260000 | 25.220000 | 62.000000 | 1012.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 23.000000 | 8.51 | 1.620000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 17.100000 | 24.500000 | 64.000000 | 1012.000000 |  | 24.340000 | 0.000000 | 10000.000000 | 25.000000 | 9.3 | 1.660000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 17.140000 | 24.300000 | 65.000000 | 1011.000000 |  | 24.130000 | 0.000000 | 10000.000000 | 35.000000 | 9.85 | 1.740000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 06:00:00 | 99.000000 | 17.000000 | 25.190000 | 61.000000 | 1011.000000 |  | 25.040000 | 0.000000 | 10000.000000 | 33.000000 | 9.34 | 1.870000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 16.810000 | 24.430000 | 63.000000 | 1010.000000 |  | 24.300000 | 0.000000 | 10000.000000 | 28.000000 | 8.38 | 1.750000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 16.660000 | 23.490000 | 66.000000 | 1009.000000 |  | 23.370000 | 0.000000 | 10000.000000 | 26.000000 | 8.67 | 1.800000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 16.470000 | 23.020000 | 67.000000 | 1010.000000 |  | 22.920000 | 0.000000 | 10000.000000 | 27.000000 | 8.94 | 1.780000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 16.060000 | 22.790000 | 66.000000 | 1010.000000 |  | 22.740000 | 0.000000 | 10000.000000 | 33.000000 | 9.02 | 1.790000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 11:00:00 | 96.000000 | 16.000000 | 22.480000 | 67.000000 | 1011.000000 |  | 22.430000 | 0.000000 | 10000.000000 | 36.000000 | 9.23 | 1.790000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 12:00:00 | 26.000000 | 16.440000 | 23.480000 | 65.000000 | 1012.000000 |  | 23.390000 | 0.210000 | 10000.000000 | 38.000000 | 10.34 | 2.040000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 13:00:00 | 31.000000 | 16.270000 | 27.500000 | 52.000000 | 1013.000000 |  | 26.960000 | 2.390000 | 10000.000000 | 40.000000 | 9.98 | 3.290000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 14:00:00 | 32.000000 | 15.010000 | 29.400000 | 41.000000 | 1014.000000 |  | 29.650000 | 5.490000 | 10000.000000 | 41.000000 | 8.41 | 4.090000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 15:00:00 | 50.000000 | 14.520000 | 30.830000 | 36.000000 | 1013.000000 |  | 31.380000 | 9.110000 | 10000.000000 | 39.000000 | 7.26 | 4.310000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 16:00:00 | 56.000000 | 14.100000 | 31.720000 | 33.000000 | 1012.000000 |  | 32.430000 | 11.300000 | 10000.000000 | 44.000000 | 6.58 | 4.280000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 17:00:00 | 52.000000 | 14.180000 | 32.390000 | 32.000000 | 1011.000000 |  | 33.070000 | 12.220000 | 10000.000000 | 48.000000 | 6.13 | 4.300000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 18:00:00 | 23.000000 | 14.200000 | 32.420000 | 32.000000 | 1010.000000 |  | 33.090000 | 11.030000 | 10000.000000 | 48.000000 | 5.75 | 4.060000 | 801 | Clouds | few clouds | 02d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 19:00:00 | 29.000000 | 14.400000 | 32.730000 | 32.000000 | 1008.000000 |  | 33.330000 | 5.820000 | 10000.000000 | 48.000000 | 5.06 | 3.460000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 20:00:00 | 35.000000 | 14.780000 | 32.750000 | 33.000000 | 1007.000000 |  | 33.220000 | 3.380000 | 10000.000000 | 52.000000 | 4.43 | 3.100000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 21:00:00 | 40.000000 | 14.750000 | 32.160000 | 34.000000 | 1007.000000 |  | 32.650000 | 1.380000 | 10000.000000 | 54.000000 | 4.36 | 3.080000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 22:00:00 | 41.000000 | 15.540000 | 31.370000 | 38.000000 | 1007.000000 |  | 31.580000 | 0.370000 | 10000.000000 | 60.000000 | 4.53 | 2.750000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 32035010 | "LA MACARENA [32035010]" | 2.176111 | -73.793333 | 248.000000 | Climática Principal | Convencional | Activa | 1967-10-14 19:00:00 | NaT | Meta | La Macarena | 0 | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Guaviare | Alto Guaviare | America/Bogota | 2022-01-10 23:00:00 | 38.000000 | 15.090000 | 28.800000 | 43.000000 | 1008.000000 |  | 28.920000 | 0.000000 | 10000.000000 | 67.000000 | 7.5 | 2.420000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station32035010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station32035010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station32035010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station32035010_OWM_Windspeed_20220111.png)
