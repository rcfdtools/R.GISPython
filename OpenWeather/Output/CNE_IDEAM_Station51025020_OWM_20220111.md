
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - RICAURTE [51025020] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station51025020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.2,-77.98333333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.2&lon=-77.98333333)


| Parameter | Value |
|---|---|
| Code | 51025020 |
| Name | RICAURTE [51025020] |
| Latitude, ° | 1.2 |
| Longitude, ° | -77.98333333 |
| Elevation, m | 1181 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1968-01-15 00:00:00 |
| Suspension date | 1993-10-15 00:00:00 |
| State | Nariño |
| County | Ricaurte (Nariño) |
| Stream | San Pedro |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Pacifico |
| ZH - Hydrographic zone | Mira |
| SZH - Hydrographic subzone | Río Mira |

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

### (CNE index 3589) Open Weather values for station 51025020 - RICAURTE [51025020]

JSON data from API OWM:

```
{'lat': 1.2, 'lon': -77.9833, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813457, 'sunset': 1641856855, 'temp': 25.18, 'feels_like': 26.26, 'pressure': 1014, 'humidity': 96, 'dew_point': 24.5, 'uvi': 4.32, 'clouds': 100, 'visibility': 787, 'wind_speed': 1.38, 'wind_deg': 297, 'wind_gust': 1.55, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, 'hourly': [{'dt': 1641772800, 'temp': 23.18, 'feels_like': 24.11, 'pressure': 1015, 'humidity': 98, 'dew_point': 22.85, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 260, 'wind_gust': 0.45, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641776400, 'temp': 18.48, 'feels_like': 18.92, 'pressure': 1016, 'humidity': 97, 'dew_point': 18, 'uvi': 0, 'clouds': 100, 'visibility': 9121, 'wind_speed': 0.18, 'wind_deg': 187, 'wind_gust': 0.25, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 18.35, 'feels_like': 18.77, 'pressure': 1017, 'humidity': 97, 'dew_point': 17.87, 'uvi': 0, 'clouds': 100, 'visibility': 9353, 'wind_speed': 0.09, 'wind_deg': 165, 'wind_gust': 0.16, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 18.39, 'feels_like': 18.79, 'pressure': 1017, 'humidity': 96, 'dew_point': 17.74, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.48, 'wind_deg': 101, 'wind_gust': 0.55, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 18.03, 'feels_like': 18.42, 'pressure': 1017, 'humidity': 97, 'dew_point': 17.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.08, 'wind_deg': 39, 'wind_gust': 0.34, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 17.78, 'feels_like': 18.15, 'pressure': 1017, 'humidity': 97, 'dew_point': 17.3, 'uvi': 0, 'clouds': 100, 'visibility': 8368, 'wind_speed': 0.43, 'wind_deg': 173, 'wind_gust': 0.52, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 17.86, 'feels_like': 18.23, 'pressure': 1016, 'humidity': 97, 'dew_point': 17.38, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 226, 'wind_gust': 0.77, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 17.62, 'feels_like': 18, 'pressure': 1016, 'humidity': 98, 'dew_point': 17.3, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 215, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641801600, 'temp': 17.79, 'feels_like': 18.16, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.31, 'uvi': 0, 'clouds': 100, 'visibility': 8173, 'wind_speed': 0.48, 'wind_deg': 123, 'wind_gust': 0.56, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641805200, 'temp': 17.84, 'feels_like': 18.19, 'pressure': 1015, 'humidity': 96, 'dew_point': 17.19, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.19, 'wind_deg': 185, 'wind_gust': 0.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641808800, 'temp': 17.68, 'feels_like': 18.04, 'pressure': 1015, 'humidity': 97, 'dew_point': 17.2, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.25, 'wind_deg': 149, 'wind_gust': 0.31, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.34}}, {'dt': 1641812400, 'temp': 17.18, 'feels_like': 17.46, 'pressure': 1016, 'humidity': 96, 'dew_point': 16.54, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.45, 'wind_deg': 111, 'wind_gust': 0.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641816000, 'temp': 18.18, 'feels_like': 18.53, 'pressure': 1017, 'humidity': 95, 'dew_point': 17.37, 'uvi': 0.22, 'clouds': 96, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 136, 'wind_gust': 0.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.31}}, {'dt': 1641819600, 'temp': 20.18, 'feels_like': 20.66, 'pressure': 1017, 'humidity': 92, 'dew_point': 18.84, 'uvi': 1.72, 'clouds': 96, 'visibility': 9642, 'wind_speed': 0.9, 'wind_deg': 305, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641823200, 'temp': 23.18, 'feels_like': 23.93, 'pressure': 1018, 'humidity': 91, 'dew_point': 21.63, 'uvi': 4.46, 'clouds': 98, 'visibility': 6279, 'wind_speed': 1.16, 'wind_deg': 309, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641826800, 'temp': 25.18, 'feels_like': 26.05, 'pressure': 1018, 'humidity': 88, 'dew_point': 23.05, 'uvi': 7.91, 'clouds': 98, 'visibility': 5300, 'wind_speed': 1.8, 'wind_deg': 318, 'wind_gust': 1.4, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.17}}, {'dt': 1641830400, 'temp': 27.18, 'feels_like': 31.25, 'pressure': 1017, 'humidity': 90, 'dew_point': 25.4, 'uvi': 8.79, 'clouds': 98, 'visibility': 5306, 'wind_speed': 1.86, 'wind_deg': 318, 'wind_gust': 1.78, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.68}}, {'dt': 1641834000, 'temp': 26.18, 'feels_like': 26.18, 'pressure': 1016, 'humidity': 89, 'dew_point': 24.22, 'uvi': 9.96, 'clouds': 98, 'visibility': 4685, 'wind_speed': 1.39, 'wind_deg': 321, 'wind_gust': 1.02, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.63}}, {'dt': 1641837600, 'temp': 27.18, 'feels_like': 31.37, 'pressure': 1016, 'humidity': 91, 'dew_point': 25.58, 'uvi': 9.45, 'clouds': 95, 'visibility': 3676, 'wind_speed': 1.83, 'wind_deg': 313, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.74}}, {'dt': 1641841200, 'temp': 28.18, 'feels_like': 35.18, 'pressure': 1015, 'humidity': 95, 'dew_point': 27.3, 'uvi': 6.88, 'clouds': 100, 'visibility': 749, 'wind_speed': 1.51, 'wind_deg': 298, 'wind_gust': 1.64, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.64}}, {'dt': 1641844800, 'temp': 25.18, 'feels_like': 26.26, 'pressure': 1014, 'humidity': 96, 'dew_point': 24.5, 'uvi': 4.32, 'clouds': 100, 'visibility': 787, 'wind_speed': 1.38, 'wind_deg': 297, 'wind_gust': 1.55, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.44}}, {'dt': 1641848400, 'temp': 23.18, 'feels_like': 24.11, 'pressure': 1014, 'humidity': 98, 'dew_point': 22.85, 'uvi': 1.98, 'clouds': 100, 'visibility': 659, 'wind_speed': 1.06, 'wind_deg': 301, 'wind_gust': 1.19, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.06}}, {'dt': 1641852000, 'temp': 22.18, 'feels_like': 23.04, 'pressure': 1014, 'humidity': 99, 'dew_point': 22.02, 'uvi': 0.68, 'clouds': 100, 'visibility': 184, 'wind_speed': 0.74, 'wind_deg': 302, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.8}}, {'dt': 1641855600, 'temp': 22.18, 'feels_like': 23.06, 'pressure': 1015, 'humidity': 100, 'dew_point': 22.18, 'uvi': 0, 'clouds': 100, 'visibility': 117, 'wind_speed': 0.37, 'wind_deg': 314, 'wind_gust': 0.66, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.33}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 22.850000 | 24.110000 | 98.000000 | 1015.000000 | 0.21 | 23.180000 | 0.000000 | 10000.000000 | 260.000000 | 0.45 | 0.350000 | 500 | Rain | light rain | 10n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 18.000000 | 18.920000 | 97.000000 | 1016.000000 |  | 18.480000 | 0.000000 | 9121.000000 | 187.000000 | 0.25 | 0.180000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 17.870000 | 18.770000 | 97.000000 | 1017.000000 |  | 18.350000 | 0.000000 | 9353.000000 | 165.000000 | 0.16 | 0.090000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 17.740000 | 18.790000 | 96.000000 | 1017.000000 |  | 18.390000 | 0.000000 | 10000.000000 | 101.000000 | 0.55 | 0.480000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 17.550000 | 18.420000 | 97.000000 | 1017.000000 |  | 18.030000 | 0.000000 | 10000.000000 | 39.000000 | 0.34 | 0.080000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 17.300000 | 18.150000 | 97.000000 | 1017.000000 |  | 17.780000 | 0.000000 | 8368.000000 | 173.000000 | 0.52 | 0.430000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 06:00:00 | 100.000000 | 17.380000 | 18.230000 | 97.000000 | 1016.000000 |  | 17.860000 | 0.000000 | 10000.000000 | 226.000000 | 0.77 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 07:00:00 | 100.000000 | 17.300000 | 18.000000 | 98.000000 | 1016.000000 | 0.29 | 17.620000 | 0.000000 | 10000.000000 | 215.000000 | 0.64 | 0.450000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 08:00:00 | 100.000000 | 17.310000 | 18.160000 | 97.000000 | 1015.000000 | 0.5 | 17.790000 | 0.000000 | 8173.000000 | 123.000000 | 0.56 | 0.480000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 09:00:00 | 100.000000 | 17.190000 | 18.190000 | 96.000000 | 1015.000000 | 0.64 | 17.840000 | 0.000000 | 10000.000000 | 185.000000 | 0.3 | 0.190000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 10:00:00 | 100.000000 | 17.200000 | 18.040000 | 97.000000 | 1015.000000 | 0.34 | 17.680000 | 0.000000 | 10000.000000 | 149.000000 | 0.31 | 0.250000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 11:00:00 | 100.000000 | 16.540000 | 17.460000 | 96.000000 | 1016.000000 | 0.3 | 17.180000 | 0.000000 | 10000.000000 | 111.000000 | 0.43 | 0.450000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 12:00:00 | 96.000000 | 17.370000 | 18.530000 | 95.000000 | 1017.000000 | 0.31 | 18.180000 | 0.220000 | 10000.000000 | 136.000000 | 0.42 | 0.220000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 13:00:00 | 96.000000 | 18.840000 | 20.660000 | 92.000000 | 1017.000000 | 0.26 | 20.180000 | 1.720000 | 9642.000000 | 305.000000 | 0.71 | 0.900000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 14:00:00 | 98.000000 | 21.630000 | 23.930000 | 91.000000 | 1018.000000 | 0.36 | 23.180000 | 4.460000 | 6279.000000 | 309.000000 | 0.71 | 1.160000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 15:00:00 | 98.000000 | 23.050000 | 26.050000 | 88.000000 | 1018.000000 | 1.17 | 25.180000 | 7.910000 | 5300.000000 | 318.000000 | 1.4 | 1.800000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 25.400000 | 31.250000 | 90.000000 | 1017.000000 | 1.68 | 27.180000 | 8.790000 | 5306.000000 | 318.000000 | 1.78 | 1.860000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 24.220000 | 26.180000 | 89.000000 | 1016.000000 | 1.63 | 26.180000 | 9.960000 | 4685.000000 | 321.000000 | 1.02 | 1.390000 | 501 | Rain | moderate rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 18:00:00 | 95.000000 | 25.580000 | 31.370000 | 91.000000 | 1016.000000 | 1.74 | 27.180000 | 9.450000 | 3676.000000 | 313.000000 | 1.64 | 1.830000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 27.300000 | 35.180000 | 95.000000 | 1015.000000 | 1.64 | 28.180000 | 6.880000 | 749.000000 | 298.000000 | 1.64 | 1.510000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 20:00:00 | 100.000000 | 24.500000 | 26.260000 | 96.000000 | 1014.000000 | 1.44 | 25.180000 | 4.320000 | 787.000000 | 297.000000 | 1.55 | 1.380000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 21:00:00 | 100.000000 | 22.850000 | 24.110000 | 98.000000 | 1014.000000 | 1.06 | 23.180000 | 1.980000 | 659.000000 | 301.000000 | 1.19 | 1.060000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 22:00:00 | 100.000000 | 22.020000 | 23.040000 | 99.000000 | 1014.000000 | 0.8 | 22.180000 | 0.680000 | 184.000000 | 302.000000 | 0.94 | 0.740000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 51025020 | "RICAURTE [51025020]" | 1.200000 | -77.983333 | 1181.000000 | Climática Principal | Convencional | Suspendida | 1968-01-15 00:00:00 | 1993-10-15 00:00:00 | Nariño | Ricaurte (Nariño) | San Pedro | Area Operativa 07 - Nariño-Putumayo | Pacifico | Mira | Río Mira | America/Bogota | 2022-01-10 23:00:00 | 100.000000 | 22.180000 | 23.060000 | 100.000000 | 1015.000000 | 1.33 | 22.180000 | 0.000000 | 117.000000 | 314.000000 | 0.66 | 0.370000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station51025020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station51025020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station51025020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station51025020_OWM_Windspeed_20220111.png)
