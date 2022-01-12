
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO BENITO SALAS [21115020] - Historical

### General parameters

* Weather date time: 2022-01-11 19:01:08.491859
* Unix time to eval: 1641841268
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
* CNE IDEAM station code filter: ['All']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* CNE IDEAM technology filter: ['All', 'Automática sin Telemetría']
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['All']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21115020_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.94875,-75.29305556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.94875&lon=-75.29305556)


| Parameter | Value |
|---|---|
| Code | 21115020 |
| Name | AEROPUERTO BENITO SALAS [21115020] |
| Latitude, ° | 2.94875 |
| Longitude, ° | -75.29305556 |
| Elevation, m | 439 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1930-01-15 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | Neiva |
| Stream | Ariari |
| Operator | Area Operativa 04 - Huila-Caquetá |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Rio Fortalecillas y otros |

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

### (CNE index 2014) Open Weather values for station 21115020 - AEROPUERTO BENITO SALAS [21115020]

JSON data from API OWM:

```
{'lat': 2.9488, 'lon': -75.2931, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641841268, 'sunrise': 1641812980, 'sunset': 1641856040, 'temp': 31.97, 'feels_like': 33.19, 'pressure': 1010, 'humidity': 45, 'dew_point': 18.56, 'uvi': 9.12, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, 'hourly': [{'dt': 1641772800, 'temp': 27.97, 'feels_like': 29.52, 'pressure': 1009, 'humidity': 61, 'dew_point': 19.75, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 50, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641776400, 'temp': 27.97, 'feels_like': 29.52, 'pressure': 1010, 'humidity': 61, 'dew_point': 19.75, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 70, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641780000, 'temp': 26.97, 'feels_like': 28.41, 'pressure': 1011, 'humidity': 65, 'dew_point': 19.83, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641783600, 'temp': 26.97, 'feels_like': 28.41, 'pressure': 1011, 'humidity': 65, 'dew_point': 19.83, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641787200, 'temp': 22.85, 'feels_like': 23.28, 'pressure': 1013, 'humidity': 80, 'dew_point': 19.22, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 144, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641790800, 'temp': 22.49, 'feels_like': 22.91, 'pressure': 1013, 'humidity': 81, 'dew_point': 19.07, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.61, 'wind_deg': 103, 'wind_gust': 1.24, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641794400, 'temp': 22.04, 'feels_like': 22.52, 'pressure': 1012, 'humidity': 85, 'dew_point': 19.4, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 78, 'wind_gust': 1.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.35}}, {'dt': 1641798000, 'temp': 22.2, 'feels_like': 22.7, 'pressure': 1012, 'humidity': 85, 'dew_point': 19.56, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 120, 'wind_gust': 0.63, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.28}}, {'dt': 1641801600, 'temp': 21.96, 'feels_like': 22.46, 'pressure': 1011, 'humidity': 86, 'dew_point': 19.51, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 184, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641805200, 'temp': 21.78, 'feels_like': 22.26, 'pressure': 1011, 'humidity': 86, 'dew_point': 19.33, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 167, 'wind_gust': 1.3, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641808800, 'temp': 21.79, 'feels_like': 22.27, 'pressure': 1012, 'humidity': 86, 'dew_point': 19.34, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 189, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641812400, 'temp': 23.97, 'feels_like': 24.59, 'pressure': 1012, 'humidity': 83, 'dew_point': 20.91, 'uvi': 0, 'clouds': 75, 'visibility': 9000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}, {'dt': 1641816000, 'temp': 23.97, 'feels_like': 24.59, 'pressure': 1013, 'humidity': 83, 'dew_point': 20.91, 'uvi': 0.46, 'clouds': 75, 'visibility': 9000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.11}}, {'dt': 1641819600, 'temp': 25.97, 'feels_like': 25.97, 'pressure': 1014, 'humidity': 78, 'dew_point': 21.84, 'uvi': 2.12, 'clouds': 75, 'visibility': 9000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]}, {'dt': 1641823200, 'temp': 27.97, 'feels_like': 29.98, 'pressure': 1015, 'humidity': 65, 'dew_point': 20.78, 'uvi': 5.16, 'clouds': 75, 'visibility': 9000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]}, {'dt': 1641826800, 'temp': 27.97, 'feels_like': 29.98, 'pressure': 1014, 'humidity': 65, 'dew_point': 20.78, 'uvi': 8.8, 'clouds': 75, 'visibility': 9000, 'wind_speed': 2.06, 'wind_deg': 20, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]}, {'dt': 1641830400, 'temp': 28.97, 'feels_like': 31.14, 'pressure': 1014, 'humidity': 61, 'dew_point': 20.69, 'uvi': 11.34, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 40, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641834000, 'temp': 29.97, 'feels_like': 31.66, 'pressure': 1013, 'humidity': 54, 'dew_point': 19.65, 'uvi': 12.5, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 50, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.29}}, {'dt': 1641837600, 'temp': 31.97, 'feels_like': 33.19, 'pressure': 1011, 'humidity': 45, 'dew_point': 18.56, 'uvi': 11.47, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.43}}, {'dt': 1641841200, 'temp': 31.97, 'feels_like': 33.19, 'pressure': 1010, 'humidity': 45, 'dew_point': 18.56, 'uvi': 9.12, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641844800, 'temp': 31.97, 'feels_like': 33.19, 'pressure': 1009, 'humidity': 45, 'dew_point': 18.56, 'uvi': 5.43, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.26}}, {'dt': 1641848400, 'temp': 30.97, 'feels_like': 32.19, 'pressure': 1008, 'humidity': 48, 'dew_point': 18.68, 'uvi': 2.32, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641852000, 'temp': 29.97, 'feels_like': 31.66, 'pressure': 1009, 'humidity': 54, 'dew_point': 19.65, 'uvi': 0.56, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.55}}, {'dt': 1641855600, 'temp': 28.97, 'feels_like': 30.69, 'pressure': 1009, 'humidity': 58, 'dew_point': 19.87, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 40, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 19.750000 | 29.520000 | 61.000000 | 1009.000000 |  | 27.970000 | 0.000000 | 10000.000000 | 50.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 00 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 19.750000 | 29.520000 | 61.000000 | 1010.000000 |  | 27.970000 | 0.000000 | 10000.000000 | 70.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 02:00:00 | 96.000000 | 19.830000 | 28.410000 | 65.000000 | 1011.000000 | 0.21 | 26.970000 | 0.000000 | 10000.000000 | 60.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 03:00:00 | 97.000000 | 19.830000 | 28.410000 | 65.000000 | 1011.000000 | 0.18 | 26.970000 | 0.000000 | 10000.000000 | 60.000000 |  | 2.060000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 04:00:00 | 93.000000 | 19.220000 | 23.280000 | 80.000000 | 1013.000000 | 0.39 | 22.850000 | 0.000000 | 10000.000000 | 144.000000 | 1.12 | 0.580000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 05:00:00 | 86.000000 | 19.070000 | 22.910000 | 81.000000 | 1013.000000 | 0.31 | 22.490000 | 0.000000 | 10000.000000 | 103.000000 | 1.24 | 0.610000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 06:00:00 | 73.000000 | 19.400000 | 22.520000 | 85.000000 | 1012.000000 | 0.35 | 22.040000 | 0.000000 | 10000.000000 | 78.000000 | 1.07 | 0.770000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 07:00:00 | 85.000000 | 19.560000 | 22.700000 | 85.000000 | 1012.000000 | 0.28 | 22.200000 | 0.000000 | 10000.000000 | 120.000000 | 0.63 | 0.500000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 08:00:00 | 89.000000 | 19.510000 | 22.460000 | 86.000000 | 1011.000000 | 0.14 | 21.960000 | 0.000000 | 10000.000000 | 184.000000 | 0.96 | 0.720000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 09:00:00 | 86.000000 | 19.330000 | 22.260000 | 86.000000 | 1011.000000 | 0.13 | 21.780000 | 0.000000 | 10000.000000 | 167.000000 | 1.3 | 1.090000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 10:00:00 | 87.000000 | 19.340000 | 22.270000 | 86.000000 | 1012.000000 | 0.19 | 21.790000 | 0.000000 | 10000.000000 | 189.000000 | 1.16 | 0.920000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 20.910000 | 24.590000 | 83.000000 | 1012.000000 | 0.14 | 23.970000 | 0.000000 | 9000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 20.910000 | 24.590000 | 83.000000 | 1013.000000 | 0.11 | 23.970000 | 0.460000 | 9000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10d | 12 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 21.840000 | 25.970000 | 78.000000 | 1014.000000 |  | 25.970000 | 2.120000 | 9000.000000 | 0.000000 |  | 0.000000 | 721 | Haze | haze | 50d | 13 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 20.780000 | 29.980000 | 65.000000 | 1015.000000 |  | 27.970000 | 5.160000 | 9000.000000 | 0.000000 |  | 0.000000 | 721 | Haze | haze | 50d | 14 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 20.780000 | 29.980000 | 65.000000 | 1014.000000 |  | 27.970000 | 8.800000 | 9000.000000 | 20.000000 |  | 2.060000 | 721 | Haze | haze | 50d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 20.690000 | 31.140000 | 61.000000 | 1014.000000 | 0.37 | 28.970000 | 11.340000 | 10000.000000 | 40.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 17:00:00 | 40.000000 | 19.650000 | 31.660000 | 54.000000 | 1013.000000 | 0.29 | 29.970000 | 12.500000 | 10000.000000 | 50.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 18:00:00 | 20.000000 | 18.560000 | 33.190000 | 45.000000 | 1011.000000 | 0.43 | 31.970000 | 11.470000 | 10000.000000 | 0.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 19:00:00 | 20.000000 | 18.560000 | 33.190000 | 45.000000 | 1010.000000 | 0.4 | 31.970000 | 9.120000 | 10000.000000 | 10.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 18.560000 | 33.190000 | 45.000000 | 1009.000000 | 0.26 | 31.970000 | 5.430000 | 10000.000000 | 0.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 21:00:00 | 75.000000 | 18.680000 | 32.190000 | 48.000000 | 1008.000000 | 0.4 | 30.970000 | 2.320000 | 10000.000000 | 20.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 22:00:00 | 40.000000 | 19.650000 | 31.660000 | 54.000000 | 1009.000000 | 0.55 | 29.970000 | 0.560000 | 10000.000000 | 20.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 19.870000 | 30.690000 | 58.000000 | 1009.000000 | 0.6 | 28.970000 | 0.000000 | 10000.000000 | 40.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21115020_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21115020_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21115020_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115020_OWM_Windspeed_20220111.png)
