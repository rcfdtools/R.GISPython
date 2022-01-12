
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CINERA-VILLA OLGA [16025040] - Historical

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
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station16025040_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=8.16777778,-72.46861111) or [Openstreet Map](https://www.openstreetmap.org/query?lat=8.16777778&lon=-72.46861111)


| Parameter | Value |
|---|---|
| Code | 16025040 |
| Name | CINERA-VILLA OLGA [16025040] |
| Latitude, ° | 8.16777778 |
| Longitude, ° | -72.46861111 |
| Elevation, m | 100 |
| Category | Climática Principal |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1965-09-15 00:00:00 |
| Suspension date | NaT |
| State | Norte de Santander |
| County | Cúcuta |
| Stream | Canal Floresta |
| Operator | Area Operativa 08 - Santanderes-Arauca |
| AH - Hydrographic area | Caribe |
| ZH - Hydrographic zone | Catatumbo |
| SZH - Hydrographic subzone | Río Zulia |

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

### (CNE index 2859) Open Weather values for station 16025040 - CINERA-VILLA OLGA [16025040]

JSON data from API OWM:

```
{'lat': 8.1678, 'lon': -72.4686, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812810, 'sunset': 1641854854, 'temp': 30.23, 'feels_like': 30.48, 'pressure': 1009, 'humidity': 44, 'dew_point': 16.63, 'uvi': 3.65, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.97, 'wind_deg': 32, 'wind_gust': 2.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1641772800, 'temp': 25.23, 'feels_like': 25.79, 'pressure': 1013, 'humidity': 76, 'dew_point': 20.7, 'uvi': 0, 'clouds': 80, 'visibility': 10000, 'wind_speed': 1.23, 'wind_deg': 173, 'wind_gust': 1.33, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641776400, 'temp': 25.23, 'feels_like': 25.82, 'pressure': 1014, 'humidity': 77, 'dew_point': 20.91, 'uvi': 0, 'clouds': 89, 'visibility': 10000, 'wind_speed': 1.34, 'wind_deg': 197, 'wind_gust': 1.44, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 24.23, 'feels_like': 24.75, 'pressure': 1015, 'humidity': 78, 'dew_point': 20.15, 'uvi': 0, 'clouds': 73, 'visibility': 10000, 'wind_speed': 1.5, 'wind_deg': 199, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641783600, 'temp': 23.23, 'feels_like': 23.65, 'pressure': 1015, 'humidity': 78, 'dew_point': 19.18, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.22, 'wind_deg': 193, 'wind_gust': 1.39, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641787200, 'temp': 22.23, 'feels_like': 22.55, 'pressure': 1015, 'humidity': 78, 'dew_point': 18.21, 'uvi': 0, 'clouds': 61, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 187, 'wind_gust': 0.89, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641790800, 'temp': 22.23, 'feels_like': 22.6, 'pressure': 1015, 'humidity': 80, 'dew_point': 18.62, 'uvi': 0, 'clouds': 49, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 317, 'wind_gust': 1.07, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 22.23, 'feels_like': 22.6, 'pressure': 1014, 'humidity': 80, 'dew_point': 18.62, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 239, 'wind_gust': 0.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 21.23, 'feels_like': 21.45, 'pressure': 1014, 'humidity': 78, 'dew_point': 17.24, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.92, 'wind_deg': 225, 'wind_gust': 1.32, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641801600, 'temp': 21.32, 'feels_like': 21.49, 'pressure': 1013, 'humidity': 76, 'dew_point': 16.92, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.08, 'wind_deg': 215, 'wind_gust': 1.49, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641805200, 'temp': 21.46, 'feels_like': 21.59, 'pressure': 1013, 'humidity': 74, 'dew_point': 16.64, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 208, 'wind_gust': 1.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641808800, 'temp': 20.23, 'feels_like': 20.21, 'pressure': 1014, 'humidity': 73, 'dew_point': 15.24, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 198, 'wind_gust': 1.6, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 19.23, 'feels_like': 19.09, 'pressure': 1014, 'humidity': 72, 'dew_point': 14.06, 'uvi': 0, 'clouds': 74, 'visibility': 10000, 'wind_speed': 1.3, 'wind_deg': 191, 'wind_gust': 1.73, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641816000, 'temp': 19.23, 'feels_like': 18.98, 'pressure': 1015, 'humidity': 68, 'dew_point': 13.19, 'uvi': 0.49, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 196, 'wind_gust': 2.72, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 23.23, 'feels_like': 23.1, 'pressure': 1016, 'humidity': 57, 'dew_point': 14.25, 'uvi': 2, 'clouds': 79, 'visibility': 10000, 'wind_speed': 1.19, 'wind_deg': 219, 'wind_gust': 2.2, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 26.23, 'feels_like': 26.23, 'pressure': 1016, 'humidity': 50, 'dew_point': 14.99, 'uvi': 4.66, 'clouds': 67, 'visibility': 10000, 'wind_speed': 0.68, 'wind_deg': 262, 'wind_gust': 1.04, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641826800, 'temp': 27.23, 'feels_like': 27.38, 'pressure': 1016, 'humidity': 46, 'dew_point': 14.61, 'uvi': 7.7, 'clouds': 65, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 345, 'wind_gust': 1.05, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641830400, 'temp': 29.23, 'feels_like': 29.14, 'pressure': 1015, 'humidity': 43, 'dew_point': 15.37, 'uvi': 10.12, 'clouds': 67, 'visibility': 10000, 'wind_speed': 1.63, 'wind_deg': 5, 'wind_gust': 1.64, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641834000, 'temp': 29.23, 'feels_like': 28.94, 'pressure': 1013, 'humidity': 41, 'dew_point': 14.63, 'uvi': 10.77, 'clouds': 69, 'visibility': 10000, 'wind_speed': 2.05, 'wind_deg': 11, 'wind_gust': 1.82, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 30.23, 'feels_like': 30.08, 'pressure': 1012, 'humidity': 41, 'dew_point': 15.52, 'uvi': 9.5, 'clouds': 80, 'visibility': 10000, 'wind_speed': 2.39, 'wind_deg': 20, 'wind_gust': 1.9, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 31.23, 'feels_like': 31.37, 'pressure': 1010, 'humidity': 41, 'dew_point': 16.42, 'uvi': 6.66, 'clouds': 96, 'visibility': 10000, 'wind_speed': 2.62, 'wind_deg': 27, 'wind_gust': 1.96, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641844800, 'temp': 30.23, 'feels_like': 30.48, 'pressure': 1009, 'humidity': 44, 'dew_point': 16.63, 'uvi': 3.65, 'clouds': 98, 'visibility': 10000, 'wind_speed': 2.97, 'wind_deg': 32, 'wind_gust': 2.35, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641848400, 'temp': 29.23, 'feels_like': 29.96, 'pressure': 1010, 'humidity': 50, 'dew_point': 17.74, 'uvi': 1.35, 'clouds': 98, 'visibility': 10000, 'wind_speed': 3.02, 'wind_deg': 35, 'wind_gust': 3.3, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641852000, 'temp': 28.23, 'feels_like': 29.79, 'pressure': 1010, 'humidity': 60, 'dew_point': 19.73, 'uvi': 0.23, 'clouds': 97, 'visibility': 10000, 'wind_speed': 2.03, 'wind_deg': 49, 'wind_gust': 3.95, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}, {'dt': 1641855600, 'temp': 28.23, 'feels_like': 30.98, 'pressure': 1011, 'humidity': 69, 'dew_point': 22, 'uvi': 0, 'clouds': 98, 'visibility': 10000, 'wind_speed': 0.84, 'wind_deg': 94, 'wind_gust': 1.19, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 00:00:00 | 80.000000 | 20.700000 | 25.790000 | 76.000000 | 1013.000000 |  | 25.230000 | 0.000000 | 10000.000000 | 173.000000 | 1.33 | 1.230000 | 803 | Clouds | broken clouds | 04n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 01:00:00 | 89.000000 | 20.910000 | 25.820000 | 77.000000 | 1014.000000 |  | 25.230000 | 0.000000 | 10000.000000 | 197.000000 | 1.44 | 1.340000 | 804 | Clouds | overcast clouds | 04n | 01 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 02:00:00 | 73.000000 | 20.150000 | 24.750000 | 78.000000 | 1015.000000 |  | 24.230000 | 0.000000 | 10000.000000 | 199.000000 | 2.2 | 1.500000 | 803 | Clouds | broken clouds | 04n | 02 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 03:00:00 | 74.000000 | 19.180000 | 23.650000 | 78.000000 | 1015.000000 |  | 23.230000 | 0.000000 | 10000.000000 | 193.000000 | 1.39 | 1.220000 | 803 | Clouds | broken clouds | 04n | 03 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 04:00:00 | 61.000000 | 18.210000 | 22.550000 | 78.000000 | 1015.000000 |  | 22.230000 | 0.000000 | 10000.000000 | 187.000000 | 0.89 | 0.650000 | 803 | Clouds | broken clouds | 04n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 05:00:00 | 49.000000 | 18.620000 | 22.600000 | 80.000000 | 1015.000000 |  | 22.230000 | 0.000000 | 10000.000000 | 317.000000 | 1.07 | 0.490000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 06:00:00 | 66.000000 | 18.620000 | 22.600000 | 80.000000 | 1014.000000 |  | 22.230000 | 0.000000 | 10000.000000 | 239.000000 | 0.95 | 0.680000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 07:00:00 | 75.000000 | 17.240000 | 21.450000 | 78.000000 | 1014.000000 |  | 21.230000 | 0.000000 | 10000.000000 | 225.000000 | 1.32 | 0.920000 | 803 | Clouds | broken clouds | 04n | 07 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 08:00:00 | 74.000000 | 16.920000 | 21.490000 | 76.000000 | 1013.000000 |  | 21.320000 | 0.000000 | 10000.000000 | 215.000000 | 1.49 | 1.080000 | 803 | Clouds | broken clouds | 04n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 09:00:00 | 74.000000 | 16.640000 | 21.590000 | 74.000000 | 1013.000000 |  | 21.460000 | 0.000000 | 10000.000000 | 208.000000 | 1.83 | 1.200000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 10:00:00 | 74.000000 | 15.240000 | 20.210000 | 73.000000 | 1014.000000 |  | 20.230000 | 0.000000 | 10000.000000 | 198.000000 | 1.6 | 1.140000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 11:00:00 | 74.000000 | 14.060000 | 19.090000 | 72.000000 | 1014.000000 |  | 19.230000 | 0.000000 | 10000.000000 | 191.000000 | 1.73 | 1.300000 | 803 | Clouds | broken clouds | 04n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 12:00:00 | 79.000000 | 13.190000 | 18.980000 | 68.000000 | 1015.000000 |  | 19.230000 | 0.490000 | 10000.000000 | 196.000000 | 2.72 | 1.320000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 13:00:00 | 79.000000 | 14.250000 | 23.100000 | 57.000000 | 1016.000000 |  | 23.230000 | 2.000000 | 10000.000000 | 219.000000 | 2.2 | 1.190000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 14:00:00 | 67.000000 | 14.990000 | 26.230000 | 50.000000 | 1016.000000 |  | 26.230000 | 4.660000 | 10000.000000 | 262.000000 | 1.04 | 0.680000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 15:00:00 | 65.000000 | 14.610000 | 27.380000 | 46.000000 | 1016.000000 |  | 27.230000 | 7.700000 | 10000.000000 | 345.000000 | 1.05 | 1.030000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 16:00:00 | 67.000000 | 15.370000 | 29.140000 | 43.000000 | 1015.000000 |  | 29.230000 | 10.120000 | 10000.000000 | 5.000000 | 1.64 | 1.630000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 17:00:00 | 69.000000 | 14.630000 | 28.940000 | 41.000000 | 1013.000000 |  | 29.230000 | 10.770000 | 10000.000000 | 11.000000 | 1.82 | 2.050000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 18:00:00 | 80.000000 | 15.520000 | 30.080000 | 41.000000 | 1012.000000 |  | 30.230000 | 9.500000 | 10000.000000 | 20.000000 | 1.9 | 2.390000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 19:00:00 | 96.000000 | 16.420000 | 31.370000 | 41.000000 | 1010.000000 |  | 31.230000 | 6.660000 | 10000.000000 | 27.000000 | 1.96 | 2.620000 | 804 | Clouds | overcast clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 20:00:00 | 98.000000 | 16.630000 | 30.480000 | 44.000000 | 1009.000000 |  | 30.230000 | 3.650000 | 10000.000000 | 32.000000 | 2.35 | 2.970000 | 804 | Clouds | overcast clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 21:00:00 | 98.000000 | 17.740000 | 29.960000 | 50.000000 | 1010.000000 |  | 29.230000 | 1.350000 | 10000.000000 | 35.000000 | 3.3 | 3.020000 | 804 | Clouds | overcast clouds | 04d | 21 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 22:00:00 | 97.000000 | 19.730000 | 29.790000 | 60.000000 | 1010.000000 |  | 28.230000 | 0.230000 | 10000.000000 | 49.000000 | 3.95 | 2.030000 | 804 | Clouds | overcast clouds | 04d | 22 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 16025040 | "CINERA-VILLA OLGA [16025040]" | 8.167778 | -72.468611 | 100.000000 | Climática Principal | Convencional | Activa | 1965-09-15 00:00:00 | NaT | Norte de Santander | Cúcuta | Canal Floresta | Area Operativa 08 - Santanderes-Arauca | Caribe | Catatumbo | Río Zulia | America/Bogota | 2022-01-10 23:00:00 | 98.000000 | 22.000000 | 30.980000 | 69.000000 | 1011.000000 |  | 28.230000 | 0.000000 | 10000.000000 | 94.000000 | 1.19 | 0.840000 | 804 | Clouds | overcast clouds | 04n | 23 |


### Weather plots

![CNE_IDEAM_Station16025040_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Rain_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Temp_20220111.png)
![CNE_IDEAM_Station16025040_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_UVI_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station16025040_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station16025040_OWM_Windspeed_20220111.png)
