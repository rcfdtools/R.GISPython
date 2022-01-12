
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - SILOE - AUT [23085250] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23085250_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.4255,-76.56061111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.4255&lon=-76.56061111)


| Parameter | Value |
|---|---|
| Code | 23085250 |
| Name | SILOE - AUT [23085250] |
| Latitude, ° | 3.4255 |
| Longitude, ° | -76.56061111 |
| Elevation, m | 1238 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2005-06-28 00:00:00 |
| Suspension date | 2009-07-06 00:00:00 |
| State | Valle del Cauca |
| County | Cali |
| Stream | Guaviare |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Lilí, Melendez y Canaveralejo |

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

### (CNE index 2079) Open Weather values for station 23085250 - SILOE - AUT [23085250]

JSON data from API OWM:

```
{'lat': 3.4255, 'lon': -76.5606, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813330, 'sunset': 1641856298, 'temp': 26.81, 'feels_like': 29.32, 'pressure': 1011, 'humidity': 80, 'dew_point': 23.07, 'uvi': 3.72, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 298, 'wind_gust': 1.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, 'hourly': [{'dt': 1641772800, 'temp': 23.81, 'feels_like': 24.6, 'pressure': 1013, 'humidity': 90, 'dew_point': 22.07, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 292, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.57}}, {'dt': 1641776400, 'temp': 21.81, 'feels_like': 22.42, 'pressure': 1014, 'humidity': 91, 'dew_point': 20.28, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 284, 'wind_gust': 2.06, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.53}}, {'dt': 1641780000, 'temp': 21.81, 'feels_like': 22.42, 'pressure': 1015, 'humidity': 91, 'dew_point': 20.28, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 254, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.43}}, {'dt': 1641783600, 'temp': 21.81, 'feels_like': 22.45, 'pressure': 1016, 'humidity': 92, 'dew_point': 20.45, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 261, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641787200, 'temp': 21.81, 'feels_like': 22.45, 'pressure': 1015, 'humidity': 92, 'dew_point': 20.45, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 236, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641790800, 'temp': 20.81, 'feels_like': 21.37, 'pressure': 1015, 'humidity': 93, 'dew_point': 19.64, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 235, 'wind_gust': 0.51, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.81, 'feels_like': 21.37, 'pressure': 1014, 'humidity': 93, 'dew_point': 19.64, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 257, 'wind_gust': 0.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 19.81, 'feels_like': 20.27, 'pressure': 1014, 'humidity': 93, 'dew_point': 18.65, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 259, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641801600, 'temp': 19.81, 'feels_like': 20.3, 'pressure': 1013, 'humidity': 94, 'dew_point': 18.82, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.16, 'wind_deg': 254, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 19.81, 'feels_like': 20.33, 'pressure': 1014, 'humidity': 95, 'dew_point': 18.99, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 228, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641808800, 'temp': 18.81, 'feels_like': 19.23, 'pressure': 1014, 'humidity': 95, 'dew_point': 17.99, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 302, 'wind_gust': 0.41, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641812400, 'temp': 18.81, 'feels_like': 19.23, 'pressure': 1015, 'humidity': 95, 'dew_point': 17.99, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 291, 'wind_gust': 0.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 19.81, 'feels_like': 20.3, 'pressure': 1015, 'humidity': 94, 'dew_point': 18.82, 'uvi': 0.37, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 312, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641819600, 'temp': 20.81, 'feels_like': 21.35, 'pressure': 1016, 'humidity': 92, 'dew_point': 19.46, 'uvi': 1.66, 'clouds': 100, 'visibility': 8970, 'wind_speed': 0.25, 'wind_deg': 3, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641823200, 'temp': 21.81, 'feels_like': 22.34, 'pressure': 1017, 'humidity': 88, 'dew_point': 19.73, 'uvi': 4.22, 'clouds': 77, 'visibility': 9761, 'wind_speed': 0.69, 'wind_deg': 15, 'wind_gust': 1.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641826800, 'temp': 23.81, 'feels_like': 24.44, 'pressure': 1016, 'humidity': 84, 'dew_point': 20.94, 'uvi': 7.42, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 12, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641830400, 'temp': 24.81, 'feels_like': 25.41, 'pressure': 1015, 'humidity': 79, 'dew_point': 20.92, 'uvi': 8.93, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 347, 'wind_gust': 1.21, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641834000, 'temp': 25.81, 'feels_like': 26.46, 'pressure': 1014, 'humidity': 77, 'dew_point': 21.47, 'uvi': 10.02, 'clouds': 81, 'visibility': 8926, 'wind_speed': 0.63, 'wind_deg': 324, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.13}}, {'dt': 1641837600, 'temp': 25.81, 'feels_like': 26.46, 'pressure': 1013, 'humidity': 77, 'dew_point': 21.47, 'uvi': 9.37, 'clouds': 51, 'visibility': 4299, 'wind_speed': 1, 'wind_deg': 295, 'wind_gust': 1.57, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.29}}, {'dt': 1641841200, 'temp': 26.81, 'feels_like': 29.16, 'pressure': 1012, 'humidity': 78, 'dew_point': 22.65, 'uvi': 6.08, 'clouds': 75, 'visibility': 6138, 'wind_speed': 1.39, 'wind_deg': 289, 'wind_gust': 1.94, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.34}}, {'dt': 1641844800, 'temp': 26.81, 'feels_like': 29.32, 'pressure': 1011, 'humidity': 80, 'dew_point': 23.07, 'uvi': 3.72, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 298, 'wind_gust': 1.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, {'dt': 1641848400, 'temp': 22.81, 'feels_like': 23.34, 'pressure': 1011, 'humidity': 84, 'dew_point': 19.97, 'uvi': 1.65, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 302, 'wind_gust': 1.88, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.53}}, {'dt': 1641852000, 'temp': 20.81, 'feels_like': 21.22, 'pressure': 1012, 'humidity': 87, 'dew_point': 18.57, 'uvi': 0.37, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 312, 'wind_gust': 1.59, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641855600, 'temp': 18.81, 'feels_like': 19.12, 'pressure': 1013, 'humidity': 91, 'dew_point': 17.31, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 301, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 00:00:00 | 39.000000 | 22.070000 | 24.600000 | 90.000000 | 1013.000000 | 0.57 | 23.810000 | 0.000000 | 10000.000000 | 292.000000 | 2.49 | 1.490000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 01:00:00 | 55.000000 | 20.280000 | 22.420000 | 91.000000 | 1014.000000 | 0.53 | 21.810000 | 0.000000 | 10000.000000 | 284.000000 | 2.06 | 1.310000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 02:00:00 | 51.000000 | 20.280000 | 22.420000 | 91.000000 | 1015.000000 | 0.43 | 21.810000 | 0.000000 | 10000.000000 | 254.000000 | 1.14 | 0.750000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 03:00:00 | 50.000000 | 20.450000 | 22.450000 | 92.000000 | 1016.000000 | 0.25 | 21.810000 | 0.000000 | 10000.000000 | 261.000000 | 0.76 | 0.630000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 04:00:00 | 61.000000 | 20.450000 | 22.450000 | 92.000000 | 1015.000000 | 0.22 | 21.810000 | 0.000000 | 10000.000000 | 236.000000 | 0.7 | 0.530000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 05:00:00 | 67.000000 | 19.640000 | 21.370000 | 93.000000 | 1015.000000 |  | 20.810000 | 0.000000 | 10000.000000 | 235.000000 | 0.51 | 0.310000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 06:00:00 | 66.000000 | 19.640000 | 21.370000 | 93.000000 | 1014.000000 |  | 20.810000 | 0.000000 | 10000.000000 | 257.000000 | 0.57 | 0.440000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 18.650000 | 20.270000 | 93.000000 | 1014.000000 | 0.14 | 19.810000 | 0.000000 | 10000.000000 | 259.000000 | 0.72 | 0.340000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 18.820000 | 20.300000 | 94.000000 | 1013.000000 | 0.13 | 19.810000 | 0.000000 | 10000.000000 | 254.000000 | 0.79 | 0.160000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 18.990000 | 20.330000 | 95.000000 | 1014.000000 | 0.23 | 19.810000 | 0.000000 | 10000.000000 | 228.000000 | 0.57 | 0.150000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 17.990000 | 19.230000 | 95.000000 | 1014.000000 | 0.2 | 18.810000 | 0.000000 | 10000.000000 | 302.000000 | 0.41 | 0.110000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 17.990000 | 19.230000 | 95.000000 | 1015.000000 |  | 18.810000 | 0.000000 | 10000.000000 | 291.000000 | 0.45 | 0.270000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 12:00:00 | 98.000000 | 18.820000 | 20.300000 | 94.000000 | 1015.000000 | 0.11 | 19.810000 | 0.370000 | 10000.000000 | 312.000000 | 0.67 | 0.120000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 19.460000 | 21.350000 | 92.000000 | 1016.000000 | 0.45 | 20.810000 | 1.660000 | 8970.000000 | 3.000000 | 1.04 | 0.250000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 14:00:00 | 77.000000 | 19.730000 | 22.340000 | 88.000000 | 1017.000000 | 0.66 | 21.810000 | 4.220000 | 9761.000000 | 15.000000 | 1.28 | 0.690000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 20.940000 | 24.440000 | 84.000000 | 1016.000000 | 0.68 | 23.810000 | 7.420000 | 10000.000000 | 12.000000 | 1.31 | 0.730000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 16:00:00 | 77.000000 | 20.920000 | 25.410000 | 79.000000 | 1015.000000 | 1.15 | 24.810000 | 8.930000 | 10000.000000 | 347.000000 | 1.21 | 0.580000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 17:00:00 | 81.000000 | 21.470000 | 26.460000 | 77.000000 | 1014.000000 | 1.13 | 25.810000 | 10.020000 | 8926.000000 | 324.000000 | 1.39 | 0.630000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 18:00:00 | 51.000000 | 21.470000 | 26.460000 | 77.000000 | 1013.000000 | 1.29 | 25.810000 | 9.370000 | 4299.000000 | 295.000000 | 1.57 | 1.000000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 22.650000 | 29.160000 | 78.000000 | 1012.000000 | 1.34 | 26.810000 | 6.080000 | 6138.000000 | 289.000000 | 1.94 | 1.390000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 20:00:00 | 87.000000 | 23.070000 | 29.320000 | 80.000000 | 1011.000000 | 1.37 | 26.810000 | 3.720000 | 10000.000000 | 298.000000 | 1.88 | 1.280000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 21:00:00 | 91.000000 | 19.970000 | 23.340000 | 84.000000 | 1011.000000 | 1.53 | 22.810000 | 1.650000 | 10000.000000 | 302.000000 | 1.88 | 1.290000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 22:00:00 | 93.000000 | 18.570000 | 21.220000 | 87.000000 | 1012.000000 | 1.16 | 20.810000 | 0.370000 | 10000.000000 | 312.000000 | 1.59 | 1.010000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23085250 | "SILOE - AUT [23085250]" | 3.425500 | -76.560611 | 1238.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-06-28 00:00:00 | 2009-07-06 00:00:00 | Valle del Cauca | Cali | Guaviare | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Lilí, Melendez y Canaveralejo | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 17.310000 | 19.120000 | 91.000000 | 1013.000000 | 1.14 | 18.810000 | 0.000000 | 10000.000000 | 301.000000 | 1.75 | 1.250000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station23085250_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23085250_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23085250_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23085250_OWM_Windspeed_20220111.png)
