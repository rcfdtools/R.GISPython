
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LAS BRISAS - AUT [26155150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26155150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.93452778,-75.35038889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.93452778&lon=-75.35038889)


| Parameter | Value |
|---|---|
| Code | 26155150 |
| Name | LAS BRISAS - AUT [26155150] |
| Latitude, ° | 4.93452778 |
| Longitude, ° | -75.35038889 |
| Elevation, m | 4133 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1981-10-14 19:00:00 |
| Suspension date | NaT |
| State | Caldas |
| County | Villamaria |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Gualí |

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

### (CNE index 318) Open Weather values for station 26155150 - LAS BRISAS - AUT [26155150]

JSON data from API OWM:

```
{'lat': 4.9345, 'lon': -75.3504, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813186, 'sunset': 1641855861, 'temp': 0.98, 'feels_like': -1.39, 'pressure': 1026, 'humidity': 100, 'dew_point': 0.98, 'uvi': 3, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.6}}, 'hourly': [{'dt': 1641772800, 'temp': 3.69, 'feels_like': 3.69, 'pressure': 1018, 'humidity': 97, 'dew_point': 3.26, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 60, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.36}}, {'dt': 1641776400, 'temp': 3.69, 'feels_like': 3.69, 'pressure': 1019, 'humidity': 95, 'dew_point': 2.96, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.43, 'wind_deg': 61, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641780000, 'temp': 2.69, 'feels_like': 2.69, 'pressure': 1020, 'humidity': 96, 'dew_point': 2.12, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 92, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641783600, 'temp': 2.69, 'feels_like': 2.69, 'pressure': 1020, 'humidity': 95, 'dew_point': 1.97, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 248, 'wind_gust': 0.83, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 1.69, 'feels_like': 1.69, 'pressure': 1020, 'humidity': 95, 'dew_point': 0.98, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.32, 'wind_deg': 245, 'wind_gust': 0.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 1.69, 'feels_like': 1.69, 'pressure': 1019, 'humidity': 96, 'dew_point': 1.12, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 229, 'wind_gust': 0.69, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 1.69, 'feels_like': 1.69, 'pressure': 1018, 'humidity': 96, 'dew_point': 1.12, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 243, 'wind_gust': 0.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 1.69, 'feels_like': 1.69, 'pressure': 1018, 'humidity': 96, 'dew_point': 1.12, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 204, 'wind_gust': 0.84, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 0.08, 'feels_like': 0.08, 'pressure': 1018, 'humidity': 96, 'dew_point': -0.42, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 234, 'wind_gust': 0.94, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'snow': {'1h': 0.11}}, {'dt': 1641805200, 'temp': 0.06, 'feels_like': 0.06, 'pressure': 1018, 'humidity': 96, 'dew_point': -0.44, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 248, 'wind_gust': 0.99, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 0.69, 'feels_like': 0.69, 'pressure': 1018, 'humidity': 96, 'dew_point': 0.13, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 250, 'wind_gust': 1.52, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 0.63, 'feels_like': -1.1, 'pressure': 1026, 'humidity': 100, 'dew_point': 0.63, 'uvi': 0, 'clouds': 75, 'visibility': 2000, 'wind_speed': 1.54, 'wind_deg': 120, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09n'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 0.75, 'feels_like': -1.65, 'pressure': 1026, 'humidity': 100, 'dew_point': 0.75, 'uvi': 0.14, 'clouds': 75, 'visibility': 2000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 0.75, 'feels_like': 0.75, 'pressure': 1027, 'humidity': 100, 'dew_point': 0.75, 'uvi': 1.92, 'clouds': 75, 'visibility': 3000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 1.87, 'feels_like': 1.87, 'pressure': 1028, 'humidity': 100, 'dew_point': 1.87, 'uvi': 4.8, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641826800, 'temp': 3.63, 'feels_like': 3.63, 'pressure': 1028, 'humidity': 94, 'dew_point': 2.76, 'uvi': 8.25, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641830400, 'temp': 6.27, 'feels_like': 3.1, 'pressure': 1027, 'humidity': 77, 'dew_point': 2.54, 'uvi': 9.29, 'clouds': 75, 'visibility': 7000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641834000, 'temp': 3.63, 'feels_like': -0.18, 'pressure': 1027, 'humidity': 94, 'dew_point': 2.76, 'uvi': 10.23, 'clouds': 75, 'visibility': 6000, 'wind_speed': 4.63, 'wind_deg': 290, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641837600, 'temp': 1.87, 'feels_like': -1.71, 'pressure': 1027, 'humidity': 100, 'dew_point': 1.87, 'uvi': 9.4, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}, {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641841200, 'temp': 1.87, 'feels_like': -1.71, 'pressure': 1026, 'humidity': 100, 'dew_point': 1.87, 'uvi': 5.06, 'clouds': 90, 'visibility': 1000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.62}}, {'dt': 1641844800, 'temp': 0.98, 'feels_like': -1.39, 'pressure': 1026, 'humidity': 100, 'dew_point': 0.98, 'uvi': 3, 'clouds': 90, 'visibility': 1000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}], 'rain': {'1h': 0.6}}, {'dt': 1641848400, 'temp': 1.98, 'feels_like': -0.22, 'pressure': 1025, 'humidity': 100, 'dew_point': 1.98, 'uvi': 1.25, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1641852000, 'temp': 1.63, 'feels_like': -0.63, 'pressure': 1026, 'humidity': 100, 'dew_point': 1.63, 'uvi': 0.4, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 100, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641855600, 'temp': 0.87, 'feels_like': 0.87, 'pressure': 1026, 'humidity': 100, 'dew_point': 0.87, 'uvi': 0, 'clouds': 75, 'visibility': 7000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 00:00:00 | 69.000000 | 3.260000 | 3.690000 | 97.000000 | 1018.000000 | 0.36 | 3.690000 | 0.000000 | 10000.000000 | 60.000000 | 0.98 | 0.370000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 01:00:00 | 97.000000 | 2.960000 | 3.690000 | 95.000000 | 1019.000000 | 0.11 | 3.690000 | 0.000000 | 10000.000000 | 61.000000 | 0.86 | 0.430000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 02:00:00 | 96.000000 | 2.120000 | 2.690000 | 96.000000 | 1020.000000 | 0.13 | 2.690000 | 0.000000 | 10000.000000 | 92.000000 | 0.89 | 0.120000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 1.970000 | 2.690000 | 95.000000 | 1020.000000 |  | 2.690000 | 0.000000 | 10000.000000 | 248.000000 | 0.83 | 0.190000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 04:00:00 | 94.000000 | 0.980000 | 1.690000 | 95.000000 | 1020.000000 |  | 1.690000 | 0.000000 | 10000.000000 | 245.000000 | 0.8 | 0.320000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 1.120000 | 1.690000 | 96.000000 | 1019.000000 |  | 1.690000 | 0.000000 | 10000.000000 | 229.000000 | 0.69 | 0.440000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 06:00:00 | 33.000000 | 1.120000 | 1.690000 | 96.000000 | 1018.000000 |  | 1.690000 | 0.000000 | 10000.000000 | 243.000000 | 0.73 | 0.460000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 07:00:00 | 51.000000 | 1.120000 | 1.690000 | 96.000000 | 1018.000000 |  | 1.690000 | 0.000000 | 10000.000000 | 204.000000 | 0.84 | 0.370000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![13n.png](http://openweathermap.org/img/w/13n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 08:00:00 | 60.000000 | -0.420000 | 0.080000 | 96.000000 | 1018.000000 |  | 0.080000 | 0.000000 | 10000.000000 | 234.000000 | 0.94 | 0.560000 | 600 | Snow | light snow | 13n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 09:00:00 | 62.000000 | -0.440000 | 0.060000 | 96.000000 | 1018.000000 |  | 0.060000 | 0.000000 | 10000.000000 | 248.000000 | 0.99 | 0.830000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 10:00:00 | 71.000000 | 0.130000 | 0.690000 | 96.000000 | 1018.000000 |  | 0.690000 | 0.000000 | 10000.000000 | 250.000000 | 1.52 | 1.080000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![09n.png](http://openweathermap.org/img/w/09n.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 0.630000 | -1.100000 | 100.000000 | 1026.000000 |  | 0.630000 | 0.000000 | 2000.000000 | 120.000000 |  | 1.540000 | 301 | Drizzle | drizzle | 09n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 0.750000 | -1.650000 | 100.000000 | 1026.000000 |  | 0.750000 | 0.140000 | 2000.000000 | 290.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 12 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 0.750000 | 0.750000 | 100.000000 | 1027.000000 |  | 0.750000 | 1.920000 | 3000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 13 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 1.870000 | 1.870000 | 100.000000 | 1028.000000 |  | 1.870000 | 4.800000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 14 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 2.760000 | 3.630000 | 94.000000 | 1028.000000 |  | 3.630000 | 8.250000 | 7000.000000 | 0.000000 |  | 0.000000 | 741 | Fog | fog | 50d | 15 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 2.540000 | 3.100000 | 77.000000 | 1027.000000 |  | 6.270000 | 9.290000 | 7000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 16 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 2.760000 | -0.180000 | 94.000000 | 1027.000000 |  | 3.630000 | 10.230000 | 6000.000000 | 290.000000 |  | 4.630000 | 741 | Fog | fog | 50d | 17 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 1.870000 | -1.710000 | 100.000000 | 1027.000000 | 0.73 | 1.870000 | 9.400000 | 1000.000000 | 300.000000 |  | 3.600000 | 741 | Fog | fog | 50d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 19:00:00 | 90.000000 | 1.870000 | -1.710000 | 100.000000 | 1026.000000 | 0.62 | 1.870000 | 5.060000 | 1000.000000 | 290.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 20:00:00 | 90.000000 | 0.980000 | -1.390000 | 100.000000 | 1026.000000 | 0.6 | 0.980000 | 3.000000 | 1000.000000 | 310.000000 |  | 2.060000 | 501 | Rain | moderate rain | 10d | 20 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 1.980000 | -0.220000 | 100.000000 | 1025.000000 |  | 1.980000 | 1.250000 | 9000.000000 | 100.000000 |  | 2.060000 | 741 | Fog | fog | 50d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 1.630000 | -0.630000 | 100.000000 | 1026.000000 | 0.43 | 1.630000 | 0.400000 | 9000.000000 | 100.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26155150 | "LAS BRISAS - AUT [26155150]" | 4.934528 | -75.350389 | 4133.000000 | Climática Principal | Automática con Telemetría | Activa | 1981-10-14 19:00:00 | NaT | Caldas | Villamaria | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Medio Magdalena | Río Gualí | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 0.870000 | 0.870000 | 100.000000 | 1026.000000 | 0.58 | 0.870000 | 0.000000 | 7000.000000 | 0.000000 |  | 0.000000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26155150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26155150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26155150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26155150_OWM_Windspeed_20220111.png)
