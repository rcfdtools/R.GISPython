
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PALETARA  - AUT [26015050] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26015050_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.19172222,-76.48202778) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.19172222&lon=-76.48202778)


| Parameter | Value |
|---|---|
| Code | 26015050 |
| Name | PALETARA  - AUT [26015050] |
| Latitude, ° | 2.19172222 |
| Longitude, ° | -76.48202778 |
| Elevation, m | 3009 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2011-12-20 00:00:00 |
| Suspension date | NaT |
| State | Cauca |
| County | Puracé (Coconuco) |
| Stream | 0 |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Alto Río Cauca |

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

### (CNE index 1915) Open Weather values for station 26015050 - PALETARA  - AUT [26015050]

JSON data from API OWM:

```
{'lat': 2.1917, 'lon': -76.482, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813192, 'sunset': 1641856398, 'temp': 11.22, 'feels_like': 10.88, 'pressure': 1015, 'humidity': 95, 'dew_point': 10.45, 'uvi': 3.92, 'clouds': 100, 'visibility': 2724, 'wind_speed': 1.22, 'wind_deg': 295, 'wind_gust': 1.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, 'hourly': [{'dt': 1641772800, 'temp': 9.65, 'feels_like': 9.65, 'pressure': 1017, 'humidity': 99, 'dew_point': 9.5, 'uvi': 0, 'clouds': 100, 'visibility': 4429, 'wind_speed': 0.47, 'wind_deg': 292, 'wind_gust': 0.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641776400, 'temp': 9.66, 'feels_like': 9.66, 'pressure': 1018, 'humidity': 99, 'dew_point': 9.51, 'uvi': 0, 'clouds': 100, 'visibility': 5829, 'wind_speed': 0.63, 'wind_deg': 295, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641780000, 'temp': 9.64, 'feels_like': 9.64, 'pressure': 1019, 'humidity': 99, 'dew_point': 9.49, 'uvi': 0, 'clouds': 100, 'visibility': 4794, 'wind_speed': 0.62, 'wind_deg': 295, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.17}}, {'dt': 1641783600, 'temp': 9.54, 'feels_like': 9.54, 'pressure': 1019, 'humidity': 99, 'dew_point': 9.39, 'uvi': 0, 'clouds': 100, 'visibility': 4013, 'wind_speed': 0.45, 'wind_deg': 287, 'wind_gust': 0.95, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 9.4, 'feels_like': 9.4, 'pressure': 1019, 'humidity': 99, 'dew_point': 9.25, 'uvi': 0, 'clouds': 100, 'visibility': 1322, 'wind_speed': 0.47, 'wind_deg': 268, 'wind_gust': 0.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641790800, 'temp': 9.39, 'feels_like': 9.39, 'pressure': 1018, 'humidity': 99, 'dew_point': 9.24, 'uvi': 0, 'clouds': 100, 'visibility': 1017, 'wind_speed': 0.25, 'wind_deg': 292, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 9, 'feels_like': 9, 'pressure': 1018, 'humidity': 99, 'dew_point': 8.85, 'uvi': 0, 'clouds': 100, 'visibility': 2730, 'wind_speed': 0.32, 'wind_deg': 273, 'wind_gust': 0.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641798000, 'temp': 8.8, 'feels_like': 8.8, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.65, 'uvi': 0, 'clouds': 100, 'visibility': 2609, 'wind_speed': 0.58, 'wind_deg': 296, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641801600, 'temp': 8.73, 'feels_like': 8.73, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.58, 'uvi': 0, 'clouds': 100, 'visibility': 2096, 'wind_speed': 0.67, 'wind_deg': 287, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641805200, 'temp': 8.8, 'feels_like': 8.8, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.65, 'uvi': 0, 'clouds': 100, 'visibility': 2174, 'wind_speed': 0.68, 'wind_deg': 294, 'wind_gust': 1.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641808800, 'temp': 8.73, 'feels_like': 8.73, 'pressure': 1017, 'humidity': 99, 'dew_point': 8.58, 'uvi': 0, 'clouds': 100, 'visibility': 2256, 'wind_speed': 0.94, 'wind_deg': 305, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641812400, 'temp': 8.59, 'feels_like': 8.59, 'pressure': 1018, 'humidity': 99, 'dew_point': 8.44, 'uvi': 0, 'clouds': 100, 'visibility': 1704, 'wind_speed': 1.06, 'wind_deg': 303, 'wind_gust': 1.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 9.11, 'feels_like': 9.11, 'pressure': 1018, 'humidity': 98, 'dew_point': 8.81, 'uvi': 0.26, 'clouds': 98, 'visibility': 3252, 'wind_speed': 1.03, 'wind_deg': 310, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641819600, 'temp': 9.89, 'feels_like': 9.89, 'pressure': 1019, 'humidity': 96, 'dew_point': 9.28, 'uvi': 1.55, 'clouds': 100, 'visibility': 3921, 'wind_speed': 0.83, 'wind_deg': 305, 'wind_gust': 1.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.51, 'feels_like': 10.07, 'pressure': 1020, 'humidity': 94, 'dew_point': 9.59, 'uvi': 3.88, 'clouds': 100, 'visibility': 4867, 'wind_speed': 0.83, 'wind_deg': 315, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.27}}, {'dt': 1641826800, 'temp': 11.47, 'feels_like': 11.05, 'pressure': 1019, 'humidity': 91, 'dew_point': 10.05, 'uvi': 6.73, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 303, 'wind_gust': 1.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641830400, 'temp': 12.55, 'feels_like': 12.18, 'pressure': 1018, 'humidity': 89, 'dew_point': 10.79, 'uvi': 11.64, 'clouds': 100, 'visibility': 8830, 'wind_speed': 1.34, 'wind_deg': 305, 'wind_gust': 1.77, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641834000, 'temp': 12.6, 'feels_like': 12.29, 'pressure': 1017, 'humidity': 91, 'dew_point': 11.17, 'uvi': 12.98, 'clouds': 100, 'visibility': 7759, 'wind_speed': 1.06, 'wind_deg': 304, 'wind_gust': 1.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.15}}, {'dt': 1641837600, 'temp': 12.2, 'feels_like': 11.88, 'pressure': 1016, 'humidity': 92, 'dew_point': 10.94, 'uvi': 12.07, 'clouds': 94, 'visibility': 7889, 'wind_speed': 1.04, 'wind_deg': 308, 'wind_gust': 1.42, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.19}}, {'dt': 1641841200, 'temp': 11.88, 'feels_like': 11.55, 'pressure': 1015, 'humidity': 93, 'dew_point': 10.79, 'uvi': 6.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 300, 'wind_gust': 1.49, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.07}}, {'dt': 1641844800, 'temp': 11.22, 'feels_like': 10.88, 'pressure': 1015, 'humidity': 95, 'dew_point': 10.45, 'uvi': 3.92, 'clouds': 100, 'visibility': 2724, 'wind_speed': 1.22, 'wind_deg': 295, 'wind_gust': 1.87, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.08}}, {'dt': 1641848400, 'temp': 10.82, 'feels_like': 10.46, 'pressure': 1015, 'humidity': 96, 'dew_point': 10.21, 'uvi': 1.72, 'clouds': 100, 'visibility': 2540, 'wind_speed': 1.14, 'wind_deg': 288, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641852000, 'temp': 10.44, 'feels_like': 10.07, 'pressure': 1015, 'humidity': 97, 'dew_point': 9.98, 'uvi': 0.54, 'clouds': 99, 'visibility': 4002, 'wind_speed': 1.09, 'wind_deg': 293, 'wind_gust': 1.79, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.67}}, {'dt': 1641855600, 'temp': 9.67, 'feels_like': 9.67, 'pressure': 1016, 'humidity': 99, 'dew_point': 9.52, 'uvi': 0, 'clouds': 98, 'visibility': 3221, 'wind_speed': 0.97, 'wind_deg': 296, 'wind_gust': 1.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 9.500000 | 9.650000 | 99.000000 | 1017.000000 | 0.37 | 9.650000 | 0.000000 | 4429.000000 | 292.000000 | 0.79 | 0.470000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 9.510000 | 9.660000 | 99.000000 | 1018.000000 | 0.23 | 9.660000 | 0.000000 | 5829.000000 | 295.000000 | 0.88 | 0.630000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 9.490000 | 9.640000 | 99.000000 | 1019.000000 | 0.17 | 9.640000 | 0.000000 | 4794.000000 | 295.000000 | 1.01 | 0.620000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 9.390000 | 9.540000 | 99.000000 | 1019.000000 | 0.12 | 9.540000 | 0.000000 | 4013.000000 | 287.000000 | 0.95 | 0.450000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 9.250000 | 9.400000 | 99.000000 | 1019.000000 | 0.22 | 9.400000 | 0.000000 | 1322.000000 | 268.000000 | 0.89 | 0.470000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 9.240000 | 9.390000 | 99.000000 | 1018.000000 |  | 9.390000 | 0.000000 | 1017.000000 | 292.000000 | 0.52 | 0.250000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 8.850000 | 9.000000 | 99.000000 | 1018.000000 | 0.19 | 9.000000 | 0.000000 | 2730.000000 | 273.000000 | 0.54 | 0.320000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 8.650000 | 8.800000 | 99.000000 | 1017.000000 | 0.23 | 8.800000 | 0.000000 | 2609.000000 | 296.000000 | 0.9 | 0.580000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 8.580000 | 8.730000 | 99.000000 | 1017.000000 | 0.13 | 8.730000 | 0.000000 | 2096.000000 | 287.000000 | 1.14 | 0.670000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 8.650000 | 8.800000 | 99.000000 | 1017.000000 | 0.13 | 8.800000 | 0.000000 | 2174.000000 | 294.000000 | 1.25 | 0.680000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 8.580000 | 8.730000 | 99.000000 | 1017.000000 | 0.16 | 8.730000 | 0.000000 | 2256.000000 | 305.000000 | 1.65 | 0.940000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 8.440000 | 8.590000 | 99.000000 | 1018.000000 |  | 8.590000 | 0.000000 | 1704.000000 | 303.000000 | 1.88 | 1.060000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 12:00:00 | 98.000000 | 8.810000 | 9.110000 | 98.000000 | 1018.000000 | 0.24 | 9.110000 | 0.260000 | 3252.000000 | 310.000000 | 1.71 | 1.030000 | 500 | Rain | light rain | 10d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 9.280000 | 9.890000 | 96.000000 | 1019.000000 |  | 9.890000 | 1.550000 | 3921.000000 | 305.000000 | 1.58 | 0.830000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 9.590000 | 10.070000 | 94.000000 | 1020.000000 | 0.27 | 10.510000 | 3.880000 | 4867.000000 | 315.000000 | 1.37 | 0.830000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 10.050000 | 11.050000 | 91.000000 | 1019.000000 | 0.45 | 11.470000 | 6.730000 | 10000.000000 | 303.000000 | 1.83 | 1.280000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 10.790000 | 12.180000 | 89.000000 | 1018.000000 | 0.72 | 12.550000 | 11.640000 | 8830.000000 | 305.000000 | 1.77 | 1.340000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 11.170000 | 12.290000 | 91.000000 | 1017.000000 | 1.15 | 12.600000 | 12.980000 | 7759.000000 | 304.000000 | 1.51 | 1.060000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 18:00:00 | 94.000000 | 10.940000 | 11.880000 | 92.000000 | 1016.000000 | 1.19 | 12.200000 | 12.070000 | 7889.000000 | 308.000000 | 1.42 | 1.040000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 10.790000 | 11.550000 | 93.000000 | 1015.000000 | 1.07 | 11.880000 | 6.430000 | 10000.000000 | 300.000000 | 1.49 | 1.150000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 10.450000 | 10.880000 | 95.000000 | 1015.000000 | 1.08 | 11.220000 | 3.920000 | 2724.000000 | 295.000000 | 1.87 | 1.220000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 10.210000 | 10.460000 | 96.000000 | 1015.000000 | 0.96 | 10.820000 | 1.720000 | 2540.000000 | 288.000000 | 1.66 | 1.140000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 22:00:00 | 99.000000 | 9.980000 | 10.070000 | 97.000000 | 1015.000000 | 0.67 | 10.440000 | 0.540000 | 4002.000000 | 293.000000 | 1.79 | 1.090000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015050 | "PALETARA  - AUT [26015050]" | 2.191722 | -76.482028 | 3009.000000 | Climática Principal | Automática con Telemetría | Activa | 2011-12-20 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 9.520000 | 9.670000 | 99.000000 | 1016.000000 | 0.48 | 9.670000 | 0.000000 | 3221.000000 | 296.000000 | 1.84 | 0.970000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26015050_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26015050_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26015050_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015050_OWM_Windspeed_20220111.png)
