
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNILLANOS [35035070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35035070_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.07672222,-73.582) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.07672222&lon=-73.582)


| Parameter | Value |
|---|---|
| Code | 35035070 |
| Name | UNILLANOS [35035070] |
| Latitude, ° | 4.07672222 |
| Longitude, ° | -73.582 |
| Elevation, m | 340 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1983-10-15 00:00:00 |
| Suspension date | NaT |
| State | Meta |
| County | Villavicencio |
| Stream | Guayuriba |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Negro |

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

### (CNE index 1417) Open Weather values for station 35035070 - UNILLANOS [35035070]

JSON data from API OWM:

```
{'lat': 4.0767, 'lon': -73.582, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812678, 'sunset': 1641855520, 'temp': 30.5, 'feels_like': 30.69, 'pressure': 1009, 'humidity': 43, 'dew_point': 16.51, 'uvi': 4.36, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 80, 'wind_gust': 2.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.54, 'feels_like': 25.72, 'pressure': 1011, 'humidity': 60, 'dew_point': 17.21, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 314, 'wind_gust': 3.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.66, 'feels_like': 25.82, 'pressure': 1012, 'humidity': 59, 'dew_point': 17.05, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 326, 'wind_gust': 2.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.7, 'feels_like': 25.84, 'pressure': 1013, 'humidity': 58, 'dew_point': 16.82, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 337, 'wind_gust': 2.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.6, 'feels_like': 25.7, 'pressure': 1013, 'humidity': 57, 'dew_point': 16.46, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 326, 'wind_gust': 1.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.41, 'feels_like': 25.49, 'pressure': 1014, 'humidity': 57, 'dew_point': 16.28, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 322, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.15, 'feels_like': 25.24, 'pressure': 1013, 'humidity': 58, 'dew_point': 16.31, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 330, 'wind_gust': 2.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.69, 'feels_like': 24.76, 'pressure': 1012, 'humidity': 59, 'dew_point': 16.15, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 320, 'wind_gust': 2.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.57, 'feels_like': 24.65, 'pressure': 1011, 'humidity': 60, 'dew_point': 16.3, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 308, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.5, 'feels_like': 24.57, 'pressure': 1011, 'humidity': 60, 'dew_point': 16.23, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 296, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.24, 'feels_like': 24.31, 'pressure': 1011, 'humidity': 61, 'dew_point': 16.25, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 292, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.23, 'feels_like': 24.28, 'pressure': 1012, 'humidity': 60, 'dew_point': 15.98, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 280, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.96, 'feels_like': 24, 'pressure': 1013, 'humidity': 61, 'dew_point': 15.98, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 276, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.46, 'feels_like': 24.61, 'pressure': 1014, 'humidity': 63, 'dew_point': 16.96, 'uvi': 0.32, 'clouds': 53, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 15, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.19, 'feels_like': 26.19, 'pressure': 1015, 'humidity': 56, 'dew_point': 16.73, 'uvi': 2.48, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 86, 'wind_gust': 3.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.87, 'feels_like': 28.22, 'pressure': 1016, 'humidity': 49, 'dew_point': 16.18, 'uvi': 5.81, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 78, 'wind_gust': 4.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 28.74, 'feels_like': 28.9, 'pressure': 1015, 'humidity': 46, 'dew_point': 15.98, 'uvi': 9.71, 'clouds': 50, 'visibility': 10000, 'wind_speed': 4.02, 'wind_deg': 76, 'wind_gust': 4.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 29.35, 'feels_like': 29.5, 'pressure': 1014, 'humidity': 45, 'dew_point': 16.19, 'uvi': 11.23, 'clouds': 49, 'visibility': 10000, 'wind_speed': 4.14, 'wind_deg': 73, 'wind_gust': 4.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 29.9, 'feels_like': 29.93, 'pressure': 1013, 'humidity': 43, 'dew_point': 15.97, 'uvi': 12.15, 'clouds': 49, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 68, 'wind_gust': 3.34, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 30.48, 'feels_like': 30.67, 'pressure': 1012, 'humidity': 43, 'dew_point': 16.49, 'uvi': 10.96, 'clouds': 55, 'visibility': 10000, 'wind_speed': 2.68, 'wind_deg': 70, 'wind_gust': 2.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 30.86, 'feels_like': 31.02, 'pressure': 1010, 'humidity': 42, 'dew_point': 16.47, 'uvi': 7.56, 'clouds': 73, 'visibility': 10000, 'wind_speed': 2.32, 'wind_deg': 74, 'wind_gust': 2.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.5, 'feels_like': 30.69, 'pressure': 1009, 'humidity': 43, 'dew_point': 16.51, 'uvi': 4.36, 'clouds': 77, 'visibility': 10000, 'wind_speed': 2.01, 'wind_deg': 80, 'wind_gust': 2.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.6, 'feels_like': 29.93, 'pressure': 1009, 'humidity': 46, 'dew_point': 16.76, 'uvi': 1.73, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 66, 'wind_gust': 2.45, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.23, 'feels_like': 28.81, 'pressure': 1010, 'humidity': 51, 'dew_point': 17.14, 'uvi': 0.32, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 33, 'wind_gust': 3.26, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 26.76, 'feels_like': 27.48, 'pressure': 1010, 'humidity': 55, 'dew_point': 16.97, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 350, 'wind_gust': 3.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 00:00:00 | 98.000000 | 17.210000 | 25.720000 | 60.000000 | 1011.000000 |  | 25.540000 | 0.000000 | 10000.000000 | 314.000000 | 3.69 | 2.100000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 17.050000 | 25.820000 | 59.000000 | 1012.000000 |  | 25.660000 | 0.000000 | 10000.000000 | 326.000000 | 2.72 | 1.700000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 16.820000 | 25.840000 | 58.000000 | 1013.000000 |  | 25.700000 | 0.000000 | 10000.000000 | 337.000000 | 2.18 | 1.560000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 16.460000 | 25.700000 | 57.000000 | 1013.000000 |  | 25.600000 | 0.000000 | 10000.000000 | 326.000000 | 1.82 | 1.520000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 16.280000 | 25.490000 | 57.000000 | 1014.000000 |  | 25.410000 | 0.000000 | 10000.000000 | 322.000000 | 1.74 | 1.430000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 16.310000 | 25.240000 | 58.000000 | 1013.000000 |  | 25.150000 | 0.000000 | 10000.000000 | 330.000000 | 2.19 | 1.610000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 06:00:00 | 94.000000 | 16.150000 | 24.760000 | 59.000000 | 1012.000000 |  | 24.690000 | 0.000000 | 10000.000000 | 320.000000 | 2.09 | 1.640000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 16.300000 | 24.650000 | 60.000000 | 1011.000000 |  | 24.570000 | 0.000000 | 10000.000000 | 308.000000 | 1.46 | 1.340000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 16.230000 | 24.570000 | 60.000000 | 1011.000000 |  | 24.500000 | 0.000000 | 10000.000000 | 296.000000 | 1.14 | 1.160000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 16.250000 | 24.310000 | 61.000000 | 1011.000000 |  | 24.240000 | 0.000000 | 10000.000000 | 292.000000 | 1.03 | 1.110000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 15.980000 | 24.280000 | 60.000000 | 1012.000000 |  | 24.230000 | 0.000000 | 10000.000000 | 280.000000 | 0.78 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 15.980000 | 24.000000 | 61.000000 | 1013.000000 |  | 23.960000 | 0.000000 | 10000.000000 | 276.000000 | 0.75 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 12:00:00 | 53.000000 | 16.960000 | 24.610000 | 63.000000 | 1014.000000 |  | 24.460000 | 0.320000 | 10000.000000 | 15.000000 | 0.9 | 0.170000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 13:00:00 | 72.000000 | 16.730000 | 26.190000 | 56.000000 | 1015.000000 |  | 26.190000 | 2.480000 | 10000.000000 | 86.000000 | 3.83 | 1.180000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 14:00:00 | 52.000000 | 16.180000 | 28.220000 | 49.000000 | 1016.000000 |  | 27.870000 | 5.810000 | 10000.000000 | 78.000000 | 4.2 | 2.780000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 15:00:00 | 50.000000 | 15.980000 | 28.900000 | 46.000000 | 1015.000000 |  | 28.740000 | 9.710000 | 10000.000000 | 76.000000 | 4.45 | 4.020000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 16:00:00 | 49.000000 | 16.190000 | 29.500000 | 45.000000 | 1014.000000 |  | 29.350000 | 11.230000 | 10000.000000 | 73.000000 | 4.02 | 4.140000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 17:00:00 | 49.000000 | 15.970000 | 29.930000 | 43.000000 | 1013.000000 |  | 29.900000 | 12.150000 | 10000.000000 | 68.000000 | 3.34 | 3.280000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 18:00:00 | 55.000000 | 16.490000 | 30.670000 | 43.000000 | 1012.000000 |  | 30.480000 | 10.960000 | 10000.000000 | 70.000000 | 2.86 | 2.680000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 19:00:00 | 73.000000 | 16.470000 | 31.020000 | 42.000000 | 1010.000000 |  | 30.860000 | 7.560000 | 10000.000000 | 74.000000 | 2.52 | 2.320000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 20:00:00 | 77.000000 | 16.510000 | 30.690000 | 43.000000 | 1009.000000 |  | 30.500000 | 4.360000 | 10000.000000 | 80.000000 | 2.42 | 2.010000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 21:00:00 | 78.000000 | 16.760000 | 29.930000 | 46.000000 | 1009.000000 |  | 29.600000 | 1.730000 | 10000.000000 | 66.000000 | 2.45 | 1.650000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 22:00:00 | 83.000000 | 17.140000 | 28.810000 | 51.000000 | 1010.000000 |  | 28.230000 | 0.320000 | 10000.000000 | 33.000000 | 3.26 | 1.330000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35035070 | "UNILLANOS [35035070]" | 4.076722 | -73.582000 | 340.000000 | Climática Principal | Convencional | Activa | 1983-10-15 00:00:00 | NaT | Meta | Villavicencio | Guayuriba | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 23:00:00 | 86.000000 | 16.970000 | 27.480000 | 55.000000 | 1010.000000 |  | 26.760000 | 0.000000 | 10000.000000 | 350.000000 | 3.12 | 1.430000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35035070_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35035070_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35035070_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35035070_OWM_Windspeed_20220111.png)
