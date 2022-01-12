
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA SIERRA - AUT [24025030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24025030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.96638889,-73.16389139) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.96638889&lon=-73.16389139)


| Parameter | Value |
|---|---|
| Code | 24025030 |
| Name | LA SIERRA - AUT [24025030] |
| Latitude, ° | 5.96638889 |
| Longitude, ° | -73.16389139 |
| Elevation, m | 2700 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1967-02-14 19:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Paipa |
| Stream | 0 |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Suárez |

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

### (CNE index 1019) Open Weather values for station 24025030 - LA SIERRA - AUT [24025030]

JSON data from API OWM:

```
{'lat': 5.9664, 'lon': -73.1639, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812762, 'sunset': 1641855236, 'temp': 16.3, 'feels_like': 15.6, 'pressure': 1011, 'humidity': 62, 'dew_point': 9.01, 'uvi': 3.84, 'clouds': 72, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 320, 'wind_gust': 3.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, 'hourly': [{'dt': 1641772800, 'temp': 9.68, 'feels_like': 9.68, 'pressure': 1017, 'humidity': 98, 'dew_point': 9.38, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 54, 'wind_gust': 1.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 9.23, 'feels_like': 9.23, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.93, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 119, 'wind_gust': 1.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 9.02, 'feels_like': 9.02, 'pressure': 1019, 'humidity': 97, 'dew_point': 8.57, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 125, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.76, 'feels_like': 8.76, 'pressure': 1019, 'humidity': 96, 'dew_point': 8.16, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 121, 'wind_gust': 1.01, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.73, 'feels_like': 8.73, 'pressure': 1019, 'humidity': 95, 'dew_point': 7.97, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 129, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 8.99, 'feels_like': 8.99, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.92, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 148, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 8.51, 'feels_like': 8.51, 'pressure': 1017, 'humidity': 94, 'dew_point': 7.6, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 147, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 8.36, 'feels_like': 8.36, 'pressure': 1016, 'humidity': 94, 'dew_point': 7.45, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 140, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 8.18, 'feels_like': 8.18, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 148, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 8.3, 'feels_like': 8.3, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.24, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 121, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.34, 'feels_like': 8.34, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.12, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 136, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 8.08, 'feels_like': 8.08, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.02, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 142, 'wind_gust': 0.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.83, 'feels_like': 8.83, 'pressure': 1018, 'humidity': 91, 'dew_point': 7.44, 'uvi': 0.57, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 115, 'wind_gust': 0.72, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 11.41, 'feels_like': 10.72, 'pressure': 1019, 'humidity': 81, 'dew_point': 8.27, 'uvi': 2.33, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 334, 'wind_gust': 0.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 13.69, 'feels_like': 12.92, 'pressure': 1018, 'humidity': 69, 'dew_point': 8.11, 'uvi': 5.47, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 315, 'wind_gust': 1.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 15.6, 'feels_like': 14.81, 'pressure': 1017, 'humidity': 61, 'dew_point': 8.11, 'uvi': 9.11, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 315, 'wind_gust': 2.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 16.74, 'feels_like': 15.93, 'pressure': 1016, 'humidity': 56, 'dew_point': 7.93, 'uvi': 11.79, 'clouds': 65, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 315, 'wind_gust': 2.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 17.67, 'feels_like': 16.85, 'pressure': 1015, 'humidity': 52, 'dew_point': 7.7, 'uvi': 12.68, 'clouds': 55, 'visibility': 10000, 'wind_speed': 2.85, 'wind_deg': 315, 'wind_gust': 2.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 18.19, 'feels_like': 17.37, 'pressure': 1013, 'humidity': 50, 'dew_point': 7.61, 'uvi': 11.35, 'clouds': 38, 'visibility': 10000, 'wind_speed': 3.05, 'wind_deg': 318, 'wind_gust': 3.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 18, 'feels_like': 17.21, 'pressure': 1012, 'humidity': 52, 'dew_point': 8.01, 'uvi': 6.78, 'clouds': 53, 'visibility': 10000, 'wind_speed': 3.17, 'wind_deg': 319, 'wind_gust': 3.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 16.3, 'feels_like': 15.6, 'pressure': 1011, 'humidity': 62, 'dew_point': 9.01, 'uvi': 3.84, 'clouds': 72, 'visibility': 10000, 'wind_speed': 3.01, 'wind_deg': 320, 'wind_gust': 3.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641848400, 'temp': 14.02, 'feels_like': 13.54, 'pressure': 1012, 'humidity': 79, 'dew_point': 10.44, 'uvi': 1.5, 'clouds': 81, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 318, 'wind_gust': 2.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641852000, 'temp': 12.68, 'feels_like': 12.33, 'pressure': 1014, 'humidity': 89, 'dew_point': 10.92, 'uvi': 0.36, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 320, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641855600, 'temp': 10.38, 'feels_like': 10.01, 'pressure': 1015, 'humidity': 97, 'dew_point': 9.92, 'uvi': 0, 'clouds': 85, 'visibility': 5299, 'wind_speed': 0.84, 'wind_deg': 320, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 9.380000 | 9.680000 | 98.000000 | 1017.000000 |  | 9.680000 | 0.000000 | 10000.000000 | 54.000000 | 1.07 | 0.180000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 01:00:00 | 45.000000 | 8.930000 | 9.230000 | 98.000000 | 1018.000000 |  | 9.230000 | 0.000000 | 10000.000000 | 119.000000 | 1.13 | 0.230000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 02:00:00 | 54.000000 | 8.570000 | 9.020000 | 97.000000 | 1019.000000 |  | 9.020000 | 0.000000 | 10000.000000 | 125.000000 | 1.11 | 0.340000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 03:00:00 | 65.000000 | 8.160000 | 8.760000 | 96.000000 | 1019.000000 |  | 8.760000 | 0.000000 | 10000.000000 | 121.000000 | 1.01 | 0.510000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 04:00:00 | 66.000000 | 7.970000 | 8.730000 | 95.000000 | 1019.000000 |  | 8.730000 | 0.000000 | 10000.000000 | 129.000000 | 0.97 | 0.650000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 05:00:00 | 67.000000 | 7.920000 | 8.990000 | 93.000000 | 1018.000000 |  | 8.990000 | 0.000000 | 10000.000000 | 148.000000 | 0.8 | 0.580000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 06:00:00 | 58.000000 | 7.600000 | 8.510000 | 94.000000 | 1017.000000 |  | 8.510000 | 0.000000 | 10000.000000 | 147.000000 | 0.78 | 0.630000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 07:00:00 | 83.000000 | 7.450000 | 8.360000 | 94.000000 | 1016.000000 |  | 8.360000 | 0.000000 | 10000.000000 | 140.000000 | 0.75 | 0.510000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 08:00:00 | 75.000000 | 7.120000 | 8.180000 | 93.000000 | 1016.000000 |  | 8.180000 | 0.000000 | 10000.000000 | 148.000000 | 0.8 | 0.360000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 09:00:00 | 74.000000 | 7.240000 | 8.300000 | 93.000000 | 1016.000000 |  | 8.300000 | 0.000000 | 10000.000000 | 121.000000 | 0.89 | 0.320000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 10:00:00 | 76.000000 | 7.120000 | 8.340000 | 92.000000 | 1017.000000 |  | 8.340000 | 0.000000 | 10000.000000 | 136.000000 | 0.83 | 0.350000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 11:00:00 | 76.000000 | 7.020000 | 8.080000 | 93.000000 | 1017.000000 |  | 8.080000 | 0.000000 | 10000.000000 | 142.000000 | 0.61 | 0.370000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 12:00:00 | 31.000000 | 7.440000 | 8.830000 | 91.000000 | 1018.000000 |  | 8.830000 | 0.570000 | 10000.000000 | 115.000000 | 0.72 | 0.240000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 13:00:00 | 59.000000 | 8.270000 | 10.720000 | 81.000000 | 1019.000000 |  | 11.410000 | 2.330000 | 10000.000000 | 334.000000 | 0.68 | 0.530000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 8.110000 | 12.920000 | 69.000000 | 1018.000000 |  | 13.690000 | 5.470000 | 10000.000000 | 315.000000 | 1.12 | 1.410000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 15:00:00 | 71.000000 | 8.110000 | 14.810000 | 61.000000 | 1017.000000 |  | 15.600000 | 9.110000 | 10000.000000 | 315.000000 | 2.32 | 2.170000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 16:00:00 | 65.000000 | 7.930000 | 15.930000 | 56.000000 | 1016.000000 |  | 16.740000 | 11.790000 | 10000.000000 | 315.000000 | 2.63 | 2.540000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 17:00:00 | 55.000000 | 7.700000 | 16.850000 | 52.000000 | 1015.000000 |  | 17.670000 | 12.680000 | 10000.000000 | 315.000000 | 2.88 | 2.850000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 18:00:00 | 38.000000 | 7.610000 | 17.370000 | 50.000000 | 1013.000000 |  | 18.190000 | 11.350000 | 10000.000000 | 318.000000 | 3.05 | 3.050000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 19:00:00 | 53.000000 | 8.010000 | 17.210000 | 52.000000 | 1012.000000 |  | 18.000000 | 6.780000 | 10000.000000 | 319.000000 | 3.06 | 3.170000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 20:00:00 | 72.000000 | 9.010000 | 15.600000 | 62.000000 | 1011.000000 | 0.21 | 16.300000 | 3.840000 | 10000.000000 | 320.000000 | 3.11 | 3.010000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 21:00:00 | 81.000000 | 10.440000 | 13.540000 | 79.000000 | 1012.000000 | 0.47 | 14.020000 | 1.500000 | 10000.000000 | 318.000000 | 2.8 | 2.260000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 22:00:00 | 81.000000 | 10.920000 | 12.330000 | 89.000000 | 1014.000000 | 0.38 | 12.680000 | 0.360000 | 10000.000000 | 320.000000 | 2.06 | 1.590000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24025030 | "LA SIERRA - AUT [24025030]" | 5.966389 | -73.163891 | 2700.000000 | Climática Principal | Automática con Telemetría | Activa | 1967-02-14 19:00:00 | NaT | Boyacá | Paipa | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 9.920000 | 10.010000 | 97.000000 | 1015.000000 | 0.16 | 10.380000 | 0.000000 | 5299.000000 | 320.000000 | 1.21 | 0.840000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24025030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24025030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24025030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24025030_OWM_Windspeed_20220111.png)
