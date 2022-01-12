
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA CAPILLA - AUT [35085080] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station35085080_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=5.09919444,-73.436) or [Openstreet Map](https://www.openstreetmap.org/query?lat=5.09919444&lon=-73.436)


| Parameter | Value |
|---|---|
| Code | 35085080 |
| Name | LA CAPILLA - AUT [35085080] |
| Latitude, ° | 5.09919444 |
| Longitude, ° | -73.436 |
| Elevation, m | 1917 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-03-08 00:00:00 |
| Suspension date | NaT |
| State | Boyacá |
| County | La Capilla |
| Stream | San Juan |
| Operator | Area Operativa 06 - Boyacá-Casanare-Vichada |
| AH - Hydrographic area | Orinoco |
| ZH - Hydrographic zone | Meta |
| SZH - Hydrographic subzone | Río Garagoa |

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

### (CNE index 134) Open Weather values for station 35085080 - LA CAPILLA - AUT [35085080]

JSON data from API OWM:

```
{'lat': 5.0992, 'lon': -73.436, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812743, 'sunset': 1641855386, 'temp': 19.23, 'feels_like': 19.09, 'pressure': 1012, 'humidity': 72, 'dew_point': 14.06, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 128, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, 'hourly': [{'dt': 1641772800, 'temp': 15.06, 'feels_like': 15.13, 'pressure': 1016, 'humidity': 96, 'dew_point': 14.43, 'uvi': 0, 'clouds': 97, 'visibility': 4049, 'wind_speed': 0.52, 'wind_deg': 127, 'wind_gust': 0.98, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 14.99, 'feels_like': 15.05, 'pressure': 1017, 'humidity': 96, 'dew_point': 14.36, 'uvi': 0, 'clouds': 100, 'visibility': 5079, 'wind_speed': 0.3, 'wind_deg': 136, 'wind_gust': 0.74, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 14.9, 'feels_like': 14.95, 'pressure': 1018, 'humidity': 96, 'dew_point': 14.27, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.38, 'wind_deg': 149, 'wind_gust': 0.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 14.87, 'feels_like': 14.89, 'pressure': 1018, 'humidity': 95, 'dew_point': 14.08, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 168, 'wind_gust': 0.76, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 14.7, 'feels_like': 14.71, 'pressure': 1018, 'humidity': 95, 'dew_point': 13.91, 'uvi': 0, 'clouds': 99, 'visibility': 10000, 'wind_speed': 0.36, 'wind_deg': 169, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 14.63, 'feels_like': 14.63, 'pressure': 1018, 'humidity': 95, 'dew_point': 13.84, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.35, 'wind_deg': 156, 'wind_gust': 0.9, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 14.65, 'feels_like': 14.68, 'pressure': 1016, 'humidity': 96, 'dew_point': 14.02, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 0.3, 'wind_deg': 140, 'wind_gust': 0.76, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 14.28, 'feels_like': 14.24, 'pressure': 1015, 'humidity': 95, 'dew_point': 13.49, 'uvi': 0, 'clouds': 95, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 234, 'wind_gust': 0.5, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 14, 'feels_like': 13.88, 'pressure': 1015, 'humidity': 93, 'dew_point': 12.89, 'uvi': 0, 'clouds': 94, 'visibility': 10000, 'wind_speed': 0.58, 'wind_deg': 291, 'wind_gust': 0.56, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 13.49, 'feels_like': 13.35, 'pressure': 1015, 'humidity': 94, 'dew_point': 12.54, 'uvi': 0, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.41, 'wind_deg': 298, 'wind_gust': 0.51, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 13.02, 'feels_like': 12.86, 'pressure': 1016, 'humidity': 95, 'dew_point': 12.24, 'uvi': 0, 'clouds': 86, 'visibility': 10000, 'wind_speed': 0.64, 'wind_deg': 289, 'wind_gust': 0.65, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 12.75, 'feels_like': 12.56, 'pressure': 1017, 'humidity': 95, 'dew_point': 11.97, 'uvi': 0, 'clouds': 82, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 284, 'wind_gust': 0.92, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 14.34, 'feels_like': 14.15, 'pressure': 1018, 'humidity': 89, 'dew_point': 12.55, 'uvi': 0.61, 'clouds': 59, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 273, 'wind_gust': 0.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 16.74, 'feels_like': 16.51, 'pressure': 1018, 'humidity': 78, 'dew_point': 12.89, 'uvi': 2.53, 'clouds': 76, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 156, 'wind_gust': 0.7, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 19.14, 'feels_like': 18.83, 'pressure': 1018, 'humidity': 66, 'dew_point': 12.64, 'uvi': 5.9, 'clouds': 70, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 125, 'wind_gust': 1.08, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 21.23, 'feels_like': 20.9, 'pressure': 1017, 'humidity': 57, 'dew_point': 12.38, 'uvi': 9.82, 'clouds': 64, 'visibility': 10000, 'wind_speed': 1.76, 'wind_deg': 122, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 21.7, 'feels_like': 21.36, 'pressure': 1015, 'humidity': 55, 'dew_point': 12.27, 'uvi': 12.42, 'clouds': 70, 'visibility': 10000, 'wind_speed': 2.27, 'wind_deg': 118, 'wind_gust': 2.68, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 20.77, 'feels_like': 20.47, 'pressure': 1015, 'humidity': 60, 'dew_point': 12.73, 'uvi': 13.35, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.64, 'wind_deg': 123, 'wind_gust': 2.3, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 20.19, 'feels_like': 19.99, 'pressure': 1014, 'humidity': 66, 'dew_point': 13.64, 'uvi': 11.96, 'clouds': 93, 'visibility': 10000, 'wind_speed': 2.41, 'wind_deg': 129, 'wind_gust': 1.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 19.09, 'feels_like': 18.93, 'pressure': 1013, 'humidity': 72, 'dew_point': 13.93, 'uvi': 7.26, 'clouds': 100, 'visibility': 10000, 'wind_speed': 2.16, 'wind_deg': 131, 'wind_gust': 1.8, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 19.23, 'feels_like': 19.09, 'pressure': 1012, 'humidity': 72, 'dew_point': 14.06, 'uvi': 4.13, 'clouds': 99, 'visibility': 10000, 'wind_speed': 2.1, 'wind_deg': 128, 'wind_gust': 1.69, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.12}}, {'dt': 1641848400, 'temp': 17.81, 'feels_like': 17.76, 'pressure': 1013, 'humidity': 81, 'dew_point': 14.51, 'uvi': 1.61, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.95, 'wind_deg': 126, 'wind_gust': 2.14, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.25}}, {'dt': 1641852000, 'temp': 16.88, 'feels_like': 16.9, 'pressure': 1014, 'humidity': 87, 'dew_point': 14.7, 'uvi': 0.29, 'clouds': 95, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 125, 'wind_gust': 1.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.17}}, {'dt': 1641855600, 'temp': 15.54, 'feels_like': 15.6, 'pressure': 1015, 'humidity': 94, 'dew_point': 14.58, 'uvi': 0, 'clouds': 96, 'visibility': 10000, 'wind_speed': 1.07, 'wind_deg': 129, 'wind_gust': 1.9, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.14}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 00:00:00 | 97.000000 | 14.430000 | 15.130000 | 96.000000 | 1016.000000 |  | 15.060000 | 0.000000 | 4049.000000 | 127.000000 | 0.98 | 0.520000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 14.360000 | 15.050000 | 96.000000 | 1017.000000 |  | 14.990000 | 0.000000 | 5079.000000 | 136.000000 | 0.74 | 0.300000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 14.270000 | 14.950000 | 96.000000 | 1018.000000 |  | 14.900000 | 0.000000 | 10000.000000 | 149.000000 | 0.96 | 0.380000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 14.080000 | 14.890000 | 95.000000 | 1018.000000 |  | 14.870000 | 0.000000 | 10000.000000 | 168.000000 | 0.76 | 0.280000 | 804 | Clouds | overcast clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 04:00:00 | 99.000000 | 13.910000 | 14.710000 | 95.000000 | 1018.000000 |  | 14.700000 | 0.000000 | 10000.000000 | 169.000000 | 0.78 | 0.360000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 05:00:00 | 100.000000 | 13.840000 | 14.630000 | 95.000000 | 1018.000000 |  | 14.630000 | 0.000000 | 10000.000000 | 156.000000 | 0.9 | 0.350000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 06:00:00 | 74.000000 | 14.020000 | 14.680000 | 96.000000 | 1016.000000 |  | 14.650000 | 0.000000 | 10000.000000 | 140.000000 | 0.76 | 0.300000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 07:00:00 | 95.000000 | 13.490000 | 14.240000 | 95.000000 | 1015.000000 |  | 14.280000 | 0.000000 | 10000.000000 | 234.000000 | 0.5 | 0.330000 | 804 | Clouds | overcast clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 08:00:00 | 94.000000 | 12.890000 | 13.880000 | 93.000000 | 1015.000000 |  | 14.000000 | 0.000000 | 10000.000000 | 291.000000 | 0.56 | 0.580000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 09:00:00 | 93.000000 | 12.540000 | 13.350000 | 94.000000 | 1015.000000 |  | 13.490000 | 0.000000 | 10000.000000 | 298.000000 | 0.51 | 0.410000 | 804 | Clouds | overcast clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 10:00:00 | 86.000000 | 12.240000 | 12.860000 | 95.000000 | 1016.000000 |  | 13.020000 | 0.000000 | 10000.000000 | 289.000000 | 0.65 | 0.640000 | 804 | Clouds | overcast clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 11:00:00 | 82.000000 | 11.970000 | 12.560000 | 95.000000 | 1017.000000 |  | 12.750000 | 0.000000 | 10000.000000 | 284.000000 | 0.92 | 0.930000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 12:00:00 | 59.000000 | 12.550000 | 14.150000 | 89.000000 | 1018.000000 |  | 14.340000 | 0.610000 | 10000.000000 | 273.000000 | 0.83 | 0.510000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 13:00:00 | 76.000000 | 12.890000 | 16.510000 | 78.000000 | 1018.000000 |  | 16.740000 | 2.530000 | 10000.000000 | 156.000000 | 0.7 | 0.490000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 14:00:00 | 70.000000 | 12.640000 | 18.830000 | 66.000000 | 1018.000000 |  | 19.140000 | 5.900000 | 10000.000000 | 125.000000 | 1.08 | 1.180000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 15:00:00 | 64.000000 | 12.380000 | 20.900000 | 57.000000 | 1017.000000 |  | 21.230000 | 9.820000 | 10000.000000 | 122.000000 | 2.2 | 1.760000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 16:00:00 | 70.000000 | 12.270000 | 21.360000 | 55.000000 | 1015.000000 |  | 21.700000 | 12.420000 | 10000.000000 | 118.000000 | 2.68 | 2.270000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 12.730000 | 20.470000 | 60.000000 | 1015.000000 |  | 20.770000 | 13.350000 | 10000.000000 | 123.000000 | 2.3 | 2.640000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 18:00:00 | 93.000000 | 13.640000 | 19.990000 | 66.000000 | 1014.000000 |  | 20.190000 | 11.960000 | 10000.000000 | 129.000000 | 1.95 | 2.410000 | 804 | Clouds | overcast clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 13.930000 | 18.930000 | 72.000000 | 1013.000000 |  | 19.090000 | 7.260000 | 10000.000000 | 131.000000 | 1.8 | 2.160000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 14.060000 | 19.090000 | 72.000000 | 1012.000000 | 0.12 | 19.230000 | 4.130000 | 10000.000000 | 128.000000 | 1.69 | 2.100000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 21:00:00 | 99.000000 | 14.510000 | 17.760000 | 81.000000 | 1013.000000 | 0.25 | 17.810000 | 1.610000 | 10000.000000 | 126.000000 | 2.14 | 1.950000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 22:00:00 | 95.000000 | 14.700000 | 16.900000 | 87.000000 | 1014.000000 | 0.17 | 16.880000 | 0.290000 | 10000.000000 | 125.000000 | 1.97 | 1.680000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 35085080 | "LA CAPILLA - AUT [35085080]" | 5.099194 | -73.436000 | 1917.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-03-08 00:00:00 | NaT | Boyacá | La Capilla | San Juan | Area Operativa 06 - Boyacá-Casanare-Vichada | Orinoco | Meta | Río Garagoa | America/Bogota | 2022-01-10 23:00:00 | 96.000000 | 14.580000 | 15.600000 | 94.000000 | 1015.000000 | 0.14 | 15.540000 | 0.000000 | 10000.000000 | 129.000000 | 1.9 | 1.070000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station35085080_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Rain_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Temp_20220111.png)
![CNE_IDEAM_Station35085080_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_UVI_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station35085080_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station35085080_OWM_Windspeed_20220111.png)
