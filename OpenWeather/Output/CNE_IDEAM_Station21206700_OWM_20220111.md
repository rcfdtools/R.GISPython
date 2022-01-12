
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - CEA CENT.EST.AERO. [21206700] - Historical

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
* CNE IDEAM category filter: ['Clim�tica Principal']
* CNE IDEAM technology filter: ['All', 'Autom�tica sin Telemetr�a']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['All']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21206700_OWM_20220111.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220111.csv)


#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.69102778,-74.13441667) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.69102778&lon=-74.13441667)


| Parameter | Value |
|---|---|
| Code | 21206700 |
| Name | CEA CENT.EST.AERO. [21206700] |
| Latitude, � | 4.69102778 |
| Longitude, � | -74.13441667 |
| Elevation, m | 2545 |
| Category | Clim�tica Principal |
| Technology | Convencional |
| Status | Suspendida |
| Installation date | 2002-08-15 00:00:00 |
| Suspension date | 2009-09-07 00:00:00 |
| State | Bogot� |
| County | Bogota, D.C |
| Stream | Sumapaz |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | R�o Bogot� |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit | openweathermap name |
|---|---|---|
| Temperature | �C | temp |
| Dew Point | �C | dew_point |
| Feels like | �C | feels_like |
| Clouds | % | clouds |
| Humidity | % | humidity |
| Pressure | hPa | pressure |
| Wind Direction | � | wind_deg |
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

### (CNE index 1243) Open Weather values for station 21206700 - CEA CENT.EST.AERO. [21206700]

JSON data from API OWM:

```
{'lat': 4.691, 'lon': -74.1344, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1641843725, 'sunrise': 1641812871, 'sunset': 1641855593, 'temp': 18.02, 'feels_like': 17.42, 'pressure': 1024, 'humidity': 59, 'dew_point': 9.9, 'uvi': 4.08, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, 'hourly': [{'dt': 1641772800, 'temp': 13.02, 'feels_like': 12.68, 'pressure': 1025, 'humidity': 88, 'dew_point': 11.08, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641776400, 'temp': 14.02, 'feels_like': 13.62, 'pressure': 1026, 'humidity': 82, 'dew_point': 11, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 300, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641780000, 'temp': 13.02, 'feels_like': 12.68, 'pressure': 1027, 'humidity': 88, 'dew_point': 11.08, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 300, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641783600, 'temp': 13.02, 'feels_like': 12.68, 'pressure': 1027, 'humidity': 88, 'dew_point': 11.08, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 240, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641787200, 'temp': 13.02, 'feels_like': 12.68, 'pressure': 1027, 'humidity': 88, 'dew_point': 11.08, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 290, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641790800, 'temp': 11.02, 'feels_like': 10.61, 'pressure': 1027, 'humidity': 93, 'dew_point': 9.93, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641794400, 'temp': 9.02, 'feels_like': 7.61, 'pressure': 1026, 'humidity': 100, 'dew_point': 9.02, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641798000, 'temp': 8.02, 'feels_like': 8.02, 'pressure': 1025, 'humidity': 100, 'dew_point': 8.02, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641801600, 'temp': 8.02, 'feels_like': 6.83, 'pressure': 1025, 'humidity': 93, 'dew_point': 6.96, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 300, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1641805200, 'temp': 8.02, 'feels_like': 7.35, 'pressure': 1025, 'humidity': 93, 'dew_point': 6.96, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 270, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641808800, 'temp': 9.02, 'feels_like': 9.02, 'pressure': 1025, 'humidity': 93, 'dew_point': 7.95, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]}, {'dt': 1641812400, 'temp': 10.02, 'feels_like': 9.69, 'pressure': 1025, 'humidity': 100, 'dew_point': 10.02, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 0, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1641816000, 'temp': 10.02, 'feels_like': 9.69, 'pressure': 1027, 'humidity': 100, 'dew_point': 10.02, 'uvi': 0.51, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641819600, 'temp': 11.02, 'feels_like': 10.79, 'pressure': 1028, 'humidity': 100, 'dew_point': 11.02, 'uvi': 2.15, 'clouds': 75, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 50, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641823200, 'temp': 14.02, 'feels_like': 13.49, 'pressure': 1028, 'humidity': 77, 'dew_point': 10.06, 'uvi': 5.15, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641826800, 'temp': 16.02, 'feels_like': 15.43, 'pressure': 1028, 'humidity': 67, 'dew_point': 9.9, 'uvi': 8.7, 'clouds': 40, 'visibility': 10000, 'wind_speed': 2.06, 'wind_deg': 310, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641830400, 'temp': 17.02, 'feels_like': 16.42, 'pressure': 1027, 'humidity': 63, 'dew_point': 9.93, 'uvi': 11.7, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 40, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1641834000, 'temp': 17.02, 'feels_like': 16.42, 'pressure': 1027, 'humidity': 63, 'dew_point': 9.93, 'uvi': 12.73, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 280, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641837600, 'temp': 18.02, 'feels_like': 17.42, 'pressure': 1026, 'humidity': 59, 'dew_point': 9.9, 'uvi': 11.55, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 320, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1641841200, 'temp': 18.02, 'feels_like': 17.42, 'pressure': 1025, 'humidity': 59, 'dew_point': 9.9, 'uvi': 7.01, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.23}}, {'dt': 1641844800, 'temp': 18.02, 'feels_like': 17.42, 'pressure': 1024, 'humidity': 59, 'dew_point': 9.9, 'uvi': 4.08, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.4}}, {'dt': 1641848400, 'temp': 18.02, 'feels_like': 17.31, 'pressure': 1024, 'humidity': 55, 'dew_point': 8.85, 'uvi': 1.64, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 260, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.47}}, {'dt': 1641852000, 'temp': 17.02, 'feels_like': 16.42, 'pressure': 1024, 'humidity': 63, 'dew_point': 9.93, 'uvi': 0.43, 'clouds': 40, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 280, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.44}}, {'dt': 1641855600, 'temp': 15.02, 'feels_like': 14.72, 'pressure': 1025, 'humidity': 82, 'dew_point': 11.98, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 4.63, 'wind_deg': 270, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.3}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 00:00:00 | 40.000000 | 11.080000 | 12.680000 | 88.000000 | 1025.000000 |  | 13.020000 | 0.000000 | 10000.000000 | 310.000000 |  | 3.600000 | 802 | Clouds | scattered clouds | 03n | 00 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 01:00:00 | 75.000000 | 11.000000 | 13.620000 | 82.000000 | 1026.000000 |  | 14.020000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.090000 | 803 | Clouds | broken clouds | 04n | 01 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 02:00:00 | 20.000000 | 11.080000 | 12.680000 | 88.000000 | 1027.000000 |  | 13.020000 | 0.000000 | 10000.000000 | 300.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 02 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 03:00:00 | 20.000000 | 11.080000 | 12.680000 | 88.000000 | 1027.000000 |  | 13.020000 | 0.000000 | 10000.000000 | 240.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 04:00:00 | 20.000000 | 11.080000 | 12.680000 | 88.000000 | 1027.000000 |  | 13.020000 | 0.000000 | 10000.000000 | 290.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 04 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 05:00:00 | 40.000000 | 9.930000 | 10.610000 | 93.000000 | 1027.000000 |  | 11.020000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 05 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 06:00:00 | 75.000000 | 9.020000 | 7.610000 | 100.000000 | 1026.000000 |  | 9.020000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 803 | Clouds | broken clouds | 04n | 06 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 07:00:00 | 20.000000 | 8.020000 | 8.020000 | 100.000000 | 1025.000000 |  | 8.020000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 801 | Clouds | few clouds | 02n | 07 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 08:00:00 | 20.000000 | 6.960000 | 6.830000 | 93.000000 | 1025.000000 |  | 8.020000 | 0.000000 | 10000.000000 | 300.000000 |  | 2.060000 | 801 | Clouds | few clouds | 02n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 09:00:00 | 40.000000 | 6.960000 | 7.350000 | 93.000000 | 1025.000000 |  | 8.020000 | 0.000000 | 10000.000000 | 270.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![04n.png](http://openweathermap.org/img/w/04n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 10:00:00 | 75.000000 | 7.950000 | 9.020000 | 93.000000 | 1025.000000 |  | 9.020000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 803 | Clouds | broken clouds | 04n | 10 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 11:00:00 | 40.000000 | 10.020000 | 9.690000 | 100.000000 | 1025.000000 |  | 10.020000 | 0.000000 | 10000.000000 | 0.000000 |  | 0.000000 | 802 | Clouds | scattered clouds | 03n | 11 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 12:00:00 | 75.000000 | 10.020000 | 9.690000 | 100.000000 | 1027.000000 |  | 10.020000 | 0.510000 | 10000.000000 | 0.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 12 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 13:00:00 | 75.000000 | 11.020000 | 10.790000 | 100.000000 | 1028.000000 |  | 11.020000 | 2.150000 | 10000.000000 | 50.000000 |  | 2.060000 | 803 | Clouds | broken clouds | 04d | 13 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 14:00:00 | 40.000000 | 10.060000 | 13.490000 | 77.000000 | 1028.000000 |  | 14.020000 | 5.150000 | 10000.000000 | 40.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 14 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 15:00:00 | 40.000000 | 9.900000 | 15.430000 | 67.000000 | 1028.000000 |  | 16.020000 | 8.700000 | 10000.000000 | 310.000000 |  | 2.060000 | 802 | Clouds | scattered clouds | 03d | 15 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 16:00:00 | 40.000000 | 9.930000 | 16.420000 | 63.000000 | 1027.000000 |  | 17.020000 | 11.700000 | 10000.000000 | 40.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 17:00:00 | 75.000000 | 9.930000 | 16.420000 | 63.000000 | 1027.000000 |  | 17.020000 | 12.730000 | 10000.000000 | 280.000000 |  | 4.120000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 18:00:00 | 75.000000 | 9.900000 | 17.420000 | 59.000000 | 1026.000000 |  | 18.020000 | 11.550000 | 10000.000000 | 320.000000 |  | 4.630000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 19:00:00 | 75.000000 | 9.900000 | 17.420000 | 59.000000 | 1025.000000 | 0.23 | 18.020000 | 7.010000 | 10000.000000 | 310.000000 |  | 4.630000 | 500 | Rain | light rain | 10d | 19 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 20:00:00 | 75.000000 | 9.900000 | 17.420000 | 59.000000 | 1024.000000 | 0.4 | 18.020000 | 4.080000 | 10000.000000 | 300.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 20 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 21:00:00 | 40.000000 | 8.850000 | 17.310000 | 55.000000 | 1024.000000 | 0.47 | 18.020000 | 1.640000 | 10000.000000 | 260.000000 |  | 4.120000 | 500 | Rain | light rain | 10d | 21 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 22:00:00 | 40.000000 | 9.930000 | 16.420000 | 63.000000 | 1024.000000 | 0.44 | 17.020000 | 0.430000 | 10000.000000 | 280.000000 |  | 5.140000 | 500 | Rain | light rain | 10d | 22 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21206700 | "CEA CENT.EST.AERO. [21206700]" | 4.691028 | -74.134417 | 2545.000000 | Clim�tica Principal | Convencional | Suspendida | 2002-08-15 00:00:00 | 2009-09-07 00:00:00 | Bogot� | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-10 23:00:00 | 40.000000 | 11.980000 | 14.720000 | 82.000000 | 1025.000000 | 0.3 | 15.020000 | 0.000000 | 10000.000000 | 270.000000 |  | 4.630000 | 500 | Rain | light rain | 10n | 23 |


### Weather plots

![CNE_IDEAM_Station21206700_OWM_Clouds_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Clouds_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Dewpoint_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Dewpoint_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Feelslike_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Feelslike_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Humidity_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Humidity_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Pressure_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Pressure_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Rain_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Rain_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Temp_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Temp_20220111.png)
![CNE_IDEAM_Station21206700_OWM_UVI_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_UVI_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Visibility_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Visibility_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Windgust_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Windgust_20220111.png)
![CNE_IDEAM_Station21206700_OWM_Windspeed_20220111.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21206700_OWM_Windspeed_20220111.png)
