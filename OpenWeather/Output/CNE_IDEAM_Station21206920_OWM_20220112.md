
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA TERESA - AUT [21206920] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot? - Colombia - Suram?rica

### GitHub repository and system information

* Python version: 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.0
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-01-12 11:11:05.365344
* Unix time to eval: 1641899465
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220112.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4494
* CNE IDEAM attributes: 20
* CNE IDEAM station code filter: ['All', 26055120, 1508500053]
* CNE IDEAM category filter: ['All']
* CNE IDEAM technology filter: ['All', 'Autom?tica sin Telemetr?a']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogot?']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206920_OWM_20220112.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220112.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.35,-74.15) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.35&lon=-74.15)

| Parameter | Value |
|---|---|
| Code | 21206920 |
| Name | VILLA TERESA - AUT [21206920] |
| Latitude, ? | 4.35 |
| Longitude, ? | -74.15 |
| Elevation, m | 3624 |
| Category | Clim?tica Principal |
| Technology | Autom?tica con Telemetr?a |
| Status | Activa |
| Installation date | 2005-07-19 00:00:00 |
| Suspension date | NaT |
| State | Bogot? |
| County | Bogota, D.C |
| Stream | Guatiquia |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | R?o Bogot? |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit metric system | Unit imperial system | openweathermap name |
|---|---|---|---|
| Temperature | ?C | ?F | temp |
| Dew Point | ?C | ?F | dew_point |
| Feels like | ?C | ?F | feels_like |
| Clouds | % | % | clouds |
| Humidity | % | % | humidity |
| Pressure | hPa | hPa | pressure |
| Wind Direction | ? | ? | wind_deg |
| Wind Speed | m/s | mi/h | wind_speed |
| Wind Gust | m/s | mi/h | wind_gust |
| Rain | mm | mm | rain |
| Visibility | m | m | visibility |
| UV Index | DN | DN | uvi |

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

### (CNE index 86) Open Weather values for station 21206920 - VILLA TERESA - AUT [21206920]

JSON data from API OWM:

```
{'lat': 4.35, 'lon': -74.15, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641899465, 'sunrise': 1641899262, 'sunset': 1641942057, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.16, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 324, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641859200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.83, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 76, 'wind_gust': 0.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641862800, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1017, 'humidity': 93, 'dew_point': 7.83, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 37, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641866400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 67, 'wind_gust': 0.87, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641870000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 166, 'wind_gust': 0.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641873600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 91, 'dew_point': 6.52, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 241, 'wind_gust': 0.79, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641877200, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.52, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 31, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641880800, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 292, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641884400, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.68, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 301, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641888000, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1016, 'humidity': 93, 'dew_point': 5.85, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 315, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641891600, 'temp': 6.9, 'feels_like': 6.9, 'pressure': 1016, 'humidity': 94, 'dew_point': 6, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 306, 'wind_gust': 1.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641895200, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.16, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 322, 'wind_gust': 0.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641898800, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1017, 'humidity': 95, 'dew_point': 5.16, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 324, 'wind_gust': 0.81, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641902400, 'temp': 5.9, 'feels_like': 5.9, 'pressure': 1018, 'humidity': 93, 'dew_point': 4.86, 'uvi': 0.41, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.59, 'wind_deg': 312, 'wind_gust': 1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641906000, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1019, 'humidity': 89, 'dew_point': 6.2, 'uvi': 1.88, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 325, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641909600, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 86, 'dew_point': 6.69, 'uvi': 4.49, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 336, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641913200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1019, 'humidity': 80, 'dew_point': 5.64, 'uvi': 7.58, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 332, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641916800, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1017, 'humidity': 76, 'dew_point': 5.87, 'uvi': 11.73, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 288, 'wind_gust': 1.52, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641920400, 'temp': 11.9, 'feels_like': 11.16, 'pressure': 1016, 'humidity': 77, 'dew_point': 8, 'uvi': 12.76, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 286, 'wind_gust': 1.78, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641924000, 'temp': 12.9, 'feels_like': 12.33, 'pressure': 1015, 'humidity': 80, 'dew_point': 9.54, 'uvi': 11.59, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 289, 'wind_gust': 1.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.54}}, {'dt': 1641927600, 'temp': 13.9, 'feels_like': 13.64, 'pressure': 1015, 'humidity': 88, 'dew_point': 11.95, 'uvi': 8.33, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 291, 'wind_gust': 1.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641931200, 'temp': 12.9, 'feels_like': 12.57, 'pressure': 1014, 'humidity': 89, 'dew_point': 11.13, 'uvi': 4.85, 'clouds': 100, 'visibility': 7732, 'wind_speed': 0.73, 'wind_deg': 280, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.53}}, {'dt': 1641934800, 'temp': 11.9, 'feels_like': 11.47, 'pressure': 1014, 'humidity': 89, 'dew_point': 10.15, 'uvi': 1.96, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 266, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.32}}, {'dt': 1641938400, 'temp': 11.9, 'feels_like': 11.52, 'pressure': 1015, 'humidity': 91, 'dew_point': 10.48, 'uvi': 0.46, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 272, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641942000, 'temp': 9.9, 'feels_like': 9.9, 'pressure': 1016, 'humidity': 96, 'dew_point': 9.29, 'uvi': 0, 'clouds': 93, 'visibility': 9233, 'wind_speed': 0.19, 'wind_deg': 295, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 00:00:00 | 80.000000 | 7.830000 | 8.900000 | 93.000000 | 1016.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 76.000000 | 0.77 | 0.220000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 01:00:00 | 88.000000 | 7.830000 | 8.900000 | 93.000000 | 1017.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 37.000000 | 0.88 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 02:00:00 | 88.000000 | 6.840000 | 7.900000 | 93.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 67.000000 | 0.87 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 03:00:00 | 79.000000 | 6.840000 | 7.900000 | 93.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 166.000000 | 0.9 | 0.350000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 04:00:00 | 78.000000 | 6.520000 | 7.900000 | 91.000000 | 1019.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 241.000000 | 0.79 | 0.080000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 05:00:00 | 81.000000 | 6.520000 | 7.900000 | 91.000000 | 1018.000000 | 0.15 | 7.900000 | 0.000000 | 10000.000000 | 31.000000 | 0.85 | 0.080000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 06:00:00 | 75.000000 | 6.680000 | 7.900000 | 92.000000 | 1017.000000 | 0.19 | 7.900000 | 0.000000 | 10000.000000 | 292.000000 | 0.8 | 0.420000 | 500 | Rain | light rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 07:00:00 | 85.000000 | 6.680000 | 7.900000 | 92.000000 | 1017.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 301.000000 | 1.05 | 0.540000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 08:00:00 | 87.000000 | 5.850000 | 6.900000 | 93.000000 | 1016.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 315.000000 | 0.88 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 09:00:00 | 91.000000 | 6.000000 | 6.900000 | 94.000000 | 1016.000000 |  | 6.900000 | 0.000000 | 10000.000000 | 306.000000 | 1.16 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 10:00:00 | 93.000000 | 5.160000 | 5.900000 | 95.000000 | 1017.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 322.000000 | 0.84 | 0.420000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 11:00:00 | 94.000000 | 5.160000 | 5.900000 | 95.000000 | 1017.000000 |  | 5.900000 | 0.000000 | 10000.000000 | 324.000000 | 0.81 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 12:00:00 | 86.000000 | 4.860000 | 5.900000 | 93.000000 | 1018.000000 |  | 5.900000 | 0.410000 | 10000.000000 | 312.000000 | 1 | 0.590000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 13:00:00 | 95.000000 | 6.200000 | 7.900000 | 89.000000 | 1019.000000 |  | 7.900000 | 1.880000 | 10000.000000 | 325.000000 | 1.18 | 0.660000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 14:00:00 | 97.000000 | 6.690000 | 8.900000 | 86.000000 | 1019.000000 | 0.12 | 8.900000 | 4.490000 | 10000.000000 | 336.000000 | 1.1 | 0.550000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 15:00:00 | 97.000000 | 5.640000 | 8.900000 | 80.000000 | 1019.000000 | 0.11 | 8.900000 | 7.580000 | 10000.000000 | 332.000000 | 1.2 | 0.680000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 16:00:00 | 97.000000 | 5.870000 | 9.900000 | 76.000000 | 1017.000000 | 0.16 | 9.900000 | 11.730000 | 10000.000000 | 288.000000 | 1.52 | 0.870000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 17:00:00 | 96.000000 | 8.000000 | 11.160000 | 77.000000 | 1016.000000 | 0.32 | 11.900000 | 12.760000 | 10000.000000 | 286.000000 | 1.78 | 1.000000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 18:00:00 | 93.000000 | 9.540000 | 12.330000 | 80.000000 | 1015.000000 | 0.54 | 12.900000 | 11.590000 | 10000.000000 | 289.000000 | 1.92 | 0.860000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 19:00:00 | 100.000000 | 11.950000 | 13.640000 | 88.000000 | 1015.000000 | 0.45 | 13.900000 | 8.330000 | 10000.000000 | 291.000000 | 1.98 | 0.790000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 20:00:00 | 100.000000 | 11.130000 | 12.570000 | 89.000000 | 1014.000000 | 0.53 | 12.900000 | 4.850000 | 7732.000000 | 280.000000 | 1.69 | 0.730000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 21:00:00 | 98.000000 | 10.150000 | 11.470000 | 89.000000 | 1014.000000 | 0.32 | 11.900000 | 1.960000 | 10000.000000 | 266.000000 | 1.57 | 0.380000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 22:00:00 | 97.000000 | 10.480000 | 11.520000 | 91.000000 | 1015.000000 | 0.14 | 11.900000 | 0.460000 | 10000.000000 | 272.000000 | 1.22 | 0.170000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206920 | "VILLA TERESA - AUT [21206920]" | 4.350000 | -74.150000 | 3624.000000 | Clim?tica Principal | Autom?tica con Telemetr?a | Activa | 2005-07-19 00:00:00 | NaT | Bogot? | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-01-11 23:00:00 | 93.000000 | 9.290000 | 9.900000 | 96.000000 | 1016.000000 | 0.13 | 9.900000 | 0.000000 | 9233.000000 | 295.000000 | 1.1 | 0.190000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206920_OWM_Clouds_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Clouds_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Dewpoint_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Dewpoint_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Feelslike_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Feelslike_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Humidity_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Humidity_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Pressure_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Pressure_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Rain_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Rain_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Temp_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Temp_20220112.png)
![CNE_IDEAM_Station21206920_OWM_UVI_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_UVI_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Visibility_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Visibility_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Windgust_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windgust_20220112.png)
![CNE_IDEAM_Station21206920_OWM_Windspeed_20220112.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206920_OWM_Windspeed_20220112.png)
