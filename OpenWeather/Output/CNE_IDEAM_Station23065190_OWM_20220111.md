
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - QUEBRADA NEGRA - AUT [23065190] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23065190_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.13761111,-74.48125) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.13761111&lon=-74.48125)


| Parameter | Value |
|---|---|
| Code | 23065190 |
| Name | QUEBRADA NEGRA - AUT [23065190] |
| Latitude, ° | 5.13761111 |
| Longitude, ° | -74.48125 |
| Elevation, m | 1107 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-10-06 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Quebradanegra |
| Stream | Negro |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
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

### (CNE index 136) Open Weather values for station 23065190 - QUEBRADA NEGRA - AUT [23065190]

JSON data from API OWM:

```
{'lat': 5.1376, 'lon': -74.4813, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812997, 'sunset': 1641855633, 'temp': 27.27, 'feels_like': 29.82, 'pressure': 1009, 'humidity': 75, 'dew_point': 22.45, 'uvi': 4.34, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 324, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, 'hourly': [{'dt': 1641772800, 'temp': 22.27, 'feels_like': 23.09, 'pressure': 1012, 'humidity': 97, 'dew_point': 21.77, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 86, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.46}}, {'dt': 1641776400, 'temp': 23.27, 'feels_like': 24.19, 'pressure': 1014, 'humidity': 97, 'dew_point': 22.77, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 92, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 22.27, 'feels_like': 23.09, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.77, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 97, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 22.27, 'feels_like': 23.09, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.77, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.46, 'wind_deg': 104, 'wind_gust': 1.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 22.27, 'feels_like': 23.09, 'pressure': 1015, 'humidity': 97, 'dew_point': 21.77, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 108, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.27, 'feels_like': 20.89, 'pressure': 1014, 'humidity': 97, 'dew_point': 19.78, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 109, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 18.27, 'feels_like': 18.66, 'pressure': 1013, 'humidity': 96, 'dew_point': 17.62, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 110, 'wind_gust': 1.15, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 17.27, 'feels_like': 17.56, 'pressure': 1013, 'humidity': 96, 'dew_point': 16.63, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 112, 'wind_gust': 1.16, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 17.27, 'feels_like': 17.56, 'pressure': 1012, 'humidity': 96, 'dew_point': 16.63, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 110, 'wind_gust': 1.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 17.27, 'feels_like': 17.56, 'pressure': 1013, 'humidity': 96, 'dew_point': 16.63, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 109, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 18.27, 'feels_like': 18.66, 'pressure': 1013, 'humidity': 96, 'dew_point': 17.62, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 111, 'wind_gust': 1.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 19.27, 'feels_like': 19.76, 'pressure': 1014, 'humidity': 96, 'dew_point': 18.62, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 111, 'wind_gust': 1.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 19.27, 'feels_like': 19.68, 'pressure': 1015, 'humidity': 93, 'dew_point': 18.11, 'uvi': 0.32, 'clouds': 19, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 110, 'wind_gust': 1.21, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 20.27, 'feels_like': 20.57, 'pressure': 1016, 'humidity': 85, 'dew_point': 17.67, 'uvi': 2.05, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 57, 'wind_gust': 1.32, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 23.27, 'feels_like': 23.58, 'pressure': 1016, 'humidity': 74, 'dew_point': 18.38, 'uvi': 4.95, 'clouds': 38, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 342, 'wind_gust': 1.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 25.27, 'feels_like': 25.5, 'pressure': 1015, 'humidity': 63, 'dew_point': 17.73, 'uvi': 8.38, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 338, 'wind_gust': 1.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1014, 'humidity': 58, 'dew_point': 17.35, 'uvi': 10.81, 'clouds': 52, 'visibility': 10000, 'wind_speed': 1.98, 'wind_deg': 320, 'wind_gust': 1.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1012, 'humidity': 56, 'dew_point': 16.8, 'uvi': 11.77, 'clouds': 52, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 317, 'wind_gust': 1.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 27.27, 'feels_like': 28.11, 'pressure': 1011, 'humidity': 56, 'dew_point': 17.73, 'uvi': 10.67, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 313, 'wind_gust': 2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 27.27, 'feels_like': 28.95, 'pressure': 1010, 'humidity': 66, 'dew_point': 20.36, 'uvi': 7.48, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 315, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641844800, 'temp': 27.27, 'feels_like': 29.82, 'pressure': 1009, 'humidity': 75, 'dew_point': 22.45, 'uvi': 4.34, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 324, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641848400, 'temp': 27.27, 'feels_like': 30.8, 'pressure': 1010, 'humidity': 84, 'dew_point': 24.33, 'uvi': 1.74, 'clouds': 62, 'visibility': 9985, 'wind_speed': 1.33, 'wind_deg': 339, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, {'dt': 1641852000, 'temp': 26.27, 'feels_like': 26.27, 'pressure': 1010, 'humidity': 91, 'dew_point': 24.68, 'uvi': 0.39, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 1, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641855600, 'temp': 24.27, 'feels_like': 25.29, 'pressure': 1011, 'humidity': 97, 'dew_point': 23.76, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 50, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.88}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 00:00:00 | 50.000000 | 21.770000 | 23.090000 | 97.000000 | 1012.000000 | 0.46 | 22.270000 | 0.000000 | 10000.000000 | 86.000000 | 1.16 | 1.270000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 01:00:00 | 61.000000 | 22.770000 | 24.190000 | 97.000000 | 1014.000000 |  | 23.270000 | 0.000000 | 10000.000000 | 92.000000 | 1.18 | 1.430000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 02:00:00 | 52.000000 | 21.770000 | 23.090000 | 97.000000 | 1015.000000 |  | 22.270000 | 0.000000 | 10000.000000 | 97.000000 | 1.19 | 1.490000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 03:00:00 | 50.000000 | 21.770000 | 23.090000 | 97.000000 | 1015.000000 |  | 22.270000 | 0.000000 | 10000.000000 | 104.000000 | 1.2 | 1.460000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 04:00:00 | 52.000000 | 21.770000 | 23.090000 | 97.000000 | 1015.000000 |  | 22.270000 | 0.000000 | 10000.000000 | 108.000000 | 1.19 | 1.530000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 05:00:00 | 57.000000 | 19.780000 | 20.890000 | 97.000000 | 1014.000000 |  | 20.270000 | 0.000000 | 10000.000000 | 109.000000 | 1.19 | 1.570000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 06:00:00 | 20.000000 | 17.620000 | 18.660000 | 96.000000 | 1013.000000 |  | 18.270000 | 0.000000 | 10000.000000 | 110.000000 | 1.15 | 1.500000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 07:00:00 | 34.000000 | 16.630000 | 17.560000 | 96.000000 | 1013.000000 |  | 17.270000 | 0.000000 | 10000.000000 | 112.000000 | 1.16 | 1.470000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 08:00:00 | 57.000000 | 16.630000 | 17.560000 | 96.000000 | 1012.000000 |  | 17.270000 | 0.000000 | 10000.000000 | 110.000000 | 1.17 | 1.490000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 09:00:00 | 55.000000 | 16.630000 | 17.560000 | 96.000000 | 1013.000000 |  | 17.270000 | 0.000000 | 10000.000000 | 109.000000 | 1.21 | 1.590000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 10:00:00 | 46.000000 | 17.620000 | 18.660000 | 96.000000 | 1013.000000 |  | 18.270000 | 0.000000 | 10000.000000 | 111.000000 | 1.2 | 1.620000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 11:00:00 | 49.000000 | 18.620000 | 19.760000 | 96.000000 | 1014.000000 |  | 19.270000 | 0.000000 | 10000.000000 | 111.000000 | 1.2 | 1.580000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 12:00:00 | 19.000000 | 18.110000 | 19.680000 | 93.000000 | 1015.000000 |  | 19.270000 | 0.320000 | 10000.000000 | 110.000000 | 1.21 | 1.350000 | 801 | Clouds | few clouds | 02d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 13:00:00 | 33.000000 | 17.670000 | 20.570000 | 85.000000 | 1016.000000 |  | 20.270000 | 2.050000 | 10000.000000 | 57.000000 | 1.32 | 0.700000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 14:00:00 | 38.000000 | 18.380000 | 23.580000 | 74.000000 | 1016.000000 |  | 23.270000 | 4.950000 | 10000.000000 | 342.000000 | 1.71 | 1.160000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 15:00:00 | 53.000000 | 17.730000 | 25.500000 | 63.000000 | 1015.000000 |  | 25.270000 | 8.380000 | 10000.000000 | 338.000000 | 1.99 | 1.700000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 16:00:00 | 52.000000 | 17.350000 | 26.270000 | 58.000000 | 1014.000000 |  | 26.270000 | 10.810000 | 10000.000000 | 320.000000 | 1.85 | 1.980000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 17:00:00 | 52.000000 | 16.800000 | 26.270000 | 56.000000 | 1012.000000 |  | 26.270000 | 11.770000 | 10000.000000 | 317.000000 | 1.99 | 2.150000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 18:00:00 | 76.000000 | 17.730000 | 28.110000 | 56.000000 | 1011.000000 |  | 27.270000 | 10.670000 | 10000.000000 | 313.000000 | 2 | 2.270000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 19:00:00 | 85.000000 | 20.360000 | 28.950000 | 66.000000 | 1010.000000 | 0.34 | 27.270000 | 7.480000 | 10000.000000 | 315.000000 | 1.9 | 1.940000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 20:00:00 | 65.000000 | 22.450000 | 29.820000 | 75.000000 | 1009.000000 | 0.66 | 27.270000 | 4.340000 | 10000.000000 | 324.000000 | 1.79 | 1.440000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 21:00:00 | 62.000000 | 24.330000 | 30.800000 | 84.000000 | 1010.000000 | 0.89 | 27.270000 | 1.740000 | 9985.000000 | 339.000000 | 1.88 | 1.330000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 22:00:00 | 61.000000 | 24.680000 | 26.270000 | 91.000000 | 1010.000000 | 0.77 | 26.270000 | 0.390000 | 10000.000000 | 1.000000 | 1.52 | 1.010000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23065190 | "QUEBRADA NEGRA - AUT [23065190]" | 5.137611 | -74.481250 | 1107.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-06 00:00:00 | NaT | Cundinamarca | Quebradanegra | Negro | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Medio Magdalena | Río Negro | America/Bogota | 2022-01-10 23:00:00 | 68.000000 | 23.760000 | 25.290000 | 97.000000 | 1011.000000 | 0.88 | 24.270000 | 0.000000 | 10000.000000 | 50.000000 | 1.24 | 1.310000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23065190_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23065190_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23065190_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23065190_OWM_Windspeed_20220111.png)
