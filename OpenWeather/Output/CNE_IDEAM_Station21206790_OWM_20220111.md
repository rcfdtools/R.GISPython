
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - HACIENDA SANTA ANA - AUT [21206790] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206790_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.0905,-73.88125) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.0905&lon=-73.88125)


| Parameter | Value |
|---|---|
| Code | 21206790 |
| Name | HACIENDA SANTA ANA - AUT [21206790] |
| Latitude, ° | 5.0905 |
| Longitude, ° | -73.88125 |
| Elevation, m | 2572 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-06-10 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Nemocón |
| Stream | San Juan |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 133) Open Weather values for station 21206790 - HACIENDA SANTA ANA - AUT [21206790]

JSON data from API OWM:

```
{'lat': 5.0905, 'lon': -73.8813, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812849, 'sunset': 1641855493, 'temp': 17.86, 'feels_like': 17.58, 'pressure': 1012, 'humidity': 72, 'dew_point': 12.75, 'uvi': 3.53, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 314, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, 'hourly': [{'dt': 1641772800, 'temp': 12.86, 'feels_like': 12.66, 'pressure': 1016, 'humidity': 94, 'dew_point': 11.92, 'uvi': 0, 'clouds': 88, 'visibility': 8710, 'wind_speed': 0.5, 'wind_deg': 7, 'wind_gust': 1.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 13.86, 'feels_like': 13.78, 'pressure': 1017, 'humidity': 95, 'dew_point': 13.07, 'uvi': 0, 'clouds': 97, 'visibility': 6833, 'wind_speed': 0.49, 'wind_deg': 5, 'wind_gust': 1.26, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.86, 'feels_like': 12.68, 'pressure': 1018, 'humidity': 95, 'dew_point': 12.08, 'uvi': 0, 'clouds': 98, 'visibility': 6078, 'wind_speed': 0.59, 'wind_deg': 7, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.86, 'feels_like': 12.68, 'pressure': 1018, 'humidity': 95, 'dew_point': 12.08, 'uvi': 0, 'clouds': 99, 'visibility': 7488, 'wind_speed': 0.58, 'wind_deg': 17, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 12.86, 'feels_like': 12.68, 'pressure': 1019, 'humidity': 95, 'dew_point': 12.08, 'uvi': 0, 'clouds': 95, 'visibility': 9420, 'wind_speed': 0.35, 'wind_deg': 3, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.86, 'feels_like': 10.51, 'pressure': 1018, 'humidity': 96, 'dew_point': 10.25, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 29, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 8.86, 'feels_like': 8.86, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.79, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 31, 'wind_gust': 0.89, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 7.86, 'feels_like': 7.86, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.8, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 348, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 7.86, 'feels_like': 7.86, 'pressure': 1016, 'humidity': 93, 'dew_point': 6.8, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 341, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 7.86, 'feels_like': 7.86, 'pressure': 1017, 'humidity': 94, 'dew_point': 6.96, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 322, 'wind_gust': 0.97, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.86, 'feels_like': 8.86, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.95, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 314, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 9.86, 'feels_like': 9.86, 'pressure': 1018, 'humidity': 94, 'dew_point': 8.94, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 296, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 9.86, 'feels_like': 9.86, 'pressure': 1019, 'humidity': 89, 'dew_point': 8.13, 'uvi': 0.55, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 278, 'wind_gust': 0.69, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 10.86, 'feels_like': 10.09, 'pressure': 1019, 'humidity': 80, 'dew_point': 7.55, 'uvi': 2.29, 'clouds': 41, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 237, 'wind_gust': 0.83, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 13.86, 'feels_like': 13.1, 'pressure': 1019, 'humidity': 69, 'dew_point': 8.28, 'uvi': 5.42, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 253, 'wind_gust': 1.04, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 15.86, 'feels_like': 15.07, 'pressure': 1017, 'humidity': 60, 'dew_point': 8.12, 'uvi': 9.1, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 270, 'wind_gust': 1.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 16.86, 'feels_like': 16.04, 'pressure': 1016, 'humidity': 55, 'dew_point': 7.77, 'uvi': 11.35, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 288, 'wind_gust': 2.09, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 16.86, 'feels_like': 16.04, 'pressure': 1015, 'humidity': 55, 'dew_point': 7.77, 'uvi': 12.28, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 301, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641837600, 'temp': 17.86, 'feels_like': 17.29, 'pressure': 1014, 'humidity': 61, 'dew_point': 10.24, 'uvi': 11.06, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 313, 'wind_gust': 1.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 17.86, 'feels_like': 17.48, 'pressure': 1013, 'humidity': 68, 'dew_point': 11.88, 'uvi': 6.14, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 315, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.21}}, {'dt': 1641844800, 'temp': 17.86, 'feels_like': 17.58, 'pressure': 1012, 'humidity': 72, 'dew_point': 12.75, 'uvi': 3.53, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 314, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641848400, 'temp': 17.86, 'feels_like': 17.74, 'pressure': 1012, 'humidity': 78, 'dew_point': 13.97, 'uvi': 1.4, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 325, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641852000, 'temp': 16.86, 'feels_like': 16.74, 'pressure': 1013, 'humidity': 82, 'dew_point': 13.77, 'uvi': 0.33, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 350, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.19}}, {'dt': 1641855600, 'temp': 14.86, 'feels_like': 14.8, 'pressure': 1015, 'humidity': 92, 'dew_point': 13.57, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 2, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 00:00:00 | 88.000000 | 11.920000 | 12.660000 | 94.000000 | 1016.000000 |  | 12.860000 | 0.000000 | 8710.000000 | 7.000000 | 1.34 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 01:00:00 | 97.000000 | 13.070000 | 13.780000 | 95.000000 | 1017.000000 |  | 13.860000 | 0.000000 | 6833.000000 | 5.000000 | 1.26 | 0.490000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | 12.080000 | 12.680000 | 95.000000 | 1018.000000 |  | 12.860000 | 0.000000 | 6078.000000 | 7.000000 | 1.09 | 0.590000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 12.080000 | 12.680000 | 95.000000 | 1018.000000 |  | 12.860000 | 0.000000 | 7488.000000 | 17.000000 | 1.07 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 12.080000 | 12.680000 | 95.000000 | 1019.000000 |  | 12.860000 | 0.000000 | 9420.000000 | 3.000000 | 0.97 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 05:00:00 | 96.000000 | 10.250000 | 10.510000 | 96.000000 | 1018.000000 |  | 10.860000 | 0.000000 | 10000.000000 | 29.000000 | 0.79 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 06:00:00 | 48.000000 | 7.790000 | 8.860000 | 93.000000 | 1017.000000 |  | 8.860000 | 0.000000 | 10000.000000 | 31.000000 | 0.89 | 0.360000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 07:00:00 | 71.000000 | 6.800000 | 7.860000 | 93.000000 | 1017.000000 |  | 7.860000 | 0.000000 | 10000.000000 | 348.000000 | 0.74 | 0.160000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 08:00:00 | 69.000000 | 6.800000 | 7.860000 | 93.000000 | 1016.000000 |  | 7.860000 | 0.000000 | 10000.000000 | 341.000000 | 0.89 | 0.360000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 09:00:00 | 65.000000 | 6.960000 | 7.860000 | 94.000000 | 1017.000000 |  | 7.860000 | 0.000000 | 10000.000000 | 322.000000 | 0.97 | 0.590000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 10:00:00 | 58.000000 | 7.950000 | 8.860000 | 94.000000 | 1018.000000 |  | 8.860000 | 0.000000 | 10000.000000 | 314.000000 | 0.74 | 0.430000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 11:00:00 | 57.000000 | 8.940000 | 9.860000 | 94.000000 | 1018.000000 |  | 9.860000 | 0.000000 | 10000.000000 | 296.000000 | 0.76 | 0.360000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 12:00:00 | 36.000000 | 8.130000 | 9.860000 | 89.000000 | 1019.000000 |  | 9.860000 | 0.550000 | 10000.000000 | 278.000000 | 0.69 | 0.080000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 13:00:00 | 41.000000 | 7.550000 | 10.090000 | 80.000000 | 1019.000000 |  | 10.860000 | 2.290000 | 10000.000000 | 237.000000 | 0.83 | 0.590000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 14:00:00 | 35.000000 | 8.280000 | 13.100000 | 69.000000 | 1019.000000 |  | 13.860000 | 5.420000 | 10000.000000 | 253.000000 | 1.04 | 0.780000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 15:00:00 | 33.000000 | 8.120000 | 15.070000 | 60.000000 | 1017.000000 |  | 15.860000 | 9.100000 | 10000.000000 | 270.000000 | 1.81 | 1.330000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 16:00:00 | 41.000000 | 7.770000 | 16.040000 | 55.000000 | 1016.000000 |  | 16.860000 | 11.350000 | 10000.000000 | 288.000000 | 2.09 | 1.590000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 17:00:00 | 50.000000 | 7.770000 | 16.040000 | 55.000000 | 1015.000000 | 0.1 | 16.860000 | 12.280000 | 10000.000000 | 301.000000 | 2.04 | 1.810000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | 10.240000 | 17.290000 | 61.000000 | 1014.000000 |  | 17.860000 | 11.060000 | 10000.000000 | 313.000000 | 1.56 | 1.230000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 19:00:00 | 93.000000 | 11.880000 | 17.480000 | 68.000000 | 1013.000000 | 0.21 | 17.860000 | 6.140000 | 10000.000000 | 315.000000 | 1.73 | 0.640000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 20:00:00 | 89.000000 | 12.750000 | 17.580000 | 72.000000 | 1012.000000 | 0.38 | 17.860000 | 3.530000 | 10000.000000 | 314.000000 | 1.5 | 0.700000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 21:00:00 | 84.000000 | 13.970000 | 17.740000 | 78.000000 | 1012.000000 | 0.49 | 17.860000 | 1.400000 | 10000.000000 | 325.000000 | 1.44 | 0.670000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 22:00:00 | 80.000000 | 13.770000 | 16.740000 | 82.000000 | 1013.000000 | 0.19 | 16.860000 | 0.330000 | 10000.000000 | 350.000000 | 1.67 | 0.550000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206790 | "HACIENDA SANTA ANA - AUT [21206790]" | 5.090500 | -73.881250 | 2572.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Cundinamarca | Nemocón | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 23:00:00 | 81.000000 | 13.570000 | 14.800000 | 92.000000 | 1015.000000 | 0.27 | 14.860000 | 0.000000 | 10000.000000 | 2.000000 | 1.45 | 0.560000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station21206790_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206790_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206790_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206790_OWM_Windspeed_20220111.png)
