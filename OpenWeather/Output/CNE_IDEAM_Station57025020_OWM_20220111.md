
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - GORGONA GUAPI [57025020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station57025020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.96294444,-78.17436111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.96294444&lon=-78.17436111)


| Parameter | Value |
|---|---|
| Code | 57025020 |
| Name | GORGONA GUAPI [57025020] |
| Latitude, ° | 2.96294444 |
| Longitude, ° | -78.17436111 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-09-18 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Guapi |
| Stream | Magdalena |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Guaviare |
| SZH - Hydrographic subzone | Medio Guaviare |

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

### (CNE index 38) Open Weather values for station 57025020 - GORGONA GUAPI [57025020]

JSON data from API OWM:

```
{'lat': 2.9629, 'lon': -78.1744, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813673, 'sunset': 1641856730, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.75, 'uvi': 5.9, 'clouds': 69, 'visibility': 10000, 'wind_speed': 3.53, 'wind_deg': 297, 'wind_gust': 4.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.61, 'feels_like': 26.61, 'pressure': 1011, 'humidity': 78, 'dew_point': 22.46, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.7, 'wind_deg': 257, 'wind_gust': 3.82, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 26.55, 'feels_like': 26.55, 'pressure': 1012, 'humidity': 79, 'dew_point': 22.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.03, 'wind_deg': 251, 'wind_gust': 3.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641780000, 'temp': 26.29, 'feels_like': 26.29, 'pressure': 1013, 'humidity': 80, 'dew_point': 22.56, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.48, 'wind_deg': 240, 'wind_gust': 2.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1641783600, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1013, 'humidity': 81, 'dew_point': 22.58, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 2.12, 'wind_deg': 232, 'wind_gust': 2.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.96}}, {'dt': 1641787200, 'temp': 25.94, 'feels_like': 26.7, 'pressure': 1013, 'humidity': 81, 'dew_point': 22.43, 'uvi': 0, 'clouds': 96, 'visibility': 7582, 'wind_speed': 2.53, 'wind_deg': 220, 'wind_gust': 2.81, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1641790800, 'temp': 25.77, 'feels_like': 26.54, 'pressure': 1012, 'humidity': 82, 'dew_point': 22.46, 'uvi': 0, 'clouds': 97, 'visibility': 9887, 'wind_speed': 3.33, 'wind_deg': 215, 'wind_gust': 3.5, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.03}}, {'dt': 1641794400, 'temp': 25.57, 'feels_like': 26.35, 'pressure': 1012, 'humidity': 83, 'dew_point': 22.47, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 4.13, 'wind_deg': 209, 'wind_gust': 4.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.54}}, {'dt': 1641798000, 'temp': 25.46, 'feels_like': 26.25, 'pressure': 1011, 'humidity': 84, 'dew_point': 22.56, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 4.82, 'wind_deg': 208, 'wind_gust': 5.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.94}}, {'dt': 1641801600, 'temp': 25.27, 'feels_like': 26.05, 'pressure': 1011, 'humidity': 84, 'dew_point': 22.37, 'uvi': 0, 'clouds': 85, 'visibility': 7373, 'wind_speed': 5.1, 'wind_deg': 216, 'wind_gust': 5.56, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.77}}, {'dt': 1641805200, 'temp': 25.36, 'feels_like': 26.12, 'pressure': 1011, 'humidity': 83, 'dew_point': 22.26, 'uvi': 0, 'clouds': 88, 'visibility': 7382, 'wind_speed': 5.75, 'wind_deg': 217, 'wind_gust': 6.34, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.89}}, {'dt': 1641808800, 'temp': 25.34, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 83, 'dew_point': 22.24, 'uvi': 0, 'clouds': 91, 'visibility': 5650, 'wind_speed': 5.76, 'wind_deg': 215, 'wind_gust': 6.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.15}}, {'dt': 1641812400, 'temp': 25.4, 'feels_like': 26.16, 'pressure': 1012, 'humidity': 83, 'dew_point': 22.3, 'uvi': 0, 'clouds': 91, 'visibility': 5586, 'wind_speed': 6.02, 'wind_deg': 220, 'wind_gust': 6.85, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.14}}, {'dt': 1641816000, 'temp': 25.51, 'feels_like': 26.26, 'pressure': 1013, 'humidity': 82, 'dew_point': 22.21, 'uvi': 0.3, 'clouds': 100, 'visibility': 9219, 'wind_speed': 5.78, 'wind_deg': 224, 'wind_gust': 6.52, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.74}}, {'dt': 1641819600, 'temp': 25.72, 'feels_like': 26.46, 'pressure': 1014, 'humidity': 81, 'dew_point': 22.21, 'uvi': 1.63, 'clouds': 99, 'visibility': 10000, 'wind_speed': 5.08, 'wind_deg': 230, 'wind_gust': 5.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641823200, 'temp': 25.58, 'feels_like': 26.33, 'pressure': 1014, 'humidity': 82, 'dew_point': 22.28, 'uvi': 4.29, 'clouds': 100, 'visibility': 7785, 'wind_speed': 5.41, 'wind_deg': 240, 'wind_gust': 6.17, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.34}}, {'dt': 1641826800, 'temp': 25.84, 'feels_like': 26.57, 'pressure': 1015, 'humidity': 80, 'dew_point': 22.13, 'uvi': 7.76, 'clouds': 97, 'visibility': 10000, 'wind_speed': 5.38, 'wind_deg': 248, 'wind_gust': 5.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641830400, 'temp': 25.92, 'feels_like': 26.66, 'pressure': 1014, 'humidity': 80, 'dew_point': 22.2, 'uvi': 10.98, 'clouds': 88, 'visibility': 10000, 'wind_speed': 5.65, 'wind_deg': 258, 'wind_gust': 6.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.59}}, {'dt': 1641834000, 'temp': 26.07, 'feels_like': 26.07, 'pressure': 1013, 'humidity': 79, 'dew_point': 22.14, 'uvi': 12.55, 'clouds': 90, 'visibility': 10000, 'wind_speed': 6.22, 'wind_deg': 267, 'wind_gust': 6.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 25.95, 'feels_like': 25.95, 'pressure': 1013, 'humidity': 79, 'dew_point': 22.03, 'uvi': 11.95, 'clouds': 81, 'visibility': 10000, 'wind_speed': 4.76, 'wind_deg': 285, 'wind_gust': 5.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 25.93, 'feels_like': 26.64, 'pressure': 1012, 'humidity': 79, 'dew_point': 22.01, 'uvi': 9.37, 'clouds': 85, 'visibility': 10000, 'wind_speed': 4.43, 'wind_deg': 291, 'wind_gust': 4.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641844800, 'temp': 26.1, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 77, 'dew_point': 21.75, 'uvi': 5.9, 'clouds': 69, 'visibility': 10000, 'wind_speed': 3.53, 'wind_deg': 297, 'wind_gust': 4.12, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 26.28, 'feels_like': 26.28, 'pressure': 1010, 'humidity': 75, 'dew_point': 21.5, 'uvi': 2.71, 'clouds': 67, 'visibility': 10000, 'wind_speed': 3.04, 'wind_deg': 300, 'wind_gust': 3.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 26.45, 'feels_like': 26.45, 'pressure': 1011, 'humidity': 75, 'dew_point': 21.66, 'uvi': 0.74, 'clouds': 69, 'visibility': 10000, 'wind_speed': 3.56, 'wind_deg': 294, 'wind_gust': 4.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641855600, 'temp': 26.58, 'feels_like': 26.58, 'pressure': 1011, 'humidity': 74, 'dew_point': 21.57, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.04, 'wind_deg': 287, 'wind_gust': 3.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.460000 | 26.610000 | 78.000000 | 1011.000000 |  | 26.610000 | 0.000000 | 10000.000000 | 257.000000 | 3.82 | 3.700000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 22.610000 | 26.550000 | 79.000000 | 1012.000000 | 0.23 | 26.550000 | 0.000000 | 10000.000000 | 251.000000 | 3.2 | 3.030000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 02:00:00 | 93.000000 | 22.560000 | 26.290000 | 80.000000 | 1013.000000 | 0.65 | 26.290000 | 0.000000 | 10000.000000 | 240.000000 | 2.73 | 2.480000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 22.580000 | 26.100000 | 81.000000 | 1013.000000 | 0.96 | 26.100000 | 0.000000 | 10000.000000 | 232.000000 | 2.44 | 2.120000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 04:00:00 | 96.000000 | 22.430000 | 26.700000 | 81.000000 | 1013.000000 | 1.15 | 25.940000 | 0.000000 | 7582.000000 | 220.000000 | 2.81 | 2.530000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 05:00:00 | 97.000000 | 22.460000 | 26.540000 | 82.000000 | 1012.000000 | 1.03 | 25.770000 | 0.000000 | 9887.000000 | 215.000000 | 3.5 | 3.330000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 06:00:00 | 69.000000 | 22.470000 | 26.350000 | 83.000000 | 1012.000000 | 0.54 | 25.570000 | 0.000000 | 10000.000000 | 209.000000 | 4.28 | 4.130000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 07:00:00 | 76.000000 | 22.560000 | 26.250000 | 84.000000 | 1011.000000 | 0.94 | 25.460000 | 0.000000 | 10000.000000 | 208.000000 | 5.11 | 4.820000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 08:00:00 | 85.000000 | 22.370000 | 26.050000 | 84.000000 | 1011.000000 | 1.77 | 25.270000 | 0.000000 | 7373.000000 | 216.000000 | 5.56 | 5.100000 | 501 | Rain | moderate rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 09:00:00 | 88.000000 | 22.260000 | 26.120000 | 83.000000 | 1011.000000 | 1.89 | 25.360000 | 0.000000 | 7382.000000 | 217.000000 | 6.34 | 5.750000 | 501 | Rain | moderate rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 22.240000 | 26.100000 | 83.000000 | 1011.000000 | 2.15 | 25.340000 | 0.000000 | 5650.000000 | 215.000000 | 6.49 | 5.760000 | 501 | Rain | moderate rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 11:00:00 | 91.000000 | 22.300000 | 26.160000 | 83.000000 | 1012.000000 | 2.14 | 25.400000 | 0.000000 | 5586.000000 | 220.000000 | 6.85 | 6.020000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 22.210000 | 26.260000 | 82.000000 | 1013.000000 | 1.74 | 25.510000 | 0.300000 | 9219.000000 | 224.000000 | 6.52 | 5.780000 | 501 | Rain | moderate rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 22.210000 | 26.460000 | 81.000000 | 1014.000000 | 1.09 | 25.720000 | 1.630000 | 10000.000000 | 230.000000 | 5.7 | 5.080000 | 501 | Rain | moderate rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 22.280000 | 26.330000 | 82.000000 | 1014.000000 | 1.34 | 25.580000 | 4.290000 | 7785.000000 | 240.000000 | 6.17 | 5.410000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 15:00:00 | 97.000000 | 22.130000 | 26.570000 | 80.000000 | 1015.000000 | 0.77 | 25.840000 | 7.760000 | 10000.000000 | 248.000000 | 5.98 | 5.380000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 22.200000 | 26.660000 | 80.000000 | 1014.000000 | 0.59 | 25.920000 | 10.980000 | 10000.000000 | 258.000000 | 6.13 | 5.650000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 17:00:00 | 90.000000 | 22.140000 | 26.070000 | 79.000000 | 1013.000000 |  | 26.070000 | 12.550000 | 10000.000000 | 267.000000 | 6.56 | 6.220000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 18:00:00 | 81.000000 | 22.030000 | 25.950000 | 79.000000 | 1013.000000 |  | 25.950000 | 11.950000 | 10000.000000 | 285.000000 | 5.03 | 4.760000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 19:00:00 | 85.000000 | 22.010000 | 26.640000 | 79.000000 | 1012.000000 | 0.13 | 25.930000 | 9.370000 | 10000.000000 | 291.000000 | 4.84 | 4.430000 | 500 | Rain | light rain | 10d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 20:00:00 | 69.000000 | 21.750000 | 26.100000 | 77.000000 | 1011.000000 |  | 26.100000 | 5.900000 | 10000.000000 | 297.000000 | 4.12 | 3.530000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 21:00:00 | 67.000000 | 21.500000 | 26.280000 | 75.000000 | 1010.000000 |  | 26.280000 | 2.710000 | 10000.000000 | 300.000000 | 3.71 | 3.040000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 22:00:00 | 69.000000 | 21.660000 | 26.450000 | 75.000000 | 1011.000000 | 0.13 | 26.450000 | 0.740000 | 10000.000000 | 294.000000 | 4.16 | 3.560000 | 500 | Rain | light rain | 10d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 57025020 | "GORGONA GUAPI [57025020]" | 2.962944 | -78.174361 | 10.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-18 00:00:00 | NaT | Cauca | Guapi | Magdalena | Area Operativa 07 - Nariño-Putumayo | Orinoco | Guaviare | Medio Guaviare | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 21.570000 | 26.580000 | 74.000000 | 1011.000000 |  | 26.580000 | 0.000000 | 10000.000000 | 287.000000 | 3.61 | 3.040000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station57025020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station57025020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station57025020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station57025020_OWM_Windspeed_20220111.png)
