
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - HUERTA LA GRANDE [35095110] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35095110_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.65508333,-72.91733333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.65508333&lon=-72.91733333)


| Parameter | Value |
|---|---|
| Code | 35095110 |
| Name | HUERTA LA GRANDE [35095110] |
| Latitude, ° | 4.65508333 |
| Longitude, ° | -72.91733333 |
| Elevation, m | 255 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1994-09-15 00:00:00 |
| Suspension date | NaT |
| State | Casanare |
| County | Villanueva (Casanare) |
| Stream | Seco |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Túa y otros directos al Meta |

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

### (CNE index 2238) Open Weather values for station 35095110 - HUERTA LA GRANDE [35095110]

JSON data from API OWM:

```
{'lat': 4.6551, 'lon': -72.9173, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812575, 'sunset': 1641855304, 'temp': 31.79, 'feels_like': 31.2, 'pressure': 1008, 'humidity': 35, 'dew_point': 14.45, 'uvi': 2.12, 'clouds': 80, 'visibility': 10000, 'wind_speed': 3.44, 'wind_deg': 70, 'wind_gust': 4.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.24, 'feels_like': 27.39, 'pressure': 1010, 'humidity': 46, 'dew_point': 14.62, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 48, 'wind_gust': 4.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.88, 'feels_like': 27.14, 'pressure': 1011, 'humidity': 47, 'dew_point': 14.63, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 47, 'wind_gust': 5.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.69, 'feels_like': 26.98, 'pressure': 1012, 'humidity': 47, 'dew_point': 14.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 37, 'wind_gust': 5.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1012, 'humidity': 49, 'dew_point': 14.43, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 35, 'wind_gust': 5.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.05, 'feels_like': 24.97, 'pressure': 1012, 'humidity': 52, 'dew_point': 14.52, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 11, 'wind_gust': 4.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 24.3, 'feels_like': 24.22, 'pressure': 1012, 'humidity': 55, 'dew_point': 14.69, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 340, 'wind_gust': 2.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.92, 'feels_like': 23.86, 'pressure': 1011, 'humidity': 57, 'dew_point': 14.89, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 335, 'wind_gust': 1.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.28, 'feels_like': 23.2, 'pressure': 1010, 'humidity': 59, 'dew_point': 14.83, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 339, 'wind_gust': 1.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 23.61, 'feels_like': 23.54, 'pressure': 1010, 'humidity': 58, 'dew_point': 14.87, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 360, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.53, 'feels_like': 23.48, 'pressure': 1010, 'humidity': 59, 'dew_point': 15.06, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 15, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.56, 'feels_like': 23.51, 'pressure': 1011, 'humidity': 59, 'dew_point': 15.09, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 30, 'wind_gust': 1.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.14, 'feels_like': 23.08, 'pressure': 1012, 'humidity': 60, 'dew_point': 14.96, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 41, 'wind_gust': 1.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.23, 'feels_like': 24.22, 'pressure': 1013, 'humidity': 58, 'dew_point': 15.45, 'uvi': 0.37, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 45, 'wind_gust': 3.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.45, 'feels_like': 25.46, 'pressure': 1014, 'humidity': 54, 'dew_point': 15.47, 'uvi': 1.76, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.79, 'wind_deg': 57, 'wind_gust': 4.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.63, 'feels_like': 26.63, 'pressure': 1015, 'humidity': 49, 'dew_point': 15.04, 'uvi': 4.01, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.59, 'wind_deg': 53, 'wind_gust': 5.85, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.29, 'feels_like': 27.5, 'pressure': 1015, 'humidity': 47, 'dew_point': 15, 'uvi': 6.6, 'clouds': 91, 'visibility': 10000, 'wind_speed': 3.34, 'wind_deg': 51, 'wind_gust': 6.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.37, 'feels_like': 28.99, 'pressure': 1014, 'humidity': 40, 'dew_point': 14.37, 'uvi': 7.13, 'clouds': 88, 'visibility': 10000, 'wind_speed': 4.27, 'wind_deg': 55, 'wind_gust': 5.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 31.74, 'feels_like': 31.14, 'pressure': 1012, 'humidity': 35, 'dew_point': 14.4, 'uvi': 7.62, 'clouds': 85, 'visibility': 10000, 'wind_speed': 3.99, 'wind_deg': 62, 'wind_gust': 4.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 32.17, 'feels_like': 31.69, 'pressure': 1011, 'humidity': 35, 'dew_point': 14.78, 'uvi': 6.78, 'clouds': 55, 'visibility': 10000, 'wind_speed': 3.84, 'wind_deg': 65, 'wind_gust': 4.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 32.61, 'feels_like': 32.1, 'pressure': 1009, 'humidity': 34, 'dew_point': 14.72, 'uvi': 3.76, 'clouds': 66, 'visibility': 10000, 'wind_speed': 3.63, 'wind_deg': 69, 'wind_gust': 3.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 31.79, 'feels_like': 31.2, 'pressure': 1008, 'humidity': 35, 'dew_point': 14.45, 'uvi': 2.12, 'clouds': 80, 'visibility': 10000, 'wind_speed': 3.44, 'wind_deg': 70, 'wind_gust': 4.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.57, 'feels_like': 30.24, 'pressure': 1008, 'humidity': 39, 'dew_point': 15.05, 'uvi': 0.83, 'clouds': 86, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 76, 'wind_gust': 4.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.33, 'feels_like': 29.15, 'pressure': 1008, 'humidity': 42, 'dew_point': 15.09, 'uvi': 0.12, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 72, 'wind_gust': 2.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.94, 'feels_like': 27.97, 'pressure': 1009, 'humidity': 45, 'dew_point': 14.91, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 54, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 00:00:00 | 95.000000 | 14.620000 | 27.390000 | 46.000000 | 1010.000000 |  | 27.240000 | 0.000000 | 10000.000000 | 48.000000 | 4.78 | 1.840000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 14.630000 | 27.140000 | 47.000000 | 1011.000000 |  | 26.880000 | 0.000000 | 10000.000000 | 47.000000 | 5.22 | 1.940000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 14.450000 | 26.980000 | 47.000000 | 1012.000000 |  | 26.690000 | 0.000000 | 10000.000000 | 37.000000 | 5.87 | 2.260000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 03:00:00 | 97.000000 | 14.430000 | 25.960000 | 49.000000 | 1012.000000 |  | 25.960000 | 0.000000 | 10000.000000 | 35.000000 | 5.97 | 2.250000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 14.520000 | 24.970000 | 52.000000 | 1012.000000 |  | 25.050000 | 0.000000 | 10000.000000 | 11.000000 | 4.4 | 1.700000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | 14.690000 | 24.220000 | 55.000000 | 1012.000000 |  | 24.300000 | 0.000000 | 10000.000000 | 340.000000 | 2.72 | 1.380000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 06:00:00 | 59.000000 | 14.890000 | 23.860000 | 57.000000 | 1011.000000 |  | 23.920000 | 0.000000 | 10000.000000 | 335.000000 | 1.46 | 1.070000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 14.830000 | 23.200000 | 59.000000 | 1010.000000 |  | 23.280000 | 0.000000 | 10000.000000 | 339.000000 | 1.17 | 1.040000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 08:00:00 | 87.000000 | 14.870000 | 23.540000 | 58.000000 | 1010.000000 |  | 23.610000 | 0.000000 | 10000.000000 | 360.000000 | 1.17 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 09:00:00 | 92.000000 | 15.060000 | 23.480000 | 59.000000 | 1010.000000 |  | 23.530000 | 0.000000 | 10000.000000 | 15.000000 | 1.46 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 10:00:00 | 94.000000 | 15.090000 | 23.510000 | 59.000000 | 1011.000000 |  | 23.560000 | 0.000000 | 10000.000000 | 30.000000 | 1.73 | 0.700000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 11:00:00 | 95.000000 | 14.960000 | 23.080000 | 60.000000 | 1012.000000 |  | 23.140000 | 0.000000 | 10000.000000 | 41.000000 | 1.45 | 0.800000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 12:00:00 | 79.000000 | 15.450000 | 24.220000 | 58.000000 | 1013.000000 |  | 24.230000 | 0.370000 | 10000.000000 | 45.000000 | 3.11 | 0.900000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 13:00:00 | 92.000000 | 15.470000 | 25.460000 | 54.000000 | 1014.000000 |  | 25.450000 | 1.760000 | 10000.000000 | 57.000000 | 4.6 | 1.790000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 14:00:00 | 90.000000 | 15.040000 | 26.630000 | 49.000000 | 1015.000000 |  | 26.630000 | 4.010000 | 10000.000000 | 53.000000 | 5.85 | 2.590000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 15:00:00 | 91.000000 | 15.000000 | 27.500000 | 47.000000 | 1015.000000 |  | 27.290000 | 6.600000 | 10000.000000 | 51.000000 | 6.18 | 3.340000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 14.370000 | 28.990000 | 40.000000 | 1014.000000 |  | 29.370000 | 7.130000 | 10000.000000 | 55.000000 | 5.5 | 4.270000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 17:00:00 | 85.000000 | 14.400000 | 31.140000 | 35.000000 | 1012.000000 |  | 31.740000 | 7.620000 | 10000.000000 | 62.000000 | 4.38 | 3.990000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 18:00:00 | 55.000000 | 14.780000 | 31.690000 | 35.000000 | 1011.000000 |  | 32.170000 | 6.780000 | 10000.000000 | 65.000000 | 4.17 | 3.840000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 19:00:00 | 66.000000 | 14.720000 | 32.100000 | 34.000000 | 1009.000000 |  | 32.610000 | 3.760000 | 10000.000000 | 69.000000 | 3.72 | 3.630000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 20:00:00 | 80.000000 | 14.450000 | 31.200000 | 35.000000 | 1008.000000 |  | 31.790000 | 2.120000 | 10000.000000 | 70.000000 | 4.13 | 3.440000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 21:00:00 | 86.000000 | 15.050000 | 30.240000 | 39.000000 | 1008.000000 |  | 30.570000 | 0.830000 | 10000.000000 | 76.000000 | 4.46 | 2.650000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 22:00:00 | 90.000000 | 15.090000 | 29.150000 | 42.000000 | 1008.000000 |  | 29.330000 | 0.120000 | 10000.000000 | 72.000000 | 2.68 | 1.740000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35095110 | "HUERTA LA GRANDE [35095110]" | 4.655083 | -72.917333 | 255.000000 | Climática Principal | Convencional | Activa | 1994-09-15 00:00:00 | NaT | Casanare | Villanueva (Casanare) | Seco | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Túa y otros directos al Meta | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 14.910000 | 27.970000 | 45.000000 | 1009.000000 |  | 27.940000 | 0.000000 | 10000.000000 | 54.000000 | 1.67 | 0.960000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35095110_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35095110_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35095110_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35095110_OWM_Windspeed_20220111.png)
