
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MONGUI - AUT [15065190] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15065190_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.22677778,-72.82063889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.22677778&lon=-72.82063889)


| Parameter | Value |
|---|---|
| Code | 15065190 |
| Name | MONGUI - AUT [15065190] |
| Latitude, ° | 11.22677778 |
| Longitude, ° | -72.82063889 |
| Elevation, m | 60 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2011-11-22 00:00:00 |
| Suspension date | NaT |
| State | La Guajira |
| County | Riohacha |
| Stream | Barroblanco |
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

### (CNE index 205) Open Weather values for station 15065190 - MONGUI - AUT [15065190]

JSON data from API OWM:

```
{'lat': 11.2268, 'lon': -72.8206, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813197, 'sunset': 1641854636, 'temp': 27.68, 'feels_like': 27.11, 'pressure': 1010, 'humidity': 35, 'dew_point': 10.85, 'uvi': 3.4, 'clouds': 25, 'visibility': 10000, 'wind_speed': 6.74, 'wind_deg': 66, 'wind_gust': 6.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 28.68, 'feels_like': 31.87, 'pressure': 1014, 'humidity': 69, 'dew_point': 22.43, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 3.89, 'wind_deg': 94, 'wind_gust': 9.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 28.68, 'feels_like': 32.92, 'pressure': 1015, 'humidity': 75, 'dew_point': 23.81, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 3.2, 'wind_deg': 97, 'wind_gust': 8.8, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 22.1, 'feels_like': 22.48, 'pressure': 1015, 'humidity': 81, 'dew_point': 18.69, 'uvi': 0, 'clouds': 15, 'visibility': 10000, 'wind_speed': 2.55, 'wind_deg': 102, 'wind_gust': 6.36, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 21.49, 'feels_like': 21.91, 'pressure': 1015, 'humidity': 85, 'dew_point': 18.86, 'uvi': 0, 'clouds': 12, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 106, 'wind_gust': 5.25, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 21.04, 'feels_like': 21.52, 'pressure': 1015, 'humidity': 89, 'dew_point': 19.16, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 110, 'wind_gust': 4.38, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 20.74, 'feels_like': 21.25, 'pressure': 1014, 'humidity': 91, 'dew_point': 19.22, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 111, 'wind_gust': 3.77, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 20.61, 'feels_like': 21.15, 'pressure': 1013, 'humidity': 93, 'dew_point': 19.44, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 102, 'wind_gust': 4.09, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 20.52, 'feels_like': 21.08, 'pressure': 1013, 'humidity': 94, 'dew_point': 19.52, 'uvi': 0, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 103, 'wind_gust': 4.08, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 20.3, 'feels_like': 20.87, 'pressure': 1012, 'humidity': 95, 'dew_point': 19.47, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 102, 'wind_gust': 3.23, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 20.16, 'feels_like': 20.71, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.33, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 106, 'wind_gust': 2.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 20.18, 'feels_like': 20.73, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.35, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 108, 'wind_gust': 2.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 22.68, 'feels_like': 23.43, 'pressure': 1014, 'humidity': 93, 'dew_point': 21.49, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 104, 'wind_gust': 3.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 22.68, 'feels_like': 23.25, 'pressure': 1015, 'humidity': 86, 'dew_point': 20.22, 'uvi': 0.36, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 92, 'wind_gust': 4.24, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 24.68, 'feels_like': 25.01, 'pressure': 1015, 'humidity': 69, 'dew_point': 18.61, 'uvi': 1.7, 'clouds': 25, 'visibility': 10000, 'wind_speed': 3.62, 'wind_deg': 84, 'wind_gust': 6.53, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 26.68, 'feels_like': 27.45, 'pressure': 1016, 'humidity': 56, 'dew_point': 17.18, 'uvi': 4.11, 'clouds': 16, 'visibility': 10000, 'wind_speed': 4.75, 'wind_deg': 87, 'wind_gust': 6.67, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 28.68, 'feels_like': 28.93, 'pressure': 1016, 'humidity': 47, 'dew_point': 16.26, 'uvi': 6.93, 'clouds': 13, 'visibility': 10000, 'wind_speed': 5.25, 'wind_deg': 85, 'wind_gust': 6.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641830400, 'temp': 31.68, 'feels_like': 32.17, 'pressure': 1014, 'humidity': 42, 'dew_point': 17.2, 'uvi': 9.27, 'clouds': 15, 'visibility': 10000, 'wind_speed': 5.75, 'wind_deg': 83, 'wind_gust': 7.1, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 30.68, 'feels_like': 30.25, 'pressure': 1013, 'humidity': 38, 'dew_point': 14.74, 'uvi': 9.94, 'clouds': 14, 'visibility': 10000, 'wind_speed': 5.89, 'wind_deg': 80, 'wind_gust': 6.96, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 31.68, 'feels_like': 31.07, 'pressure': 1011, 'humidity': 35, 'dew_point': 14.35, 'uvi': 8.8, 'clouds': 8, 'visibility': 10000, 'wind_speed': 6.22, 'wind_deg': 74, 'wind_gust': 6.79, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 32.68, 'feels_like': 32.2, 'pressure': 1010, 'humidity': 34, 'dew_point': 14.78, 'uvi': 6.22, 'clouds': 14, 'visibility': 10000, 'wind_speed': 6.71, 'wind_deg': 69, 'wind_gust': 6.81, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 27.68, 'feels_like': 27.11, 'pressure': 1010, 'humidity': 35, 'dew_point': 10.85, 'uvi': 3.4, 'clouds': 25, 'visibility': 10000, 'wind_speed': 6.74, 'wind_deg': 66, 'wind_gust': 6.55, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 27.68, 'feels_like': 27.27, 'pressure': 1010, 'humidity': 38, 'dew_point': 12.09, 'uvi': 1.23, 'clouds': 42, 'visibility': 10000, 'wind_speed': 6.42, 'wind_deg': 64, 'wind_gust': 6.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 26.68, 'feels_like': 26.82, 'pressure': 1011, 'humidity': 44, 'dew_point': 13.43, 'uvi': 0.2, 'clouds': 52, 'visibility': 10000, 'wind_speed': 5.59, 'wind_deg': 60, 'wind_gust': 6.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.68, 'feels_like': 29.84, 'pressure': 1011, 'humidity': 55, 'dew_point': 18.75, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 4.24, 'wind_deg': 63, 'wind_gust': 8.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 00:00:00 | 8.000000 | 22.430000 | 31.870000 | 69.000000 | 1014.000000 |  | 28.680000 | 0.000000 | 10000.000000 | 94.000000 | 9.94 | 3.890000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 01:00:00 | 7.000000 | 23.810000 | 32.920000 | 75.000000 | 1015.000000 |  | 28.680000 | 0.000000 | 10000.000000 | 97.000000 | 8.8 | 3.200000 | 800 | Clear | clear sky | 01n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 02:00:00 | 15.000000 | 18.690000 | 22.480000 | 81.000000 | 1015.000000 |  | 22.100000 | 0.000000 | 10000.000000 | 102.000000 | 6.36 | 2.550000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 03:00:00 | 12.000000 | 18.860000 | 21.910000 | 85.000000 | 1015.000000 |  | 21.490000 | 0.000000 | 10000.000000 | 106.000000 | 5.25 | 2.190000 | 801 | Clouds | few clouds | 02n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 04:00:00 | 9.000000 | 19.160000 | 21.520000 | 89.000000 | 1015.000000 |  | 21.040000 | 0.000000 | 10000.000000 | 110.000000 | 4.38 | 1.820000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 05:00:00 | 8.000000 | 19.220000 | 21.250000 | 91.000000 | 1014.000000 |  | 20.740000 | 0.000000 | 10000.000000 | 111.000000 | 3.77 | 1.720000 | 800 | Clear | clear sky | 01n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 06:00:00 | 5.000000 | 19.440000 | 21.150000 | 93.000000 | 1013.000000 |  | 20.610000 | 0.000000 | 10000.000000 | 102.000000 | 4.09 | 1.680000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 07:00:00 | 10.000000 | 19.520000 | 21.080000 | 94.000000 | 1013.000000 |  | 20.520000 | 0.000000 | 10000.000000 | 103.000000 | 4.08 | 1.710000 | 800 | Clear | clear sky | 01n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 08:00:00 | 14.000000 | 19.470000 | 20.870000 | 95.000000 | 1012.000000 |  | 20.300000 | 0.000000 | 10000.000000 | 102.000000 | 3.23 | 1.470000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 09:00:00 | 32.000000 | 19.330000 | 20.710000 | 95.000000 | 1013.000000 |  | 20.160000 | 0.000000 | 10000.000000 | 106.000000 | 2.55 | 1.330000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 10:00:00 | 49.000000 | 19.350000 | 20.730000 | 95.000000 | 1013.000000 |  | 20.180000 | 0.000000 | 10000.000000 | 108.000000 | 2.62 | 1.220000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 11:00:00 | 59.000000 | 21.490000 | 23.430000 | 93.000000 | 1014.000000 |  | 22.680000 | 0.000000 | 10000.000000 | 104.000000 | 3.17 | 1.090000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 12:00:00 | 19.000000 | 20.220000 | 23.250000 | 86.000000 | 1015.000000 |  | 22.680000 | 0.360000 | 10000.000000 | 92.000000 | 4.24 | 1.200000 | 801 | Clouds | few clouds | 02d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 13:00:00 | 25.000000 | 18.610000 | 25.010000 | 69.000000 | 1015.000000 |  | 24.680000 | 1.700000 | 10000.000000 | 84.000000 | 6.53 | 3.620000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 14:00:00 | 16.000000 | 17.180000 | 27.450000 | 56.000000 | 1016.000000 |  | 26.680000 | 4.110000 | 10000.000000 | 87.000000 | 6.67 | 4.750000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 15:00:00 | 13.000000 | 16.260000 | 28.930000 | 47.000000 | 1016.000000 |  | 28.680000 | 6.930000 | 10000.000000 | 85.000000 | 6.89 | 5.250000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 16:00:00 | 15.000000 | 17.200000 | 32.170000 | 42.000000 | 1014.000000 |  | 31.680000 | 9.270000 | 10000.000000 | 83.000000 | 7.1 | 5.750000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 17:00:00 | 14.000000 | 14.740000 | 30.250000 | 38.000000 | 1013.000000 |  | 30.680000 | 9.940000 | 10000.000000 | 80.000000 | 6.96 | 5.890000 | 801 | Clouds | few clouds | 02d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 18:00:00 | 8.000000 | 14.350000 | 31.070000 | 35.000000 | 1011.000000 |  | 31.680000 | 8.800000 | 10000.000000 | 74.000000 | 6.79 | 6.220000 | 800 | Clear | clear sky | 01d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 19:00:00 | 14.000000 | 14.780000 | 32.200000 | 34.000000 | 1010.000000 |  | 32.680000 | 6.220000 | 10000.000000 | 69.000000 | 6.81 | 6.710000 | 801 | Clouds | few clouds | 02d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 20:00:00 | 25.000000 | 10.850000 | 27.110000 | 35.000000 | 1010.000000 |  | 27.680000 | 3.400000 | 10000.000000 | 66.000000 | 6.55 | 6.740000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 21:00:00 | 42.000000 | 12.090000 | 27.270000 | 38.000000 | 1010.000000 |  | 27.680000 | 1.230000 | 10000.000000 | 64.000000 | 6.62 | 6.420000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 22:00:00 | 52.000000 | 13.430000 | 26.820000 | 44.000000 | 1011.000000 |  | 26.680000 | 0.200000 | 10000.000000 | 60.000000 | 6.92 | 5.590000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 15065190 | "MONGUI - AUT [15065190]" | 11.226778 | -72.820639 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-11-22 00:00:00 | NaT | La Guajira | Riohacha | Barroblanco | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Ranchería | America/Bogota | 2022-01-10 23:00:00 | 61.000000 | 18.750000 | 29.840000 | 55.000000 | 1011.000000 |  | 28.680000 | 0.000000 | 10000.000000 | 63.000000 | 8.57 | 4.240000 | 803 | Clouds | broken clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station15065190_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15065190_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15065190_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15065190_OWM_Windspeed_20220111.png)
