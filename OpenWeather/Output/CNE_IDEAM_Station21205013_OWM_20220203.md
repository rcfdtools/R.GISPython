
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - UNISALLE NORTE [21205013] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot? - Colombia - Suram?rica

### GitHub repository and system information

* Python version: 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.1
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-02-03 15:08:03.237034
* Unix time to eval: 1643814483
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220203.xls
* CNE IDEAM file downloaded and updated: Yes
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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21205013_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.79444444,-74.03055556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.79444444&lon=-74.03055556)

| Parameter | Value |
|---|---|
| Code | 21205013 |
| Name | UNISALLE NORTE [21205013] |
| Latitude, ? | 4.79444444 |
| Longitude, ? | -74.03055556 |
| Elevation, m | 2595 |
| Category | Clim?tica Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2009-12-14 00:00:00 |
| Suspension date | 2012-11-07 00:00:00 |
| State | Bogot? |
| County | Bogota, D.C |
| Stream | Guavio |
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

### (CNE index 1713) Open Weather values for station 21205013 - UNISALLE NORTE [21205013]

JSON data from API OWM:

```
{'lat': 4.7944, 'lon': -74.0306, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800327, 'sunset': 1643843249, 'temp': 15.9, 'feels_like': 14.8, 'pressure': 1027, 'humidity': 48, 'dew_point': 4.92, 'uvi': 9.17, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 170, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 12.9, 'feels_like': 12.26, 'pressure': 1024, 'humidity': 77, 'dew_point': 8.97, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 260, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643763600, 'temp': 11.9, 'feels_like': 11.44, 'pressure': 1025, 'humidity': 88, 'dew_point': 9.98, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 11.9, 'feels_like': 11.44, 'pressure': 1025, 'humidity': 88, 'dew_point': 9.98, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643770800, 'temp': 9.9, 'feels_like': 8.66, 'pressure': 1026, 'humidity': 100, 'dew_point': 9.9, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643774400, 'temp': 9.9, 'feels_like': 8.34, 'pressure': 1026, 'humidity': 93, 'dew_point': 8.82, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643778000, 'temp': 7.9, 'feels_like': 6.28, 'pressure': 1026, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 7.9, 'feels_like': 7.9, 'pressure': 1025, 'humidity': 100, 'dew_point': 7.9, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643785200, 'temp': 8.9, 'feels_like': 8.9, 'pressure': 1025, 'humidity': 100, 'dew_point': 8.9, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643788800, 'temp': 9.9, 'feels_like': 9.49, 'pressure': 1024, 'humidity': 100, 'dew_point': 9.9, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643792400, 'temp': 8.9, 'feels_like': 8.35, 'pressure': 1024, 'humidity': 100, 'dew_point': 8.9, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643796000, 'temp': 7.9, 'feels_like': 7.21, 'pressure': 1025, 'humidity': 93, 'dew_point': 6.84, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643799600, 'temp': 8.9, 'feels_like': 7.86, 'pressure': 1025, 'humidity': 87, 'dew_point': 6.86, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 40, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 8.9, 'feels_like': 7.47, 'pressure': 1026, 'humidity': 87, 'dew_point': 6.86, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643806800, 'temp': 10.9, 'feels_like': 10.19, 'pressure': 1026, 'humidity': 82, 'dew_point': 7.95, 'uvi': 2.3, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643810400, 'temp': 13.9, 'feels_like': 12.99, 'pressure': 1027, 'humidity': 63, 'dew_point': 6.98, 'uvi': 5.45, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 50, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643814000, 'temp': 15.9, 'feels_like': 14.8, 'pressure': 1027, 'humidity': 48, 'dew_point': 4.92, 'uvi': 9.17, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 170, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643817600, 'temp': 17.9, 'feels_like': 16.76, 'pressure': 1026, 'humidity': 39, 'dew_point': 3.76, 'uvi': 12.18, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 17.9, 'feels_like': 16.71, 'pressure': 1025, 'humidity': 37, 'dew_point': 3.02, 'uvi': 13.25, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643824800, 'temp': 16.9, 'feels_like': 16, 'pressure': 1025, 'humidity': 52, 'dew_point': 6.99, 'uvi': 12.02, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 290, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643828400, 'temp': 17.9, 'feels_like': 17.1, 'pressure': 1024, 'humidity': 52, 'dew_point': 7.92, 'uvi': 7.48, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643832000, 'temp': 17.9, 'feels_like': 17.1, 'pressure': 1023, 'humidity': 52, 'dew_point': 7.92, 'uvi': 4.35, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1643835600, 'temp': 16.9, 'feels_like': 16.08, 'pressure': 1023, 'humidity': 55, 'dew_point': 7.81, 'uvi': 1.78, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1643839200, 'temp': 15.9, 'feels_like': 15.19, 'pressure': 1023, 'humidity': 63, 'dew_point': 8.87, 'uvi': 0.42, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1643842800, 'temp': 13.9, 'feels_like': 13.23, 'pressure': 1023, 'humidity': 72, 'dew_point': 8.94, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 280, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 00:00:00 | 75.000000 | 8.970000 | 12.260000 | 77.000000 | 1024.000000 | 0.11 | 12.900000 | 0.000000 | 10000.000000 | 260.000000 |  | 3.600000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 01:00:00 | 75.000000 | 9.980000 | 11.440000 | 88.000000 | 1025.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 290.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 02:00:00 | 40.000000 | 9.980000 | 11.440000 | 88.000000 | 1025.000000 |  | 11.900000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 03:00:00 | 40.000000 | 9.900000 | 8.660000 | 100.000000 | 1026.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 04:00:00 | 40.000000 | 8.820000 | 8.340000 | 93.000000 | 1026.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 05:00:00 | 75.000000 | 6.840000 | 6.280000 | 93.000000 | 1026.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 06:00:00 | 75.000000 | 7.900000 | 7.900000 | 100.000000 | 1025.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 06 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 07:00:00 | 75.000000 | 8.900000 | 8.900000 | 100.000000 | 1025.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 08:00:00 | 40.000000 | 9.900000 | 9.490000 | 100.000000 | 1024.000000 |  | 9.900000 | 0.000000 | 10000.000000 | 10.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 09:00:00 | 40.000000 | 8.900000 | 8.350000 | 100.000000 | 1024.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 30.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 10:00:00 | 20.000000 | 6.840000 | 7.210000 | 93.000000 | 1025.000000 |  | 7.900000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 11:00:00 | 90.000000 | 6.860000 | 7.860000 | 87.000000 | 1025.000000 |  | 8.900000 | 0.000000 | 10000.000000 | 40.000000 |  | 2.060000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 12:00:00 | 40.000000 | 6.860000 | 7.470000 | 87.000000 | 1026.000000 |  | 8.900000 | 0.540000 | 10000.000000 | 40.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 13:00:00 | 20.000000 | 7.950000 | 10.190000 | 82.000000 | 1026.000000 |  | 10.900000 | 2.300000 | 10000.000000 | 40.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 14:00:00 | 20.000000 | 6.980000 | 12.990000 | 63.000000 | 1027.000000 |  | 13.900000 | 5.450000 | 10000.000000 | 50.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 15:00:00 | 40.000000 | 4.920000 | 14.800000 | 48.000000 | 1027.000000 |  | 15.900000 | 9.170000 | 10000.000000 | 170.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 16:00:00 | 75.000000 | 3.760000 | 16.760000 | 39.000000 | 1026.000000 |  | 17.900000 | 12.180000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 17:00:00 | 75.000000 | 3.020000 | 16.710000 | 37.000000 | 1025.000000 |  | 17.900000 | 13.250000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 18:00:00 | 40.000000 | 6.990000 | 16.000000 | 52.000000 | 1025.000000 |  | 16.900000 | 12.020000 | 10000.000000 | 290.000000 |  | 4.120000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 19:00:00 | 40.000000 | 7.920000 | 17.100000 | 52.000000 | 1024.000000 |  | 17.900000 | 7.480000 | 10000.000000 | 300.000000 |  | 4.630000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 20:00:00 | 40.000000 | 7.920000 | 17.100000 | 52.000000 | 1023.000000 | 0.11 | 17.900000 | 4.350000 | 10000.000000 | 280.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 21:00:00 | 40.000000 | 7.810000 | 16.080000 | 55.000000 | 1023.000000 | 0.15 | 16.900000 | 1.780000 | 10000.000000 | 280.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 22:00:00 | 40.000000 | 8.870000 | 15.190000 | 63.000000 | 1023.000000 | 0.17 | 15.900000 | 0.420000 | 10000.000000 | 280.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 22 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205013 | "UNISALLE NORTE [21205013]" | 4.794444 | -74.030556 | 2595.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2009-12-14 00:00:00 | 2012-11-07 00:00:00 | Bogot? | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 23:00:00 | 40.000000 | 8.940000 | 13.230000 | 72.000000 | 1023.000000 |  | 13.900000 | 0.000000 | 10000.000000 | 280.000000 |  | 5.140000 | 802 | Clouds | scattered clouds | 03d | 23 |


### Weather plots

![CNE_IDEAM_Station21205013_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21205013_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21205013_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205013_OWM_Windspeed_20220203.png)
