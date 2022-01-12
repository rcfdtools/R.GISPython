
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PARAMO RABANAL - AUT [35075080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35075080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.39238889,-73.56277778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.39238889&lon=-73.56277778)


| Parameter | Value |
|---|---|
| Code | 35075080 |
| Name | PARAMO RABANAL - AUT [35075080] |
| Latitude, ° | 5.39238889 |
| Longitude, ° | -73.56277778 |
| Elevation, m | 3398 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-03-13 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Ventaquemada |
| Stream | Bogota |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Garagoa |

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

### (CNE index 122) Open Weather values for station 35075080 - PARAMO RABANAL - AUT [35075080]

JSON data from API OWM:

```
{'lat': 5.3924, 'lon': -73.5628, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812801, 'sunset': 1641855388, 'temp': 11.9, 'feels_like': 10.97, 'pressure': 1012, 'humidity': 70, 'dew_point': 6.61, 'uvi': 3.53, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 276, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, 'hourly': [{'dt': 1641772800, 'temp': 7.49, 'feels_like': 7.49, 'pressure': 1016, 'humidity': 95, 'dew_point': 6.74, 'uvi': 0, 'clouds': 80, 'visibility': 5357, 'wind_speed': 0.57, 'wind_deg': 345, 'wind_gust': 1.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 7.44, 'feels_like': 7.44, 'pressure': 1017, 'humidity': 95, 'dew_point': 6.69, 'uvi': 0, 'clouds': 93, 'visibility': 5353, 'wind_speed': 0.67, 'wind_deg': 2, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 6.93, 'feels_like': 6.93, 'pressure': 1018, 'humidity': 96, 'dew_point': 6.34, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 350, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 6.89, 'feels_like': 6.89, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.99, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 349, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 6.78, 'feels_like': 6.78, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.88, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 7, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 6.5, 'feels_like': 6.5, 'pressure': 1018, 'humidity': 94, 'dew_point': 5.61, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 80, 'wind_gust': 0.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 6.38, 'feels_like': 6.38, 'pressure': 1017, 'humidity': 93, 'dew_point': 5.33, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 83, 'wind_gust': 0.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 5.39, 'feels_like': 5.39, 'pressure': 1016, 'humidity': 93, 'dew_point': 4.35, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.07, 'wind_deg': 69, 'wind_gust': 0.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 4.79, 'feels_like': 4.79, 'pressure': 1016, 'humidity': 92, 'dew_point': 3.6, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 321, 'wind_gust': 0.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 4.45, 'feels_like': 4.45, 'pressure': 1016, 'humidity': 93, 'dew_point': 3.42, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 343, 'wind_gust': 0.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.06, 'feels_like': 4.06, 'pressure': 1017, 'humidity': 94, 'dew_point': 3.18, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 339, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.53, 'feels_like': 3.53, 'pressure': 1018, 'humidity': 95, 'dew_point': 2.81, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 299, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 5.32, 'feels_like': 5.32, 'pressure': 1019, 'humidity': 90, 'dew_point': 3.81, 'uvi': 0.55, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 283, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 8.28, 'feels_like': 8.28, 'pressure': 1019, 'humidity': 79, 'dew_point': 4.86, 'uvi': 2.29, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 262, 'wind_gust': 0.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.85, 'feels_like': 9.74, 'pressure': 1018, 'humidity': 67, 'dew_point': 4.97, 'uvi': 5.42, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 241, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 13.05, 'feels_like': 11.9, 'pressure': 1017, 'humidity': 57, 'dew_point': 4.74, 'uvi': 9.1, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 291, 'wind_gust': 2.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 14.07, 'feels_like': 12.86, 'pressure': 1016, 'humidity': 51, 'dew_point': 4.1, 'uvi': 11.35, 'clouds': 53, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 329, 'wind_gust': 2.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 14.11, 'feels_like': 12.93, 'pressure': 1014, 'humidity': 52, 'dew_point': 4.41, 'uvi': 12.28, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 336, 'wind_gust': 2.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 13.83, 'feels_like': 12.76, 'pressure': 1013, 'humidity': 57, 'dew_point': 5.47, 'uvi': 11.06, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 315, 'wind_gust': 2.29, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 12.64, 'feels_like': 11.63, 'pressure': 1012, 'humidity': 64, 'dew_point': 6.02, 'uvi': 6.14, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 288, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641844800, 'temp': 11.9, 'feels_like': 10.97, 'pressure': 1012, 'humidity': 70, 'dew_point': 6.61, 'uvi': 3.53, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 276, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641848400, 'temp': 10.79, 'feels_like': 9.96, 'pressure': 1012, 'humidity': 78, 'dew_point': 7.11, 'uvi': 1.4, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 294, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641852000, 'temp': 9.82, 'feels_like': 9.82, 'pressure': 1013, 'humidity': 84, 'dew_point': 7.25, 'uvi': 0.33, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 359, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641855600, 'temp': 7.87, 'feels_like': 7.87, 'pressure': 1015, 'humidity': 93, 'dew_point': 6.81, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 335, 'wind_gust': 1.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 00:00:00 | 80.000000 | 6.740000 | 7.490000 | 95.000000 | 1016.000000 |  | 7.490000 | 0.000000 | 5357.000000 | 345.000000 | 1.29 | 0.570000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 01:00:00 | 93.000000 | 6.690000 | 7.440000 | 95.000000 | 1017.000000 |  | 7.440000 | 0.000000 | 5353.000000 | 2.000000 | 1.22 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 02:00:00 | 91.000000 | 6.340000 | 6.930000 | 96.000000 | 1018.000000 |  | 6.930000 | 0.000000 | 10000.000000 | 350.000000 | 1.2 | 0.740000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 5.990000 | 6.890000 | 94.000000 | 1018.000000 |  | 6.890000 | 0.000000 | 10000.000000 | 349.000000 | 1.1 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 5.880000 | 6.780000 | 94.000000 | 1018.000000 |  | 6.780000 | 0.000000 | 10000.000000 | 7.000000 | 0.87 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 05:00:00 | 92.000000 | 5.610000 | 6.500000 | 94.000000 | 1018.000000 |  | 6.500000 | 0.000000 | 10000.000000 | 80.000000 | 0.58 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 06:00:00 | 58.000000 | 5.330000 | 6.380000 | 93.000000 | 1017.000000 |  | 6.380000 | 0.000000 | 10000.000000 | 83.000000 | 0.57 | 0.340000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 07:00:00 | 74.000000 | 4.350000 | 5.390000 | 93.000000 | 1016.000000 |  | 5.390000 | 0.000000 | 10000.000000 | 69.000000 | 0.44 | 0.070000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 08:00:00 | 71.000000 | 3.600000 | 4.790000 | 92.000000 | 1016.000000 |  | 4.790000 | 0.000000 | 10000.000000 | 321.000000 | 0.54 | 0.230000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 09:00:00 | 70.000000 | 3.420000 | 4.450000 | 93.000000 | 1016.000000 |  | 4.450000 | 0.000000 | 10000.000000 | 343.000000 | 0.71 | 0.510000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 10:00:00 | 69.000000 | 3.180000 | 4.060000 | 94.000000 | 1017.000000 |  | 4.060000 | 0.000000 | 10000.000000 | 339.000000 | 0.76 | 0.590000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 11:00:00 | 71.000000 | 2.810000 | 3.530000 | 95.000000 | 1018.000000 |  | 3.530000 | 0.000000 | 10000.000000 | 299.000000 | 0.84 | 0.480000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 12:00:00 | 64.000000 | 3.810000 | 5.320000 | 90.000000 | 1019.000000 |  | 5.320000 | 0.550000 | 10000.000000 | 283.000000 | 0.75 | 0.370000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 13:00:00 | 67.000000 | 4.860000 | 8.280000 | 79.000000 | 1019.000000 |  | 8.280000 | 2.290000 | 10000.000000 | 262.000000 | 0.64 | 0.330000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 14:00:00 | 62.000000 | 4.970000 | 9.740000 | 67.000000 | 1018.000000 |  | 10.850000 | 5.420000 | 10000.000000 | 241.000000 | 1.03 | 0.320000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 15:00:00 | 51.000000 | 4.740000 | 11.900000 | 57.000000 | 1017.000000 |  | 13.050000 | 9.100000 | 10000.000000 | 291.000000 | 2.07 | 0.690000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 16:00:00 | 53.000000 | 4.100000 | 12.860000 | 51.000000 | 1016.000000 |  | 14.070000 | 11.350000 | 10000.000000 | 329.000000 | 2.61 | 1.230000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 17:00:00 | 61.000000 | 4.410000 | 12.930000 | 52.000000 | 1014.000000 |  | 14.110000 | 12.280000 | 10000.000000 | 336.000000 | 2.43 | 1.320000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 18:00:00 | 71.000000 | 5.470000 | 12.760000 | 57.000000 | 1013.000000 |  | 13.830000 | 11.060000 | 10000.000000 | 315.000000 | 2.29 | 0.940000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 6.020000 | 11.630000 | 64.000000 | 1012.000000 | 0.15 | 12.640000 | 6.140000 | 10000.000000 | 288.000000 | 2.01 | 0.700000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 20:00:00 | 88.000000 | 6.610000 | 10.970000 | 70.000000 | 1012.000000 | 0.31 | 11.900000 | 3.530000 | 10000.000000 | 276.000000 | 1.9 | 0.520000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 21:00:00 | 89.000000 | 7.110000 | 9.960000 | 78.000000 | 1012.000000 | 0.54 | 10.790000 | 1.400000 | 10000.000000 | 294.000000 | 1.78 | 0.350000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 22:00:00 | 85.000000 | 7.250000 | 9.820000 | 84.000000 | 1013.000000 | 0.47 | 9.820000 | 0.330000 | 10000.000000 | 359.000000 | 1.67 | 0.280000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35075080 | "PARAMO RABANAL - AUT [35075080]" | 5.392389 | -73.562778 | 3398.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-13 00:00:00 | NaT | Boyacá | Ventaquemada | Bogota | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 23:00:00 | 85.000000 | 6.810000 | 7.870000 | 93.000000 | 1015.000000 | 0.34 | 7.870000 | 0.000000 | 10000.000000 | 335.000000 | 1.39 | 0.360000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station35075080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35075080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35075080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075080_OWM_Windspeed_20220111.png)
