
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BERLIN - AUT [37015030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station37015030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.187,-72.8685) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.187&lon=-72.8685)


| Parameter | Value |
|---|---|
| Code | 37015030 |
| Name | BERLIN - AUT [37015030] |
| Latitude, ° | 7.187 |
| Longitude, ° | -72.8685 |
| Elevation, m | 3316 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2008-08-21 00:00:00 |
| Suspension date | NaT |
| State | Santander |
| County | Tona |
| Stream | Zulia |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Arauca |
| SZH - Hydrographic subzone | Río Chítaga |

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

### (CNE index 182) Open Weather values for station 37015030 - BERLIN - AUT [37015030]

JSON data from API OWM:

```
{'lat': 7.187, 'lon': -72.8685, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812810, 'sunset': 1641855046, 'temp': 9.9, 'feels_like': 9.42, 'pressure': 1014, 'humidity': 80, 'dew_point': 6.62, 'uvi': 2.46, 'clouds': 78, 'visibility': 9522, 'wind_speed': 1.61, 'wind_deg': 310, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, 'hourly': [{'dt': 1641772800, 'temp': 5.9, 'feels_like': 4.76, 'pressure': 1018, 'humidity': 95, 'dew_point': 5.16, 'uvi': 0, 'clouds': 81, 'visibility': 4045, 'wind_speed': 1.68, 'wind_deg': 54, 'wind_gust': 1.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 4.9, 'feels_like': 3.91, 'pressure': 1019, 'humidity': 93, 'dew_point': 3.86, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 55, 'wind_gust': 1.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 4.9, 'feels_like': 3.83, 'pressure': 1019, 'humidity': 92, 'dew_point': 3.71, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 59, 'wind_gust': 1.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1019, 'humidity': 92, 'dew_point': 3.71, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 63, 'wind_gust': 1.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1019, 'humidity': 91, 'dew_point': 4.55, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 61, 'wind_gust': 1.18, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1018, 'humidity': 91, 'dew_point': 4.55, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 85, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 4.82, 'feels_like': 4.82, 'pressure': 1018, 'humidity': 90, 'dew_point': 3.32, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 108, 'wind_gust': 1.23, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 4.51, 'feels_like': 4.51, 'pressure': 1017, 'humidity': 91, 'dew_point': 3.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 142, 'wind_gust': 1.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 4.61, 'feels_like': 4.61, 'pressure': 1016, 'humidity': 91, 'dew_point': 3.27, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 186, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 4.27, 'feels_like': 4.27, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.09, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 201, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 4.39, 'feels_like': 4.39, 'pressure': 1017, 'humidity': 92, 'dew_point': 3.21, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 212, 'wind_gust': 1.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1018, 'humidity': 92, 'dew_point': 3.71, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 211, 'wind_gust': 1.03, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 4.9, 'feels_like': 4.9, 'pressure': 1019, 'humidity': 88, 'dew_point': 3.08, 'uvi': 0.56, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 194, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1019, 'humidity': 81, 'dew_point': 2.89, 'uvi': 1.83, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 216, 'wind_gust': 0.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 73, 'dew_point': 3.37, 'uvi': 4.28, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 270, 'wind_gust': 1.09, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 8.9, 'feels_like': 8.52, 'pressure': 1018, 'humidity': 67, 'dew_point': 3.11, 'uvi': 7.11, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 284, 'wind_gust': 1.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 8.9, 'feels_like': 8.09, 'pressure': 1017, 'humidity': 63, 'dew_point': 2.25, 'uvi': 10.25, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 287, 'wind_gust': 2.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 10.9, 'feels_like': 9.66, 'pressure': 1016, 'humidity': 62, 'dew_point': 3.91, 'uvi': 10.99, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.96, 'wind_deg': 291, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 10.9, 'feels_like': 9.74, 'pressure': 1015, 'humidity': 65, 'dew_point': 4.59, 'uvi': 9.76, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.98, 'wind_deg': 298, 'wind_gust': 2.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 10.9, 'feels_like': 9.87, 'pressure': 1014, 'humidity': 70, 'dew_point': 5.65, 'uvi': 4.42, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 306, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 9.9, 'feels_like': 9.42, 'pressure': 1014, 'humidity': 80, 'dew_point': 6.62, 'uvi': 2.46, 'clouds': 78, 'visibility': 9522, 'wind_speed': 1.61, 'wind_deg': 310, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641848400, 'temp': 9.9, 'feels_like': 9.65, 'pressure': 1014, 'humidity': 87, 'dew_point': 7.84, 'uvi': 0.93, 'clouds': 85, 'visibility': 4952, 'wind_speed': 1.39, 'wind_deg': 321, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641852000, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1015, 'humidity': 91, 'dew_point': 7.51, 'uvi': 0.16, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 338, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641855600, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1016, 'humidity': 94, 'dew_point': 6, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 358, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 00:00:00 | 81.000000 | 5.160000 | 4.760000 | 95.000000 | 1018.000000 |  | 5.900000 | 0.000000 | 4045.000000 | 54.000000 | 1.82 | 1.680000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 01:00:00 | 91.000000 | 3.860000 | 3.910000 | 93.000000 | 1019.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 55.000000 | 1.4 | 1.440000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 02:00:00 | 82.000000 | 3.710000 | 3.830000 | 92.000000 | 1019.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 59.000000 | 1.62 | 1.500000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 03:00:00 | 82.000000 | 3.710000 | 4.900000 | 92.000000 | 1019.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 63.000000 | 1.27 | 1.150000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 04:00:00 | 77.000000 | 4.550000 | 5.900000 | 91.000000 | 1019.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 61.000000 | 1.18 | 1.030000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 05:00:00 | 76.000000 | 4.550000 | 5.900000 | 91.000000 | 1018.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 85.000000 | 1.05 | 1.020000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 3.320000 | 4.820000 | 90.000000 | 1018.000000 |  | 4.820000 | 0.000000 | 10000.000000 | 108.000000 | 1.23 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 3.170000 | 4.510000 | 91.000000 | 1017.000000 |  | 4.510000 | 0.000000 | 10000.000000 | 142.000000 | 1.15 | 0.810000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 08:00:00 | 77.000000 | 3.270000 | 4.610000 | 91.000000 | 1016.000000 |  | 4.610000 | 0.000000 | 10000.000000 | 186.000000 | 1.11 | 0.720000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 09:00:00 | 71.000000 | 3.090000 | 4.270000 | 92.000000 | 1017.000000 |  | 4.270000 | 0.000000 | 10000.000000 | 201.000000 | 1.04 | 0.730000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 10:00:00 | 74.000000 | 3.210000 | 4.390000 | 92.000000 | 1017.000000 |  | 4.390000 | 0.000000 | 10000.000000 | 212.000000 | 1.14 | 0.840000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 11:00:00 | 73.000000 | 3.710000 | 4.900000 | 92.000000 | 1018.000000 |  | 4.900000 | 0.000000 | 10000.000000 | 211.000000 | 1.03 | 0.740000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 12:00:00 | 62.000000 | 3.080000 | 4.900000 | 88.000000 | 1019.000000 |  | 4.900000 | 0.560000 | 10000.000000 | 194.000000 | 0.9 | 0.580000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 13:00:00 | 76.000000 | 2.890000 | 5.900000 | 81.000000 | 1019.000000 |  | 5.900000 | 1.830000 | 10000.000000 | 216.000000 | 0.94 | 0.600000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 14:00:00 | 87.000000 | 3.370000 | 7.900000 | 73.000000 | 1019.000000 |  | 7.900000 | 4.280000 | 10000.000000 | 270.000000 | 1.09 | 0.840000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 15:00:00 | 89.000000 | 3.110000 | 8.520000 | 67.000000 | 1018.000000 |  | 8.900000 | 7.110000 | 10000.000000 | 284.000000 | 1.66 | 1.390000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 16:00:00 | 88.000000 | 2.250000 | 8.090000 | 63.000000 | 1017.000000 |  | 8.900000 | 10.250000 | 10000.000000 | 287.000000 | 2.06 | 1.800000 | 804 | Clouds | overcast clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 17:00:00 | 83.000000 | 3.910000 | 9.660000 | 62.000000 | 1016.000000 |  | 10.900000 | 10.990000 | 10000.000000 | 291.000000 | 2.3 | 1.960000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 18:00:00 | 60.000000 | 4.590000 | 9.740000 | 65.000000 | 1015.000000 |  | 10.900000 | 9.760000 | 10000.000000 | 298.000000 | 2.46 | 1.980000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 19:00:00 | 72.000000 | 5.650000 | 9.870000 | 70.000000 | 1014.000000 |  | 10.900000 | 4.420000 | 10000.000000 | 306.000000 | 2.38 | 1.710000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 20:00:00 | 78.000000 | 6.620000 | 9.420000 | 80.000000 | 1014.000000 | 0.14 | 9.900000 | 2.460000 | 9522.000000 | 310.000000 | 2.06 | 1.610000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 21:00:00 | 85.000000 | 7.840000 | 9.650000 | 87.000000 | 1014.000000 | 0.13 | 9.900000 | 0.930000 | 4952.000000 | 321.000000 | 1.79 | 1.390000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 7.510000 | 8.900000 | 91.000000 | 1015.000000 | 0.14 | 8.900000 | 0.160000 | 10000.000000 | 338.000000 | 1.58 | 1.160000 | 500 | Rain | light rain | 10d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 37015030 | "BERLIN - AUT [37015030]" | 7.187000 | -72.868500 | 3316.000000 | Climática Principal | Automática con Telemetría | Activa | 2008-08-21 00:00:00 | NaT | Santander | Tona | Zulia | Area Operativa 08 - Santanderes-Arauca | Orinoco | Arauca | Río Chítaga | America/Bogota | 2022-01-10 23:00:00 | 91.000000 | 6.000000 | 6.900000 | 94.000000 | 1016.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 358.000000 | 1.22 | 0.920000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station37015030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station37015030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station37015030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station37015030_OWM_Windspeed_20220111.png)
