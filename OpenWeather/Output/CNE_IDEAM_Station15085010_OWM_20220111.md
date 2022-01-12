
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO MAICAO [15085010] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station15085010_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=11.4,-72.25) or [Openstreet Map](https://www.openstreetmap.org/query?lat=11.4&lon=-72.25)


| Parameter | Value |
|---|---|
| Code | 15085010 |
| Name | AEROPUERTO MAICAO [15085010] |
| Latitude, ° | 11.4 |
| Longitude, ° | -72.25 |
| Elevation, m | 53 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1971-06-15 00:00:00 |
| Suspension date | 1996-06-15 00:00:00 |
| State | La Guajira |
| County | Maicao |
| Stream | Carraipia |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Caribe - Guajira |
| SZH - Hydrographic subzone | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo |

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

### (CNE index 2557) Open Weather values for station 15085010 - AEROPUERTO MAICAO [15085010]

JSON data from API OWM:

```
{'lat': 11.4, 'lon': -72.25, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813077, 'sunset': 1641854481, 'temp': 29.24, 'feels_like': 29.6, 'pressure': 1011, 'humidity': 47, 'dew_point': 16.77, 'uvi': 3.35, 'clouds': 45, 'visibility': 10000, 'wind_speed': 6.3, 'wind_deg': 92, 'wind_gust': 7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.71, 'feels_like': 25.09, 'pressure': 1014, 'humidity': 71, 'dew_point': 19.1, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 4.67, 'wind_deg': 81, 'wind_gust': 8.47, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641776400, 'temp': 24.46, 'feels_like': 24.89, 'pressure': 1015, 'humidity': 74, 'dew_point': 19.52, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 4.79, 'wind_deg': 78, 'wind_gust': 8.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641780000, 'temp': 24.24, 'feels_like': 24.73, 'pressure': 1015, 'humidity': 77, 'dew_point': 19.95, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 4.6, 'wind_deg': 80, 'wind_gust': 8.64, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641783600, 'temp': 23.89, 'feels_like': 24.4, 'pressure': 1015, 'humidity': 79, 'dew_point': 20.03, 'uvi': 0, 'clouds': 6, 'visibility': 10000, 'wind_speed': 4.27, 'wind_deg': 86, 'wind_gust': 8.22, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641787200, 'temp': 23.65, 'feels_like': 24.16, 'pressure': 1015, 'humidity': 80, 'dew_point': 20, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 4.55, 'wind_deg': 88, 'wind_gust': 8.77, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641790800, 'temp': 23.5, 'feels_like': 24.02, 'pressure': 1014, 'humidity': 81, 'dew_point': 20.05, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 4.47, 'wind_deg': 87, 'wind_gust': 8.62, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641794400, 'temp': 23.07, 'feels_like': 23.6, 'pressure': 1014, 'humidity': 83, 'dew_point': 20.03, 'uvi': 0, 'clouds': 5, 'visibility': 10000, 'wind_speed': 4.11, 'wind_deg': 88, 'wind_gust': 8.08, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 22.75, 'feels_like': 23.27, 'pressure': 1013, 'humidity': 84, 'dew_point': 19.91, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 3.86, 'wind_deg': 93, 'wind_gust': 7.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641801600, 'temp': 22.45, 'feels_like': 22.97, 'pressure': 1012, 'humidity': 85, 'dew_point': 19.8, 'uvi': 0, 'clouds': 12, 'visibility': 10000, 'wind_speed': 3.4, 'wind_deg': 94, 'wind_gust': 6.42, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 22.5, 'feels_like': 23.02, 'pressure': 1013, 'humidity': 85, 'dew_point': 19.85, 'uvi': 0, 'clouds': 21, 'visibility': 10000, 'wind_speed': 3.22, 'wind_deg': 89, 'wind_gust': 6.55, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641808800, 'temp': 22.45, 'feels_like': 23, 'pressure': 1013, 'humidity': 86, 'dew_point': 19.99, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 83, 'wind_gust': 5.89, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 22.13, 'feels_like': 22.7, 'pressure': 1014, 'humidity': 88, 'dew_point': 20.05, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.47, 'wind_deg': 88, 'wind_gust': 4.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641816000, 'temp': 23.44, 'feels_like': 23.98, 'pressure': 1015, 'humidity': 82, 'dew_point': 20.19, 'uvi': 0.37, 'clouds': 59, 'visibility': 10000, 'wind_speed': 3.32, 'wind_deg': 93, 'wind_gust': 7.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641819600, 'temp': 25.39, 'feels_like': 25.86, 'pressure': 1016, 'humidity': 72, 'dew_point': 19.98, 'uvi': 1.75, 'clouds': 61, 'visibility': 10000, 'wind_speed': 5.88, 'wind_deg': 88, 'wind_gust': 8.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.92, 'feels_like': 28.26, 'pressure': 1016, 'humidity': 64, 'dew_point': 19.54, 'uvi': 4.18, 'clouds': 34, 'visibility': 10000, 'wind_speed': 6.88, 'wind_deg': 90, 'wind_gust': 8.13, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 28.34, 'feels_like': 29.48, 'pressure': 1016, 'humidity': 56, 'dew_point': 18.72, 'uvi': 7, 'clouds': 26, 'visibility': 10000, 'wind_speed': 7.22, 'wind_deg': 91, 'wind_gust': 8.27, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 29.26, 'feels_like': 30.14, 'pressure': 1015, 'humidity': 51, 'dew_point': 18.08, 'uvi': 9.32, 'clouds': 23, 'visibility': 10000, 'wind_speed': 7.16, 'wind_deg': 92, 'wind_gust': 8.1, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641834000, 'temp': 29.73, 'feels_like': 30.51, 'pressure': 1014, 'humidity': 49, 'dew_point': 17.88, 'uvi': 9.92, 'clouds': 20, 'visibility': 10000, 'wind_speed': 7.17, 'wind_deg': 96, 'wind_gust': 7.93, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641837600, 'temp': 29.79, 'feels_like': 30.31, 'pressure': 1013, 'humidity': 47, 'dew_point': 17.27, 'uvi': 8.72, 'clouds': 8, 'visibility': 10000, 'wind_speed': 7.12, 'wind_deg': 93, 'wind_gust': 7.66, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 29.63, 'feels_like': 30.1, 'pressure': 1011, 'humidity': 47, 'dew_point': 17.13, 'uvi': 6.2, 'clouds': 15, 'visibility': 10000, 'wind_speed': 7.01, 'wind_deg': 93, 'wind_gust': 7.69, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641844800, 'temp': 29.24, 'feels_like': 29.6, 'pressure': 1011, 'humidity': 47, 'dew_point': 16.77, 'uvi': 3.35, 'clouds': 45, 'visibility': 10000, 'wind_speed': 6.3, 'wind_deg': 92, 'wind_gust': 7, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 28.56, 'feels_like': 28.9, 'pressure': 1011, 'humidity': 48, 'dew_point': 16.48, 'uvi': 1.18, 'clouds': 56, 'visibility': 10000, 'wind_speed': 5.68, 'wind_deg': 88, 'wind_gust': 6.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 27.36, 'feels_like': 27.99, 'pressure': 1011, 'humidity': 53, 'dew_point': 16.94, 'uvi': 0.2, 'clouds': 50, 'visibility': 10000, 'wind_speed': 5.08, 'wind_deg': 85, 'wind_gust': 6.75, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 25.14, 'feels_like': 25.33, 'pressure': 1012, 'humidity': 62, 'dew_point': 17.35, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 3.99, 'wind_deg': 91, 'wind_gust': 6.98, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 00:00:00 | 6.000000 | 19.100000 | 25.090000 | 71.000000 | 1014.000000 |  | 24.710000 | 0.000000 | 10000.000000 | 81.000000 | 8.47 | 4.670000 | 800 | Clear | clear sky | 01n | 00 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 01:00:00 | 5.000000 | 19.520000 | 24.890000 | 74.000000 | 1015.000000 |  | 24.460000 | 0.000000 | 10000.000000 | 78.000000 | 8.96 | 4.790000 | 800 | Clear | clear sky | 01n | 01 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 02:00:00 | 6.000000 | 19.950000 | 24.730000 | 77.000000 | 1015.000000 |  | 24.240000 | 0.000000 | 10000.000000 | 80.000000 | 8.64 | 4.600000 | 800 | Clear | clear sky | 01n | 02 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 03:00:00 | 6.000000 | 20.030000 | 24.400000 | 79.000000 | 1015.000000 |  | 23.890000 | 0.000000 | 10000.000000 | 86.000000 | 8.22 | 4.270000 | 800 | Clear | clear sky | 01n | 03 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 04:00:00 | 4.000000 | 20.000000 | 24.160000 | 80.000000 | 1015.000000 |  | 23.650000 | 0.000000 | 10000.000000 | 88.000000 | 8.77 | 4.550000 | 800 | Clear | clear sky | 01n | 04 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 05:00:00 | 4.000000 | 20.050000 | 24.020000 | 81.000000 | 1014.000000 |  | 23.500000 | 0.000000 | 10000.000000 | 87.000000 | 8.62 | 4.470000 | 800 | Clear | clear sky | 01n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 06:00:00 | 5.000000 | 20.030000 | 23.600000 | 83.000000 | 1014.000000 |  | 23.070000 | 0.000000 | 10000.000000 | 88.000000 | 8.08 | 4.110000 | 800 | Clear | clear sky | 01n | 06 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 07:00:00 | 8.000000 | 19.910000 | 23.270000 | 84.000000 | 1013.000000 |  | 22.750000 | 0.000000 | 10000.000000 | 93.000000 | 7.57 | 3.860000 | 800 | Clear | clear sky | 01n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 08:00:00 | 12.000000 | 19.800000 | 22.970000 | 85.000000 | 1012.000000 |  | 22.450000 | 0.000000 | 10000.000000 | 94.000000 | 6.42 | 3.400000 | 801 | Clouds | few clouds | 02n | 08 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 09:00:00 | 21.000000 | 19.850000 | 23.020000 | 85.000000 | 1013.000000 |  | 22.500000 | 0.000000 | 10000.000000 | 89.000000 | 6.55 | 3.220000 | 801 | Clouds | few clouds | 02n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 10:00:00 | 41.000000 | 19.990000 | 23.000000 | 86.000000 | 1013.000000 |  | 22.450000 | 0.000000 | 10000.000000 | 83.000000 | 5.89 | 2.840000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 11:00:00 | 52.000000 | 20.050000 | 22.700000 | 88.000000 | 1014.000000 | 0.17 | 22.130000 | 0.000000 | 10000.000000 | 88.000000 | 4.19 | 2.470000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 12:00:00 | 59.000000 | 20.190000 | 23.980000 | 82.000000 | 1015.000000 | 0.11 | 23.440000 | 0.370000 | 10000.000000 | 93.000000 | 7.7 | 3.320000 | 500 | Rain | light rain | 10d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 13:00:00 | 61.000000 | 19.980000 | 25.860000 | 72.000000 | 1016.000000 |  | 25.390000 | 1.750000 | 10000.000000 | 88.000000 | 8.1 | 5.880000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 14:00:00 | 34.000000 | 19.540000 | 28.260000 | 64.000000 | 1016.000000 |  | 26.920000 | 4.180000 | 10000.000000 | 90.000000 | 8.13 | 6.880000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 15:00:00 | 26.000000 | 18.720000 | 29.480000 | 56.000000 | 1016.000000 |  | 28.340000 | 7.000000 | 10000.000000 | 91.000000 | 8.27 | 7.220000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 16:00:00 | 23.000000 | 18.080000 | 30.140000 | 51.000000 | 1015.000000 |  | 29.260000 | 9.320000 | 10000.000000 | 92.000000 | 8.1 | 7.160000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 17:00:00 | 20.000000 | 17.880000 | 30.510000 | 49.000000 | 1014.000000 |  | 29.730000 | 9.920000 | 10000.000000 | 96.000000 | 7.93 | 7.170000 | 801 | Clouds | few clouds | 02d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 18:00:00 | 8.000000 | 17.270000 | 30.310000 | 47.000000 | 1013.000000 |  | 29.790000 | 8.720000 | 10000.000000 | 93.000000 | 7.66 | 7.120000 | 800 | Clear | clear sky | 01d | 18 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 19:00:00 | 15.000000 | 17.130000 | 30.100000 | 47.000000 | 1011.000000 |  | 29.630000 | 6.200000 | 10000.000000 | 93.000000 | 7.69 | 7.010000 | 801 | Clouds | few clouds | 02d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 20:00:00 | 45.000000 | 16.770000 | 29.600000 | 47.000000 | 1011.000000 |  | 29.240000 | 3.350000 | 10000.000000 | 92.000000 | 7 | 6.300000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 21:00:00 | 56.000000 | 16.480000 | 28.900000 | 48.000000 | 1011.000000 |  | 28.560000 | 1.180000 | 10000.000000 | 88.000000 | 6.56 | 5.680000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 22:00:00 | 50.000000 | 16.940000 | 27.990000 | 53.000000 | 1011.000000 |  | 27.360000 | 0.200000 | 10000.000000 | 85.000000 | 6.75 | 5.080000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 15085010 | "AEROPUERTO MAICAO [15085010]" | 11.400000 | -72.250000 | 53.000000 | Climática Principal | Convencional | Suspendida | 1971-06-15 00:00:00 | 1996-06-15 00:00:00 | La Guajira | Maicao | Carraipia | Area Operativa 05 - Magdalena-Cesar-Guajira | Caribe | Caribe - Guajira | Río Carraipia - Paraguachon, Directos al Golfo Maracaibo | America/Bogota | 2022-01-10 23:00:00 | 45.000000 | 17.350000 | 25.330000 | 62.000000 | 1012.000000 |  | 25.140000 | 0.000000 | 10000.000000 | 91.000000 | 6.98 | 3.990000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station15085010_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Rain_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Temp_20220111.png)
![CNE_IDEAM_Station15085010_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_UVI_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station15085010_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station15085010_OWM_Windspeed_20220111.png)
