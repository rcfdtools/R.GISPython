
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ACUEDUCTO MOCOA - AUT [44015060] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station44015060_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=1.15733333,-76.65183333) or [Openstreet Map](https://www.openstreetmap.org/query?lat=1.15733333&lon=-76.65183333)


| Parameter | Value |
|---|---|
| Code | 44015060 |
| Name | ACUEDUCTO MOCOA - AUT [44015060] |
| Latitude, ° | 1.15733333 |
| Longitude, ° | -76.65183333 |
| Elevation, m | 650 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2006-03-29 00:00:00 |
| Suspension date | NaT |
| State | Putumayo |
| County | Mocoa |
| Stream | Hacha |
| Operator | Area Operativa 07 - Nariño-Putumayo |
| AH - Hydrographic area | Amazonas |
| ZH - Hydrographic zone | Caquetá |
| SZH - Hydrographic subzone | Alto Caqueta |

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

### (CNE index 19) Open Weather values for station 44015060 - ACUEDUCTO MOCOA - AUT [44015060]

JSON data from API OWM:

```
{'lat': 1.1573, 'lon': -76.6518, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813133, 'sunset': 1641856539, 'temp': 25.92, 'feels_like': 26.79, 'pressure': 1011, 'humidity': 85, 'dew_point': 23.2, 'uvi': 4.1, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 136, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, 'hourly': [{'dt': 1641772800, 'temp': 22.73, 'feels_like': 23.46, 'pressure': 1013, 'humidity': 92, 'dew_point': 21.36, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 311, 'wind_gust': 1.1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.58}}, {'dt': 1641776400, 'temp': 22.55, 'feels_like': 23.29, 'pressure': 1014, 'humidity': 93, 'dew_point': 21.36, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.49, 'wind_deg': 313, 'wind_gust': 1.6, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1641780000, 'temp': 22.71, 'feels_like': 23.44, 'pressure': 1015, 'humidity': 92, 'dew_point': 21.34, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 316, 'wind_gust': 1.22, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641783600, 'temp': 22.58, 'feels_like': 23.35, 'pressure': 1015, 'humidity': 94, 'dew_point': 21.57, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.31, 'wind_deg': 305, 'wind_gust': 1.19, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.37}}, {'dt': 1641787200, 'temp': 22.42, 'feels_like': 23.2, 'pressure': 1015, 'humidity': 95, 'dew_point': 21.58, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 297, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.67}}, {'dt': 1641790800, 'temp': 22.25, 'feels_like': 23.01, 'pressure': 1015, 'humidity': 95, 'dew_point': 21.41, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 290, 'wind_gust': 1.03, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.65}}, {'dt': 1641794400, 'temp': 22.04, 'feels_like': 22.83, 'pressure': 1014, 'humidity': 97, 'dew_point': 21.54, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.97, 'wind_deg': 283, 'wind_gust': 0.92, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.52}}, {'dt': 1641798000, 'temp': 21.83, 'feels_like': 22.6, 'pressure': 1013, 'humidity': 97, 'dew_point': 21.33, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.12, 'wind_deg': 291, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.73}}, {'dt': 1641801600, 'temp': 21.48, 'feels_like': 22.22, 'pressure': 1013, 'humidity': 97, 'dew_point': 20.98, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 295, 'wind_gust': 1.18, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.89}}, {'dt': 1641805200, 'temp': 21.23, 'feels_like': 21.94, 'pressure': 1013, 'humidity': 97, 'dew_point': 20.73, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 301, 'wind_gust': 1.15, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.64}}, {'dt': 1641808800, 'temp': 21.12, 'feels_like': 21.79, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.46, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 297, 'wind_gust': 1.53, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641812400, 'temp': 21.12, 'feels_like': 21.79, 'pressure': 1014, 'humidity': 96, 'dew_point': 20.46, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.48, 'wind_deg': 297, 'wind_gust': 1.27, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641816000, 'temp': 21.72, 'feels_like': 22.43, 'pressure': 1015, 'humidity': 95, 'dew_point': 20.88, 'uvi': 0.27, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 292, 'wind_gust': 1.32, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.68, 'feels_like': 24.43, 'pressure': 1016, 'humidity': 89, 'dew_point': 21.76, 'uvi': 1.04, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.09, 'wind_deg': 68, 'wind_gust': 0.67, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 24.92, 'feels_like': 25.71, 'pressure': 1016, 'humidity': 86, 'dew_point': 22.42, 'uvi': 2.61, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 133, 'wind_gust': 0.96, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.41}}, {'dt': 1641826800, 'temp': 25.27, 'feels_like': 26.18, 'pressure': 1016, 'humidity': 89, 'dew_point': 23.33, 'uvi': 4.56, 'clouds': 94, 'visibility': 7325, 'wind_speed': 1.4, 'wind_deg': 144, 'wind_gust': 1.61, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.23}}, {'dt': 1641830400, 'temp': 25.54, 'feels_like': 26.45, 'pressure': 1016, 'humidity': 88, 'dew_point': 23.4, 'uvi': 8.31, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.51, 'wind_deg': 149, 'wind_gust': 1.6, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.12}}, {'dt': 1641834000, 'temp': 25.84, 'feels_like': 26.73, 'pressure': 1015, 'humidity': 86, 'dew_point': 23.32, 'uvi': 9.31, 'clouds': 92, 'visibility': 6716, 'wind_speed': 1.51, 'wind_deg': 150, 'wind_gust': 1.44, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.99}}, {'dt': 1641837600, 'temp': 25.78, 'feels_like': 26.66, 'pressure': 1014, 'humidity': 86, 'dew_point': 23.26, 'uvi': 8.72, 'clouds': 88, 'visibility': 6811, 'wind_speed': 1.22, 'wind_deg': 148, 'wind_gust': 1.2, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.01}}, {'dt': 1641841200, 'temp': 26.16, 'feels_like': 26.16, 'pressure': 1012, 'humidity': 85, 'dew_point': 23.44, 'uvi': 6.65, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 140, 'wind_gust': 1.11, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641844800, 'temp': 25.92, 'feels_like': 26.79, 'pressure': 1011, 'humidity': 85, 'dew_point': 23.2, 'uvi': 4.1, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 136, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.73}}, {'dt': 1641848400, 'temp': 25.2, 'feels_like': 26.1, 'pressure': 1011, 'humidity': 89, 'dew_point': 23.26, 'uvi': 1.84, 'clouds': 90, 'visibility': 5874, 'wind_speed': 0.85, 'wind_deg': 136, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.65}}, {'dt': 1641852000, 'temp': 24.4, 'feels_like': 25.35, 'pressure': 1012, 'humidity': 94, 'dew_point': 23.37, 'uvi': 0.42, 'clouds': 89, 'visibility': 6608, 'wind_speed': 0.12, 'wind_deg': 118, 'wind_gust': 0.72, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.68}}, {'dt': 1641855600, 'temp': 23.12, 'feels_like': 23.99, 'pressure': 1012, 'humidity': 96, 'dew_point': 22.45, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 310, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.72}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 21.360000 | 23.460000 | 92.000000 | 1013.000000 | 0.58 | 22.730000 | 0.000000 | 10000.000000 | 311.000000 | 1.1 | 1.330000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 21.360000 | 23.290000 | 93.000000 | 1014.000000 | 0.24 | 22.550000 | 0.000000 | 10000.000000 | 313.000000 | 1.6 | 1.490000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 21.340000 | 23.440000 | 92.000000 | 1015.000000 | 0.15 | 22.710000 | 0.000000 | 10000.000000 | 316.000000 | 1.22 | 1.430000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 21.570000 | 23.350000 | 94.000000 | 1015.000000 | 0.37 | 22.580000 | 0.000000 | 10000.000000 | 305.000000 | 1.19 | 1.310000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 21.580000 | 23.200000 | 95.000000 | 1015.000000 | 0.67 | 22.420000 | 0.000000 | 10000.000000 | 297.000000 | 1.16 | 1.240000 | 500 | Rain | light rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 21.410000 | 23.010000 | 95.000000 | 1015.000000 | 0.65 | 22.250000 | 0.000000 | 10000.000000 | 290.000000 | 1.03 | 1.000000 | 500 | Rain | light rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 06:00:00 | 82.000000 | 21.540000 | 22.830000 | 97.000000 | 1014.000000 | 0.52 | 22.040000 | 0.000000 | 10000.000000 | 283.000000 | 0.92 | 0.970000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 07:00:00 | 96.000000 | 21.330000 | 22.600000 | 97.000000 | 1013.000000 | 0.73 | 21.830000 | 0.000000 | 10000.000000 | 291.000000 | 1.01 | 1.120000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 08:00:00 | 97.000000 | 20.980000 | 22.220000 | 97.000000 | 1013.000000 | 0.89 | 21.480000 | 0.000000 | 10000.000000 | 295.000000 | 1.18 | 1.240000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 09:00:00 | 98.000000 | 20.730000 | 21.940000 | 97.000000 | 1013.000000 | 0.64 | 21.230000 | 0.000000 | 10000.000000 | 301.000000 | 1.15 | 1.330000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 10:00:00 | 99.000000 | 20.460000 | 21.790000 | 96.000000 | 1014.000000 | 0.29 | 21.120000 | 0.000000 | 10000.000000 | 297.000000 | 1.53 | 1.500000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 11:00:00 | 99.000000 | 20.460000 | 21.790000 | 96.000000 | 1014.000000 | 0.21 | 21.120000 | 0.000000 | 10000.000000 | 297.000000 | 1.27 | 1.480000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 20.880000 | 22.430000 | 95.000000 | 1015.000000 |  | 21.720000 | 0.270000 | 10000.000000 | 292.000000 | 1.32 | 1.250000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 21.760000 | 24.430000 | 89.000000 | 1016.000000 |  | 23.680000 | 1.040000 | 10000.000000 | 68.000000 | 0.67 | 0.090000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 22.420000 | 25.710000 | 86.000000 | 1016.000000 | 0.41 | 24.920000 | 2.610000 | 10000.000000 | 133.000000 | 0.96 | 0.890000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 15:00:00 | 94.000000 | 23.330000 | 26.180000 | 89.000000 | 1016.000000 | 1.23 | 25.270000 | 4.560000 | 7325.000000 | 144.000000 | 1.61 | 1.400000 | 501 | Rain | moderate rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 16:00:00 | 90.000000 | 23.400000 | 26.450000 | 88.000000 | 1016.000000 | 1.12 | 25.540000 | 8.310000 | 10000.000000 | 149.000000 | 1.6 | 1.510000 | 501 | Rain | moderate rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 17:00:00 | 92.000000 | 23.320000 | 26.730000 | 86.000000 | 1015.000000 | 0.99 | 25.840000 | 9.310000 | 6716.000000 | 150.000000 | 1.44 | 1.510000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 18:00:00 | 88.000000 | 23.260000 | 26.660000 | 86.000000 | 1014.000000 | 1.01 | 25.780000 | 8.720000 | 6811.000000 | 148.000000 | 1.2 | 1.220000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 19:00:00 | 99.000000 | 23.440000 | 26.160000 | 85.000000 | 1012.000000 | 0.81 | 26.160000 | 6.650000 | 10000.000000 | 140.000000 | 1.11 | 1.030000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 20:00:00 | 94.000000 | 23.200000 | 26.790000 | 85.000000 | 1011.000000 | 0.73 | 25.920000 | 4.100000 | 10000.000000 | 136.000000 | 1.05 | 0.990000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 21:00:00 | 90.000000 | 23.260000 | 26.100000 | 89.000000 | 1011.000000 | 0.65 | 25.200000 | 1.840000 | 5874.000000 | 136.000000 | 1.12 | 0.850000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 23.370000 | 25.350000 | 94.000000 | 1012.000000 | 0.68 | 24.400000 | 0.420000 | 6608.000000 | 118.000000 | 0.72 | 0.120000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 44015060 | "ACUEDUCTO MOCOA - AUT [44015060]" | 1.157333 | -76.651833 | 650.000000 | Climática Principal | Automática con Telemetría | Activa | 2006-03-29 00:00:00 | NaT | Putumayo | Mocoa | Hacha | Area Operativa 07 - Nariño-Putumayo | Amazonas | Caquetá | Alto Caqueta | America/Bogota | 2022-01-10 23:00:00 | 89.000000 | 22.450000 | 23.990000 | 96.000000 | 1012.000000 | 0.72 | 23.120000 | 0.000000 | 10000.000000 | 310.000000 | 0.62 | 0.650000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station44015060_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Rain_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Temp_20220111.png)
![CNE_IDEAM_Station44015060_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_UVI_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station44015060_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station44015060_OWM_Windspeed_20220111.png)
