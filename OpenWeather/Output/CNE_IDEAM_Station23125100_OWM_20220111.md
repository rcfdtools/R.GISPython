
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BUENAVISTA [23125100] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23125100_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.51491667,-73.94311111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.51491667&lon=-73.94311111)


| Parameter | Value |
|---|---|
| Code | 23125100 |
| Name | BUENAVISTA [23125100] |
| Latitude, ° | 5.51491667 |
| Longitude, ° | -73.94311111 |
| Elevation, m | 2200 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1993-11-14 19:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Buenavista (Boyacá) |
| Stream | 0 |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Carare (Minero) |

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

### (CNE index 1785) Open Weather values for station 23125100 - BUENAVISTA [23125100]

JSON data from API OWM:

```
{'lat': 5.5149, 'lon': -73.9431, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812905, 'sunset': 1641855467, 'temp': 16.02, 'feels_like': 15.92, 'pressure': 1012, 'humidity': 86, 'dew_point': 13.68, 'uvi': 3.54, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 314, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, 'hourly': [{'dt': 1641772800, 'temp': 12.92, 'feels_like': 12.8, 'pressure': 1015, 'humidity': 97, 'dew_point': 12.46, 'uvi': 0, 'clouds': 58, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 108, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641776400, 'temp': 12.64, 'feels_like': 12.47, 'pressure': 1016, 'humidity': 96, 'dew_point': 12.02, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 112, 'wind_gust': 0.88, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641780000, 'temp': 12.12, 'feels_like': 11.89, 'pressure': 1017, 'humidity': 96, 'dew_point': 11.5, 'uvi': 0, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 117, 'wind_gust': 1.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 11.86, 'feels_like': 11.61, 'pressure': 1017, 'humidity': 96, 'dew_point': 11.24, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 117, 'wind_gust': 1.13, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 11.57, 'feels_like': 11.29, 'pressure': 1017, 'humidity': 96, 'dew_point': 10.95, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 125, 'wind_gust': 1.11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 11.18, 'feels_like': 10.86, 'pressure': 1017, 'humidity': 96, 'dew_point': 10.57, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 128, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 11, 'feels_like': 10.64, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.23, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 125, 'wind_gust': 1, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]}, {'dt': 1641798000, 'temp': 10.19, 'feels_like': 9.75, 'pressure': 1015, 'humidity': 95, 'dew_point': 9.43, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 128, 'wind_gust': 1.15, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 9.79, 'feels_like': 9.23, 'pressure': 1015, 'humidity': 95, 'dew_point': 9.03, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 123, 'wind_gust': 1.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 9.53, 'feels_like': 9.04, 'pressure': 1015, 'humidity': 95, 'dew_point': 8.77, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 1.57, 'wind_deg': 126, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 9.39, 'feels_like': 8.75, 'pressure': 1016, 'humidity': 96, 'dew_point': 8.79, 'uvi': 0, 'clouds': 55, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 122, 'wind_gust': 1.21, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 9.7, 'feels_like': 9.19, 'pressure': 1017, 'humidity': 95, 'dew_point': 8.94, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 126, 'wind_gust': 1.22, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 10.95, 'feels_like': 10.5, 'pressure': 1017, 'humidity': 92, 'dew_point': 9.7, 'uvi': 0.49, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 125, 'wind_gust': 1.21, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 14.06, 'feels_like': 13.64, 'pressure': 1018, 'humidity': 81, 'dew_point': 10.85, 'uvi': 1.55, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 328, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 16.18, 'feels_like': 15.73, 'pressure': 1018, 'humidity': 72, 'dew_point': 11.13, 'uvi': 3.7, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 313, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 17.54, 'feels_like': 17.13, 'pressure': 1017, 'humidity': 68, 'dew_point': 11.57, 'uvi': 6.21, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 308, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.41, 'feels_like': 18.03, 'pressure': 1016, 'humidity': 66, 'dew_point': 11.95, 'uvi': 10.1, 'clouds': 66, 'visibility': 10000, 'wind_speed': 2.33, 'wind_deg': 308, 'wind_gust': 1.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641834000, 'temp': 18.93, 'feels_like': 18.55, 'pressure': 1014, 'humidity': 64, 'dew_point': 11.98, 'uvi': 10.93, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.48, 'wind_deg': 306, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 18.31, 'feels_like': 18, 'pressure': 1013, 'humidity': 69, 'dew_point': 12.53, 'uvi': 9.84, 'clouds': 71, 'visibility': 10000, 'wind_speed': 2.36, 'wind_deg': 309, 'wind_gust': 1.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641841200, 'temp': 16.94, 'feels_like': 16.75, 'pressure': 1013, 'humidity': 79, 'dew_point': 13.28, 'uvi': 6.19, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 315, 'wind_gust': 1.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641844800, 'temp': 16.02, 'feels_like': 15.92, 'pressure': 1012, 'humidity': 86, 'dew_point': 13.68, 'uvi': 3.54, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 314, 'wind_gust': 1.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641848400, 'temp': 15.76, 'feels_like': 15.64, 'pressure': 1012, 'humidity': 86, 'dew_point': 13.43, 'uvi': 1.4, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 311, 'wind_gust': 1.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.38}}, {'dt': 1641852000, 'temp': 14.58, 'feels_like': 14.52, 'pressure': 1013, 'humidity': 93, 'dew_point': 13.46, 'uvi': 0.23, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 331, 'wind_gust': 1.46, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641855600, 'temp': 12.9, 'feels_like': 12.75, 'pressure': 1014, 'humidity': 96, 'dew_point': 12.28, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 34, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 00:00:00 | 58.000000 | 12.460000 | 12.800000 | 97.000000 | 1015.000000 | 0.11 | 12.920000 | 0.000000 | 10000.000000 | 108.000000 | 0.93 | 0.560000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 01:00:00 | 68.000000 | 12.020000 | 12.470000 | 96.000000 | 1016.000000 | 0.19 | 12.640000 | 0.000000 | 10000.000000 | 112.000000 | 0.88 | 0.540000 | 500 | Rain | light rain | 10n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 02:00:00 | 68.000000 | 11.500000 | 11.890000 | 96.000000 | 1017.000000 |  | 12.120000 | 0.000000 | 10000.000000 | 117.000000 | 1.02 | 0.750000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 03:00:00 | 72.000000 | 11.240000 | 11.610000 | 96.000000 | 1017.000000 |  | 11.860000 | 0.000000 | 10000.000000 | 117.000000 | 1.13 | 1.050000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 04:00:00 | 70.000000 | 10.950000 | 11.290000 | 96.000000 | 1017.000000 |  | 11.570000 | 0.000000 | 10000.000000 | 125.000000 | 1.11 | 1.220000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 05:00:00 | 73.000000 | 10.570000 | 10.860000 | 96.000000 | 1017.000000 |  | 11.180000 | 0.000000 | 10000.000000 | 128.000000 | 1.07 | 1.450000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![01n.png](http://openweathermap.org/img/w/01n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 06:00:00 | 9.000000 | 10.230000 | 10.640000 | 95.000000 | 1016.000000 |  | 11.000000 | 0.000000 | 10000.000000 | 125.000000 | 1 | 1.350000 | 800 | Clear | clear sky | 01n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 07:00:00 | 22.000000 | 9.430000 | 9.750000 | 95.000000 | 1015.000000 |  | 10.190000 | 0.000000 | 10000.000000 | 128.000000 | 1.15 | 1.560000 | 801 | Clouds | few clouds | 02n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 08:00:00 | 45.000000 | 9.030000 | 9.230000 | 95.000000 | 1015.000000 |  | 9.790000 | 0.000000 | 10000.000000 | 123.000000 | 1.23 | 1.680000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 09:00:00 | 46.000000 | 8.770000 | 9.040000 | 95.000000 | 1015.000000 |  | 9.530000 | 0.000000 | 10000.000000 | 126.000000 | 1.11 | 1.570000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 10:00:00 | 55.000000 | 8.790000 | 8.750000 | 96.000000 | 1016.000000 |  | 9.390000 | 0.000000 | 10000.000000 | 122.000000 | 1.21 | 1.700000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 11:00:00 | 61.000000 | 8.940000 | 9.190000 | 95.000000 | 1017.000000 |  | 9.700000 | 0.000000 | 10000.000000 | 126.000000 | 1.22 | 1.610000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 12:00:00 | 93.000000 | 9.700000 | 10.500000 | 92.000000 | 1017.000000 |  | 10.950000 | 0.490000 | 10000.000000 | 125.000000 | 1.21 | 1.360000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 13:00:00 | 99.000000 | 10.850000 | 13.640000 | 81.000000 | 1018.000000 |  | 14.060000 | 1.550000 | 10000.000000 | 328.000000 | 0.7 | 0.340000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 14:00:00 | 97.000000 | 11.130000 | 15.730000 | 72.000000 | 1018.000000 |  | 16.180000 | 3.700000 | 10000.000000 | 313.000000 | 1.06 | 1.420000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 15:00:00 | 76.000000 | 11.570000 | 17.130000 | 68.000000 | 1017.000000 |  | 17.540000 | 6.210000 | 10000.000000 | 308.000000 | 1.4 | 2.150000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 16:00:00 | 66.000000 | 11.950000 | 18.030000 | 66.000000 | 1016.000000 | 0.12 | 18.410000 | 10.100000 | 10000.000000 | 308.000000 | 1.71 | 2.330000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 17:00:00 | 63.000000 | 11.980000 | 18.550000 | 64.000000 | 1014.000000 | 0.11 | 18.930000 | 10.930000 | 10000.000000 | 306.000000 | 1.75 | 2.480000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 18:00:00 | 71.000000 | 12.530000 | 18.000000 | 69.000000 | 1013.000000 | 0.14 | 18.310000 | 9.840000 | 10000.000000 | 309.000000 | 1.66 | 2.360000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 19:00:00 | 87.000000 | 13.280000 | 16.750000 | 79.000000 | 1013.000000 | 0.54 | 16.940000 | 6.190000 | 10000.000000 | 315.000000 | 1.93 | 2.180000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 20:00:00 | 84.000000 | 13.680000 | 15.920000 | 86.000000 | 1012.000000 | 0.54 | 16.020000 | 3.540000 | 10000.000000 | 314.000000 | 1.72 | 1.680000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 21:00:00 | 86.000000 | 13.430000 | 15.640000 | 86.000000 | 1012.000000 | 0.38 | 15.760000 | 1.400000 | 10000.000000 | 311.000000 | 1.31 | 1.310000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 13.460000 | 14.520000 | 93.000000 | 1013.000000 | 0.46 | 14.580000 | 0.230000 | 10000.000000 | 331.000000 | 1.46 | 1.080000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23125100 | "BUENAVISTA [23125100]" | 5.514917 | -73.943111 | 2200.000000 | Climática Principal | Convencional | Activa | 1993-11-14 19:00:00 | NaT | Boyacá | Buenavista (Boyacá) | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Medio Magdalena | Río Carare (Minero) | America/Bogota | 2022-01-10 23:00:00 | 84.000000 | 12.280000 | 12.750000 | 96.000000 | 1014.000000 | 0.18 | 12.900000 | 0.000000 | 10000.000000 | 34.000000 | 0.76 | 0.490000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station23125100_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23125100_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23125100_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23125100_OWM_Windspeed_20220111.png)
