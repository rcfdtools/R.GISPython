
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ISLA DEL SANTUARIO [24015120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24015120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.46727778,-73.73480556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.46727778&lon=-73.73480556)


| Parameter | Value |
|---|---|
| Code | 24015120 |
| Name | ISLA DEL SANTUARIO [24015120] |
| Latitude, ° | 5.46727778 |
| Longitude, ° | -73.73480556 |
| Elevation, m | 2580 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1942-05-15 00:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | Fúquene |
| Stream | Gachaneca |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
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

### (CNE index 1543) Open Weather values for station 24015120 - ISLA DEL SANTUARIO [24015120]

JSON data from API OWM:

```
{'lat': 5.4673, 'lon': -73.7348, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812850, 'sunset': 1641855422, 'temp': 16.24, 'feels_like': 15.98, 'pressure': 1012, 'humidity': 79, 'dew_point': 12.6, 'uvi': 3.53, 'clouds': 72, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 312, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, 'hourly': [{'dt': 1641772800, 'temp': 12.5, 'feels_like': 12.29, 'pressure': 1016, 'humidity': 95, 'dew_point': 11.72, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 318, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 12.57, 'feels_like': 12.34, 'pressure': 1017, 'humidity': 94, 'dew_point': 11.63, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 338, 'wind_gust': 1.41, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 12.16, 'feels_like': 11.89, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.22, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 330, 'wind_gust': 1.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.07, 'feels_like': 11.79, 'pressure': 1018, 'humidity': 94, 'dew_point': 11.13, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 338, 'wind_gust': 1.17, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 11.93, 'feels_like': 11.63, 'pressure': 1018, 'humidity': 94, 'dew_point': 11, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 356, 'wind_gust': 0.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 11.19, 'feels_like': 10.85, 'pressure': 1018, 'humidity': 95, 'dew_point': 10.42, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 38, 'wind_gust': 0.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 10.46, 'feels_like': 10.02, 'pressure': 1017, 'humidity': 94, 'dew_point': 9.54, 'uvi': 0, 'clouds': 19, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 98, 'wind_gust': 0.34, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641798000, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.61, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 183, 'wind_gust': 0.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 8.84, 'feels_like': 8.84, 'pressure': 1016, 'humidity': 95, 'dew_point': 8.08, 'uvi': 0, 'clouds': 32, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 156, 'wind_gust': 0.62, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 8.49, 'feels_like': 8.49, 'pressure': 1017, 'humidity': 96, 'dew_point': 7.89, 'uvi': 0, 'clouds': 35, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 146, 'wind_gust': 0.5, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 8.21, 'feels_like': 8.21, 'pressure': 1017, 'humidity': 96, 'dew_point': 7.61, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 117, 'wind_gust': 0.58, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 8.05, 'feels_like': 8.05, 'pressure': 1018, 'humidity': 96, 'dew_point': 7.45, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 178, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1019, 'humidity': 92, 'dew_point': 8.66, 'uvi': 0.55, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 168, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 13, 'feels_like': 12.5, 'pressure': 1019, 'humidity': 82, 'dew_point': 10, 'uvi': 2.29, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 229, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 15.59, 'feels_like': 15.03, 'pressure': 1018, 'humidity': 70, 'dew_point': 10.15, 'uvi': 5.42, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 278, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.47, 'feels_like': 16.87, 'pressure': 1017, 'humidity': 61, 'dew_point': 9.88, 'uvi': 9.1, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 303, 'wind_gust': 2.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.41, 'feels_like': 17.79, 'pressure': 1016, 'humidity': 57, 'dew_point': 9.75, 'uvi': 11.35, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.11, 'wind_deg': 319, 'wind_gust': 2.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 18.52, 'feels_like': 17.94, 'pressure': 1015, 'humidity': 58, 'dew_point': 10.11, 'uvi': 12.28, 'clouds': 64, 'visibility': 10000, 'wind_speed': 2.55, 'wind_deg': 315, 'wind_gust': 2.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 17.96, 'feels_like': 17.48, 'pressure': 1014, 'humidity': 64, 'dew_point': 11.06, 'uvi': 11.06, 'clouds': 67, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 312, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641841200, 'temp': 17.09, 'feels_like': 16.71, 'pressure': 1013, 'humidity': 71, 'dew_point': 11.8, 'uvi': 6.14, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.52, 'wind_deg': 313, 'wind_gust': 2.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641844800, 'temp': 16.24, 'feels_like': 15.98, 'pressure': 1012, 'humidity': 79, 'dew_point': 12.6, 'uvi': 3.53, 'clouds': 72, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 312, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641848400, 'temp': 15.33, 'feels_like': 15.09, 'pressure': 1013, 'humidity': 83, 'dew_point': 12.46, 'uvi': 1.4, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 307, 'wind_gust': 2.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641852000, 'temp': 14.34, 'feels_like': 14.1, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.21, 'uvi': 0.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641855600, 'temp': 12.67, 'feels_like': 12.42, 'pressure': 1015, 'humidity': 93, 'dew_point': 11.57, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 322, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 00:00:00 | 89.000000 | 11.720000 | 12.290000 | 95.000000 | 1016.000000 |  | 12.500000 | 0.000000 | 10000.000000 | 318.000000 | 1.35 | 1.080000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 01:00:00 | 99.000000 | 11.630000 | 12.340000 | 94.000000 | 1017.000000 |  | 12.570000 | 0.000000 | 10000.000000 | 338.000000 | 1.41 | 1.070000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 11.220000 | 11.890000 | 94.000000 | 1018.000000 |  | 12.160000 | 0.000000 | 10000.000000 | 330.000000 | 1.38 | 1.050000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 11.130000 | 11.790000 | 94.000000 | 1018.000000 |  | 12.070000 | 0.000000 | 10000.000000 | 338.000000 | 1.17 | 0.940000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 11.000000 | 11.630000 | 94.000000 | 1018.000000 |  | 11.930000 | 0.000000 | 10000.000000 | 356.000000 | 0.82 | 0.680000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 05:00:00 | 98.000000 | 10.420000 | 10.850000 | 95.000000 | 1018.000000 |  | 11.190000 | 0.000000 | 10000.000000 | 38.000000 | 0.35 | 0.160000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 06:00:00 | 19.000000 | 9.540000 | 10.020000 | 94.000000 | 1017.000000 |  | 10.460000 | 0.000000 | 10000.000000 | 98.000000 | 0.34 | 0.230000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 07:00:00 | 38.000000 | 8.610000 | 9.370000 | 95.000000 | 1016.000000 |  | 9.370000 | 0.000000 | 10000.000000 | 183.000000 | 0.6 | 0.410000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 08:00:00 | 32.000000 | 8.080000 | 8.840000 | 95.000000 | 1016.000000 |  | 8.840000 | 0.000000 | 10000.000000 | 156.000000 | 0.62 | 0.390000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 09:00:00 | 35.000000 | 7.890000 | 8.490000 | 96.000000 | 1017.000000 |  | 8.490000 | 0.000000 | 10000.000000 | 146.000000 | 0.5 | 0.150000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 10:00:00 | 42.000000 | 7.610000 | 8.210000 | 96.000000 | 1017.000000 |  | 8.210000 | 0.000000 | 10000.000000 | 117.000000 | 0.58 | 0.300000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 11:00:00 | 51.000000 | 7.450000 | 8.050000 | 96.000000 | 1018.000000 |  | 8.050000 | 0.000000 | 10000.000000 | 178.000000 | 0.89 | 0.620000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 12:00:00 | 89.000000 | 8.660000 | 9.900000 | 92.000000 | 1019.000000 |  | 9.900000 | 0.550000 | 10000.000000 | 168.000000 | 0.76 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 13:00:00 | 91.000000 | 10.000000 | 12.500000 | 82.000000 | 1019.000000 |  | 13.000000 | 2.290000 | 10000.000000 | 229.000000 | 0.65 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 14:00:00 | 89.000000 | 10.150000 | 15.030000 | 70.000000 | 1018.000000 |  | 15.590000 | 5.420000 | 10000.000000 | 278.000000 | 1.18 | 0.750000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 15:00:00 | 69.000000 | 9.880000 | 16.870000 | 61.000000 | 1017.000000 |  | 17.470000 | 9.100000 | 10000.000000 | 303.000000 | 2.02 | 1.560000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 16:00:00 | 63.000000 | 9.750000 | 17.790000 | 57.000000 | 1016.000000 | 0.11 | 18.410000 | 11.350000 | 10000.000000 | 319.000000 | 2.41 | 2.110000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 17:00:00 | 64.000000 | 10.110000 | 17.940000 | 58.000000 | 1015.000000 |  | 18.520000 | 12.280000 | 10000.000000 | 315.000000 | 2.57 | 2.550000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 18:00:00 | 67.000000 | 11.060000 | 17.480000 | 64.000000 | 1014.000000 | 0.16 | 17.960000 | 11.060000 | 10000.000000 | 312.000000 | 2.13 | 2.540000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 11.800000 | 16.710000 | 71.000000 | 1013.000000 | 0.44 | 17.090000 | 6.140000 | 10000.000000 | 313.000000 | 2.36 | 2.520000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 20:00:00 | 72.000000 | 12.600000 | 15.980000 | 79.000000 | 1012.000000 | 0.63 | 16.240000 | 3.530000 | 10000.000000 | 312.000000 | 2.38 | 2.160000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 21:00:00 | 72.000000 | 12.460000 | 15.090000 | 83.000000 | 1013.000000 | 0.41 | 15.330000 | 1.400000 | 10000.000000 | 307.000000 | 2.24 | 1.960000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 12.210000 | 14.100000 | 87.000000 | 1014.000000 | 0.32 | 14.340000 | 0.330000 | 10000.000000 | 320.000000 | 1.94 | 1.540000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24015120 | "ISLA DEL SANTUARIO [24015120]" | 5.467278 | -73.734806 | 2580.000000 | Climática Principal | Convencional | Activa | 1942-05-15 00:00:00 | NaT | Cundinamarca | Fúquene | Gachaneca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 23:00:00 | 78.000000 | 11.570000 | 12.420000 | 93.000000 | 1015.000000 | 0.17 | 12.670000 | 0.000000 | 10000.000000 | 322.000000 | 1.3 | 1.260000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24015120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24015120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24015120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015120_OWM_Windspeed_20220111.png)
