
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO SANTIAGO VILA [21185040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21185040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.27544444,-74.798) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.27544444&lon=-74.798)


| Parameter | Value |
|---|---|
| Code | 21185040 |
| Name | AEROPUERTO SANTIAGO VILA [21185040] |
| Latitude, ° | 4.27544444 |
| Longitude, ° | -74.798 |
| Elevation, m | 305 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1951-01-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Flandes |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Luisa y otros directos al Magdalena |

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

### (CNE index 1502) Open Weather values for station 21185040 - AEROPUERTO SANTIAGO VILA [21185040]

JSON data from API OWM:

```
{'lat': 4.2754, 'lon': -74.798, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812990, 'sunset': 1641855793, 'temp': 29.01, 'feels_like': 29.55, 'pressure': 1006, 'humidity': 49, 'dew_point': 17.22, 'uvi': 5.14, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 151, 'wind_gust': 2.45, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.01, 'feels_like': 28.39, 'pressure': 1009, 'humidity': 64, 'dew_point': 19.62, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 12, 'wind_gust': 1.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1010, 'humidity': 68, 'dew_point': 19.65, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 43, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 74, 'dew_point': 21.02, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 29, 'wind_gust': 1.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641783600, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1011, 'humidity': 79, 'dew_point': 22.08, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 34, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641787200, 'temp': 23.45, 'feels_like': 23.99, 'pressure': 1012, 'humidity': 82, 'dew_point': 20.2, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 40, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641790800, 'temp': 23.02, 'feels_like': 23.57, 'pressure': 1011, 'humidity': 84, 'dew_point': 20.17, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 49, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641794400, 'temp': 22.54, 'feels_like': 23.1, 'pressure': 1011, 'humidity': 86, 'dew_point': 20.08, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 65, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 22.2, 'feels_like': 22.77, 'pressure': 1010, 'humidity': 88, 'dew_point': 20.12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 69, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641801600, 'temp': 21.82, 'feels_like': 22.41, 'pressure': 1010, 'humidity': 90, 'dew_point': 20.11, 'uvi': 0, 'clouds': 54, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 50, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641805200, 'temp': 21.66, 'feels_like': 22.26, 'pressure': 1010, 'humidity': 91, 'dew_point': 20.13, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 35, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641808800, 'temp': 21.57, 'feels_like': 22.16, 'pressure': 1011, 'humidity': 91, 'dew_point': 20.04, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 63, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.33}}, {'dt': 1641812400, 'temp': 24.01, 'feels_like': 24.87, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.63, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 52, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.56}}, {'dt': 1641816000, 'temp': 25.01, 'feels_like': 25.89, 'pressure': 1013, 'humidity': 89, 'dew_point': 23.07, 'uvi': 0.21, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 18, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641819600, 'temp': 25.01, 'feels_like': 25.81, 'pressure': 1014, 'humidity': 86, 'dew_point': 22.5, 'uvi': 1.94, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 336, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641823200, 'temp': 25.01, 'feels_like': 25.73, 'pressure': 1014, 'humidity': 83, 'dew_point': 21.92, 'uvi': 4.72, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 140, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641826800, 'temp': 27.01, 'feels_like': 29.39, 'pressure': 1014, 'humidity': 76, 'dew_point': 22.42, 'uvi': 8.02, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 110, 'wind_gust': 1.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 28.01, 'feels_like': 30.17, 'pressure': 1013, 'humidity': 66, 'dew_point': 21.07, 'uvi': 11.69, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 42, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.01, 'feels_like': 30.75, 'pressure': 1011, 'humidity': 58, 'dew_point': 19.91, 'uvi': 12.8, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 3, 'wind_gust': 1.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.01, 'feels_like': 31.56, 'pressure': 1009, 'humidity': 53, 'dew_point': 19.39, 'uvi': 11.69, 'clouds': 5, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 120, 'wind_gust': 2.01, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 31.01, 'feels_like': 32.83, 'pressure': 1008, 'humidity': 51, 'dew_point': 19.69, 'uvi': 8.74, 'clouds': 8, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 166, 'wind_gust': 2.3, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641844800, 'temp': 29.01, 'feels_like': 29.55, 'pressure': 1006, 'humidity': 49, 'dew_point': 17.22, 'uvi': 5.14, 'clouds': 12, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 151, 'wind_gust': 2.45, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641848400, 'temp': 28.01, 'feels_like': 28.46, 'pressure': 1006, 'humidity': 50, 'dew_point': 16.62, 'uvi': 2.12, 'clouds': 18, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 146, 'wind_gust': 1.78, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641852000, 'temp': 28.01, 'feels_like': 28.94, 'pressure': 1007, 'humidity': 55, 'dew_point': 18.13, 'uvi': 0.49, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 109, 'wind_gust': 2.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 27.01, 'feels_like': 28.32, 'pressure': 1007, 'humidity': 63, 'dew_point': 19.37, 'uvi': 0, 'clouds': 30, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 2, 'wind_gust': 1.19, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 76.000000 | 19.620000 | 28.390000 | 64.000000 | 1009.000000 |  | 27.010000 | 0.000000 | 10000.000000 | 12.000000 | 1.6 | 1.370000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 80.000000 | 19.650000 | 26.010000 | 68.000000 | 1010.000000 |  | 26.010000 | 0.000000 | 10000.000000 | 43.000000 | 1.79 | 1.570000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 77.000000 | 21.020000 | 26.010000 | 74.000000 | 1011.000000 | 0.29 | 26.010000 | 0.000000 | 10000.000000 | 29.000000 | 1.4 | 1.240000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 84.000000 | 22.080000 | 26.010000 | 79.000000 | 1011.000000 | 0.32 | 26.010000 | 0.000000 | 10000.000000 | 34.000000 | 1.71 | 1.580000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 88.000000 | 20.200000 | 23.990000 | 82.000000 | 1012.000000 | 0.12 | 23.450000 | 0.000000 | 10000.000000 | 40.000000 | 1.36 | 1.160000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 90.000000 | 20.170000 | 23.570000 | 84.000000 | 1011.000000 | 0.15 | 23.020000 | 0.000000 | 10000.000000 | 49.000000 | 0.87 | 0.700000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 69.000000 | 20.080000 | 23.100000 | 86.000000 | 1011.000000 |  | 22.540000 | 0.000000 | 10000.000000 | 65.000000 | 0.78 | 0.570000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 75.000000 | 20.120000 | 22.770000 | 88.000000 | 1010.000000 | 0.1 | 22.200000 | 0.000000 | 10000.000000 | 69.000000 | 0.81 | 0.640000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 54.000000 | 20.110000 | 22.410000 | 90.000000 | 1010.000000 | 0.27 | 21.820000 | 0.000000 | 10000.000000 | 50.000000 | 0.41 | 0.280000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 49.000000 | 20.130000 | 22.260000 | 91.000000 | 1010.000000 | 0.2 | 21.660000 | 0.000000 | 10000.000000 | 35.000000 | 0.69 | 0.620000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 20.040000 | 22.160000 | 91.000000 | 1011.000000 | 0.33 | 21.570000 | 0.000000 | 10000.000000 | 63.000000 | 0.86 | 0.710000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 63.000000 | 22.630000 | 24.870000 | 92.000000 | 1012.000000 | 0.56 | 24.010000 | 0.000000 | 10000.000000 | 52.000000 | 0.76 | 0.650000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 23.070000 | 25.890000 | 89.000000 | 1013.000000 | 0.54 | 25.010000 | 0.210000 | 10000.000000 | 18.000000 | 0.88 | 0.690000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 22.500000 | 25.810000 | 86.000000 | 1014.000000 | 0.54 | 25.010000 | 1.940000 | 10000.000000 | 336.000000 | 0.81 | 0.300000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 21.920000 | 25.730000 | 83.000000 | 1014.000000 | 0.16 | 25.010000 | 4.720000 | 10000.000000 | 140.000000 | 1.02 | 0.380000 | 500 | Rain | light rain | 10d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 22.420000 | 29.390000 | 76.000000 | 1014.000000 |  | 27.010000 | 8.020000 | 10000.000000 | 110.000000 | 1.55 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 86.000000 | 21.070000 | 30.170000 | 66.000000 | 1013.000000 |  | 28.010000 | 11.690000 | 10000.000000 | 42.000000 | 1.76 | 0.470000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 74.000000 | 19.910000 | 30.750000 | 58.000000 | 1011.000000 |  | 29.010000 | 12.800000 | 10000.000000 | 3.000000 | 1.79 | 0.510000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 5.000000 | 19.390000 | 31.560000 | 53.000000 | 1009.000000 |  | 30.010000 | 11.690000 | 10000.000000 | 120.000000 | 2.01 | 0.310000 | 800 | Clear | clear sky | 01d | 18 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 8.000000 | 19.690000 | 32.830000 | 51.000000 | 1008.000000 |  | 31.010000 | 8.740000 | 10000.000000 | 166.000000 | 2.3 | 1.150000 | 800 | Clear | clear sky | 01d | 19 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 12.000000 | 17.220000 | 29.550000 | 49.000000 | 1006.000000 |  | 29.010000 | 5.140000 | 10000.000000 | 151.000000 | 2.45 | 1.250000 | 801 | Clouds | few clouds | 02d | 20 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 18.000000 | 16.620000 | 28.460000 | 50.000000 | 1006.000000 |  | 28.010000 | 2.120000 | 10000.000000 | 146.000000 | 1.78 | 1.080000 | 801 | Clouds | few clouds | 02d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 31.000000 | 18.130000 | 28.940000 | 55.000000 | 1007.000000 |  | 28.010000 | 0.490000 | 10000.000000 | 109.000000 | 2.07 | 0.730000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21185040 | "AEROPUERTO SANTIAGO VILA [21185040]" | 4.275444 | -74.798000 | 305.000000 | Climática Principal | Convencional | Activa | 1951-01-15 00:00:00 | NaT | Tolima | Flandes | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Luisa y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 30.000000 | 19.370000 | 28.320000 | 63.000000 | 1007.000000 |  | 27.010000 | 0.000000 | 10000.000000 | 2.000000 | 1.19 | 0.370000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station21185040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21185040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21185040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21185040_OWM_Windspeed_20220111.png)
