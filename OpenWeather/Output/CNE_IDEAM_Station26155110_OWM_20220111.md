
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO LA NUBIA [26155110] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26155110_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.02977778,-75.46991667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.02977778&lon=-75.46991667)


| Parameter | Value |
|---|---|
| Code | 26155110 |
| Name | AEROPUERTO LA NUBIA [26155110] |
| Latitude, ° | 5.02977778 |
| Longitude, ° | -75.46991667 |
| Elevation, m | 2104 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1968-06-15 00:00:00 |
| Suspension date | NaT |
| State | Caldas |
| County | Manizales |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Chinchiná |

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

### (CNE index 259) Open Weather values for station 26155110 - AEROPUERTO LA NUBIA [26155110]

JSON data from API OWM:

```
{'lat': 5.0298, 'lon': -75.4699, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813224, 'sunset': 1641855881, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.1, 'uvi': 4.7, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.43}}, 'hourly': [{'dt': 1641772800, 'temp': 17.17, 'feels_like': 17.5, 'pressure': 1017, 'humidity': 98, 'dew_point': 16.85, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 104, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.59}}, {'dt': 1641776400, 'temp': 17.17, 'feels_like': 17.45, 'pressure': 1018, 'humidity': 96, 'dew_point': 16.53, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 102, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 16.17, 'feels_like': 16.35, 'pressure': 1019, 'humidity': 96, 'dew_point': 15.53, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 109, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641783600, 'temp': 16.17, 'feels_like': 16.35, 'pressure': 1019, 'humidity': 96, 'dew_point': 15.53, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 114, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 15.17, 'feels_like': 15.25, 'pressure': 1018, 'humidity': 96, 'dew_point': 14.54, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 123, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 15.17, 'feels_like': 15.28, 'pressure': 1018, 'humidity': 97, 'dew_point': 14.7, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 130, 'wind_gust': 0.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.17, 'feels_like': 15.3, 'pressure': 1017, 'humidity': 98, 'dew_point': 14.86, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 152, 'wind_gust': 0.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 15.17, 'feels_like': 15.3, 'pressure': 1017, 'humidity': 98, 'dew_point': 14.86, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 129, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641801600, 'temp': 13.13, 'feels_like': 13.06, 'pressure': 1016, 'humidity': 98, 'dew_point': 12.82, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 154, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641805200, 'temp': 13.47, 'feels_like': 13.41, 'pressure': 1016, 'humidity': 97, 'dew_point': 13, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 173, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 14.17, 'feels_like': 14.18, 'pressure': 1017, 'humidity': 97, 'dew_point': 13.7, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 193, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641812400, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.1, 'uvi': 0, 'clouds': 75, 'visibility': 2000, 'wind_speed': 1.54, 'wind_deg': 120, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09n'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.1, 'uvi': 0.13, 'clouds': 75, 'visibility': 2000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1027, 'humidity': 100, 'dew_point': 14.1, 'uvi': 1.27, 'clouds': 75, 'visibility': 3000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 15.1, 'feels_like': 15.28, 'pressure': 1028, 'humidity': 100, 'dew_point': 15.1, 'uvi': 3.19, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641826800, 'temp': 17.1, 'feels_like': 17.32, 'pressure': 1028, 'humidity': 94, 'dew_point': 16.13, 'uvi': 5.5, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641830400, 'temp': 20.1, 'feels_like': 20.18, 'pressure': 1027, 'humidity': 77, 'dew_point': 15.95, 'uvi': 10.61, 'clouds': 75, 'visibility': 7000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641834000, 'temp': 17.1, 'feels_like': 17.32, 'pressure': 1027, 'humidity': 94, 'dew_point': 16.13, 'uvi': 11.7, 'clouds': 75, 'visibility': 6000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641837600, 'temp': 15.1, 'feels_like': 15.28, 'pressure': 1027, 'humidity': 100, 'dew_point': 15.1, 'uvi': 10.74, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.7}}, {'dt': 1641841200, 'temp': 15.1, 'feels_like': 15.28, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.1, 'uvi': 7.94, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.57}}, {'dt': 1641844800, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.1, 'uvi': 4.7, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.43}}, {'dt': 1641848400, 'temp': 15.1, 'feels_like': 15.28, 'pressure': 1025, 'humidity': 100, 'dew_point': 15.1, 'uvi': 1.94, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641852000, 'temp': 15.1, 'feels_like': 15.28, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.1, 'uvi': 0.43, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641855600, 'temp': 14.1, 'feels_like': 14.18, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.1, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 00:00:00 | 65.000000 | 16.850000 | 17.500000 | 98.000000 | 1017.000000 | 0.59 | 17.170000 | 0.000000 | 10000.000000 | 104.000000 | 1.43 | 1.550000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 01:00:00 | 93.000000 | 16.530000 | 17.450000 | 96.000000 | 1018.000000 |  | 17.170000 | 0.000000 | 10000.000000 | 102.000000 | 1.32 | 1.550000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 02:00:00 | 88.000000 | 15.530000 | 16.350000 | 96.000000 | 1019.000000 | 0.28 | 16.170000 | 0.000000 | 10000.000000 | 109.000000 | 1.18 | 1.380000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 03:00:00 | 85.000000 | 15.530000 | 16.350000 | 96.000000 | 1019.000000 |  | 16.170000 | 0.000000 | 10000.000000 | 114.000000 | 0.88 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 14.540000 | 15.250000 | 96.000000 | 1018.000000 |  | 15.170000 | 0.000000 | 10000.000000 | 123.000000 | 0.74 | 0.800000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 05:00:00 | 82.000000 | 14.700000 | 15.280000 | 97.000000 | 1018.000000 |  | 15.170000 | 0.000000 | 10000.000000 | 130.000000 | 0.63 | 0.670000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 06:00:00 | 47.000000 | 14.860000 | 15.300000 | 98.000000 | 1017.000000 |  | 15.170000 | 0.000000 | 10000.000000 | 152.000000 | 0.57 | 0.580000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 07:00:00 | 82.000000 | 14.860000 | 15.300000 | 98.000000 | 1017.000000 | 0.11 | 15.170000 | 0.000000 | 10000.000000 | 129.000000 | 0.8 | 0.910000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 12.820000 | 13.060000 | 98.000000 | 1016.000000 | 0.17 | 13.130000 | 0.000000 | 10000.000000 | 154.000000 | 0.74 | 0.640000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 09:00:00 | 89.000000 | 13.000000 | 13.410000 | 97.000000 | 1016.000000 | 0.18 | 13.470000 | 0.000000 | 10000.000000 | 173.000000 | 0.7 | 0.450000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 10:00:00 | 92.000000 | 13.700000 | 14.180000 | 97.000000 | 1017.000000 | 0.11 | 14.170000 | 0.000000 | 10000.000000 | 193.000000 | 0.91 | 0.540000 | 500 | Rain | light rain | 10n | 10 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 14.100000 | 14.180000 | 100.000000 | 1026.000000 |  | 14.100000 | 0.000000 | 2000.000000 | 120.000000 |  | 1.540000 | 301 | Drizzle | drizzle | 09n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 14.100000 | 14.180000 | 100.000000 | 1026.000000 |  | 14.100000 | 0.130000 | 2000.000000 | 290.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 12 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 14.100000 | 14.180000 | 100.000000 | 1027.000000 |  | 14.100000 | 1.270000 | 3000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 13 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 15.100000 | 15.280000 | 100.000000 | 1028.000000 |  | 15.100000 | 3.190000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 14 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 16.130000 | 17.320000 | 94.000000 | 1028.000000 |  | 17.100000 | 5.500000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 15 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 15.950000 | 20.180000 | 77.000000 | 1027.000000 |  | 20.100000 | 10.610000 | 7000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 16 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 16.130000 | 17.320000 | 94.000000 | 1027.000000 |  | 17.100000 | 11.700000 | 6000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 15.100000 | 15.280000 | 100.000000 | 1027.000000 | 0.7 | 15.100000 | 10.740000 | 1000.000000 | 300.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 15.100000 | 15.280000 | 100.000000 | 1026.000000 | 0.57 | 15.100000 | 7.940000 | 1000.000000 | 290.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 20:00:00 | 90.000000 | 14.100000 | 14.180000 | 100.000000 | 1026.000000 | 0.43 | 14.100000 | 4.700000 | 1000.000000 | 310.000000 |  | 2.060000 | 501 | Rain | moderate rain | 10d | 20 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 15.100000 | 15.280000 | 100.000000 | 1025.000000 |  | 15.100000 | 1.940000 | 9000.000000 | 100.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 15.100000 | 15.280000 | 100.000000 | 1026.000000 | 0.49 | 15.100000 | 0.430000 | 9000.000000 | 100.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155110 | "AEROPUERTO LA NUBIA [26155110]" | 5.029778 | -75.469917 | 2104.000000 | Climática Principal | Convencional | Activa | 1968-06-15 00:00:00 | NaT | Caldas | Manizales | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 14.100000 | 14.180000 | 100.000000 | 1026.000000 | 0.85 | 14.100000 | 0.000000 | 7000.000000 | 0.000000 |  | 0.000000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26155110_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26155110_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26155110_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155110_OWM_Windspeed_20220111.png)
