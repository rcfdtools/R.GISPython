
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - LA PLATA - AUT [21115170] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21115170_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=2.75913889,-75.07455556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=2.75913889&lon=-75.07455556)


| Parameter | Value |
|---|---|
| Code | 21115170 |
| Name | LA PLATA - AUT [21115170] |
| Latitude, ° | 2.75913889 |
| Longitude, ° | -75.07455556 |
| Elevation, m | 2101 |
| Category | Climática Principal |
| Technology | Automática con Telemetría |
| Status | Activa |
| Installation date | 2005-07-20 00:00:00 |
| Suspension date | NaT |
| State | Huila |
| County | Neiva |
| Stream | Paez |
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

### (CNE index 36) Open Weather values for station 21115170 - LA PLATA - AUT [21115170]

JSON data from API OWM:

```
{'lat': 2.7591, 'lon': -75.0746, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812909, 'sunset': 1641856006, 'temp': 20.69, 'feels_like': 21.01, 'pressure': 1012, 'humidity': 84, 'dew_point': 17.89, 'uvi': 5.43, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 85, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, 'hourly': [{'dt': 1641772800, 'temp': 16.69, 'feels_like': 16.84, 'pressure': 1014, 'humidity': 93, 'dew_point': 15.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.21, 'wind_deg': 114, 'wind_gust': 0.99, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 16.69, 'feels_like': 16.84, 'pressure': 1016, 'humidity': 93, 'dew_point': 15.55, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.28, 'wind_deg': 114, 'wind_gust': 1.05, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 15.69, 'feels_like': 15.77, 'pressure': 1017, 'humidity': 94, 'dew_point': 14.73, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 111, 'wind_gust': 1.01, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 15.69, 'feels_like': 15.77, 'pressure': 1017, 'humidity': 94, 'dew_point': 14.73, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 107, 'wind_gust': 0.97, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641787200, 'temp': 11.06, 'feels_like': 10.68, 'pressure': 1017, 'humidity': 94, 'dew_point': 10.13, 'uvi': 0, 'clouds': 100, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 118, 'wind_gust': 0.92, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 10.77, 'feels_like': 10.36, 'pressure': 1016, 'humidity': 94, 'dew_point': 9.84, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.17, 'wind_deg': 116, 'wind_gust': 0.91, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641794400, 'temp': 11.1, 'feels_like': 10.72, 'pressure': 1016, 'humidity': 94, 'dew_point': 10.17, 'uvi': 0, 'clouds': 71, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 107, 'wind_gust': 0.85, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.22}}, {'dt': 1641798000, 'temp': 10.97, 'feels_like': 10.6, 'pressure': 1015, 'humidity': 95, 'dew_point': 10.2, 'uvi': 0, 'clouds': 77, 'visibility': 10000, 'wind_speed': 1.01, 'wind_deg': 101, 'wind_gust': 0.87, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.19}}, {'dt': 1641801600, 'temp': 11.19, 'feels_like': 10.82, 'pressure': 1014, 'humidity': 94, 'dew_point': 10.26, 'uvi': 0, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 111, 'wind_gust': 0.78, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 11.31, 'feels_like': 10.98, 'pressure': 1014, 'humidity': 95, 'dew_point': 10.54, 'uvi': 0, 'clouds': 84, 'visibility': 10000, 'wind_speed': 0.69, 'wind_deg': 115, 'wind_gust': 0.66, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1641808800, 'temp': 11.56, 'feels_like': 11.23, 'pressure': 1015, 'humidity': 94, 'dew_point': 10.63, 'uvi': 0, 'clouds': 88, 'visibility': 10000, 'wind_speed': 0.81, 'wind_deg': 111, 'wind_gust': 0.8, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641812400, 'temp': 12.69, 'feels_like': 12.47, 'pressure': 1015, 'humidity': 94, 'dew_point': 11.75, 'uvi': 0, 'clouds': 87, 'visibility': 10000, 'wind_speed': 1.04, 'wind_deg': 108, 'wind_gust': 0.93, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641816000, 'temp': 12.69, 'feels_like': 12.44, 'pressure': 1016, 'humidity': 93, 'dew_point': 11.59, 'uvi': 0.46, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 112, 'wind_gust': 0.61, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 14.69, 'feels_like': 14.56, 'pressure': 1017, 'humidity': 90, 'dew_point': 13.07, 'uvi': 2.12, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.2, 'wind_deg': 88, 'wind_gust': 0.71, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 16.69, 'feels_like': 16.63, 'pressure': 1017, 'humidity': 85, 'dew_point': 14.16, 'uvi': 5.16, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.4, 'wind_deg': 28, 'wind_gust': 1.05, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.24}}, {'dt': 1641826800, 'temp': 16.69, 'feels_like': 16.45, 'pressure': 1016, 'humidity': 78, 'dew_point': 12.84, 'uvi': 8.8, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.51, 'wind_deg': 8, 'wind_gust': 1.5, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.6}}, {'dt': 1641830400, 'temp': 17.69, 'feels_like': 17.45, 'pressure': 1015, 'humidity': 74, 'dew_point': 13, 'uvi': 11.34, 'clouds': 81, 'visibility': 10000, 'wind_speed': 0.44, 'wind_deg': 0, 'wind_gust': 1.43, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.39}}, {'dt': 1641834000, 'temp': 18.69, 'feels_like': 18.73, 'pressure': 1015, 'humidity': 81, 'dew_point': 15.37, 'uvi': 12.5, 'clouds': 85, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 48, 'wind_gust': 1.7, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.77}}, {'dt': 1641837600, 'temp': 20.69, 'feels_like': 21.06, 'pressure': 1014, 'humidity': 86, 'dew_point': 18.27, 'uvi': 11.47, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.62, 'wind_deg': 80, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.81}}, {'dt': 1641841200, 'temp': 20.69, 'feels_like': 21.06, 'pressure': 1013, 'humidity': 86, 'dew_point': 18.27, 'uvi': 9.12, 'clouds': 100, 'visibility': 10000, 'wind_speed': 0.87, 'wind_deg': 80, 'wind_gust': 1.61, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.83}}, {'dt': 1641844800, 'temp': 20.69, 'feels_like': 21.01, 'pressure': 1012, 'humidity': 84, 'dew_point': 17.89, 'uvi': 5.43, 'clouds': 99, 'visibility': 10000, 'wind_speed': 1.02, 'wind_deg': 85, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.37}}, {'dt': 1641848400, 'temp': 19.69, 'feels_like': 19.93, 'pressure': 1012, 'humidity': 85, 'dew_point': 17.1, 'uvi': 2.32, 'clouds': 93, 'visibility': 10000, 'wind_speed': 0.99, 'wind_deg': 93, 'wind_gust': 1.75, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.49}}, {'dt': 1641852000, 'temp': 18.69, 'feels_like': 18.96, 'pressure': 1012, 'humidity': 90, 'dew_point': 17.02, 'uvi': 0.56, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 99, 'wind_gust': 2.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.56}}, {'dt': 1641855600, 'temp': 17.69, 'feels_like': 17.94, 'pressure': 1013, 'humidity': 93, 'dew_point': 16.54, 'uvi': 0, 'clouds': 81, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 116, 'wind_gust': 1.81, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.28}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 00:00:00 | 100.000000 | 15.550000 | 16.840000 | 93.000000 | 1014.000000 |  | 16.690000 | 0.000000 | 10000.000000 | 114.000000 | 0.99 | 1.210000 | 804 | Clouds | overcast clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 01:00:00 | 100.000000 | 15.550000 | 16.840000 | 93.000000 | 1016.000000 |  | 16.690000 | 0.000000 | 10000.000000 | 114.000000 | 1.05 | 1.280000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 02:00:00 | 100.000000 | 14.730000 | 15.770000 | 94.000000 | 1017.000000 |  | 15.690000 | 0.000000 | 10000.000000 | 111.000000 | 1.01 | 1.190000 | 804 | Clouds | overcast clouds | 04n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 03:00:00 | 100.000000 | 14.730000 | 15.770000 | 94.000000 | 1017.000000 | 0.12 | 15.690000 | 0.000000 | 10000.000000 | 107.000000 | 0.97 | 1.150000 | 500 | Rain | light rain | 10n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 04:00:00 | 100.000000 | 10.130000 | 10.680000 | 94.000000 | 1017.000000 |  | 11.060000 | 0.000000 | 10000.000000 | 118.000000 | 0.92 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 04 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 05:00:00 | 87.000000 | 9.840000 | 10.360000 | 94.000000 | 1016.000000 |  | 10.770000 | 0.000000 | 10000.000000 | 116.000000 | 0.91 | 1.170000 | 804 | Clouds | overcast clouds | 04n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 06:00:00 | 71.000000 | 10.170000 | 10.720000 | 94.000000 | 1016.000000 | 0.22 | 11.100000 | 0.000000 | 10000.000000 | 107.000000 | 0.85 | 1.080000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 07:00:00 | 77.000000 | 10.200000 | 10.600000 | 95.000000 | 1015.000000 | 0.19 | 10.970000 | 0.000000 | 10000.000000 | 101.000000 | 0.87 | 1.010000 | 500 | Rain | light rain | 10n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 08:00:00 | 85.000000 | 10.260000 | 10.820000 | 94.000000 | 1014.000000 |  | 11.190000 | 0.000000 | 10000.000000 | 111.000000 | 0.78 | 0.870000 | 804 | Clouds | overcast clouds | 04n | 08 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 09:00:00 | 84.000000 | 10.540000 | 10.980000 | 95.000000 | 1014.000000 | 0.11 | 11.310000 | 0.000000 | 10000.000000 | 115.000000 | 0.66 | 0.690000 | 500 | Rain | light rain | 10n | 09 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 10:00:00 | 88.000000 | 10.630000 | 11.230000 | 94.000000 | 1015.000000 | 0.12 | 11.560000 | 0.000000 | 10000.000000 | 111.000000 | 0.8 | 0.810000 | 500 | Rain | light rain | 10n | 10 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 11:00:00 | 87.000000 | 11.750000 | 12.470000 | 94.000000 | 1015.000000 | 0.12 | 12.690000 | 0.000000 | 10000.000000 | 108.000000 | 0.93 | 1.040000 | 500 | Rain | light rain | 10n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 12:00:00 | 100.000000 | 11.590000 | 12.440000 | 93.000000 | 1016.000000 |  | 12.690000 | 0.460000 | 10000.000000 | 112.000000 | 0.61 | 0.620000 | 804 | Clouds | overcast clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 13:00:00 | 100.000000 | 13.070000 | 14.560000 | 90.000000 | 1017.000000 |  | 14.690000 | 2.120000 | 10000.000000 | 88.000000 | 0.71 | 0.200000 | 804 | Clouds | overcast clouds | 04d | 13 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 14:00:00 | 90.000000 | 14.160000 | 16.630000 | 85.000000 | 1017.000000 | 0.24 | 16.690000 | 5.160000 | 10000.000000 | 28.000000 | 1.05 | 0.400000 | 500 | Rain | light rain | 10d | 14 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 15:00:00 | 75.000000 | 12.840000 | 16.450000 | 78.000000 | 1016.000000 | 0.6 | 16.690000 | 8.800000 | 10000.000000 | 8.000000 | 1.5 | 0.510000 | 500 | Rain | light rain | 10d | 15 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 16:00:00 | 81.000000 | 13.000000 | 17.450000 | 74.000000 | 1015.000000 | 0.39 | 17.690000 | 11.340000 | 10000.000000 | 0.000000 | 1.43 | 0.440000 | 500 | Rain | light rain | 10d | 16 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 17:00:00 | 85.000000 | 15.370000 | 18.730000 | 81.000000 | 1015.000000 | 0.77 | 18.690000 | 12.500000 | 10000.000000 | 48.000000 | 1.7 | 0.490000 | 500 | Rain | light rain | 10d | 17 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 18:00:00 | 100.000000 | 18.270000 | 21.060000 | 86.000000 | 1014.000000 | 0.81 | 20.690000 | 11.470000 | 10000.000000 | 80.000000 | 2.01 | 0.620000 | 500 | Rain | light rain | 10d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 19:00:00 | 100.000000 | 18.270000 | 21.060000 | 86.000000 | 1013.000000 | 0.83 | 20.690000 | 9.120000 | 10000.000000 | 80.000000 | 1.61 | 0.870000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 20:00:00 | 99.000000 | 17.890000 | 21.010000 | 84.000000 | 1012.000000 | 0.37 | 20.690000 | 5.430000 | 10000.000000 | 85.000000 | 1.75 | 1.020000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 21:00:00 | 93.000000 | 17.100000 | 19.930000 | 85.000000 | 1012.000000 | 0.49 | 19.690000 | 2.320000 | 10000.000000 | 93.000000 | 1.75 | 0.990000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 22:00:00 | 89.000000 | 17.020000 | 18.960000 | 90.000000 | 1012.000000 | 0.56 | 18.690000 | 0.560000 | 10000.000000 | 99.000000 | 2.01 | 1.200000 | 500 | Rain | light rain | 10d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115170 | "LA PLATA - AUT [21115170]" | 2.759139 | -75.074556 | 2101.000000 | Climática Principal | Automática con Telemetría | Activa | 2005-07-20 00:00:00 | NaT | Huila | Neiva | Paez | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-10 23:00:00 | 81.000000 | 16.540000 | 17.940000 | 93.000000 | 1013.000000 | 0.28 | 17.690000 | 0.000000 | 10000.000000 | 116.000000 | 1.81 | 1.380000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21115170_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21115170_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21115170_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21115170_OWM_Windspeed_20220111.png)
