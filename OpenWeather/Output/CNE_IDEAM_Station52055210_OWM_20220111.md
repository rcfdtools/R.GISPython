
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BOTANA - AUT [52055210] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52055210_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.16,-77.27880556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.16&lon=-77.27880556)


| Parameter | Value |
|---|---|
| Code | 52055210 |
| Name | BOTANA - AUT [52055210] |
| Latitude, ° | 1.16 |
| Longitude, ° | -77.27880556 |
| Elevation, m | 2820 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-03-01 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Pasto |
| Stream | Hacha |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Juananbú |

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

### (CNE index 20) Open Weather values for station 52055210 - BOTANA - AUT [52055210]

JSON data from API OWM:

```
{'lat': 1.16, 'lon': -77.2788, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813284, 'sunset': 1641856689, 'temp': 11.38, 'feels_like': 10.95, 'pressure': 1014, 'humidity': 91, 'dew_point': 9.96, 'uvi': 4.56, 'clouds': 99, 'visibility': 6819, 'wind_speed': 1.82, 'wind_deg': 328, 'wind_gust': 2.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, 'hourly': [{'dt': 1641772800, 'temp': 11.24, 'feels_like': 10.9, 'pressure': 1017, 'humidity': 95, 'dew_point': 10.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 323, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641776400, 'temp': 10.21, 'feels_like': 9.74, 'pressure': 1018, 'humidity': 94, 'dew_point': 9.29, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 325, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 10.09, 'feels_like': 9.64, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.33, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 328, 'wind_gust': 0.59, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 10.08, 'feels_like': 9.65, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 270, 'wind_gust': 0.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 10.03, 'feels_like': 9.57, 'pressure': 1019, 'humidity': 95, 'dew_point': 9.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 165, 'wind_gust': 0.4, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.01, 'feels_like': 9.55, 'pressure': 1018, 'humidity': 95, 'dew_point': 9.25, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 222, 'wind_gust': 0.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 9.93, 'feels_like': 9.93, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.17, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 273, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 9.82, 'feels_like': 9.82, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.06, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 256, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.4, 'feels_like': 9.4, 'pressure': 1016, 'humidity': 96, 'dew_point': 8.8, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 264, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.18, 'feels_like': 9.18, 'pressure': 1016, 'humidity': 97, 'dew_point': 8.73, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 308, 'wind_gust': 0.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 8.89, 'feels_like': 8.89, 'pressure': 1017, 'humidity': 97, 'dew_point': 8.44, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 239, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 8.24, 'feels_like': 8.24, 'pressure': 1018, 'humidity': 97, 'dew_point': 7.79, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 250, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.24, 'feels_like': 8.24, 'pressure': 1018, 'humidity': 95, 'dew_point': 7.49, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 216, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 9.27, 'feels_like': 9.27, 'pressure': 1019, 'humidity': 90, 'dew_point': 7.72, 'uvi': 1.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 284, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.34, 'feels_like': 9.54, 'pressure': 1018, 'humidity': 81, 'dew_point': 7.23, 'uvi': 2.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 320, 'wind_gust': 0.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 12.34, 'feels_like': 11.67, 'pressure': 1018, 'humidity': 78, 'dew_point': 8.62, 'uvi': 5.22, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 327, 'wind_gust': 1.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641830400, 'temp': 12.41, 'feels_like': 11.87, 'pressure': 1017, 'humidity': 83, 'dew_point': 9.61, 'uvi': 8.9, 'clouds': 100, 'visibility': 6908, 'wind_speed': 1.88, 'wind_deg': 339, 'wind_gust': 1.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641834000, 'temp': 13.34, 'feels_like': 13.05, 'pressure': 1017, 'humidity': 89, 'dew_point': 11.57, 'uvi': 10.03, 'clouds': 100, 'visibility': 4724, 'wind_speed': 1.59, 'wind_deg': 342, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641837600, 'temp': 13.38, 'feels_like': 13.07, 'pressure': 1016, 'humidity': 88, 'dew_point': 11.44, 'uvi': 9.45, 'clouds': 90, 'visibility': 7367, 'wind_speed': 1.6, 'wind_deg': 340, 'wind_gust': 1.69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641841200, 'temp': 12.45, 'feels_like': 12.02, 'pressure': 1015, 'humidity': 87, 'dew_point': 10.35, 'uvi': 7.32, 'clouds': 100, 'visibility': 6030, 'wind_speed': 1.92, 'wind_deg': 328, 'wind_gust': 2.23, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641844800, 'temp': 11.38, 'feels_like': 10.95, 'pressure': 1014, 'humidity': 91, 'dew_point': 9.96, 'uvi': 4.56, 'clouds': 99, 'visibility': 6819, 'wind_speed': 1.82, 'wind_deg': 328, 'wind_gust': 2.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641848400, 'temp': 11.31, 'feels_like': 10.92, 'pressure': 1014, 'humidity': 93, 'dew_point': 10.22, 'uvi': 2.07, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 326, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.9}}, {'dt': 1641852000, 'temp': 11.27, 'feels_like': 10.99, 'pressure': 1015, 'humidity': 97, 'dew_point': 10.81, 'uvi': 0.62, 'clouds': 100, 'visibility': 3985, 'wind_speed': 1.38, 'wind_deg': 319, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641855600, 'temp': 10.24, 'feels_like': 9.88, 'pressure': 1016, 'humidity': 98, 'dew_point': 9.94, 'uvi': 0, 'clouds': 100, 'visibility': 3291, 'wind_speed': 1.4, 'wind_deg': 317, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 10.470000 | 10.900000 | 95.000000 | 1017.000000 | 0.12 | 11.240000 | 0.000000 | 10000.000000 | 323.000000 | 0.93 | 0.770000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.290000 | 9.740000 | 94.000000 | 1018.000000 |  | 10.210000 | 0.000000 | 10000.000000 | 325.000000 | 0.87 | 0.560000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 9.330000 | 9.640000 | 95.000000 | 1019.000000 | 0.12 | 10.090000 | 0.000000 | 10000.000000 | 328.000000 | 0.59 | 0.390000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.470000 | 9.650000 | 96.000000 | 1019.000000 |  | 10.080000 | 0.000000 | 10000.000000 | 270.000000 | 0.39 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.270000 | 9.570000 | 95.000000 | 1019.000000 |  | 10.030000 | 0.000000 | 10000.000000 | 165.000000 | 0.4 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 9.250000 | 9.550000 | 95.000000 | 1018.000000 |  | 10.010000 | 0.000000 | 10000.000000 | 222.000000 | 0.39 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 9.170000 | 9.930000 | 95.000000 | 1017.000000 |  | 9.930000 | 0.000000 | 10000.000000 | 273.000000 | 0.51 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 9.060000 | 9.820000 | 95.000000 | 1017.000000 |  | 9.820000 | 0.000000 | 10000.000000 | 256.000000 | 0.88 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 8.800000 | 9.400000 | 96.000000 | 1016.000000 |  | 9.400000 | 0.000000 | 10000.000000 | 264.000000 | 0.94 | 0.670000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 8.730000 | 9.180000 | 97.000000 | 1016.000000 |  | 9.180000 | 0.000000 | 10000.000000 | 308.000000 | 0.95 | 0.620000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 8.440000 | 8.890000 | 97.000000 | 1017.000000 |  | 8.890000 | 0.000000 | 10000.000000 | 239.000000 | 0.75 | 0.570000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 7.790000 | 8.240000 | 97.000000 | 1018.000000 |  | 8.240000 | 0.000000 | 10000.000000 | 250.000000 | 0.86 | 0.450000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 7.490000 | 8.240000 | 95.000000 | 1018.000000 |  | 8.240000 | 0.260000 | 10000.000000 | 216.000000 | 1.1 | 0.760000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 7.720000 | 9.270000 | 90.000000 | 1019.000000 |  | 9.270000 | 1.160000 | 10000.000000 | 284.000000 | 0.91 | 0.720000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 7.230000 | 9.540000 | 81.000000 | 1018.000000 |  | 10.340000 | 2.970000 | 10000.000000 | 320.000000 | 0.99 | 1.150000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 8.620000 | 11.670000 | 78.000000 | 1018.000000 | 0.36 | 12.340000 | 5.220000 | 10000.000000 | 327.000000 | 1.56 | 1.740000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 9.610000 | 11.870000 | 83.000000 | 1017.000000 | 0.76 | 12.410000 | 8.900000 | 6908.000000 | 339.000000 | 1.97 | 1.880000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 11.570000 | 13.050000 | 89.000000 | 1017.000000 | 0.94 | 13.340000 | 10.030000 | 4724.000000 | 342.000000 | 1.77 | 1.590000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 11.440000 | 13.070000 | 88.000000 | 1016.000000 | 1.02 | 13.380000 | 9.450000 | 7367.000000 | 340.000000 | 1.69 | 1.600000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 10.350000 | 12.020000 | 87.000000 | 1015.000000 | 1.03 | 12.450000 | 7.320000 | 6030.000000 | 328.000000 | 2.23 | 1.920000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 9.960000 | 10.950000 | 91.000000 | 1014.000000 | 1.02 | 11.380000 | 4.560000 | 6819.000000 | 328.000000 | 2.19 | 1.820000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 10.220000 | 10.920000 | 93.000000 | 1014.000000 | 0.9 | 11.310000 | 2.070000 | 10000.000000 | 326.000000 | 2.19 | 1.580000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 10.810000 | 10.990000 | 97.000000 | 1015.000000 | 0.67 | 11.270000 | 0.620000 | 3985.000000 | 319.000000 | 2.01 | 1.380000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52055210 | "BOTANA - AUT [52055210]" | 1.160000 | -77.278806 | 2820.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-03-01 00:00:00 | NaT | Nariño | Pasto | Hacha | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Juananbú | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 9.940000 | 9.880000 | 98.000000 | 1016.000000 | 0.42 | 10.240000 | 0.000000 | 3291.000000 | 317.000000 | 2.1 | 1.400000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52055210_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52055210_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52055210_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52055210_OWM_Windspeed_20220111.png)
