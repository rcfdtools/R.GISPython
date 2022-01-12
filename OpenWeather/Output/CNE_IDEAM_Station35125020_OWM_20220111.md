
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VUELTA LARGA [35125020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35125020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.86666667,-72.2) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.86666667&lon=-72.2)


| Parameter | Value |
|---|---|
| Code | 35125020 |
| Name | VUELTA LARGA [35125020] |
| Latitude, ° | 3.86666667 |
| Longitude, ° | -72.2 |
| Elevation, m | 200 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1987-03-15 00:00:00 |
| Suspension date | 1989-08-15 00:00:00 |
| State | Meta |
| County | Puerto López |
| Stream | Chenche |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Manacacias |

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

### (CNE index 1142) Open Weather values for station 35125020 - VUELTA LARGA [35125020]

JSON data from API OWM:

```
{'lat': 3.8667, 'lon': -72.2, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812326, 'sunset': 1641855208, 'temp': 33.3, 'feels_like': 32.69, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.38, 'uvi': 4.37, 'clouds': 8, 'visibility': 10000, 'wind_speed': 6.73, 'wind_deg': 28, 'wind_gust': 7.67, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 30.06, 'feels_like': 29.76, 'pressure': 1009, 'humidity': 40, 'dew_point': 14.99, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 5.88, 'wind_deg': 10, 'wind_gust': 10.27, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 29, 'feels_like': 28.79, 'pressure': 1010, 'humidity': 42, 'dew_point': 14.8, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 5.43, 'wind_deg': 11, 'wind_gust': 11.2, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 29.09, 'feels_like': 28.79, 'pressure': 1011, 'humidity': 41, 'dew_point': 14.51, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 5.57, 'wind_deg': 21, 'wind_gust': 11.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 28.52, 'feels_like': 28.38, 'pressure': 1012, 'humidity': 43, 'dew_point': 14.73, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 5.11, 'wind_deg': 32, 'wind_gust': 11.15, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 27.74, 'feels_like': 27.78, 'pressure': 1011, 'humidity': 45, 'dew_point': 14.73, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 4.48, 'wind_deg': 26, 'wind_gust': 10.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 27.43, 'feels_like': 27.56, 'pressure': 1011, 'humidity': 46, 'dew_point': 14.79, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 4.62, 'wind_deg': 22, 'wind_gust': 10.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.6, 'feels_like': 25.57, 'pressure': 1011, 'humidity': 52, 'dew_point': 15.02, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 3.45, 'wind_deg': 27, 'wind_gust': 9.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.81, 'feels_like': 24.76, 'pressure': 1010, 'humidity': 54, 'dew_point': 14.88, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 3.51, 'wind_deg': 32, 'wind_gust': 9.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.74, 'feels_like': 24.68, 'pressure': 1010, 'humidity': 54, 'dew_point': 14.81, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 3.88, 'wind_deg': 34, 'wind_gust': 10.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.61, 'feels_like': 24.54, 'pressure': 1010, 'humidity': 54, 'dew_point': 14.69, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 4.26, 'wind_deg': 31, 'wind_gust': 10.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.23, 'feels_like': 24.14, 'pressure': 1011, 'humidity': 55, 'dew_point': 14.62, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 4.28, 'wind_deg': 33, 'wind_gust': 10.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.42, 'feels_like': 23.31, 'pressure': 1011, 'humidity': 57, 'dew_point': 14.42, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 3.98, 'wind_deg': 37, 'wind_gust': 10.94, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641816000, 'temp': 24.41, 'feels_like': 24.32, 'pressure': 1013, 'humidity': 54, 'dew_point': 14.51, 'uvi': 0.3, 'clouds': 63, 'visibility': 10000, 'wind_speed': 4.41, 'wind_deg': 32, 'wind_gust': 11.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.8, 'feels_like': 27.02, 'pressure': 1014, 'humidity': 46, 'dew_point': 14.22, 'uvi': 1.21, 'clouds': 76, 'visibility': 10000, 'wind_speed': 6.19, 'wind_deg': 30, 'wind_gust': 11.54, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.46, 'feels_like': 28.24, 'pressure': 1015, 'humidity': 42, 'dew_point': 14.31, 'uvi': 2.7, 'clouds': 79, 'visibility': 10000, 'wind_speed': 7.64, 'wind_deg': 34, 'wind_gust': 11, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.05, 'feels_like': 28.75, 'pressure': 1014, 'humidity': 41, 'dew_point': 14.47, 'uvi': 4.38, 'clouds': 83, 'visibility': 10000, 'wind_speed': 7.66, 'wind_deg': 27, 'wind_gust': 10.42, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.61, 'feels_like': 29.25, 'pressure': 1014, 'humidity': 40, 'dew_point': 14.59, 'uvi': 11.07, 'clouds': 83, 'visibility': 10000, 'wind_speed': 7.51, 'wind_deg': 21, 'wind_gust': 9.88, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.62, 'feels_like': 30.18, 'pressure': 1012, 'humidity': 38, 'dew_point': 14.69, 'uvi': 11.77, 'clouds': 82, 'visibility': 10000, 'wind_speed': 7.5, 'wind_deg': 22, 'wind_gust': 9.37, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 31.33, 'feels_like': 30.91, 'pressure': 1011, 'humidity': 37, 'dew_point': 14.9, 'uvi': 10.42, 'clouds': 7, 'visibility': 10000, 'wind_speed': 7.37, 'wind_deg': 26, 'wind_gust': 9.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641841200, 'temp': 32.97, 'feels_like': 32.42, 'pressure': 1009, 'humidity': 33, 'dew_point': 14.57, 'uvi': 7.77, 'clouds': 9, 'visibility': 10000, 'wind_speed': 7.31, 'wind_deg': 27, 'wind_gust': 8.5, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641844800, 'temp': 33.3, 'feels_like': 32.69, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.38, 'uvi': 4.37, 'clouds': 8, 'visibility': 10000, 'wind_speed': 6.73, 'wind_deg': 28, 'wind_gust': 7.67, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641848400, 'temp': 33.11, 'feels_like': 32.44, 'pressure': 1007, 'humidity': 32, 'dew_point': 14.21, 'uvi': 1.68, 'clouds': 9, 'visibility': 10000, 'wind_speed': 6.2, 'wind_deg': 23, 'wind_gust': 6.98, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1641852000, 'temp': 32.17, 'feels_like': 31.69, 'pressure': 1007, 'humidity': 35, 'dew_point': 14.78, 'uvi': 0.32, 'clouds': 15, 'visibility': 10000, 'wind_speed': 6.15, 'wind_deg': 17, 'wind_gust': 7.04, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641855600, 'temp': 29.84, 'feels_like': 29.4, 'pressure': 1008, 'humidity': 39, 'dew_point': 14.4, 'uvi': 0, 'clouds': 31, 'visibility': 10000, 'wind_speed': 4.85, 'wind_deg': 5, 'wind_gust': 8.71, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 00:00:00 | 80.000000 | 14.990000 | 29.760000 | 40.000000 | 1009.000000 |  | 30.060000 | 0.000000 | 10000.000000 | 10.000000 | 10.27 | 5.880000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 01:00:00 | 86.000000 | 14.800000 | 28.790000 | 42.000000 | 1010.000000 |  | 29.000000 | 0.000000 | 10000.000000 | 11.000000 | 11.2 | 5.430000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 02:00:00 | 92.000000 | 14.510000 | 28.790000 | 41.000000 | 1011.000000 |  | 29.090000 | 0.000000 | 10000.000000 | 21.000000 | 11.25 | 5.570000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 03:00:00 | 92.000000 | 14.730000 | 28.380000 | 43.000000 | 1012.000000 |  | 28.520000 | 0.000000 | 10000.000000 | 32.000000 | 11.15 | 5.110000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 04:00:00 | 92.000000 | 14.730000 | 27.780000 | 45.000000 | 1011.000000 |  | 27.740000 | 0.000000 | 10000.000000 | 26.000000 | 10.99 | 4.480000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 05:00:00 | 93.000000 | 14.790000 | 27.560000 | 46.000000 | 1011.000000 |  | 27.430000 | 0.000000 | 10000.000000 | 22.000000 | 10.91 | 4.620000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 06:00:00 | 70.000000 | 15.020000 | 25.570000 | 52.000000 | 1011.000000 |  | 25.600000 | 0.000000 | 10000.000000 | 27.000000 | 9.54 | 3.450000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 07:00:00 | 78.000000 | 14.880000 | 24.760000 | 54.000000 | 1010.000000 |  | 24.810000 | 0.000000 | 10000.000000 | 32.000000 | 9.74 | 3.510000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 08:00:00 | 84.000000 | 14.810000 | 24.680000 | 54.000000 | 1010.000000 |  | 24.740000 | 0.000000 | 10000.000000 | 34.000000 | 10.42 | 3.880000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 09:00:00 | 89.000000 | 14.690000 | 24.540000 | 54.000000 | 1010.000000 |  | 24.610000 | 0.000000 | 10000.000000 | 31.000000 | 10.77 | 4.260000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 10:00:00 | 91.000000 | 14.620000 | 24.140000 | 55.000000 | 1011.000000 |  | 24.230000 | 0.000000 | 10000.000000 | 33.000000 | 10.9 | 4.280000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 11:00:00 | 91.000000 | 14.420000 | 23.310000 | 57.000000 | 1011.000000 |  | 23.420000 | 0.000000 | 10000.000000 | 37.000000 | 10.94 | 3.980000 | 804 | Clouds | overcast clouds | 04d | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 12:00:00 | 63.000000 | 14.510000 | 24.320000 | 54.000000 | 1013.000000 |  | 24.410000 | 0.300000 | 10000.000000 | 32.000000 | 11.1 | 4.410000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 13:00:00 | 76.000000 | 14.220000 | 27.020000 | 46.000000 | 1014.000000 |  | 26.800000 | 1.210000 | 10000.000000 | 30.000000 | 11.54 | 6.190000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 14:00:00 | 79.000000 | 14.310000 | 28.240000 | 42.000000 | 1015.000000 |  | 28.460000 | 2.700000 | 10000.000000 | 34.000000 | 11 | 7.640000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 15:00:00 | 83.000000 | 14.470000 | 28.750000 | 41.000000 | 1014.000000 |  | 29.050000 | 4.380000 | 10000.000000 | 27.000000 | 10.42 | 7.660000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 16:00:00 | 83.000000 | 14.590000 | 29.250000 | 40.000000 | 1014.000000 |  | 29.610000 | 11.070000 | 10000.000000 | 21.000000 | 9.88 | 7.510000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 17:00:00 | 82.000000 | 14.690000 | 30.180000 | 38.000000 | 1012.000000 |  | 30.620000 | 11.770000 | 10000.000000 | 22.000000 | 9.37 | 7.500000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 18:00:00 | 7.000000 | 14.900000 | 30.910000 | 37.000000 | 1011.000000 |  | 31.330000 | 10.420000 | 10000.000000 | 26.000000 | 9.11 | 7.370000 | 800 | Clear | clear sky | 01d | 18 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 19:00:00 | 9.000000 | 14.570000 | 32.420000 | 33.000000 | 1009.000000 |  | 32.970000 | 7.770000 | 10000.000000 | 27.000000 | 8.5 | 7.310000 | 800 | Clear | clear sky | 01d | 19 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 20:00:00 | 8.000000 | 14.380000 | 32.690000 | 32.000000 | 1007.000000 |  | 33.300000 | 4.370000 | 10000.000000 | 28.000000 | 7.67 | 6.730000 | 800 | Clear | clear sky | 01d | 20 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 21:00:00 | 9.000000 | 14.210000 | 32.440000 | 32.000000 | 1007.000000 |  | 33.110000 | 1.680000 | 10000.000000 | 23.000000 | 6.98 | 6.200000 | 800 | Clear | clear sky | 01d | 21 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 22:00:00 | 15.000000 | 14.780000 | 31.690000 | 35.000000 | 1007.000000 |  | 32.170000 | 0.320000 | 10000.000000 | 17.000000 | 7.04 | 6.150000 | 801 | Clouds | few clouds | 02d | 22 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 35125020 | "VUELTA LARGA [35125020]" | 3.866667 | -72.200000 | 200.000000 | Climática Principal | Convencional | Suspendida | 1987-03-15 00:00:00 | 1989-08-15 00:00:00 | Meta | Puerto López | Chenche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Manacacias | America/Bogota | 2022-01-10 23:00:00 | 31.000000 | 14.400000 | 29.400000 | 39.000000 | 1008.000000 |  | 29.840000 | 0.000000 | 10000.000000 | 5.000000 | 8.71 | 4.850000 | 802 | Clouds | scattered clouds | 03n | 23 |


### Weather plots

![CNE_IDEAM_Station35125020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35125020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35125020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35125020_OWM_Windspeed_20220111.png)
