
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PNN PURACE - AUT [26015030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26015030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.35684889,-76.40354444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.35684889&lon=-76.40354444)


| Parameter | Value |
|---|---|
| Code | 26015030 |
| Name | PNN PURACE - AUT [26015030] |
| Latitude, ° | 2.35684889 |
| Longitude, ° | -76.40354444 |
| Elevation, m | 3683 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2007-09-26 00:00:00 |
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

### (CNE index 1796) Open Weather values for station 26015030 - PNN PURACE - AUT [26015030]

JSON data from API OWM:

```
{'lat': 2.3568, 'lon': -76.4035, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813189, 'sunset': 1641856364, 'temp': 7.39, 'feels_like': 7.39, 'pressure': 1014, 'humidity': 95, 'dew_point': 6.64, 'uvi': 3.92, 'clouds': 100, 'visibility': 3494, 'wind_speed': 1.08, 'wind_deg': 287, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, 'hourly': [{'dt': 1641772800, 'temp': 5.44, 'feels_like': 5.44, 'pressure': 1017, 'humidity': 99, 'dew_point': 5.3, 'uvi': 0, 'clouds': 99, 'visibility': 3495, 'wind_speed': 0.3, 'wind_deg': 294, 'wind_gust': 0.91, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.41}}, {'dt': 1641776400, 'temp': 5.4, 'feels_like': 5.4, 'pressure': 1018, 'humidity': 99, 'dew_point': 5.26, 'uvi': 0, 'clouds': 100, 'visibility': 7751, 'wind_speed': 0.4, 'wind_deg': 289, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641780000, 'temp': 5.48, 'feels_like': 5.48, 'pressure': 1019, 'humidity': 99, 'dew_point': 5.34, 'uvi': 0, 'clouds': 99, 'visibility': 5001, 'wind_speed': 0.31, 'wind_deg': 302, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 5.48, 'feels_like': 5.48, 'pressure': 1019, 'humidity': 99, 'dew_point': 5.34, 'uvi': 0, 'clouds': 98, 'visibility': 4432, 'wind_speed': 0.19, 'wind_deg': 278, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641787200, 'temp': 5.4, 'feels_like': 5.4, 'pressure': 1019, 'humidity': 99, 'dew_point': 5.26, 'uvi': 0, 'clouds': 99, 'visibility': 3752, 'wind_speed': 0.32, 'wind_deg': 247, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641790800, 'temp': 5.36, 'feels_like': 5.36, 'pressure': 1018, 'humidity': 99, 'dew_point': 5.22, 'uvi': 0, 'clouds': 99, 'visibility': 6346, 'wind_speed': 0.02, 'wind_deg': 216, 'wind_gust': 0.54, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 5.12, 'feels_like': 5.12, 'pressure': 1017, 'humidity': 98, 'dew_point': 4.83, 'uvi': 0, 'clouds': 95, 'visibility': 4180, 'wind_speed': 0.25, 'wind_deg': 258, 'wind_gust': 0.47, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641798000, 'temp': 4.97, 'feels_like': 4.97, 'pressure': 1017, 'humidity': 99, 'dew_point': 4.83, 'uvi': 0, 'clouds': 100, 'visibility': 7127, 'wind_speed': 0.43, 'wind_deg': 275, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641801600, 'temp': 4.86, 'feels_like': 4.86, 'pressure': 1016, 'humidity': 99, 'dew_point': 4.72, 'uvi': 0, 'clouds': 100, 'visibility': 3377, 'wind_speed': 0.5, 'wind_deg': 271, 'wind_gust': 1.02, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.16}}, {'dt': 1641805200, 'temp': 4.82, 'feels_like': 4.82, 'pressure': 1016, 'humidity': 99, 'dew_point': 4.68, 'uvi': 0, 'clouds': 100, 'visibility': 4223, 'wind_speed': 0.56, 'wind_deg': 279, 'wind_gust': 1.04, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641808800, 'temp': 4.69, 'feels_like': 4.69, 'pressure': 1017, 'humidity': 99, 'dew_point': 4.55, 'uvi': 0, 'clouds': 100, 'visibility': 4566, 'wind_speed': 0.79, 'wind_deg': 300, 'wind_gust': 1.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.23}}, {'dt': 1641812400, 'temp': 4.6, 'feels_like': 4.6, 'pressure': 1018, 'humidity': 99, 'dew_point': 4.46, 'uvi': 0, 'clouds': 100, 'visibility': 4258, 'wind_speed': 0.9, 'wind_deg': 297, 'wind_gust': 1.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 5.14, 'feels_like': 5.14, 'pressure': 1018, 'humidity': 98, 'dew_point': 4.85, 'uvi': 0.26, 'clouds': 99, 'visibility': 3643, 'wind_speed': 0.85, 'wind_deg': 303, 'wind_gust': 1.51, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641819600, 'temp': 6.05, 'feels_like': 6.05, 'pressure': 1019, 'humidity': 96, 'dew_point': 5.46, 'uvi': 1.55, 'clouds': 100, 'visibility': 3069, 'wind_speed': 0.66, 'wind_deg': 308, 'wind_gust': 1.28, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641823200, 'temp': 7.05, 'feels_like': 7.05, 'pressure': 1019, 'humidity': 92, 'dew_point': 5.84, 'uvi': 3.88, 'clouds': 100, 'visibility': 7215, 'wind_speed': 0.66, 'wind_deg': 302, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641826800, 'temp': 8.03, 'feels_like': 8.03, 'pressure': 1019, 'humidity': 89, 'dew_point': 6.33, 'uvi': 6.73, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 292, 'wind_gust': 1.65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.58}}, {'dt': 1641830400, 'temp': 8.81, 'feels_like': 8.81, 'pressure': 1018, 'humidity': 88, 'dew_point': 6.93, 'uvi': 11.64, 'clouds': 100, 'visibility': 9917, 'wind_speed': 1.05, 'wind_deg': 305, 'wind_gust': 1.54, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.85}}, {'dt': 1641834000, 'temp': 8.67, 'feels_like': 8.67, 'pressure': 1017, 'humidity': 90, 'dew_point': 7.12, 'uvi': 12.98, 'clouds': 100, 'visibility': 7893, 'wind_speed': 1.02, 'wind_deg': 297, 'wind_gust': 1.46, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641837600, 'temp': 8.58, 'feels_like': 8.58, 'pressure': 1016, 'humidity': 91, 'dew_point': 7.2, 'uvi': 12.07, 'clouds': 96, 'visibility': 5865, 'wind_speed': 0.94, 'wind_deg': 293, 'wind_gust': 1.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.3}}, {'dt': 1641841200, 'temp': 8.23, 'feels_like': 8.23, 'pressure': 1015, 'humidity': 92, 'dew_point': 7.01, 'uvi': 6.43, 'clouds': 100, 'visibility': 6735, 'wind_speed': 0.99, 'wind_deg': 286, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.22}}, {'dt': 1641844800, 'temp': 7.39, 'feels_like': 7.39, 'pressure': 1014, 'humidity': 95, 'dew_point': 6.64, 'uvi': 3.92, 'clouds': 100, 'visibility': 3494, 'wind_speed': 1.08, 'wind_deg': 287, 'wind_gust': 1.75, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.14}}, {'dt': 1641848400, 'temp': 7.03, 'feels_like': 7.03, 'pressure': 1014, 'humidity': 96, 'dew_point': 6.44, 'uvi': 1.72, 'clouds': 100, 'visibility': 1006, 'wind_speed': 1.04, 'wind_deg': 272, 'wind_gust': 1.67, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641852000, 'temp': 6.6, 'feels_like': 6.6, 'pressure': 1015, 'humidity': 97, 'dew_point': 6.16, 'uvi': 0.54, 'clouds': 98, 'visibility': 1730, 'wind_speed': 0.96, 'wind_deg': 276, 'wind_gust': 1.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.87}}, {'dt': 1641855600, 'temp': 5.74, 'feels_like': 5.74, 'pressure': 1016, 'humidity': 99, 'dew_point': 5.6, 'uvi': 0, 'clouds': 95, 'visibility': 2968, 'wind_speed': 0.76, 'wind_deg': 282, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 00:00:00 | 99.000000 | 5.300000 | 5.440000 | 99.000000 | 1017.000000 | 0.41 | 5.440000 | 0.000000 | 3495.000000 | 294.000000 | 0.91 | 0.300000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 5.260000 | 5.400000 | 99.000000 | 1018.000000 | 0.3 | 5.400000 | 0.000000 | 7751.000000 | 289.000000 | 0.92 | 0.400000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 5.340000 | 5.480000 | 99.000000 | 1019.000000 | 0.12 | 5.480000 | 0.000000 | 5001.000000 | 302.000000 | 0.94 | 0.310000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 03:00:00 | 98.000000 | 5.340000 | 5.480000 | 99.000000 | 1019.000000 | 0.13 | 5.480000 | 0.000000 | 4432.000000 | 278.000000 | 0.83 | 0.190000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 5.260000 | 5.400000 | 99.000000 | 1019.000000 | 0.19 | 5.400000 | 0.000000 | 3752.000000 | 247.000000 | 0.76 | 0.320000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 5.220000 | 5.360000 | 99.000000 | 1018.000000 |  | 5.360000 | 0.000000 | 6346.000000 | 216.000000 | 0.54 | 0.020000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 06:00:00 | 95.000000 | 4.830000 | 5.120000 | 98.000000 | 1017.000000 | 0.19 | 5.120000 | 0.000000 | 4180.000000 | 258.000000 | 0.47 | 0.250000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 4.830000 | 4.970000 | 99.000000 | 1017.000000 | 0.22 | 4.970000 | 0.000000 | 7127.000000 | 275.000000 | 0.73 | 0.430000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 4.720000 | 4.860000 | 99.000000 | 1016.000000 | 0.16 | 4.860000 | 0.000000 | 3377.000000 | 271.000000 | 1.02 | 0.500000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 4.680000 | 4.820000 | 99.000000 | 1016.000000 | 0.18 | 4.820000 | 0.000000 | 4223.000000 | 279.000000 | 1.04 | 0.560000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 4.550000 | 4.690000 | 99.000000 | 1017.000000 | 0.23 | 4.690000 | 0.000000 | 4566.000000 | 300.000000 | 1.37 | 0.790000 | 500 | Rain | light rain | 10n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 4.460000 | 4.600000 | 99.000000 | 1018.000000 |  | 4.600000 | 0.000000 | 4258.000000 | 297.000000 | 1.67 | 0.900000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 4.850000 | 5.140000 | 98.000000 | 1018.000000 | 0.23 | 5.140000 | 0.260000 | 3643.000000 | 303.000000 | 1.51 | 0.850000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 5.460000 | 6.050000 | 96.000000 | 1019.000000 | 0.14 | 6.050000 | 1.550000 | 3069.000000 | 308.000000 | 1.28 | 0.660000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 5.840000 | 7.050000 | 92.000000 | 1019.000000 | 0.31 | 7.050000 | 3.880000 | 7215.000000 | 302.000000 | 1.3 | 0.660000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 6.330000 | 8.030000 | 89.000000 | 1019.000000 | 0.58 | 8.030000 | 6.730000 | 10000.000000 | 292.000000 | 1.65 | 1.050000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 16:00:00 | 100.000000 | 6.930000 | 8.810000 | 88.000000 | 1018.000000 | 0.85 | 8.810000 | 11.640000 | 9917.000000 | 305.000000 | 1.54 | 1.050000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 17:00:00 | 100.000000 | 7.120000 | 8.670000 | 90.000000 | 1017.000000 | 1.18 | 8.670000 | 12.980000 | 7893.000000 | 297.000000 | 1.46 | 1.020000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 18:00:00 | 96.000000 | 7.200000 | 8.580000 | 91.000000 | 1016.000000 | 1.3 | 8.580000 | 12.070000 | 5865.000000 | 293.000000 | 1.4 | 0.940000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 7.010000 | 8.230000 | 92.000000 | 1015.000000 | 1.22 | 8.230000 | 6.430000 | 6735.000000 | 286.000000 | 1.54 | 0.990000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 6.640000 | 7.390000 | 95.000000 | 1014.000000 | 1.14 | 7.390000 | 3.920000 | 3494.000000 | 287.000000 | 1.75 | 1.080000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 6.440000 | 7.030000 | 96.000000 | 1014.000000 | 1.18 | 7.030000 | 1.720000 | 1006.000000 | 272.000000 | 1.67 | 1.040000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 6.160000 | 6.600000 | 97.000000 | 1015.000000 | 0.87 | 6.600000 | 0.540000 | 1730.000000 | 276.000000 | 1.82 | 0.960000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26015030 | "PNN PURACE - AUT [26015030]" | 2.356849 | -76.403544 | 3683.000000 | Climática Principal | Automática con Telemetría | Activa | 2007-09-26 00:00:00 | NaT | Cauca | Puracé (Coconuco) | 0 | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Alto Río Cauca | America/Bogota | 2022-01-10 23:00:00 | 95.000000 | 5.600000 | 5.740000 | 99.000000 | 1016.000000 | 0.75 | 5.740000 | 0.000000 | 2968.000000 | 282.000000 | 1.52 | 0.760000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26015030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26015030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26015030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26015030_OWM_Windspeed_20220111.png)
