
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - VENADO ORO VIVERO [21205580] - Historical

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogot� - Colombia - Suram�rica

### GitHub repository and system information

* Python version: 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.GISPython\\OpenWeather', 'D:\\R.GISPython', 'D:\\R.GISPython.wiki', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs']
* matplotlib version: 3.5.1
* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/OpenWeather
* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License
* Credits: r.cfdtools@gmail.com

### General parameters

* Current date time: 2022-01-30 14:37:17.220329
* Unix time to eval: 1643467037
* Days before (for historical data): 1
* Show historical: True
* Show OWM API detail: True
* Request OWM data: True
* Unit system: metric
* Icons source: http://openweathermap.org/img/w/
* CNE IDEAM source: http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
* CNE IDEAM file: D:/R.GISPython/OpenWeather/Data/CNE_IDEAM_20220130.xls
* CNE IDEAM file downloaded and updated: Yes
* CNE IDEAM stations: 4499
* CNE IDEAM attributes: 20
* CNE IDEAM station code filter: ['All', 26055120, 1508500053]
* CNE IDEAM category filter: ['All']
* CNE IDEAM technology filter: ['All', 'Autom�tica sin Telemetr�a']
* CNE IDEAM status filter: ['All', 'Activa', 'En Mantenimiento']
* CNE IDEAM state filter: ['Bogot�']
* CNE IDEAM county filter: ['All']
* CNE IDEAM stream filter: ['All']
* CNE IDEAM operator filter: ['All']
* CNE IDEAM hydro area filter: ['All']
* CNE IDEAM hydro zone filter: ['All']
* CNE IDEAM hydro subzone filter: ['All']
* Related files: [Station Markdown, ](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_Station21205580_OWM_20220130.md)[General CSV]( https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Output/CNE_IDEAM_OWM_20220130.csv)

> For historical data, the weather information obtain with the OWM API, correspond to the `Current date time` reported less the number of day define in `Days before (for historical data)`. 

> For forecast data, the weather information obtain with the OWM API, correspond to the `Current date time` reported and some further days. 

#### Station parameters and location over [Google Maps](http://maps.google.com/maps?q=4.59836111,-74.06155556) or [Openstreet Map](https://www.openstreetmap.org/query?lat=4.59836111&lon=-74.06155556)

| Parameter | Value |
|---|---|
| Code | 21205580 |
| Name | VENADO ORO VIVERO [21205580] |
| Latitude, � | 4.59836111 |
| Longitude, � | -74.06155556 |
| Elevation, m | 2725 |
| Category | Clim�tica Ordinaria |
| Technology | Convencional |
| Status | Activa |
| Installation date | 1965-08-15 00:00:00 |
| Suspension date | NaT |
| State | Bogot� |
| County | Bogota, D.C |
| Stream | Cauca |
| Operator | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s |
| AH - Hydrographic area | Magdalena Cauca |
| ZH - Hydrographic zone | Alto Magdalena |
| SZH - Hydrographic subzone | R�o Bogot� |

> For `Show historical`, `True` means that we are getting weather historic values with the `Time Machine` option from the openweathermap server, `False` means that we are getting the `Forecast` weather values.

#### Unit system (metric)

| Parameter | Unit metric system | Unit imperial system | openweathermap name |
|---|---|---|---|
| Temperature | �C | �F | temp |
| Dew Point | �C | �F | dew_point |
| Feels like | �C | �F | feels_like |
| Clouds | % | % | clouds |
| Humidity | % | % | humidity |
| Pressure | hPa | hPa | pressure |
| Wind Direction | � | � | wind_deg |
| Wind Speed | m/s | mi/h | wind_speed |
| Wind Gust | m/s | mi/h | wind_gust |
| Rain | mm | mm | rain |
| Visibility | m | m | visibility |
| UV Index | DN | DN | uvi |

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

### (CNE index 2394) Open Weather values for station 21205580 - VENADO ORO VIVERO [21205580]

JSON data from API OWM:

```
{'lat': 4.5984, 'lon': -74.0616, 'timezone': 'America/Bogota', 'timezone_offset': -18000, 'current': {'dt': 1643467037, 'sunrise': 1643454704, 'sunset': 1643497610, 'temp': 12.49, 'feels_like': 11.54, 'pressure': 1028, 'humidity': 67, 'dew_point': 6.54, 'uvi': 9.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 220, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, 'hourly': [{'dt': 1643414400, 'temp': 12.49, 'feels_like': 11.81, 'pressure': 1025, 'humidity': 77, 'dew_point': 8.57, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.71}}, {'dt': 1643418000, 'temp': 12.49, 'feels_like': 11.94, 'pressure': 1025, 'humidity': 82, 'dew_point': 9.5, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 310, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.42}}, {'dt': 1643421600, 'temp': 11.49, 'feels_like': 10.55, 'pressure': 1026, 'humidity': 71, 'dew_point': 6.42, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 300, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.11}}, {'dt': 1643425200, 'temp': 10.49, 'feels_like': 9.58, 'pressure': 1027, 'humidity': 76, 'dew_point': 6.44, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.31}}, {'dt': 1643428800, 'temp': 9.49, 'feels_like': 8.17, 'pressure': 1027, 'humidity': 87, 'dew_point': 7.44, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 310, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643432400, 'temp': 9.49, 'feels_like': 8.17, 'pressure': 1026, 'humidity': 87, 'dew_point': 7.44, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 2.57, 'wind_deg': 320, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'rain': {'1h': 0.24}}, {'dt': 1643436000, 'temp': 8.49, 'feels_like': 6.64, 'pressure': 1026, 'humidity': 87, 'dew_point': 6.45, 'uvi': 0, 'clouds': 20, 'visibility': 10000, 'wind_speed': 3.09, 'wind_deg': 340, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}, {'dt': 1643439600, 'temp': 8.49, 'feels_like': 7.88, 'pressure': 1026, 'humidity': 87, 'dew_point': 6.45, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 320, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643443200, 'temp': 6.49, 'feels_like': 6.49, 'pressure': 1025, 'humidity': 93, 'dew_point': 5.44, 'uvi': 0, 'clouds': 33, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643446800, 'temp': 5.49, 'feels_like': 5.49, 'pressure': 1025, 'humidity': 93, 'dew_point': 4.45, 'uvi': 0, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}]}, {'dt': 1643450400, 'temp': 4.49, 'feels_like': 4.49, 'pressure': 1026, 'humidity': 100, 'dew_point': 4.49, 'uvi': 0, 'clouds': 25, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643454000, 'temp': 3.49, 'feels_like': 3.49, 'pressure': 1026, 'humidity': 100, 'dew_point': 3.49, 'uvi': 0, 'clouds': 23, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50n'}]}, {'dt': 1643457600, 'temp': 4.49, 'feels_like': 3.31, 'pressure': 1027, 'humidity': 100, 'dew_point': 4.49, 'uvi': 0.54, 'clouds': 40, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 310, 'weather': [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]}, {'dt': 1643461200, 'temp': 8.49, 'feels_like': 8.49, 'pressure': 1028, 'humidity': 93, 'dew_point': 7.42, 'uvi': 2.31, 'clouds': 10, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 0, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, {'dt': 1643464800, 'temp': 12.49, 'feels_like': 11.54, 'pressure': 1028, 'humidity': 67, 'dew_point': 6.54, 'uvi': 5.48, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.03, 'wind_deg': 220, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643468400, 'temp': 15.49, 'feels_like': 14.43, 'pressure': 1028, 'humidity': 51, 'dew_point': 5.41, 'uvi': 9.24, 'clouds': 75, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 230, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643472000, 'temp': 16.49, 'feels_like': 15.45, 'pressure': 1027, 'humidity': 48, 'dew_point': 5.46, 'uvi': 12.35, 'clouds': 75, 'visibility': 10000, 'wind_speed': 3.6, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643475600, 'temp': 18.49, 'feels_like': 17.44, 'pressure': 1026, 'humidity': 40, 'dew_point': 4.65, 'uvi': 13.45, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643479200, 'temp': 17.49, 'feels_like': 16.39, 'pressure': 1025, 'humidity': 42, 'dew_point': 4.45, 'uvi': 12.2, 'clouds': 75, 'visibility': 10000, 'wind_speed': 5.66, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643482800, 'temp': 18.49, 'feels_like': 17.49, 'pressure': 1024, 'humidity': 42, 'dew_point': 5.35, 'uvi': 9.16, 'clouds': 75, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643486400, 'temp': 17.49, 'feels_like': 16.65, 'pressure': 1023, 'humidity': 52, 'dew_point': 7.54, 'uvi': 5.33, 'clouds': 75, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643490000, 'temp': 17.49, 'feels_like': 16.65, 'pressure': 1023, 'humidity': 52, 'dew_point': 7.54, 'uvi': 2.17, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 310, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]}, {'dt': 1643493600, 'temp': 16.49, 'feels_like': 15.63, 'pressure': 1023, 'humidity': 55, 'dew_point': 7.43, 'uvi': 0.46, 'clouds': 40, 'visibility': 10000, 'wind_speed': 7.2, 'wind_deg': 300, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]}, {'dt': 1643497200, 'temp': 14.49, 'feels_like': 13.64, 'pressure': 1024, 'humidity': 63, 'dew_point': 7.54, 'uvi': 0, 'clouds': 75, 'visibility': 10000, 'wind_speed': 6.69, 'wind_deg': 290, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'rain': {'1h': 0.18}}]}

```

| Weather | Station | Statname | Latitude | Longitude | Elevation | Category | Technology | Status | InstDate | SuspDate | State | County | Stream | Operator | AHName | SZName | SZHName | Timezone | Datetime | Clouds | Dewpoint | Feelslike | Humidity | Pressure | Rain | Temp | UVI | Visibility | Winddeg | Windgust | Windspeed | OWMid | OWMmain | OWMdesc | OWMicon | Hour |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 00:00:00 | 75.000000 | 8.570000 | 11.810000 | 77.000000 | 1025.000000 | 0.71 | 12.490000 | 0.000000 | 10000.000000 | 300.000000 |  | 4.120000 | 500 | Rain | light rain | 10n | 00 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 01:00:00 | 75.000000 | 9.500000 | 11.940000 | 82.000000 | 1025.000000 | 0.42 | 12.490000 | 0.000000 | 10000.000000 | 310.000000 |  | 3.090000 | 500 | Rain | light rain | 10n | 01 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 02:00:00 | 40.000000 | 6.420000 | 10.550000 | 71.000000 | 1026.000000 | 0.11 | 11.490000 | 0.000000 | 10000.000000 | 300.000000 |  | 3.600000 | 500 | Rain | light rain | 10n | 02 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 03:00:00 | 40.000000 | 6.440000 | 9.580000 | 76.000000 | 1027.000000 | 0.31 | 10.490000 | 0.000000 | 10000.000000 | 320.000000 |  | 3.090000 | 500 | Rain | light rain | 10n | 03 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 04:00:00 | 20.000000 | 7.440000 | 8.170000 | 87.000000 | 1027.000000 |  | 9.490000 | 0.000000 | 10000.000000 | 310.000000 |  | 2.570000 | 801 | Clouds | few clouds | 02n | 04 |
| ![10n.png](http://openweathermap.org/img/w/10n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 05:00:00 | 20.000000 | 7.440000 | 8.170000 | 87.000000 | 1026.000000 | 0.24 | 9.490000 | 0.000000 | 10000.000000 | 320.000000 |  | 2.570000 | 500 | Rain | light rain | 10n | 05 |
| ![02n.png](http://openweathermap.org/img/w/02n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 06:00:00 | 20.000000 | 6.450000 | 6.640000 | 87.000000 | 1026.000000 |  | 8.490000 | 0.000000 | 10000.000000 | 340.000000 |  | 3.090000 | 801 | Clouds | few clouds | 02n | 06 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 07:00:00 | 40.000000 | 6.450000 | 7.880000 | 87.000000 | 1026.000000 |  | 8.490000 | 0.000000 | 10000.000000 | 320.000000 |  | 1.540000 | 802 | Clouds | scattered clouds | 03n | 07 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 08:00:00 | 33.000000 | 5.440000 | 6.490000 | 93.000000 | 1025.000000 |  | 6.490000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 08 |
| ![03n.png](http://openweathermap.org/img/w/03n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 09:00:00 | 40.000000 | 4.450000 | 5.490000 | 93.000000 | 1025.000000 |  | 5.490000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 802 | Clouds | scattered clouds | 03n | 09 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 10:00:00 | 25.000000 | 4.490000 | 4.490000 | 100.000000 | 1026.000000 |  | 4.490000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 10 |
| ![50n.png](http://openweathermap.org/img/w/50n.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 11:00:00 | 23.000000 | 3.490000 | 3.490000 | 100.000000 | 1026.000000 |  | 3.490000 | 0.000000 | 10000.000000 | 0.000000 |  | 1.030000 | 741 | Fog | fog | 50n | 11 |
| ![50d.png](http://openweathermap.org/img/w/50d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 12:00:00 | 40.000000 | 4.490000 | 3.310000 | 100.000000 | 1027.000000 |  | 4.490000 | 0.540000 | 10000.000000 | 310.000000 |  | 1.540000 | 741 | Fog | fog | 50d | 12 |
| ![01d.png](http://openweathermap.org/img/w/01d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 13:00:00 | 10.000000 | 7.420000 | 8.490000 | 93.000000 | 1028.000000 |  | 8.490000 | 2.310000 | 10000.000000 | 0.000000 |  | 1.030000 | 800 | Clear | clear sky | 01d | 13 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 14:00:00 | 75.000000 | 6.540000 | 11.540000 | 67.000000 | 1028.000000 |  | 12.490000 | 5.480000 | 10000.000000 | 220.000000 |  | 1.030000 | 803 | Clouds | broken clouds | 04d | 14 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 15:00:00 | 75.000000 | 5.410000 | 14.430000 | 51.000000 | 1028.000000 |  | 15.490000 | 9.240000 | 10000.000000 | 230.000000 |  | 1.540000 | 803 | Clouds | broken clouds | 04d | 15 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 16:00:00 | 75.000000 | 5.460000 | 15.450000 | 48.000000 | 1027.000000 |  | 16.490000 | 12.350000 | 10000.000000 | 310.000000 |  | 3.600000 | 803 | Clouds | broken clouds | 04d | 16 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 17:00:00 | 75.000000 | 4.650000 | 17.440000 | 40.000000 | 1026.000000 |  | 18.490000 | 13.450000 | 10000.000000 | 310.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 17 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 18:00:00 | 75.000000 | 4.450000 | 16.390000 | 42.000000 | 1025.000000 |  | 17.490000 | 12.200000 | 10000.000000 | 310.000000 |  | 5.660000 | 803 | Clouds | broken clouds | 04d | 18 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 19:00:00 | 75.000000 | 5.350000 | 17.490000 | 42.000000 | 1024.000000 |  | 18.490000 | 9.160000 | 10000.000000 | 310.000000 |  | 7.200000 | 803 | Clouds | broken clouds | 04d | 19 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 20:00:00 | 75.000000 | 7.540000 | 16.650000 | 52.000000 | 1023.000000 |  | 17.490000 | 5.330000 | 10000.000000 | 310.000000 |  | 7.200000 | 803 | Clouds | broken clouds | 04d | 20 |
| ![04d.png](http://openweathermap.org/img/w/04d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 21:00:00 | 75.000000 | 7.540000 | 16.650000 | 52.000000 | 1023.000000 |  | 17.490000 | 2.170000 | 10000.000000 | 310.000000 |  | 6.690000 | 803 | Clouds | broken clouds | 04d | 21 |
| ![03d.png](http://openweathermap.org/img/w/03d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 22:00:00 | 40.000000 | 7.430000 | 15.630000 | 55.000000 | 1023.000000 |  | 16.490000 | 0.460000 | 10000.000000 | 300.000000 |  | 7.200000 | 802 | Clouds | scattered clouds | 03d | 22 |
| ![10d.png](http://openweathermap.org/img/w/10d.png) | 21205580 | "VENADO ORO VIVERO [21205580]" | 4.598361 | -74.061556 | 2725.000000 | Clim�tica Ordinaria | Convencional | Activa | 1965-08-15 00:00:00 | NaT | Bogot� | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andr�s | Magdalena Cauca | Alto Magdalena | R�o Bogot� | America/Bogota | 2022-01-29 23:00:00 | 75.000000 | 7.540000 | 13.640000 | 63.000000 | 1024.000000 | 0.18 | 14.490000 | 0.000000 | 10000.000000 | 290.000000 |  | 6.690000 | 500 | Rain | light rain | 10d | 23 |


### Weather plots

![CNE_IDEAM_Station21205580_OWM_Clouds_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Clouds_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Dewpoint_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Dewpoint_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Feelslike_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Feelslike_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Humidity_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Humidity_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Pressure_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Pressure_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Rain_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Rain_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Temp_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Temp_20220130.png)
![CNE_IDEAM_Station21205580_OWM_UVI_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_UVI_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Visibility_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Visibility_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Winddeg_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Winddeg_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Windgust_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Windgust_20220130.png)
![CNE_IDEAM_Station21205580_OWM_Windspeed_20220130.png](https://github.com/rcfdtools/R.GISPython/blob/main/OpenWeather/Graph/CNE_IDEAM_Station21205580_OWM_Windspeed_20220130.png)