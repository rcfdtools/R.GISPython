es: Análisis de la distribución espacial de la red de estaciones hidroclimatológicas de Colombia y su importancia en los estudios hidrológicos
en: Spatial distribution analysis from the National Colombia stations catalog and their relevance in hydrologic studies

----------------------------------
Preliminary
----------------------------------
1. Get the IDEAM CNE stations and other stations catalogs
	http://dhime.ideam.gov.co/atencionciudadano/
	http://www.ideam.gov.co/solicitud-de-informacion
	http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls
	http://bart.ideam.gov.co/cneideam/CNE_OE.xls
2. Delete not updated or not required attributes: OBJECTID, AREA_HIDROGRAFICA, ZONA_HIDROGRAFICA, SUBZONA_HIDROGRAFICA.....
3. Concat catalogs
4. Update locations with an external manual locations table. Many current CNE locations are not accurate. updated_locations.csv
5. Create station categories dictionary with abbreviations (category_dict.csv) and join with stations catalog
6. Convert joined catalog into a shapefile. Longer attributes names has to be reduced to 10 characters
7. Create categories parametes dictionary (category_parameter_dict.csv). Required for the main study analysis

----------------------------------
Colombia hydrographic subzones
----------------------------------
1. Get the Colombia hydrographic subzones. Zonificacion_hidrografica_2013.shp
	http://bart.ideam.gov.co/cneideam/Capasgeo/Zonificacion_Hidrografica_2013.zip
	http://geoservicios.ideam.gov.co/geonetwork?uuid=e3737d23-dceb-41e1-8680-2816fc1b0fc2
	http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=1a8712e4-8d39-4db3-8821-6c7a0ada7c2a
	Manually download
2. Dissolve subzones to zones and hydrographic areas. Calculate areas in international units system (attribute: Akm2). Manually once time using ArcGIS Pro and the CRS 3857 WGS_1984_Web_Mercator_Auxiliary_Sphere
3. Spatial intersection between stations catalog and hydrographic subzones as points. New attributes: COD_AH, COD_ZH, COD_SZH, NOM_AH, NOM_ZH, NOM_SZH, Akm2

----------------------------------
Research analysis
----------------------------------
