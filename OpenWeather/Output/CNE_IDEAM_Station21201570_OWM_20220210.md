
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA COL INGENIERIA [21201570] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot? - Colombia - Suram?rica

### GitHub repository and system information

* Python version: 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.1
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-02-10 14:08:04.180886
* Unix time to eval: 1644329284
* Days before (for historical data): 2
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220210.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM stations: 4499
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201570_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.78333333,-74.05) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.78333333&lon=-74.05)

| Parameter | Value |
|---|---|
| Code | 21201570 |
| Name | ESCUELA COL INGENIERIA [21201570] |
| Latitude, ? | 4.78333333 |
| Longitude, ? | -74.05 |
| Elevation, m | 2650 |
| Category | Pluviom?trica |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1981-11-15 00:00:00 |
| Suspension date | 1986-04-15 00:00:00 |
| State | Bogot? |
| County | Bogota, D.C |
| Stream | Tuamo |
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
| Latitude | latitud | lat | Geolocation latitude degrees |
| Longitude | longitud | lon | Geolocation longitude degrees |
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

### (CNE index 1701) Open Weather values for station 21201570 - ESCUELA COL INGENIERIA [21201570]

JSON data from API OWM:

```
{'lat': 4.7833, 'lon': -74.05, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318726, 'sunset': 1644361726, 'temp': 13.94, 'feels_like': 13.4, 'pressure': 1028, 'humidity': 77, 'dew_point': 9.98, 'uvi': 3.22, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 50, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 13.94, 'feels_like': 13.84, 'pressure': 1025, 'humidity': 94, 'dew_point': 12.99, 'uvi': 0, 'clouds': 75, 'visibility': 8000, 'wind_speed': 3.09, 'wind_deg': 240, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 13.94, 'feels_like': 13.84, 'pressure': 1026, 'humidity': 94, 'dew_point': 12.99, 'uvi': 0, 'clouds': 75, 'visibility': 8000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 12.94, 'feels_like': 12.74, 'pressure': 1027, 'humidity': 94, 'dew_point': 12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 12.94, 'feels_like': 12.74, 'pressure': 1028, 'humidity': 94, 'dew_point': 12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644292800, 'temp': 12.94, 'feels_like': 12.74, 'pressure': 1027, 'humidity': 94, 'dew_point': 12, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 20, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644296400, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1027, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 50, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 1}}, {'dt': 1644300000, 'temp': 11.94, 'feels_like': 11.46, 'pressure': 1026, 'humidity': 87, 'dew_point': 9.85, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 20, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.15}}, {'dt': 1644303600, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1025, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644307200, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1025, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644310800, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1024, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 12.94, 'feels_like': 12.59, 'pressure': 1025, 'humidity': 88, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 50, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 11.94, 'feels_like': 11.64, 'pressure': 1025, 'humidity': 94, 'dew_point': 11.01, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 11.94, 'feels_like': 11.64, 'pressure': 1026, 'humidity': 94, 'dew_point': 11.01, 'uvi': 0.28, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 13.94, 'feels_like': 13.53, 'pressure': 1027, 'humidity': 82, 'dew_point': 10.92, 'uvi': 1.36, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 13.94, 'feels_like': 13.4, 'pressure': 1028, 'humidity': 77, 'dew_point': 9.98, 'uvi': 3.22, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 50, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 14.94, 'feels_like': 14.24, 'pressure': 1028, 'humidity': 67, 'dew_point': 8.87, 'uvi': 5.42, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1644336000, 'temp': 12.94, 'feels_like': 12.74, 'pressure': 1028, 'humidity': 94, 'dew_point': 12, 'uvi': 9.18, 'clouds': 100, 'visibility': 7000, 'wind_speed': 3.09, 'wind_deg': 130, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 4.86}}, {'dt': 1644339600, 'temp': 11.94, 'feels_like': 11.64, 'pressure': 1028, 'humidity': 94, 'dew_point': 11.01, 'uvi': 9.99, 'clouds': 100, 'visibility': 6000, 'wind_speed': 2.06, 'wind_deg': 110, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}]}, {'dt': 1644343200, 'temp': 13.94, 'feels_like': 13.4, 'pressure': 1027, 'humidity': 77, 'dew_point': 9.98, 'uvi': 9.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 170, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644346800, 'temp': 14.94, 'feels_like': 14.37, 'pressure': 1026, 'humidity': 72, 'dew_point': 9.94, 'uvi': 3.65, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 250, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 14.94, 'feels_like': 14.37, 'pressure': 1025, 'humidity': 72, 'dew_point': 9.94, 'uvi': 2.13, 'clouds': 100, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 30, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 15.94, 'feels_like': 15.34, 'pressure': 1024, 'humidity': 67, 'dew_point': 9.83, 'uvi': 0.87, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 15.94, 'feels_like': 15.23, 'pressure': 1024, 'humidity': 63, 'dew_point': 8.91, 'uvi': 0.14, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 30, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 14.94, 'feels_like': 14.24, 'pressure': 1024, 'humidity': 67, 'dew_point': 8.87, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 00:00:00 | 75.000000 | 12.990000 | 13.840000 | 94.000000 | 1025.000000 |  | 13.940000 | 0.000000 | 8000.000000 | 240.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 01:00:00 | 75.000000 | 12.990000 | 13.840000 | 94.000000 | 1026.000000 |  | 13.940000 | 0.000000 | 8000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 02:00:00 | 75.000000 | 12.000000 | 12.740000 | 94.000000 | 1027.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 03:00:00 | 75.000000 | 12.000000 | 12.740000 | 94.000000 | 1028.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 290.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 04:00:00 | 75.000000 | 12.000000 | 12.740000 | 94.000000 | 1027.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 20.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 05:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1027.000000 | 1 | 12.940000 | 0.000000 | 10000.000000 | 50.000000 |  | 2.570000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 06:00:00 | 40.000000 | 9.850000 | 11.460000 | 87.000000 | 1026.000000 | 1.15 | 11.940000 | 0.000000 | 10000.000000 | 20.000000 |  | 3.090000 | 501 | Rain | moderate rain | 10n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 07:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1025.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 40.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 08:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1025.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 40.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 09:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1024.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 30.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 10:00:00 | 75.000000 | 11.000000 | 12.590000 | 88.000000 | 1025.000000 |  | 12.940000 | 0.000000 | 10000.000000 | 50.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 11:00:00 | 75.000000 | 11.010000 | 11.640000 | 94.000000 | 1025.000000 |  | 11.940000 | 0.000000 | 10000.000000 | 30.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 12:00:00 | 75.000000 | 11.010000 | 11.640000 | 94.000000 | 1026.000000 |  | 11.940000 | 0.280000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 13:00:00 | 75.000000 | 10.920000 | 13.530000 | 82.000000 | 1027.000000 |  | 13.940000 | 1.360000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 14:00:00 | 75.000000 | 9.980000 | 13.400000 | 77.000000 | 1028.000000 |  | 13.940000 | 3.220000 | 10000.000000 | 50.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 15:00:00 | 75.000000 | 8.870000 | 14.240000 | 67.000000 | 1028.000000 | 0.36 | 14.940000 | 5.420000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 16:00:00 | 100.000000 | 12.000000 | 12.740000 | 94.000000 | 1028.000000 | 4.86 | 12.940000 | 9.180000 | 7000.000000 | 130.000000 |  | 3.090000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 17:00:00 | 100.000000 | 11.010000 | 11.640000 | 94.000000 | 1028.000000 |  | 11.940000 | 9.990000 | 6000.000000 | 110.000000 |  | 2.060000 | 300 | Drizzle | light intensity drizzle | 09d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 18:00:00 | 100.000000 | 9.980000 | 13.400000 | 77.000000 | 1027.000000 |  | 13.940000 | 9.070000 | 10000.000000 | 170.000000 |  | 2.060000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 9.940000 | 14.370000 | 72.000000 | 1026.000000 |  | 14.940000 | 3.650000 | 10000.000000 | 250.000000 |  | 2.060000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 9.940000 | 14.370000 | 72.000000 | 1025.000000 |  | 14.940000 | 2.130000 | 10000.000000 | 30.000000 |  | 3.090000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 21:00:00 | 75.000000 | 9.830000 | 15.340000 | 67.000000 | 1024.000000 |  | 15.940000 | 0.870000 | 10000.000000 | 30.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 22:00:00 | 75.000000 | 8.910000 | 15.230000 | 63.000000 | 1024.000000 |  | 15.940000 | 0.140000 | 10000.000000 | 30.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201570 | "ESCUELA COL INGENIERIA [21201570]" | 4.783333 | -74.050000 | 2650.000000 | Pluviom?trica | Convencional | Suspendida | 1981-11-15 00:00:00 | 1986-04-15 00:00:00 | Bogot? | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 23:00:00 | 75.000000 | 8.870000 | 14.240000 | 67.000000 | 1024.000000 |  | 14.940000 | 0.000000 | 10000.000000 | 360.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201570_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21201570_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21201570_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201570_OWM_Windspeed_20220210.png)
