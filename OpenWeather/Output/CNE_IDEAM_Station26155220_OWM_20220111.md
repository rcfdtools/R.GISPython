
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLAMARIA - AUT [26155220] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26155220_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.04866667,-75.51388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.04866667&lon=-75.51388889)


| Parameter | Value |
|---|---|
| Code | 26155220 |
| Name | VILLAMARIA - AUT [26155220] |
| Latitude, ° | 5.04866667 |
| Longitude, ° | -75.51388889 |
| Elevation, m | 1906 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-06-14 00:00:00 |
| Suspension date | NaT |
| State | Caldas |
| County | Villamaria |
| Stream | San Juan |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río Chinchiná |

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

### (CNE index 130) Open Weather values for station 26155220 - VILLAMARIA - AUT [26155220]

JSON data from API OWM:

```
{'lat': 5.0487, 'lon': -75.5139, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813236, 'sunset': 1641855889, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.52, 'uvi': 3.28, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.44}}, 'hourly': [{'dt': 1641772800, 'temp': 18.59, 'feels_like': 19.06, 'pressure': 1016, 'humidity': 98, 'dew_point': 18.27, 'uvi': 0, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 104, 'wind_gust': 1.48, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641776400, 'temp': 18.59, 'feels_like': 19.01, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.94, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 102, 'wind_gust': 1.39, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 17.59, 'feels_like': 17.91, 'pressure': 1018, 'humidity': 96, 'dew_point': 16.94, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 107, 'wind_gust': 1.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641783600, 'temp': 17.59, 'feels_like': 17.91, 'pressure': 1018, 'humidity': 96, 'dew_point': 16.94, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 111, 'wind_gust': 0.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 16.59, 'feels_like': 16.81, 'pressure': 1018, 'humidity': 96, 'dew_point': 15.95, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 116, 'wind_gust': 0.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 16.59, 'feels_like': 16.84, 'pressure': 1017, 'humidity': 97, 'dew_point': 16.11, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 121, 'wind_gust': 0.62, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 16.59, 'feels_like': 16.86, 'pressure': 1017, 'humidity': 98, 'dew_point': 16.27, 'uvi': 0, 'clouds': 52, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 144, 'wind_gust': 0.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 16.59, 'feels_like': 16.89, 'pressure': 1016, 'humidity': 99, 'dew_point': 16.43, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 125, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641801600, 'temp': 14.34, 'feels_like': 14.39, 'pressure': 1016, 'humidity': 98, 'dew_point': 14.03, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 146, 'wind_gust': 0.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641805200, 'temp': 14.71, 'feels_like': 14.77, 'pressure': 1016, 'humidity': 97, 'dew_point': 14.24, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 158, 'wind_gust': 0.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641808800, 'temp': 15.59, 'feels_like': 15.74, 'pressure': 1017, 'humidity': 97, 'dew_point': 15.12, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 175, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641812400, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.52, 'uvi': 0, 'clouds': 75, 'visibility': 2000, 'wind_speed': 1.54, 'wind_deg': 120, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09n'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.52, 'uvi': 0.2, 'clouds': 75, 'visibility': 2000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1027, 'humidity': 100, 'dew_point': 15.52, 'uvi': 1.1, 'clouds': 75, 'visibility': 3000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 16.52, 'feels_like': 16.84, 'pressure': 1028, 'humidity': 100, 'dew_point': 16.52, 'uvi': 2.79, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641826800, 'temp': 18.52, 'feels_like': 18.88, 'pressure': 1028, 'humidity': 94, 'dew_point': 17.54, 'uvi': 4.85, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641830400, 'temp': 21.52, 'feels_like': 21.74, 'pressure': 1027, 'humidity': 77, 'dew_point': 17.32, 'uvi': 6.75, 'clouds': 75, 'visibility': 7000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641834000, 'temp': 18.52, 'feels_like': 18.88, 'pressure': 1027, 'humidity': 94, 'dew_point': 17.54, 'uvi': 7.49, 'clouds': 75, 'visibility': 6000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641837600, 'temp': 16.52, 'feels_like': 16.84, 'pressure': 1027, 'humidity': 100, 'dew_point': 16.52, 'uvi': 6.92, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.66}}, {'dt': 1641841200, 'temp': 16.52, 'feels_like': 16.84, 'pressure': 1026, 'humidity': 100, 'dew_point': 16.52, 'uvi': 5.5, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.61}}, {'dt': 1641844800, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.52, 'uvi': 3.28, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.44}}, {'dt': 1641848400, 'temp': 16.52, 'feels_like': 16.84, 'pressure': 1025, 'humidity': 100, 'dew_point': 16.52, 'uvi': 1.38, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641852000, 'temp': 16.52, 'feels_like': 16.84, 'pressure': 1026, 'humidity': 100, 'dew_point': 16.52, 'uvi': 0.3, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641855600, 'temp': 15.52, 'feels_like': 15.74, 'pressure': 1026, 'humidity': 100, 'dew_point': 15.52, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 00:00:00 | 67.000000 | 18.270000 | 19.060000 | 98.000000 | 1016.000000 | 0.64 | 18.590000 | 0.000000 | 10000.000000 | 104.000000 | 1.48 | 1.720000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 01:00:00 | 94.000000 | 17.940000 | 19.010000 | 96.000000 | 1017.000000 |  | 18.590000 | 0.000000 | 10000.000000 | 102.000000 | 1.39 | 1.670000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 02:00:00 | 87.000000 | 16.940000 | 17.910000 | 96.000000 | 1018.000000 | 0.3 | 17.590000 | 0.000000 | 10000.000000 | 107.000000 | 1.21 | 1.530000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 03:00:00 | 83.000000 | 16.940000 | 17.910000 | 96.000000 | 1018.000000 |  | 17.590000 | 0.000000 | 10000.000000 | 111.000000 | 0.88 | 1.180000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 04:00:00 | 79.000000 | 15.950000 | 16.810000 | 96.000000 | 1018.000000 |  | 16.590000 | 0.000000 | 10000.000000 | 116.000000 | 0.73 | 0.960000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 05:00:00 | 79.000000 | 16.110000 | 16.840000 | 97.000000 | 1017.000000 |  | 16.590000 | 0.000000 | 10000.000000 | 121.000000 | 0.62 | 0.780000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 06:00:00 | 52.000000 | 16.270000 | 16.860000 | 98.000000 | 1017.000000 |  | 16.590000 | 0.000000 | 10000.000000 | 144.000000 | 0.54 | 0.630000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 07:00:00 | 89.000000 | 16.430000 | 16.890000 | 99.000000 | 1016.000000 | 0.12 | 16.590000 | 0.000000 | 10000.000000 | 125.000000 | 0.75 | 0.950000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 14.030000 | 14.390000 | 98.000000 | 1016.000000 | 0.18 | 14.340000 | 0.000000 | 10000.000000 | 146.000000 | 0.68 | 0.680000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 09:00:00 | 95.000000 | 14.240000 | 14.770000 | 97.000000 | 1016.000000 | 0.19 | 14.710000 | 0.000000 | 10000.000000 | 158.000000 | 0.65 | 0.450000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 10:00:00 | 95.000000 | 15.120000 | 15.740000 | 97.000000 | 1017.000000 | 0.12 | 15.590000 | 0.000000 | 10000.000000 | 175.000000 | 0.76 | 0.490000 | 500 | Rain | light rain | 10n | 10 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 15.520000 | 15.740000 | 100.000000 | 1026.000000 |  | 15.520000 | 0.000000 | 2000.000000 | 120.000000 |  | 1.540000 | 301 | Drizzle | drizzle | 09n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 15.520000 | 15.740000 | 100.000000 | 1026.000000 |  | 15.520000 | 0.200000 | 2000.000000 | 290.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 12 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 15.520000 | 15.740000 | 100.000000 | 1027.000000 |  | 15.520000 | 1.100000 | 3000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 13 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 16.520000 | 16.840000 | 100.000000 | 1028.000000 |  | 16.520000 | 2.790000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 14 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 17.540000 | 18.880000 | 94.000000 | 1028.000000 |  | 18.520000 | 4.850000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 15 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 17.320000 | 21.740000 | 77.000000 | 1027.000000 |  | 21.520000 | 6.750000 | 7000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 16 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 17.540000 | 18.880000 | 94.000000 | 1027.000000 |  | 18.520000 | 7.490000 | 6000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 16.520000 | 16.840000 | 100.000000 | 1027.000000 | 0.66 | 16.520000 | 6.920000 | 1000.000000 | 300.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 16.520000 | 16.840000 | 100.000000 | 1026.000000 | 0.61 | 16.520000 | 5.500000 | 1000.000000 | 290.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 20:00:00 | 90.000000 | 15.520000 | 15.740000 | 100.000000 | 1026.000000 | 0.44 | 15.520000 | 3.280000 | 1000.000000 | 310.000000 |  | 2.060000 | 501 | Rain | moderate rain | 10d | 20 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 16.520000 | 16.840000 | 100.000000 | 1025.000000 |  | 16.520000 | 1.380000 | 9000.000000 | 100.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 16.520000 | 16.840000 | 100.000000 | 1026.000000 | 0.58 | 16.520000 | 0.300000 | 9000.000000 | 100.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155220 | "VILLAMARIA - AUT [26155220]" | 5.048667 | -75.513889 | 1906.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-14 00:00:00 | NaT | Caldas | Villamaria | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 15.520000 | 15.740000 | 100.000000 | 1026.000000 | 0.99 | 15.520000 | 0.000000 | 7000.000000 | 0.000000 |  | 0.000000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26155220_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26155220_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26155220_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155220_OWM_Windspeed_20220111.png)
