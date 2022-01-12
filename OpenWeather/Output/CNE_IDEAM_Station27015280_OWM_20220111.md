
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PARAMO BELMIRA - AUT [27015280] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station27015280_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=6.63202778,-75.64444444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=6.63202778&lon=-75.64444444)


| Parameter | Value |
|---|---|
| Code | 27015280 |
| Name | PARAMO BELMIRA - AUT [27015280] |
| Latitude, ° | 6.63202778 |
| Longitude, ° | -75.64444444 |
| Elevation, m | 3221 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2004-11-22 19:00:00 |
| Suspension date | NaT |
| State | Antioquia |
| County | Entrerrios |
| Stream | 0 |
| Operator | Area Operativa 01 - Antioquia-Chocó |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Nechí |
| SZH - Hydrographic subzone | Río Porce |

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

### (CNE index 176) Open Weather values for station 27015280 - PARAMO BELMIRA - AUT [27015280]

JSON data from API OWM:

```
{'lat': 6.632, 'lon': -75.6444, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813422, 'sunset': 1641855767, 'temp': 14.13, 'feels_like': 13.64, 'pressure': 1012, 'humidity': 78, 'dew_point': 10.36, 'uvi': 3.45, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 346, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, 'hourly': [{'dt': 1641772800, 'temp': 11.12, 'feels_like': 10.77, 'pressure': 1015, 'humidity': 95, 'dew_point': 10.35, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 46, 'wind_gust': 2.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641776400, 'temp': 9.15, 'feels_like': 9.15, 'pressure': 1016, 'humidity': 96, 'dew_point': 8.55, 'uvi': 0, 'clouds': 60, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 43, 'wind_gust': 1.48, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 8.93, 'feels_like': 8.93, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.33, 'uvi': 0, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.8, 'wind_deg': 46, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 8.93, 'feels_like': 8.93, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.33, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 60, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 8.93, 'feels_like': 8.93, 'pressure': 1017, 'humidity': 96, 'dew_point': 8.33, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 0.42, 'wind_deg': 67, 'wind_gust': 0.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 7.41, 'feels_like': 7.41, 'pressure': 1017, 'humidity': 96, 'dew_point': 6.81, 'uvi': 0, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 65, 'wind_gust': 0.78, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 7.41, 'feels_like': 7.41, 'pressure': 1016, 'humidity': 97, 'dew_point': 6.97, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 56, 'wind_gust': 0.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 7.41, 'feels_like': 7.41, 'pressure': 1015, 'humidity': 97, 'dew_point': 6.97, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.34, 'wind_deg': 53, 'wind_gust': 0.57, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1015, 'humidity': 97, 'dew_point': 6.53, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 45, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 6.75, 'feels_like': 6.75, 'pressure': 1015, 'humidity': 97, 'dew_point': 6.31, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 19, 'wind_gust': 0.58, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 6.97, 'feels_like': 6.97, 'pressure': 1016, 'humidity': 97, 'dew_point': 6.53, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 7, 'wind_gust': 0.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 7.23, 'feels_like': 7.23, 'pressure': 1016, 'humidity': 96, 'dew_point': 6.64, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 336, 'wind_gust': 0.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 7.29, 'feels_like': 7.29, 'pressure': 1017, 'humidity': 95, 'dew_point': 6.54, 'uvi': 0.22, 'clouds': 72, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 63, 'wind_gust': 0.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 9.21, 'feels_like': 9.21, 'pressure': 1018, 'humidity': 88, 'dew_point': 7.33, 'uvi': 1.75, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.24, 'wind_deg': 150, 'wind_gust': 0.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 10.22, 'feels_like': 9.33, 'pressure': 1018, 'humidity': 78, 'dew_point': 6.56, 'uvi': 4.45, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 229, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 10.18, 'feels_like': 9.06, 'pressure': 1017, 'humidity': 69, 'dew_point': 4.75, 'uvi': 7.82, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 243, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.1}}, {'dt': 1641830400, 'temp': 9.37, 'feels_like': 9.37, 'pressure': 1015, 'humidity': 64, 'dew_point': 2.91, 'uvi': 7.9, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 252, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 9.33, 'feels_like': 9.33, 'pressure': 1015, 'humidity': 67, 'dew_point': 3.52, 'uvi': 8.79, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 280, 'wind_gust': 1.38, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.13}}, {'dt': 1641837600, 'temp': 11.14, 'feels_like': 10.19, 'pressure': 1014, 'humidity': 72, 'dew_point': 6.29, 'uvi': 8.11, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 310, 'wind_gust': 1.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641841200, 'temp': 12.29, 'feels_like': 11.53, 'pressure': 1013, 'humidity': 75, 'dew_point': 7.99, 'uvi': 5.83, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.53, 'wind_deg': 345, 'wind_gust': 1.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641844800, 'temp': 14.13, 'feels_like': 13.64, 'pressure': 1012, 'humidity': 78, 'dew_point': 10.36, 'uvi': 3.45, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 346, 'wind_gust': 1.57, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641848400, 'temp': 13.14, 'feels_like': 12.65, 'pressure': 1012, 'humidity': 82, 'dew_point': 10.14, 'uvi': 1.43, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 349, 'wind_gust': 1.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641852000, 'temp': 12.17, 'feels_like': 11.74, 'pressure': 1013, 'humidity': 88, 'dew_point': 10.24, 'uvi': 0.24, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.73, 'wind_deg': 347, 'wind_gust': 1.68, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641855600, 'temp': 10.25, 'feels_like': 9.76, 'pressure': 1014, 'humidity': 93, 'dew_point': 9.17, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 17, 'wind_gust': 1.26, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 00:00:00 | 51.000000 | 10.350000 | 10.770000 | 95.000000 | 1015.000000 | 0.12 | 11.120000 | 0.000000 | 10000.000000 | 46.000000 | 2.05 | 1.230000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 01:00:00 | 60.000000 | 8.550000 | 9.150000 | 96.000000 | 1016.000000 |  | 9.150000 | 0.000000 | 10000.000000 | 43.000000 | 1.48 | 0.970000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 02:00:00 | 57.000000 | 8.330000 | 8.930000 | 96.000000 | 1017.000000 |  | 8.930000 | 0.000000 | 10000.000000 | 46.000000 | 1.05 | 0.800000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 03:00:00 | 61.000000 | 8.330000 | 8.930000 | 96.000000 | 1017.000000 |  | 8.930000 | 0.000000 | 10000.000000 | 60.000000 | 1.05 | 0.750000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 04:00:00 | 71.000000 | 8.330000 | 8.930000 | 96.000000 | 1017.000000 |  | 8.930000 | 0.000000 | 10000.000000 | 67.000000 | 0.65 | 0.420000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 05:00:00 | 72.000000 | 6.810000 | 7.410000 | 96.000000 | 1017.000000 |  | 7.410000 | 0.000000 | 10000.000000 | 65.000000 | 0.78 | 0.580000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 06:00:00 | 89.000000 | 6.970000 | 7.410000 | 97.000000 | 1016.000000 |  | 7.410000 | 0.000000 | 10000.000000 | 56.000000 | 0.6 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 07:00:00 | 99.000000 | 6.970000 | 7.410000 | 97.000000 | 1015.000000 |  | 7.410000 | 0.000000 | 10000.000000 | 53.000000 | 0.57 | 0.340000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 08:00:00 | 93.000000 | 6.530000 | 6.970000 | 97.000000 | 1015.000000 |  | 6.970000 | 0.000000 | 10000.000000 | 45.000000 | 0.66 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 09:00:00 | 90.000000 | 6.310000 | 6.750000 | 97.000000 | 1015.000000 |  | 6.750000 | 0.000000 | 10000.000000 | 19.000000 | 0.58 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 10:00:00 | 85.000000 | 6.530000 | 6.970000 | 97.000000 | 1016.000000 |  | 6.970000 | 0.000000 | 10000.000000 | 7.000000 | 0.7 | 0.240000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 11:00:00 | 79.000000 | 6.640000 | 7.230000 | 96.000000 | 1016.000000 |  | 7.230000 | 0.000000 | 10000.000000 | 336.000000 | 0.66 | 0.220000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 12:00:00 | 72.000000 | 6.540000 | 7.290000 | 95.000000 | 1017.000000 |  | 7.290000 | 0.220000 | 10000.000000 | 63.000000 | 0.56 | 0.250000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 7.330000 | 9.210000 | 88.000000 | 1018.000000 |  | 9.210000 | 1.750000 | 10000.000000 | 150.000000 | 0.56 | 0.240000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 14:00:00 | 61.000000 | 6.560000 | 9.330000 | 78.000000 | 1018.000000 |  | 10.220000 | 4.450000 | 10000.000000 | 229.000000 | 0.7 | 0.480000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 15:00:00 | 70.000000 | 4.750000 | 9.060000 | 69.000000 | 1017.000000 | 0.1 | 10.180000 | 7.820000 | 10000.000000 | 243.000000 | 1.03 | 0.780000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 16:00:00 | 70.000000 | 2.910000 | 9.370000 | 64.000000 | 1015.000000 | 0.11 | 9.370000 | 7.900000 | 10000.000000 | 252.000000 | 1.05 | 0.760000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 17:00:00 | 69.000000 | 3.520000 | 9.330000 | 67.000000 | 1015.000000 | 0.13 | 9.330000 | 8.790000 | 10000.000000 | 280.000000 | 1.38 | 0.530000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 18:00:00 | 80.000000 | 6.290000 | 10.190000 | 72.000000 | 1014.000000 | 0.31 | 11.140000 | 8.110000 | 10000.000000 | 310.000000 | 1.42 | 0.460000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 19:00:00 | 84.000000 | 7.990000 | 11.530000 | 75.000000 | 1013.000000 | 0.29 | 12.290000 | 5.830000 | 10000.000000 | 345.000000 | 1.34 | 0.530000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 20:00:00 | 89.000000 | 10.360000 | 13.640000 | 78.000000 | 1012.000000 | 0.29 | 14.130000 | 3.450000 | 10000.000000 | 346.000000 | 1.57 | 0.650000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 21:00:00 | 93.000000 | 10.140000 | 12.650000 | 82.000000 | 1012.000000 | 0.3 | 13.140000 | 1.430000 | 10000.000000 | 349.000000 | 1.7 | 0.700000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 10.240000 | 11.740000 | 88.000000 | 1013.000000 | 0.29 | 12.170000 | 0.240000 | 10000.000000 | 347.000000 | 1.68 | 0.730000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 27015280 | "PARAMO BELMIRA - AUT [27015280]" | 6.632028 | -75.644444 | 3221.000000 | Climática Principal | Automática con Telemetría | Activa | 2004-11-22 19:00:00 | NaT | Antioquia | Entrerrios | 0 | Area Operativa 01 - Antioquia-Chocó | Magdalena Cauca | Nechí | Río Porce | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 9.170000 | 9.760000 | 93.000000 | 1014.000000 | 0.28 | 10.250000 | 0.000000 | 10000.000000 | 17.000000 | 1.26 | 0.750000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station27015280_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Rain_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Temp_20220111.png)
![CNE_IDEAM_Station27015280_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_UVI_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station27015280_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station27015280_OWM_Windspeed_20220111.png)
