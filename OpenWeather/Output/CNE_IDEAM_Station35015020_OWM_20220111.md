
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - IRACA GRANJA [35015020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35015020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.68333333,-73.7) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.68333333&lon=-73.7)


| Parameter | Value |
|---|---|
| Code | 35015020 |
| Name | IRACA GRANJA [35015020] |
| Latitude, ° | 3.68333333 |
| Longitude, ° | -73.7 |
| Elevation, m | 400 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1960-08-15 00:00:00 |
| Suspension date | 1984-01-15 00:00:00 |
| State | Meta |
| County | San Martín (Meta) |
| Stream | Meche |
| Operator | Area Operativa 03 - Meta-Guaviare-Guainía |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Rio Metica (Guamal - Humadea) |

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

### (CNE index 2212) Open Weather values for station 35015020 - IRACA GRANJA [35015020]

JSON data from API OWM:

```
{'lat': 3.6833, 'lon': -73.7, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812669, 'sunset': 1641855586, 'temp': 30.95, 'feels_like': 30.57, 'pressure': 1008, 'humidity': 38, 'dew_point': 14.98, 'uvi': 2.35, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.66, 'wind_deg': 37, 'wind_gust': 3.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 24.75, 'feels_like': 24.85, 'pressure': 1010, 'humidity': 60, 'dew_point': 16.47, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.97, 'wind_deg': 303, 'wind_gust': 5.68, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.65, 'feels_like': 25.73, 'pressure': 1011, 'humidity': 56, 'dew_point': 16.22, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.64, 'wind_deg': 311, 'wind_gust': 5.12, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 25.75, 'feels_like': 25.79, 'pressure': 1012, 'humidity': 54, 'dew_point': 15.75, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.55, 'wind_deg': 318, 'wind_gust': 4.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 25.82, 'feels_like': 25.84, 'pressure': 1013, 'humidity': 53, 'dew_point': 15.52, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.56, 'wind_deg': 313, 'wind_gust': 4.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 25.8, 'feels_like': 25.79, 'pressure': 1013, 'humidity': 52, 'dew_point': 15.21, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.53, 'wind_deg': 312, 'wind_gust': 5.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 25.58, 'feels_like': 25.55, 'pressure': 1012, 'humidity': 52, 'dew_point': 15, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.28, 'wind_deg': 319, 'wind_gust': 5.03, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 24.86, 'feels_like': 24.81, 'pressure': 1011, 'humidity': 54, 'dew_point': 14.92, 'uvi': 0, 'clouds': 91, 'visibility': 10000, 'wind_speed': 2.26, 'wind_deg': 313, 'wind_gust': 4.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 24.61, 'feels_like': 24.56, 'pressure': 1011, 'humidity': 55, 'dew_point': 14.98, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 313, 'wind_gust': 3.27, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 24.41, 'feels_like': 24.34, 'pressure': 1010, 'humidity': 55, 'dew_point': 14.79, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.88, 'wind_deg': 308, 'wind_gust': 2.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 23.8, 'feels_like': 23.72, 'pressure': 1010, 'humidity': 57, 'dew_point': 14.78, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.69, 'wind_deg': 312, 'wind_gust': 1.7, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 23.64, 'feels_like': 23.57, 'pressure': 1011, 'humidity': 58, 'dew_point': 14.9, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.62, 'wind_deg': 312, 'wind_gust': 1.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 23.37, 'feels_like': 23.28, 'pressure': 1012, 'humidity': 58, 'dew_point': 14.65, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 1.59, 'wind_deg': 308, 'wind_gust': 1.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 24.35, 'feels_like': 24.38, 'pressure': 1013, 'humidity': 59, 'dew_point': 15.83, 'uvi': 0.3, 'clouds': 69, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 334, 'wind_gust': 2.43, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 26.64, 'feels_like': 26.64, 'pressure': 1014, 'humidity': 50, 'dew_point': 15.37, 'uvi': 1.91, 'clouds': 83, 'visibility': 10000, 'wind_speed': 2.84, 'wind_deg': 42, 'wind_gust': 6.69, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 28.28, 'feels_like': 28.14, 'pressure': 1015, 'humidity': 43, 'dew_point': 14.52, 'uvi': 4.45, 'clouds': 72, 'visibility': 10000, 'wind_speed': 4.75, 'wind_deg': 48, 'wind_gust': 6.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 29.53, 'feels_like': 29.16, 'pressure': 1015, 'humidity': 40, 'dew_point': 14.52, 'uvi': 7.43, 'clouds': 67, 'visibility': 10000, 'wind_speed': 5.46, 'wind_deg': 50, 'wind_gust': 6.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 30.12, 'feels_like': 29.6, 'pressure': 1014, 'humidity': 38, 'dew_point': 14.25, 'uvi': 5.35, 'clouds': 65, 'visibility': 10000, 'wind_speed': 5.54, 'wind_deg': 51, 'wind_gust': 5.44, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 30.4, 'feels_like': 29.92, 'pressure': 1013, 'humidity': 38, 'dew_point': 14.5, 'uvi': 5.79, 'clouds': 68, 'visibility': 10000, 'wind_speed': 4.61, 'wind_deg': 40, 'wind_gust': 4.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.84, 'feels_like': 30.44, 'pressure': 1011, 'humidity': 38, 'dew_point': 14.89, 'uvi': 5.22, 'clouds': 61, 'visibility': 10000, 'wind_speed': 3.82, 'wind_deg': 28, 'wind_gust': 4.02, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.08, 'feels_like': 30.73, 'pressure': 1009, 'humidity': 38, 'dew_point': 15.1, 'uvi': 4.07, 'clouds': 81, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 28, 'wind_gust': 3.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.95, 'feels_like': 30.57, 'pressure': 1008, 'humidity': 38, 'dew_point': 14.98, 'uvi': 2.35, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.66, 'wind_deg': 37, 'wind_gust': 3.06, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 30.34, 'feels_like': 30.09, 'pressure': 1008, 'humidity': 40, 'dew_point': 15.24, 'uvi': 0.94, 'clouds': 84, 'visibility': 10000, 'wind_speed': 2.25, 'wind_deg': 37, 'wind_gust': 2.85, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 29.41, 'feels_like': 29.35, 'pressure': 1008, 'humidity': 43, 'dew_point': 15.53, 'uvi': 0.18, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 14, 'wind_gust': 3.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 27.18, 'feels_like': 27.52, 'pressure': 1009, 'humidity': 49, 'dew_point': 15.55, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 2.07, 'wind_deg': 323, 'wind_gust': 4.36, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 00:00:00 | 97.000000 | 16.470000 | 24.850000 | 60.000000 | 1010.000000 |  | 24.750000 | 0.000000 | 10000.000000 | 303.000000 | 5.68 | 2.970000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 16.220000 | 25.730000 | 56.000000 | 1011.000000 |  | 25.650000 | 0.000000 | 10000.000000 | 311.000000 | 5.12 | 2.640000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 02:00:00 | 99.000000 | 15.750000 | 25.790000 | 54.000000 | 1012.000000 |  | 25.750000 | 0.000000 | 10000.000000 | 318.000000 | 4.95 | 2.550000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 03:00:00 | 99.000000 | 15.520000 | 25.840000 | 53.000000 | 1013.000000 |  | 25.820000 | 0.000000 | 10000.000000 | 313.000000 | 4.78 | 2.560000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 15.210000 | 25.790000 | 52.000000 | 1013.000000 |  | 25.800000 | 0.000000 | 10000.000000 | 312.000000 | 5.01 | 2.530000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 05:00:00 | 99.000000 | 15.000000 | 25.550000 | 52.000000 | 1012.000000 |  | 25.580000 | 0.000000 | 10000.000000 | 319.000000 | 5.03 | 2.280000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 06:00:00 | 91.000000 | 14.920000 | 24.810000 | 54.000000 | 1011.000000 |  | 24.860000 | 0.000000 | 10000.000000 | 313.000000 | 4.05 | 2.260000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 14.980000 | 24.560000 | 55.000000 | 1011.000000 |  | 24.610000 | 0.000000 | 10000.000000 | 313.000000 | 3.27 | 2.050000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 08:00:00 | 95.000000 | 14.790000 | 24.340000 | 55.000000 | 1010.000000 |  | 24.410000 | 0.000000 | 10000.000000 | 308.000000 | 2.44 | 1.880000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 09:00:00 | 96.000000 | 14.780000 | 23.720000 | 57.000000 | 1010.000000 |  | 23.800000 | 0.000000 | 10000.000000 | 312.000000 | 1.7 | 1.690000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 10:00:00 | 97.000000 | 14.900000 | 23.570000 | 58.000000 | 1011.000000 |  | 23.640000 | 0.000000 | 10000.000000 | 312.000000 | 1.76 | 1.620000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 11:00:00 | 94.000000 | 14.650000 | 23.280000 | 58.000000 | 1012.000000 |  | 23.370000 | 0.000000 | 10000.000000 | 308.000000 | 1.77 | 1.590000 | 804 | Clouds | overcast clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 12:00:00 | 69.000000 | 15.830000 | 24.380000 | 59.000000 | 1013.000000 |  | 24.350000 | 0.300000 | 10000.000000 | 334.000000 | 2.43 | 1.230000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 13:00:00 | 83.000000 | 15.370000 | 26.640000 | 50.000000 | 1014.000000 |  | 26.640000 | 1.910000 | 10000.000000 | 42.000000 | 6.69 | 2.840000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 14:00:00 | 72.000000 | 14.520000 | 28.140000 | 43.000000 | 1015.000000 |  | 28.280000 | 4.450000 | 10000.000000 | 48.000000 | 6.68 | 4.750000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 15:00:00 | 67.000000 | 14.520000 | 29.160000 | 40.000000 | 1015.000000 |  | 29.530000 | 7.430000 | 10000.000000 | 50.000000 | 6.08 | 5.460000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 16:00:00 | 65.000000 | 14.250000 | 29.600000 | 38.000000 | 1014.000000 |  | 30.120000 | 5.350000 | 10000.000000 | 51.000000 | 5.44 | 5.540000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 17:00:00 | 68.000000 | 14.500000 | 29.920000 | 38.000000 | 1013.000000 |  | 30.400000 | 5.790000 | 10000.000000 | 40.000000 | 4.63 | 4.610000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 18:00:00 | 61.000000 | 14.890000 | 30.440000 | 38.000000 | 1011.000000 |  | 30.840000 | 5.220000 | 10000.000000 | 28.000000 | 4.02 | 3.820000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 19:00:00 | 81.000000 | 15.100000 | 30.730000 | 38.000000 | 1009.000000 |  | 31.080000 | 4.070000 | 10000.000000 | 28.000000 | 3.49 | 3.090000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 20:00:00 | 80.000000 | 14.980000 | 30.570000 | 38.000000 | 1008.000000 |  | 30.950000 | 2.350000 | 10000.000000 | 37.000000 | 3.06 | 2.660000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 21:00:00 | 84.000000 | 15.240000 | 30.090000 | 40.000000 | 1008.000000 |  | 30.340000 | 0.940000 | 10000.000000 | 37.000000 | 2.85 | 2.250000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 22:00:00 | 86.000000 | 15.530000 | 29.350000 | 43.000000 | 1008.000000 |  | 29.410000 | 0.180000 | 10000.000000 | 14.000000 | 3.51 | 1.760000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35015020 | "IRACA GRANJA [35015020]" | 3.683333 | -73.700000 | 400.000000 | Climática Principal | Convencional | Suspendida | 1960-08-15 00:00:00 | 1984-01-15 00:00:00 | Meta | San Martín (Meta) | Meche | Area Operativa 03 - Meta-Guaviare-Guainía | Orinoco | Meta | Rio Metica (Guamal - Humadea) | America/Bogota | 2022-01-10 23:00:00 | 87.000000 | 15.550000 | 27.520000 | 49.000000 | 1009.000000 |  | 27.180000 | 0.000000 | 10000.000000 | 323.000000 | 4.36 | 2.070000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station35015020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35015020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35015020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35015020_OWM_Windspeed_20220111.png)
