
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - BELENCITO [24035150] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station24035150_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.78158333,-72.89430556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.78158333&lon=-72.89430556)


| Parameter | Value |
|---|---|
| Code | 24035150 |
| Name | BELENCITO [24035150] |
| Latitude, ° | 5.78158333 |
| Longitude, ° | -72.89430556 |
| Elevation, m | 2530 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1967-02-15 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | Nobsa |
| Stream | Chicamocha |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Sogamoso |
| SZH - Hydrographic subzone | Río Chicamocha |

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

### (CNE index 386) Open Weather values for station 24035150 - BELENCITO [24035150]

JSON data from API OWM:

```
{'lat': 5.7816, 'lon': -72.8943, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812679, 'sunset': 1641855189, 'temp': 17.7, 'feels_like': 17.09, 'pressure': 1011, 'humidity': 60, 'dew_point': 9.85, 'uvi': 4.8, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 325, 'wind_gust': 3.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 11.98, 'feels_like': 11.69, 'pressure': 1016, 'humidity': 94, 'dew_point': 11.05, 'uvi': 0, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.74, 'wind_deg': 320, 'wind_gust': 1.34, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 11.71, 'feels_like': 11.42, 'pressure': 1018, 'humidity': 95, 'dew_point': 10.94, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.79, 'wind_deg': 324, 'wind_gust': 1.31, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 11.38, 'feels_like': 11.05, 'pressure': 1019, 'humidity': 95, 'dew_point': 10.61, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 333, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641783600, 'temp': 10.48, 'feels_like': 10.12, 'pressure': 1019, 'humidity': 97, 'dew_point': 10.02, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 326, 'wind_gust': 1.1, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 9.94, 'feels_like': 9.94, 'pressure': 1019, 'humidity': 97, 'dew_point': 9.49, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 298, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 9.79, 'feels_like': 9.79, 'pressure': 1019, 'humidity': 97, 'dew_point': 9.34, 'uvi': 0, 'clouds': 83, 'visibility': 3737, 'wind_speed': 0.58, 'wind_deg': 271, 'wind_gust': 0.8, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 9.76, 'feels_like': 9.76, 'pressure': 1018, 'humidity': 96, 'dew_point': 9.15, 'uvi': 0, 'clouds': 64, 'visibility': 3187, 'wind_speed': 0.59, 'wind_deg': 268, 'wind_gust': 0.74, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 9.87, 'feels_like': 9.87, 'pressure': 1017, 'humidity': 95, 'dew_point': 9.11, 'uvi': 0, 'clouds': 82, 'visibility': 9538, 'wind_speed': 0.59, 'wind_deg': 292, 'wind_gust': 0.86, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 9.86, 'feels_like': 9.86, 'pressure': 1016, 'humidity': 92, 'dew_point': 8.62, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.86, 'wind_deg': 294, 'wind_gust': 1.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 9.85, 'feels_like': 9.85, 'pressure': 1017, 'humidity': 92, 'dew_point': 8.61, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 308, 'wind_gust': 1.18, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 9.93, 'feels_like': 9.93, 'pressure': 1017, 'humidity': 91, 'dew_point': 8.53, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 310, 'wind_gust': 1.1, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 9.85, 'feels_like': 9.85, 'pressure': 1018, 'humidity': 90, 'dew_point': 8.29, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.15, 'wind_deg': 335, 'wind_gust': 1.14, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 10.15, 'feels_like': 9.54, 'pressure': 1019, 'humidity': 89, 'dew_point': 8.42, 'uvi': 0.42, 'clouds': 43, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 352, 'wind_gust': 1.11, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641819600, 'temp': 12.47, 'feels_like': 11.78, 'pressure': 1019, 'humidity': 77, 'dew_point': 8.55, 'uvi': 2.52, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 312, 'wind_gust': 1.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 14.6, 'feels_like': 13.89, 'pressure': 1019, 'humidity': 68, 'dew_point': 8.77, 'uvi': 5.81, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 295, 'wind_gust': 1.66, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 16.6, 'feels_like': 15.86, 'pressure': 1018, 'humidity': 59, 'dew_point': 8.56, 'uvi': 9.59, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 290, 'wind_gust': 2.24, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 18.16, 'feels_like': 17.39, 'pressure': 1016, 'humidity': 52, 'dew_point': 8.16, 'uvi': 12.58, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.29, 'wind_deg': 279, 'wind_gust': 3.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 19.34, 'feels_like': 18.58, 'pressure': 1014, 'humidity': 48, 'dew_point': 8.06, 'uvi': 13.45, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.55, 'wind_deg': 276, 'wind_gust': 3.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 19.77, 'feels_like': 19.06, 'pressure': 1013, 'humidity': 48, 'dew_point': 8.46, 'uvi': 11.95, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 298, 'wind_gust': 3.88, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 18.85, 'feels_like': 18.17, 'pressure': 1012, 'humidity': 53, 'dew_point': 9.08, 'uvi': 8.57, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 312, 'wind_gust': 3.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 17.7, 'feels_like': 17.09, 'pressure': 1011, 'humidity': 60, 'dew_point': 9.85, 'uvi': 4.8, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 325, 'wind_gust': 3.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 16.52, 'feels_like': 16, 'pressure': 1012, 'humidity': 68, 'dew_point': 10.6, 'uvi': 1.85, 'clouds': 93, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 323, 'wind_gust': 2.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 14.92, 'feels_like': 14.5, 'pressure': 1013, 'humidity': 78, 'dew_point': 11.12, 'uvi': 0.34, 'clouds': 83, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 321, 'wind_gust': 2.87, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 12.2, 'feels_like': 11.85, 'pressure': 1015, 'humidity': 91, 'dew_point': 10.78, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 321, 'wind_gust': 1.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 00:00:00 | 76.000000 | 11.050000 | 11.690000 | 94.000000 | 1016.000000 |  | 11.980000 | 0.000000 | 10000.000000 | 320.000000 | 1.34 | 0.740000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 01:00:00 | 82.000000 | 10.940000 | 11.420000 | 95.000000 | 1018.000000 |  | 11.710000 | 0.000000 | 10000.000000 | 324.000000 | 1.31 | 0.790000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 02:00:00 | 82.000000 | 10.610000 | 11.050000 | 95.000000 | 1019.000000 | 0.12 | 11.380000 | 0.000000 | 10000.000000 | 333.000000 | 1.43 | 0.780000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 03:00:00 | 80.000000 | 10.020000 | 10.120000 | 97.000000 | 1019.000000 |  | 10.480000 | 0.000000 | 10000.000000 | 326.000000 | 1.1 | 0.640000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 04:00:00 | 84.000000 | 9.490000 | 9.940000 | 97.000000 | 1019.000000 |  | 9.940000 | 0.000000 | 10000.000000 | 298.000000 | 0.8 | 0.540000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 05:00:00 | 83.000000 | 9.340000 | 9.790000 | 97.000000 | 1019.000000 |  | 9.790000 | 0.000000 | 3737.000000 | 271.000000 | 0.8 | 0.580000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 06:00:00 | 64.000000 | 9.150000 | 9.760000 | 96.000000 | 1018.000000 |  | 9.760000 | 0.000000 | 3187.000000 | 268.000000 | 0.74 | 0.590000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 07:00:00 | 82.000000 | 9.110000 | 9.870000 | 95.000000 | 1017.000000 |  | 9.870000 | 0.000000 | 9538.000000 | 292.000000 | 0.86 | 0.590000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 08:00:00 | 87.000000 | 8.620000 | 9.860000 | 92.000000 | 1016.000000 |  | 9.860000 | 0.000000 | 10000.000000 | 294.000000 | 1.06 | 0.860000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 09:00:00 | 91.000000 | 8.610000 | 9.850000 | 92.000000 | 1017.000000 |  | 9.850000 | 0.000000 | 10000.000000 | 308.000000 | 1.18 | 0.660000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 8.530000 | 9.930000 | 91.000000 | 1017.000000 |  | 9.930000 | 0.000000 | 10000.000000 | 310.000000 | 1.1 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 11:00:00 | 93.000000 | 8.290000 | 9.850000 | 90.000000 | 1018.000000 |  | 9.850000 | 0.000000 | 10000.000000 | 335.000000 | 1.14 | 0.150000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 12:00:00 | 43.000000 | 8.420000 | 9.540000 | 89.000000 | 1019.000000 |  | 10.150000 | 0.420000 | 10000.000000 | 352.000000 | 1.11 | 0.190000 | 802 | Clouds | scattered clouds | 03d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 13:00:00 | 69.000000 | 8.550000 | 11.780000 | 77.000000 | 1019.000000 |  | 12.470000 | 2.520000 | 10000.000000 | 312.000000 | 1.3 | 0.780000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 14:00:00 | 82.000000 | 8.770000 | 13.890000 | 68.000000 | 1019.000000 |  | 14.600000 | 5.810000 | 10000.000000 | 295.000000 | 1.66 | 1.000000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 15:00:00 | 79.000000 | 8.560000 | 15.860000 | 59.000000 | 1018.000000 |  | 16.600000 | 9.590000 | 10000.000000 | 290.000000 | 2.24 | 1.090000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 16:00:00 | 73.000000 | 8.160000 | 17.390000 | 52.000000 | 1016.000000 |  | 18.160000 | 12.580000 | 10000.000000 | 279.000000 | 3.06 | 1.290000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 17:00:00 | 67.000000 | 8.060000 | 18.580000 | 48.000000 | 1014.000000 |  | 19.340000 | 13.450000 | 10000.000000 | 276.000000 | 3.59 | 1.550000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 18:00:00 | 90.000000 | 8.460000 | 19.060000 | 48.000000 | 1013.000000 |  | 19.770000 | 11.950000 | 10000.000000 | 298.000000 | 3.88 | 1.650000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 19:00:00 | 89.000000 | 9.080000 | 18.170000 | 53.000000 | 1012.000000 |  | 18.850000 | 8.570000 | 10000.000000 | 312.000000 | 3.68 | 1.880000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 20:00:00 | 94.000000 | 9.850000 | 17.090000 | 60.000000 | 1011.000000 |  | 17.700000 | 4.800000 | 10000.000000 | 325.000000 | 3.34 | 1.610000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 21:00:00 | 93.000000 | 10.600000 | 16.000000 | 68.000000 | 1012.000000 |  | 16.520000 | 1.850000 | 10000.000000 | 323.000000 | 2.86 | 1.450000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 22:00:00 | 83.000000 | 11.120000 | 14.500000 | 78.000000 | 1013.000000 |  | 14.920000 | 0.340000 | 10000.000000 | 321.000000 | 2.87 | 1.000000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 24035150 | "BELENCITO [24035150]" | 5.781583 | -72.894306 | 2530.000000 | Climática Principal | Convencional | Activa | 1967-02-15 00:00:00 | NaT | Boyacá | Nobsa | Chicamocha | Area Operativa 06 - Boyacá-Casanare-Vichada | Magdalena Cauca | Sogamoso | Río Chicamocha | America/Bogota | 2022-01-10 23:00:00 | 86.000000 | 10.780000 | 11.850000 | 91.000000 | 1015.000000 |  | 12.200000 | 0.000000 | 10000.000000 | 321.000000 | 1.74 | 0.460000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station24035150_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Rain_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Temp_20220111.png)
![CNE_IDEAM_Station24035150_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_UVI_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station24035150_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station24035150_OWM_Windspeed_20220111.png)
