
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16015110_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.89877778,-72.48716667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.89877778&lon=-72.48716667)


| Parameter | Value |
|---|---|
| Code | 16015110 |
| Name | UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110] |
| Latitude, ° | 7.89877778 |
| Longitude, ° | -72.48716667 |
| Elevation, m | 311 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-10-10 19:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Cúcuta |
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

### (CNE index 2888) Open Weather values for station 16015110 - UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]

JSON data from API OWM:

```
{'lat': 7.8988, 'lon': -72.4872, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812788, 'sunset': 1641854885, 'temp': 29.12, 'feels_like': 29.94, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.95, 'uvi': 3.84, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.12, 'feels_like': 24.62, 'pressure': 1016, 'humidity': 78, 'dew_point': 20.04, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 24.12, 'feels_like': 24.62, 'pressure': 1016, 'humidity': 78, 'dew_point': 20.04, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 23.12, 'feels_like': 23.79, 'pressure': 1017, 'humidity': 88, 'dew_point': 21.02, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 22.12, 'feels_like': 23, 'pressure': 1017, 'humidity': 100, 'dew_point': 22.12, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 120, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 21.12, 'feels_like': 21.9, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.12, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 140, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641790800, 'temp': 21.12, 'feels_like': 21.9, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.12, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 21.12, 'feels_like': 21.9, 'pressure': 1016, 'humidity': 100, 'dew_point': 21.12, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 20.07, 'feels_like': 20.12, 'pressure': 1015, 'humidity': 76, 'dew_point': 15.71, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 192, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.09, 'feels_like': 20.09, 'pressure': 1014, 'humidity': 74, 'dew_point': 15.32, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 184, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 19.98, 'feels_like': 19.91, 'pressure': 1014, 'humidity': 72, 'dew_point': 14.78, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 185, 'wind_gust': 1.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 19.12, 'feels_like': 19.39, 'pressure': 1015, 'humidity': 88, 'dew_point': 17.09, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641812400, 'temp': 18.12, 'feels_like': 18.44, 'pressure': 1016, 'humidity': 94, 'dew_point': 17.14, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 130, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 18.12, 'feels_like': 18.44, 'pressure': 1016, 'humidity': 94, 'dew_point': 17.14, 'uvi': 0.52, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 22.12, 'feels_like': 22.29, 'pressure': 1018, 'humidity': 73, 'dew_point': 17.06, 'uvi': 2.11, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 25.12, 'feels_like': 25.28, 'pressure': 1018, 'humidity': 61, 'dew_point': 17.07, 'uvi': 4.88, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 330, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 26.12, 'feels_like': 26.12, 'pressure': 1018, 'humidity': 57, 'dew_point': 16.94, 'uvi': 8.05, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 28.12, 'feels_like': 28.68, 'pressure': 1017, 'humidity': 51, 'dew_point': 17.04, 'uvi': 10.48, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 28.12, 'feels_like': 28.97, 'pressure': 1016, 'humidity': 54, 'dew_point': 17.94, 'uvi': 11.16, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 29.12, 'feels_like': 29.94, 'pressure': 1015, 'humidity': 51, 'dew_point': 17.95, 'uvi': 9.84, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 360, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 30.12, 'feels_like': 30.91, 'pressure': 1014, 'humidity': 48, 'dew_point': 17.91, 'uvi': 7, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 350, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 29.12, 'feels_like': 29.94, 'pressure': 1013, 'humidity': 51, 'dew_point': 17.95, 'uvi': 3.84, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 20, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641848400, 'temp': 28.12, 'feels_like': 28.97, 'pressure': 1013, 'humidity': 54, 'dew_point': 17.94, 'uvi': 1.43, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 360, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641852000, 'temp': 27.12, 'feels_like': 28.01, 'pressure': 1014, 'humidity': 57, 'dew_point': 17.87, 'uvi': 0.25, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641855600, 'temp': 27.12, 'feels_like': 28.01, 'pressure': 1014, 'humidity': 57, 'dew_point': 17.87, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 350, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 20.040000 | 24.620000 | 78.000000 | 1016.000000 |  | 24.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 01:00:00 | 40.000000 | 20.040000 | 24.620000 | 78.000000 | 1016.000000 |  | 24.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 02:00:00 | 40.000000 | 21.020000 | 23.790000 | 88.000000 | 1017.000000 |  | 23.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 03:00:00 | 40.000000 | 22.120000 | 23.000000 | 100.000000 | 1017.000000 |  | 22.120000 | 0.000000 | 10000.000000 | 120.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 04:00:00 | 40.000000 | 21.120000 | 21.900000 | 100.000000 | 1016.000000 |  | 21.120000 | 0.000000 | 10000.000000 | 140.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 05:00:00 | 40.000000 | 21.120000 | 21.900000 | 100.000000 | 1016.000000 |  | 21.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 06:00:00 | 40.000000 | 21.120000 | 21.900000 | 100.000000 | 1016.000000 |  | 21.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 07:00:00 | 82.000000 | 15.710000 | 20.120000 | 76.000000 | 1015.000000 |  | 20.070000 | 0.000000 | 10000.000000 | 192.000000 | 1.13 | 0.850000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 08:00:00 | 70.000000 | 15.320000 | 20.090000 | 74.000000 | 1014.000000 |  | 20.090000 | 0.000000 | 10000.000000 | 184.000000 | 1.14 | 1.010000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 09:00:00 | 67.000000 | 14.780000 | 19.910000 | 72.000000 | 1014.000000 |  | 19.980000 | 0.000000 | 10000.000000 | 185.000000 | 1.75 | 1.430000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 10:00:00 | 20.000000 | 17.090000 | 19.390000 | 88.000000 | 1015.000000 |  | 19.120000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 17.140000 | 18.440000 | 94.000000 | 1016.000000 |  | 18.120000 | 0.000000 | 10000.000000 | 130.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 17.140000 | 18.440000 | 94.000000 | 1016.000000 |  | 18.120000 | 0.520000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 17.060000 | 22.290000 | 73.000000 | 1018.000000 |  | 22.120000 | 2.110000 | 10000.000000 | 140.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 17.070000 | 25.280000 | 61.000000 | 1018.000000 |  | 25.120000 | 4.880000 | 10000.000000 | 330.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 15:00:00 | 40.000000 | 16.940000 | 26.120000 | 57.000000 | 1018.000000 |  | 26.120000 | 8.050000 | 10000.000000 | 0.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 17.040000 | 28.680000 | 51.000000 | 1017.000000 |  | 28.120000 | 10.480000 | 10000.000000 | 0.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 17.940000 | 28.970000 | 54.000000 | 1016.000000 |  | 28.120000 | 11.160000 | 10000.000000 | 20.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 17.950000 | 29.940000 | 51.000000 | 1015.000000 |  | 29.120000 | 9.840000 | 10000.000000 | 360.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 17.910000 | 30.910000 | 48.000000 | 1014.000000 |  | 30.120000 | 7.000000 | 10000.000000 | 350.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 20:00:00 | 40.000000 | 17.950000 | 29.940000 | 51.000000 | 1013.000000 |  | 29.120000 | 3.840000 | 10000.000000 | 20.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 21:00:00 | 40.000000 | 17.940000 | 28.970000 | 54.000000 | 1013.000000 |  | 28.120000 | 1.430000 | 10000.000000 | 360.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 22:00:00 | 40.000000 | 17.870000 | 28.010000 | 57.000000 | 1014.000000 |  | 27.120000 | 0.250000 | 10000.000000 | 10.000000 |  | 4.630000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16015110 | "UNIVERSIDAD FRANCISO DE PAULA SANTANDER - AUT [16015110]" | 7.898778 | -72.487167 | 311.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-10 19:00:00 | NaT | Norte de Santander | Cúcuta | 0 | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Pamplonita | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 17.870000 | 28.010000 | 57.000000 | 1014.000000 |  | 27.120000 | 0.000000 | 10000.000000 | 350.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station16015110_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16015110_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16015110_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16015110_OWM_Windspeed_20220111.png)
