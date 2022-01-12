
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - ITA-BUGA [26095220] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station26095220_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=3.91666667,-76.3) or [Openstreet Map](https://www.openstreetmap.org/query?lat=3.91666667&lon=-76.3)


| Parameter | Value |
|---|---|
| Code | 26095220 |
| Name | ITA-BUGA [26095220] |
| Latitude, ° | 3.91666667 |
| Longitude, ° | -76.3 |
| Elevation, m | 10 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 1969-07-15 00:00:00 |
| Suspension date | 1981-08-15 00:00:00 |
| State | Valle del Cauca |
| County | Buga |
| Stream | Guayabero |
| Operator | Area Operativa 09 - Cauca-Valle-Caldas |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Cauca |
| SZH - Hydrographic subzone | Ríos Guadalajara y San Pedro |

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

### (CNE index 1228) Open Weather values for station 26095220 - ITA-BUGA [26095220]

JSON data from API OWM:

```
{'lat': 3.9167, 'lon': -76.3, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641813315, 'sunset': 1641856188, 'temp': 27.98, 'feels_like': 31.9, 'pressure': 1011, 'humidity': 79, 'dew_point': 24, 'uvi': 3.14, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 261, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, 'hourly': [{'dt': 1641772800, 'temp': 24.98, 'feels_like': 25.96, 'pressure': 1013, 'humidity': 93, 'dew_point': 23.77, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 344, 'wind_gust': 1.16, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.18}}, {'dt': 1641776400, 'temp': 22.98, 'feels_like': 23.79, 'pressure': 1015, 'humidity': 94, 'dew_point': 21.96, 'uvi': 0, 'clouds': 46, 'visibility': 10000, 'wind_speed': 0.22, 'wind_deg': 339, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.75}}, {'dt': 1641780000, 'temp': 22.98, 'feels_like': 23.79, 'pressure': 1016, 'humidity': 94, 'dew_point': 21.96, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 317, 'wind_gust': 0.98, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.5}}, {'dt': 1641783600, 'temp': 22.98, 'feels_like': 23.76, 'pressure': 1016, 'humidity': 93, 'dew_point': 21.79, 'uvi': 0, 'clouds': 36, 'visibility': 10000, 'wind_speed': 0.13, 'wind_deg': 273, 'wind_gust': 0.82, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.2}}, {'dt': 1641787200, 'temp': 22.98, 'feels_like': 23.76, 'pressure': 1016, 'humidity': 93, 'dew_point': 21.79, 'uvi': 0, 'clouds': 39, 'visibility': 10000, 'wind_speed': 0.1, 'wind_deg': 199, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.13}}, {'dt': 1641790800, 'temp': 21.98, 'feels_like': 22.69, 'pressure': 1015, 'humidity': 94, 'dew_point': 20.97, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.21, 'wind_deg': 166, 'wind_gust': 0.73, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 21.98, 'feels_like': 22.69, 'pressure': 1015, 'humidity': 94, 'dew_point': 20.97, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 216, 'wind_gust': 0.75, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 20.98, 'feels_like': 21.61, 'pressure': 1014, 'humidity': 95, 'dew_point': 20.15, 'uvi': 0, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.37, 'wind_deg': 165, 'wind_gust': 0.75, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 20.98, 'feels_like': 21.61, 'pressure': 1014, 'humidity': 95, 'dew_point': 20.15, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 180, 'wind_gust': 0.64, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.21}}, {'dt': 1641805200, 'temp': 20.98, 'feels_like': 21.61, 'pressure': 1014, 'humidity': 95, 'dew_point': 20.15, 'uvi': 0, 'clouds': 92, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 206, 'wind_gust': 0.62, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641808800, 'temp': 19.98, 'feels_like': 20.54, 'pressure': 1015, 'humidity': 96, 'dew_point': 19.32, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.17, 'wind_deg': 213, 'wind_gust': 0.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.29}}, {'dt': 1641812400, 'temp': 19.98, 'feels_like': 20.54, 'pressure': 1015, 'humidity': 96, 'dew_point': 19.32, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.12, 'wind_deg': 1, 'wind_gust': 0.37, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641816000, 'temp': 20.98, 'feels_like': 21.61, 'pressure': 1016, 'humidity': 95, 'dew_point': 20.15, 'uvi': 0.2, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.5, 'wind_deg': 44, 'wind_gust': 0.83, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641819600, 'temp': 21.98, 'feels_like': 22.66, 'pressure': 1017, 'humidity': 93, 'dew_point': 20.8, 'uvi': 1.36, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.39, 'wind_deg': 28, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641823200, 'temp': 22.98, 'feels_like': 23.66, 'pressure': 1017, 'humidity': 89, 'dew_point': 21.07, 'uvi': 3.44, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 12, 'wind_gust': 1.12, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.3}}, {'dt': 1641826800, 'temp': 24.98, 'feels_like': 25.73, 'pressure': 1017, 'humidity': 84, 'dew_point': 22.09, 'uvi': 6.01, 'clouds': 97, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 354, 'wind_gust': 1.08, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.45}}, {'dt': 1641830400, 'temp': 25.98, 'feels_like': 25.98, 'pressure': 1015, 'humidity': 77, 'dew_point': 21.64, 'uvi': 7.7, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.78, 'wind_deg': 300, 'wind_gust': 0.94, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.61}}, {'dt': 1641834000, 'temp': 26.98, 'feels_like': 29.07, 'pressure': 1014, 'humidity': 73, 'dew_point': 21.73, 'uvi': 8.58, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.54, 'wind_deg': 275, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641837600, 'temp': 26.98, 'feels_like': 29.07, 'pressure': 1013, 'humidity': 73, 'dew_point': 21.73, 'uvi': 7.98, 'clouds': 41, 'visibility': 9021, 'wind_speed': 0.98, 'wind_deg': 283, 'wind_gust': 1, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.03}}, {'dt': 1641841200, 'temp': 27.98, 'feels_like': 31.45, 'pressure': 1012, 'humidity': 76, 'dew_point': 23.35, 'uvi': 5.2, 'clouds': 55, 'visibility': 8656, 'wind_speed': 1.14, 'wind_deg': 266, 'wind_gust': 1.39, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.28}}, {'dt': 1641844800, 'temp': 27.98, 'feels_like': 31.9, 'pressure': 1011, 'humidity': 79, 'dew_point': 24, 'uvi': 3.14, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 261, 'wind_gust': 1.26, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.37}}, {'dt': 1641848400, 'temp': 23.98, 'feels_like': 24.6, 'pressure': 1011, 'humidity': 83, 'dew_point': 20.91, 'uvi': 1.37, 'clouds': 82, 'visibility': 8522, 'wind_speed': 1.13, 'wind_deg': 259, 'wind_gust': 1.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.32}}, {'dt': 1641852000, 'temp': 21.98, 'feels_like': 22.56, 'pressure': 1012, 'humidity': 89, 'dew_point': 20.08, 'uvi': 0.21, 'clouds': 87, 'visibility': 6793, 'wind_speed': 0.73, 'wind_deg': 271, 'wind_gust': 1.22, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.24}}, {'dt': 1641855600, 'temp': 19.98, 'feels_like': 20.44, 'pressure': 1013, 'humidity': 92, 'dew_point': 18.64, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 0.27, 'wind_deg': 275, 'wind_gust': 0.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'rain': {'1h': 1.32}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 00:00:00 | 29.000000 | 23.770000 | 25.960000 | 93.000000 | 1013.000000 | 0.18 | 24.980000 | 0.000000 | 10000.000000 | 344.000000 | 1.16 | 0.390000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 01:00:00 | 46.000000 | 21.960000 | 23.790000 | 94.000000 | 1015.000000 | 0.75 | 22.980000 | 0.000000 | 10000.000000 | 339.000000 | 1.05 | 0.220000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 02:00:00 | 44.000000 | 21.960000 | 23.790000 | 94.000000 | 1016.000000 | 0.5 | 22.980000 | 0.000000 | 10000.000000 | 317.000000 | 0.98 | 0.100000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 03:00:00 | 36.000000 | 21.790000 | 23.760000 | 93.000000 | 1016.000000 | 0.2 | 22.980000 | 0.000000 | 10000.000000 | 273.000000 | 0.82 | 0.130000 | 500 | Rain | light rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 04:00:00 | 39.000000 | 21.790000 | 23.760000 | 93.000000 | 1016.000000 | 0.13 | 22.980000 | 0.000000 | 10000.000000 | 199.000000 | 0.71 | 0.100000 | 500 | Rain | light rain | 10n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 05:00:00 | 44.000000 | 20.970000 | 22.690000 | 94.000000 | 1015.000000 |  | 21.980000 | 0.000000 | 10000.000000 | 166.000000 | 0.73 | 0.210000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 06:00:00 | 77.000000 | 20.970000 | 22.690000 | 94.000000 | 1015.000000 |  | 21.980000 | 0.000000 | 10000.000000 | 216.000000 | 0.75 | 0.360000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 07:00:00 | 97.000000 | 20.150000 | 21.610000 | 95.000000 | 1014.000000 |  | 20.980000 | 0.000000 | 10000.000000 | 165.000000 | 0.75 | 0.370000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 08:00:00 | 88.000000 | 20.150000 | 21.610000 | 95.000000 | 1014.000000 | 0.21 | 20.980000 | 0.000000 | 10000.000000 | 180.000000 | 0.64 | 0.300000 | 500 | Rain | light rain | 10n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 09:00:00 | 92.000000 | 20.150000 | 21.610000 | 95.000000 | 1014.000000 | 0.15 | 20.980000 | 0.000000 | 10000.000000 | 206.000000 | 0.62 | 0.400000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 10:00:00 | 93.000000 | 19.320000 | 20.540000 | 96.000000 | 1015.000000 | 0.29 | 19.980000 | 0.000000 | 10000.000000 | 213.000000 | 0.42 | 0.170000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 11:00:00 | 94.000000 | 19.320000 | 20.540000 | 96.000000 | 1015.000000 | 0.19 | 19.980000 | 0.000000 | 10000.000000 | 1.000000 | 0.37 | 0.120000 | 500 | Rain | light rain | 10n | 11 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 12:00:00 | 99.000000 | 20.150000 | 21.610000 | 95.000000 | 1016.000000 | 0.17 | 20.980000 | 0.200000 | 10000.000000 | 44.000000 | 0.83 | 0.500000 | 500 | Rain | light rain | 10d | 12 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 20.800000 | 22.660000 | 93.000000 | 1017.000000 | 0.25 | 21.980000 | 1.360000 | 10000.000000 | 28.000000 | 0.93 | 0.390000 | 500 | Rain | light rain | 10d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 14:00:00 | 100.000000 | 21.070000 | 23.660000 | 89.000000 | 1017.000000 | 0.3 | 22.980000 | 3.440000 | 10000.000000 | 12.000000 | 1.12 | 0.650000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 15:00:00 | 97.000000 | 22.090000 | 25.730000 | 84.000000 | 1017.000000 | 0.45 | 24.980000 | 6.010000 | 10000.000000 | 354.000000 | 1.08 | 0.810000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 16:00:00 | 98.000000 | 21.640000 | 25.980000 | 77.000000 | 1015.000000 | 0.61 | 25.980000 | 7.700000 | 10000.000000 | 300.000000 | 0.94 | 0.780000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 17:00:00 | 98.000000 | 21.730000 | 29.070000 | 73.000000 | 1014.000000 | 0.81 | 26.980000 | 8.580000 | 10000.000000 | 275.000000 | 0.97 | 0.540000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 18:00:00 | 41.000000 | 21.730000 | 29.070000 | 73.000000 | 1013.000000 | 1.03 | 26.980000 | 7.980000 | 9021.000000 | 283.000000 | 1 | 0.980000 | 501 | Rain | moderate rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 19:00:00 | 55.000000 | 23.350000 | 31.450000 | 76.000000 | 1012.000000 | 1.28 | 27.980000 | 5.200000 | 8656.000000 | 266.000000 | 1.39 | 1.140000 | 501 | Rain | moderate rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 20:00:00 | 73.000000 | 24.000000 | 31.900000 | 79.000000 | 1011.000000 | 1.37 | 27.980000 | 3.140000 | 10000.000000 | 261.000000 | 1.26 | 1.070000 | 501 | Rain | moderate rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 21:00:00 | 82.000000 | 20.910000 | 24.600000 | 83.000000 | 1011.000000 | 1.32 | 23.980000 | 1.370000 | 8522.000000 | 259.000000 | 1.51 | 1.130000 | 501 | Rain | moderate rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 22:00:00 | 87.000000 | 20.080000 | 22.560000 | 89.000000 | 1012.000000 | 1.24 | 21.980000 | 0.210000 | 6793.000000 | 271.000000 | 1.22 | 0.730000 | 501 | Rain | moderate rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 26095220 | "ITA-BUGA [26095220]" | 3.916667 | -76.300000 | 10.000000 | Climática Principal | Convencional | Suspendida | 1969-07-15 00:00:00 | 1981-08-15 00:00:00 | Valle del Cauca | Buga | Guayabero | Area Operativa 09 - Cauca-Valle-Caldas | Magdalena Cauca | Cauca | Ríos Guadalajara y San Pedro | America/Bogota | 2022-01-10 23:00:00 | 89.000000 | 18.640000 | 20.440000 | 92.000000 | 1013.000000 | 1.32 | 19.980000 | 0.000000 | 10000.000000 | 275.000000 | 0.86 | 0.270000 | 501 | Rain | moderate rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station26095220_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Rain_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Temp_20220111.png)
![CNE_IDEAM_Station26095220_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_UVI_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station26095220_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station26095220_OWM_Windspeed_20220111.png)
