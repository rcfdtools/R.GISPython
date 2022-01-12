
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - HIDROPARAISO [21206160] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206160_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.57316667,-74.40483333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.57316667&lon=-74.40483333)


| Parameter | Value |
|---|---|
| Code | 21206160 |
| Name | HIDROPARAISO [21206160] |
| Latitude, ° | 4.57316667 |
| Longitude, ° | -74.40483333 |
| Elevation, m | 1600 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1984-04-15 00:00:00 |
| Suspension date | 1998-12-15 00:00:00 |
| State | Cundinamarca |
| County | El Colegio |
| Stream | Meta |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Bogotá |

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

### (CNE index 2305) Open Weather values for station 21206160 - HIDROPARAISO [21206160]

JSON data from API OWM:

```
{'lat': 4.5732, 'lon': -74.4048, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812924, 'sunset': 1641855669, 'temp': 23.76, 'feels_like': 24.18, 'pressure': 1011, 'humidity': 76, 'dew_point': 19.28, 'uvi': 4.08, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 262, 'wind_gust': 1.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.8}}, 'hourly': [{'dt': 1641772800, 'temp': 18.76, 'feels_like': 19.02, 'pressure': 1014, 'humidity': 89, 'dew_point': 16.91, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 66, 'wind_gust': 1.55, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641776400, 'temp': 19.76, 'feels_like': 20.14, 'pressure': 1015, 'humidity': 90, 'dew_point': 18.07, 'uvi': 0, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.7, 'wind_deg': 64, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.7}}, {'dt': 1641780000, 'temp': 18.76, 'feels_like': 18.99, 'pressure': 1015, 'humidity': 88, 'dew_point': 16.73, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 1.61, 'wind_deg': 66, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641783600, 'temp': 18.76, 'feels_like': 18.96, 'pressure': 1016, 'humidity': 87, 'dew_point': 16.55, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 66, 'wind_gust': 1.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.76, 'feels_like': 18.99, 'pressure': 1016, 'humidity': 88, 'dew_point': 16.73, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 72, 'wind_gust': 1.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641790800, 'temp': 16.76, 'feels_like': 16.76, 'pressure': 1015, 'humidity': 87, 'dew_point': 14.59, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.66, 'wind_deg': 80, 'wind_gust': 1.61, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.76, 'feels_like': 14.56, 'pressure': 1014, 'humidity': 87, 'dew_point': 12.62, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 78, 'wind_gust': 1.4, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641798000, 'temp': 13.76, 'feels_like': 13.46, 'pressure': 1014, 'humidity': 87, 'dew_point': 11.64, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 75, 'wind_gust': 1.2, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641801600, 'temp': 13.76, 'feels_like': 13.46, 'pressure': 1013, 'humidity': 87, 'dew_point': 11.64, 'uvi': 0, 'clouds': 45, 'visibility': 10000, 'wind_speed': 1.41, 'wind_deg': 71, 'wind_gust': 1.36, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641805200, 'temp': 13.76, 'feels_like': 13.46, 'pressure': 1013, 'humidity': 87, 'dew_point': 11.64, 'uvi': 0, 'clouds': 41, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 65, 'wind_gust': 1.28, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 14.76, 'feels_like': 14.62, 'pressure': 1014, 'humidity': 89, 'dew_point': 12.97, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 56, 'wind_gust': 1.22, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641812400, 'temp': 15.76, 'feels_like': 15.74, 'pressure': 1015, 'humidity': 90, 'dew_point': 14.12, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 74, 'wind_gust': 1.39, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 15.76, 'feels_like': 15.64, 'pressure': 1016, 'humidity': 86, 'dew_point': 13.43, 'uvi': 0.51, 'clouds': 78, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 64, 'wind_gust': 1.4, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 16.76, 'feels_like': 16.53, 'pressure': 1016, 'humidity': 78, 'dew_point': 12.91, 'uvi': 2.15, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 304, 'wind_gust': 1.02, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 19.76, 'feels_like': 19.7, 'pressure': 1017, 'humidity': 73, 'dew_point': 14.79, 'uvi': 5.15, 'clouds': 76, 'visibility': 10000, 'wind_speed': 1.65, 'wind_deg': 276, 'wind_gust': 1.19, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.76, 'feels_like': 21.77, 'pressure': 1016, 'humidity': 68, 'dew_point': 15.6, 'uvi': 8.7, 'clouds': 63, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 274, 'wind_gust': 1.59, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 22.76, 'feels_like': 22.81, 'pressure': 1015, 'humidity': 66, 'dew_point': 16.08, 'uvi': 11.7, 'clouds': 61, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 270, 'wind_gust': 1.89, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641834000, 'temp': 22.76, 'feels_like': 22.79, 'pressure': 1013, 'humidity': 65, 'dew_point': 15.84, 'uvi': 12.73, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.6, 'wind_deg': 273, 'wind_gust': 2.15, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 23.76, 'feels_like': 23.99, 'pressure': 1013, 'humidity': 69, 'dew_point': 17.74, 'uvi': 11.55, 'clouds': 42, 'visibility': 10000, 'wind_speed': 2.96, 'wind_deg': 269, 'wind_gust': 2.34, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641841200, 'temp': 23.76, 'feels_like': 24.07, 'pressure': 1011, 'humidity': 72, 'dew_point': 18.41, 'uvi': 7.01, 'clouds': 58, 'visibility': 10000, 'wind_speed': 2.43, 'wind_deg': 268, 'wind_gust': 2.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641844800, 'temp': 23.76, 'feels_like': 24.18, 'pressure': 1011, 'humidity': 76, 'dew_point': 19.28, 'uvi': 4.08, 'clouds': 60, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 262, 'wind_gust': 1.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.8}}, {'dt': 1641848400, 'temp': 23.76, 'feels_like': 24.25, 'pressure': 1011, 'humidity': 79, 'dew_point': 19.9, 'uvi': 1.64, 'clouds': 63, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 268, 'wind_gust': 0.99, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.96}}, {'dt': 1641852000, 'temp': 22.76, 'feels_like': 23.28, 'pressure': 1012, 'humidity': 84, 'dew_point': 19.92, 'uvi': 0.43, 'clouds': 64, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 299, 'wind_gust': 1.06, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641855600, 'temp': 20.76, 'feels_like': 21.19, 'pressure': 1012, 'humidity': 88, 'dew_point': 18.7, 'uvi': 0, 'clouds': 62, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 49, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 00:00:00 | 89.000000 | 16.910000 | 19.020000 | 89.000000 | 1014.000000 | 0.28 | 18.760000 | 0.000000 | 10000.000000 | 66.000000 | 1.55 | 1.180000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 01:00:00 | 90.000000 | 18.070000 | 20.140000 | 90.000000 | 1015.000000 | 0.7 | 19.760000 | 0.000000 | 10000.000000 | 64.000000 | 2.01 | 1.700000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 02:00:00 | 61.000000 | 16.730000 | 18.990000 | 88.000000 | 1015.000000 | 0.21 | 18.760000 | 0.000000 | 10000.000000 | 66.000000 | 1.89 | 1.610000 | 500 | Rain | light rain | 10n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 03:00:00 | 74.000000 | 16.550000 | 18.960000 | 87.000000 | 1016.000000 |  | 18.760000 | 0.000000 | 10000.000000 | 66.000000 | 1.72 | 1.300000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 04:00:00 | 81.000000 | 16.730000 | 18.990000 | 88.000000 | 1016.000000 | 0.25 | 18.760000 | 0.000000 | 10000.000000 | 72.000000 | 1.94 | 1.510000 | 500 | Rain | light rain | 10n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 05:00:00 | 79.000000 | 14.590000 | 16.760000 | 87.000000 | 1015.000000 |  | 16.760000 | 0.000000 | 10000.000000 | 80.000000 | 1.61 | 1.660000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 06:00:00 | 33.000000 | 12.620000 | 14.560000 | 87.000000 | 1014.000000 |  | 14.760000 | 0.000000 | 10000.000000 | 78.000000 | 1.4 | 1.380000 | 802 | Clouds | scattered clouds | 03n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 07:00:00 | 37.000000 | 11.640000 | 13.460000 | 87.000000 | 1014.000000 |  | 13.760000 | 0.000000 | 10000.000000 | 75.000000 | 1.2 | 1.200000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 08:00:00 | 45.000000 | 11.640000 | 13.460000 | 87.000000 | 1013.000000 |  | 13.760000 | 0.000000 | 10000.000000 | 71.000000 | 1.36 | 1.410000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 09:00:00 | 41.000000 | 11.640000 | 13.460000 | 87.000000 | 1013.000000 |  | 13.760000 | 0.000000 | 10000.000000 | 65.000000 | 1.28 | 1.190000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 10:00:00 | 36.000000 | 12.970000 | 14.620000 | 89.000000 | 1014.000000 |  | 14.760000 | 0.000000 | 10000.000000 | 56.000000 | 1.22 | 1.150000 | 802 | Clouds | scattered clouds | 03n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 11:00:00 | 36.000000 | 14.120000 | 15.740000 | 90.000000 | 1015.000000 |  | 15.760000 | 0.000000 | 10000.000000 | 74.000000 | 1.39 | 1.430000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 12:00:00 | 78.000000 | 13.430000 | 15.640000 | 86.000000 | 1016.000000 |  | 15.760000 | 0.510000 | 10000.000000 | 64.000000 | 1.4 | 1.250000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 13:00:00 | 94.000000 | 12.910000 | 16.530000 | 78.000000 | 1016.000000 |  | 16.760000 | 2.150000 | 10000.000000 | 304.000000 | 1.02 | 0.720000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 14:00:00 | 76.000000 | 14.790000 | 19.700000 | 73.000000 | 1017.000000 |  | 19.760000 | 5.150000 | 10000.000000 | 276.000000 | 1.19 | 1.650000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 15:00:00 | 63.000000 | 15.600000 | 21.770000 | 68.000000 | 1016.000000 |  | 21.760000 | 8.700000 | 10000.000000 | 274.000000 | 1.59 | 2.160000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 16:00:00 | 61.000000 | 16.080000 | 22.810000 | 66.000000 | 1015.000000 | 0.11 | 22.760000 | 11.700000 | 10000.000000 | 270.000000 | 1.89 | 2.650000 | 500 | Rain | light rain | 10d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 17:00:00 | 58.000000 | 15.840000 | 22.790000 | 65.000000 | 1013.000000 |  | 22.760000 | 12.730000 | 10000.000000 | 273.000000 | 2.15 | 2.600000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 18:00:00 | 42.000000 | 17.740000 | 23.990000 | 69.000000 | 1013.000000 | 0.15 | 23.760000 | 11.550000 | 10000.000000 | 269.000000 | 2.34 | 2.960000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 19:00:00 | 58.000000 | 18.410000 | 24.070000 | 72.000000 | 1011.000000 | 0.56 | 23.760000 | 7.010000 | 10000.000000 | 268.000000 | 2.19 | 2.430000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 20:00:00 | 60.000000 | 19.280000 | 24.180000 | 76.000000 | 1011.000000 | 0.8 | 23.760000 | 4.080000 | 10000.000000 | 262.000000 | 1.7 | 1.580000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 21:00:00 | 63.000000 | 19.900000 | 24.250000 | 79.000000 | 1011.000000 | 0.96 | 23.760000 | 1.640000 | 10000.000000 | 268.000000 | 0.99 | 1.000000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 22:00:00 | 64.000000 | 19.920000 | 23.280000 | 84.000000 | 1012.000000 | 1.01 | 22.760000 | 0.430000 | 10000.000000 | 299.000000 | 1.06 | 0.920000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206160 | "HIDROPARAISO [21206160]" | 4.573167 | -74.404833 | 1600.000000 | Climática Principal | Convencional | Suspendida | 1984-04-15 00:00:00 | 1998-12-15 00:00:00 | Cundinamarca | El Colegio | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá | America/Bogota | 2022-01-10 23:00:00 | 62.000000 | 18.700000 | 21.190000 | 88.000000 | 1012.000000 | 0.83 | 20.760000 | 0.000000 | 10000.000000 | 49.000000 | 1.22 | 0.720000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21206160_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206160_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206160_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206160_OWM_Windspeed_20220111.png)
