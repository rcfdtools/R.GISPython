
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ALCALDIA DE HERRAN  - AUT [16015130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16015130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.50672222,-72.48536111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.50672222&lon=-72.48536111)


| Parameter | Value |
|---|---|
| Code | 16015130 |
| Name | ALCALDIA DE HERRAN  - AUT [16015130] |
| Latitude, ° | 7.50672222 |
| Longitude, ° | -72.48536111 |
| Elevation, m | 240 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-08-18 19:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Herrán |
| Stream | 0 |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Pamplonita |

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

### (CNE index 332) Open Weather values for station 16015130 - ALCALDIA DE HERRAN  - AUT [16015130]

JSON data from API OWM:

```
{'lat': 7.5067, 'lon': -72.4854, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812749, 'sunset': 1641854923, 'temp': 19.04, 'feels_like': 18.75, 'pressure': 1014, 'humidity': 67, 'dew_point': 12.78, 'uvi': 3.84, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 355, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 14.04, 'feels_like': 14.08, 'pressure': 1018, 'humidity': 99, 'dew_point': 13.89, 'uvi': 0, 'clouds': 90, 'visibility': 1232, 'wind_speed': 1.14, 'wind_deg': 335, 'wind_gust': 2.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641776400, 'temp': 14.04, 'feels_like': 14.06, 'pressure': 1019, 'humidity': 98, 'dew_point': 13.73, 'uvi': 0, 'clouds': 97, 'visibility': 1356, 'wind_speed': 0.93, 'wind_deg': 328, 'wind_gust': 2.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641780000, 'temp': 13.04, 'feels_like': 12.96, 'pressure': 1020, 'humidity': 98, 'dew_point': 12.73, 'uvi': 0, 'clouds': 98, 'visibility': 5803, 'wind_speed': 0.82, 'wind_deg': 305, 'wind_gust': 2.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 12.04, 'feels_like': 11.83, 'pressure': 1020, 'humidity': 97, 'dew_point': 11.58, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 265, 'wind_gust': 1.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 11.04, 'feels_like': 10.73, 'pressure': 1020, 'humidity': 97, 'dew_point': 10.58, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 240, 'wind_gust': 1.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 11.04, 'feels_like': 10.71, 'pressure': 1020, 'humidity': 96, 'dew_point': 10.43, 'uvi': 0, 'clouds': 91, 'visibility': 8133, 'wind_speed': 1.13, 'wind_deg': 207, 'wind_gust': 1.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 11.04, 'feels_like': 10.68, 'pressure': 1019, 'humidity': 95, 'dew_point': 10.27, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 195, 'wind_gust': 1.8, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 10.18, 'feels_like': 9.71, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.26, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 1.84, 'wind_deg': 186, 'wind_gust': 2.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.97, 'feels_like': 9.3, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.05, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 179, 'wind_gust': 2.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.98, 'feels_like': 9.31, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.06, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 174, 'wind_gust': 1.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 9.04, 'feels_like': 8.37, 'pressure': 1018, 'humidity': 93, 'dew_point': 7.97, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 168, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 8.04, 'feels_like': 7.27, 'pressure': 1018, 'humidity': 94, 'dew_point': 7.13, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 166, 'wind_gust': 1.43, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 8.04, 'feels_like': 7.61, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.66, 'uvi': 0.52, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 161, 'wind_gust': 2.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 12.04, 'feels_like': 11.44, 'pressure': 1019, 'humidity': 82, 'dew_point': 9.07, 'uvi': 2.11, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 115, 'wind_gust': 1.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 15.04, 'feels_like': 14.56, 'pressure': 1020, 'humidity': 75, 'dew_point': 10.65, 'uvi': 4.88, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 69, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 16.04, 'feels_like': 15.5, 'pressure': 1019, 'humidity': 69, 'dew_point': 10.36, 'uvi': 8.05, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 44, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.04, 'feels_like': 17.57, 'pressure': 1018, 'humidity': 64, 'dew_point': 11.13, 'uvi': 10.48, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 24, 'wind_gust': 1.43, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 18.04, 'feels_like': 17.68, 'pressure': 1018, 'humidity': 68, 'dew_point': 12.05, 'uvi': 11.16, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 28, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 19.04, 'feels_like': 18.78, 'pressure': 1017, 'humidity': 68, 'dew_point': 13, 'uvi': 9.84, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 27, 'wind_gust': 1.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 20.04, 'feels_like': 19.8, 'pressure': 1015, 'humidity': 65, 'dew_point': 13.27, 'uvi': 7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.81, 'wind_deg': 8, 'wind_gust': 1.59, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 19.04, 'feels_like': 18.75, 'pressure': 1014, 'humidity': 67, 'dew_point': 12.78, 'uvi': 3.84, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 355, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 18.04, 'feels_like': 17.81, 'pressure': 1015, 'humidity': 73, 'dew_point': 13.13, 'uvi': 1.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 357, 'wind_gust': 2.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 17.04, 'feels_like': 16.91, 'pressure': 1016, 'humidity': 81, 'dew_point': 13.76, 'uvi': 0.25, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 2, 'wind_gust': 3.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 17.04, 'feels_like': 17.12, 'pressure': 1016, 'humidity': 89, 'dew_point': 15.21, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 340, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 00:00:00 | 90.000000 | 13.890000 | 14.080000 | 99.000000 | 1018.000000 | 0.18 | 14.040000 | 0.000000 | 1232.000000 | 335.000000 | 2.52 | 1.140000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 01:00:00 | 97.000000 | 13.730000 | 14.060000 | 98.000000 | 1019.000000 | 0.18 | 14.040000 | 0.000000 | 1356.000000 | 328.000000 | 2.38 | 0.930000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 02:00:00 | 98.000000 | 12.730000 | 12.960000 | 98.000000 | 1020.000000 |  | 13.040000 | 0.000000 | 5803.000000 | 305.000000 | 2.03 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 03:00:00 | 95.000000 | 11.580000 | 11.830000 | 97.000000 | 1020.000000 |  | 12.040000 | 0.000000 | 10000.000000 | 265.000000 | 1.86 | 0.740000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 10.580000 | 10.730000 | 97.000000 | 1020.000000 |  | 11.040000 | 0.000000 | 10000.000000 | 240.000000 | 1.94 | 0.940000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 05:00:00 | 91.000000 | 10.430000 | 10.710000 | 96.000000 | 1020.000000 |  | 11.040000 | 0.000000 | 8133.000000 | 207.000000 | 1.56 | 1.130000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 06:00:00 | 41.000000 | 10.270000 | 10.680000 | 95.000000 | 1019.000000 |  | 11.040000 | 0.000000 | 10000.000000 | 195.000000 | 1.8 | 1.590000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 07:00:00 | 58.000000 | 9.260000 | 9.710000 | 94.000000 | 1018.000000 |  | 10.180000 | 0.000000 | 10000.000000 | 186.000000 | 2.35 | 1.840000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 08:00:00 | 51.000000 | 9.050000 | 9.300000 | 94.000000 | 1018.000000 |  | 9.970000 | 0.000000 | 10000.000000 | 179.000000 | 2.25 | 1.830000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 09:00:00 | 48.000000 | 9.060000 | 9.310000 | 94.000000 | 1018.000000 |  | 9.980000 | 0.000000 | 10000.000000 | 174.000000 | 1.97 | 1.830000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 10:00:00 | 42.000000 | 7.970000 | 8.370000 | 93.000000 | 1018.000000 |  | 9.040000 | 0.000000 | 10000.000000 | 168.000000 | 1.43 | 1.680000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 11:00:00 | 47.000000 | 7.130000 | 7.270000 | 94.000000 | 1018.000000 |  | 8.040000 | 0.000000 | 10000.000000 | 166.000000 | 1.43 | 1.630000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 12:00:00 | 66.000000 | 6.660000 | 7.610000 | 91.000000 | 1019.000000 |  | 8.040000 | 0.520000 | 10000.000000 | 161.000000 | 2.06 | 1.340000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 13:00:00 | 88.000000 | 9.070000 | 11.440000 | 82.000000 | 1019.000000 |  | 12.040000 | 2.110000 | 10000.000000 | 115.000000 | 1.61 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 14:00:00 | 94.000000 | 10.650000 | 14.560000 | 75.000000 | 1020.000000 |  | 15.040000 | 4.880000 | 10000.000000 | 69.000000 | 1.44 | 0.740000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 15:00:00 | 96.000000 | 10.360000 | 15.500000 | 69.000000 | 1019.000000 |  | 16.040000 | 8.050000 | 10000.000000 | 44.000000 | 1.18 | 1.060000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 16:00:00 | 96.000000 | 11.130000 | 17.570000 | 64.000000 | 1018.000000 |  | 18.040000 | 10.480000 | 10000.000000 | 24.000000 | 1.43 | 1.870000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 17:00:00 | 97.000000 | 12.050000 | 17.680000 | 68.000000 | 1018.000000 |  | 18.040000 | 11.160000 | 10000.000000 | 28.000000 | 1.77 | 2.050000 | 804 | Clouds | overcast clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 18:00:00 | 98.000000 | 13.000000 | 18.780000 | 68.000000 | 1017.000000 |  | 19.040000 | 9.840000 | 10000.000000 | 27.000000 | 1.49 | 1.730000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.270000 | 19.800000 | 65.000000 | 1015.000000 |  | 20.040000 | 7.000000 | 10000.000000 | 8.000000 | 1.59 | 1.810000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 12.780000 | 18.750000 | 67.000000 | 1014.000000 |  | 19.040000 | 3.840000 | 10000.000000 | 355.000000 | 1.88 | 1.860000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 13.130000 | 17.810000 | 73.000000 | 1015.000000 |  | 18.040000 | 1.430000 | 10000.000000 | 357.000000 | 2.51 | 1.690000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 13.760000 | 16.910000 | 81.000000 | 1016.000000 |  | 17.040000 | 0.250000 | 10000.000000 | 2.000000 | 3.03 | 1.500000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015130 | "ALCALDIA DE HERRAN  - AUT [16015130]" | 7.506722 | -72.485361 | 240.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-08-18 19:00:00 | NaT | Norte de Santander | Herrán | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 15.210000 | 17.120000 | 89.000000 | 1016.000000 |  | 17.040000 | 0.000000 | 10000.000000 | 340.000000 | 2.3 | 0.990000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16015130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16015130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16015130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015130_OWM_Windspeed_20220111.png)
