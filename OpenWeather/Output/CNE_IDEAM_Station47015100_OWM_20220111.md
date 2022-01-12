
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL ENCANO - AUT [47015100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station47015100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.15994444,-77.16147222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.15994444&lon=-77.16147222)


| Parameter | Value |
|---|---|
| Code | 47015100 |
| Name | EL ENCANO - AUT [47015100] |
| Latitude, ° | 1.15994444 |
| Longitude, ° | -77.16147222 |
| Elevation, m | 2830 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1984-09-14 19:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Pasto |
| Stream | 0 |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Putumayo |
| SZH - Hydrographic subzone | Alto Río Putumayo |

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

### (CNE index 3567) Open Weather values for station 47015100 - EL ENCANO - AUT [47015100]

JSON data from API OWM:

```
{'lat': 1.1599, 'lon': -77.1615, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813256, 'sunset': 1641856661, 'temp': 11.38, 'feels_like': 10.98, 'pressure': 1014, 'humidity': 92, 'dew_point': 10.13, 'uvi': 4.56, 'clouds': 100, 'visibility': 4854, 'wind_speed': 1.22, 'wind_deg': 327, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}, 'hourly': [{'dt': 1641772800, 'temp': 11.38, 'feels_like': 11.08, 'pressure': 1017, 'humidity': 96, 'dew_point': 10.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 321, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641776400, 'temp': 10.47, 'feels_like': 10.05, 'pressure': 1018, 'humidity': 95, 'dew_point': 9.7, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 319, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641780000, 'temp': 10.38, 'feels_like': 9.98, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 321, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 10.32, 'feels_like': 9.91, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 282, 'wind_gust': 0.33, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 10.22, 'feels_like': 9.83, 'pressure': 1019, 'humidity': 97, 'dew_point': 9.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 172, 'wind_gust': 0.31, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.16, 'feels_like': 9.74, 'pressure': 1018, 'humidity': 96, 'dew_point': 9.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 225, 'wind_gust': 0.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 9.92, 'feels_like': 9.92, 'pressure': 1017, 'humidity': 97, 'dew_point': 9.47, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 285, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641798000, 'temp': 9.83, 'feels_like': 9.83, 'pressure': 1017, 'humidity': 97, 'dew_point': 9.38, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 270, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.53, 'feels_like': 9.53, 'pressure': 1016, 'humidity': 97, 'dew_point': 9.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 278, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.34, 'feels_like': 9.34, 'pressure': 1016, 'humidity': 98, 'dew_point': 9.04, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 312, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 9.15, 'feels_like': 9.15, 'pressure': 1017, 'humidity': 98, 'dew_point': 8.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 265, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 281, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 8.38, 'feels_like': 8.38, 'pressure': 1018, 'humidity': 96, 'dew_point': 7.78, 'uvi': 0.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 239, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1018, 'humidity': 90, 'dew_point': 7.83, 'uvi': 1.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 284, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.38, 'feels_like': 9.61, 'pressure': 1018, 'humidity': 82, 'dew_point': 7.44, 'uvi': 2.97, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.67, 'wind_deg': 312, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641826800, 'temp': 12.38, 'feels_like': 11.74, 'pressure': 1018, 'humidity': 79, 'dew_point': 8.85, 'uvi': 5.22, 'clouds': 100, 'visibility': 8357, 'wind_speed': 1.03, 'wind_deg': 327, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1641830400, 'temp': 12.38, 'feels_like': 11.89, 'pressure': 1017, 'humidity': 85, 'dew_point': 9.93, 'uvi': 8.9, 'clouds': 100, 'visibility': 6208, 'wind_speed': 1.13, 'wind_deg': 347, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641834000, 'temp': 13.38, 'feels_like': 13.15, 'pressure': 1017, 'humidity': 91, 'dew_point': 11.94, 'uvi': 10.03, 'clouds': 100, 'visibility': 3380, 'wind_speed': 0.91, 'wind_deg': 348, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641837600, 'temp': 13.38, 'feels_like': 13.1, 'pressure': 1016, 'humidity': 89, 'dew_point': 11.61, 'uvi': 9.45, 'clouds': 94, 'visibility': 5975, 'wind_speed': 0.93, 'wind_deg': 340, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641841200, 'temp': 12.38, 'feels_like': 11.97, 'pressure': 1015, 'humidity': 88, 'dew_point': 10.45, 'uvi': 7.32, 'clouds': 100, 'visibility': 4481, 'wind_speed': 1.23, 'wind_deg': 326, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.9}}, {'dt': 1641844800, 'temp': 11.38, 'feels_like': 10.98, 'pressure': 1014, 'humidity': 92, 'dew_point': 10.13, 'uvi': 4.56, 'clouds': 100, 'visibility': 4854, 'wind_speed': 1.22, 'wind_deg': 327, 'wind_gust': 1.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.95}}, {'dt': 1641848400, 'temp': 11.38, 'feels_like': 11.03, 'pressure': 1014, 'humidity': 94, 'dew_point': 10.45, 'uvi': 2.07, 'clouds': 100, 'visibility': 7124, 'wind_speed': 1.17, 'wind_deg': 326, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641852000, 'temp': 11.38, 'feels_like': 11.08, 'pressure': 1015, 'humidity': 96, 'dew_point': 10.77, 'uvi': 0.62, 'clouds': 100, 'visibility': 1897, 'wind_speed': 1.13, 'wind_deg': 315, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641855600, 'temp': 10.38, 'feels_like': 10.03, 'pressure': 1016, 'humidity': 98, 'dew_point': 10.08, 'uvi': 0, 'clouds': 99, 'visibility': 1927, 'wind_speed': 1.13, 'wind_deg': 318, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 10.770000 | 11.080000 | 96.000000 | 1017.000000 | 0.17 | 11.380000 | 0.000000 | 10000.000000 | 321.000000 | 0.71 | 0.630000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.700000 | 10.050000 | 95.000000 | 1018.000000 | 0.12 | 10.470000 | 0.000000 | 10000.000000 | 319.000000 | 0.73 | 0.530000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 9.770000 | 9.980000 | 96.000000 | 1019.000000 | 0.13 | 10.380000 | 0.000000 | 10000.000000 | 321.000000 | 0.64 | 0.480000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.710000 | 9.910000 | 96.000000 | 1019.000000 | 0.12 | 10.320000 | 0.000000 | 10000.000000 | 282.000000 | 0.33 | 0.260000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.770000 | 9.830000 | 97.000000 | 1019.000000 |  | 10.220000 | 0.000000 | 10000.000000 | 172.000000 | 0.31 | 0.210000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 9.550000 | 9.740000 | 96.000000 | 1018.000000 |  | 10.160000 | 0.000000 | 10000.000000 | 225.000000 | 0.29 | 0.220000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 9.470000 | 9.920000 | 97.000000 | 1017.000000 | 0.12 | 9.920000 | 0.000000 | 10000.000000 | 285.000000 | 0.63 | 0.500000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 9.380000 | 9.830000 | 97.000000 | 1017.000000 |  | 9.830000 | 0.000000 | 10000.000000 | 270.000000 | 1.07 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 9.080000 | 9.530000 | 97.000000 | 1016.000000 |  | 9.530000 | 0.000000 | 10000.000000 | 278.000000 | 1.16 | 0.810000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 9.040000 | 9.340000 | 98.000000 | 1016.000000 |  | 9.340000 | 0.000000 | 10000.000000 | 312.000000 | 1.14 | 0.760000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 8.850000 | 9.150000 | 98.000000 | 1017.000000 |  | 9.150000 | 0.000000 | 10000.000000 | 265.000000 | 1 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 8.080000 | 8.380000 | 98.000000 | 1018.000000 |  | 8.380000 | 0.000000 | 10000.000000 | 281.000000 | 1.07 | 0.510000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 7.780000 | 8.380000 | 96.000000 | 1018.000000 |  | 8.380000 | 0.260000 | 10000.000000 | 239.000000 | 1.18 | 0.710000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 7.830000 | 9.380000 | 90.000000 | 1018.000000 |  | 9.380000 | 1.160000 | 10000.000000 | 284.000000 | 1 | 0.530000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 7.440000 | 9.610000 | 82.000000 | 1018.000000 | 0.15 | 10.380000 | 2.970000 | 10000.000000 | 312.000000 | 1.01 | 0.670000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 8.850000 | 11.740000 | 79.000000 | 1018.000000 | 0.42 | 12.380000 | 5.220000 | 8357.000000 | 327.000000 | 1.46 | 1.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 9.930000 | 11.890000 | 85.000000 | 1017.000000 | 0.76 | 12.380000 | 8.900000 | 6208.000000 | 347.000000 | 1.75 | 1.130000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 11.940000 | 13.150000 | 91.000000 | 1017.000000 | 0.86 | 13.380000 | 10.030000 | 3380.000000 | 348.000000 | 1.43 | 0.910000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 18:00:00 | 94.000000 | 11.610000 | 13.100000 | 89.000000 | 1016.000000 | 0.96 | 13.380000 | 9.450000 | 5975.000000 | 340.000000 | 1.45 | 0.930000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 10.450000 | 11.970000 | 88.000000 | 1015.000000 | 0.9 | 12.380000 | 7.320000 | 4481.000000 | 326.000000 | 1.92 | 1.230000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 10.130000 | 10.980000 | 92.000000 | 1014.000000 | 0.95 | 11.380000 | 4.560000 | 4854.000000 | 327.000000 | 1.88 | 1.220000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 10.450000 | 11.030000 | 94.000000 | 1014.000000 | 0.86 | 11.380000 | 2.070000 | 7124.000000 | 326.000000 | 1.94 | 1.170000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 10.770000 | 11.080000 | 96.000000 | 1015.000000 | 0.66 | 11.380000 | 0.620000 | 1897.000000 | 315.000000 | 1.87 | 1.130000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 47015100 | "EL ENCANO - AUT [47015100]" | 1.159944 | -77.161472 | 2830.000000 | Climática Principal | Automática con Telemetría | Activa | 1984-09-14 19:00:00 | NaT | Nariño | Pasto | 0 | Area Operativa 07 - Nariño-Putumayo | Amazonas | Putumayo | Alto Río Putumayo | America/Bogota | 2022-01-10 23:00:00 | 99.000000 | 10.080000 | 10.030000 | 98.000000 | 1016.000000 | 0.41 | 10.380000 | 0.000000 | 1927.000000 | 318.000000 | 1.9 | 1.130000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station47015100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station47015100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station47015100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station47015100_OWM_Windspeed_20220111.png)
