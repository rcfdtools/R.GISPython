
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CERROS NOROCCIDENTALES  - AUT [21215160] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21215160_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.47036111,-75.24386111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.47036111&lon=-75.24386111)


| Parameter | Value |
|---|---|
| Code | 21215160 |
| Name | CERROS NOROCCIDENTALES  - AUT [21215160] |
| Latitude, ° | 4.47036111 |
| Longitude, ° | -75.24386111 |
| Elevation, m | 1946 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-10-17 19:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Ibagué |
| Stream | 0 |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Coello |

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

### (CNE index 94) Open Weather values for station 21215160 - CERROS NOROCCIDENTALES  - AUT [21215160]

JSON data from API OWM:

```
{'lat': 4.4704, 'lon': -75.2439, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813116, 'sunset': 1641855881, 'temp': 18.9, 'feels_like': 18.75, 'pressure': 1016, 'humidity': 73, 'dew_point': 13.96, 'uvi': 4.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.17}}, 'hourly': [{'dt': 1641772800, 'temp': 16.96, 'feels_like': 16.75, 'pressure': 1016, 'humidity': 78, 'dew_point': 13.1, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1641776400, 'temp': 15.96, 'feels_like': 15.78, 'pressure': 1017, 'humidity': 83, 'dew_point': 13.08, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641780000, 'temp': 15.93, 'feels_like': 15.88, 'pressure': 1018, 'humidity': 88, 'dew_point': 13.95, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641783600, 'temp': 15.9, 'feels_like': 15.84, 'pressure': 1018, 'humidity': 88, 'dew_point': 13.92, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641787200, 'temp': 15.87, 'feels_like': 15.94, 'pressure': 1017, 'humidity': 93, 'dew_point': 14.74, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 310, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641790800, 'temp': 15.87, 'feels_like': 15.94, 'pressure': 1017, 'humidity': 93, 'dew_point': 14.74, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 323, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641794400, 'temp': 16.66, 'feels_like': 16.84, 'pressure': 1016, 'humidity': 94, 'dew_point': 15.69, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 307, 'wind_gust': 0.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 16.66, 'feels_like': 16.86, 'pressure': 1015, 'humidity': 95, 'dew_point': 15.86, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 309, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 15.04, 'feels_like': 15.08, 'pressure': 1015, 'humidity': 95, 'dew_point': 14.25, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 302, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641805200, 'temp': 14.42, 'feels_like': 14.4, 'pressure': 1015, 'humidity': 95, 'dew_point': 13.63, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 321, 'wind_gust': 1.13, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641808800, 'temp': 15.66, 'feels_like': 15.74, 'pressure': 1016, 'humidity': 94, 'dew_point': 14.7, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 322, 'wind_gust': 1.37, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 13.93, 'feels_like': 13.99, 'pressure': 1018, 'humidity': 100, 'dew_point': 13.93, 'uvi': 0, 'clouds': 75, 'visibility': 3000, 'wind_speed': 1.54, 'wind_deg': 90, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 14.9, 'feels_like': 15.06, 'pressure': 1019, 'humidity': 100, 'dew_point': 14.9, 'uvi': 0.2, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 14.93, 'feels_like': 15.09, 'pressure': 1020, 'humidity': 100, 'dew_point': 14.93, 'uvi': 1.15, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 14.99, 'feels_like': 15.16, 'pressure': 1021, 'humidity': 100, 'dew_point': 14.99, 'uvi': 2.85, 'clouds': 75, 'visibility': 8000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641826800, 'temp': 16.99, 'feels_like': 17.04, 'pressure': 1021, 'humidity': 88, 'dew_point': 14.99, 'uvi': 4.9, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641830400, 'temp': 17.93, 'feels_like': 17.95, 'pressure': 1020, 'humidity': 83, 'dew_point': 15, 'uvi': 10.26, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.82}}, {'dt': 1641834000, 'temp': 18.93, 'feels_like': 18.78, 'pressure': 1019, 'humidity': 73, 'dew_point': 13.99, 'uvi': 11.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 80, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.8}}, {'dt': 1641837600, 'temp': 19.9, 'feels_like': 19.75, 'pressure': 1018, 'humidity': 69, 'dew_point': 14.05, 'uvi': 10.39, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 70, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.64}}, {'dt': 1641841200, 'temp': 20.88, 'feels_like': 20.72, 'pressure': 1017, 'humidity': 65, 'dew_point': 14.06, 'uvi': 7.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 50, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641844800, 'temp': 18.9, 'feels_like': 18.75, 'pressure': 1016, 'humidity': 73, 'dew_point': 13.96, 'uvi': 4.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.17}}, {'dt': 1641848400, 'temp': 17.9, 'feels_like': 17.91, 'pressure': 1016, 'humidity': 83, 'dew_point': 14.97, 'uvi': 1.88, 'clouds': 90, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 40, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641852000, 'temp': 17.85, 'feels_like': 17.86, 'pressure': 1016, 'humidity': 83, 'dew_point': 14.93, 'uvi': 0.43, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.71}}, {'dt': 1641855600, 'temp': 16.82, 'feels_like': 16.86, 'pressure': 1017, 'humidity': 88, 'dew_point': 14.82, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 13.100000 | 16.750000 | 78.000000 | 1016.000000 | 0.42 | 16.960000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 13.080000 | 15.780000 | 83.000000 | 1017.000000 | 0.22 | 15.960000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 13.950000 | 15.880000 | 88.000000 | 1018.000000 | 0.25 | 15.930000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 13.920000 | 15.840000 | 88.000000 | 1018.000000 | 0.19 | 15.900000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 04:00:00 | 90.000000 | 14.740000 | 15.940000 | 93.000000 | 1017.000000 | 0.14 | 15.870000 | 0.000000 | 10000.000000 | 310.000000 | 1.17 | 1.450000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 05:00:00 | 91.000000 | 14.740000 | 15.940000 | 93.000000 | 1017.000000 | 0.12 | 15.870000 | 0.000000 | 10000.000000 | 323.000000 | 1.12 | 1.340000 | 500 | Rain | light rain | 10n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 06:00:00 | 73.000000 | 15.690000 | 16.840000 | 94.000000 | 1016.000000 |  | 16.660000 | 0.000000 | 10000.000000 | 307.000000 | 0.24 | 0.410000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 15.860000 | 16.860000 | 95.000000 | 1015.000000 |  | 16.660000 | 0.000000 | 10000.000000 | 309.000000 | 0.51 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 14.250000 | 15.080000 | 95.000000 | 1015.000000 | 0.14 | 15.040000 | 0.000000 | 10000.000000 | 302.000000 | 0.63 | 0.770000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 09:00:00 | 94.000000 | 13.630000 | 14.400000 | 95.000000 | 1015.000000 | 0.16 | 14.420000 | 0.000000 | 10000.000000 | 321.000000 | 1.13 | 1.430000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 10:00:00 | 96.000000 | 14.700000 | 15.740000 | 94.000000 | 1016.000000 |  | 15.660000 | 0.000000 | 10000.000000 | 322.000000 | 1.37 | 1.830000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 13.930000 | 13.990000 | 100.000000 | 1018.000000 |  | 13.930000 | 0.000000 | 3000.000000 | 90.000000 |  | 1.540000 | 701 | Mist | mist | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 14.900000 | 15.060000 | 100.000000 | 1019.000000 |  | 14.900000 | 0.200000 | 5000.000000 | 230.000000 |  | 1.540000 | 701 | Mist | mist | 50d | 12 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 14.930000 | 15.090000 | 100.000000 | 1020.000000 |  | 14.930000 | 1.150000 | 5000.000000 | 140.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 13 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 14.990000 | 15.160000 | 100.000000 | 1021.000000 | 0.24 | 14.990000 | 2.850000 | 8000.000000 | 360.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 14.990000 | 17.040000 | 88.000000 | 1021.000000 | 0.53 | 16.990000 | 4.900000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 15.000000 | 17.950000 | 83.000000 | 1020.000000 | 0.82 | 17.930000 | 10.260000 | 10000.000000 | 30.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 13.990000 | 18.780000 | 73.000000 | 1019.000000 | 0.8 | 18.930000 | 11.300000 | 10000.000000 | 80.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 14.050000 | 19.750000 | 69.000000 | 1018.000000 | 0.64 | 19.900000 | 10.390000 | 10000.000000 | 70.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 14.060000 | 20.720000 | 65.000000 | 1017.000000 | 1.18 | 20.880000 | 7.550000 | 10000.000000 | 50.000000 |  | 5.140000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 13.960000 | 18.750000 | 73.000000 | 1016.000000 | 1.17 | 18.900000 | 4.480000 | 10000.000000 | 60.000000 |  | 3.600000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 14.970000 | 17.910000 | 83.000000 | 1016.000000 | 1.14 | 17.900000 | 1.880000 | 10000.000000 | 40.000000 |  | 4.120000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 14.930000 | 17.860000 | 83.000000 | 1016.000000 | 0.71 | 17.850000 | 0.430000 | 10000.000000 | 20.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21215160 | "CERROS NOROCCIDENTALES  - AUT [21215160]" | 4.470361 | -75.243861 | 1946.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-10-17 19:00:00 | NaT | Tolima | Ibagué | 0 | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Coello | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 14.820000 | 16.860000 | 88.000000 | 1017.000000 | 0.99 | 16.820000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21215160_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21215160_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21215160_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21215160_OWM_Windspeed_20220111.png)
