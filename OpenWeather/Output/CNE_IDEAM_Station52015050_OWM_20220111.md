
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BALBOA - AUT [52015050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station52015050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.03277778,-77.22166667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.03277778&lon=-77.22166667)


| Parameter | Value |
|---|---|
| Code | 52015050 |
| Name | BALBOA - AUT [52015050] |
| Latitude, ° | 2.03277778 |
| Longitude, ° | -77.22166667 |
| Elevation, m | 1700 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-09-27 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Balboa (Cauca) |
| Stream | Suaza |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Patía |
| SZH - Hydrographic subzone | Río Patia Alto |

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

### (CNE index 27) Open Weather values for station 52015050 - BALBOA - AUT [52015050]

JSON data from API OWM:

```
{'lat': 2.0328, 'lon': -77.2217, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813355, 'sunset': 1641856591, 'temp': 20.13, 'feels_like': 20.44, 'pressure': 1012, 'humidity': 86, 'dew_point': 17.72, 'uvi': 3.14, 'clouds': 89, 'visibility': 4253, 'wind_speed': 1.7, 'wind_deg': 252, 'wind_gust': 2.31, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.31}}, 'hourly': [{'dt': 1641772800, 'temp': 16.64, 'feels_like': 16.89, 'pressure': 1014, 'humidity': 97, 'dew_point': 16.16, 'uvi': 0, 'clouds': 100, 'visibility': 3114, 'wind_speed': 1.6, 'wind_deg': 285, 'wind_gust': 2.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.95}}, {'dt': 1641776400, 'temp': 16.47, 'feels_like': 16.68, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 292, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641780000, 'temp': 16.64, 'feels_like': 16.84, 'pressure': 1016, 'humidity': 95, 'dew_point': 15.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 293, 'wind_gust': 1.09, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641783600, 'temp': 16.52, 'feels_like': 16.73, 'pressure': 1016, 'humidity': 96, 'dew_point': 15.88, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 294, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641787200, 'temp': 16.41, 'feels_like': 16.61, 'pressure': 1016, 'humidity': 96, 'dew_point': 15.77, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 269, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 16.29, 'feels_like': 16.51, 'pressure': 1016, 'humidity': 97, 'dew_point': 15.81, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 278, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641794400, 'temp': 16.61, 'feels_like': 16.86, 'pressure': 1015, 'humidity': 97, 'dew_point': 16.13, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 277, 'wind_gust': 0.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641798000, 'temp': 16.42, 'feels_like': 16.68, 'pressure': 1014, 'humidity': 98, 'dew_point': 16.1, 'uvi': 0, 'clouds': 100, 'visibility': 7263, 'wind_speed': 0.51, 'wind_deg': 303, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.87}}, {'dt': 1641801600, 'temp': 16.22, 'feels_like': 16.46, 'pressure': 1014, 'humidity': 98, 'dew_point': 15.9, 'uvi': 0, 'clouds': 100, 'visibility': 9935, 'wind_speed': 0.52, 'wind_deg': 276, 'wind_gust': 0.73, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.17}}, {'dt': 1641805200, 'temp': 16.23, 'feels_like': 16.47, 'pressure': 1014, 'humidity': 98, 'dew_point': 15.91, 'uvi': 0, 'clouds': 100, 'visibility': 7537, 'wind_speed': 0.5, 'wind_deg': 261, 'wind_gust': 0.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.05}}, {'dt': 1641808800, 'temp': 16.29, 'feels_like': 16.53, 'pressure': 1014, 'humidity': 98, 'dew_point': 15.97, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 255, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.91}}, {'dt': 1641812400, 'temp': 16.24, 'feels_like': 16.5, 'pressure': 1015, 'humidity': 99, 'dew_point': 16.08, 'uvi': 0, 'clouds': 100, 'visibility': 7893, 'wind_speed': 0.59, 'wind_deg': 238, 'wind_gust': 0.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.47}}, {'dt': 1641816000, 'temp': 16.43, 'feels_like': 16.69, 'pressure': 1016, 'humidity': 98, 'dew_point': 16.11, 'uvi': 0.36, 'clouds': 96, 'visibility': 7635, 'wind_speed': 0.49, 'wind_deg': 274, 'wind_gust': 0.79, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.26}}, {'dt': 1641819600, 'temp': 16.76, 'feels_like': 17.05, 'pressure': 1016, 'humidity': 98, 'dew_point': 16.44, 'uvi': 1.56, 'clouds': 100, 'visibility': 6326, 'wind_speed': 0.62, 'wind_deg': 256, 'wind_gust': 1.09, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.95}}, {'dt': 1641823200, 'temp': 17.22, 'feels_like': 17.5, 'pressure': 1017, 'humidity': 96, 'dew_point': 16.58, 'uvi': 4, 'clouds': 100, 'visibility': 4201, 'wind_speed': 0.99, 'wind_deg': 242, 'wind_gust': 1.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 3.46}}, {'dt': 1641826800, 'temp': 17.51, 'feels_like': 17.82, 'pressure': 1017, 'humidity': 96, 'dew_point': 16.87, 'uvi': 7.08, 'clouds': 100, 'visibility': 5317, 'wind_speed': 0.79, 'wind_deg': 233, 'wind_gust': 1.32, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.66}}, {'dt': 1641830400, 'temp': 19.2, 'feels_like': 19.53, 'pressure': 1016, 'humidity': 90, 'dew_point': 17.52, 'uvi': 9.19, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 215, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}, {'dt': 1641834000, 'temp': 20.15, 'feels_like': 20.47, 'pressure': 1015, 'humidity': 86, 'dew_point': 17.74, 'uvi': 10.36, 'clouds': 96, 'visibility': 8950, 'wind_speed': 1.54, 'wind_deg': 233, 'wind_gust': 2.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.93}}, {'dt': 1641837600, 'temp': 20.67, 'feels_like': 20.96, 'pressure': 1014, 'humidity': 83, 'dew_point': 17.68, 'uvi': 9.76, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 248, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641841200, 'temp': 20.5, 'feels_like': 20.82, 'pressure': 1013, 'humidity': 85, 'dew_point': 17.89, 'uvi': 5.06, 'clouds': 100, 'visibility': 6583, 'wind_speed': 1.5, 'wind_deg': 249, 'wind_gust': 2.06, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.2}}, {'dt': 1641844800, 'temp': 20.13, 'feels_like': 20.44, 'pressure': 1012, 'humidity': 86, 'dew_point': 17.72, 'uvi': 3.14, 'clouds': 89, 'visibility': 4253, 'wind_speed': 1.7, 'wind_deg': 252, 'wind_gust': 2.31, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.31}}, {'dt': 1641848400, 'temp': 19.78, 'feels_like': 20.06, 'pressure': 1012, 'humidity': 86, 'dew_point': 17.37, 'uvi': 1.42, 'clouds': 78, 'visibility': 5237, 'wind_speed': 1.7, 'wind_deg': 254, 'wind_gust': 2.4, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641852000, 'temp': 19.08, 'feels_like': 19.37, 'pressure': 1012, 'humidity': 89, 'dew_point': 17.23, 'uvi': 0.17, 'clouds': 76, 'visibility': 8283, 'wind_speed': 1.41, 'wind_deg': 258, 'wind_gust': 2.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.91}}, {'dt': 1641855600, 'temp': 17.49, 'feels_like': 17.75, 'pressure': 1013, 'humidity': 94, 'dew_point': 16.51, 'uvi': 0, 'clouds': 76, 'visibility': 7027, 'wind_speed': 1.44, 'wind_deg': 260, 'wind_gust': 2.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.84}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 16.160000 | 16.890000 | 97.000000 | 1014.000000 | 0.95 | 16.640000 | 0.000000 | 3114.000000 | 285.000000 | 2.26 | 1.600000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 15.830000 | 16.680000 | 96.000000 | 1015.000000 | 0.42 | 16.470000 | 0.000000 | 10000.000000 | 292.000000 | 1.61 | 1.250000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 15.840000 | 16.840000 | 95.000000 | 1016.000000 | 0.16 | 16.640000 | 0.000000 | 10000.000000 | 293.000000 | 1.09 | 0.850000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 15.880000 | 16.730000 | 96.000000 | 1016.000000 | 0.23 | 16.520000 | 0.000000 | 10000.000000 | 294.000000 | 0.87 | 0.680000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 15.770000 | 16.610000 | 96.000000 | 1016.000000 |  | 16.410000 | 0.000000 | 10000.000000 | 269.000000 | 0.66 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 15.810000 | 16.510000 | 97.000000 | 1016.000000 | 0.17 | 16.290000 | 0.000000 | 10000.000000 | 278.000000 | 0.71 | 0.540000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 16.130000 | 16.860000 | 97.000000 | 1015.000000 | 0.42 | 16.610000 | 0.000000 | 10000.000000 | 277.000000 | 0.61 | 0.490000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 16.100000 | 16.680000 | 98.000000 | 1014.000000 | 0.87 | 16.420000 | 0.000000 | 7263.000000 | 303.000000 | 0.76 | 0.510000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 15.900000 | 16.460000 | 98.000000 | 1014.000000 | 1.17 | 16.220000 | 0.000000 | 9935.000000 | 276.000000 | 0.73 | 0.520000 | 501 | Rain | moderate rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 15.910000 | 16.470000 | 98.000000 | 1014.000000 | 1.05 | 16.230000 | 0.000000 | 7537.000000 | 261.000000 | 0.75 | 0.500000 | 501 | Rain | moderate rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 15.970000 | 16.530000 | 98.000000 | 1014.000000 | 0.91 | 16.290000 | 0.000000 | 10000.000000 | 255.000000 | 0.63 | 0.380000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 16.080000 | 16.500000 | 99.000000 | 1015.000000 | 1.47 | 16.240000 | 0.000000 | 7893.000000 | 238.000000 | 0.86 | 0.590000 | 501 | Rain | moderate rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 16.110000 | 16.690000 | 98.000000 | 1016.000000 | 2.26 | 16.430000 | 0.360000 | 7635.000000 | 274.000000 | 0.79 | 0.490000 | 501 | Rain | moderate rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 16.440000 | 17.050000 | 98.000000 | 1016.000000 | 2.95 | 16.760000 | 1.560000 | 6326.000000 | 256.000000 | 1.09 | 0.620000 | 501 | Rain | moderate rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 16.580000 | 17.500000 | 96.000000 | 1017.000000 | 3.46 | 17.220000 | 4.000000 | 4201.000000 | 242.000000 | 1.48 | 0.990000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 16.870000 | 17.820000 | 96.000000 | 1017.000000 | 1.66 | 17.510000 | 7.080000 | 5317.000000 | 233.000000 | 1.32 | 0.790000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 17.520000 | 19.530000 | 90.000000 | 1016.000000 | 0.75 | 19.200000 | 9.190000 | 10000.000000 | 215.000000 | 1.82 | 1.340000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 17:00:00 | 96.000000 | 17.740000 | 20.470000 | 86.000000 | 1015.000000 | 0.93 | 20.150000 | 10.360000 | 8950.000000 | 233.000000 | 2.1 | 1.540000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 17.680000 | 20.960000 | 83.000000 | 1014.000000 | 0.92 | 20.670000 | 9.760000 | 10000.000000 | 248.000000 | 1.83 | 1.300000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 17.890000 | 20.820000 | 85.000000 | 1013.000000 | 1.2 | 20.500000 | 5.060000 | 6583.000000 | 249.000000 | 2.06 | 1.500000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 20:00:00 | 89.000000 | 17.720000 | 20.440000 | 86.000000 | 1012.000000 | 1.31 | 20.130000 | 3.140000 | 4253.000000 | 252.000000 | 2.31 | 1.700000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 21:00:00 | 78.000000 | 17.370000 | 20.060000 | 86.000000 | 1012.000000 | 0.94 | 19.780000 | 1.420000 | 5237.000000 | 254.000000 | 2.4 | 1.700000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 22:00:00 | 76.000000 | 17.230000 | 19.370000 | 89.000000 | 1012.000000 | 0.91 | 19.080000 | 0.170000 | 8283.000000 | 258.000000 | 2.3 | 1.410000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 52015050 | "BALBOA - AUT [52015050]" | 2.032778 | -77.221667 | 1700.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-09-27 00:00:00 | NaT | Cauca | Balboa (Cauca) | Suaza | Area Operativa 07 - Nariño-Putumayo | Pacifico | Patía | Río Patia Alto | America/Bogota | 2022-01-10 23:00:00 | 76.000000 | 16.510000 | 17.750000 | 94.000000 | 1013.000000 | 0.84 | 17.490000 | 0.000000 | 7027.000000 | 260.000000 | 2.13 | 1.440000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station52015050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station52015050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station52015050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station52015050_OWM_Windspeed_20220111.png)
