
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA SIERRA - AUT [52025090] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52025090_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.19383333,-76.75033333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.19383333&lon=-76.75033333)


| Parameter | Value |
|---|---|
| Code | 52025090 |
| Name | LA SIERRA - AUT [52025090] |
| Latitude, ° | 2.19383333 |
| Longitude, ° | -76.75033333 |
| Elevation, m | 1870 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-09-23 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | La Sierra |
| Stream | Suaza |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Guachicono |

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

### (CNE index 28) Open Weather values for station 52025090 - LA SIERRA - AUT [52025090]

JSON data from API OWM:

```
{'lat': 2.1938, 'lon': -76.7503, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813257, 'sunset': 1641856463, 'temp': 17.75, 'feels_like': 17.93, 'pressure': 1013, 'humidity': 90, 'dew_point': 16.09, 'uvi': 2.35, 'clouds': 100, 'visibility': 2854, 'wind_speed': 1.58, 'wind_deg': 263, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.5}}, 'hourly': [{'dt': 1641772800, 'temp': 14.71, 'feels_like': 14.77, 'pressure': 1015, 'humidity': 97, 'dew_point': 14.24, 'uvi': 0, 'clouds': 100, 'visibility': 6029, 'wind_speed': 0.5, 'wind_deg': 141, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.85}}, {'dt': 1641776400, 'temp': 14.47, 'feels_like': 14.48, 'pressure': 1017, 'humidity': 96, 'dew_point': 13.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 97, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.49}}, {'dt': 1641780000, 'temp': 14.27, 'feels_like': 14.26, 'pressure': 1018, 'humidity': 96, 'dew_point': 13.64, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 92, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641783600, 'temp': 14.22, 'feels_like': 14.23, 'pressure': 1018, 'humidity': 97, 'dew_point': 13.75, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 108, 'wind_gust': 0.79, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 14.21, 'feels_like': 14.22, 'pressure': 1018, 'humidity': 97, 'dew_point': 13.74, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 107, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641790800, 'temp': 14.26, 'feels_like': 14.25, 'pressure': 1017, 'humidity': 96, 'dew_point': 13.63, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 98, 'wind_gust': 0.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.96, 'feels_like': 13.94, 'pressure': 1016, 'humidity': 97, 'dew_point': 13.49, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 66, 'wind_gust': 0.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 13.92, 'feels_like': 13.9, 'pressure': 1016, 'humidity': 97, 'dew_point': 13.45, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 56, 'wind_gust': 0.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14.29, 'feels_like': 14.31, 'pressure': 1015, 'humidity': 97, 'dew_point': 13.82, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 54, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 14.22, 'feels_like': 14.23, 'pressure': 1015, 'humidity': 97, 'dew_point': 13.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 352, 'wind_gust': 0.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641808800, 'temp': 14.06, 'feels_like': 14.08, 'pressure': 1016, 'humidity': 98, 'dew_point': 13.75, 'uvi': 0, 'clouds': 100, 'visibility': 580, 'wind_speed': 0.28, 'wind_deg': 24, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641812400, 'temp': 13.82, 'feels_like': 13.82, 'pressure': 1017, 'humidity': 98, 'dew_point': 13.51, 'uvi': 0, 'clouds': 100, 'visibility': 343, 'wind_speed': 0.16, 'wind_deg': 286, 'wind_gust': 0.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 14.71, 'feels_like': 14.74, 'pressure': 1017, 'humidity': 96, 'dew_point': 14.08, 'uvi': 0.28, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 47, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641819600, 'temp': 15.75, 'feels_like': 15.81, 'pressure': 1018, 'humidity': 93, 'dew_point': 14.62, 'uvi': 1.24, 'clouds': 100, 'visibility': 9185, 'wind_speed': 0.54, 'wind_deg': 307, 'wind_gust': 0.38, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 16.99, 'feels_like': 17.04, 'pressure': 1018, 'humidity': 88, 'dew_point': 14.99, 'uvi': 3.16, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 303, 'wind_gust': 0.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641826800, 'temp': 17.5, 'feels_like': 17.6, 'pressure': 1018, 'humidity': 88, 'dew_point': 15.49, 'uvi': 5.53, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 275, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641830400, 'temp': 17.93, 'feels_like': 18.1, 'pressure': 1017, 'humidity': 89, 'dew_point': 16.09, 'uvi': 9.04, 'clouds': 100, 'visibility': 4340, 'wind_speed': 1.9, 'wind_deg': 269, 'wind_gust': 1.43, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.09}}, {'dt': 1641834000, 'temp': 18.22, 'feels_like': 18.42, 'pressure': 1016, 'humidity': 89, 'dew_point': 16.38, 'uvi': 10.14, 'clouds': 100, 'visibility': 5426, 'wind_speed': 1.86, 'wind_deg': 269, 'wind_gust': 1.56, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641837600, 'temp': 18.03, 'feels_like': 18.24, 'pressure': 1015, 'humidity': 90, 'dew_point': 16.37, 'uvi': 9.48, 'clouds': 99, 'visibility': 6129, 'wind_speed': 1.77, 'wind_deg': 263, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, {'dt': 1641841200, 'temp': 17.87, 'feels_like': 18.04, 'pressure': 1014, 'humidity': 89, 'dew_point': 16.03, 'uvi': 3.83, 'clouds': 100, 'visibility': 5790, 'wind_speed': 1.57, 'wind_deg': 268, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, {'dt': 1641844800, 'temp': 17.75, 'feels_like': 17.93, 'pressure': 1013, 'humidity': 90, 'dew_point': 16.09, 'uvi': 2.35, 'clouds': 100, 'visibility': 2854, 'wind_speed': 1.58, 'wind_deg': 263, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.5}}, {'dt': 1641848400, 'temp': 17.27, 'feels_like': 17.43, 'pressure': 1013, 'humidity': 91, 'dew_point': 15.79, 'uvi': 1.05, 'clouds': 90, 'visibility': 2512, 'wind_speed': 1.47, 'wind_deg': 257, 'wind_gust': 1.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1641852000, 'temp': 16.69, 'feels_like': 16.84, 'pressure': 1014, 'humidity': 93, 'dew_point': 15.55, 'uvi': 0.24, 'clouds': 82, 'visibility': 2743, 'wind_speed': 1.3, 'wind_deg': 260, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.59}}, {'dt': 1641855600, 'temp': 15.32, 'feels_like': 15.44, 'pressure': 1015, 'humidity': 97, 'dew_point': 14.85, 'uvi': 0, 'clouds': 80, 'visibility': 739, 'wind_speed': 0.95, 'wind_deg': 246, 'wind_gust': 1.22, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 14.240000 | 14.770000 | 97.000000 | 1015.000000 | 0.85 | 14.710000 | 0.000000 | 6029.000000 | 141.000000 | 0.65 | 0.500000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 13.840000 | 14.480000 | 96.000000 | 1017.000000 | 0.49 | 14.470000 | 0.000000 | 10000.000000 | 97.000000 | 0.79 | 0.420000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 13.640000 | 14.260000 | 96.000000 | 1018.000000 | 0.2 | 14.270000 | 0.000000 | 10000.000000 | 92.000000 | 0.75 | 0.470000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 03:00:00 | 86.000000 | 13.750000 | 14.230000 | 97.000000 | 1018.000000 |  | 14.220000 | 0.000000 | 10000.000000 | 108.000000 | 0.79 | 0.500000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 04:00:00 | 89.000000 | 13.740000 | 14.220000 | 97.000000 | 1018.000000 | 0.12 | 14.210000 | 0.000000 | 10000.000000 | 107.000000 | 0.86 | 0.700000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 05:00:00 | 91.000000 | 13.630000 | 14.250000 | 96.000000 | 1017.000000 |  | 14.260000 | 0.000000 | 10000.000000 | 98.000000 | 0.55 | 0.450000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 06:00:00 | 98.000000 | 13.490000 | 13.940000 | 97.000000 | 1016.000000 |  | 13.960000 | 0.000000 | 10000.000000 | 66.000000 | 0.33 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 13.450000 | 13.900000 | 97.000000 | 1016.000000 |  | 13.920000 | 0.000000 | 10000.000000 | 56.000000 | 0.48 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 08:00:00 | 99.000000 | 13.820000 | 14.310000 | 97.000000 | 1015.000000 | 0.13 | 14.290000 | 0.000000 | 10000.000000 | 54.000000 | 0.54 | 0.340000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 13.750000 | 14.230000 | 97.000000 | 1015.000000 | 0.22 | 14.220000 | 0.000000 | 10000.000000 | 352.000000 | 0.47 | 0.360000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 13.750000 | 14.080000 | 98.000000 | 1016.000000 | 0.19 | 14.060000 | 0.000000 | 580.000000 | 24.000000 | 0.45 | 0.280000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 13.510000 | 13.820000 | 98.000000 | 1017.000000 | 0.12 | 13.820000 | 0.000000 | 343.000000 | 286.000000 | 0.4 | 0.160000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 14.080000 | 14.740000 | 96.000000 | 1017.000000 | 0.15 | 14.710000 | 0.280000 | 10000.000000 | 47.000000 | 0.57 | 0.330000 | 500 | Rain | light rain | 10d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 14.620000 | 15.810000 | 93.000000 | 1018.000000 |  | 15.750000 | 1.240000 | 9185.000000 | 307.000000 | 0.38 | 0.540000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 14.990000 | 17.040000 | 88.000000 | 1018.000000 | 0.5 | 16.990000 | 3.160000 | 10000.000000 | 303.000000 | 0.48 | 0.810000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 15.490000 | 17.600000 | 88.000000 | 1018.000000 | 0.72 | 17.500000 | 5.530000 | 10000.000000 | 275.000000 | 0.94 | 1.390000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 16.090000 | 18.100000 | 89.000000 | 1017.000000 | 1.09 | 17.930000 | 9.040000 | 4340.000000 | 269.000000 | 1.43 | 1.900000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 16.380000 | 18.420000 | 89.000000 | 1016.000000 | 1.35 | 18.220000 | 10.140000 | 5426.000000 | 269.000000 | 1.56 | 1.860000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 18:00:00 | 99.000000 | 16.370000 | 18.240000 | 90.000000 | 1015.000000 | 1.37 | 18.030000 | 9.480000 | 6129.000000 | 263.000000 | 1.66 | 1.770000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 16.030000 | 18.040000 | 89.000000 | 1014.000000 | 1.37 | 17.870000 | 3.830000 | 5790.000000 | 268.000000 | 1.39 | 1.570000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 16.090000 | 17.930000 | 90.000000 | 1013.000000 | 1.5 | 17.750000 | 2.350000 | 2854.000000 | 263.000000 | 1.64 | 1.580000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 15.790000 | 17.430000 | 91.000000 | 1013.000000 | 1.78 | 17.270000 | 1.050000 | 2512.000000 | 257.000000 | 1.66 | 1.470000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 22:00:00 | 82.000000 | 15.550000 | 16.840000 | 93.000000 | 1014.000000 | 1.59 | 16.690000 | 0.240000 | 2743.000000 | 260.000000 | 1.6 | 1.300000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52025090 | "LA SIERRA - AUT [52025090]" | 2.193833 | -76.750333 | 1870.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-23 00:00:00 | NaT | Cauca | La Sierra | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Guachicono | America/Bogota | 2022-01-10 23:00:00 | 80.000000 | 14.850000 | 15.440000 | 97.000000 | 1015.000000 | 1.16 | 15.320000 | 0.000000 | 739.000000 | 246.000000 | 1.22 | 0.950000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52025090_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52025090_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52025090_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52025090_OWM_Windspeed_20220111.png)
