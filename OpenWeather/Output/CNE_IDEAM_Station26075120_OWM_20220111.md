
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA DIANA - AUT [26075120] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26075120_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.31405556,-76.18569444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.31405556&lon=-76.18569444)


| Parameter | Value |
|---|---|
| Code | 26075120 |
| Name | LA DIANA - AUT [26075120] |
| Latitude, ° | 3.31405556 |
| Longitude, ° | -76.18569444 |
| Elevation, m | 1615 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-26 00:00:00 |
| Suspension date | NaT |
| State | Valle del Cauca |
| County | Florida |
| Stream | Yaguara |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Guachal (Bolo - Fraile y Párraga) |

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

### (CNE index 67) Open Weather values for station 26075120 - LA DIANA - AUT [26075120]

JSON data from API OWM:

```
{'lat': 3.3141, 'lon': -76.1857, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813230, 'sunset': 1641856219, 'temp': 24.43, 'feels_like': 25.07, 'pressure': 1013, 'humidity': 82, 'dew_point': 21.16, 'uvi': 4.75, 'clouds': 90, 'visibility': 5530, 'wind_speed': 1.34, 'wind_deg': 289, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.04}}, 'hourly': [{'dt': 1641772800, 'temp': 21.43, 'feels_like': 22.06, 'pressure': 1015, 'humidity': 93, 'dew_point': 20.25, 'uvi': 0, 'clouds': 60, 'visibility': 6598, 'wind_speed': 0.83, 'wind_deg': 103, 'wind_gust': 1.29, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.12}}, {'dt': 1641776400, 'temp': 19.43, 'feels_like': 19.88, 'pressure': 1016, 'humidity': 94, 'dew_point': 18.44, 'uvi': 0, 'clouds': 84, 'visibility': 9020, 'wind_speed': 0.99, 'wind_deg': 102, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.16}}, {'dt': 1641780000, 'temp': 19.43, 'feels_like': 19.91, 'pressure': 1017, 'humidity': 95, 'dew_point': 18.61, 'uvi': 0, 'clouds': 88, 'visibility': 7376, 'wind_speed': 0.82, 'wind_deg': 110, 'wind_gust': 1.07, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.01}}, {'dt': 1641783600, 'temp': 19.43, 'feels_like': 19.91, 'pressure': 1017, 'humidity': 95, 'dew_point': 18.61, 'uvi': 0, 'clouds': 90, 'visibility': 8823, 'wind_speed': 0.44, 'wind_deg': 100, 'wind_gust': 0.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.57}}, {'dt': 1641787200, 'temp': 19.43, 'feels_like': 19.94, 'pressure': 1017, 'humidity': 96, 'dew_point': 18.78, 'uvi': 0, 'clouds': 93, 'visibility': 9448, 'wind_speed': 0.23, 'wind_deg': 147, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1641790800, 'temp': 18.43, 'feels_like': 18.84, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.78, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.29, 'wind_deg': 125, 'wind_gust': 0.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.38}}, {'dt': 1641794400, 'temp': 18.43, 'feels_like': 18.89, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.11, 'uvi': 0, 'clouds': 64, 'visibility': 9224, 'wind_speed': 0.01, 'wind_deg': 250, 'wind_gust': 0.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641798000, 'temp': 17.43, 'feels_like': 17.81, 'pressure': 1016, 'humidity': 99, 'dew_point': 17.27, 'uvi': 0, 'clouds': 92, 'visibility': 8914, 'wind_speed': 0.06, 'wind_deg': 78, 'wind_gust': 0.39, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641801600, 'temp': 17.43, 'feels_like': 17.79, 'pressure': 1015, 'humidity': 98, 'dew_point': 17.11, 'uvi': 0, 'clouds': 96, 'visibility': 4508, 'wind_speed': 0.03, 'wind_deg': 132, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641805200, 'temp': 17.43, 'feels_like': 17.79, 'pressure': 1015, 'humidity': 98, 'dew_point': 17.11, 'uvi': 0, 'clouds': 97, 'visibility': 1843, 'wind_speed': 0.35, 'wind_deg': 283, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641808800, 'temp': 16.43, 'feels_like': 16.69, 'pressure': 1016, 'humidity': 98, 'dew_point': 16.11, 'uvi': 0, 'clouds': 98, 'visibility': 1523, 'wind_speed': 0.21, 'wind_deg': 320, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.46}}, {'dt': 1641812400, 'temp': 16.43, 'feels_like': 16.66, 'pressure': 1016, 'humidity': 97, 'dew_point': 15.95, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 289, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641816000, 'temp': 17.43, 'feels_like': 17.74, 'pressure': 1017, 'humidity': 96, 'dew_point': 16.79, 'uvi': 0.32, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.05, 'wind_deg': 358, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641819600, 'temp': 18.43, 'feels_like': 18.76, 'pressure': 1018, 'humidity': 93, 'dew_point': 17.28, 'uvi': 1.34, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 279, 'wind_gust': 0.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641823200, 'temp': 19.43, 'feels_like': 19.73, 'pressure': 1018, 'humidity': 88, 'dew_point': 17.39, 'uvi': 3.39, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 306, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.5}}, {'dt': 1641826800, 'temp': 21.43, 'feels_like': 21.8, 'pressure': 1018, 'humidity': 83, 'dew_point': 18.42, 'uvi': 5.91, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 296, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641830400, 'temp': 22.43, 'feels_like': 22.77, 'pressure': 1017, 'humidity': 78, 'dew_point': 18.41, 'uvi': 11.68, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.64, 'wind_deg': 290, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}, {'dt': 1641834000, 'temp': 23.43, 'feels_like': 23.81, 'pressure': 1015, 'humidity': 76, 'dew_point': 18.96, 'uvi': 13.02, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 289, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641837600, 'temp': 23.43, 'feels_like': 23.81, 'pressure': 1015, 'humidity': 76, 'dew_point': 18.96, 'uvi': 12.1, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 281, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.9}}, {'dt': 1641841200, 'temp': 24.43, 'feels_like': 24.97, 'pressure': 1013, 'humidity': 78, 'dew_point': 20.34, 'uvi': 7.84, 'clouds': 92, 'visibility': 5676, 'wind_speed': 1.56, 'wind_deg': 287, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641844800, 'temp': 24.43, 'feels_like': 25.07, 'pressure': 1013, 'humidity': 82, 'dew_point': 21.16, 'uvi': 4.75, 'clouds': 90, 'visibility': 5530, 'wind_speed': 1.34, 'wind_deg': 289, 'wind_gust': 1.36, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.04}}, {'dt': 1641848400, 'temp': 20.43, 'feels_like': 20.77, 'pressure': 1013, 'humidity': 86, 'dew_point': 18.01, 'uvi': 2.08, 'clouds': 94, 'visibility': 5670, 'wind_speed': 1.16, 'wind_deg': 298, 'wind_gust': 1.3, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641852000, 'temp': 18.43, 'feels_like': 18.7, 'pressure': 1014, 'humidity': 91, 'dew_point': 16.93, 'uvi': 0.5, 'clouds': 95, 'visibility': 5818, 'wind_speed': 1.09, 'wind_deg': 296, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.1}}, {'dt': 1641855600, 'temp': 16.43, 'feels_like': 16.58, 'pressure': 1015, 'humidity': 94, 'dew_point': 15.46, 'uvi': 0, 'clouds': 96, 'visibility': 7942, 'wind_speed': 0.42, 'wind_deg': 55, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.97}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 00:00:00 | 60.000000 | 20.250000 | 22.060000 | 93.000000 | 1015.000000 | 1.12 | 21.430000 | 0.000000 | 6598.000000 | 103.000000 | 1.29 | 0.830000 | 501 | Rain | moderate rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 01:00:00 | 84.000000 | 18.440000 | 19.880000 | 94.000000 | 1016.000000 | 1.16 | 19.430000 | 0.000000 | 9020.000000 | 102.000000 | 1.3 | 0.990000 | 501 | Rain | moderate rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 02:00:00 | 88.000000 | 18.610000 | 19.910000 | 95.000000 | 1017.000000 | 1.01 | 19.430000 | 0.000000 | 7376.000000 | 110.000000 | 1.07 | 0.820000 | 501 | Rain | moderate rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 03:00:00 | 90.000000 | 18.610000 | 19.910000 | 95.000000 | 1017.000000 | 0.57 | 19.430000 | 0.000000 | 8823.000000 | 100.000000 | 0.69 | 0.440000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 18.780000 | 19.940000 | 96.000000 | 1017.000000 | 0.47 | 19.430000 | 0.000000 | 9448.000000 | 147.000000 | 0.54 | 0.230000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | 17.780000 | 18.840000 | 96.000000 | 1017.000000 | 0.38 | 18.430000 | 0.000000 | 10000.000000 | 125.000000 | 0.38 | 0.290000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 06:00:00 | 64.000000 | 18.110000 | 18.890000 | 98.000000 | 1016.000000 | 0.21 | 18.430000 | 0.000000 | 9224.000000 | 250.000000 | 0.28 | 0.010000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 07:00:00 | 92.000000 | 17.270000 | 17.810000 | 99.000000 | 1016.000000 | 0.25 | 17.430000 | 0.000000 | 8914.000000 | 78.000000 | 0.39 | 0.060000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 08:00:00 | 96.000000 | 17.110000 | 17.790000 | 98.000000 | 1015.000000 | 0.42 | 17.430000 | 0.000000 | 4508.000000 | 132.000000 | 0.57 | 0.030000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 09:00:00 | 97.000000 | 17.110000 | 17.790000 | 98.000000 | 1015.000000 | 0.42 | 17.430000 | 0.000000 | 1843.000000 | 283.000000 | 0.74 | 0.350000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 16.110000 | 16.690000 | 98.000000 | 1016.000000 | 0.46 | 16.430000 | 0.000000 | 1523.000000 | 320.000000 | 0.79 | 0.210000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 15.950000 | 16.660000 | 97.000000 | 1016.000000 | 0.39 | 16.430000 | 0.000000 | 10000.000000 | 289.000000 | 0.66 | 0.250000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 12:00:00 | 97.000000 | 16.790000 | 17.740000 | 96.000000 | 1017.000000 | 0.26 | 17.430000 | 0.320000 | 10000.000000 | 358.000000 | 0.72 | 0.050000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 17.280000 | 18.760000 | 93.000000 | 1018.000000 | 0.39 | 18.430000 | 1.340000 | 10000.000000 | 279.000000 | 0.77 | 0.350000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 17.390000 | 19.730000 | 88.000000 | 1018.000000 | 0.5 | 19.430000 | 3.390000 | 10000.000000 | 306.000000 | 0.81 | 0.890000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 18.420000 | 21.800000 | 83.000000 | 1018.000000 | 0.56 | 21.430000 | 5.910000 | 10000.000000 | 296.000000 | 1.02 | 1.500000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 18.410000 | 22.770000 | 78.000000 | 1017.000000 | 0.42 | 22.430000 | 11.680000 | 10000.000000 | 290.000000 | 1.05 | 1.640000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 18.960000 | 23.810000 | 76.000000 | 1015.000000 | 0.6 | 23.430000 | 13.020000 | 10000.000000 | 289.000000 | 1.32 | 1.720000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 18:00:00 | 93.000000 | 18.960000 | 23.810000 | 76.000000 | 1015.000000 | 0.9 | 23.430000 | 12.100000 | 10000.000000 | 281.000000 | 1.37 | 1.700000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 19:00:00 | 92.000000 | 20.340000 | 24.970000 | 78.000000 | 1013.000000 | 0.94 | 24.430000 | 7.840000 | 5676.000000 | 287.000000 | 1.38 | 1.560000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 20:00:00 | 90.000000 | 21.160000 | 25.070000 | 82.000000 | 1013.000000 | 1.04 | 24.430000 | 4.750000 | 5530.000000 | 289.000000 | 1.36 | 1.340000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 21:00:00 | 94.000000 | 18.010000 | 20.770000 | 86.000000 | 1013.000000 | 1.01 | 20.430000 | 2.080000 | 5670.000000 | 298.000000 | 1.3 | 1.160000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 16.930000 | 18.700000 | 91.000000 | 1014.000000 | 1.1 | 18.430000 | 0.500000 | 5818.000000 | 296.000000 | 1.64 | 1.090000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26075120 | "LA DIANA - AUT [26075120]" | 3.314056 | -76.185694 | 1615.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-26 00:00:00 | NaT | Valle del Cauca | Florida | Yaguara | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Guachal (Bolo - Fraile y Párraga) | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 15.460000 | 16.580000 | 94.000000 | 1015.000000 | 0.97 | 16.430000 | 0.000000 | 7942.000000 | 55.000000 | 1.02 | 0.420000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26075120_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26075120_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26075120_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26075120_OWM_Windspeed_20220111.png)
