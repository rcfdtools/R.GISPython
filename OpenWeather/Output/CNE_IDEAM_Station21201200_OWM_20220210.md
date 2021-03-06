
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ESCUELA LA UNION [21201200] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21201200_OWM_20220210.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220210.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.34294444,-74.18388889) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.34294444&lon=-74.18388889)

| Parameter | Value |
|---|---|
| Code | 21201200 |
| Name | ESCUELA LA UNION [21201200] |
| Latitude, ? | 4.34294444 |
| Longitude, ? | -74.18388889 |
| Elevation, m | 3320 |
| Category | Pluviom?trica |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1985-03-14 19:00:00 |
| Suspension date | NaT |
| State | Bogot? |
| County | Bogota, D.C |
| Stream | 0 |
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

### (CNE index 3317) Open Weather values for station 21201200 - ESCUELA LA UNION [21201200]

JSON data from API OWM:

```
{'lat': 4.3429, 'lon': -74.1839, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1644329284, 'sunrise': 1644318730, 'sunset': 1644361786, 'temp': 8.58, 'feels_like': 8.58, 'pressure': 1019, 'humidity': 86, 'dew_point': 6.37, 'uvi': 3.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.03, 'wind_deg': 356, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1644278400, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1016, 'humidity': 93, 'dew_point': 7.91, 'uvi': 0, 'clouds': 100, 'visibility': 9010, 'wind_speed': 1.2, 'wind_deg': 112, 'wind_gust': 1.84, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644282000, 'temp': 8.98, 'feels_like': 8.57, 'pressure': 1017, 'humidity': 92, 'dew_point': 7.75, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 109, 'wind_gust': 1.97, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644285600, 'temp': 7.98, 'feels_like': 7.18, 'pressure': 1018, 'humidity': 91, 'dew_point': 6.6, 'uvi': 0, 'clouds': 100, 'visibility': 5138, 'wind_speed': 1.65, 'wind_deg': 101, 'wind_gust': 2.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644289200, 'temp': 7.98, 'feels_like': 7.31, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 4090, 'wind_speed': 1.53, 'wind_deg': 97, 'wind_gust': 2.16, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 3.16}}, {'dt': 1644292800, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1019, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 2034, 'wind_speed': 0.89, 'wind_deg': 109, 'wind_gust': 1.47, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.33}}, {'dt': 1644296400, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1018, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 7157, 'wind_speed': 0.35, 'wind_deg': 110, 'wind_gust': 1.11, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 2.37}}, {'dt': 1644300000, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1018, 'humidity': 94, 'dew_point': 6.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 95, 'wind_gust': 0.79, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.78}}, {'dt': 1644303600, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 93, 'dew_point': 6.92, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 101, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 1}}, {'dt': 1644307200, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.11, 'wind_deg': 161, 'wind_gust': 0.7, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.54}}, {'dt': 1644310800, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1016, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.18, 'wind_deg': 152, 'wind_gust': 0.63, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644314400, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 6.76, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 118, 'wind_gust': 0.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644318000, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1017, 'humidity': 92, 'dew_point': 5.77, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 109, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1644321600, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1018, 'humidity': 91, 'dew_point': 5.61, 'uvi': 0.07, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 107, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644325200, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1018, 'humidity': 89, 'dew_point': 7.27, 'uvi': 1.41, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 84, 'wind_gust': 1.46, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644328800, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1019, 'humidity': 86, 'dew_point': 6.77, 'uvi': 3.32, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.03, 'wind_deg': 356, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644332400, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1018, 'humidity': 83, 'dew_point': 7.23, 'uvi': 5.57, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 316, 'wind_gust': 1.73, 'weather': [{'id': 503, 'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'}], 'rain': {'1h': 20.5}}, {'dt': 1644336000, 'temp': 7.98, 'feels_like': 7.98, 'pressure': 1017, 'humidity': 86, 'dew_point': 5.78, 'uvi': 5.67, 'clouds': 97, 'visibility': 8972, 'wind_speed': 0.52, 'wind_deg': 272, 'wind_gust': 1.68, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 5.62}}, {'dt': 1644339600, 'temp': 6.98, 'feels_like': 6.98, 'pressure': 1016, 'humidity': 90, 'dew_point': 5.45, 'uvi': 6.17, 'clouds': 98, 'visibility': 7486, 'wind_speed': 0.21, 'wind_deg': 310, 'wind_gust': 1.54, 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'}], 'rain': {'1h': 4.21}}, {'dt': 1644343200, 'temp': 8.98, 'feels_like': 8.98, 'pressure': 1016, 'humidity': 90, 'dew_point': 7.43, 'uvi': 5.61, 'clouds': 99, 'visibility': 5543, 'wind_speed': 0.38, 'wind_deg': 336, 'wind_gust': 1.25, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.78}}, {'dt': 1644346800, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 92, 'dew_point': 8.74, 'uvi': 5.44, 'clouds': 100, 'visibility': 4801, 'wind_speed': 0.44, 'wind_deg': 333, 'wind_gust': 1.13, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644350400, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1015, 'humidity': 93, 'dew_point': 8.9, 'uvi': 3.18, 'clouds': 100, 'visibility': 3529, 'wind_speed': 0.41, 'wind_deg': 323, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644354000, 'temp': 10.98, 'feels_like': 10.56, 'pressure': 1015, 'humidity': 93, 'dew_point': 9.89, 'uvi': 1.31, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.14, 'wind_deg': 45, 'wind_gust': 1.29, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644357600, 'temp': 10.98, 'feels_like': 10.54, 'pressure': 1015, 'humidity': 92, 'dew_point': 9.73, 'uvi': 0.5, 'clouds': 100, 'visibility': 9357, 'wind_speed': 0.36, 'wind_deg': 104, 'wind_gust': 1.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1644361200, 'temp': 9.98, 'feels_like': 9.98, 'pressure': 1016, 'humidity': 95, 'dew_point': 9.22, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.23, 'wind_deg': 118, 'wind_gust': 1.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 00:00:00 | 100.000000 | 7.910000 | 8.980000 | 93.000000 | 1016.000000 |  | 8.980000 | 0.000000 | 9010.000000 | 112.000000 | 1.84 | 1.200000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 01:00:00 | 100.000000 | 7.750000 | 8.570000 | 92.000000 | 1017.000000 |  | 8.980000 | 0.000000 | 10000.000000 | 109.000000 | 1.97 | 1.420000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 02:00:00 | 100.000000 | 6.600000 | 7.180000 | 91.000000 | 1018.000000 |  | 7.980000 | 0.000000 | 5138.000000 | 101.000000 | 2.3 | 1.650000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 03:00:00 | 100.000000 | 6.760000 | 7.310000 | 92.000000 | 1019.000000 | 3.16 | 7.980000 | 0.000000 | 4090.000000 | 97.000000 | 2.16 | 1.530000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 04:00:00 | 100.000000 | 6.760000 | 7.980000 | 92.000000 | 1019.000000 | 1.33 | 7.980000 | 0.000000 | 2034.000000 | 109.000000 | 1.47 | 0.890000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 05:00:00 | 100.000000 | 6.760000 | 7.980000 | 92.000000 | 1018.000000 | 2.37 | 7.980000 | 0.000000 | 7157.000000 | 110.000000 | 1.11 | 0.350000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 06:00:00 | 100.000000 | 6.080000 | 6.980000 | 94.000000 | 1018.000000 | 1.78 | 6.980000 | 0.000000 | 10000.000000 | 95.000000 | 0.79 | 0.120000 | 501 | Rain | moderate rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 07:00:00 | 100.000000 | 6.920000 | 7.980000 | 93.000000 | 1017.000000 | 1 | 7.980000 | 0.000000 | 10000.000000 | 101.000000 | 0.9 | 0.350000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 08:00:00 | 100.000000 | 6.760000 | 7.980000 | 92.000000 | 1016.000000 | 1.54 | 7.980000 | 0.000000 | 10000.000000 | 161.000000 | 0.7 | 0.110000 | 501 | Rain | moderate rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 09:00:00 | 100.000000 | 6.760000 | 7.980000 | 92.000000 | 1016.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 152.000000 | 0.63 | 0.180000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 10:00:00 | 100.000000 | 6.760000 | 7.980000 | 92.000000 | 1017.000000 |  | 7.980000 | 0.000000 | 10000.000000 | 118.000000 | 0.73 | 0.610000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 11:00:00 | 100.000000 | 5.770000 | 6.980000 | 92.000000 | 1017.000000 |  | 6.980000 | 0.000000 | 10000.000000 | 109.000000 | 0.98 | 0.710000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 12:00:00 | 100.000000 | 5.610000 | 6.980000 | 91.000000 | 1018.000000 |  | 6.980000 | 0.070000 | 10000.000000 | 107.000000 | 1.18 | 0.700000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 13:00:00 | 100.000000 | 7.270000 | 8.980000 | 89.000000 | 1018.000000 |  | 8.980000 | 1.410000 | 10000.000000 | 84.000000 | 1.46 | 0.610000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 14:00:00 | 95.000000 | 6.770000 | 8.980000 | 86.000000 | 1019.000000 |  | 8.980000 | 3.320000 | 10000.000000 | 356.000000 | 1.44 | 0.030000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 15:00:00 | 96.000000 | 7.230000 | 9.980000 | 83.000000 | 1018.000000 | 20.5 | 9.980000 | 5.570000 | 10000.000000 | 316.000000 | 1.73 | 0.220000 | 503 | Rain | very heavy rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 16:00:00 | 97.000000 | 5.780000 | 7.980000 | 86.000000 | 1017.000000 | 5.62 | 7.980000 | 5.670000 | 8972.000000 | 272.000000 | 1.68 | 0.520000 | 502 | Rain | heavy intensity rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 17:00:00 | 98.000000 | 5.450000 | 6.980000 | 90.000000 | 1016.000000 | 4.21 | 6.980000 | 6.170000 | 7486.000000 | 310.000000 | 1.54 | 0.210000 | 502 | Rain | heavy intensity rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 18:00:00 | 99.000000 | 7.430000 | 8.980000 | 90.000000 | 1016.000000 | 1.78 | 8.980000 | 5.610000 | 5543.000000 | 336.000000 | 1.25 | 0.380000 | 501 | Rain | moderate rain | 10d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 19:00:00 | 100.000000 | 8.740000 | 9.980000 | 92.000000 | 1015.000000 |  | 9.980000 | 5.440000 | 4801.000000 | 333.000000 | 1.13 | 0.440000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 20:00:00 | 100.000000 | 8.900000 | 9.980000 | 93.000000 | 1015.000000 |  | 9.980000 | 3.180000 | 3529.000000 | 323.000000 | 1.11 | 0.410000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 21:00:00 | 100.000000 | 9.890000 | 10.560000 | 93.000000 | 1015.000000 |  | 10.980000 | 1.310000 | 10000.000000 | 45.000000 | 1.29 | 0.140000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 22:00:00 | 100.000000 | 9.730000 | 10.540000 | 92.000000 | 1015.000000 |  | 10.980000 | 0.500000 | 9357.000000 | 104.000000 | 1.51 | 0.360000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21201200 | "ESCUELA LA UNION [21201200]" | 4.342944 | -74.183889 | 3320.000000 | Pluviom?trica | Convencional | Activa | 1985-03-14 19:00:00 | NaT | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-08 23:00:00 | 100.000000 | 9.220000 | 9.980000 | 95.000000 | 1016.000000 |  | 9.980000 | 0.000000 | 10000.000000 | 118.000000 | 1.2 | 0.230000 | 804 | Clouds | overcast clouds | 04d | 23 |


### Weather plots

![CNE_IDEAM_Station21201200_OWM_Clouds_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Clouds_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Dewpoint_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Dewpoint_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Feelslike_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Feelslike_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Humidity_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Humidity_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Pressure_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Pressure_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Rain_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Rain_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Temp_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Temp_20220210.png)
![CNE_IDEAM_Station21201200_OWM_UVI_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_UVI_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Visibility_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Visibility_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Winddeg_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Winddeg_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Windgust_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windgust_20220210.png)
![CNE_IDEAM_Station21201200_OWM_Windspeed_20220210.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21201200_OWM_Windspeed_20220210.png)
