
## Weather values for the IDEAM national station catalog - CNE from OWM https://openweathermap.org - AEROPUERTO BENITO SALAS [21115020]

### General parameters

* Current date time: 2022-01-10 17:27:30.876955
* Unix time to eval: 1641749250
* Show historical: True
* Show yesterday: True
* Show OWM API detail: True
* Request OWM data: True
* Days before: 1
* Unit system: metric
* Icons from: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file downloaded and updated: No
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220110.xls
* CNE IDEAM stations: 4489
* CNE IDEAM attributes: 19
* CNE IDEAM status filter: ['Activa', 'En Mantenimiento']
* CNE IDEAM category filter: ['Sinóptica Secundaria']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21115020_OWM_20220110.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220110.csv)


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
| Julian | N/A | N/A | Pseudo julian value for spatial intepolation. [More info.](https://github.com/rcfdtools/R.GISPython/tree/main/TableInterpolatedGrid) |

> Some definitions are taken from https://openweathermap.org/

> N/A: Does not apply. Some parameters become from the IDEAM CNE file or from the openweathermap dictionary API

### 2051 - Open Weather values for station 000021115020: AEROPUERTO BENITO SALAS [21115020]

JSON data from API OWM:

```
{'lat': 2.9488, 'lon': -75.2931, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641749250, 'sunrise': 1641726558, 'sunset': 1641769614, 'temp': 30.97, 'feels_like': 32.77, 'pressure': 1013, 'humidity': 51, 'dew_point': 19.65, 'uvi': 12.57, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, 'hourly': [{'dt': 1641686400, 'temp': 27.97, 'feels_like': 29.52, 'pressure': 1011, 'humidity': 61, 'dew_point': 19.75, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 40, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.27}}, {'dt': 1641690000, 'temp': 26.97, 'feels_like': 28.41, 'pressure': 1012, 'humidity': 65, 'dew_point': 19.83, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 10, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.25}}, {'dt': 1641693600, 'temp': 26.97, 'feels_like': 28.41, 'pressure': 1013, 'humidity': 65, 'dew_point': 19.83, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.69}}, {'dt': 1641697200, 'temp': 26.97, 'feels_like': 28.41, 'pressure': 1013, 'humidity': 65, 'dew_point': 19.83, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.08}}, {'dt': 1641700800, 'temp': 21.8, 'feels_like': 22.2, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.79, 'uvi': 0, 'clouds': 46, 'visibility': 6356, 'wind_speed': 0.94, 'wind_deg': 173, 'wind_gust': 1.56, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.29}}, {'dt': 1641704400, 'temp': 21.66, 'feels_like': 22.05, 'pressure': 1015, 'humidity': 83, 'dew_point': 18.65, 'uvi': 0, 'clouds': 47, 'visibility': 10000, 'wind_speed': 0.83, 'wind_deg': 164, 'wind_gust': 1.35, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'rain': {'1h': 1.31}}, {'dt': 1641708000, 'temp': 21.36, 'feels_like': 21.77, 'pressure': 1014, 'humidity': 85, 'dew_point': 18.74, 'uvi': 0, 'clouds': 44, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 172, 'wind_gust': 1.01, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.68}}, {'dt': 1641711600, 'temp': 21.53, 'feels_like': 21.93, 'pressure': 1014, 'humidity': 84, 'dew_point': 18.71, 'uvi': 0, 'clouds': 70, 'visibility': 10000, 'wind_speed': 0.28, 'wind_deg': 171, 'wind_gust': 0.71, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.12}}, {'dt': 1641715200, 'temp': 21.45, 'feels_like': 21.87, 'pressure': 1013, 'humidity': 85, 'dew_point': 18.82, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0.65, 'wind_deg': 148, 'wind_gust': 1, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.15}}, {'dt': 1641718800, 'temp': 21.4, 'feels_like': 21.82, 'pressure': 1013, 'humidity': 85, 'dew_point': 18.77, 'uvi': 0, 'clouds': 78, 'visibility': 10000, 'wind_speed': 0.49, 'wind_deg': 129, 'wind_gust': 0.81, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641722400, 'temp': 21.34, 'feels_like': 21.75, 'pressure': 1014, 'humidity': 85, 'dew_point': 18.72, 'uvi': 0, 'clouds': 79, 'visibility': 10000, 'wind_speed': 0.33, 'wind_deg': 135, 'wind_gust': 0.67, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641726000, 'temp': 23.97, 'feels_like': 24.59, 'pressure': 1014, 'humidity': 83, 'dew_point': 20.91, 'uvi': 0, 'clouds': 90, 'visibility': 9000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}]}, {'dt': 1641729600, 'temp': 23.97, 'feels_like': 24.59, 'pressure': 1015, 'humidity': 83, 'dew_point': 20.91, 'uvi': 0.23, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641733200, 'temp': 24.97, 'feels_like': 25.56, 'pressure': 1016, 'humidity': 78, 'dew_point': 20.87, 'uvi': 2.08, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641736800, 'temp': 26.97, 'feels_like': 28.72, 'pressure': 1016, 'humidity': 69, 'dew_point': 20.8, 'uvi': 5.03, 'clouds': 20, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641740400, 'temp': 28.97, 'feels_like': 31.14, 'pressure': 1016, 'humidity': 61, 'dew_point': 20.69, 'uvi': 8.58, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 40, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641744000, 'temp': 30.97, 'feels_like': 33.61, 'pressure': 1015, 'humidity': 55, 'dew_point': 20.87, 'uvi': 11.4, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641747600, 'temp': 30.97, 'feels_like': 32.77, 'pressure': 1013, 'humidity': 51, 'dew_point': 19.65, 'uvi': 12.57, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641751200, 'temp': 31.97, 'feels_like': 33.19, 'pressure': 1011, 'humidity': 45, 'dew_point': 18.56, 'uvi': 11.54, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 10, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641754800, 'temp': 32.97, 'feels_like': 33.74, 'pressure': 1010, 'humidity': 40, 'dew_point': 17.58, 'uvi': 8.17, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.15}}, {'dt': 1641758400, 'temp': 32.97, 'feels_like': 34.41, 'pressure': 1009, 'humidity': 43, 'dew_point': 18.73, 'uvi': 4.87, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 30, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}, {'dt': 1641762000, 'temp': 32.97, 'feels_like': 33.74, 'pressure': 1008, 'humidity': 40, 'dew_point': 17.58, 'uvi': 2.08, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 20, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.2}}, {'dt': 1641765600, 'temp': 32.97, 'feels_like': 33.74, 'pressure': 1008, 'humidity': 40, 'dew_point': 17.58, 'uvi': 0.42, 'clouds': 20, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 20, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}, {'dt': 1641769200, 'temp': 29.97, 'feels_like': 31.66, 'pressure': 1008, 'humidity': 54, 'dew_point': 19.65, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 20, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Julian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 00:00:00 | 75.000000 | 19.750000 | 29.520000 | 61.000000 | 1011.000000 | 0.27 | 27.970000 | 0.000000 | 10000.000000 | 40.000000 |  | 2.570000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 01:00:00 | 75.000000 | 19.830000 | 28.410000 | 65.000000 | 1012.000000 | 0.25 | 26.970000 | 0.000000 | 10000.000000 | 10.000000 |  | 1.540000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 02:00:00 | 40.000000 | 19.830000 | 28.410000 | 65.000000 | 1013.000000 | 0.69 | 26.970000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 03:00:00 | 40.000000 | 19.830000 | 28.410000 | 65.000000 | 1013.000000 | 1.08 | 26.970000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 501 | Rain | moderate rain | 10n | 03 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 04:00:00 | 46.000000 | 18.790000 | 22.200000 | 83.000000 | 1015.000000 | 1.29 | 21.800000 | 0.000000 | 6356.000000 | 173.000000 | 1.56 | 0.940000 | 501 | Rain | moderate rain | 10n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 05:00:00 | 47.000000 | 18.650000 | 22.050000 | 83.000000 | 1015.000000 | 1.31 | 21.660000 | 0.000000 | 10000.000000 | 164.000000 | 1.35 | 0.830000 | 501 | Rain | moderate rain | 10n | 05 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 06:00:00 | 44.000000 | 18.740000 | 21.770000 | 85.000000 | 1014.000000 | 0.68 | 21.360000 | 0.000000 | 10000.000000 | 172.000000 | 1.01 | 0.550000 | 500 | Rain | light rain | 10n | 06 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 07:00:00 | 70.000000 | 18.710000 | 21.930000 | 84.000000 | 1014.000000 | 0.12 | 21.530000 | 0.000000 | 10000.000000 | 171.000000 | 0.71 | 0.280000 | 500 | Rain | light rain | 10n | 07 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 08:00:00 | 75.000000 | 18.820000 | 21.870000 | 85.000000 | 1013.000000 | 0.15 | 21.450000 | 0.000000 | 10000.000000 | 148.000000 | 1 | 0.650000 | 500 | Rain | light rain | 10n | 08 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 09:00:00 | 78.000000 | 18.770000 | 21.820000 | 85.000000 | 1013.000000 |  | 21.400000 | 0.000000 | 10000.000000 | 129.000000 | 0.81 | 0.490000 | 803 | Clouds | broken clouds | 04n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 10:00:00 | 79.000000 | 18.720000 | 21.750000 | 85.000000 | 1014.000000 |  | 21.340000 | 0.000000 | 10000.000000 | 135.000000 | 0.67 | 0.330000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 11:00:00 | 90.000000 | 20.910000 | 24.590000 | 83.000000 | 1014.000000 |  | 23.970000 | 0.000000 | 9000.000000 | 0.000000 |  | 0.000000 | 721 | Haze | haze | 50n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 12:00:00 | 75.000000 | 20.910000 | 24.590000 | 83.000000 | 1015.000000 |  | 23.970000 | 0.230000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 13:00:00 | 40.000000 | 20.870000 | 25.560000 | 78.000000 | 1016.000000 |  | 24.970000 | 2.080000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03d | 13 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 14:00:00 | 20.000000 | 20.800000 | 28.720000 | 69.000000 | 1016.000000 |  | 26.970000 | 5.030000 | 10000.000000 | 0.000000 |  | 1.030000 | 801 | Clouds | few clouds | 02d | 14 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 15:00:00 | 20.000000 | 20.690000 | 31.140000 | 61.000000 | 1016.000000 |  | 28.970000 | 8.580000 | 10000.000000 | 40.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 15 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 16:00:00 | 20.000000 | 20.870000 | 33.610000 | 55.000000 | 1015.000000 |  | 30.970000 | 11.400000 | 10000.000000 | 0.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02d | 16 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 17:00:00 | 20.000000 | 19.650000 | 32.770000 | 51.000000 | 1013.000000 |  | 30.970000 | 12.570000 | 10000.000000 | 20.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 17 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 18:00:00 | 20.000000 | 18.560000 | 33.190000 | 45.000000 | 1011.000000 |  | 31.970000 | 11.540000 | 10000.000000 | 10.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 19:00:00 | 20.000000 | 17.580000 | 33.740000 | 40.000000 | 1010.000000 | 0.15 | 32.970000 | 8.170000 | 10000.000000 | 20.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 20:00:00 | 20.000000 | 18.730000 | 34.410000 | 43.000000 | 1009.000000 | 0.18 | 32.970000 | 4.870000 | 10000.000000 | 30.000000 |  | 3.600000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 21:00:00 | 20.000000 | 17.580000 | 33.740000 | 40.000000 | 1008.000000 | 0.2 | 32.970000 | 2.080000 | 10000.000000 | 20.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 21 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 22:00:00 | 20.000000 | 17.580000 | 33.740000 | 40.000000 | 1008.000000 |  | 32.970000 | 0.420000 | 10000.000000 | 20.000000 |  | 4.120000 | 801 | Clouds | few clouds | 02d | 22 |
| ![02d.png](http://openweathermap.org/img/w/02d.png) | 21115020 | "AEROPUERTO BENITO SALAS [21115020]" | 2.948750 | -75.293056 | 439.000000 | Sinóptica Secundaria | Convencional | Activa | 1930-01-15 00:00:00 | NaT | Huila | Neiva | Ariari | Area Operativa 04 - Huila-Caquetá | Magdalena Cauca | Alto Magdalena | Rio Fortalecillas y otros | America/Bogota | 2022-01-09 23:00:00 | 20.000000 | 19.650000 | 31.660000 | 54.000000 | 1008.000000 |  | 29.970000 | 0.000000 | 10000.000000 | 20.000000 |  | 3.600000 | 801 | Clouds | few clouds | 02d | 23 |
