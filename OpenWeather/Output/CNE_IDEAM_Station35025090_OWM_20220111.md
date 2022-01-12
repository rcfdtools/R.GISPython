
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BOSQUE INTERVENIDO  - AUT [35025090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.66488889,-73.84663889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.66488889&lon=-73.84663889)


| Parameter | Value |
|---|---|
| Code | 35025090 |
| Name | BOSQUE INTERVENIDO  - AUT [35025090] |
| Latitude, ° | 4.66488889 |
| Longitude, ° | -73.84663889 |
| Elevation, m | 2944 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2008-07-08 19:00:00 |
| Suspension date | NaT |
| State | Cundinamarca |
| County | La Calera |
| Stream | 0 |
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

### (CNE index 335) Open Weather values for station 35025090 - BOSQUE INTERVENIDO  - AUT [35025090]

JSON data from API OWM:

```
{'lat': 4.6649, 'lon': -73.8466, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812799, 'sunset': 1641855526, 'temp': 15, 'feels_like': 14.59, 'pressure': 1013, 'humidity': 78, 'dew_point': 11.2, 'uvi': 4.16, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.05, 'wind_deg': 155, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, 'hourly': [{'dt': 1641772800, 'temp': 10, 'feels_like': 10, 'pressure': 1016, 'humidity': 97, 'dew_point': 9.55, 'uvi': 0, 'clouds': 96, 'visibility': 6450, 'wind_speed': 0.37, 'wind_deg': 126, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 11, 'feels_like': 10.69, 'pressure': 1017, 'humidity': 97, 'dew_point': 10.54, 'uvi': 0, 'clouds': 100, 'visibility': 3281, 'wind_speed': 0.34, 'wind_deg': 138, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 10, 'feels_like': 10, 'pressure': 1018, 'humidity': 97, 'dew_point': 9.55, 'uvi': 0, 'clouds': 100, 'visibility': 6420, 'wind_speed': 0.35, 'wind_deg': 134, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 10, 'feels_like': 10, 'pressure': 1018, 'humidity': 98, 'dew_point': 9.7, 'uvi': 0, 'clouds': 100, 'visibility': 6375, 'wind_speed': 0.38, 'wind_deg': 154, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10, 'feels_like': 10, 'pressure': 1018, 'humidity': 98, 'dew_point': 9.7, 'uvi': 0, 'clouds': 100, 'visibility': 7634, 'wind_speed': 0.4, 'wind_deg': 179, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 8, 'feels_like': 8, 'pressure': 1018, 'humidity': 97, 'dew_point': 7.55, 'uvi': 0, 'clouds': 100, 'visibility': 9356, 'wind_speed': 0.33, 'wind_deg': 193, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 6, 'feels_like': 6, 'pressure': 1017, 'humidity': 98, 'dew_point': 5.71, 'uvi': 0, 'clouds': 82, 'visibility': 8293, 'wind_speed': 0.25, 'wind_deg': 190, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641798000, 'temp': 5, 'feels_like': 5, 'pressure': 1016, 'humidity': 98, 'dew_point': 4.71, 'uvi': 0, 'clouds': 88, 'visibility': 5971, 'wind_speed': 0.41, 'wind_deg': 206, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 5, 'feels_like': 5, 'pressure': 1016, 'humidity': 98, 'dew_point': 4.71, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 229, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 5, 'feels_like': 5, 'pressure': 1016, 'humidity': 98, 'dew_point': 4.71, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 236, 'wind_gust': 0.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 6, 'feels_like': 6, 'pressure': 1017, 'humidity': 98, 'dew_point': 5.71, 'uvi': 0, 'clouds': 82, 'visibility': 8978, 'wind_speed': 0.46, 'wind_deg': 268, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 7, 'feels_like': 7, 'pressure': 1018, 'humidity': 97, 'dew_point': 6.56, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 262, 'wind_gust': 0.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 7, 'feels_like': 7, 'pressure': 1019, 'humidity': 95, 'dew_point': 6.26, 'uvi': 0.42, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 236, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 8, 'feels_like': 8, 'pressure': 1019, 'humidity': 86, 'dew_point': 5.8, 'uvi': 2.46, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 260, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 11, 'feels_like': 10.04, 'pressure': 1019, 'humidity': 72, 'dew_point': 6.15, 'uvi': 5.81, 'clouds': 83, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 264, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 13, 'feels_like': 11.87, 'pressure': 1017, 'humidity': 58, 'dew_point': 4.94, 'uvi': 9.73, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 280, 'wind_gust': 2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 14, 'feels_like': 12.84, 'pressure': 1015, 'humidity': 53, 'dew_point': 4.58, 'uvi': 9.4, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 319, 'wind_gust': 2.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 14, 'feels_like': 12.92, 'pressure': 1014, 'humidity': 56, 'dew_point': 5.37, 'uvi': 10.18, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 115, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641837600, 'temp': 15, 'feels_like': 14.36, 'pressure': 1014, 'humidity': 69, 'dew_point': 9.37, 'uvi': 9.17, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 119, 'wind_gust': 2.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 15, 'feels_like': 14.41, 'pressure': 1013, 'humidity': 71, 'dew_point': 9.79, 'uvi': 7.23, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 48, 'wind_gust': 2.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641844800, 'temp': 15, 'feels_like': 14.59, 'pressure': 1013, 'humidity': 78, 'dew_point': 11.2, 'uvi': 4.16, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.05, 'wind_deg': 155, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1641848400, 'temp': 15, 'feels_like': 14.8, 'pressure': 1013, 'humidity': 86, 'dew_point': 12.68, 'uvi': 1.65, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 190, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641852000, 'temp': 14, 'feels_like': 13.83, 'pressure': 1014, 'humidity': 91, 'dew_point': 12.56, 'uvi': 0.41, 'clouds': 87, 'visibility': 8863, 'wind_speed': 0.61, 'wind_deg': 165, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641855600, 'temp': 12, 'feels_like': 11.76, 'pressure': 1016, 'humidity': 96, 'dew_point': 11.38, 'uvi': 0, 'clouds': 89, 'visibility': 6020, 'wind_speed': 0.55, 'wind_deg': 162, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 00:00:00 | 96.000000 | 9.550000 | 10.000000 | 97.000000 | 1016.000000 |  | 10.000000 | 0.000000 | 6450.000000 | 126.000000 | 1.01 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 10.540000 | 10.690000 | 97.000000 | 1017.000000 |  | 11.000000 | 0.000000 | 3281.000000 | 138.000000 | 0.95 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 9.550000 | 10.000000 | 97.000000 | 1018.000000 |  | 10.000000 | 0.000000 | 6420.000000 | 134.000000 | 0.91 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.700000 | 10.000000 | 98.000000 | 1018.000000 |  | 10.000000 | 0.000000 | 6375.000000 | 154.000000 | 1.06 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.700000 | 10.000000 | 98.000000 | 1018.000000 |  | 10.000000 | 0.000000 | 7634.000000 | 179.000000 | 0.96 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 7.550000 | 8.000000 | 97.000000 | 1018.000000 | 0.12 | 8.000000 | 0.000000 | 9356.000000 | 193.000000 | 0.82 | 0.330000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 5.710000 | 6.000000 | 98.000000 | 1017.000000 | 0.1 | 6.000000 | 0.000000 | 8293.000000 | 190.000000 | 0.7 | 0.250000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 07:00:00 | 88.000000 | 4.710000 | 5.000000 | 98.000000 | 1016.000000 |  | 5.000000 | 0.000000 | 5971.000000 | 206.000000 | 0.75 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 08:00:00 | 86.000000 | 4.710000 | 5.000000 | 98.000000 | 1016.000000 |  | 5.000000 | 0.000000 | 10000.000000 | 229.000000 | 0.94 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 09:00:00 | 81.000000 | 4.710000 | 5.000000 | 98.000000 | 1016.000000 |  | 5.000000 | 0.000000 | 10000.000000 | 236.000000 | 0.85 | 0.600000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 10:00:00 | 82.000000 | 5.710000 | 6.000000 | 98.000000 | 1017.000000 |  | 6.000000 | 0.000000 | 8978.000000 | 268.000000 | 0.7 | 0.460000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 11:00:00 | 80.000000 | 6.560000 | 7.000000 | 97.000000 | 1018.000000 |  | 7.000000 | 0.000000 | 10000.000000 | 262.000000 | 0.82 | 0.580000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 12:00:00 | 79.000000 | 6.260000 | 7.000000 | 95.000000 | 1019.000000 |  | 7.000000 | 0.420000 | 10000.000000 | 236.000000 | 0.9 | 0.430000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 13:00:00 | 88.000000 | 5.800000 | 8.000000 | 86.000000 | 1019.000000 |  | 8.000000 | 2.460000 | 10000.000000 | 260.000000 | 1.05 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 14:00:00 | 83.000000 | 6.150000 | 10.040000 | 72.000000 | 1019.000000 |  | 11.000000 | 5.810000 | 10000.000000 | 264.000000 | 1.34 | 0.410000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 15:00:00 | 71.000000 | 4.940000 | 11.870000 | 58.000000 | 1017.000000 |  | 13.000000 | 9.730000 | 10000.000000 | 280.000000 | 2 | 0.400000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 16:00:00 | 70.000000 | 4.580000 | 12.840000 | 53.000000 | 1015.000000 |  | 14.000000 | 9.400000 | 10000.000000 | 319.000000 | 2.54 | 0.130000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 17:00:00 | 71.000000 | 5.370000 | 12.920000 | 56.000000 | 1014.000000 | 0.1 | 14.000000 | 10.180000 | 10000.000000 | 115.000000 | 2.49 | 0.260000 | 500 | Rain | light rain | 10d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 18:00:00 | 64.000000 | 9.370000 | 14.360000 | 69.000000 | 1014.000000 |  | 15.000000 | 9.170000 | 10000.000000 | 119.000000 | 2.07 | 0.540000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 19:00:00 | 73.000000 | 9.790000 | 14.410000 | 71.000000 | 1013.000000 | 0.23 | 15.000000 | 7.230000 | 10000.000000 | 48.000000 | 2.05 | 0.230000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 20:00:00 | 82.000000 | 11.200000 | 14.590000 | 78.000000 | 1013.000000 | 0.42 | 15.000000 | 4.160000 | 10000.000000 | 155.000000 | 1.92 | 0.050000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 21:00:00 | 88.000000 | 12.680000 | 14.800000 | 86.000000 | 1013.000000 | 0.56 | 15.000000 | 1.650000 | 10000.000000 | 190.000000 | 1.83 | 0.520000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 22:00:00 | 87.000000 | 12.560000 | 13.830000 | 91.000000 | 1014.000000 | 0.23 | 14.000000 | 0.410000 | 8863.000000 | 165.000000 | 1.78 | 0.610000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35025090 | "BOSQUE INTERVENIDO  - AUT [35025090]" | 4.664889 | -73.846639 | 2944.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-07-08 19:00:00 | NaT | Cundinamarca | La Calera | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba | America/Bogota | 2022-01-10 23:00:00 | 89.000000 | 11.380000 | 11.760000 | 96.000000 | 1016.000000 | 0.23 | 12.000000 | 0.000000 | 6020.000000 | 162.000000 | 1.57 | 0.550000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station35025090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35025090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35025090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025090_OWM_Windspeed_20220111.png)
