
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - AEROPUERTO PERALES [21245040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21245040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.42413889,-75.13941667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.42413889&lon=-75.13941667)


| Parameter | Value |
|---|---|
| Code | 21245040 |
| Name | AEROPUERTO PERALES [21245040] |
| Latitude, ° | 4.42413889 |
| Longitude, ° | -75.13941667 |
| Elevation, m | 943 |
| Category | Sinóptica Secundaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1970-11-15 00:00:00 |
| Suspension date | NaT |
| State | Tolima |
| County | Ibagué |
| Stream | Meta |
| Operator | Area Operativa 10 - Tolima |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | Río Opía |

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

### (CNE index 2156) Open Weather values for station 21245040 - AEROPUERTO PERALES [21245040]

JSON data from API OWM:

```
{'lat': 4.4241, 'lon': -75.1394, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641841268, 'sunrise': 1641813086, 'sunset': 1641855860, 'temp': 26.91, 'feels_like': 28.32, 'pressure': 1017, 'humidity': 65, 'dew_point': 19.78, 'uvi': 7.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 50, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, 'hourly': [{'dt': 1641772800, 'temp': 22.91, 'feels_like': 23.29, 'pressure': 1016, 'humidity': 78, 'dew_point': 18.87, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.32}}, {'dt': 1641776400, 'temp': 21.91, 'feels_like': 22.32, 'pressure': 1017, 'humidity': 83, 'dew_point': 18.89, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641780000, 'temp': 21.91, 'feels_like': 22.45, 'pressure': 1018, 'humidity': 88, 'dew_point': 19.83, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}, {'dt': 1641783600, 'temp': 21.91, 'feels_like': 22.45, 'pressure': 1018, 'humidity': 88, 'dew_point': 19.83, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 250, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641787200, 'temp': 21.88, 'feels_like': 22.37, 'pressure': 1015, 'humidity': 86, 'dew_point': 19.43, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 320, 'wind_gust': 1.35, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 21.88, 'feels_like': 22.34, 'pressure': 1014, 'humidity': 85, 'dew_point': 19.24, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 321, 'wind_gust': 1.07, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 20.49, 'feels_like': 20.87, 'pressure': 1014, 'humidity': 87, 'dew_point': 18.25, 'uvi': 0, 'clouds': 69, 'visibility': 10000, 'wind_speed': 0.77, 'wind_deg': 308, 'wind_gust': 0.63, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.26, 'feels_like': 20.64, 'pressure': 1013, 'humidity': 88, 'dew_point': 18.21, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 310, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641801600, 'temp': 20.03, 'feels_like': 20.44, 'pressure': 1013, 'humidity': 90, 'dew_point': 18.34, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 312, 'wind_gust': 0.76, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1641805200, 'temp': 19.57, 'feels_like': 19.96, 'pressure': 1013, 'humidity': 91, 'dew_point': 18.06, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 322, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.39}}, {'dt': 1641808800, 'temp': 19.51, 'feels_like': 19.87, 'pressure': 1014, 'humidity': 90, 'dew_point': 17.83, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 326, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641812400, 'temp': 19.91, 'feels_like': 20.57, 'pressure': 1018, 'humidity': 100, 'dew_point': 19.91, 'uvi': 0, 'clouds': 75, 'visibility': 3000, 'wind_speed': 1.54, 'wind_deg': 90, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}]}, {'dt': 1641816000, 'temp': 20.91, 'feels_like': 21.67, 'pressure': 1019, 'humidity': 100, 'dew_point': 20.91, 'uvi': 0.2, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}]}, {'dt': 1641819600, 'temp': 20.91, 'feels_like': 21.67, 'pressure': 1020, 'humidity': 100, 'dew_point': 20.91, 'uvi': 1.15, 'clouds': 75, 'visibility': 5000, 'wind_speed': 1.54, 'wind_deg': 140, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641823200, 'temp': 20.91, 'feels_like': 21.67, 'pressure': 1021, 'humidity': 100, 'dew_point': 20.91, 'uvi': 2.85, 'clouds': 75, 'visibility': 8000, 'wind_speed': 1.54, 'wind_deg': 360, 'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}, {'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}, {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641826800, 'temp': 22.91, 'feels_like': 23.55, 'pressure': 1021, 'humidity': 88, 'dew_point': 20.82, 'uvi': 4.9, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.48}}, {'dt': 1641830400, 'temp': 23.91, 'feels_like': 24.52, 'pressure': 1020, 'humidity': 83, 'dew_point': 20.85, 'uvi': 10.26, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 30, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641834000, 'temp': 24.91, 'feels_like': 25.36, 'pressure': 1019, 'humidity': 73, 'dew_point': 19.74, 'uvi': 11.3, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 80, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641837600, 'temp': 25.91, 'feels_like': 26.36, 'pressure': 1018, 'humidity': 69, 'dew_point': 19.79, 'uvi': 10.39, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 70, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.36}}, {'dt': 1641841200, 'temp': 26.91, 'feels_like': 28.32, 'pressure': 1017, 'humidity': 65, 'dew_point': 19.78, 'uvi': 7.55, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 50, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.76}}, {'dt': 1641844800, 'temp': 24.91, 'feels_like': 25.36, 'pressure': 1016, 'humidity': 73, 'dew_point': 19.74, 'uvi': 4.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 60, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641848400, 'temp': 23.91, 'feels_like': 24.52, 'pressure': 1016, 'humidity': 83, 'dew_point': 20.85, 'uvi': 1.88, 'clouds': 90, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 40, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.7}}, {'dt': 1641852000, 'temp': 23.91, 'feels_like': 24.52, 'pressure': 1016, 'humidity': 83, 'dew_point': 20.85, 'uvi': 0.43, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.52}}, {'dt': 1641855600, 'temp': 22.91, 'feels_like': 23.55, 'pressure': 1017, 'humidity': 88, 'dew_point': 20.82, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.75}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 00:00:00 | 20.000000 | 18.870000 | 23.290000 | 78.000000 | 1016.000000 | 0.32 | 22.910000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 01:00:00 | 20.000000 | 18.890000 | 22.320000 | 83.000000 | 1017.000000 | 0.2 | 21.910000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 19.830000 | 22.450000 | 88.000000 | 1018.000000 | 0.3 | 21.910000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 19.830000 | 22.450000 | 88.000000 | 1018.000000 | 0.2 | 21.910000 | 0.000000 | 10000.000000 | 250.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 04:00:00 | 79.000000 | 19.430000 | 22.370000 | 86.000000 | 1015.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 320.000000 | 1.35 | 1.430000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 05:00:00 | 82.000000 | 19.240000 | 22.340000 | 85.000000 | 1014.000000 |  | 21.880000 | 0.000000 | 10000.000000 | 321.000000 | 1.07 | 1.200000 | 803 | Clouds | broken clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 06:00:00 | 69.000000 | 18.250000 | 20.870000 | 87.000000 | 1014.000000 |  | 20.490000 | 0.000000 | 10000.000000 | 308.000000 | 0.63 | 0.770000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 07:00:00 | 87.000000 | 18.210000 | 20.640000 | 88.000000 | 1013.000000 | 0.13 | 20.260000 | 0.000000 | 10000.000000 | 310.000000 | 0.71 | 0.780000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 18.340000 | 20.440000 | 90.000000 | 1013.000000 | 0.31 | 20.030000 | 0.000000 | 10000.000000 | 312.000000 | 0.76 | 0.780000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 09:00:00 | 84.000000 | 18.060000 | 19.960000 | 91.000000 | 1013.000000 | 0.39 | 19.570000 | 0.000000 | 10000.000000 | 322.000000 | 1.03 | 1.120000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 10:00:00 | 87.000000 | 17.830000 | 19.870000 | 90.000000 | 1014.000000 | 0.2 | 19.510000 | 0.000000 | 10000.000000 | 326.000000 | 1.08 | 1.270000 | 500 | Rain | light rain | 10n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 11:00:00 | 75.000000 | 19.910000 | 20.570000 | 100.000000 | 1018.000000 |  | 19.910000 | 0.000000 | 3000.000000 | 90.000000 |  | 1.540000 | 701 | Mist | mist | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 20.910000 | 21.670000 | 100.000000 | 1019.000000 |  | 20.910000 | 0.200000 | 5000.000000 | 230.000000 |  | 1.540000 | 701 | Mist | mist | 50d | 12 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 20.910000 | 21.670000 | 100.000000 | 1020.000000 | 0.12 | 20.910000 | 1.150000 | 5000.000000 | 140.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 13 |
| ![09d.png](http://openweathermap.org/img/w/09d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 14:00:00 | 75.000000 | 20.910000 | 21.670000 | 100.000000 | 1021.000000 | 0.25 | 20.910000 | 2.850000 | 8000.000000 | 360.000000 |  | 1.540000 | 300 | Drizzle | light intensity drizzle | 09d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 20.820000 | 23.550000 | 88.000000 | 1021.000000 | 0.48 | 22.910000 | 4.900000 | 10000.000000 | 310.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 16:00:00 | 75.000000 | 20.850000 | 24.520000 | 83.000000 | 1020.000000 | 0.65 | 23.910000 | 10.260000 | 10000.000000 | 30.000000 |  | 2.570000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 19.740000 | 25.360000 | 73.000000 | 1019.000000 | 0.49 | 24.910000 | 11.300000 | 10000.000000 | 80.000000 |  | 3.090000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 19.790000 | 26.360000 | 69.000000 | 1018.000000 | 0.36 | 25.910000 | 10.390000 | 10000.000000 | 70.000000 |  | 5.660000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 19:00:00 | 40.000000 | 19.780000 | 28.320000 | 65.000000 | 1017.000000 | 0.76 | 26.910000 | 7.550000 | 10000.000000 | 50.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 19.740000 | 25.360000 | 73.000000 | 1016.000000 | 0.7 | 24.910000 | 4.480000 | 10000.000000 | 60.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 20.850000 | 24.520000 | 83.000000 | 1016.000000 | 0.7 | 23.910000 | 1.880000 | 10000.000000 | 40.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 22:00:00 | 75.000000 | 20.850000 | 24.520000 | 83.000000 | 1016.000000 | 0.52 | 23.910000 | 0.430000 | 10000.000000 | 20.000000 |  | 2.060000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21245040 | "AEROPUERTO PERALES [21245040]" | 4.424139 | -75.139417 | 943.000000 | Sinóptica Secundaria | Convencional | Activa | 1970-11-15 00:00:00 | NaT | Tolima | Ibagué | Meta | Area Operativa 10 - Tolima | Magdalena Cauca | Alto Magdalena | Río Opía | America/Bogota | 2022-01-10 23:00:00 | 75.000000 | 20.820000 | 23.550000 | 88.000000 | 1017.000000 | 0.75 | 22.910000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21245040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21245040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21245040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21245040_OWM_Windspeed_20220111.png)
