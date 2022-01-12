
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MEREY EL [38015020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station38015020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.16666667,-67.53333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.16666667&lon=-67.53333333)


| Parameter | Value |
|---|---|
| Code | 38015020 |
| Name | MEREY EL [38015020] |
| Latitude, ° | 6.16666667 |
| Longitude, ° | -67.53333333 |
| Elevation, m | 55 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-01-15 00:00:00 |
| Suspension date | 1972-05-15 00:00:00 |
| State | Vichada |
| County | Puerto Carreño |
| Stream | Minero |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Orinoco Directos |
| SZH - Hydrographic subzone | Río Vita |

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

### (CNE index 751) Open Weather values for station 38015020 - MEREY EL [38015020]

JSON data from API OWM:

```
{'lat': 6.1667, 'lon': -67.5333, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641811429, 'sunset': 1641853865, 'temp': 33.09, 'feels_like': 33.93, 'pressure': 1008, 'humidity': 40, 'dew_point': 17.69, 'uvi': 3.15, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 350, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 30.09, 'feels_like': 30.87, 'pressure': 1010, 'humidity': 48, 'dew_point': 17.88, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 26.89, 'feels_like': 26.88, 'pressure': 1011, 'humidity': 42, 'dew_point': 12.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.56, 'wind_deg': 16, 'wind_gust': 10.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.96, 'feels_like': 25.96, 'pressure': 1011, 'humidity': 45, 'dew_point': 13.12, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 22, 'wind_gust': 9.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.22, 'feels_like': 25.05, 'pressure': 1011, 'humidity': 48, 'dew_point': 13.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.86, 'wind_deg': 29, 'wind_gust': 9.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 24.53, 'feels_like': 24.34, 'pressure': 1011, 'humidity': 50, 'dew_point': 13.43, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.44, 'wind_deg': 41, 'wind_gust': 7.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 23.87, 'feels_like': 23.67, 'pressure': 1010, 'humidity': 52, 'dew_point': 13.43, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.19, 'wind_deg': 41, 'wind_gust': 5.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 23.33, 'feels_like': 23.15, 'pressure': 1010, 'humidity': 55, 'dew_point': 13.79, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 5.08, 'wind_deg': 18, 'wind_gust': 9.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 23.3, 'feels_like': 23.1, 'pressure': 1010, 'humidity': 54, 'dew_point': 13.48, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 5.56, 'wind_deg': 30, 'wind_gust': 13.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 22.64, 'feels_like': 22.5, 'pressure': 1010, 'humidity': 59, 'dew_point': 14.23, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 4.99, 'wind_deg': 29, 'wind_gust': 12.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 22.18, 'feels_like': 22.1, 'pressure': 1010, 'humidity': 63, 'dew_point': 14.81, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 4.61, 'wind_deg': 27, 'wind_gust': 11.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 21.75, 'feels_like': 21.76, 'pressure': 1011, 'humidity': 68, 'dew_point': 15.59, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 4.17, 'wind_deg': 28, 'wind_gust': 10.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.09, 'feels_like': 23.49, 'pressure': 1011, 'humidity': 78, 'dew_point': 19.05, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 40, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641816000, 'temp': 24.09, 'feels_like': 24.59, 'pressure': 1013, 'humidity': 78, 'dew_point': 20.02, 'uvi': 0.93, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.4, 'wind_deg': 35, 'wind_gust': 10.72, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 26.09, 'feels_like': 26.09, 'pressure': 1014, 'humidity': 73, 'dew_point': 20.87, 'uvi': 2.92, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641823200, 'temp': 28.09, 'feels_like': 29.7, 'pressure': 1014, 'humidity': 61, 'dew_point': 19.86, 'uvi': 5.97, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 60, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641826800, 'temp': 29.09, 'feels_like': 30.88, 'pressure': 1014, 'humidity': 58, 'dew_point': 19.99, 'uvi': 9.03, 'clouds': 0, 'visibility': 10000, 'wind_speed': 7.72, 'wind_deg': 50, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641830400, 'temp': 31.09, 'feels_like': 32.97, 'pressure': 1013, 'humidity': 51, 'dew_point': 19.76, 'uvi': 11.03, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 50, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641834000, 'temp': 32.09, 'feels_like': 33.39, 'pressure': 1011, 'humidity': 45, 'dew_point': 18.66, 'uvi': 11.09, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 33.09, 'feels_like': 34.61, 'pressure': 1010, 'humidity': 43, 'dew_point': 18.84, 'uvi': 9.25, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641841200, 'temp': 33.09, 'feels_like': 34.61, 'pressure': 1009, 'humidity': 43, 'dew_point': 18.84, 'uvi': 6.25, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 10, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 33.09, 'feels_like': 33.93, 'pressure': 1008, 'humidity': 40, 'dew_point': 17.69, 'uvi': 3.15, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 350, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641848400, 'temp': 33.09, 'feels_like': 33.93, 'pressure': 1008, 'humidity': 40, 'dew_point': 17.69, 'uvi': 1.01, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 350, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641852000, 'temp': 33.09, 'feels_like': 33.93, 'pressure': 1009, 'humidity': 40, 'dew_point': 17.69, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 360, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641855600, 'temp': 31.09, 'feels_like': 32.38, 'pressure': 1009, 'humidity': 48, 'dew_point': 18.79, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 10, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 17.880000 | 30.870000 | 48.000000 | 1010.000000 |  | 30.090000 | 0.000000 | 10000.000000 | 30.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 12.910000 | 26.880000 | 42.000000 | 1011.000000 |  | 26.890000 | 0.000000 | 10000.000000 | 16.000000 | 10.36 | 4.560000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 13.120000 | 25.960000 | 45.000000 | 1011.000000 |  | 25.960000 | 0.000000 | 10000.000000 | 22.000000 | 9.32 | 4.120000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 13.440000 | 25.050000 | 48.000000 | 1011.000000 |  | 25.220000 | 0.000000 | 10000.000000 | 29.000000 | 9.41 | 3.860000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 13.430000 | 24.340000 | 50.000000 | 1011.000000 |  | 24.530000 | 0.000000 | 10000.000000 | 41.000000 | 7.51 | 3.440000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 13.430000 | 23.670000 | 52.000000 | 1010.000000 |  | 23.870000 | 0.000000 | 10000.000000 | 41.000000 | 5.54 | 3.190000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 06:00:00 | 72.000000 | 13.790000 | 23.150000 | 55.000000 | 1010.000000 |  | 23.330000 | 0.000000 | 10000.000000 | 18.000000 | 9.38 | 5.080000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 07:00:00 | 79.000000 | 13.480000 | 23.100000 | 54.000000 | 1010.000000 |  | 23.300000 | 0.000000 | 10000.000000 | 30.000000 | 13.16 | 5.560000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 08:00:00 | 65.000000 | 14.230000 | 22.500000 | 59.000000 | 1010.000000 |  | 22.640000 | 0.000000 | 10000.000000 | 29.000000 | 12.82 | 4.990000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 09:00:00 | 71.000000 | 14.810000 | 22.100000 | 63.000000 | 1010.000000 |  | 22.180000 | 0.000000 | 10000.000000 | 27.000000 | 11.84 | 4.610000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 10:00:00 | 74.000000 | 15.590000 | 21.760000 | 68.000000 | 1011.000000 |  | 21.750000 | 0.000000 | 10000.000000 | 28.000000 | 10.85 | 4.170000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 11:00:00 | 0.000000 | 19.050000 | 23.490000 | 78.000000 | 1011.000000 |  | 23.090000 | 0.000000 | 10000.000000 | 40.000000 |  | 2.060000 | 800 | Clear | clear sky | 01d | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 12:00:00 | 0.000000 | 20.020000 | 24.590000 | 78.000000 | 1013.000000 |  | 24.090000 | 0.930000 | 10000.000000 | 35.000000 | 10.72 | 5.400000 | 800 | Clear | clear sky | 01d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 13:00:00 | 0.000000 | 20.870000 | 26.090000 | 73.000000 | 1014.000000 |  | 26.090000 | 2.920000 | 10000.000000 | 40.000000 |  | 3.600000 | 800 | Clear | clear sky | 01d | 13 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 14:00:00 | 0.000000 | 19.860000 | 29.700000 | 61.000000 | 1014.000000 |  | 28.090000 | 5.970000 | 10000.000000 | 60.000000 |  | 4.630000 | 800 | Clear | clear sky | 01d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 15:00:00 | 0.000000 | 19.990000 | 30.880000 | 58.000000 | 1014.000000 |  | 29.090000 | 9.030000 | 10000.000000 | 50.000000 |  | 7.720000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 16:00:00 | 0.000000 | 19.760000 | 32.970000 | 51.000000 | 1013.000000 |  | 31.090000 | 11.030000 | 10000.000000 | 50.000000 |  | 3.090000 | 800 | Clear | clear sky | 01d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 17:00:00 | 20.000000 | 18.660000 | 33.390000 | 45.000000 | 1011.000000 |  | 32.090000 | 11.090000 | 10000.000000 | 60.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 18:00:00 | 20.000000 | 18.840000 | 34.610000 | 43.000000 | 1010.000000 |  | 33.090000 | 9.250000 | 10000.000000 | 40.000000 |  | 5.660000 | 801 | Clouds | few clouds | 02d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 19:00:00 | 20.000000 | 18.840000 | 34.610000 | 43.000000 | 1009.000000 |  | 33.090000 | 6.250000 | 10000.000000 | 10.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 20:00:00 | 20.000000 | 17.690000 | 33.930000 | 40.000000 | 1008.000000 |  | 33.090000 | 3.150000 | 10000.000000 | 350.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 20 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 21:00:00 | 20.000000 | 17.690000 | 33.930000 | 40.000000 | 1008.000000 |  | 33.090000 | 1.010000 | 10000.000000 | 350.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02d | 21 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 22:00:00 | 20.000000 | 17.690000 | 33.930000 | 40.000000 | 1009.000000 |  | 33.090000 | 0.000000 | 10000.000000 | 360.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 22 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 38015020 | "MEREY EL [38015020]" | 6.166667 | -67.533333 | 55.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1972-05-15 00:00:00 | Vichada | Puerto Carreño | Minero | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Orinoco Directos | Río Vita | America/Bogota | 2022-01-10 23:00:00 | 20.000000 | 18.790000 | 32.380000 | 48.000000 | 1009.000000 |  | 31.090000 | 0.000000 | 10000.000000 | 10.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02n | 23 |


### Weather plots

![CNE_IDEAM_Station38015020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station38015020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station38015020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station38015020_OWM_Windspeed_20220111.png)
