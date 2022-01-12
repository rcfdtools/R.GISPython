
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GRANJA EL MIRA - - AUT [51025090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station51025090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.55019444,-78.69558333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.55019444&lon=-78.69558333)


| Parameter | Value |
|---|---|
| Code | 51025090 |
| Name | GRANJA EL MIRA - - AUT [51025090] |
| Latitude, ° | 1.55019444 |
| Longitude, ° | -78.69558333 |
| Elevation, m | 16 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2016-08-01 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Tumaco |
| Stream | 0 |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Mira |
| SZH - Hydrographic subzone | Río Mira |

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

### (CNE index 14) Open Weather values for station 51025090 - GRANJA EL MIRA - - AUT [51025090]

JSON data from API OWM:

```
{'lat': 1.5502, 'lon': -78.6956, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813662, 'sunset': 1641856992, 'temp': 26.78, 'feels_like': 29.1, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.62, 'uvi': 6.17, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 290, 'wind_gust': 3.94, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, 'hourly': [{'dt': 1641772800, 'temp': 23.99, 'feels_like': 24.82, 'pressure': 1011, 'humidity': 91, 'dew_point': 22.43, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 251, 'wind_gust': 2.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641776400, 'temp': 23.78, 'feels_like': 24.62, 'pressure': 1012, 'humidity': 92, 'dew_point': 22.4, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 247, 'wind_gust': 2.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 23.59, 'feels_like': 24.43, 'pressure': 1013, 'humidity': 93, 'dew_point': 22.39, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 239, 'wind_gust': 1.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641783600, 'temp': 23.43, 'feels_like': 24.28, 'pressure': 1014, 'humidity': 94, 'dew_point': 22.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 223, 'wind_gust': 2.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641787200, 'temp': 23.16, 'feels_like': 24.01, 'pressure': 1013, 'humidity': 95, 'dew_point': 22.31, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 209, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.51}}, {'dt': 1641790800, 'temp': 22.99, 'feels_like': 23.85, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.32, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 203, 'wind_gust': 3.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.48}}, {'dt': 1641794400, 'temp': 22.85, 'feels_like': 23.7, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.18, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 204, 'wind_gust': 4.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641798000, 'temp': 22.81, 'feels_like': 23.65, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 196, 'wind_gust': 3.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641801600, 'temp': 22.58, 'feels_like': 23.4, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.91, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 198, 'wind_gust': 2.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.69}}, {'dt': 1641805200, 'temp': 22.49, 'feels_like': 23.3, 'pressure': 1011, 'humidity': 96, 'dew_point': 21.82, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 190, 'wind_gust': 1.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.57}}, {'dt': 1641808800, 'temp': 22.45, 'feels_like': 23.26, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.78, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 202, 'wind_gust': 1.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641812400, 'temp': 22.35, 'feels_like': 23.15, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.68, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 194, 'wind_gust': 2.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641816000, 'temp': 22.7, 'feels_like': 23.53, 'pressure': 1013, 'humidity': 96, 'dew_point': 22.03, 'uvi': 0.29, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 173, 'wind_gust': 3.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641819600, 'temp': 24.21, 'feels_like': 25.04, 'pressure': 1014, 'humidity': 90, 'dew_point': 22.46, 'uvi': 1.62, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.02, 'wind_deg': 199, 'wind_gust': 3.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.62}}, {'dt': 1641823200, 'temp': 25.61, 'feels_like': 26.42, 'pressure': 1015, 'humidity': 84, 'dew_point': 22.7, 'uvi': 4.3, 'clouds': 88, 'visibility': 10000, 'wind_speed': 2.54, 'wind_deg': 227, 'wind_gust': 4.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641826800, 'temp': 26.92, 'feels_like': 29.3, 'pressure': 1015, 'humidity': 77, 'dew_point': 22.54, 'uvi': 7.81, 'clouds': 79, 'visibility': 10000, 'wind_speed': 2.49, 'wind_deg': 249, 'wind_gust': 3.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641830400, 'temp': 28, 'feels_like': 30.8, 'pressure': 1014, 'humidity': 71, 'dew_point': 22.25, 'uvi': 11.14, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 269, 'wind_gust': 3.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641834000, 'temp': 28.09, 'feels_like': 30.98, 'pressure': 1013, 'humidity': 71, 'dew_point': 22.34, 'uvi': 12.79, 'clouds': 70, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 280, 'wind_gust': 3.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641837600, 'temp': 27.75, 'feels_like': 30.56, 'pressure': 1013, 'humidity': 73, 'dew_point': 22.47, 'uvi': 12.27, 'clouds': 47, 'visibility': 8708, 'wind_speed': 2.95, 'wind_deg': 292, 'wind_gust': 3.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641841200, 'temp': 27.31, 'feels_like': 30, 'pressure': 1012, 'humidity': 76, 'dew_point': 22.71, 'uvi': 9.67, 'clouds': 59, 'visibility': 9455, 'wind_speed': 3.04, 'wind_deg': 292, 'wind_gust': 4.06, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, {'dt': 1641844800, 'temp': 26.78, 'feels_like': 29.1, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.62, 'uvi': 6.17, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 290, 'wind_gust': 3.94, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641848400, 'temp': 26.6, 'feels_like': 26.6, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.45, 'uvi': 2.89, 'clouds': 74, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 290, 'wind_gust': 3.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641852000, 'temp': 26.02, 'feels_like': 26.02, 'pressure': 1011, 'humidity': 81, 'dew_point': 22.51, 'uvi': 0.83, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.94, 'wind_deg': 291, 'wind_gust': 3.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641855600, 'temp': 24.72, 'feels_like': 25.52, 'pressure': 1011, 'humidity': 87, 'dew_point': 22.41, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 295, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.430000 | 24.820000 | 91.000000 | 1011.000000 | 0.15 | 23.990000 | 0.000000 | 10000.000000 | 251.000000 | 2.56 | 1.590000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 22.400000 | 24.620000 | 92.000000 | 1012.000000 |  | 23.780000 | 0.000000 | 10000.000000 | 247.000000 | 2.1 | 1.420000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 22.390000 | 24.430000 | 93.000000 | 1013.000000 | 0.27 | 23.590000 | 0.000000 | 10000.000000 | 239.000000 | 1.73 | 1.320000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 22.410000 | 24.280000 | 94.000000 | 1014.000000 | 0.4 | 23.430000 | 0.000000 | 10000.000000 | 223.000000 | 2.04 | 1.470000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 22.310000 | 24.010000 | 95.000000 | 1013.000000 | 0.51 | 23.160000 | 0.000000 | 10000.000000 | 209.000000 | 2.49 | 1.650000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 22.320000 | 23.850000 | 96.000000 | 1013.000000 | 0.48 | 22.990000 | 0.000000 | 10000.000000 | 203.000000 | 3.3 | 1.710000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 22.180000 | 23.700000 | 96.000000 | 1012.000000 | 0.2 | 22.850000 | 0.000000 | 10000.000000 | 204.000000 | 4.17 | 1.800000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 22.140000 | 23.650000 | 96.000000 | 1012.000000 | 0.13 | 22.810000 | 0.000000 | 10000.000000 | 196.000000 | 3.11 | 1.630000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 21.910000 | 23.400000 | 96.000000 | 1011.000000 | 0.69 | 22.580000 | 0.000000 | 10000.000000 | 198.000000 | 2.91 | 1.550000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 21.820000 | 23.300000 | 96.000000 | 1011.000000 | 0.57 | 22.490000 | 0.000000 | 10000.000000 | 190.000000 | 1.8 | 1.270000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 21.780000 | 23.260000 | 96.000000 | 1012.000000 | 0.53 | 22.450000 | 0.000000 | 10000.000000 | 202.000000 | 1.63 | 1.260000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 11:00:00 | 92.000000 | 21.680000 | 23.150000 | 96.000000 | 1012.000000 | 0.34 | 22.350000 | 0.000000 | 10000.000000 | 194.000000 | 2.31 | 1.450000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 12:00:00 | 84.000000 | 22.030000 | 23.530000 | 96.000000 | 1013.000000 | 0.33 | 22.700000 | 0.290000 | 10000.000000 | 173.000000 | 3.52 | 1.570000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 13:00:00 | 93.000000 | 22.460000 | 25.040000 | 90.000000 | 1014.000000 | 0.62 | 24.210000 | 1.620000 | 10000.000000 | 199.000000 | 3.94 | 2.020000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 14:00:00 | 88.000000 | 22.700000 | 26.420000 | 84.000000 | 1015.000000 | 0.72 | 25.610000 | 4.300000 | 10000.000000 | 227.000000 | 4.44 | 2.540000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 22.540000 | 29.300000 | 77.000000 | 1015.000000 | 0.68 | 26.920000 | 7.810000 | 10000.000000 | 249.000000 | 3.87 | 2.490000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 16:00:00 | 71.000000 | 22.250000 | 30.800000 | 71.000000 | 1014.000000 | 0.55 | 28.000000 | 11.140000 | 10000.000000 | 269.000000 | 3.29 | 2.560000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 17:00:00 | 70.000000 | 22.340000 | 30.980000 | 71.000000 | 1013.000000 | 0.94 | 28.090000 | 12.790000 | 10000.000000 | 280.000000 | 3.45 | 2.780000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 18:00:00 | 47.000000 | 22.470000 | 30.560000 | 73.000000 | 1013.000000 | 0.85 | 27.750000 | 12.270000 | 8708.000000 | 292.000000 | 3.88 | 2.950000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 19:00:00 | 59.000000 | 22.710000 | 30.000000 | 76.000000 | 1012.000000 | 1.22 | 27.310000 | 9.670000 | 9455.000000 | 292.000000 | 4.06 | 3.040000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 20:00:00 | 71.000000 | 22.620000 | 29.100000 | 78.000000 | 1011.000000 | 1.08 | 26.780000 | 6.170000 | 10000.000000 | 290.000000 | 3.94 | 2.690000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 21:00:00 | 74.000000 | 22.450000 | 26.600000 | 78.000000 | 1011.000000 | 0.81 | 26.600000 | 2.890000 | 10000.000000 | 290.000000 | 3.69 | 2.410000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 22:00:00 | 70.000000 | 22.510000 | 26.020000 | 81.000000 | 1011.000000 | 0.61 | 26.020000 | 0.830000 | 10000.000000 | 291.000000 | 3.46 | 1.940000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025090 | "GRANJA EL MIRA - - AUT [51025090]" | 1.550194 | -78.695583 | 16.000000 | Climática Principal | Automática con Telemetría | Activa | 2016-08-01 00:00:00 | NaT | Nariño | Tumaco | 0 | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 23:00:00 | 62.000000 | 22.410000 | 25.520000 | 87.000000 | 1011.000000 | 0.44 | 24.720000 | 0.000000 | 10000.000000 | 295.000000 | 2.23 | 1.410000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station51025090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station51025090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station51025090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025090_OWM_Windspeed_20220111.png)
