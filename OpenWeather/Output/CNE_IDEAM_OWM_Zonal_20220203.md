
## Weather values for the IDEAM National Station Catalog - CNE from OWM https://openweathermap.org - Zonal Analysis

Study case: Weather evaluation from historical openweathermap data for the CNE IDEAM network stations in Bogotá - Colombia - Suramérica

* File: CNE_IDEAM_OWM_20220203.csv
* Type: <class 'pandas.core.frame.DataFrame'>
* Shape: (1608, 36)


### Station list for the study case

The below table, show the station list used for the zonal analysis for the current study case.

| Station | Latitude° | Longitude°| Category | Technology | Status | State | County | Stream | Operator | AHName | SZName | SZHName |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 21206920 | 4.350000 | -74.150000 | Climática Principal | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | Guatiquia | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206940 | 4.576861 | -74.176778 | Climática Principal | Automática con Telemetría | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206960 | 4.600000 | -74.066667 | Climática Principal | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205012 | 4.638083 | -74.089083 | Climática Principal | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 2120500127 | 4.621667 | -74.103333 | Radio Sonda | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206570 | 4.705583 | -74.150667 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206600 | 4.782222 | -74.094333 | Climática Ordinaria | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205710 | 4.669333 | -74.102667 | Climática Ordinaria | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206560 | 4.661111 | -74.134778 | Climática Ordinaria | Convencional | Activa | Bogotá | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206230 | 4.661667 | -74.151419 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada La Baja | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205529 | 4.667542 | -74.060447 | Meteorológica Especial | Automática sin Telemetría | Activa | Bogotá | Bogota, D.C | Murca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21202280 | 4.684000 | -74.129000 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206190 | 4.666667 | -74.066667 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206000 | 4.680750 | -74.123639 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | San Juan | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206540 | 4.686944 | -74.054222 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206700 | 4.691028 | -74.134417 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Sumapaz | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201230 | 4.701125 | -74.070306 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | Cravo Sur | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205730 | 4.698167 | -74.036833 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Cravo Sur | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21202100 | 4.700000 | -74.166667 | Pluviográfica | Convencional | Suspendida | Bogotá | Bogota, D.C | Cravo Sur | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205520 | 4.700000 | -74.150000 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Cravo Sur | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206150 | 4.700000 | -74.050000 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Cravo Sur | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206130 | 4.705583 | -74.150667 | Radio Sonda | Automática sin Telemetría | Activa | Bogotá | Bogota, D.C | Batatas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205791 | 4.705583 | -74.150667 | Sinóptica Principal | Automática con Telemetría | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21190270 | 4.031028 | -74.311167 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | Cucuana | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Sumapaz |
| 21206680 | 4.734111 | -74.037028 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Meta | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206630 | 4.751139 | -74.091583 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206500 | 4.756639 | -74.061583 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Ocoa | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201300 | 4.394250 | -74.132000 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 35027150 | 4.137972 | -74.173806 | Limnigráfica | Convencional | Activa | Bogotá | Bogota, D.C | Chochal | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba |
| 21206050 | 4.783333 | -74.050000 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201570 | 4.783333 | -74.050000 | Pluviométrica | Convencional | Suspendida | Bogotá | Bogota, D.C | Tuamo | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206670 | 4.792056 | -74.049583 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205013 | 4.794444 | -74.030556 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Guavio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206260 | 4.798639 | -74.049722 | Climática Ordinaria | Convencional | Activa | Bogotá | Bogota, D.C | Recio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 35020310 | 4.172250 | -74.146000 | Pluviográfica | Convencional | Activa | Bogotá | Bogota, D.C | Ceibas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba |
| 35025070 | 4.196667 | -74.190944 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba |
| 35020350 | 4.218889 | -74.146861 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | Blanco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Orinoco | Meta | Río Guayuriba |
| 21206690 | 4.813167 | -74.031111 | Climática Ordinaria | Convencional | Activa | Bogotá | Bogota, D.C | Recio | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201240 | 4.481306 | -74.126278 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | Bogota | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206170 | 4.600000 | -74.200000 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205830 | 4.600000 | -74.133333 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206510 | 4.600000 | -74.083333 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201580 | 4.446500 | -74.154833 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201600 | 4.607111 | -74.072889 | Pluviográfica | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205528 | 4.629583 | -74.090197 | Meteorológica Especial | Automática sin Telemetría | Activa | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205810 | 4.600000 | -74.083333 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206240 | 4.600000 | -74.066667 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205820 | 4.616667 | -74.100000 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205600 | 4.616667 | -74.066667 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205230 | 4.633333 | -74.100000 | Climática Principal | Convencional | Suspendida | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206620 | 4.634611 | -74.173750 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205860 | 4.650000 | -74.200000 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Seco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205800 | 4.650000 | -74.066667 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Seco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206660 | 4.576222 | -74.130917 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206610 | 4.583333 | -74.066667 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206640 | 4.501556 | -74.119306 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | Guaviare | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205840 | 4.595361 | -74.111833 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206970 | 4.595000 | -74.070361 | Climática Ordinaria | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205580 | 4.598361 | -74.061556 | Climática Ordinaria | Convencional | Activa | Bogotá | Bogota, D.C | Cauca | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21201200 | 4.342944 | -74.183889 | Pluviométrica | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206650 | 4.516753 | -74.088222 | Climática Ordinaria | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21205760 | 4.600000 | -74.083333 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Quebrada Perlas | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 21206040 | 4.646778 | -74.096361 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | Seco | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 2120000159 | 4.696447 | -74.158914 | Pluviométrica | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 2120500157 | 4.621664 | -74.103436 | Meteorológica Especial | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 2120500172 | 4.696447 | -74.158914 | Meteorológica Especial | Convencional | Suspendida | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
| 2120500173 | 4.621664 | -74.103436 | Meteorológica Especial | Convencional | Activa | Bogotá | Bogota, D.C | 0 | Area Operativa 11 - Cundinamarca-Amazonas-San Andrés | Magdalena Cauca | Alto Magdalena | Río Bogotá |
