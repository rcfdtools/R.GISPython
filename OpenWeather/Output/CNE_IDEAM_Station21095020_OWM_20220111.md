
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - HIDROBETANIA [21095020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21095020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.71344444,-75.42491667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.71344444&lon=-75.42491667)


| Parameter | Value |
|---|---|
| Code | 21095020 |
| Name | HIDROBETANIA [21095020] |
| Latitude, ° | 2.71344444 |
| Longitude, ° | -75.42491667 |
| Elevation, m | 500 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1990-03-15 00:00:00 |
| Suspension date | 2003-08-15 00:00:00 |
| State | Huila |
| County | Campoalegre |
| Stream | Iquira |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Ríos directos Magdalena (md) |

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

### (CNE index 1394) Open Weather values for station 21095020 - HIDROBETANIA [21095020]

JSON data from API OWM:

```
{'lat': 2.7134, 'lon': -75.4249, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812989, 'sunset': 1641856094, 'temp': 31.25, 'feels_like': 35.12, 'pressure': 1009, 'humidity': 59, 'dew_point': 22.28, 'uvi': 5.43, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 35, 'wind_gust': 2.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, 'hourly': [{'dt': 1641772800, 'temp': 27.25, 'feels_like': 29.88, 'pressure': 1011, 'humidity': 76, 'dew_point': 22.65, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 61, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 27.25, 'feels_like': 30.09, 'pressure': 1012, 'humidity': 78, 'dew_point': 23.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 319, 'wind_gust': 1.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1014, 'humidity': 82, 'dew_point': 22.93, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 301, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 26.25, 'feels_like': 26.25, 'pressure': 1014, 'humidity': 85, 'dew_point': 23.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 266, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641787200, 'temp': 21.93, 'feels_like': 22.45, 'pressure': 1014, 'humidity': 87, 'dew_point': 19.67, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 245, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641790800, 'temp': 21.46, 'feels_like': 21.96, 'pressure': 1014, 'humidity': 88, 'dew_point': 19.39, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 241, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641794400, 'temp': 21.46, 'feels_like': 21.96, 'pressure': 1013, 'humidity': 88, 'dew_point': 19.39, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 212, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641798000, 'temp': 21.21, 'feels_like': 21.71, 'pressure': 1013, 'humidity': 89, 'dew_point': 19.32, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 271, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641801600, 'temp': 20.89, 'feels_like': 21.38, 'pressure': 1012, 'humidity': 90, 'dew_point': 19.19, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 224, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641805200, 'temp': 20.57, 'feels_like': 21.06, 'pressure': 1012, 'humidity': 91, 'dew_point': 19.05, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 214, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641808800, 'temp': 20.77, 'feels_like': 21.25, 'pressure': 1013, 'humidity': 90, 'dew_point': 19.07, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 213, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641812400, 'temp': 23.25, 'feels_like': 23.98, 'pressure': 1013, 'humidity': 90, 'dew_point': 21.52, 'uvi': 0, 'clouds': 65, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 217, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641816000, 'temp': 23.25, 'feels_like': 23.93, 'pressure': 1014, 'humidity': 88, 'dew_point': 21.15, 'uvi': 0.46, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 254, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.25, 'feels_like': 26, 'pressure': 1015, 'humidity': 83, 'dew_point': 22.16, 'uvi': 2.12, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 225, 'wind_gust': 0.72, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 27.25, 'feels_like': 30.09, 'pressure': 1015, 'humidity': 78, 'dew_point': 23.08, 'uvi': 5.16, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 58, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641826800, 'temp': 27.25, 'feels_like': 29.68, 'pressure': 1015, 'humidity': 74, 'dew_point': 22.21, 'uvi': 8.8, 'clouds': 73, 'visibility': 9296, 'wind_speed': 1.72, 'wind_deg': 31, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641830400, 'temp': 28.25, 'feels_like': 31.16, 'pressure': 1014, 'humidity': 70, 'dew_point': 22.26, 'uvi': 11.34, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 24, 'wind_gust': 3.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641834000, 'temp': 29.25, 'feels_like': 32.51, 'pressure': 1013, 'humidity': 66, 'dew_point': 22.24, 'uvi': 12.5, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 20, 'wind_gust': 3.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}, {'dt': 1641837600, 'temp': 31.25, 'feels_like': 35.65, 'pressure': 1011, 'humidity': 61, 'dew_point': 22.83, 'uvi': 11.47, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 23, 'wind_gust': 2.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641841200, 'temp': 31.25, 'feels_like': 35.12, 'pressure': 1010, 'humidity': 59, 'dew_point': 22.28, 'uvi': 9.12, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.79, 'wind_deg': 33, 'wind_gust': 2.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641844800, 'temp': 31.25, 'feels_like': 35.12, 'pressure': 1009, 'humidity': 59, 'dew_point': 22.28, 'uvi': 5.43, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 35, 'wind_gust': 2.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1641848400, 'temp': 30.25, 'feels_like': 33.53, 'pressure': 1008, 'humidity': 61, 'dew_point': 21.89, 'uvi': 2.32, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 37, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641852000, 'temp': 29.25, 'feels_like': 32.7, 'pressure': 1009, 'humidity': 67, 'dew_point': 22.49, 'uvi': 0.56, 'clouds': 78, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 39, 'wind_gust': 2.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.69}}, {'dt': 1641855600, 'temp': 28.25, 'feels_like': 32.56, 'pressure': 1010, 'humidity': 79, 'dew_point': 24.26, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.88, 'wind_deg': 29, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.650000 | 29.880000 | 76.000000 | 1011.000000 |  | 27.250000 | 0.000000 | 10000.000000 | 61.000000 | 1.2 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 23.080000 | 30.090000 | 78.000000 | 1012.000000 |  | 27.250000 | 0.000000 | 10000.000000 | 319.000000 | 1.33 | 0.130000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 22.930000 | 26.250000 | 82.000000 | 1014.000000 | 0.15 | 26.250000 | 0.000000 | 10000.000000 | 301.000000 | 1.45 | 0.300000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 23.530000 | 26.250000 | 85.000000 | 1014.000000 | 0.19 | 26.250000 | 0.000000 | 10000.000000 | 266.000000 | 1.5 | 0.380000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 04:00:00 | 96.000000 | 19.670000 | 22.450000 | 87.000000 | 1014.000000 | 0.28 | 21.930000 | 0.000000 | 10000.000000 | 245.000000 | 1.55 | 0.650000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 19.390000 | 21.960000 | 88.000000 | 1014.000000 | 0.29 | 21.460000 | 0.000000 | 10000.000000 | 241.000000 | 1.54 | 0.540000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 06:00:00 | 25.000000 | 19.390000 | 21.960000 | 88.000000 | 1013.000000 | 0.22 | 21.460000 | 0.000000 | 10000.000000 | 212.000000 | 1.26 | 0.430000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 07:00:00 | 24.000000 | 19.320000 | 21.710000 | 89.000000 | 1013.000000 | 0.26 | 21.210000 | 0.000000 | 10000.000000 | 271.000000 | 1.1 | 0.120000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 08:00:00 | 59.000000 | 19.190000 | 21.380000 | 90.000000 | 1012.000000 | 0.19 | 20.890000 | 0.000000 | 10000.000000 | 224.000000 | 1.03 | 0.300000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 19.050000 | 21.060000 | 91.000000 | 1012.000000 | 0.3 | 20.570000 | 0.000000 | 10000.000000 | 214.000000 | 1.18 | 0.520000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 10:00:00 | 70.000000 | 19.070000 | 21.250000 | 90.000000 | 1013.000000 | 0.15 | 20.770000 | 0.000000 | 10000.000000 | 213.000000 | 1.16 | 0.590000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 11:00:00 | 65.000000 | 21.520000 | 23.980000 | 90.000000 | 1013.000000 | 0.11 | 23.250000 | 0.000000 | 10000.000000 | 217.000000 | 0.96 | 0.210000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 12:00:00 | 90.000000 | 21.150000 | 23.930000 | 88.000000 | 1014.000000 |  | 23.250000 | 0.460000 | 10000.000000 | 254.000000 | 1.02 | 0.500000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 13:00:00 | 86.000000 | 22.160000 | 26.000000 | 83.000000 | 1015.000000 |  | 25.250000 | 2.120000 | 10000.000000 | 225.000000 | 0.72 | 0.460000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 14:00:00 | 73.000000 | 23.080000 | 30.090000 | 78.000000 | 1015.000000 | 0.23 | 27.250000 | 5.160000 | 10000.000000 | 58.000000 | 1.05 | 0.660000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 15:00:00 | 73.000000 | 22.210000 | 29.680000 | 74.000000 | 1015.000000 | 0.76 | 27.250000 | 8.800000 | 9296.000000 | 31.000000 | 2.23 | 1.720000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 16:00:00 | 80.000000 | 22.260000 | 31.160000 | 70.000000 | 1014.000000 | 0.6 | 28.250000 | 11.340000 | 10000.000000 | 24.000000 | 3.01 | 2.390000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 17:00:00 | 84.000000 | 22.240000 | 32.510000 | 66.000000 | 1013.000000 | 0.63 | 29.250000 | 12.500000 | 10000.000000 | 20.000000 | 3.18 | 2.600000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 18:00:00 | 91.000000 | 22.830000 | 35.650000 | 61.000000 | 1011.000000 | 0.68 | 31.250000 | 11.470000 | 10000.000000 | 23.000000 | 2.85 | 2.490000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 19:00:00 | 93.000000 | 22.280000 | 35.120000 | 59.000000 | 1010.000000 | 0.58 | 31.250000 | 9.120000 | 10000.000000 | 33.000000 | 2.99 | 2.790000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 20:00:00 | 96.000000 | 22.280000 | 35.120000 | 59.000000 | 1009.000000 | 0.42 | 31.250000 | 5.430000 | 10000.000000 | 35.000000 | 2.65 | 2.490000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 21:00:00 | 84.000000 | 21.890000 | 33.530000 | 61.000000 | 1008.000000 | 0.46 | 30.250000 | 2.320000 | 10000.000000 | 37.000000 | 2.49 | 2.300000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 22:00:00 | 78.000000 | 22.490000 | 32.700000 | 67.000000 | 1009.000000 | 0.69 | 29.250000 | 0.560000 | 10000.000000 | 39.000000 | 2.72 | 2.070000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21095020 | "HIDROBETANIA [21095020]" | 2.713444 | -75.424917 | 500.000000 | Climática Principal | Convencional | Suspendida | 1990-03-15 00:00:00 | 2003-08-15 00:00:00 | Huila | Campoalegre | Iquira | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Ríos directos Magdalena (md) | America/Bogota | 2022-01-10 23:00:00 | 73.000000 | 24.260000 | 32.560000 | 79.000000 | 1010.000000 | 1.14 | 28.250000 | 0.000000 | 10000.000000 | 29.000000 | 1.49 | 0.880000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21095020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21095020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21095020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21095020_OWM_Windspeed_20220111.png)
