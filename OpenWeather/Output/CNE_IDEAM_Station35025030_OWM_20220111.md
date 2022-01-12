
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - PACHAQUIARO [35025030] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35025030_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.06666667,-73.18333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.06666667&lon=-73.18333333)


| Parameter | Value |
|---|---|
| Code | 35025030 |
| Name | PACHAQUIARO [35025030] |
| Latitude, ° | 4.06666667 |
| Longitude, ° | -73.18333333 |
| Elevation, m | 200 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-06-15 00:00:00 |
| Suspension date | 1986-06-15 00:00:00 |
| State | Meta |
| County | Puerto López |
| Stream | Prado |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Negro |

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

### (CNE index 1415) Open Weather values for station 35025030 - PACHAQUIARO [35025030]

JSON data from API OWM:

```
{'lat': 4.0667, 'lon': -73.1833, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812582, 'sunset': 1641855425, 'temp': 32.89, 'feels_like': 32.48, 'pressure': 1007, 'humidity': 34, 'dew_point': 14.96, 'uvi': 1.52, 'clouds': 65, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 56, 'wind_gust': 3.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 27.62, 'feels_like': 27.96, 'pressure': 1010, 'humidity': 49, 'dew_point': 15.95, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 20, 'wind_gust': 3.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 27.53, 'feels_like': 27.79, 'pressure': 1011, 'humidity': 48, 'dew_point': 15.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.91, 'wind_deg': 24, 'wind_gust': 3.86, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 27.28, 'feels_like': 27.55, 'pressure': 1012, 'humidity': 48, 'dew_point': 15.32, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.14, 'wind_deg': 17, 'wind_gust': 5.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 27.02, 'feels_like': 27.32, 'pressure': 1012, 'humidity': 48, 'dew_point': 15.08, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 14, 'wind_gust': 6.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 26.92, 'feels_like': 27.23, 'pressure': 1012, 'humidity': 48, 'dew_point': 14.99, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.34, 'wind_deg': 10, 'wind_gust': 7.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1012, 'humidity': 49, 'dew_point': 15.05, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 2, 'wind_gust': 7.06, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 25.88, 'feels_like': 25.88, 'pressure': 1011, 'humidity': 52, 'dew_point': 15.28, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 354, 'wind_gust': 2.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 25.4, 'feels_like': 25.41, 'pressure': 1010, 'humidity': 54, 'dew_point': 15.42, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 346, 'wind_gust': 1.47, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 25.15, 'feels_like': 25.13, 'pressure': 1009, 'humidity': 54, 'dew_point': 15.19, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.82, 'wind_deg': 12, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 24.82, 'feels_like': 24.79, 'pressure': 1010, 'humidity': 55, 'dew_point': 15.17, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.05, 'wind_deg': 57, 'wind_gust': 1.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 24.55, 'feels_like': 24.52, 'pressure': 1011, 'humidity': 56, 'dew_point': 15.2, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 63, 'wind_gust': 2.22, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 24.32, 'feels_like': 24.3, 'pressure': 1012, 'humidity': 57, 'dew_point': 15.26, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.4, 'wind_deg': 60, 'wind_gust': 3.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.64, 'feels_like': 24.67, 'pressure': 1013, 'humidity': 58, 'dew_point': 15.83, 'uvi': 0.07, 'clouds': 92, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 54, 'wind_gust': 5.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 25.45, 'feels_like': 25.49, 'pressure': 1014, 'humidity': 55, 'dew_point': 15.76, 'uvi': 1.68, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.83, 'wind_deg': 53, 'wind_gust': 7.45, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.83, 'feels_like': 27.26, 'pressure': 1015, 'humidity': 50, 'dew_point': 15.54, 'uvi': 3.87, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3.05, 'wind_deg': 50, 'wind_gust': 8.33, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.11, 'feels_like': 29.01, 'pressure': 1015, 'humidity': 43, 'dew_point': 15.26, 'uvi': 6.42, 'clouds': 96, 'visibility': 10000, 'wind_speed': 4.39, 'wind_deg': 42, 'wind_gust': 8.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 31.17, 'feels_like': 30.71, 'pressure': 1013, 'humidity': 37, 'dew_point': 14.76, 'uvi': 3.55, 'clouds': 83, 'visibility': 10000, 'wind_speed': 5.11, 'wind_deg': 41, 'wind_gust': 6.77, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 32.61, 'feels_like': 32.1, 'pressure': 1012, 'humidity': 34, 'dew_point': 14.72, 'uvi': 3.82, 'clouds': 73, 'visibility': 10000, 'wind_speed': 5, 'wind_deg': 44, 'wind_gust': 5.56, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 32.87, 'feels_like': 32.45, 'pressure': 1011, 'humidity': 34, 'dew_point': 14.94, 'uvi': 3.42, 'clouds': 38, 'visibility': 10000, 'wind_speed': 4.42, 'wind_deg': 47, 'wind_gust': 4.96, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641841200, 'temp': 33.23, 'feels_like': 32.94, 'pressure': 1009, 'humidity': 34, 'dew_point': 15.26, 'uvi': 2.67, 'clouds': 54, 'visibility': 10000, 'wind_speed': 3.47, 'wind_deg': 51, 'wind_gust': 3.93, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 32.89, 'feels_like': 32.48, 'pressure': 1007, 'humidity': 34, 'dew_point': 14.96, 'uvi': 1.52, 'clouds': 65, 'visibility': 10000, 'wind_speed': 3.27, 'wind_deg': 56, 'wind_gust': 3.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 31.78, 'feels_like': 31.48, 'pressure': 1007, 'humidity': 37, 'dew_point': 15.3, 'uvi': 0.6, 'clouds': 76, 'visibility': 10000, 'wind_speed': 2.89, 'wind_deg': 55, 'wind_gust': 3.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 30.28, 'feels_like': 30.27, 'pressure': 1008, 'humidity': 42, 'dew_point': 15.95, 'uvi': 0.05, 'clouds': 82, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 50, 'wind_gust': 3.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 29.02, 'feels_like': 29.01, 'pressure': 1008, 'humidity': 44, 'dew_point': 15.54, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 43, 'wind_gust': 2.73, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 15.950000 | 27.960000 | 49.000000 | 1010.000000 |  | 27.620000 | 0.000000 | 10000.000000 | 20.000000 | 3.47 | 1.650000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 15.550000 | 27.790000 | 48.000000 | 1011.000000 |  | 27.530000 | 0.000000 | 10000.000000 | 24.000000 | 3.86 | 1.910000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 15.320000 | 27.550000 | 48.000000 | 1012.000000 |  | 27.280000 | 0.000000 | 10000.000000 | 17.000000 | 5.74 | 2.140000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 15.080000 | 27.320000 | 48.000000 | 1012.000000 |  | 27.020000 | 0.000000 | 10000.000000 | 14.000000 | 6.75 | 2.180000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 14.990000 | 27.230000 | 48.000000 | 1012.000000 |  | 26.920000 | 0.000000 | 10000.000000 | 10.000000 | 7.99 | 2.340000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 15.050000 | 26.640000 | 49.000000 | 1012.000000 |  | 26.640000 | 0.000000 | 10000.000000 | 2.000000 | 7.06 | 2.060000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 06:00:00 | 85.000000 | 15.280000 | 25.880000 | 52.000000 | 1011.000000 |  | 25.880000 | 0.000000 | 10000.000000 | 354.000000 | 2.98 | 1.440000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 15.420000 | 25.410000 | 54.000000 | 1010.000000 |  | 25.400000 | 0.000000 | 10000.000000 | 346.000000 | 1.47 | 1.140000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 15.190000 | 25.130000 | 54.000000 | 1009.000000 |  | 25.150000 | 0.000000 | 10000.000000 | 12.000000 | 0.96 | 0.820000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 15.170000 | 24.790000 | 55.000000 | 1010.000000 |  | 24.820000 | 0.000000 | 10000.000000 | 57.000000 | 1.22 | 1.050000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 10:00:00 | 98.000000 | 15.200000 | 24.520000 | 56.000000 | 1011.000000 |  | 24.550000 | 0.000000 | 10000.000000 | 63.000000 | 2.22 | 1.400000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 11:00:00 | 98.000000 | 15.260000 | 24.300000 | 57.000000 | 1012.000000 |  | 24.320000 | 0.000000 | 10000.000000 | 60.000000 | 3.67 | 1.400000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 12:00:00 | 92.000000 | 15.830000 | 24.670000 | 58.000000 | 1013.000000 |  | 24.640000 | 0.070000 | 10000.000000 | 54.000000 | 5.7 | 1.230000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 15.760000 | 25.490000 | 55.000000 | 1014.000000 |  | 25.450000 | 1.680000 | 10000.000000 | 53.000000 | 7.45 | 1.830000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 15.540000 | 27.260000 | 50.000000 | 1015.000000 |  | 26.830000 | 3.870000 | 10000.000000 | 50.000000 | 8.33 | 3.050000 | 804 | Clouds | overcast clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 15:00:00 | 96.000000 | 15.260000 | 29.010000 | 43.000000 | 1015.000000 |  | 29.110000 | 6.420000 | 10000.000000 | 42.000000 | 8.67 | 4.390000 | 804 | Clouds | overcast clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 16:00:00 | 83.000000 | 14.760000 | 30.710000 | 37.000000 | 1013.000000 |  | 31.170000 | 3.550000 | 10000.000000 | 41.000000 | 6.77 | 5.110000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 17:00:00 | 73.000000 | 14.720000 | 32.100000 | 34.000000 | 1012.000000 |  | 32.610000 | 3.820000 | 10000.000000 | 44.000000 | 5.56 | 5.000000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 18:00:00 | 38.000000 | 14.940000 | 32.450000 | 34.000000 | 1011.000000 |  | 32.870000 | 3.420000 | 10000.000000 | 47.000000 | 4.96 | 4.420000 | 802 | Clouds | scattered clouds | 03d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 19:00:00 | 54.000000 | 15.260000 | 32.940000 | 34.000000 | 1009.000000 |  | 33.230000 | 2.670000 | 10000.000000 | 51.000000 | 3.93 | 3.470000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 20:00:00 | 65.000000 | 14.960000 | 32.480000 | 34.000000 | 1007.000000 |  | 32.890000 | 1.520000 | 10000.000000 | 56.000000 | 3.92 | 3.270000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 21:00:00 | 76.000000 | 15.300000 | 31.480000 | 37.000000 | 1007.000000 |  | 31.780000 | 0.600000 | 10000.000000 | 55.000000 | 3.81 | 2.890000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 22:00:00 | 82.000000 | 15.950000 | 30.270000 | 42.000000 | 1008.000000 |  | 30.280000 | 0.050000 | 10000.000000 | 50.000000 | 3.9 | 2.050000 | 803 | Clouds | broken clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35025030 | "PACHAQUIARO [35025030]" | 4.066667 | -73.183333 | 200.000000 | Climática Principal | Convencional | Suspendida | 1968-06-15 00:00:00 | 1986-06-15 00:00:00 | Meta | Puerto López | Prado | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Río Negro | America/Bogota | 2022-01-10 23:00:00 | 86.000000 | 15.540000 | 29.010000 | 44.000000 | 1008.000000 |  | 29.020000 | 0.000000 | 10000.000000 | 43.000000 | 2.73 | 1.700000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35025030_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35025030_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35025030_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35025030_OWM_Windspeed_20220111.png)
