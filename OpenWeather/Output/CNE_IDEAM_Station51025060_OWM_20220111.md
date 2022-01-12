
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BIOTOPO - AUT [51025060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station51025060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.40863889,-78.28161111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.40863889&lon=-78.28161111)


| Parameter | Value |
|---|---|
| Code | 51025060 |
| Name | BIOTOPO - AUT [51025060] |
| Latitude, ° | 1.40863889 |
| Longitude, ° | -78.28161111 |
| Elevation, m | 512 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-12-12 00:00:00 |
| Suspension date | NaT |
| State | Nariño |
| County | Barbacoas |
| Stream | Guarapas |
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

### (CNE index 13) Open Weather values for station 51025060 - BIOTOPO - AUT [51025060]

JSON data from API OWM:

```
{'lat': 1.4086, 'lon': -78.2816, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813549, 'sunset': 1641856906, 'temp': 22.94, 'feels_like': 23.59, 'pressure': 1012, 'humidity': 88, 'dew_point': 20.85, 'uvi': 4.68, 'clouds': 92, 'visibility': 4838, 'wind_speed': 2.08, 'wind_deg': 297, 'wind_gust': 2.97, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.67}}, 'hourly': [{'dt': 1641772800, 'temp': 20.93, 'feels_like': 21.56, 'pressure': 1012, 'humidity': 95, 'dew_point': 20.1, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 229, 'wind_gust': 1.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.76}}, {'dt': 1641776400, 'temp': 20.8, 'feels_like': 21.44, 'pressure': 1013, 'humidity': 96, 'dew_point': 20.14, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 219, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641780000, 'temp': 20.67, 'feels_like': 21.3, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.01, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 211, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641783600, 'temp': 20.58, 'feels_like': 21.23, 'pressure': 1015, 'humidity': 97, 'dew_point': 20.09, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 206, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641787200, 'temp': 20.42, 'feels_like': 21.05, 'pressure': 1014, 'humidity': 97, 'dew_point': 19.93, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 197, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 20.32, 'feels_like': 20.94, 'pressure': 1014, 'humidity': 97, 'dew_point': 19.83, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 207, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.2, 'feels_like': 20.83, 'pressure': 1013, 'humidity': 98, 'dew_point': 19.87, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 209, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641798000, 'temp': 20.08, 'feels_like': 20.7, 'pressure': 1013, 'humidity': 98, 'dew_point': 19.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 189, 'wind_gust': 1.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 19.99, 'feels_like': 20.58, 'pressure': 1012, 'humidity': 97, 'dew_point': 19.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 183, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641805200, 'temp': 19.95, 'feels_like': 20.53, 'pressure': 1012, 'humidity': 97, 'dew_point': 19.46, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 189, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641808800, 'temp': 20.16, 'feels_like': 20.74, 'pressure': 1013, 'humidity': 96, 'dew_point': 19.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 165, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.16, 'feels_like': 20.71, 'pressure': 1013, 'humidity': 95, 'dew_point': 19.33, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 173, 'wind_gust': 0.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641816000, 'temp': 20.54, 'feels_like': 21.1, 'pressure': 1014, 'humidity': 94, 'dew_point': 19.54, 'uvi': 0.32, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 228, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641819600, 'temp': 21.95, 'feels_like': 22.52, 'pressure': 1015, 'humidity': 89, 'dew_point': 20.05, 'uvi': 1.7, 'clouds': 98, 'visibility': 9728, 'wind_speed': 0.66, 'wind_deg': 223, 'wind_gust': 1.29, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641823200, 'temp': 23.31, 'feels_like': 23.89, 'pressure': 1015, 'humidity': 84, 'dew_point': 20.45, 'uvi': 4.46, 'clouds': 99, 'visibility': 6718, 'wind_speed': 1.24, 'wind_deg': 263, 'wind_gust': 2.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.35}}, {'dt': 1641826800, 'temp': 24.1, 'feels_like': 24.68, 'pressure': 1015, 'humidity': 81, 'dew_point': 20.64, 'uvi': 7.99, 'clouds': 85, 'visibility': 8247, 'wind_speed': 1.77, 'wind_deg': 278, 'wind_gust': 2.61, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.48}}, {'dt': 1641830400, 'temp': 24.56, 'feels_like': 25.16, 'pressure': 1015, 'humidity': 80, 'dew_point': 20.88, 'uvi': 10.67, 'clouds': 85, 'visibility': 6867, 'wind_speed': 1.82, 'wind_deg': 295, 'wind_gust': 2.2, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.69}}, {'dt': 1641834000, 'temp': 24.76, 'feels_like': 25.38, 'pressure': 1014, 'humidity': 80, 'dew_point': 21.08, 'uvi': 12.18, 'clouds': 83, 'visibility': 5729, 'wind_speed': 2.4, 'wind_deg': 294, 'wind_gust': 2.82, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.86}}, {'dt': 1641837600, 'temp': 23.92, 'feels_like': 24.53, 'pressure': 1013, 'humidity': 83, 'dew_point': 20.86, 'uvi': 11.62, 'clouds': 83, 'visibility': 5364, 'wind_speed': 1.91, 'wind_deg': 300, 'wind_gust': 2.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.29}}, {'dt': 1641841200, 'temp': 23.63, 'feels_like': 24.27, 'pressure': 1013, 'humidity': 85, 'dew_point': 20.96, 'uvi': 7.38, 'clouds': 93, 'visibility': 4911, 'wind_speed': 2.05, 'wind_deg': 300, 'wind_gust': 2.69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.58}}, {'dt': 1641844800, 'temp': 22.94, 'feels_like': 23.59, 'pressure': 1012, 'humidity': 88, 'dew_point': 20.85, 'uvi': 4.68, 'clouds': 92, 'visibility': 4838, 'wind_speed': 2.08, 'wind_deg': 297, 'wind_gust': 2.97, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.67}}, {'dt': 1641848400, 'temp': 22.31, 'feels_like': 22.97, 'pressure': 1011, 'humidity': 91, 'dew_point': 20.77, 'uvi': 2.17, 'clouds': 92, 'visibility': 5622, 'wind_speed': 1.83, 'wind_deg': 293, 'wind_gust': 2.97, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.42}}, {'dt': 1641852000, 'temp': 21.94, 'feels_like': 22.62, 'pressure': 1012, 'humidity': 93, 'dew_point': 20.76, 'uvi': 0.73, 'clouds': 90, 'visibility': 4418, 'wind_speed': 1.64, 'wind_deg': 283, 'wind_gust': 2.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 2.08}}, {'dt': 1641855600, 'temp': 21.3, 'feels_like': 21.97, 'pressure': 1012, 'humidity': 95, 'dew_point': 20.47, 'uvi': 0, 'clouds': 87, 'visibility': 5643, 'wind_speed': 1.08, 'wind_deg': 276, 'wind_gust': 1.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.61}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 20.100000 | 21.560000 | 95.000000 | 1012.000000 | 0.76 | 20.930000 | 0.000000 | 10000.000000 | 229.000000 | 1.45 | 1.210000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 20.140000 | 21.440000 | 96.000000 | 1013.000000 | 0.31 | 20.800000 | 0.000000 | 10000.000000 | 219.000000 | 1.24 | 1.080000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 20.010000 | 21.300000 | 96.000000 | 1014.000000 | 0.29 | 20.670000 | 0.000000 | 10000.000000 | 211.000000 | 1.03 | 0.920000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 20.090000 | 21.230000 | 97.000000 | 1015.000000 | 0.11 | 20.580000 | 0.000000 | 10000.000000 | 206.000000 | 0.85 | 0.800000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 19.930000 | 21.050000 | 97.000000 | 1014.000000 |  | 20.420000 | 0.000000 | 10000.000000 | 197.000000 | 0.87 | 0.850000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 19.830000 | 20.940000 | 97.000000 | 1014.000000 |  | 20.320000 | 0.000000 | 10000.000000 | 207.000000 | 1.07 | 0.970000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 19.870000 | 20.830000 | 98.000000 | 1013.000000 | 0.13 | 20.200000 | 0.000000 | 10000.000000 | 209.000000 | 1.38 | 1.120000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 19.750000 | 20.700000 | 98.000000 | 1013.000000 |  | 20.080000 | 0.000000 | 10000.000000 | 189.000000 | 1.12 | 0.970000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 19.500000 | 20.580000 | 97.000000 | 1012.000000 | 0.17 | 19.990000 | 0.000000 | 10000.000000 | 183.000000 | 0.89 | 0.810000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 19.460000 | 20.530000 | 97.000000 | 1012.000000 | 0.21 | 19.950000 | 0.000000 | 10000.000000 | 189.000000 | 0.82 | 0.760000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 19.500000 | 20.740000 | 96.000000 | 1013.000000 |  | 20.160000 | 0.000000 | 10000.000000 | 165.000000 | 0.77 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 19.330000 | 20.710000 | 95.000000 | 1013.000000 | 0.18 | 20.160000 | 0.000000 | 10000.000000 | 173.000000 | 0.38 | 0.140000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 12:00:00 | 93.000000 | 19.540000 | 21.100000 | 94.000000 | 1014.000000 | 0.33 | 20.540000 | 0.320000 | 10000.000000 | 228.000000 | 0.87 | 0.490000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 13:00:00 | 98.000000 | 20.050000 | 22.520000 | 89.000000 | 1015.000000 | 0.6 | 21.950000 | 1.700000 | 9728.000000 | 223.000000 | 1.29 | 0.660000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 14:00:00 | 99.000000 | 20.450000 | 23.890000 | 84.000000 | 1015.000000 | 1.35 | 23.310000 | 4.460000 | 6718.000000 | 263.000000 | 2.19 | 1.240000 | 501 | Rain | moderate rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 15:00:00 | 85.000000 | 20.640000 | 24.680000 | 81.000000 | 1015.000000 | 1.48 | 24.100000 | 7.990000 | 8247.000000 | 278.000000 | 2.61 | 1.770000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 16:00:00 | 85.000000 | 20.880000 | 25.160000 | 80.000000 | 1015.000000 | 1.69 | 24.560000 | 10.670000 | 6867.000000 | 295.000000 | 2.2 | 1.820000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 17:00:00 | 83.000000 | 21.080000 | 25.380000 | 80.000000 | 1014.000000 | 1.86 | 24.760000 | 12.180000 | 5729.000000 | 294.000000 | 2.82 | 2.400000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 18:00:00 | 83.000000 | 20.860000 | 24.530000 | 83.000000 | 1013.000000 | 2.29 | 23.920000 | 11.620000 | 5364.000000 | 300.000000 | 2.35 | 1.910000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 19:00:00 | 93.000000 | 20.960000 | 24.270000 | 85.000000 | 1013.000000 | 2.58 | 23.630000 | 7.380000 | 4911.000000 | 300.000000 | 2.69 | 2.050000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 20:00:00 | 92.000000 | 20.850000 | 23.590000 | 88.000000 | 1012.000000 | 2.67 | 22.940000 | 4.680000 | 4838.000000 | 297.000000 | 2.97 | 2.080000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 21:00:00 | 92.000000 | 20.770000 | 22.970000 | 91.000000 | 1011.000000 | 2.42 | 22.310000 | 2.170000 | 5622.000000 | 293.000000 | 2.97 | 1.830000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 22:00:00 | 90.000000 | 20.760000 | 22.620000 | 93.000000 | 1012.000000 | 2.08 | 21.940000 | 0.730000 | 4418.000000 | 283.000000 | 2.88 | 1.640000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025060 | "BIOTOPO - AUT [51025060]" | 1.408639 | -78.281611 | 512.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-12-12 00:00:00 | NaT | Nariño | Barbacoas | Guarapas | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 23:00:00 | 87.000000 | 20.470000 | 21.970000 | 95.000000 | 1012.000000 | 1.61 | 21.300000 | 0.000000 | 5643.000000 | 276.000000 | 1.87 | 1.080000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station51025060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station51025060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station51025060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025060_OWM_Windspeed_20220111.png)
