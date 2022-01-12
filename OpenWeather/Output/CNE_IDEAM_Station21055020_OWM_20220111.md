
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA AGRICOLA LA PLATA [21055020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21055020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.38,-75.89) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.38&lon=-75.89)


| Parameter | Value |
|---|---|
| Code | 21055020 |
| Name | ESCUELA AGRICOLA LA PLATA [21055020] |
| Latitude, ° | 2.38 |
| Longitude, ° | -75.89 |
| Elevation, m | 1070 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1969-12-15 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | La Plata |
| Stream | 0 |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Páez |

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

### (CNE index 4382) Open Weather values for station 21055020 - ESCUELA AGRICOLA LA PLATA [21055020]

JSON data from API OWM:

```
{'lat': 2.38, 'lon': -75.89, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813068, 'sunset': 1641856238, 'temp': 24.75, 'feels_like': 25.29, 'pressure': 1010, 'humidity': 77, 'dew_point': 20.45, 'uvi': 5, 'clouds': 79, 'visibility': 8159, 'wind_speed': 0.98, 'wind_deg': 101, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, 'hourly': [{'dt': 1641772800, 'temp': 20.84, 'feels_like': 21.23, 'pressure': 1013, 'humidity': 86, 'dew_point': 18.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 316, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641776400, 'temp': 20.31, 'feels_like': 20.72, 'pressure': 1014, 'humidity': 89, 'dew_point': 18.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 291, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641780000, 'temp': 20.18, 'feels_like': 20.63, 'pressure': 1015, 'humidity': 91, 'dew_point': 18.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 292, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641783600, 'temp': 20.18, 'feels_like': 20.63, 'pressure': 1015, 'humidity': 91, 'dew_point': 18.66, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 292, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641787200, 'temp': 19.88, 'feels_like': 20.35, 'pressure': 1015, 'humidity': 93, 'dew_point': 18.71, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 291, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.38}}, {'dt': 1641790800, 'temp': 19.64, 'feels_like': 20.11, 'pressure': 1015, 'humidity': 94, 'dew_point': 18.65, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 283, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641794400, 'temp': 19.31, 'feels_like': 19.8, 'pressure': 1014, 'humidity': 96, 'dew_point': 18.66, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 278, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641798000, 'temp': 19.24, 'feels_like': 19.73, 'pressure': 1014, 'humidity': 96, 'dew_point': 18.59, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 270, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641801600, 'temp': 19.35, 'feels_like': 19.82, 'pressure': 1013, 'humidity': 95, 'dew_point': 18.53, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 268, 'wind_gust': 0.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641805200, 'temp': 19.33, 'feels_like': 19.8, 'pressure': 1013, 'humidity': 95, 'dew_point': 18.51, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 241, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 19.06, 'feels_like': 19.5, 'pressure': 1014, 'humidity': 95, 'dew_point': 18.24, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 233, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 18.5, 'feels_like': 18.91, 'pressure': 1015, 'humidity': 96, 'dew_point': 17.85, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 264, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 19.66, 'feels_like': 20.14, 'pressure': 1015, 'humidity': 94, 'dew_point': 18.67, 'uvi': 0.45, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 254, 'wind_gust': 0.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 21.04, 'feels_like': 21.58, 'pressure': 1016, 'humidity': 91, 'dew_point': 19.51, 'uvi': 2.21, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 91, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641823200, 'temp': 22.34, 'feels_like': 22.88, 'pressure': 1016, 'humidity': 86, 'dew_point': 19.88, 'uvi': 5.43, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 106, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.57}}, {'dt': 1641826800, 'temp': 23.55, 'feels_like': 24.1, 'pressure': 1016, 'humidity': 82, 'dew_point': 20.3, 'uvi': 9.34, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.1, 'wind_deg': 110, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641830400, 'temp': 24.74, 'feels_like': 25.25, 'pressure': 1014, 'humidity': 76, 'dew_point': 20.22, 'uvi': 11.37, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 92, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}, {'dt': 1641834000, 'temp': 25.51, 'feels_like': 26.02, 'pressure': 1013, 'humidity': 73, 'dew_point': 20.31, 'uvi': 12.59, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 85, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}, {'dt': 1641837600, 'temp': 25.65, 'feels_like': 26.18, 'pressure': 1012, 'humidity': 73, 'dew_point': 20.45, 'uvi': 11.64, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 81, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1641841200, 'temp': 25.61, 'feels_like': 26.13, 'pressure': 1011, 'humidity': 73, 'dew_point': 20.41, 'uvi': 8.28, 'clouds': 83, 'visibility': 7329, 'wind_speed': 1.21, 'wind_deg': 81, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641844800, 'temp': 24.75, 'feels_like': 25.29, 'pressure': 1010, 'humidity': 77, 'dew_point': 20.45, 'uvi': 5, 'clouds': 79, 'visibility': 8159, 'wind_speed': 0.98, 'wind_deg': 101, 'wind_gust': 1.45, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.25}}, {'dt': 1641848400, 'temp': 23.73, 'feels_like': 24.3, 'pressure': 1010, 'humidity': 82, 'dew_point': 20.47, 'uvi': 2.17, 'clouds': 75, 'visibility': 7771, 'wind_speed': 0.85, 'wind_deg': 133, 'wind_gust': 1.43, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.39}}, {'dt': 1641852000, 'temp': 22.8, 'feels_like': 23.43, 'pressure': 1011, 'humidity': 88, 'dew_point': 20.71, 'uvi': 0.59, 'clouds': 74, 'visibility': 6273, 'wind_speed': 0.69, 'wind_deg': 147, 'wind_gust': 1.11, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, {'dt': 1641855600, 'temp': 21.07, 'feels_like': 21.61, 'pressure': 1012, 'humidity': 91, 'dew_point': 19.54, 'uvi': 0, 'clouds': 77, 'visibility': 7286, 'wind_speed': 0.4, 'wind_deg': 154, 'wind_gust': 0.67, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.72}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 18.410000 | 21.230000 | 86.000000 | 1013.000000 | 0.15 | 20.840000 | 0.000000 | 10000.000000 | 316.000000 | 1.02 | 0.810000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 18.440000 | 20.720000 | 89.000000 | 1014.000000 | 0.19 | 20.310000 | 0.000000 | 10000.000000 | 291.000000 | 1.17 | 1.170000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 18.660000 | 20.630000 | 91.000000 | 1015.000000 | 0.14 | 20.180000 | 0.000000 | 10000.000000 | 292.000000 | 1.14 | 1.140000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 03:00:00 | 97.000000 | 18.660000 | 20.630000 | 91.000000 | 1015.000000 | 0.23 | 20.180000 | 0.000000 | 10000.000000 | 292.000000 | 0.88 | 0.840000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 04:00:00 | 98.000000 | 18.710000 | 20.350000 | 93.000000 | 1015.000000 | 0.38 | 19.880000 | 0.000000 | 10000.000000 | 291.000000 | 0.74 | 0.660000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 18.650000 | 20.110000 | 94.000000 | 1015.000000 | 0.34 | 19.640000 | 0.000000 | 10000.000000 | 283.000000 | 0.8 | 0.750000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 18.660000 | 19.800000 | 96.000000 | 1014.000000 | 0.26 | 19.310000 | 0.000000 | 10000.000000 | 278.000000 | 0.71 | 0.670000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 07:00:00 | 89.000000 | 18.590000 | 19.730000 | 96.000000 | 1014.000000 | 0.27 | 19.240000 | 0.000000 | 10000.000000 | 270.000000 | 0.71 | 0.520000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 18.530000 | 19.820000 | 95.000000 | 1013.000000 | 0.11 | 19.350000 | 0.000000 | 10000.000000 | 268.000000 | 0.53 | 0.390000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 09:00:00 | 94.000000 | 18.510000 | 19.800000 | 95.000000 | 1013.000000 |  | 19.330000 | 0.000000 | 10000.000000 | 241.000000 | 0.52 | 0.310000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 18.240000 | 19.500000 | 95.000000 | 1014.000000 |  | 19.060000 | 0.000000 | 10000.000000 | 233.000000 | 0.57 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 11:00:00 | 93.000000 | 17.850000 | 18.910000 | 96.000000 | 1015.000000 |  | 18.500000 | 0.000000 | 10000.000000 | 264.000000 | 0.71 | 0.740000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 12:00:00 | 74.000000 | 18.670000 | 20.140000 | 94.000000 | 1015.000000 |  | 19.660000 | 0.450000 | 10000.000000 | 254.000000 | 0.33 | 0.330000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 13:00:00 | 92.000000 | 19.510000 | 21.580000 | 91.000000 | 1016.000000 | 0.24 | 21.040000 | 2.210000 | 10000.000000 | 91.000000 | 0.62 | 0.560000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 14:00:00 | 95.000000 | 19.880000 | 22.880000 | 86.000000 | 1016.000000 | 0.57 | 22.340000 | 5.430000 | 10000.000000 | 106.000000 | 0.89 | 1.010000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 15:00:00 | 92.000000 | 20.300000 | 24.100000 | 82.000000 | 1016.000000 | 0.85 | 23.550000 | 9.340000 | 10000.000000 | 110.000000 | 1.18 | 1.100000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 16:00:00 | 94.000000 | 20.220000 | 25.250000 | 76.000000 | 1014.000000 | 0.83 | 24.740000 | 11.370000 | 10000.000000 | 92.000000 | 1.53 | 1.170000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 17:00:00 | 94.000000 | 20.310000 | 26.020000 | 73.000000 | 1013.000000 | 0.99 | 25.510000 | 12.590000 | 10000.000000 | 85.000000 | 1.72 | 1.120000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 20.450000 | 26.180000 | 73.000000 | 1012.000000 | 1 | 25.650000 | 11.640000 | 10000.000000 | 81.000000 | 1.65 | 1.130000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 19:00:00 | 83.000000 | 20.410000 | 26.130000 | 73.000000 | 1011.000000 | 1.14 | 25.610000 | 8.280000 | 7329.000000 | 81.000000 | 1.66 | 1.210000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 20:00:00 | 79.000000 | 20.450000 | 25.290000 | 77.000000 | 1010.000000 | 1.25 | 24.750000 | 5.000000 | 8159.000000 | 101.000000 | 1.45 | 0.980000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 20.470000 | 24.300000 | 82.000000 | 1010.000000 | 1.39 | 23.730000 | 2.170000 | 7771.000000 | 133.000000 | 1.43 | 0.850000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 22:00:00 | 74.000000 | 20.710000 | 23.430000 | 88.000000 | 1011.000000 | 1.44 | 22.800000 | 0.590000 | 6273.000000 | 147.000000 | 1.11 | 0.690000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21055020 | "ESCUELA AGRICOLA LA PLATA [21055020]" | 2.380000 | -75.890000 | 1070.000000 | Climática Principal | Convencional | Activa | 1969-12-15 00:00:00 | NaT | Huila | La Plata | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Río Páez | America/Bogota | 2022-01-10 23:00:00 | 77.000000 | 19.540000 | 21.610000 | 91.000000 | 1012.000000 | 1.72 | 21.070000 | 0.000000 | 7286.000000 | 154.000000 | 0.67 | 0.400000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21055020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21055020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21055020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21055020_OWM_Windspeed_20220111.png)
