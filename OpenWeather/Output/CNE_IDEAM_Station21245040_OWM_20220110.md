
## Weather values for the IDEAM national station catalog - CNE from OWM https://openweathermap.org - AEROPUERTO PERALES [21245040]

### General parameters

* Current date time: 2022-01-10 17:28:01.133661
* Unix time to eval: 1641749281
* Show historical: True
* Show yesterday: True
* Show OWM API detail: True
* Request OWM data: True
* Days before: 1
* Unit system: metric
* Icons from: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220110.xls
* CNE IDEAM stations: 4489
* CNE IDEAM attributes: 19
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21245040_OWM_20220110.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220110.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.42413889,-75.13941667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.42413889&lon=-75.13941667)


| Parameter | Value |
|---|---|
| Code | 21245040 |
| Name | AEROPUERTO PERALES [21245040] |
| Latitude, ° | 4.42413889 |
| Longitude, ° | -75.13941667 |
| Elevation, m | 943 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1970-11-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Ibagué |
| Stream | Meta |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Opía |

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
| Julian | N/A | N/A | Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API

### 2192 - Open Weather values for station 000021245040: AEROPUERTO PERALES [21245040]

JSON data from API OWM:

```
{'lat': 4.4241, 'lon': -75.1394, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641749281, 'sunrise': 1641726665, 'sunset': 1641769433, 'temp': 25.91, 'feels_like': 26.36, 'pressure': 1020, 'humidity': 69, 'dew_point': 19.79, 'uvi': 10.22, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 90, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, 'hourly': [{'dt': 1641686400, 'temp': 23.91, 'feels_like': 24.26, 'pressure': 1018, 'humidity': 73, 'dew_point': 18.78, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 20, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641690000, 'temp': 21.91, 'feels_like': 22.32, 'pressure': 1019, 'humidity': 83, 'dew_point': 18.89, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641693600, 'temp': 21.91, 'feels_like': 22.45, 'pressure': 1020, 'humidity': 88, 'dew_point': 19.83, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641697200, 'temp': 21.91, 'feels_like': 22.45, 'pressure': 1020, 'humidity': 88, 'dew_point': 19.83, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641700800, 'temp': 21.88, 'feels_like': 22.19, 'pressure': 1017, 'humidity': 79, 'dew_point': 18.08, 'uvi': 0, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.35, 'wind_deg': 326, 'wind_gust': 1.81, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641704400, 'temp': 21.88, 'feels_like': 22.19, 'pressure': 1017, 'humidity': 79, 'dew_point': 18.08, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 328, 'wind_gust': 1.65, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641708000, 'temp': 19.32, 'feels_like': 19.42, 'pressure': 1016, 'humidity': 81, 'dew_point': 15.98, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.97, 'wind_deg': 325, 'wind_gust': 1.52, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641711600, 'temp': 19.15, 'feels_like': 19.26, 'pressure': 1015, 'humidity': 82, 'dew_point': 16.01, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 322, 'wind_gust': 1.33, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641715200, 'temp': 19.02, 'feels_like': 19.12, 'pressure': 1015, 'humidity': 82, 'dew_point': 15.88, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 326, 'wind_gust': 1.22, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641718800, 'temp': 18.77, 'feels_like': 18.9, 'pressure': 1015, 'humidity': 84, 'dew_point': 16.01, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.39, 'wind_deg': 325, 'wind_gust': 1.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641722400, 'temp': 18.78, 'feels_like': 18.88, 'pressure': 1016, 'humidity': 83, 'dew_point': 15.83, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 316, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641726000, 'temp': 18.91, 'feels_like': 19, 'pressure': 1020, 'humidity': 82, 'dew_point': 15.77, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641729600, 'temp': 19.91, 'feels_like': 19.86, 'pressure': 1020, 'humidity': 73, 'dew_point': 14.93, 'uvi': 0.42, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 290, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641733200, 'temp': 19.91, 'feels_like': 19.86, 'pressure': 1020, 'humidity': 73, 'dew_point': 14.93, 'uvi': 1.05, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 290, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641736800, 'temp': 24.91, 'feels_like': 25.15, 'pressure': 1022, 'humidity': 65, 'dew_point': 17.88, 'uvi': 2.6, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641740400, 'temp': 25.91, 'feels_like': 26.15, 'pressure': 1022, 'humidity': 61, 'dew_point': 17.82, 'uvi': 4.46, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641744000, 'temp': 26.91, 'feels_like': 28.04, 'pressure': 1021, 'humidity': 61, 'dew_point': 18.76, 'uvi': 9.28, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 90, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641747600, 'temp': 25.91, 'feels_like': 26.36, 'pressure': 1020, 'humidity': 69, 'dew_point': 19.79, 'uvi': 10.22, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 90, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641751200, 'temp': 27.91, 'feels_like': 29.01, 'pressure': 1018, 'humidity': 57, 'dew_point': 18.61, 'uvi': 9.4, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 40, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641754800, 'temp': 27.91, 'feels_like': 29.01, 'pressure': 1017, 'humidity': 57, 'dew_point': 18.61, 'uvi': 6.22, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641758400, 'temp': 27.91, 'feels_like': 29.01, 'pressure': 1016, 'humidity': 57, 'dew_point': 18.61, 'uvi': 3.68, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 70, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641762000, 'temp': 27.91, 'feels_like': 29.01, 'pressure': 1015, 'humidity': 57, 'dew_point': 18.61, 'uvi': 1.54, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 70, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.33}}, {'dt': 1641765600, 'temp': 26.91, 'feels_like': 28.04, 'pressure': 1015, 'humidity': 61, 'dew_point': 18.76, 'uvi': 0.47, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 80, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641769200, 'temp': 24.91, 'feels_like': 25.36, 'pressure': 1015, 'humidity': 73, 'dew_point': 19.74, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.42}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Julian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 00:00:00 | 20.000000 | 18.780000 | 24.260000 | 73.000000 | 1018.000000 |  | 23.910000 | 0.000000 | 10000.000000 | 20.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 01:00:00 | 20.000000 | 18.890000 | 22.320000 | 83.000000 | 1019.000000 |  | 21.910000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 02:00:00 | 20.000000 | 19.830000 | 22.450000 | 88.000000 | 1020.000000 |  | 21.910000 | 0.000000 | 10000.000000 | 230.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 03:00:00 | 20.000000 | 19.830000 | 22.450000 | 88.000000 | 1020.000000 |  | 21.910000 | 0.000000 | 10000.000000 | 230.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 04:00:00 | 42.000000 | 18.080000 | 22.190000 | 79.000000 | 1017.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 326.000000 | 1.81 | 2.350000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 05:00:00 | 49.000000 | 18.080000 | 22.190000 | 79.000000 | 1017.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 328.000000 | 1.65 | 2.160000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 06:00:00 | 11.000000 | 15.980000 | 19.420000 | 81.000000 | 1016.000000 |  | 19.320000 | 0.000000 | 10000.000000 | 325.000000 | 1.52 | 1.970000 | 801 | Clouds | few clouds | 02n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 07:00:00 | 11.000000 | 16.010000 | 19.260000 | 82.000000 | 1015.000000 |  | 19.150000 | 0.000000 | 10000.000000 | 322.000000 | 1.33 | 1.720000 | 801 | Clouds | few clouds | 02n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 08:00:00 | 28.000000 | 15.880000 | 19.120000 | 82.000000 | 1015.000000 |  | 19.020000 | 0.000000 | 10000.000000 | 326.000000 | 1.22 | 1.500000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 09:00:00 | 36.000000 | 16.010000 | 18.900000 | 84.000000 | 1015.000000 | 0.11 | 18.770000 | 0.000000 | 10000.000000 | 325.000000 | 1.14 | 1.390000 | 500 | Rain | light rain | 10n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 10:00:00 | 33.000000 | 15.830000 | 18.880000 | 83.000000 | 1016.000000 |  | 18.780000 | 0.000000 | 10000.000000 | 316.000000 | 1.11 | 1.420000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 11:00:00 | 20.000000 | 15.770000 | 19.000000 | 82.000000 | 1020.000000 |  | 18.910000 | 0.000000 | 10000.000000 | 290.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 12:00:00 | 20.000000 | 14.930000 | 19.860000 | 73.000000 | 1020.000000 |  | 19.910000 | 0.420000 | 10000.000000 | 290.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 13:00:00 | 20.000000 | 14.930000 | 19.860000 | 73.000000 | 1020.000000 |  | 19.910000 | 1.050000 | 10000.000000 | 290.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 14:00:00 | 20.000000 | 17.880000 | 25.150000 | 65.000000 | 1022.000000 |  | 24.910000 | 2.600000 | 10000.000000 | 0.000000 |  | 0.000000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 15:00:00 | 20.000000 | 17.820000 | 26.150000 | 61.000000 | 1022.000000 |  | 25.910000 | 4.460000 | 10000.000000 | 0.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 16:00:00 | 40.000000 | 18.760000 | 28.040000 | 61.000000 | 1021.000000 |  | 26.910000 | 9.280000 | 10000.000000 | 90.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 17:00:00 | 40.000000 | 19.790000 | 26.360000 | 69.000000 | 1020.000000 | 0.18 | 25.910000 | 10.220000 | 10000.000000 | 90.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 18:00:00 | 40.000000 | 18.610000 | 29.010000 | 57.000000 | 1018.000000 | 0.3 | 27.910000 | 9.400000 | 10000.000000 | 40.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 19:00:00 | 40.000000 | 18.610000 | 29.010000 | 57.000000 | 1017.000000 | 0.13 | 27.910000 | 6.220000 | 10000.000000 | 60.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 19 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 20:00:00 | 40.000000 | 18.610000 | 29.010000 | 57.000000 | 1016.000000 |  | 27.910000 | 3.680000 | 10000.000000 | 70.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 21:00:00 | 20.000000 | 18.610000 | 29.010000 | 57.000000 | 1015.000000 | 0.33 | 27.910000 | 1.540000 | 10000.000000 | 70.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 22:00:00 | 20.000000 | 18.760000 | 28.040000 | 61.000000 | 1015.000000 | 0.44 | 26.910000 | 0.470000 | 10000.000000 | 80.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-09 23:00:00 | 20.000000 | 19.740000 | 25.360000 | 73.000000 | 1015.000000 | 0.42 | 24.910000 | 0.000000 | 10000.000000 | 60.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 23 |
