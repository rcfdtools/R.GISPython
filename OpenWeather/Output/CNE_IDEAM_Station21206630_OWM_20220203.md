
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BILBAO MAXIMO POTI [21206630] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206630_OWM_20220203.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220203.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.75113889,-74.09158333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.75113889&lon=-74.09158333)

| Parameter | Value |
|---|---|
| Code | 21206630 |
| Name | BILBAO MAXIMO POTI [21206630] |
| Latitude, ? | 4.75113889 |
| Longitude, ? | -74.09158333 |
| Elevation, m | 2600 |
| Category | Clim?tica Ordinaria |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2001-11-15 00:00:00 |
| Suspension date | 2018-04-12 16:36:29 |
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

### (CNE index 1358) Open Weather values for station 21206630 - BILBAO MAXIMO POTI [21206630]

JSON data from API OWM:

```
{'lat': 4.7511, 'lon': -74.0916, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643814483, 'sunrise': 1643800338, 'sunset': 1643843267, 'temp': 16.95, 'feels_like': 15.95, 'pressure': 1027, 'humidity': 48, 'dew_point': 5.88, 'uvi': 9.17, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 170, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, 'hourly': [{'dt': 1643760000, 'temp': 13.95, 'feels_like': 13.41, 'pressure': 1024, 'humidity': 77, 'dew_point': 9.99, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 260, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1643763600, 'temp': 12.95, 'feels_like': 12.6, 'pressure': 1025, 'humidity': 88, 'dew_point': 11.01, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 290, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643767200, 'temp': 12.95, 'feels_like': 12.6, 'pressure': 1025, 'humidity': 88, 'dew_point': 11.01, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643770800, 'temp': 10.95, 'feels_like': 10.71, 'pressure': 1026, 'humidity': 100, 'dew_point': 10.95, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643774400, 'temp': 10.95, 'feels_like': 10.53, 'pressure': 1026, 'humidity': 93, 'dew_point': 9.86, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643778000, 'temp': 8.95, 'feels_like': 7.53, 'pressure': 1026, 'humidity': 93, 'dew_point': 7.88, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1643781600, 'temp': 8.95, 'feels_like': 8.95, 'pressure': 1025, 'humidity': 100, 'dew_point': 8.95, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643785200, 'temp': 9.95, 'feels_like': 9.95, 'pressure': 1025, 'humidity': 100, 'dew_point': 9.95, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643788800, 'temp': 10.95, 'feels_like': 10.71, 'pressure': 1024, 'humidity': 100, 'dew_point': 10.95, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 10, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643792400, 'temp': 9.95, 'feels_like': 9.55, 'pressure': 1024, 'humidity': 100, 'dew_point': 9.95, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 30, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643796000, 'temp': 8.95, 'feels_like': 8.41, 'pressure': 1025, 'humidity': 93, 'dew_point': 7.88, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643799600, 'temp': 9.95, 'feels_like': 9.09, 'pressure': 1025, 'humidity': 87, 'dew_point': 7.89, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 40, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1643803200, 'temp': 9.95, 'feels_like': 8.72, 'pressure': 1026, 'humidity': 87, 'dew_point': 7.89, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643806800, 'temp': 11.95, 'feels_like': 11.34, 'pressure': 1026, 'humidity': 82, 'dew_point': 8.98, 'uvi': 2.3, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643810400, 'temp': 14.95, 'feels_like': 14.15, 'pressure': 1027, 'humidity': 63, 'dew_point': 7.98, 'uvi': 5.45, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 50, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1643814000, 'temp': 16.95, 'feels_like': 15.95, 'pressure': 1027, 'humidity': 48, 'dew_point': 5.88, 'uvi': 9.17, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 170, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643817600, 'temp': 18.95, 'feels_like': 17.92, 'pressure': 1026, 'humidity': 39, 'dew_point': 4.7, 'uvi': 12.18, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643821200, 'temp': 18.95, 'feels_like': 17.87, 'pressure': 1025, 'humidity': 37, 'dew_point': 3.95, 'uvi': 13.25, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643824800, 'temp': 17.95, 'feels_like': 17.16, 'pressure': 1025, 'humidity': 52, 'dew_point': 7.96, 'uvi': 12.02, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 290, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643828400, 'temp': 18.95, 'feels_like': 18.26, 'pressure': 1024, 'humidity': 52, 'dew_point': 8.89, 'uvi': 7.48, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643832000, 'temp': 18.95, 'feels_like': 18.26, 'pressure': 1023, 'humidity': 52, 'dew_point': 8.89, 'uvi': 4.35, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.22}}, {'dt': 1643835600, 'temp': 17.95, 'feels_like': 17.24, 'pressure': 1023, 'humidity': 55, 'dew_point': 8.79, 'uvi': 1.78, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1643839200, 'temp': 16.95, 'feels_like': 16.35, 'pressure': 1023, 'humidity': 63, 'dew_point': 9.87, 'uvi': 0.42, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1643842800, 'temp': 14.95, 'feels_like': 14.38, 'pressure': 1023, 'humidity': 72, 'dew_point': 9.95, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 00:00:00 | 75.000000 | 9.990000 | 13.410000 | 77.000000 | 1024.000000 | 0.13 | 13.950000 | 0.000000 | 10000.000000 | 260.000000 |  | 3.600000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 01:00:00 | 75.000000 | 11.010000 | 12.600000 | 88.000000 | 1025.000000 |  | 12.950000 | 0.000000 | 10000.000000 | 290.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 02:00:00 | 40.000000 | 11.010000 | 12.600000 | 88.000000 | 1025.000000 | 0.11 | 12.950000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 03:00:00 | 40.000000 | 10.950000 | 10.710000 | 100.000000 | 1026.000000 |  | 10.950000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 04:00:00 | 40.000000 | 9.860000 | 10.530000 | 93.000000 | 1026.000000 |  | 10.950000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 05:00:00 | 75.000000 | 7.880000 | 7.530000 | 93.000000 | 1026.000000 |  | 8.950000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 06:00:00 | 75.000000 | 8.950000 | 8.950000 | 100.000000 | 1025.000000 |  | 8.950000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 06 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 07:00:00 | 75.000000 | 9.950000 | 9.950000 | 100.000000 | 1025.000000 |  | 9.950000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 08:00:00 | 40.000000 | 10.950000 | 10.710000 | 100.000000 | 1024.000000 |  | 10.950000 | 0.000000 | 10000.000000 | 10.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 09:00:00 | 40.000000 | 9.950000 | 9.550000 | 100.000000 | 1024.000000 |  | 9.950000 | 0.000000 | 10000.000000 | 30.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 10:00:00 | 20.000000 | 7.880000 | 8.410000 | 93.000000 | 1025.000000 |  | 8.950000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 11:00:00 | 92.000000 | 7.890000 | 9.090000 | 87.000000 | 1025.000000 |  | 9.950000 | 0.000000 | 10000.000000 | 40.000000 |  | 2.060000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 12:00:00 | 40.000000 | 7.890000 | 8.720000 | 87.000000 | 1026.000000 |  | 9.950000 | 0.540000 | 10000.000000 | 40.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 13:00:00 | 20.000000 | 8.980000 | 11.340000 | 82.000000 | 1026.000000 |  | 11.950000 | 2.300000 | 10000.000000 | 40.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 14:00:00 | 20.000000 | 7.980000 | 14.150000 | 63.000000 | 1027.000000 |  | 14.950000 | 5.450000 | 10000.000000 | 50.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 15:00:00 | 40.000000 | 5.880000 | 15.950000 | 48.000000 | 1027.000000 |  | 16.950000 | 9.170000 | 10000.000000 | 170.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 16:00:00 | 75.000000 | 4.700000 | 17.920000 | 39.000000 | 1026.000000 |  | 18.950000 | 12.180000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 17:00:00 | 75.000000 | 3.950000 | 17.870000 | 37.000000 | 1025.000000 |  | 18.950000 | 13.250000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 18:00:00 | 40.000000 | 7.960000 | 17.160000 | 52.000000 | 1025.000000 |  | 17.950000 | 12.020000 | 10000.000000 | 290.000000 |  | 4.120000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 19:00:00 | 40.000000 | 8.890000 | 18.260000 | 52.000000 | 1024.000000 |  | 18.950000 | 7.480000 | 10000.000000 | 300.000000 |  | 4.630000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 20:00:00 | 40.000000 | 8.890000 | 18.260000 | 52.000000 | 1023.000000 | 0.22 | 18.950000 | 4.350000 | 10000.000000 | 280.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 21:00:00 | 40.000000 | 8.790000 | 17.240000 | 55.000000 | 1023.000000 | 0.31 | 17.950000 | 1.780000 | 10000.000000 | 280.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 22:00:00 | 40.000000 | 9.870000 | 16.350000 | 63.000000 | 1023.000000 | 0.24 | 16.950000 | 0.420000 | 10000.000000 | 280.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206630 | "BILBAO MAXIMO POTI [21206630]" | 4.751139 | -74.091583 | 2600.000000 | Clim?tica Ordinaria | Convencional | Suspendida | 2001-11-15 00:00:00 | 2018-04-12 16:36:29 | Bogot? | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andr?s | Magdalena Cauca | Alto Magdalena | R?o Bogot? | America/Bogota | 2022-02-02 23:00:00 | 40.000000 | 9.950000 | 14.380000 | 72.000000 | 1023.000000 | 0.13 | 14.950000 | 0.000000 | 10000.000000 | 280.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206630_OWM_Clouds_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Clouds_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Dewpoint_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Dewpoint_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Feelslike_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Feelslike_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Humidity_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Humidity_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Pressure_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Pressure_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Rain_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Rain_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Temp_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Temp_20220203.png)
![CNE_IDEAM_Station21206630_OWM_UVI_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_UVI_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Visibility_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Visibility_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Winddeg_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Winddeg_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Windgust_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Windgust_20220203.png)
![CNE_IDEAM_Station21206630_OWM_Windspeed_20220203.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206630_OWM_Windspeed_20220203.png)
