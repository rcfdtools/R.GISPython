
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA PAULINA - AUT [15065040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15065040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=10.89813889,-72.82847222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=10.89813889&lon=-72.82847222)


| Parameter | Value |
|---|---|
| Code | 15065040 |
| Name | LA PAULINA - AUT [15065040] |
| Latitude, ° | 10.89813889 |
| Longitude, ° | -72.82847222 |
| Elevation, m | 170 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1966-09-14 19:00:00 |
| Suspension date | NaT |
| State | La Guajira |
| County | Fonseca |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río Ranchería |

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

### (CNE index 316) Open Weather values for station 15065040 - LA PAULINA - AUT [15065040]

JSON data from API OWM:

```
{'lat': 10.8981, 'lon': -72.8285, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813166, 'sunset': 1641854670, 'temp': 33.8, 'feels_like': 33.56, 'pressure': 1009, 'humidity': 33, 'dew_point': 15.29, 'uvi': 3.58, 'clouds': 60, 'visibility': 10000, 'wind_speed': 3.86, 'wind_deg': 49, 'wind_gust': 3.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.8, 'feels_like': 32.83, 'pressure': 1014, 'humidity': 73, 'dew_point': 23.48, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 60, 'wind_gust': 3.8, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 27.8, 'feels_like': 31.6, 'pressure': 1015, 'humidity': 80, 'dew_point': 24.03, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 69, 'wind_gust': 2.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 26.8, 'feels_like': 29.73, 'pressure': 1016, 'humidity': 85, 'dew_point': 24.06, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 74, 'wind_gust': 2.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 26.8, 'feels_like': 29.99, 'pressure': 1016, 'humidity': 88, 'dew_point': 24.64, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 80, 'wind_gust': 2.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 26.8, 'feels_like': 30.26, 'pressure': 1015, 'humidity': 91, 'dew_point': 25.21, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 79, 'wind_gust': 2.39, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 20.01, 'feels_like': 20.47, 'pressure': 1015, 'humidity': 92, 'dew_point': 18.67, 'uvi': 0, 'clouds': 18, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 78, 'wind_gust': 2.41, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 20.05, 'feels_like': 20.51, 'pressure': 1014, 'humidity': 92, 'dew_point': 18.71, 'uvi': 0, 'clouds': 17, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 65, 'wind_gust': 2.34, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 19.97, 'feels_like': 20.42, 'pressure': 1013, 'humidity': 92, 'dew_point': 18.63, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 66, 'wind_gust': 2.41, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 19.85, 'feels_like': 20.32, 'pressure': 1013, 'humidity': 93, 'dew_point': 18.69, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 72, 'wind_gust': 1.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 19.8, 'feels_like': 20.26, 'pressure': 1013, 'humidity': 93, 'dew_point': 18.64, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 68, 'wind_gust': 1.66, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 19.63, 'feels_like': 20.1, 'pressure': 1014, 'humidity': 94, 'dew_point': 18.64, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 75, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 22.8, 'feels_like': 23.59, 'pressure': 1014, 'humidity': 94, 'dew_point': 21.78, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 83, 'wind_gust': 1.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 23.8, 'feels_like': 24.51, 'pressure': 1015, 'humidity': 87, 'dew_point': 21.51, 'uvi': 0.39, 'clouds': 9, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 74, 'wind_gust': 2.13, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641819600, 'temp': 25.8, 'feels_like': 26.26, 'pressure': 1016, 'humidity': 70, 'dew_point': 19.91, 'uvi': 1.84, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 53, 'wind_gust': 3.2, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 27.8, 'feels_like': 28.67, 'pressure': 1016, 'humidity': 55, 'dew_point': 17.94, 'uvi': 4.45, 'clouds': 12, 'visibility': 10000, 'wind_speed': 2.04, 'wind_deg': 53, 'wind_gust': 3.02, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 29.8, 'feels_like': 30.19, 'pressure': 1016, 'humidity': 46, 'dew_point': 16.94, 'uvi': 7.5, 'clouds': 10, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 50, 'wind_gust': 3.56, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641830400, 'temp': 30.8, 'feels_like': 30.52, 'pressure': 1014, 'humidity': 39, 'dew_point': 15.25, 'uvi': 9.89, 'clouds': 9, 'visibility': 10000, 'wind_speed': 2.81, 'wind_deg': 48, 'wind_gust': 3.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641834000, 'temp': 32.8, 'feels_like': 32.52, 'pressure': 1013, 'humidity': 35, 'dew_point': 15.33, 'uvi': 10.61, 'clouds': 8, 'visibility': 10000, 'wind_speed': 3.11, 'wind_deg': 50, 'wind_gust': 3.92, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641837600, 'temp': 32.8, 'feels_like': 32.2, 'pressure': 1011, 'humidity': 33, 'dew_point': 14.42, 'uvi': 9.38, 'clouds': 31, 'visibility': 10000, 'wind_speed': 3.35, 'wind_deg': 49, 'wind_gust': 3.59, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 33.8, 'feels_like': 33.37, 'pressure': 1010, 'humidity': 32, 'dew_point': 14.81, 'uvi': 6.53, 'clouds': 33, 'visibility': 10000, 'wind_speed': 3.68, 'wind_deg': 50, 'wind_gust': 3.57, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 33.8, 'feels_like': 33.56, 'pressure': 1009, 'humidity': 33, 'dew_point': 15.29, 'uvi': 3.58, 'clouds': 60, 'visibility': 10000, 'wind_speed': 3.86, 'wind_deg': 49, 'wind_gust': 3.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 33.8, 'feels_like': 34.61, 'pressure': 1010, 'humidity': 38, 'dew_point': 17.5, 'uvi': 1.3, 'clouds': 65, 'visibility': 10000, 'wind_speed': 3.82, 'wind_deg': 48, 'wind_gust': 4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 32.8, 'feels_like': 34.84, 'pressure': 1010, 'humidity': 46, 'dew_point': 19.66, 'uvi': 0.23, 'clouds': 63, 'visibility': 10000, 'wind_speed': 3.28, 'wind_deg': 39, 'wind_gust': 5.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 30.8, 'feels_like': 33.96, 'pressure': 1012, 'humidity': 58, 'dew_point': 21.58, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 2.4, 'wind_deg': 33, 'wind_gust': 5.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 00:00:00 | 49.000000 | 23.480000 | 32.830000 | 73.000000 | 1014.000000 |  | 28.800000 | 0.000000 | 10000.000000 | 60.000000 | 3.8 | 1.690000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 01:00:00 | 46.000000 | 24.030000 | 31.600000 | 80.000000 | 1015.000000 |  | 27.800000 | 0.000000 | 10000.000000 | 69.000000 | 2.75 | 1.400000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 02:00:00 | 34.000000 | 24.060000 | 29.730000 | 85.000000 | 1016.000000 |  | 26.800000 | 0.000000 | 10000.000000 | 74.000000 | 2.57 | 1.170000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 03:00:00 | 25.000000 | 24.640000 | 29.990000 | 88.000000 | 1016.000000 |  | 26.800000 | 0.000000 | 10000.000000 | 80.000000 | 2.63 | 1.140000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 04:00:00 | 20.000000 | 25.210000 | 30.260000 | 91.000000 | 1015.000000 |  | 26.800000 | 0.000000 | 10000.000000 | 79.000000 | 2.39 | 0.900000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 05:00:00 | 18.000000 | 18.670000 | 20.470000 | 92.000000 | 1015.000000 |  | 20.010000 | 0.000000 | 10000.000000 | 78.000000 | 2.41 | 0.980000 | 801 | Clouds | few clouds | 02n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 06:00:00 | 17.000000 | 18.710000 | 20.510000 | 92.000000 | 1014.000000 |  | 20.050000 | 0.000000 | 10000.000000 | 65.000000 | 2.34 | 0.950000 | 801 | Clouds | few clouds | 02n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 07:00:00 | 19.000000 | 18.630000 | 20.420000 | 92.000000 | 1013.000000 |  | 19.970000 | 0.000000 | 10000.000000 | 66.000000 | 2.41 | 1.010000 | 801 | Clouds | few clouds | 02n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 08:00:00 | 14.000000 | 18.690000 | 20.320000 | 93.000000 | 1013.000000 |  | 19.850000 | 0.000000 | 10000.000000 | 72.000000 | 1.89 | 0.830000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 09:00:00 | 41.000000 | 18.640000 | 20.260000 | 93.000000 | 1013.000000 |  | 19.800000 | 0.000000 | 10000.000000 | 68.000000 | 1.66 | 0.730000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 18.640000 | 20.100000 | 94.000000 | 1014.000000 |  | 19.630000 | 0.000000 | 10000.000000 | 75.000000 | 1.63 | 0.730000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 11:00:00 | 63.000000 | 21.780000 | 23.590000 | 94.000000 | 1014.000000 |  | 22.800000 | 0.000000 | 10000.000000 | 83.000000 | 1.63 | 0.680000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 12:00:00 | 9.000000 | 21.510000 | 24.510000 | 87.000000 | 1015.000000 |  | 23.800000 | 0.390000 | 10000.000000 | 74.000000 | 2.13 | 0.710000 | 800 | Clear | clear sky | 01d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 13:00:00 | 11.000000 | 19.910000 | 26.260000 | 70.000000 | 1016.000000 |  | 25.800000 | 1.840000 | 10000.000000 | 53.000000 | 3.2 | 1.590000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 14:00:00 | 12.000000 | 17.940000 | 28.670000 | 55.000000 | 1016.000000 |  | 27.800000 | 4.450000 | 10000.000000 | 53.000000 | 3.02 | 2.040000 | 801 | Clouds | few clouds | 02d | 14 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 15:00:00 | 10.000000 | 16.940000 | 30.190000 | 46.000000 | 1016.000000 |  | 29.800000 | 7.500000 | 10000.000000 | 50.000000 | 3.56 | 2.440000 | 800 | Clear | clear sky | 01d | 15 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 16:00:00 | 9.000000 | 15.250000 | 30.520000 | 39.000000 | 1014.000000 |  | 30.800000 | 9.890000 | 10000.000000 | 48.000000 | 3.94 | 2.810000 | 800 | Clear | clear sky | 01d | 16 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 17:00:00 | 8.000000 | 15.330000 | 32.520000 | 35.000000 | 1013.000000 |  | 32.800000 | 10.610000 | 10000.000000 | 50.000000 | 3.92 | 3.110000 | 800 | Clear | clear sky | 01d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 18:00:00 | 31.000000 | 14.420000 | 32.200000 | 33.000000 | 1011.000000 |  | 32.800000 | 9.380000 | 10000.000000 | 49.000000 | 3.59 | 3.350000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 19:00:00 | 33.000000 | 14.810000 | 33.370000 | 32.000000 | 1010.000000 |  | 33.800000 | 6.530000 | 10000.000000 | 50.000000 | 3.57 | 3.680000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 20:00:00 | 60.000000 | 15.290000 | 33.560000 | 33.000000 | 1009.000000 |  | 33.800000 | 3.580000 | 10000.000000 | 49.000000 | 3.48 | 3.860000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 21:00:00 | 65.000000 | 17.500000 | 34.610000 | 38.000000 | 1010.000000 |  | 33.800000 | 1.300000 | 10000.000000 | 48.000000 | 4 | 3.820000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 22:00:00 | 63.000000 | 19.660000 | 34.840000 | 46.000000 | 1010.000000 |  | 32.800000 | 0.230000 | 10000.000000 | 39.000000 | 5.11 | 3.280000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065040 | "LA PAULINA - AUT [15065040]" | 10.898139 | -72.828472 | 170.000000 | Climática Principal | Automática con Telemetría | Activa | 1966-09-14 19:00:00 | NaT | La Guajira | Fonseca | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 23:00:00 | 65.000000 | 21.580000 | 33.960000 | 58.000000 | 1012.000000 |  | 30.800000 | 0.000000 | 10000.000000 | 33.000000 | 5.15 | 2.400000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15065040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15065040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15065040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065040_OWM_Windspeed_20220111.png)
