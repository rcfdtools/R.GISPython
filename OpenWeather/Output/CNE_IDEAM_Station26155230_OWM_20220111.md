
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - EMAS - AUT [26155230] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26155230_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.08525,-75.50713889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.08525&lon=-75.50713889)


| Parameter | Value |
|---|---|
| Code | 26155230 |
| Name | EMAS - AUT [26155230] |
| Latitude, ° | 5.08525 |
| Longitude, ° | -75.50713889 |
| Elevation, m | 2211 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-06-10 00:00:00 |
| Suspension date | NaT |
| State | Caldas |
| County | Manizales |
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

### (CNE index 132) Open Weather values for station 26155230 - EMAS - AUT [26155230]

JSON data from API OWM:

```
{'lat': 5.0853, 'lon': -75.5071, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813238, 'sunset': 1641855884, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1026, 'humidity': 100, 'dew_point': 13.89, 'uvi': 3.28, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.46}}, 'hourly': [{'dt': 1641772800, 'temp': 16.96, 'feels_like': 17.24, 'pressure': 1016, 'humidity': 97, 'dew_point': 16.48, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.74, 'wind_deg': 102, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.63}}, {'dt': 1641776400, 'temp': 16.96, 'feels_like': 17.22, 'pressure': 1017, 'humidity': 96, 'dew_point': 16.32, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 101, 'wind_gust': 1.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 15.96, 'feels_like': 16.12, 'pressure': 1018, 'humidity': 96, 'dew_point': 15.32, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 105, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641783600, 'temp': 15.96, 'feels_like': 16.12, 'pressure': 1018, 'humidity': 96, 'dew_point': 15.32, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 108, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 14.96, 'feels_like': 15.02, 'pressure': 1018, 'humidity': 96, 'dew_point': 14.33, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 113, 'wind_gust': 0.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 14.96, 'feels_like': 15.04, 'pressure': 1017, 'humidity': 97, 'dew_point': 14.49, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 116, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.96, 'feels_like': 15.07, 'pressure': 1017, 'humidity': 98, 'dew_point': 14.65, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 146, 'wind_gust': 0.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.96, 'feels_like': 15.1, 'pressure': 1016, 'humidity': 99, 'dew_point': 14.8, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 126, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641801600, 'temp': 12.77, 'feels_like': 12.66, 'pressure': 1016, 'humidity': 98, 'dew_point': 12.46, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 151, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641805200, 'temp': 13.08, 'feels_like': 13, 'pressure': 1016, 'humidity': 98, 'dew_point': 12.77, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 168, 'wind_gust': 0.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641808800, 'temp': 13.96, 'feels_like': 13.97, 'pressure': 1017, 'humidity': 98, 'dew_point': 13.65, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 180, 'wind_gust': 0.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641812400, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1026, 'humidity': 100, 'dew_point': 13.89, 'uvi': 0, 'clouds': 75, 'visibility': 2000, 'wind_speed': 1.54, 'wind_deg': 120, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09n'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641816000, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1026, 'humidity': 100, 'dew_point': 13.89, 'uvi': 0.2, 'clouds': 75, 'visibility': 2000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1027, 'humidity': 100, 'dew_point': 13.89, 'uvi': 1.1, 'clouds': 75, 'visibility': 3000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 14.89, 'feels_like': 15.05, 'pressure': 1028, 'humidity': 100, 'dew_point': 14.89, 'uvi': 2.79, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641826800, 'temp': 16.89, 'feels_like': 17.09, 'pressure': 1028, 'humidity': 94, 'dew_point': 15.92, 'uvi': 4.85, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641830400, 'temp': 19.89, 'feels_like': 19.95, 'pressure': 1027, 'humidity': 77, 'dew_point': 15.74, 'uvi': 6.75, 'clouds': 75, 'visibility': 7000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641834000, 'temp': 16.89, 'feels_like': 17.09, 'pressure': 1027, 'humidity': 94, 'dew_point': 15.92, 'uvi': 7.49, 'clouds': 75, 'visibility': 6000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641837600, 'temp': 14.89, 'feels_like': 15.05, 'pressure': 1027, 'humidity': 100, 'dew_point': 14.89, 'uvi': 6.92, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.6}}, {'dt': 1641841200, 'temp': 14.89, 'feels_like': 15.05, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.89, 'uvi': 5.5, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.68}}, {'dt': 1641844800, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1026, 'humidity': 100, 'dew_point': 13.89, 'uvi': 3.28, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.46}}, {'dt': 1641848400, 'temp': 14.89, 'feels_like': 15.05, 'pressure': 1025, 'humidity': 100, 'dew_point': 14.89, 'uvi': 1.38, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641852000, 'temp': 14.89, 'feels_like': 15.05, 'pressure': 1026, 'humidity': 100, 'dew_point': 14.89, 'uvi': 0.3, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641855600, 'temp': 13.89, 'feels_like': 13.95, 'pressure': 1026, 'humidity': 100, 'dew_point': 13.89, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 00:00:00 | 70.000000 | 16.480000 | 17.240000 | 97.000000 | 1016.000000 | 0.63 | 16.960000 | 0.000000 | 10000.000000 | 102.000000 | 1.43 | 1.740000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 01:00:00 | 95.000000 | 16.320000 | 17.220000 | 96.000000 | 1017.000000 |  | 16.960000 | 0.000000 | 10000.000000 | 101.000000 | 1.35 | 1.680000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 02:00:00 | 87.000000 | 15.320000 | 16.120000 | 96.000000 | 1018.000000 | 0.29 | 15.960000 | 0.000000 | 10000.000000 | 105.000000 | 1.19 | 1.520000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 03:00:00 | 83.000000 | 15.320000 | 16.120000 | 96.000000 | 1018.000000 |  | 15.960000 | 0.000000 | 10000.000000 | 108.000000 | 0.89 | 1.200000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 04:00:00 | 78.000000 | 14.330000 | 15.020000 | 96.000000 | 1018.000000 |  | 14.960000 | 0.000000 | 10000.000000 | 113.000000 | 0.77 | 1.010000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 05:00:00 | 77.000000 | 14.490000 | 15.040000 | 97.000000 | 1017.000000 |  | 14.960000 | 0.000000 | 10000.000000 | 116.000000 | 0.66 | 0.820000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 06:00:00 | 56.000000 | 14.650000 | 15.070000 | 98.000000 | 1017.000000 |  | 14.960000 | 0.000000 | 10000.000000 | 146.000000 | 0.5 | 0.570000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 07:00:00 | 90.000000 | 14.800000 | 15.100000 | 99.000000 | 1016.000000 | 0.12 | 14.960000 | 0.000000 | 10000.000000 | 126.000000 | 0.66 | 0.820000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 12.460000 | 12.660000 | 98.000000 | 1016.000000 | 0.19 | 12.770000 | 0.000000 | 10000.000000 | 151.000000 | 0.67 | 0.610000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 09:00:00 | 96.000000 | 12.770000 | 13.000000 | 98.000000 | 1016.000000 | 0.21 | 13.080000 | 0.000000 | 10000.000000 | 168.000000 | 0.7 | 0.420000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 10:00:00 | 95.000000 | 13.650000 | 13.970000 | 98.000000 | 1017.000000 | 0.12 | 13.960000 | 0.000000 | 10000.000000 | 180.000000 | 0.81 | 0.470000 | 500 | Rain | light rain | 10n | 10 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 13.890000 | 13.950000 | 100.000000 | 1026.000000 | 0.11 | 13.890000 | 0.000000 | 2000.000000 | 120.000000 |  | 1.540000 | 301 | Drizzle | drizzle | 09n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 13.890000 | 13.950000 | 100.000000 | 1026.000000 |  | 13.890000 | 0.200000 | 2000.000000 | 290.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 12 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 13.890000 | 13.950000 | 100.000000 | 1027.000000 |  | 13.890000 | 1.100000 | 3000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 13 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 14.890000 | 15.050000 | 100.000000 | 1028.000000 |  | 14.890000 | 2.790000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 14 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 15.920000 | 17.090000 | 94.000000 | 1028.000000 |  | 16.890000 | 4.850000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 15 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 15.740000 | 19.950000 | 77.000000 | 1027.000000 |  | 19.890000 | 6.750000 | 7000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 16 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 15.920000 | 17.090000 | 94.000000 | 1027.000000 |  | 16.890000 | 7.490000 | 6000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 14.890000 | 15.050000 | 100.000000 | 1027.000000 | 0.6 | 14.890000 | 6.920000 | 1000.000000 | 300.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 14.890000 | 15.050000 | 100.000000 | 1026.000000 | 0.68 | 14.890000 | 5.500000 | 1000.000000 | 290.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 20:00:00 | 90.000000 | 13.890000 | 13.950000 | 100.000000 | 1026.000000 | 0.46 | 13.890000 | 3.280000 | 1000.000000 | 310.000000 |  | 2.060000 | 501 | Rain | moderate rain | 10d | 20 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 14.890000 | 15.050000 | 100.000000 | 1025.000000 |  | 14.890000 | 1.380000 | 9000.000000 | 100.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 14.890000 | 15.050000 | 100.000000 | 1026.000000 | 0.55 | 14.890000 | 0.300000 | 9000.000000 | 100.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155230 | "EMAS - AUT [26155230]" | 5.085250 | -75.507139 | 2211.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-06-10 00:00:00 | NaT | Caldas | Manizales | San Juan | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río Chinchiná | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 13.890000 | 13.950000 | 100.000000 | 1026.000000 | 0.99 | 13.890000 | 0.000000 | 7000.000000 | 0.000000 |  | 0.000000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26155230_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26155230_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26155230_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155230_OWM_Windspeed_20220111.png)
