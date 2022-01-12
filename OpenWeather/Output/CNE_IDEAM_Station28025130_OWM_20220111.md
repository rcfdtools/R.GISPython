
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA LOMA CARBONES - AUT [28025130] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station28025130_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=9.64061111,-73.52394444) or [Openstreet Map](https://www.openstreetmap.org/query?lat=9.64061111&lon=-73.52394444)


| Parameter | Value |
|---|---|
| Code | 28025130 |
| Name | LA LOMA CARBONES - AUT [28025130] |
| Latitude, ° | 9.64061111 |
| Longitude, ° | -73.52394444 |
| Elevation, m | 60 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2010-03-01 19:00:00 |
| Suspension date | NaT |
| State | Cesar |
| County | El Paso |
| Stream | 0 |
| Operator | Area Operativa 05 - Magdalena-Cesar-Guajira |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cesar |
| SZH - Hydrographic subzone | Bajo Cesar |

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

### (CNE index 315) Open Weather values for station 28025130 - LA LOMA CARBONES - AUT [28025130]

JSON data from API OWM:

```
{'lat': 9.6406, 'lon': -73.5239, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813208, 'sunset': 1641854962, 'temp': 36.42, 'feels_like': 35.03, 'pressure': 1007, 'humidity': 22, 'dew_point': 11.3, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 293, 'wind_gust': 2.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 26.74, 'feels_like': 26.82, 'pressure': 1009, 'humidity': 43, 'dew_point': 13.13, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 2.38, 'wind_deg': 95, 'wind_gust': 5.36, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 25.43, 'feels_like': 25.26, 'pressure': 1011, 'humidity': 47, 'dew_point': 13.31, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 2.15, 'wind_deg': 91, 'wind_gust': 4.52, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 24.61, 'feels_like': 24.46, 'pressure': 1011, 'humidity': 51, 'dew_point': 13.81, 'uvi': 0, 'clouds': 28, 'visibility': 10000, 'wind_speed': 2.08, 'wind_deg': 82, 'wind_gust': 4.03, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641783600, 'temp': 24, 'feels_like': 23.84, 'pressure': 1011, 'humidity': 53, 'dew_point': 13.84, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 68, 'wind_gust': 4.23, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641787200, 'temp': 23.28, 'feels_like': 23.1, 'pressure': 1011, 'humidity': 55, 'dew_point': 13.74, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 49, 'wind_gust': 3.2, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 22.48, 'feels_like': 22.3, 'pressure': 1011, 'humidity': 58, 'dew_point': 13.81, 'uvi': 0, 'clouds': 18, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 47, 'wind_gust': 2.62, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641794400, 'temp': 21.67, 'feels_like': 21.51, 'pressure': 1011, 'humidity': 62, 'dew_point': 14.08, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 61, 'wind_gust': 1.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.18, 'feels_like': 21.02, 'pressure': 1011, 'humidity': 64, 'dew_point': 14.11, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 76, 'wind_gust': 1.6, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.84, 'feels_like': 20.7, 'pressure': 1010, 'humidity': 66, 'dew_point': 14.26, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 79, 'wind_gust': 1.42, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 20.58, 'feels_like': 20.42, 'pressure': 1011, 'humidity': 66, 'dew_point': 14.01, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 56, 'wind_gust': 1.5, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.41, 'feels_like': 20.23, 'pressure': 1011, 'humidity': 66, 'dew_point': 13.85, 'uvi': 0, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.36, 'wind_deg': 44, 'wind_gust': 1.57, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 20.1, 'feels_like': 19.92, 'pressure': 1012, 'humidity': 67, 'dew_point': 13.79, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 34, 'wind_gust': 1.02, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 21.78, 'feels_like': 21.63, 'pressure': 1013, 'humidity': 62, 'dew_point': 14.18, 'uvi': 0.37, 'clouds': 68, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 60, 'wind_gust': 1.16, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.63, 'feels_like': 25.55, 'pressure': 1014, 'humidity': 50, 'dew_point': 14.44, 'uvi': 1.71, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 58, 'wind_gust': 2.14, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.86, 'feels_like': 28.64, 'pressure': 1014, 'humidity': 42, 'dew_point': 14.67, 'uvi': 4.22, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 46, 'wind_gust': 2.65, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 31.93, 'feels_like': 31.38, 'pressure': 1014, 'humidity': 35, 'dew_point': 14.57, 'uvi': 7.22, 'clouds': 59, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 10, 'wind_gust': 2.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 34.35, 'feels_like': 33.58, 'pressure': 1012, 'humidity': 29, 'dew_point': 13.76, 'uvi': 9.68, 'clouds': 57, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 319, 'wind_gust': 2.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 36.01, 'feels_like': 35.06, 'pressure': 1011, 'humidity': 25, 'dew_point': 12.89, 'uvi': 10.5, 'clouds': 48, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 302, 'wind_gust': 2.45, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641837600, 'temp': 36.98, 'feels_like': 35.96, 'pressure': 1009, 'humidity': 23, 'dew_point': 12.43, 'uvi': 9.43, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 294, 'wind_gust': 2.48, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 36.77, 'feels_like': 35.48, 'pressure': 1008, 'humidity': 22, 'dew_point': 11.58, 'uvi': 6.6, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.17, 'wind_deg': 293, 'wind_gust': 2.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 36.42, 'feels_like': 35.03, 'pressure': 1007, 'humidity': 22, 'dew_point': 11.3, 'uvi': 3.7, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 293, 'wind_gust': 2.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 35.73, 'feels_like': 34.33, 'pressure': 1006, 'humidity': 23, 'dew_point': 11.39, 'uvi': 1.42, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.56, 'wind_deg': 294, 'wind_gust': 2.24, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 33.73, 'feels_like': 32.62, 'pressure': 1007, 'humidity': 28, 'dew_point': 12.7, 'uvi': 0.28, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 151, 'wind_gust': 1.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 29.18, 'feels_like': 28.7, 'pressure': 1008, 'humidity': 39, 'dew_point': 13.81, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 1.98, 'wind_deg': 132, 'wind_gust': 4.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 00:00:00 | 22.000000 | 13.130000 | 26.820000 | 43.000000 | 1009.000000 |  | 26.740000 | 0.000000 | 10000.000000 | 95.000000 | 5.36 | 2.380000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 01:00:00 | 22.000000 | 13.310000 | 25.260000 | 47.000000 | 1011.000000 |  | 25.430000 | 0.000000 | 10000.000000 | 91.000000 | 4.52 | 2.150000 | 801 | Clouds | few clouds | 02n | 01 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 02:00:00 | 28.000000 | 13.810000 | 24.460000 | 51.000000 | 1011.000000 |  | 24.610000 | 0.000000 | 10000.000000 | 82.000000 | 4.03 | 2.080000 | 802 | Clouds | scattered clouds | 03n | 02 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 03:00:00 | 26.000000 | 13.840000 | 23.840000 | 53.000000 | 1011.000000 |  | 24.000000 | 0.000000 | 10000.000000 | 68.000000 | 4.23 | 2.030000 | 802 | Clouds | scattered clouds | 03n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 04:00:00 | 22.000000 | 13.740000 | 23.100000 | 55.000000 | 1011.000000 |  | 23.280000 | 0.000000 | 10000.000000 | 49.000000 | 3.2 | 1.690000 | 801 | Clouds | few clouds | 02n | 04 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 05:00:00 | 18.000000 | 13.810000 | 22.300000 | 58.000000 | 1011.000000 |  | 22.480000 | 0.000000 | 10000.000000 | 47.000000 | 2.62 | 1.430000 | 801 | Clouds | few clouds | 02n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 06:00:00 | 80.000000 | 14.080000 | 21.510000 | 62.000000 | 1011.000000 |  | 21.670000 | 0.000000 | 10000.000000 | 61.000000 | 1.88 | 1.200000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 07:00:00 | 86.000000 | 14.110000 | 21.020000 | 64.000000 | 1011.000000 |  | 21.180000 | 0.000000 | 10000.000000 | 76.000000 | 1.6 | 1.020000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 08:00:00 | 87.000000 | 14.260000 | 20.700000 | 66.000000 | 1010.000000 |  | 20.840000 | 0.000000 | 10000.000000 | 79.000000 | 1.42 | 1.090000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 09:00:00 | 71.000000 | 14.010000 | 20.420000 | 66.000000 | 1011.000000 |  | 20.580000 | 0.000000 | 10000.000000 | 56.000000 | 1.5 | 1.300000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 10:00:00 | 59.000000 | 13.850000 | 20.230000 | 66.000000 | 1011.000000 |  | 20.410000 | 0.000000 | 10000.000000 | 44.000000 | 1.57 | 1.360000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 11:00:00 | 49.000000 | 13.790000 | 19.920000 | 67.000000 | 1012.000000 |  | 20.100000 | 0.000000 | 10000.000000 | 34.000000 | 1.02 | 0.900000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 12:00:00 | 68.000000 | 14.180000 | 21.630000 | 62.000000 | 1013.000000 |  | 21.780000 | 0.370000 | 10000.000000 | 60.000000 | 1.16 | 0.780000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 13:00:00 | 69.000000 | 14.440000 | 25.550000 | 50.000000 | 1014.000000 |  | 25.630000 | 1.710000 | 10000.000000 | 58.000000 | 2.14 | 1.270000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 14:00:00 | 63.000000 | 14.670000 | 28.640000 | 42.000000 | 1014.000000 |  | 28.860000 | 4.220000 | 10000.000000 | 46.000000 | 2.65 | 1.500000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 15:00:00 | 59.000000 | 14.570000 | 31.380000 | 35.000000 | 1014.000000 |  | 31.930000 | 7.220000 | 10000.000000 | 10.000000 | 2.27 | 1.030000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 16:00:00 | 57.000000 | 13.760000 | 33.580000 | 29.000000 | 1012.000000 |  | 34.350000 | 9.680000 | 10000.000000 | 319.000000 | 2.42 | 0.930000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 17:00:00 | 48.000000 | 12.890000 | 35.060000 | 25.000000 | 1011.000000 |  | 36.010000 | 10.500000 | 10000.000000 | 302.000000 | 2.45 | 1.030000 | 802 | Clouds | scattered clouds | 03d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 18:00:00 | 96.000000 | 12.430000 | 35.960000 | 23.000000 | 1009.000000 |  | 36.980000 | 9.430000 | 10000.000000 | 294.000000 | 2.48 | 1.560000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 11.580000 | 35.480000 | 22.000000 | 1008.000000 |  | 36.770000 | 6.600000 | 10000.000000 | 293.000000 | 2.74 | 2.170000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 11.300000 | 35.030000 | 22.000000 | 1007.000000 |  | 36.420000 | 3.700000 | 10000.000000 | 293.000000 | 2.67 | 2.260000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 11.390000 | 34.330000 | 23.000000 | 1006.000000 |  | 35.730000 | 1.420000 | 10000.000000 | 294.000000 | 2.24 | 1.560000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 22:00:00 | 98.000000 | 12.700000 | 32.620000 | 28.000000 | 1007.000000 |  | 33.730000 | 0.280000 | 10000.000000 | 151.000000 | 1.99 | 0.400000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 28025130 | "LA LOMA CARBONES - AUT [28025130]" | 9.640611 | -73.523944 | 60.000000 | Climática Principal | Automática con Telemetría | Activa | 2010-03-01 19:00:00 | NaT | Cesar | El Paso | 0 | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena Cauca | Cesar | Bajo Cesar | America/Bogota | 2022-01-10 23:00:00 | 88.000000 | 13.810000 | 28.700000 | 39.000000 | 1008.000000 |  | 29.180000 | 0.000000 | 10000.000000 | 132.000000 | 4.56 | 1.980000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station28025130_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Rain_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Temp_20220111.png)
![CNE_IDEAM_Station28025130_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_UVI_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station28025130_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station28025130_OWM_Windspeed_20220111.png)
