
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - MACEO - AUT [23105070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station23105070_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.57163889,-74.79472222) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.57163889&lon=-74.79472222)


| Parameter | Value |
|---|---|
| Code | 23105070 |
| Name | MACEO - AUT [23105070] |
| Latitude, ° | 6.57163889 |
| Longitude, ° | -74.79472222 |
| Elevation, m | 980 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-06-17 19:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Yolombó |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Medio Magdalena |
| SZH - Hydrographic subzone | Rió San Bartolo y otros directos al Magdalena Medio |

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

### (CNE index 174) Open Weather values for station 23105070 - MACEO - AUT [23105070]

JSON data from API OWM:

```
{'lat': 6.5716, 'lon': -74.7947, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813212, 'sunset': 1641855569, 'temp': 22.07, 'feels_like': 22.45, 'pressure': 1010, 'humidity': 81, 'dew_point': 18.66, 'uvi': 3.42, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 22, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, 'hourly': [{'dt': 1641772800, 'temp': 17.69, 'feels_like': 18.02, 'pressure': 1013, 'humidity': 96, 'dew_point': 17.04, 'uvi': 0, 'clouds': 24, 'visibility': 10000, 'wind_speed': 1.13, 'wind_deg': 311, 'wind_gust': 1.08, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 17.19, 'feels_like': 17.5, 'pressure': 1013, 'humidity': 97, 'dew_point': 16.71, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.42, 'wind_deg': 293, 'wind_gust': 1.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641780000, 'temp': 16.82, 'feels_like': 17.09, 'pressure': 1014, 'humidity': 97, 'dew_point': 16.34, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 287, 'wind_gust': 1.34, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 16.48, 'feels_like': 16.72, 'pressure': 1014, 'humidity': 97, 'dew_point': 16, 'uvi': 0, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 281, 'wind_gust': 1.87, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 16.22, 'feels_like': 16.43, 'pressure': 1014, 'humidity': 97, 'dew_point': 15.74, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 282, 'wind_gust': 1.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 15.99, 'feels_like': 16.18, 'pressure': 1014, 'humidity': 97, 'dew_point': 15.51, 'uvi': 0, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 283, 'wind_gust': 1.94, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 15.79, 'feels_like': 15.96, 'pressure': 1013, 'humidity': 97, 'dew_point': 15.32, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 289, 'wind_gust': 2.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 15.6, 'feels_like': 15.75, 'pressure': 1012, 'humidity': 97, 'dew_point': 15.13, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.67, 'wind_deg': 290, 'wind_gust': 2.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 15.49, 'feels_like': 15.6, 'pressure': 1012, 'humidity': 96, 'dew_point': 14.86, 'uvi': 0, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 292, 'wind_gust': 2.25, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 15.39, 'feels_like': 15.49, 'pressure': 1012, 'humidity': 96, 'dew_point': 14.76, 'uvi': 0, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 294, 'wind_gust': 1.98, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 15.28, 'feels_like': 15.37, 'pressure': 1013, 'humidity': 96, 'dew_point': 14.65, 'uvi': 0, 'clouds': 56, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 302, 'wind_gust': 2.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 15.06, 'feels_like': 15.13, 'pressure': 1014, 'humidity': 96, 'dew_point': 14.43, 'uvi': 0, 'clouds': 50, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 293, 'wind_gust': 1.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 15.79, 'feels_like': 15.88, 'pressure': 1015, 'humidity': 94, 'dew_point': 14.83, 'uvi': 0.41, 'clouds': 30, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 283, 'wind_gust': 1.68, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 18.6, 'feels_like': 18.74, 'pressure': 1016, 'humidity': 85, 'dew_point': 16.03, 'uvi': 1.9, 'clouds': 31, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 292, 'wind_gust': 1.05, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641823200, 'temp': 21.55, 'feels_like': 21.59, 'pressure': 1016, 'humidity': 70, 'dew_point': 15.85, 'uvi': 4.73, 'clouds': 56, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 77, 'wind_gust': 1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 23.08, 'feels_like': 23.09, 'pressure': 1015, 'humidity': 63, 'dew_point': 15.66, 'uvi': 8.13, 'clouds': 42, 'visibility': 10000, 'wind_speed': 1.53, 'wind_deg': 87, 'wind_gust': 1.63, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 23.76, 'feels_like': 23.78, 'pressure': 1014, 'humidity': 61, 'dew_point': 15.8, 'uvi': 7.32, 'clouds': 51, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 86, 'wind_gust': 1.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 23.35, 'feels_like': 23.44, 'pressure': 1013, 'humidity': 65, 'dew_point': 16.4, 'uvi': 8.05, 'clouds': 59, 'visibility': 10000, 'wind_speed': 2.3, 'wind_deg': 78, 'wind_gust': 1.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641837600, 'temp': 22.7, 'feels_like': 22.88, 'pressure': 1012, 'humidity': 71, 'dew_point': 17.17, 'uvi': 7.32, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.72, 'wind_deg': 66, 'wind_gust': 2.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.16}}, {'dt': 1641841200, 'temp': 22.59, 'feels_like': 22.89, 'pressure': 1011, 'humidity': 76, 'dew_point': 18.15, 'uvi': 5.88, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.94, 'wind_deg': 62, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641844800, 'temp': 22.07, 'feels_like': 22.45, 'pressure': 1010, 'humidity': 81, 'dew_point': 18.66, 'uvi': 3.42, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 22, 'wind_gust': 2.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.66}}, {'dt': 1641848400, 'temp': 21, 'feels_like': 21.51, 'pressure': 1010, 'humidity': 90, 'dew_point': 19.3, 'uvi': 1.38, 'clouds': 71, 'visibility': 8486, 'wind_speed': 0.99, 'wind_deg': 355, 'wind_gust': 2.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.86}}, {'dt': 1641852000, 'temp': 19.99, 'feels_like': 20.5, 'pressure': 1011, 'humidity': 94, 'dew_point': 19, 'uvi': 0.31, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 329, 'wind_gust': 2.25, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.82}}, {'dt': 1641855600, 'temp': 17.95, 'feels_like': 18.31, 'pressure': 1012, 'humidity': 96, 'dew_point': 17.3, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 304, 'wind_gust': 1.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 00:00:00 | 24.000000 | 17.040000 | 18.020000 | 96.000000 | 1013.000000 |  | 17.690000 | 0.000000 | 10000.000000 | 311.000000 | 1.08 | 1.130000 | 801 | Clouds | few clouds | 02n | 00 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 01:00:00 | 41.000000 | 16.710000 | 17.500000 | 97.000000 | 1013.000000 |  | 17.190000 | 0.000000 | 10000.000000 | 293.000000 | 1.2 | 1.420000 | 802 | Clouds | scattered clouds | 03n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 02:00:00 | 39.000000 | 16.340000 | 17.090000 | 97.000000 | 1014.000000 |  | 16.820000 | 0.000000 | 10000.000000 | 287.000000 | 1.34 | 1.580000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 03:00:00 | 48.000000 | 16.000000 | 16.720000 | 97.000000 | 1014.000000 |  | 16.480000 | 0.000000 | 10000.000000 | 281.000000 | 1.87 | 1.650000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 04:00:00 | 60.000000 | 15.740000 | 16.430000 | 97.000000 | 1014.000000 |  | 16.220000 | 0.000000 | 10000.000000 | 282.000000 | 1.89 | 1.630000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 05:00:00 | 63.000000 | 15.510000 | 16.180000 | 97.000000 | 1014.000000 |  | 15.990000 | 0.000000 | 10000.000000 | 283.000000 | 1.94 | 1.620000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 06:00:00 | 94.000000 | 15.320000 | 15.960000 | 97.000000 | 1013.000000 |  | 15.790000 | 0.000000 | 10000.000000 | 289.000000 | 2.07 | 1.670000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 07:00:00 | 98.000000 | 15.130000 | 15.750000 | 97.000000 | 1012.000000 |  | 15.600000 | 0.000000 | 10000.000000 | 290.000000 | 2.05 | 1.670000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 08:00:00 | 83.000000 | 14.860000 | 15.600000 | 96.000000 | 1012.000000 |  | 15.490000 | 0.000000 | 10000.000000 | 292.000000 | 2.25 | 1.650000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 09:00:00 | 64.000000 | 14.760000 | 15.490000 | 96.000000 | 1012.000000 |  | 15.390000 | 0.000000 | 10000.000000 | 294.000000 | 1.98 | 1.560000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 10:00:00 | 56.000000 | 14.650000 | 15.370000 | 96.000000 | 1013.000000 |  | 15.280000 | 0.000000 | 10000.000000 | 302.000000 | 2.08 | 1.530000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 11:00:00 | 50.000000 | 14.430000 | 15.130000 | 96.000000 | 1014.000000 |  | 15.060000 | 0.000000 | 10000.000000 | 293.000000 | 1.86 | 1.480000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 12:00:00 | 30.000000 | 14.830000 | 15.880000 | 94.000000 | 1015.000000 |  | 15.790000 | 0.410000 | 10000.000000 | 283.000000 | 1.68 | 1.290000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 13:00:00 | 31.000000 | 16.030000 | 18.740000 | 85.000000 | 1016.000000 |  | 18.600000 | 1.900000 | 10000.000000 | 292.000000 | 1.05 | 0.540000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 14:00:00 | 56.000000 | 15.850000 | 21.590000 | 70.000000 | 1016.000000 |  | 21.550000 | 4.730000 | 10000.000000 | 77.000000 | 1 | 0.600000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 15:00:00 | 42.000000 | 15.660000 | 23.090000 | 63.000000 | 1015.000000 |  | 23.080000 | 8.130000 | 10000.000000 | 87.000000 | 1.63 | 1.530000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 16:00:00 | 51.000000 | 15.800000 | 23.780000 | 61.000000 | 1014.000000 |  | 23.760000 | 7.320000 | 10000.000000 | 86.000000 | 1.77 | 2.050000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 17:00:00 | 59.000000 | 16.400000 | 23.440000 | 65.000000 | 1013.000000 | 0.11 | 23.350000 | 8.050000 | 10000.000000 | 78.000000 | 1.96 | 2.300000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 18:00:00 | 76.000000 | 17.170000 | 22.880000 | 71.000000 | 1012.000000 | 0.16 | 22.700000 | 7.320000 | 10000.000000 | 66.000000 | 2.43 | 1.720000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 19:00:00 | 88.000000 | 18.150000 | 22.890000 | 76.000000 | 1011.000000 | 0.36 | 22.590000 | 5.880000 | 10000.000000 | 62.000000 | 1.9 | 0.940000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 20:00:00 | 76.000000 | 18.660000 | 22.450000 | 81.000000 | 1010.000000 | 0.66 | 22.070000 | 3.420000 | 10000.000000 | 22.000000 | 2.18 | 0.800000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 21:00:00 | 71.000000 | 19.300000 | 21.510000 | 90.000000 | 1010.000000 | 0.86 | 21.000000 | 1.380000 | 8486.000000 | 355.000000 | 2.62 | 0.990000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 19.000000 | 20.500000 | 94.000000 | 1011.000000 | 0.82 | 19.990000 | 0.310000 | 10000.000000 | 329.000000 | 2.25 | 0.970000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 23105070 | "MACEO - AUT [23105070]" | 6.571639 | -74.794722 | 980.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-06-17 19:00:00 | NaT | Antioquia | Yolombó | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Medio Magdalena | Rió San Bartolo y otros directos al Magdalena Medio | America/Bogota | 2022-01-10 23:00:00 | 77.000000 | 17.300000 | 18.310000 | 96.000000 | 1012.000000 | 0.11 | 17.950000 | 0.000000 | 10000.000000 | 304.000000 | 1.17 | 1.310000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station23105070_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Rain_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Temp_20220111.png)
![CNE_IDEAM_Station23105070_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_UVI_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station23105070_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station23105070_OWM_Windspeed_20220111.png)
