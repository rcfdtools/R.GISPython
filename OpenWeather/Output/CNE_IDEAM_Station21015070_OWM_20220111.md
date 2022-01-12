
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LOS GUACHAROS  - AUT [21015070] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21015070_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.675833,-76.106841) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.675833&lon=-76.106841)


| Parameter | Value |
|---|---|
| Code | 21015070 |
| Name | LOS GUACHAROS  - AUT [21015070] |
| Latitude, ° | 1.675833 |
| Longitude, ° | -76.106841 |
| Elevation, m | 1590 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-24 19:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | Palestina (Huila) |
| Stream | 0 |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Alto Magdalena |

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

### (CNE index 320) Open Weather values for station 21015070 - LOS GUACHAROS  - AUT [21015070]

JSON data from API OWM:

```
{'lat': 1.6758, 'lon': -76.1068, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813052, 'sunset': 1641856358, 'temp': 17.19, 'feels_like': 17.26, 'pressure': 1012, 'humidity': 88, 'dew_point': 15.19, 'uvi': 3.54, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 138, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, 'hourly': [{'dt': 1641772800, 'temp': 13.94, 'feels_like': 13.84, 'pressure': 1014, 'humidity': 94, 'dew_point': 12.99, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 213, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641776400, 'temp': 13.61, 'feels_like': 13.48, 'pressure': 1015, 'humidity': 94, 'dew_point': 12.66, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.71, 'wind_deg': 230, 'wind_gust': 1.07, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 13.45, 'feels_like': 13.31, 'pressure': 1016, 'humidity': 94, 'dew_point': 12.5, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 246, 'wind_gust': 1.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 13.82, 'feels_like': 13.69, 'pressure': 1016, 'humidity': 93, 'dew_point': 12.71, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 243, 'wind_gust': 0.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 13.99, 'feels_like': 13.87, 'pressure': 1016, 'humidity': 93, 'dew_point': 12.88, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 245, 'wind_gust': 0.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 13.98, 'feels_like': 13.86, 'pressure': 1015, 'humidity': 93, 'dew_point': 12.87, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 252, 'wind_gust': 0.73, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641794400, 'temp': 13.7, 'feels_like': 13.61, 'pressure': 1015, 'humidity': 95, 'dew_point': 12.91, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 260, 'wind_gust': 0.74, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.1}}, {'dt': 1641798000, 'temp': 13.79, 'feels_like': 13.68, 'pressure': 1014, 'humidity': 94, 'dew_point': 12.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.57, 'wind_deg': 275, 'wind_gust': 0.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641801600, 'temp': 13.63, 'feels_like': 13.53, 'pressure': 1013, 'humidity': 95, 'dew_point': 12.84, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 262, 'wind_gust': 0.84, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641805200, 'temp': 13.54, 'feels_like': 13.43, 'pressure': 1014, 'humidity': 95, 'dew_point': 12.76, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 277, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.26}}, {'dt': 1641808800, 'temp': 13.36, 'feels_like': 13.23, 'pressure': 1014, 'humidity': 95, 'dew_point': 12.58, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 286, 'wind_gust': 0.66, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 13.28, 'feels_like': 13.12, 'pressure': 1015, 'humidity': 94, 'dew_point': 12.34, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.76, 'wind_deg': 271, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 14.13, 'feels_like': 14.05, 'pressure': 1015, 'humidity': 94, 'dew_point': 13.18, 'uvi': 0.37, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 319, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641819600, 'temp': 15.03, 'feels_like': 14.99, 'pressure': 1016, 'humidity': 92, 'dew_point': 13.74, 'uvi': 0.98, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 119, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641823200, 'temp': 15.52, 'feels_like': 15.53, 'pressure': 1017, 'humidity': 92, 'dew_point': 14.23, 'uvi': 2.43, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.6, 'wind_deg': 117, 'wind_gust': 0.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.46}}, {'dt': 1641826800, 'temp': 16.31, 'feels_like': 16.32, 'pressure': 1016, 'humidity': 89, 'dew_point': 14.49, 'uvi': 4.2, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 117, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641830400, 'temp': 17.86, 'feels_like': 17.87, 'pressure': 1015, 'humidity': 83, 'dew_point': 14.94, 'uvi': 9.47, 'clouds': 96, 'visibility': 8497, 'wind_speed': 1.12, 'wind_deg': 133, 'wind_gust': 1.32, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.92}}, {'dt': 1641834000, 'temp': 18.1, 'feels_like': 18.18, 'pressure': 1014, 'humidity': 85, 'dew_point': 15.54, 'uvi': 10.56, 'clouds': 94, 'visibility': 7152, 'wind_speed': 1.19, 'wind_deg': 134, 'wind_gust': 1.38, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.51}}, {'dt': 1641837600, 'temp': 18.01, 'feels_like': 18.09, 'pressure': 1013, 'humidity': 85, 'dew_point': 15.45, 'uvi': 9.82, 'clouds': 88, 'visibility': 8868, 'wind_speed': 1.32, 'wind_deg': 131, 'wind_gust': 1.48, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}, {'dt': 1641841200, 'temp': 17.69, 'feels_like': 17.76, 'pressure': 1012, 'humidity': 86, 'dew_point': 15.32, 'uvi': 5.79, 'clouds': 96, 'visibility': 8154, 'wind_speed': 1.23, 'wind_deg': 133, 'wind_gust': 1.46, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.16}}, {'dt': 1641844800, 'temp': 17.19, 'feels_like': 17.26, 'pressure': 1012, 'humidity': 88, 'dew_point': 15.19, 'uvi': 3.54, 'clouds': 91, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 138, 'wind_gust': 1.54, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.18}}, {'dt': 1641848400, 'temp': 16.78, 'feels_like': 16.84, 'pressure': 1011, 'humidity': 89, 'dew_point': 14.96, 'uvi': 1.56, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 141, 'wind_gust': 1.67, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}, {'dt': 1641852000, 'temp': 15.98, 'feels_like': 16.04, 'pressure': 1012, 'humidity': 92, 'dew_point': 14.68, 'uvi': 0.5, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.75, 'wind_deg': 159, 'wind_gust': 1.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}, {'dt': 1641855600, 'temp': 14.59, 'feels_like': 14.59, 'pressure': 1013, 'humidity': 95, 'dew_point': 13.8, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.63, 'wind_deg': 176, 'wind_gust': 1.2, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.63}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 12.990000 | 13.840000 | 94.000000 | 1014.000000 | 0.15 | 13.940000 | 0.000000 | 10000.000000 | 213.000000 | 1.01 | 0.640000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 12.660000 | 13.480000 | 94.000000 | 1015.000000 |  | 13.610000 | 0.000000 | 10000.000000 | 230.000000 | 1.07 | 0.710000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 12.500000 | 13.310000 | 94.000000 | 1016.000000 |  | 13.450000 | 0.000000 | 10000.000000 | 246.000000 | 1.03 | 0.750000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 12.710000 | 13.690000 | 93.000000 | 1016.000000 |  | 13.820000 | 0.000000 | 10000.000000 | 243.000000 | 0.94 | 0.790000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 12.880000 | 13.870000 | 93.000000 | 1016.000000 |  | 13.990000 | 0.000000 | 10000.000000 | 245.000000 | 0.86 | 0.650000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 12.870000 | 13.860000 | 93.000000 | 1015.000000 | 0.11 | 13.980000 | 0.000000 | 10000.000000 | 252.000000 | 0.73 | 0.500000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 06:00:00 | 90.000000 | 12.910000 | 13.610000 | 95.000000 | 1015.000000 | 0.1 | 13.700000 | 0.000000 | 10000.000000 | 260.000000 | 0.74 | 0.510000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 12.840000 | 13.680000 | 94.000000 | 1014.000000 | 0.18 | 13.790000 | 0.000000 | 10000.000000 | 275.000000 | 0.67 | 0.570000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 08:00:00 | 98.000000 | 12.840000 | 13.530000 | 95.000000 | 1013.000000 | 0.21 | 13.630000 | 0.000000 | 10000.000000 | 262.000000 | 0.84 | 0.760000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 09:00:00 | 99.000000 | 12.760000 | 13.430000 | 95.000000 | 1014.000000 | 0.26 | 13.540000 | 0.000000 | 10000.000000 | 277.000000 | 0.76 | 0.720000 | 500 | Rain | light rain | 10n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 12.580000 | 13.230000 | 95.000000 | 1014.000000 |  | 13.360000 | 0.000000 | 10000.000000 | 286.000000 | 0.66 | 0.600000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 12.340000 | 13.120000 | 94.000000 | 1015.000000 | 0.12 | 13.280000 | 0.000000 | 10000.000000 | 271.000000 | 0.8 | 0.760000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 13.180000 | 14.050000 | 94.000000 | 1015.000000 | 0.11 | 14.130000 | 0.370000 | 10000.000000 | 319.000000 | 0.45 | 0.200000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 13.740000 | 14.990000 | 92.000000 | 1016.000000 | 0.26 | 15.030000 | 0.980000 | 10000.000000 | 119.000000 | 0.76 | 0.360000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 14.230000 | 15.530000 | 92.000000 | 1017.000000 | 0.46 | 15.520000 | 2.430000 | 10000.000000 | 117.000000 | 0.9 | 0.600000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 15:00:00 | 100.000000 | 14.490000 | 16.320000 | 89.000000 | 1016.000000 | 0.61 | 16.310000 | 4.200000 | 10000.000000 | 117.000000 | 0.82 | 0.650000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 16:00:00 | 96.000000 | 14.940000 | 17.870000 | 83.000000 | 1015.000000 | 0.92 | 17.860000 | 9.470000 | 8497.000000 | 133.000000 | 1.32 | 1.120000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 17:00:00 | 94.000000 | 15.540000 | 18.180000 | 85.000000 | 1014.000000 | 1.51 | 18.100000 | 10.560000 | 7152.000000 | 134.000000 | 1.38 | 1.190000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 18:00:00 | 88.000000 | 15.450000 | 18.090000 | 85.000000 | 1013.000000 | 1.33 | 18.010000 | 9.820000 | 8868.000000 | 131.000000 | 1.48 | 1.320000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 19:00:00 | 96.000000 | 15.320000 | 17.760000 | 86.000000 | 1012.000000 | 1.16 | 17.690000 | 5.790000 | 8154.000000 | 133.000000 | 1.46 | 1.230000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 20:00:00 | 91.000000 | 15.190000 | 17.260000 | 88.000000 | 1012.000000 | 1.18 | 17.190000 | 3.540000 | 10000.000000 | 138.000000 | 1.54 | 1.150000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 14.960000 | 16.840000 | 89.000000 | 1011.000000 | 0.99 | 16.780000 | 1.560000 | 10000.000000 | 141.000000 | 1.67 | 1.010000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 22:00:00 | 88.000000 | 14.680000 | 16.040000 | 92.000000 | 1012.000000 | 0.72 | 15.980000 | 0.500000 | 10000.000000 | 159.000000 | 1.8 | 0.750000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21015070 | "LOS GUACHAROS  - AUT [21015070]" | 1.675833 | -76.106841 | 1590.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-24 19:00:00 | NaT | Huila | Palestina (Huila) | 0 | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Alto Magdalena | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 13.800000 | 14.590000 | 95.000000 | 1013.000000 | 0.63 | 14.590000 | 0.000000 | 10000.000000 | 176.000000 | 1.2 | 0.630000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21015070_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21015070_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21015070_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21015070_OWM_Windspeed_20220111.png)
