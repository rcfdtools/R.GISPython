
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - INSTITUCION AGRICOLA MACANAL [35075040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35075040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.97436111,-73.31675) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.97436111&lon=-73.31675)


| Parameter | Value |
|---|---|
| Code | 35075040 |
| Name | INSTITUCION AGRICOLA MACANAL [35075040] |
| Latitude, ° | 4.97436111 |
| Longitude, ° | -73.31675 |
| Elevation, m | 1300 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1982-07-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Macanal |
| Stream | Lagunilla |
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

### (CNE index 356) Open Weather values for station 35075040 - INSTITUCION AGRICOLA MACANAL [35075040]

JSON data from API OWM:

```
{'lat': 4.9744, 'lon': -73.3168, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812702, 'sunset': 1641855369, 'temp': 18.04, 'feels_like': 17.81, 'pressure': 1012, 'humidity': 73, 'dew_point': 13.13, 'uvi': 2.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 129, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 14.77, 'feels_like': 14.6, 'pressure': 1016, 'humidity': 88, 'dew_point': 12.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 291, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 14.64, 'feels_like': 14.46, 'pressure': 1016, 'humidity': 88, 'dew_point': 12.68, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 303, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 14.67, 'feels_like': 14.46, 'pressure': 1017, 'humidity': 87, 'dew_point': 12.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 278, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 14.73, 'feels_like': 14.5, 'pressure': 1017, 'humidity': 86, 'dew_point': 12.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 276, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 14.58, 'feels_like': 14.34, 'pressure': 1017, 'humidity': 86, 'dew_point': 12.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 268, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 14.54, 'feels_like': 14.32, 'pressure': 1017, 'humidity': 87, 'dew_point': 12.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 286, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.39, 'feels_like': 14.18, 'pressure': 1016, 'humidity': 88, 'dew_point': 12.43, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 294, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.18, 'feels_like': 13.95, 'pressure': 1015, 'humidity': 88, 'dew_point': 12.22, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 281, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 13.81, 'feels_like': 13.57, 'pressure': 1014, 'humidity': 89, 'dew_point': 12.03, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 301, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 12.89, 'feels_like': 12.64, 'pressure': 1015, 'humidity': 92, 'dew_point': 11.62, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 313, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 12.69, 'feels_like': 12.42, 'pressure': 1015, 'humidity': 92, 'dew_point': 11.43, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 304, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 12.74, 'feels_like': 12.47, 'pressure': 1016, 'humidity': 92, 'dew_point': 11.47, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.98, 'wind_deg': 294, 'wind_gust': 0.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 14.51, 'feels_like': 14.21, 'pressure': 1017, 'humidity': 84, 'dew_point': 11.84, 'uvi': 0.25, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 275, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 16.54, 'feels_like': 16.21, 'pressure': 1018, 'humidity': 75, 'dew_point': 12.1, 'uvi': 2.12, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 151, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 18.31, 'feels_like': 17.92, 'pressure': 1018, 'humidity': 66, 'dew_point': 11.86, 'uvi': 4.93, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 127, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 19.26, 'feels_like': 18.89, 'pressure': 1017, 'humidity': 63, 'dew_point': 12.05, 'uvi': 8.18, 'clouds': 85, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 118, 'wind_gust': 1.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 19.16, 'feels_like': 18.8, 'pressure': 1016, 'humidity': 64, 'dew_point': 12.19, 'uvi': 8.56, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 117, 'wind_gust': 1.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.09, 'feels_like': 18.75, 'pressure': 1015, 'humidity': 65, 'dew_point': 12.36, 'uvi': 9.21, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 134, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 18.98, 'feels_like': 18.71, 'pressure': 1015, 'humidity': 68, 'dew_point': 12.95, 'uvi': 8.25, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 132, 'wind_gust': 1.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 18.15, 'feels_like': 17.9, 'pressure': 1013, 'humidity': 72, 'dew_point': 13.03, 'uvi': 4.76, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 130, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 18.04, 'feels_like': 17.81, 'pressure': 1012, 'humidity': 73, 'dew_point': 13.13, 'uvi': 2.71, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 129, 'wind_gust': 1.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 17.26, 'feels_like': 17.05, 'pressure': 1013, 'humidity': 77, 'dew_point': 13.19, 'uvi': 1.06, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 132, 'wind_gust': 1.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641852000, 'temp': 16.28, 'feels_like': 16.13, 'pressure': 1013, 'humidity': 83, 'dew_point': 13.39, 'uvi': 0.23, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 141, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 15.38, 'feels_like': 15.25, 'pressure': 1014, 'humidity': 87, 'dew_point': 13.23, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 187, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 12.800000 | 14.600000 | 88.000000 | 1016.000000 |  | 14.770000 | 0.000000 | 10000.000000 | 291.000000 | 0.81 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 12.680000 | 14.460000 | 88.000000 | 1016.000000 |  | 14.640000 | 0.000000 | 10000.000000 | 303.000000 | 0.84 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 12.530000 | 14.460000 | 87.000000 | 1017.000000 |  | 14.670000 | 0.000000 | 10000.000000 | 278.000000 | 0.96 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 12.410000 | 14.500000 | 86.000000 | 1017.000000 |  | 14.730000 | 0.000000 | 10000.000000 | 276.000000 | 0.92 | 0.530000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 12.270000 | 14.340000 | 86.000000 | 1017.000000 |  | 14.580000 | 0.000000 | 10000.000000 | 268.000000 | 0.9 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 12.400000 | 14.320000 | 87.000000 | 1017.000000 |  | 14.540000 | 0.000000 | 10000.000000 | 286.000000 | 1.09 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 06:00:00 | 77.000000 | 12.430000 | 14.180000 | 88.000000 | 1016.000000 |  | 14.390000 | 0.000000 | 10000.000000 | 294.000000 | 1.03 | 0.600000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 12.220000 | 13.950000 | 88.000000 | 1015.000000 |  | 14.180000 | 0.000000 | 10000.000000 | 281.000000 | 0.83 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 08:00:00 | 93.000000 | 12.030000 | 13.570000 | 89.000000 | 1014.000000 |  | 13.810000 | 0.000000 | 10000.000000 | 301.000000 | 0.68 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 09:00:00 | 85.000000 | 11.620000 | 12.640000 | 92.000000 | 1015.000000 |  | 12.890000 | 0.000000 | 10000.000000 | 313.000000 | 0.67 | 0.730000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 10:00:00 | 79.000000 | 11.430000 | 12.420000 | 92.000000 | 1015.000000 |  | 12.690000 | 0.000000 | 10000.000000 | 304.000000 | 0.8 | 0.920000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 11.470000 | 12.470000 | 92.000000 | 1016.000000 |  | 12.740000 | 0.000000 | 10000.000000 | 294.000000 | 0.87 | 0.980000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 12:00:00 | 65.000000 | 11.840000 | 14.210000 | 84.000000 | 1017.000000 |  | 14.510000 | 0.250000 | 10000.000000 | 275.000000 | 0.85 | 0.430000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 12.100000 | 16.210000 | 75.000000 | 1018.000000 |  | 16.540000 | 2.120000 | 10000.000000 | 151.000000 | 0.87 | 0.750000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 14:00:00 | 91.000000 | 11.860000 | 17.920000 | 66.000000 | 1018.000000 |  | 18.310000 | 4.930000 | 10000.000000 | 127.000000 | 1.11 | 1.510000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 15:00:00 | 85.000000 | 12.050000 | 18.890000 | 63.000000 | 1017.000000 |  | 19.260000 | 8.180000 | 10000.000000 | 118.000000 | 1.64 | 2.060000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 12.190000 | 18.800000 | 64.000000 | 1016.000000 |  | 19.160000 | 8.560000 | 10000.000000 | 117.000000 | 1.75 | 2.260000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 12.360000 | 18.750000 | 65.000000 | 1015.000000 |  | 19.090000 | 9.210000 | 10000.000000 | 134.000000 | 2.07 | 2.460000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 18:00:00 | 84.000000 | 12.950000 | 18.710000 | 68.000000 | 1015.000000 |  | 18.980000 | 8.250000 | 10000.000000 | 132.000000 | 1.84 | 2.170000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 19:00:00 | 97.000000 | 13.030000 | 17.900000 | 72.000000 | 1013.000000 |  | 18.150000 | 4.760000 | 10000.000000 | 130.000000 | 1.7 | 1.740000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 20:00:00 | 98.000000 | 13.130000 | 17.810000 | 73.000000 | 1012.000000 |  | 18.040000 | 2.710000 | 10000.000000 | 129.000000 | 1.72 | 1.520000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 13.190000 | 17.050000 | 77.000000 | 1013.000000 | 0.12 | 17.260000 | 1.060000 | 10000.000000 | 132.000000 | 1.91 | 1.310000 | 500 | Rain | light rain | 10d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 13.390000 | 16.130000 | 83.000000 | 1013.000000 |  | 16.280000 | 0.230000 | 10000.000000 | 141.000000 | 1.7 | 0.970000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35075040 | "INSTITUCION AGRICOLA MACANAL [35075040]" | 4.974361 | -73.316750 | 1300.000000 | Climática Principal | Convencional | Activa | 1982-07-15 00:00:00 | NaT | Boyacá | Macanal | Lagunilla | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 13.230000 | 15.250000 | 87.000000 | 1014.000000 |  | 15.380000 | 0.000000 | 10000.000000 | 187.000000 | 1.23 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35075040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35075040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35075040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35075040_OWM_Windspeed_20220111.png)
