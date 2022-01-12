
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CALARCA - AUT [26125300] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26125300_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.52830556,-75.59638889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.52830556&lon=-75.59638889)


| Parameter | Value |
|---|---|
| Code | 26125300 |
| Name | CALARCA - AUT [26125300] |
| Latitude, ° | 4.52830556 |
| Longitude, ° | -75.59638889 |
| Elevation, m | 2255 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-10-04 00:00:00 |
| Suspension date | NaT |
| State | Quindío |
| County | Calarcá |
| Stream | Otun |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Río La Vieja |

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

### (CNE index 101) Open Weather values for station 26125300 - CALARCA - AUT [26125300]

JSON data from API OWM:

```
{'lat': 4.5283, 'lon': -75.5964, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813206, 'sunset': 1641855960, 'temp': 16.14, 'feels_like': 16.11, 'pressure': 1013, 'humidity': 88, 'dew_point': 14.15, 'uvi': 4.89, 'clouds': 76, 'visibility': 9820, 'wind_speed': 1.46, 'wind_deg': 269, 'wind_gust': 1.76, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, 'hourly': [{'dt': 1641772800, 'temp': 16.15, 'feels_like': 16.33, 'pressure': 1015, 'humidity': 96, 'dew_point': 15.51, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 98, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.47}}, {'dt': 1641776400, 'temp': 15.38, 'feels_like': 15.48, 'pressure': 1016, 'humidity': 96, 'dew_point': 14.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 73, 'wind_gust': 0.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641780000, 'temp': 14.38, 'feels_like': 14.41, 'pressure': 1017, 'humidity': 97, 'dew_point': 13.91, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 89, 'wind_gust': 0.86, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 13.6, 'feels_like': 13.55, 'pressure': 1018, 'humidity': 97, 'dew_point': 13.13, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 90, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641787200, 'temp': 13.2, 'feels_like': 13.11, 'pressure': 1017, 'humidity': 97, 'dew_point': 12.73, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 103, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 13.2, 'feels_like': 13.11, 'pressure': 1017, 'humidity': 97, 'dew_point': 12.73, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 95, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.98, 'feels_like': 13.97, 'pressure': 1016, 'humidity': 97, 'dew_point': 13.51, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 99, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 13.98, 'feels_like': 13.97, 'pressure': 1015, 'humidity': 97, 'dew_point': 13.51, 'uvi': 0, 'clouds': 95, 'visibility': 7680, 'wind_speed': 0.07, 'wind_deg': 178, 'wind_gust': 0.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 11.92, 'feels_like': 11.73, 'pressure': 1015, 'humidity': 98, 'dew_point': 11.61, 'uvi': 0, 'clouds': 97, 'visibility': 8002, 'wind_speed': 0.21, 'wind_deg': 283, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641805200, 'temp': 12.01, 'feels_like': 11.83, 'pressure': 1015, 'humidity': 98, 'dew_point': 11.7, 'uvi': 0, 'clouds': 97, 'visibility': 7659, 'wind_speed': 0.33, 'wind_deg': 304, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641808800, 'temp': 12.98, 'feels_like': 12.89, 'pressure': 1016, 'humidity': 98, 'dew_point': 12.67, 'uvi': 0, 'clouds': 98, 'visibility': 8951, 'wind_speed': 0.51, 'wind_deg': 282, 'wind_gust': 1.23, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641812400, 'temp': 12.39, 'feels_like': 12.24, 'pressure': 1017, 'humidity': 98, 'dew_point': 12.08, 'uvi': 0, 'clouds': 98, 'visibility': 6589, 'wind_speed': 0.53, 'wind_deg': 281, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641816000, 'temp': 12.67, 'feels_like': 12.55, 'pressure': 1017, 'humidity': 98, 'dew_point': 12.36, 'uvi': 0.21, 'clouds': 83, 'visibility': 5360, 'wind_speed': 0.4, 'wind_deg': 280, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641819600, 'temp': 13.39, 'feels_like': 13.29, 'pressure': 1018, 'humidity': 96, 'dew_point': 12.77, 'uvi': 1.24, 'clouds': 100, 'visibility': 4848, 'wind_speed': 0.82, 'wind_deg': 271, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641823200, 'temp': 15.37, 'feels_like': 15.42, 'pressure': 1018, 'humidity': 94, 'dew_point': 14.41, 'uvi': 3.13, 'clouds': 100, 'visibility': 5799, 'wind_speed': 0.98, 'wind_deg': 277, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1641826800, 'temp': 16.84, 'feels_like': 16.96, 'pressure': 1018, 'humidity': 91, 'dew_point': 15.36, 'uvi': 5.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.06, 'wind_deg': 290, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641830400, 'temp': 16.13, 'feels_like': 15.99, 'pressure': 1017, 'humidity': 84, 'dew_point': 13.43, 'uvi': 9.7, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 287, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1641834000, 'temp': 16.87, 'feels_like': 16.7, 'pressure': 1015, 'humidity': 80, 'dew_point': 13.4, 'uvi': 10.76, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 275, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641837600, 'temp': 16.88, 'feels_like': 16.79, 'pressure': 1015, 'humidity': 83, 'dew_point': 13.98, 'uvi': 9.95, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 277, 'wind_gust': 1.58, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.94}}, {'dt': 1641841200, 'temp': 16.89, 'feels_like': 16.83, 'pressure': 1013, 'humidity': 84, 'dew_point': 14.17, 'uvi': 8.19, 'clouds': 71, 'visibility': 8401, 'wind_speed': 1.23, 'wind_deg': 274, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 1}}, {'dt': 1641844800, 'temp': 16.14, 'feels_like': 16.11, 'pressure': 1013, 'humidity': 88, 'dew_point': 14.15, 'uvi': 4.89, 'clouds': 76, 'visibility': 9820, 'wind_speed': 1.46, 'wind_deg': 269, 'wind_gust': 1.76, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, {'dt': 1641848400, 'temp': 15.67, 'feels_like': 15.62, 'pressure': 1013, 'humidity': 89, 'dew_point': 13.86, 'uvi': 2.08, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 278, 'wind_gust': 1.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.02}}, {'dt': 1641852000, 'temp': 13.43, 'feels_like': 13.23, 'pressure': 1014, 'humidity': 92, 'dew_point': 12.16, 'uvi': 0.3, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.95, 'wind_deg': 283, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.89}}, {'dt': 1641855600, 'temp': 12.23, 'feels_like': 11.99, 'pressure': 1015, 'humidity': 95, 'dew_point': 11.45, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 283, 'wind_gust': 0.97, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 00:00:00 | 87.000000 | 15.510000 | 16.330000 | 96.000000 | 1015.000000 | 0.47 | 16.150000 | 0.000000 | 10000.000000 | 98.000000 | 0.8 | 0.410000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 14.750000 | 15.480000 | 96.000000 | 1016.000000 | 0.29 | 15.380000 | 0.000000 | 10000.000000 | 73.000000 | 0.75 | 0.230000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 13.910000 | 14.410000 | 97.000000 | 1017.000000 | 0.15 | 14.380000 | 0.000000 | 10000.000000 | 89.000000 | 0.86 | 0.370000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 03:00:00 | 89.000000 | 13.130000 | 13.550000 | 97.000000 | 1018.000000 | 0.17 | 13.600000 | 0.000000 | 10000.000000 | 90.000000 | 0.85 | 0.390000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 04:00:00 | 82.000000 | 12.730000 | 13.110000 | 97.000000 | 1017.000000 |  | 13.200000 | 0.000000 | 10000.000000 | 103.000000 | 0.74 | 0.530000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 05:00:00 | 80.000000 | 12.730000 | 13.110000 | 97.000000 | 1017.000000 |  | 13.200000 | 0.000000 | 10000.000000 | 95.000000 | 0.7 | 0.570000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 06:00:00 | 61.000000 | 13.510000 | 13.970000 | 97.000000 | 1016.000000 |  | 13.980000 | 0.000000 | 10000.000000 | 99.000000 | 0.7 | 0.130000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 13.510000 | 13.970000 | 97.000000 | 1015.000000 |  | 13.980000 | 0.000000 | 7680.000000 | 178.000000 | 0.68 | 0.070000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 11.610000 | 11.730000 | 98.000000 | 1015.000000 | 0.15 | 11.920000 | 0.000000 | 8002.000000 | 283.000000 | 1.04 | 0.210000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 09:00:00 | 97.000000 | 11.700000 | 11.830000 | 98.000000 | 1015.000000 | 0.12 | 12.010000 | 0.000000 | 7659.000000 | 304.000000 | 1.05 | 0.330000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 12.670000 | 12.890000 | 98.000000 | 1016.000000 | 0.17 | 12.980000 | 0.000000 | 8951.000000 | 282.000000 | 1.23 | 0.510000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 12.080000 | 12.240000 | 98.000000 | 1017.000000 | 0.14 | 12.390000 | 0.000000 | 6589.000000 | 281.000000 | 1.44 | 0.530000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 12:00:00 | 83.000000 | 12.360000 | 12.550000 | 98.000000 | 1017.000000 | 0.12 | 12.670000 | 0.210000 | 5360.000000 | 280.000000 | 1.15 | 0.400000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 12.770000 | 13.290000 | 96.000000 | 1018.000000 | 0.2 | 13.390000 | 1.240000 | 4848.000000 | 271.000000 | 1.22 | 0.820000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 14.410000 | 15.420000 | 94.000000 | 1018.000000 | 0.22 | 15.370000 | 3.130000 | 5799.000000 | 277.000000 | 1 | 0.980000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 15.360000 | 16.960000 | 91.000000 | 1018.000000 | 0.38 | 16.840000 | 5.430000 | 10000.000000 | 290.000000 | 1.16 | 1.060000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 16:00:00 | 99.000000 | 13.430000 | 15.990000 | 84.000000 | 1017.000000 | 0.27 | 16.130000 | 9.700000 | 10000.000000 | 287.000000 | 1.12 | 1.350000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 17:00:00 | 93.000000 | 13.400000 | 16.700000 | 80.000000 | 1015.000000 | 0.54 | 16.870000 | 10.760000 | 10000.000000 | 275.000000 | 1.58 | 1.700000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 18:00:00 | 56.000000 | 13.980000 | 16.790000 | 83.000000 | 1015.000000 | 0.94 | 16.880000 | 9.950000 | 10000.000000 | 277.000000 | 1.58 | 1.380000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 19:00:00 | 71.000000 | 14.170000 | 16.830000 | 84.000000 | 1013.000000 | 1 | 16.890000 | 8.190000 | 8401.000000 | 274.000000 | 1.44 | 1.230000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 20:00:00 | 76.000000 | 14.150000 | 16.110000 | 88.000000 | 1013.000000 | 1.22 | 16.140000 | 4.890000 | 9820.000000 | 269.000000 | 1.76 | 1.460000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 21:00:00 | 80.000000 | 13.860000 | 15.620000 | 89.000000 | 1013.000000 | 1.02 | 15.670000 | 2.080000 | 10000.000000 | 278.000000 | 1.35 | 1.040000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 22:00:00 | 85.000000 | 12.160000 | 13.230000 | 92.000000 | 1014.000000 | 0.89 | 13.430000 | 0.300000 | 10000.000000 | 283.000000 | 1.43 | 0.950000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26125300 | "CALARCA - AUT [26125300]" | 4.528306 | -75.596389 | 2255.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-10-04 00:00:00 | NaT | Quindío | Calarcá | Otun | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Río La Vieja | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 11.450000 | 11.990000 | 95.000000 | 1015.000000 | 1.14 | 12.230000 | 0.000000 | 10000.000000 | 283.000000 | 0.97 | 0.340000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26125300_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26125300_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26125300_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26125300_OWM_Windspeed_20220111.png)
