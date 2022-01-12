
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PNN CHINGAZA - AUT [35025080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.661,-73.82733333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.661&lon=-73.82733333)


| Parameter | Value |
|---|---|
| Code | 35025080 |
| Name | PNN CHINGAZA - AUT [35025080] |
| Latitude, ° | 4.661 |
| Longitude, ° | -73.82733333 |
| Elevation, m | 3205 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-12-06 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | La Calera |
| Stream | Otun |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Guayuriba |

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

### (CNE index 108) Open Weather values for station 35025080 - PNN CHINGAZA - AUT [35025080]

JSON data from API OWM:

```
{'lat': 4.661, 'lon': -73.8273, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812794, 'sunset': 1641855522, 'temp': 13.64, 'feels_like': 13.12, 'pressure': 1013, 'humidity': 79, 'dew_point': 10.07, 'uvi': 4.16, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 118, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, 'hourly': [{'dt': 1641772800, 'temp': 8.64, 'feels_like': 8.64, 'pressure': 1016, 'humidity': 97, 'dew_point': 8.19, 'uvi': 0, 'clouds': 97, 'visibility': 5093, 'wind_speed': 0.42, 'wind_deg': 123, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 9.64, 'feels_like': 9.64, 'pressure': 1017, 'humidity': 98, 'dew_point': 9.34, 'uvi': 0, 'clouds': 100, 'visibility': 2611, 'wind_speed': 0.39, 'wind_deg': 131, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.64, 'feels_like': 8.64, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.34, 'uvi': 0, 'clouds': 100, 'visibility': 5063, 'wind_speed': 0.4, 'wind_deg': 128, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.64, 'feels_like': 8.64, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.34, 'uvi': 0, 'clouds': 100, 'visibility': 5021, 'wind_speed': 0.41, 'wind_deg': 147, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.64, 'feels_like': 8.64, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.34, 'uvi': 0, 'clouds': 100, 'visibility': 6071, 'wind_speed': 0.42, 'wind_deg': 172, 'wind_gust': 0.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 6.64, 'feels_like': 6.64, 'pressure': 1018, 'humidity': 97, 'dew_point': 6.2, 'uvi': 0, 'clouds': 100, 'visibility': 7553, 'wind_speed': 0.33, 'wind_deg': 190, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 4.64, 'feels_like': 4.64, 'pressure': 1017, 'humidity': 98, 'dew_point': 4.35, 'uvi': 0, 'clouds': 84, 'visibility': 6783, 'wind_speed': 0.26, 'wind_deg': 181, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641798000, 'temp': 3.64, 'feels_like': 3.64, 'pressure': 1016, 'humidity': 98, 'dew_point': 3.35, 'uvi': 0, 'clouds': 91, 'visibility': 4942, 'wind_speed': 0.4, 'wind_deg': 201, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 3.64, 'feels_like': 3.64, 'pressure': 1016, 'humidity': 98, 'dew_point': 3.35, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 227, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 3.64, 'feels_like': 3.64, 'pressure': 1016, 'humidity': 98, 'dew_point': 3.35, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 232, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.64, 'feels_like': 4.64, 'pressure': 1017, 'humidity': 98, 'dew_point': 4.35, 'uvi': 0, 'clouds': 83, 'visibility': 8997, 'wind_speed': 0.51, 'wind_deg': 263, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 5.64, 'feels_like': 5.64, 'pressure': 1018, 'humidity': 97, 'dew_point': 5.2, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 260, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 5.64, 'feels_like': 5.64, 'pressure': 1019, 'humidity': 96, 'dew_point': 5.05, 'uvi': 0.42, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 236, 'wind_gust': 0.96, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 6.64, 'feels_like': 6.64, 'pressure': 1019, 'humidity': 87, 'dew_point': 4.63, 'uvi': 2.46, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 258, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 9.64, 'feels_like': 9.64, 'pressure': 1019, 'humidity': 72, 'dew_point': 4.85, 'uvi': 5.81, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 262, 'wind_gust': 1.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 11.64, 'feels_like': 10.37, 'pressure': 1017, 'humidity': 58, 'dew_point': 3.66, 'uvi': 9.73, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 269, 'wind_gust': 2.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 12.64, 'feels_like': 11.37, 'pressure': 1016, 'humidity': 54, 'dew_point': 3.58, 'uvi': 9.4, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 100, 'wind_gust': 2.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 12.64, 'feels_like': 11.45, 'pressure': 1015, 'humidity': 57, 'dew_point': 4.35, 'uvi': 10.18, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 117, 'wind_gust': 2.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 13.64, 'feels_like': 12.91, 'pressure': 1015, 'humidity': 71, 'dew_point': 8.49, 'uvi': 9.17, 'clouds': 68, 'visibility': 9545, 'wind_speed': 0.81, 'wind_deg': 118, 'wind_gust': 2.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 13.64, 'feels_like': 12.97, 'pressure': 1013, 'humidity': 73, 'dew_point': 8.9, 'uvi': 7.23, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 83, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641844800, 'temp': 13.64, 'feels_like': 13.12, 'pressure': 1013, 'humidity': 79, 'dew_point': 10.07, 'uvi': 4.16, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 118, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641848400, 'temp': 13.64, 'feels_like': 13.33, 'pressure': 1013, 'humidity': 87, 'dew_point': 11.52, 'uvi': 1.65, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 172, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641852000, 'temp': 12.64, 'feels_like': 12.36, 'pressure': 1014, 'humidity': 92, 'dew_point': 11.38, 'uvi': 0.41, 'clouds': 89, 'visibility': 7906, 'wind_speed': 0.68, 'wind_deg': 155, 'wind_gust': 1.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641855600, 'temp': 10.64, 'feels_like': 10.29, 'pressure': 1016, 'humidity': 97, 'dew_point': 10.18, 'uvi': 0, 'clouds': 91, 'visibility': 4813, 'wind_speed': 0.58, 'wind_deg': 155, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 00:00:00 | 97.000000 | 8.190000 | 8.640000 | 97.000000 | 1016.000000 |  | 8.640000 | 0.000000 | 5093.000000 | 123.000000 | 1.02 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.340000 | 9.640000 | 98.000000 | 1017.000000 |  | 9.640000 | 0.000000 | 2611.000000 | 131.000000 | 0.95 | 0.390000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 8.340000 | 8.640000 | 98.000000 | 1018.000000 |  | 8.640000 | 0.000000 | 5063.000000 | 128.000000 | 0.92 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 8.340000 | 8.640000 | 98.000000 | 1018.000000 |  | 8.640000 | 0.000000 | 5021.000000 | 147.000000 | 1.07 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 8.340000 | 8.640000 | 98.000000 | 1018.000000 |  | 8.640000 | 0.000000 | 6071.000000 | 172.000000 | 0.97 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 6.200000 | 6.640000 | 97.000000 | 1018.000000 | 0.12 | 6.640000 | 0.000000 | 7553.000000 | 190.000000 | 0.83 | 0.330000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 06:00:00 | 84.000000 | 4.350000 | 4.640000 | 98.000000 | 1017.000000 | 0.12 | 4.640000 | 0.000000 | 6783.000000 | 181.000000 | 0.69 | 0.260000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 07:00:00 | 91.000000 | 3.350000 | 3.640000 | 98.000000 | 1016.000000 |  | 3.640000 | 0.000000 | 4942.000000 | 201.000000 | 0.74 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 3.350000 | 3.640000 | 98.000000 | 1016.000000 |  | 3.640000 | 0.000000 | 10000.000000 | 227.000000 | 0.96 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 09:00:00 | 83.000000 | 3.350000 | 3.640000 | 98.000000 | 1016.000000 |  | 3.640000 | 0.000000 | 10000.000000 | 232.000000 | 0.89 | 0.620000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 10:00:00 | 83.000000 | 4.350000 | 4.640000 | 98.000000 | 1017.000000 |  | 4.640000 | 0.000000 | 8997.000000 | 263.000000 | 0.73 | 0.510000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 11:00:00 | 82.000000 | 5.200000 | 5.640000 | 97.000000 | 1018.000000 |  | 5.640000 | 0.000000 | 10000.000000 | 260.000000 | 0.86 | 0.650000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 12:00:00 | 80.000000 | 5.050000 | 5.640000 | 96.000000 | 1019.000000 |  | 5.640000 | 0.420000 | 10000.000000 | 236.000000 | 0.96 | 0.490000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 4.630000 | 6.640000 | 87.000000 | 1019.000000 |  | 6.640000 | 2.460000 | 10000.000000 | 258.000000 | 1.1 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 14:00:00 | 85.000000 | 4.850000 | 9.640000 | 72.000000 | 1019.000000 |  | 9.640000 | 5.810000 | 10000.000000 | 262.000000 | 1.36 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 15:00:00 | 72.000000 | 3.660000 | 10.370000 | 58.000000 | 1017.000000 |  | 11.640000 | 9.730000 | 10000.000000 | 269.000000 | 2.02 | 0.340000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 16:00:00 | 71.000000 | 3.580000 | 11.370000 | 54.000000 | 1016.000000 |  | 12.640000 | 9.400000 | 10000.000000 | 100.000000 | 2.56 | 0.080000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 17:00:00 | 73.000000 | 4.350000 | 11.450000 | 57.000000 | 1015.000000 | 0.11 | 12.640000 | 10.180000 | 10000.000000 | 117.000000 | 2.46 | 0.530000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 18:00:00 | 68.000000 | 8.490000 | 12.910000 | 71.000000 | 1015.000000 |  | 13.640000 | 9.170000 | 9545.000000 | 118.000000 | 2.02 | 0.810000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 19:00:00 | 77.000000 | 8.900000 | 12.970000 | 73.000000 | 1013.000000 | 0.24 | 13.640000 | 7.230000 | 10000.000000 | 83.000000 | 1.94 | 0.460000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 20:00:00 | 85.000000 | 10.070000 | 13.120000 | 79.000000 | 1013.000000 | 0.44 | 13.640000 | 4.160000 | 10000.000000 | 118.000000 | 1.79 | 0.300000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 11.520000 | 13.330000 | 87.000000 | 1013.000000 | 0.56 | 13.640000 | 1.650000 | 10000.000000 | 172.000000 | 1.74 | 0.590000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 11.380000 | 12.360000 | 92.000000 | 1014.000000 | 0.22 | 12.640000 | 0.410000 | 7906.000000 | 155.000000 | 1.74 | 0.680000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025080 | "PNN CHINGAZA - AUT [35025080]" | 4.661000 | -73.827333 | 3205.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-12-06 00:00:00 | NaT | Cundinamarca | La Calera | Otun | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 10.180000 | 10.290000 | 97.000000 | 1016.000000 | 0.22 | 10.640000 | 0.000000 | 4813.000000 | 155.000000 | 1.55 | 0.580000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station35025080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35025080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35025080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025080_OWM_Windspeed_20220111.png)
