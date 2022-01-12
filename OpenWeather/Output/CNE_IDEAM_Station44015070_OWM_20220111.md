
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EL PEPINO - AUT [44015070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44015070_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.08288889,-76.66711111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.08288889&lon=-76.66711111)


| Parameter | Value |
|---|---|
| Code | 44015070 |
| Name | EL PEPINO - AUT [44015070] |
| Latitude, ° | 1.08288889 |
| Longitude, ° | -76.66711111 |
| Elevation, m | 760 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-11-11 00:00:00 |
| Suspension date | NaT |
| State | Putumayo |
| County | Mocoa |
| Stream | Guaitara |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Caquetá |
| SZH - Hydrographic subzone | Alto Caqueta |

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

### (CNE index 4) Open Weather values for station 44015070 - EL PEPINO - AUT [44015070]

JSON data from API OWM:

```
{'lat': 1.0829, 'lon': -76.6671, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813130, 'sunset': 1641856550, 'temp': 25.56, 'feels_like': 26.29, 'pressure': 1011, 'humidity': 81, 'dew_point': 22.06, 'uvi': 4.1, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 132, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, 'hourly': [{'dt': 1641772800, 'temp': 22.09, 'feels_like': 22.7, 'pressure': 1012, 'humidity': 90, 'dew_point': 20.37, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.8, 'wind_deg': 314, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.4}}, {'dt': 1641776400, 'temp': 21.74, 'feels_like': 22.35, 'pressure': 1013, 'humidity': 91, 'dew_point': 20.21, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2, 'wind_deg': 313, 'wind_gust': 2.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641780000, 'temp': 22.03, 'feels_like': 22.64, 'pressure': 1014, 'humidity': 90, 'dew_point': 20.31, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 316, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641783600, 'temp': 21.71, 'feels_like': 22.36, 'pressure': 1015, 'humidity': 93, 'dew_point': 20.53, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 310, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641787200, 'temp': 21.44, 'feels_like': 22.12, 'pressure': 1015, 'humidity': 95, 'dew_point': 20.61, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 301, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.81}}, {'dt': 1641790800, 'temp': 21.22, 'feels_like': 21.9, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.56, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.37, 'wind_deg': 297, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.81}}, {'dt': 1641794400, 'temp': 21.13, 'feels_like': 21.81, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.47, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 285, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.6}}, {'dt': 1641798000, 'temp': 20.89, 'feels_like': 21.57, 'pressure': 1013, 'humidity': 97, 'dew_point': 20.4, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 288, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.79}}, {'dt': 1641801600, 'temp': 20.52, 'feels_like': 21.16, 'pressure': 1013, 'humidity': 97, 'dew_point': 20.03, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 295, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.88}}, {'dt': 1641805200, 'temp': 20.28, 'feels_like': 20.9, 'pressure': 1013, 'humidity': 97, 'dew_point': 19.79, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 304, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.45}}, {'dt': 1641808800, 'temp': 20.06, 'feels_like': 20.63, 'pressure': 1014, 'humidity': 96, 'dew_point': 19.4, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.82, 'wind_deg': 301, 'wind_gust': 1.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641812400, 'temp': 20.23, 'feels_like': 20.79, 'pressure': 1014, 'humidity': 95, 'dew_point': 19.4, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 301, 'wind_gust': 1.36, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641816000, 'temp': 20.83, 'feels_like': 21.42, 'pressure': 1015, 'humidity': 94, 'dew_point': 19.83, 'uvi': 0.27, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 299, 'wind_gust': 1.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 22.92, 'feels_like': 23.57, 'pressure': 1015, 'humidity': 88, 'dew_point': 20.83, 'uvi': 1.04, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 15, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 24.24, 'feels_like': 24.89, 'pressure': 1016, 'humidity': 83, 'dew_point': 21.17, 'uvi': 2.61, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 144, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641826800, 'temp': 24.29, 'feels_like': 25.07, 'pressure': 1016, 'humidity': 88, 'dew_point': 22.17, 'uvi': 4.56, 'clouds': 89, 'visibility': 7368, 'wind_speed': 1.41, 'wind_deg': 156, 'wind_gust': 1.8, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.28}}, {'dt': 1641830400, 'temp': 24.81, 'feels_like': 25.59, 'pressure': 1015, 'humidity': 86, 'dew_point': 22.31, 'uvi': 8.31, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 154, 'wind_gust': 1.47, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641834000, 'temp': 25.25, 'feels_like': 26, 'pressure': 1014, 'humidity': 83, 'dew_point': 22.16, 'uvi': 9.31, 'clouds': 89, 'visibility': 8811, 'wind_speed': 1.47, 'wind_deg': 154, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641837600, 'temp': 25.19, 'feels_like': 25.93, 'pressure': 1013, 'humidity': 83, 'dew_point': 22.1, 'uvi': 8.72, 'clouds': 83, 'visibility': 8759, 'wind_speed': 1.06, 'wind_deg': 154, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641841200, 'temp': 25.87, 'feels_like': 26.6, 'pressure': 1012, 'humidity': 80, 'dew_point': 22.16, 'uvi': 6.65, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.91, 'wind_deg': 139, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}, {'dt': 1641844800, 'temp': 25.56, 'feels_like': 26.29, 'pressure': 1011, 'humidity': 81, 'dew_point': 22.06, 'uvi': 4.1, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 132, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, {'dt': 1641848400, 'temp': 24.53, 'feels_like': 25.31, 'pressure': 1011, 'humidity': 87, 'dew_point': 22.22, 'uvi': 1.84, 'clouds': 88, 'visibility': 6735, 'wind_speed': 0.77, 'wind_deg': 130, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641852000, 'temp': 23.65, 'feels_like': 24.47, 'pressure': 1011, 'humidity': 92, 'dew_point': 22.27, 'uvi': 0.42, 'clouds': 88, 'visibility': 7625, 'wind_speed': 0.11, 'wind_deg': 8, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641855600, 'temp': 22.18, 'feels_like': 22.96, 'pressure': 1012, 'humidity': 96, 'dew_point': 21.51, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 312, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 20.370000 | 22.700000 | 90.000000 | 1012.000000 | 0.4 | 22.090000 | 0.000000 | 10000.000000 | 314.000000 | 1.37 | 1.800000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 20.210000 | 22.350000 | 91.000000 | 1013.000000 | 0.22 | 21.740000 | 0.000000 | 10000.000000 | 313.000000 | 2.23 | 2.000000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 20.310000 | 22.640000 | 90.000000 | 1014.000000 | 0.16 | 22.030000 | 0.000000 | 10000.000000 | 316.000000 | 1.51 | 1.820000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 20.530000 | 22.360000 | 93.000000 | 1015.000000 | 0.43 | 21.710000 | 0.000000 | 10000.000000 | 310.000000 | 1.36 | 1.650000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 20.610000 | 22.120000 | 95.000000 | 1015.000000 | 0.81 | 21.440000 | 0.000000 | 10000.000000 | 301.000000 | 1.3 | 1.540000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 20.560000 | 21.900000 | 96.000000 | 1014.000000 | 0.81 | 21.220000 | 0.000000 | 10000.000000 | 297.000000 | 1.18 | 1.370000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 06:00:00 | 86.000000 | 20.470000 | 21.810000 | 96.000000 | 1014.000000 | 0.6 | 21.130000 | 0.000000 | 10000.000000 | 285.000000 | 1 | 1.120000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 07:00:00 | 98.000000 | 20.400000 | 21.570000 | 97.000000 | 1013.000000 | 0.79 | 20.890000 | 0.000000 | 10000.000000 | 288.000000 | 1.13 | 1.310000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 20.030000 | 21.160000 | 97.000000 | 1013.000000 | 0.88 | 20.520000 | 0.000000 | 10000.000000 | 295.000000 | 1.43 | 1.520000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 19.790000 | 20.900000 | 97.000000 | 1013.000000 | 0.45 | 20.280000 | 0.000000 | 10000.000000 | 304.000000 | 1.32 | 1.620000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 19.400000 | 20.630000 | 96.000000 | 1014.000000 | 0.21 | 20.060000 | 0.000000 | 10000.000000 | 301.000000 | 1.87 | 1.820000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 19.400000 | 20.790000 | 95.000000 | 1014.000000 | 0.17 | 20.230000 | 0.000000 | 10000.000000 | 301.000000 | 1.36 | 1.660000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 19.830000 | 21.420000 | 94.000000 | 1015.000000 |  | 20.830000 | 0.270000 | 10000.000000 | 299.000000 | 1.54 | 1.440000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 20.830000 | 23.570000 | 88.000000 | 1015.000000 |  | 22.920000 | 1.040000 | 10000.000000 | 15.000000 | 0.63 | 0.140000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 21.170000 | 24.890000 | 83.000000 | 1016.000000 | 0.44 | 24.240000 | 2.610000 | 10000.000000 | 144.000000 | 1.15 | 1.000000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 15:00:00 | 89.000000 | 22.170000 | 25.070000 | 88.000000 | 1016.000000 | 1.28 | 24.290000 | 4.560000 | 7368.000000 | 156.000000 | 1.8 | 1.410000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 16:00:00 | 86.000000 | 22.310000 | 25.590000 | 86.000000 | 1015.000000 | 1.03 | 24.810000 | 8.310000 | 10000.000000 | 154.000000 | 1.47 | 1.420000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 17:00:00 | 89.000000 | 22.160000 | 26.000000 | 83.000000 | 1014.000000 | 0.91 | 25.250000 | 9.310000 | 8811.000000 | 154.000000 | 1.38 | 1.470000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 22.100000 | 25.930000 | 83.000000 | 1013.000000 | 0.94 | 25.190000 | 8.720000 | 8759.000000 | 154.000000 | 1.1 | 1.060000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 19:00:00 | 98.000000 | 22.160000 | 26.600000 | 80.000000 | 1012.000000 | 0.75 | 25.870000 | 6.650000 | 10000.000000 | 139.000000 | 0.93 | 0.910000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 20:00:00 | 89.000000 | 22.060000 | 26.290000 | 81.000000 | 1011.000000 | 0.71 | 25.560000 | 4.100000 | 10000.000000 | 132.000000 | 0.92 | 0.940000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 21:00:00 | 88.000000 | 22.220000 | 25.310000 | 87.000000 | 1011.000000 | 0.68 | 24.530000 | 1.840000 | 6735.000000 | 130.000000 | 1.18 | 0.770000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 22:00:00 | 88.000000 | 22.270000 | 24.470000 | 92.000000 | 1011.000000 | 0.67 | 23.650000 | 0.420000 | 7625.000000 | 8.000000 | 0.75 | 0.110000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015070 | "EL PEPINO - AUT [44015070]" | 1.082889 | -76.667111 | 760.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-11-11 00:00:00 | NaT | Putumayo | Mocoa | Guaitara | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 21.510000 | 22.960000 | 96.000000 | 1012.000000 | 0.67 | 22.180000 | 0.000000 | 10000.000000 | 312.000000 | 0.8 | 0.990000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station44015070_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44015070_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44015070_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015070_OWM_Windspeed_20220111.png)
