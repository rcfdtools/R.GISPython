
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - NEOMUNDO - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23195230_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=7.09999722,-73.11) or [Openstreet Map](https://www.openstreetmap.org/query?lat=7.09999722&lon=-73.11)


| Parameter | Value |
|---|---|
| Code | 23195230 |
| Name | NEOMUNDO |
| Latitude, ° | 7.09999722 |
| Longitude, ° | -73.11 |
| Elevation, m | 970 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Suspendida |
| Installation date | 2005-08-17 00:00:00 |
| Suspension date | 2020-02-28 13:05:29 |
| State | Santander |
| County | Bucaramanga |
| Stream | 0 |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Río Lebrija y otros directos al Magdalena |

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

### (CNE index 175) Open Weather values for station 23195230 - NEOMUNDO

JSON data from API OWM:

```
{'lat': 7.1, 'lon': -73.11, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812859, 'sunset': 1641855113, 'temp': 24.97, 'feels_like': 25.43, 'pressure': 1015, 'humidity': 73, 'dew_point': 19.8, 'uvi': 4.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, 'hourly': [{'dt': 1641772800, 'temp': 20.97, 'feels_like': 21.73, 'pressure': 1015, 'humidity': 100, 'dew_point': 20.97, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 320, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 19.97, 'feels_like': 20.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 19.97, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 320, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 19.97, 'feels_like': 20.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 19.97, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 300, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 19.97, 'feels_like': 20.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 19.97, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 20.97, 'feels_like': 21.58, 'pressure': 1016, 'humidity': 94, 'dew_point': 19.97, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 20.97, 'feels_like': 21.58, 'pressure': 1016, 'humidity': 94, 'dew_point': 19.97, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 19.35, 'feels_like': 19.61, 'pressure': 1015, 'humidity': 87, 'dew_point': 17.13, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 110, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 19.54, 'feels_like': 19.82, 'pressure': 1014, 'humidity': 87, 'dew_point': 17.32, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 114, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 19.59, 'feels_like': 19.88, 'pressure': 1013, 'humidity': 87, 'dew_point': 17.37, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 137, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 19.45, 'feels_like': 19.75, 'pressure': 1014, 'humidity': 88, 'dew_point': 17.41, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 135, 'wind_gust': 0.64, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 19.45, 'feels_like': 19.77, 'pressure': 1014, 'humidity': 89, 'dew_point': 17.59, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 124, 'wind_gust': 0.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641812400, 'temp': 19.97, 'feels_like': 20.32, 'pressure': 1015, 'humidity': 88, 'dew_point': 17.92, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641816000, 'temp': 19.97, 'feels_like': 20.63, 'pressure': 1016, 'humidity': 100, 'dew_point': 19.97, 'uvi': 0.42, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641819600, 'temp': 20.97, 'feels_like': 21.58, 'pressure': 1017, 'humidity': 94, 'dew_point': 19.97, 'uvi': 1.34, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 170, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641823200, 'temp': 22.97, 'feels_like': 23.49, 'pressure': 1018, 'humidity': 83, 'dew_point': 19.93, 'uvi': 3.18, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 140, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641826800, 'temp': 23.97, 'feels_like': 24.33, 'pressure': 1018, 'humidity': 73, 'dew_point': 18.83, 'uvi': 5.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641830400, 'temp': 23.97, 'feels_like': 24.33, 'pressure': 1018, 'humidity': 73, 'dew_point': 18.83, 'uvi': 10.38, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 350, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1017, 'humidity': 69, 'dew_point': 19.84, 'uvi': 11.19, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 340, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1016, 'humidity': 69, 'dew_point': 19.84, 'uvi': 10, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1015, 'humidity': 69, 'dew_point': 19.84, 'uvi': 7.27, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 330, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641844800, 'temp': 24.97, 'feels_like': 25.43, 'pressure': 1015, 'humidity': 73, 'dew_point': 19.8, 'uvi': 4.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641848400, 'temp': 24.97, 'feels_like': 25.43, 'pressure': 1014, 'humidity': 73, 'dew_point': 19.8, 'uvi': 1.58, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.14}}, {'dt': 1641852000, 'temp': 23.97, 'feels_like': 24.33, 'pressure': 1014, 'humidity': 73, 'dew_point': 18.83, 'uvi': 0.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641855600, 'temp': 21.97, 'feels_like': 22.39, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.95, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 20.970000 | 21.730000 | 100.000000 | 1015.000000 |  | 20.970000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 19.970000 | 20.630000 | 100.000000 | 1016.000000 |  | 19.970000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 19.970000 | 20.630000 | 100.000000 | 1016.000000 |  | 19.970000 | 0.000000 | 10000.000000 | 300.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 03:00:00 | 40.000000 | 19.970000 | 20.630000 | 100.000000 | 1016.000000 |  | 19.970000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 04:00:00 | 20.000000 | 19.970000 | 21.580000 | 94.000000 | 1016.000000 |  | 20.970000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 05:00:00 | 20.000000 | 19.970000 | 21.580000 | 94.000000 | 1016.000000 |  | 20.970000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 17.130000 | 19.610000 | 87.000000 | 1015.000000 |  | 19.350000 | 0.000000 | 10000.000000 | 110.000000 | 1.19 | 1.080000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 17.320000 | 19.820000 | 87.000000 | 1014.000000 |  | 19.540000 | 0.000000 | 10000.000000 | 114.000000 | 1.03 | 0.970000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 08:00:00 | 91.000000 | 17.370000 | 19.880000 | 87.000000 | 1013.000000 |  | 19.590000 | 0.000000 | 10000.000000 | 137.000000 | 0.86 | 0.630000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 09:00:00 | 91.000000 | 17.410000 | 19.750000 | 88.000000 | 1014.000000 |  | 19.450000 | 0.000000 | 10000.000000 | 135.000000 | 0.64 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 17.590000 | 19.770000 | 89.000000 | 1014.000000 | 0.1 | 19.450000 | 0.000000 | 10000.000000 | 124.000000 | 0.57 | 0.440000 | 500 | Rain | light rain | 10n | 10 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 11:00:00 | 20.000000 | 17.920000 | 20.320000 | 88.000000 | 1015.000000 |  | 19.970000 | 0.000000 | 10000.000000 | 40.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02n | 11 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 12:00:00 | 20.000000 | 19.970000 | 20.630000 | 100.000000 | 1016.000000 |  | 19.970000 | 0.420000 | 10000.000000 | 140.000000 |  | 1.540000 | 801 | Clouds | few clouds | 02d | 12 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 13:00:00 | 20.000000 | 19.970000 | 21.580000 | 94.000000 | 1017.000000 |  | 20.970000 | 1.340000 | 10000.000000 | 170.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 14:00:00 | 20.000000 | 19.930000 | 23.490000 | 83.000000 | 1018.000000 |  | 22.970000 | 3.180000 | 10000.000000 | 140.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 18.830000 | 24.330000 | 73.000000 | 1018.000000 | 0.1 | 23.970000 | 5.330000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 18.830000 | 24.330000 | 73.000000 | 1018.000000 |  | 23.970000 | 10.380000 | 10000.000000 | 350.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 19.840000 | 25.970000 | 69.000000 | 1017.000000 |  | 25.970000 | 11.190000 | 10000.000000 | 340.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 18:00:00 | 40.000000 | 19.840000 | 25.970000 | 69.000000 | 1016.000000 |  | 25.970000 | 10.000000 | 10000.000000 | 310.000000 |  | 3.090000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 19.840000 | 25.970000 | 69.000000 | 1015.000000 |  | 25.970000 | 7.270000 | 10000.000000 | 330.000000 |  | 2.570000 | 802 | Clouds | scattered clouds | 03d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 20:00:00 | 40.000000 | 19.800000 | 25.430000 | 73.000000 | 1015.000000 | 0.11 | 24.970000 | 4.080000 | 10000.000000 | 320.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 19.800000 | 25.430000 | 73.000000 | 1014.000000 | 0.14 | 24.970000 | 1.580000 | 10000.000000 | 310.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 18.830000 | 24.330000 | 73.000000 | 1014.000000 | 0.16 | 23.970000 | 0.300000 | 10000.000000 | 300.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23195230 | "NEOMUNDO" | 7.099997 | -73.110000 | 970.000000 | Climática Principal | Automática con Telemetría | Suspendida | 2005-08-17 00:00:00 | 2020-02-28 13:05:29 | Santander | Bucaramanga | 0 | Area Operativa 08 - Santanderes-Arauca | Magdalena Cauca | Medio Magdalena | Río Lebrija y otros directos al Magdalena | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 18.950000 | 22.390000 | 83.000000 | 1015.000000 |  | 21.970000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station23195230_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23195230_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23195230_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23195230_OWM_Windspeed_20220111.png)
