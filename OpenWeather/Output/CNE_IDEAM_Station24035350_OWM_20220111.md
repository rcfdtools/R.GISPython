
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ANDALUCIA [24035350] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035350_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.90113889,-73.05833333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.90113889&lon=-73.05833333)


| Parameter | Value |
|---|---|
| Code | 24035350 |
| Name | ANDALUCIA [24035350] |
| Latitude, ° | 5.90113889 |
| Longitude, ° | -73.05833333 |
| Elevation, m | 3265 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1996-09-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Duitama |
| Stream | Magdalena |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Chicamocha |

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

### (CNE index 997) Open Weather values for station 24035350 - ANDALUCIA [24035350]

JSON data from API OWM:

```
{'lat': 5.9011, 'lon': -73.0583, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812730, 'sunset': 1641855217, 'temp': 12.38, 'feels_like': 11.16, 'pressure': 1011, 'humidity': 57, 'dew_point': 4.11, 'uvi': 3.84, 'clouds': 82, 'visibility': 10000, 'wind_speed': 3.58, 'wind_deg': 314, 'wind_gust': 3.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 5.55, 'feels_like': 5.55, 'pressure': 1017, 'humidity': 96, 'dew_point': 4.96, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 317, 'wind_gust': 1.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 5.09, 'feels_like': 5.09, 'pressure': 1018, 'humidity': 96, 'dew_point': 4.51, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 317, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 4.68, 'feels_like': 4.68, 'pressure': 1019, 'humidity': 96, 'dew_point': 4.1, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 323, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 4.12, 'feels_like': 4.12, 'pressure': 1019, 'humidity': 97, 'dew_point': 3.69, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.52, 'wind_deg': 335, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 3.73, 'feels_like': 3.73, 'pressure': 1019, 'humidity': 96, 'dew_point': 3.15, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 342, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 3.52, 'feels_like': 3.52, 'pressure': 1019, 'humidity': 95, 'dew_point': 2.8, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 198, 'wind_gust': 0.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 3.5, 'feels_like': 3.5, 'pressure': 1018, 'humidity': 95, 'dew_point': 2.78, 'uvi': 0, 'clouds': 62, 'visibility': 9909, 'wind_speed': 0.11, 'wind_deg': 192, 'wind_gust': 0.55, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 3.56, 'feels_like': 3.56, 'pressure': 1017, 'humidity': 95, 'dew_point': 2.84, 'uvi': 0, 'clouds': 86, 'visibility': 9591, 'wind_speed': 0.15, 'wind_deg': 353, 'wind_gust': 0.49, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 3.57, 'feels_like': 3.57, 'pressure': 1017, 'humidity': 93, 'dew_point': 2.55, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 321, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 3.8, 'feels_like': 3.8, 'pressure': 1016, 'humidity': 93, 'dew_point': 2.77, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 346, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 3.89, 'feels_like': 3.89, 'pressure': 1017, 'humidity': 91, 'dew_point': 2.56, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 8, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 3.75, 'feels_like': 3.75, 'pressure': 1018, 'humidity': 91, 'dew_point': 2.42, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 78, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 4.09, 'feels_like': 4.09, 'pressure': 1019, 'humidity': 92, 'dew_point': 2.91, 'uvi': 0.57, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.31, 'wind_deg': 57, 'wind_gust': 0.76, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 6.72, 'feels_like': 6.72, 'pressure': 1019, 'humidity': 80, 'dew_point': 3.52, 'uvi': 2.33, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 328, 'wind_gust': 0.92, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 8.96, 'feels_like': 8.96, 'pressure': 1019, 'humidity': 69, 'dew_point': 3.59, 'uvi': 5.47, 'clouds': 66, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 304, 'wind_gust': 1.46, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 10.91, 'feels_like': 9.62, 'pressure': 1018, 'humidity': 60, 'dew_point': 3.46, 'uvi': 9.11, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 302, 'wind_gust': 2.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 12.01, 'feels_like': 10.7, 'pressure': 1016, 'humidity': 55, 'dew_point': 3.26, 'uvi': 11.79, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 300, 'wind_gust': 3.17, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 12.92, 'feels_like': 11.6, 'pressure': 1015, 'humidity': 51, 'dew_point': 3.04, 'uvi': 12.68, 'clouds': 56, 'visibility': 10000, 'wind_speed': 2.91, 'wind_deg': 301, 'wind_gust': 3.53, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 13.57, 'feels_like': 12.26, 'pressure': 1013, 'humidity': 49, 'dew_point': 3.07, 'uvi': 11.35, 'clouds': 62, 'visibility': 10000, 'wind_speed': 3.36, 'wind_deg': 308, 'wind_gust': 3.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 13.43, 'feels_like': 12.13, 'pressure': 1012, 'humidity': 50, 'dew_point': 3.23, 'uvi': 6.78, 'clouds': 67, 'visibility': 10000, 'wind_speed': 3.78, 'wind_deg': 310, 'wind_gust': 3.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 12.38, 'feels_like': 11.16, 'pressure': 1011, 'humidity': 57, 'dew_point': 4.11, 'uvi': 3.84, 'clouds': 82, 'visibility': 10000, 'wind_speed': 3.58, 'wind_deg': 314, 'wind_gust': 3.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 10.7, 'feels_like': 9.6, 'pressure': 1012, 'humidity': 68, 'dew_point': 5.04, 'uvi': 1.5, 'clouds': 87, 'visibility': 10000, 'wind_speed': 3.06, 'wind_deg': 313, 'wind_gust': 3.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641852000, 'temp': 8.88, 'feels_like': 7.61, 'pressure': 1013, 'humidity': 81, 'dew_point': 5.8, 'uvi': 0.36, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 314, 'wind_gust': 2.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641855600, 'temp': 6.11, 'feels_like': 5.19, 'pressure': 1015, 'humidity': 94, 'dew_point': 5.22, 'uvi': 0, 'clouds': 84, 'visibility': 9263, 'wind_speed': 1.52, 'wind_deg': 314, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 67.000000 | 4.960000 | 5.550000 | 96.000000 | 1017.000000 |  | 5.550000 | 0.000000 | 10000.000000 | 317.000000 | 1.38 | 1.010000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 76.000000 | 4.510000 | 5.090000 | 96.000000 | 1018.000000 |  | 5.090000 | 0.000000 | 10000.000000 | 317.000000 | 1.33 | 0.900000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 79.000000 | 4.100000 | 4.680000 | 96.000000 | 1019.000000 |  | 4.680000 | 0.000000 | 10000.000000 | 323.000000 | 1.3 | 0.780000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 81.000000 | 3.690000 | 4.120000 | 97.000000 | 1019.000000 |  | 4.120000 | 0.000000 | 10000.000000 | 335.000000 | 1.11 | 0.520000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 3.150000 | 3.730000 | 96.000000 | 1019.000000 |  | 3.730000 | 0.000000 | 10000.000000 | 342.000000 | 0.95 | 0.170000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 80.000000 | 2.800000 | 3.520000 | 95.000000 | 1019.000000 |  | 3.520000 | 0.000000 | 10000.000000 | 198.000000 | 0.77 | 0.110000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 62.000000 | 2.780000 | 3.500000 | 95.000000 | 1018.000000 |  | 3.500000 | 0.000000 | 9909.000000 | 192.000000 | 0.55 | 0.110000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 86.000000 | 2.840000 | 3.560000 | 95.000000 | 1017.000000 |  | 3.560000 | 0.000000 | 9591.000000 | 353.000000 | 0.49 | 0.150000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 85.000000 | 2.550000 | 3.570000 | 93.000000 | 1017.000000 |  | 3.570000 | 0.000000 | 10000.000000 | 321.000000 | 0.67 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 86.000000 | 2.770000 | 3.800000 | 93.000000 | 1016.000000 |  | 3.800000 | 0.000000 | 10000.000000 | 346.000000 | 0.76 | 0.400000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 87.000000 | 2.560000 | 3.890000 | 91.000000 | 1017.000000 |  | 3.890000 | 0.000000 | 10000.000000 | 8.000000 | 0.76 | 0.190000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 87.000000 | 2.420000 | 3.750000 | 91.000000 | 1018.000000 |  | 3.750000 | 0.000000 | 10000.000000 | 78.000000 | 0.63 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 29.000000 | 2.910000 | 4.090000 | 92.000000 | 1019.000000 |  | 4.090000 | 0.570000 | 10000.000000 | 57.000000 | 0.76 | 0.310000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 48.000000 | 3.520000 | 6.720000 | 80.000000 | 1019.000000 |  | 6.720000 | 2.330000 | 10000.000000 | 328.000000 | 0.92 | 0.730000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 66.000000 | 3.590000 | 8.960000 | 69.000000 | 1019.000000 |  | 8.960000 | 5.470000 | 10000.000000 | 304.000000 | 1.46 | 1.170000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 3.460000 | 9.620000 | 60.000000 | 1018.000000 |  | 10.910000 | 9.110000 | 10000.000000 | 302.000000 | 2.5 | 1.690000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 63.000000 | 3.260000 | 10.700000 | 55.000000 | 1016.000000 |  | 12.010000 | 11.790000 | 10000.000000 | 300.000000 | 3.17 | 2.270000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 56.000000 | 3.040000 | 11.600000 | 51.000000 | 1015.000000 |  | 12.920000 | 12.680000 | 10000.000000 | 301.000000 | 3.53 | 2.910000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 62.000000 | 3.070000 | 12.260000 | 49.000000 | 1013.000000 |  | 13.570000 | 11.350000 | 10000.000000 | 308.000000 | 3.69 | 3.360000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 67.000000 | 3.230000 | 12.130000 | 50.000000 | 1012.000000 |  | 13.430000 | 6.780000 | 10000.000000 | 310.000000 | 3.79 | 3.780000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 82.000000 | 4.110000 | 11.160000 | 57.000000 | 1011.000000 |  | 12.380000 | 3.840000 | 10000.000000 | 314.000000 | 3.67 | 3.580000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 87.000000 | 5.040000 | 9.600000 | 68.000000 | 1012.000000 | 0.18 | 10.700000 | 1.500000 | 10000.000000 | 313.000000 | 3.31 | 3.060000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 80.000000 | 5.800000 | 7.610000 | 81.000000 | 1013.000000 | 0.22 | 8.880000 | 0.360000 | 10000.000000 | 314.000000 | 2.83 | 2.350000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035350 | "ANDALUCIA [24035350]" | 5.901139 | -73.058333 | 3265.000000 | Climática Principal | Convencional | Activa | 1996-09-15 00:00:00 | NaT | Boyacá | Duitama | Magdalena | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 84.000000 | 5.220000 | 5.190000 | 94.000000 | 1015.000000 | 0.12 | 6.110000 | 0.000000 | 9263.000000 | 314.000000 | 1.93 | 1.520000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24035350_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035350_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035350_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035350_OWM_Windspeed_20220111.png)
