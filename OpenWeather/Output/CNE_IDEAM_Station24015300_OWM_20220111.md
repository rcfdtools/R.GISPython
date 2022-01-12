
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VILLA DE LEIVA  - AUT [24015300] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24015300_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.65583333,-73.54394444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.65583333&lon=-73.54394444)


| Parameter | Value |
|---|---|
| Code | 24015300 |
| Name | VILLA DE LEIVA  - AUT [24015300] |
| Latitude, ° | 5.65583333 |
| Longitude, ° | -73.54394444 |
| Elevation, m | 2215 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 1979-12-14 19:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Villa De Leiva |
| Stream | 0 |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Suárez |

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

### (CNE index 825) Open Weather values for station 24015300 - VILLA DE LEIVA  - AUT [24015300]

JSON data from API OWM:

```
{'lat': 5.6558, 'lon': -73.5439, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812823, 'sunset': 1641855357, 'temp': 19.53, 'feels_like': 19.31, 'pressure': 1011, 'humidity': 68, 'dew_point': 13.47, 'uvi': 3.54, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 317, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, 'hourly': [{'dt': 1641772800, 'temp': 14.01, 'feels_like': 14, 'pressure': 1016, 'humidity': 97, 'dew_point': 13.54, 'uvi': 0, 'clouds': 70, 'visibility': 6285, 'wind_speed': 0.73, 'wind_deg': 348, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641776400, 'temp': 13.96, 'feels_like': 13.94, 'pressure': 1017, 'humidity': 97, 'dew_point': 13.49, 'uvi': 0, 'clouds': 93, 'visibility': 5252, 'wind_speed': 0.78, 'wind_deg': 5, 'wind_gust': 1.11, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 13.97, 'feels_like': 13.9, 'pressure': 1018, 'humidity': 95, 'dew_point': 13.18, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 347, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 14.05, 'feels_like': 13.94, 'pressure': 1018, 'humidity': 93, 'dew_point': 12.94, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 343, 'wind_gust': 0.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 13.89, 'feels_like': 13.76, 'pressure': 1018, 'humidity': 93, 'dew_point': 12.78, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.26, 'wind_deg': 9, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 13.79, 'feels_like': 13.63, 'pressure': 1018, 'humidity': 92, 'dew_point': 12.51, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 124, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 13.24, 'feels_like': 13.02, 'pressure': 1017, 'humidity': 92, 'dew_point': 11.97, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 0.47, 'wind_deg': 110, 'wind_gust': 0.6, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 11.86, 'feels_like': 11.58, 'pressure': 1016, 'humidity': 95, 'dew_point': 11.09, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 123, 'wind_gust': 0.74, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 11.16, 'feels_like': 10.81, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.39, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 136, 'wind_gust': 0.78, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 10.84, 'feels_like': 10.46, 'pressure': 1016, 'humidity': 95, 'dew_point': 10.07, 'uvi': 0, 'clouds': 38, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 117, 'wind_gust': 0.91, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 10.6, 'feels_like': 10.22, 'pressure': 1017, 'humidity': 96, 'dew_point': 9.99, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 135, 'wind_gust': 1, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 10.37, 'feels_like': 9.97, 'pressure': 1018, 'humidity': 96, 'dew_point': 9.76, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 151, 'wind_gust': 0.97, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 12.21, 'feels_like': 11.86, 'pressure': 1019, 'humidity': 91, 'dew_point': 10.79, 'uvi': 0.49, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 153, 'wind_gust': 0.83, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 15.19, 'feels_like': 14.88, 'pressure': 1019, 'humidity': 81, 'dew_point': 11.95, 'uvi': 1.55, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 276, 'wind_gust': 0.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 17.82, 'feels_like': 17.46, 'pressure': 1018, 'humidity': 69, 'dew_point': 12.06, 'uvi': 3.7, 'clouds': 45, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 300, 'wind_gust': 0.67, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 19.81, 'feels_like': 19.39, 'pressure': 1017, 'humidity': 59, 'dew_point': 11.57, 'uvi': 6.21, 'clouds': 47, 'visibility': 10000, 'wind_speed': 1.6, 'wind_deg': 317, 'wind_gust': 1.61, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 21.04, 'feels_like': 20.58, 'pressure': 1016, 'humidity': 53, 'dew_point': 11.1, 'uvi': 10.1, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.19, 'wind_deg': 328, 'wind_gust': 2.26, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 21.73, 'feels_like': 21.29, 'pressure': 1014, 'humidity': 51, 'dew_point': 11.16, 'uvi': 10.93, 'clouds': 46, 'visibility': 10000, 'wind_speed': 2.55, 'wind_deg': 332, 'wind_gust': 2.54, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 21.72, 'feels_like': 21.36, 'pressure': 1013, 'humidity': 54, 'dew_point': 12.01, 'uvi': 9.84, 'clouds': 57, 'visibility': 10000, 'wind_speed': 2.69, 'wind_deg': 328, 'wind_gust': 2.38, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 20.64, 'feels_like': 20.33, 'pressure': 1012, 'humidity': 60, 'dew_point': 12.61, 'uvi': 6.19, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.46, 'wind_deg': 319, 'wind_gust': 2.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641844800, 'temp': 19.53, 'feels_like': 19.31, 'pressure': 1011, 'humidity': 68, 'dew_point': 13.47, 'uvi': 3.54, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.23, 'wind_deg': 317, 'wind_gust': 2.49, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.34}}, {'dt': 1641848400, 'temp': 17.82, 'feels_like': 17.77, 'pressure': 1012, 'humidity': 81, 'dew_point': 14.52, 'uvi': 1.4, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 324, 'wind_gust': 2.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641852000, 'temp': 16.56, 'feels_like': 16.6, 'pressure': 1014, 'humidity': 89, 'dew_point': 14.74, 'uvi': 0.23, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 330, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641855600, 'temp': 14.47, 'feels_like': 14.48, 'pressure': 1015, 'humidity': 96, 'dew_point': 13.84, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 330, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 00:00:00 | 70.000000 | 13.540000 | 14.000000 | 97.000000 | 1016.000000 | 0.11 | 14.010000 | 0.000000 | 6285.000000 | 348.000000 | 0.96 | 0.730000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 01:00:00 | 93.000000 | 13.490000 | 13.940000 | 97.000000 | 1017.000000 |  | 13.960000 | 0.000000 | 5252.000000 | 5.000000 | 1.11 | 0.780000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 02:00:00 | 90.000000 | 13.180000 | 13.900000 | 95.000000 | 1018.000000 |  | 13.970000 | 0.000000 | 10000.000000 | 347.000000 | 1.03 | 0.800000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 03:00:00 | 94.000000 | 12.940000 | 13.940000 | 93.000000 | 1018.000000 |  | 14.050000 | 0.000000 | 10000.000000 | 343.000000 | 0.88 | 0.720000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 04:00:00 | 95.000000 | 12.780000 | 13.760000 | 93.000000 | 1018.000000 |  | 13.890000 | 0.000000 | 10000.000000 | 9.000000 | 0.7 | 0.260000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 05:00:00 | 94.000000 | 12.510000 | 13.630000 | 92.000000 | 1018.000000 |  | 13.790000 | 0.000000 | 10000.000000 | 124.000000 | 0.57 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 06:00:00 | 48.000000 | 11.970000 | 13.020000 | 92.000000 | 1017.000000 |  | 13.240000 | 0.000000 | 10000.000000 | 110.000000 | 0.6 | 0.470000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 07:00:00 | 50.000000 | 11.090000 | 11.580000 | 95.000000 | 1016.000000 |  | 11.860000 | 0.000000 | 10000.000000 | 123.000000 | 0.74 | 0.580000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 08:00:00 | 44.000000 | 10.390000 | 10.810000 | 95.000000 | 1016.000000 |  | 11.160000 | 0.000000 | 10000.000000 | 136.000000 | 0.78 | 0.620000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 09:00:00 | 38.000000 | 10.070000 | 10.460000 | 95.000000 | 1016.000000 |  | 10.840000 | 0.000000 | 10000.000000 | 117.000000 | 0.91 | 0.500000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 10:00:00 | 37.000000 | 9.990000 | 10.220000 | 96.000000 | 1017.000000 |  | 10.600000 | 0.000000 | 10000.000000 | 135.000000 | 1 | 0.580000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 11:00:00 | 39.000000 | 9.760000 | 9.970000 | 96.000000 | 1018.000000 |  | 10.370000 | 0.000000 | 10000.000000 | 151.000000 | 0.97 | 0.690000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 12:00:00 | 49.000000 | 10.790000 | 11.860000 | 91.000000 | 1019.000000 |  | 12.210000 | 0.490000 | 10000.000000 | 153.000000 | 0.83 | 0.540000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 13:00:00 | 49.000000 | 11.950000 | 14.880000 | 81.000000 | 1019.000000 |  | 15.190000 | 1.550000 | 10000.000000 | 276.000000 | 0.45 | 0.190000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 14:00:00 | 45.000000 | 12.060000 | 17.460000 | 69.000000 | 1018.000000 |  | 17.820000 | 3.700000 | 10000.000000 | 300.000000 | 0.67 | 0.690000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 15:00:00 | 47.000000 | 11.570000 | 19.390000 | 59.000000 | 1017.000000 |  | 19.810000 | 6.210000 | 10000.000000 | 317.000000 | 1.61 | 1.600000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 16:00:00 | 42.000000 | 11.100000 | 20.580000 | 53.000000 | 1016.000000 |  | 21.040000 | 10.100000 | 10000.000000 | 328.000000 | 2.26 | 2.190000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 17:00:00 | 46.000000 | 11.160000 | 21.290000 | 51.000000 | 1014.000000 |  | 21.730000 | 10.930000 | 10000.000000 | 332.000000 | 2.54 | 2.550000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 18:00:00 | 57.000000 | 12.010000 | 21.360000 | 54.000000 | 1013.000000 |  | 21.720000 | 9.840000 | 10000.000000 | 328.000000 | 2.38 | 2.690000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 19:00:00 | 84.000000 | 12.610000 | 20.330000 | 60.000000 | 1012.000000 | 0.15 | 20.640000 | 6.190000 | 10000.000000 | 319.000000 | 2.2 | 2.460000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 20:00:00 | 82.000000 | 13.470000 | 19.310000 | 68.000000 | 1011.000000 | 0.34 | 19.530000 | 3.540000 | 10000.000000 | 317.000000 | 2.49 | 2.230000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 21:00:00 | 79.000000 | 14.520000 | 17.770000 | 81.000000 | 1012.000000 | 0.65 | 17.820000 | 1.400000 | 10000.000000 | 324.000000 | 2.32 | 1.830000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 22:00:00 | 77.000000 | 14.740000 | 16.600000 | 89.000000 | 1014.000000 | 0.6 | 16.560000 | 0.230000 | 10000.000000 | 330.000000 | 1.94 | 1.410000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24015300 | "VILLA DE LEIVA  - AUT [24015300]" | 5.655833 | -73.543944 | 2215.000000 | Climática Principal | Automática con Telemetría | Activa | 1979-12-14 19:00:00 | NaT | Boyacá | Villa De Leiva | 0 | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Suárez | America/Bogota | 2022-01-10 23:00:00 | 77.000000 | 13.840000 | 14.480000 | 96.000000 | 1015.000000 | 0.25 | 14.470000 | 0.000000 | 10000.000000 | 330.000000 | 1.11 | 1.000000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station24015300_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24015300_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24015300_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24015300_OWM_Windspeed_20220111.png)
