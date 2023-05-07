# -*- coding: UTF-8 -*-

import os
import pandas as pd
import geopandas
from exif import Image

def decimal_coords(coords, ref):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 if ref == 'S' or ref == 'W':
     decimal_degrees = -decimal_degrees
 return decimal_degrees

def image_coordinates(image_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref),
                      img.gps_altitude)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
    print(f"Was taken: {img.datetime_original}, and has coordinates:{coords}")

# Variables
path = 'D:/R.GISPython/GISMobile/.poi/'
poi_file = 'poi.csv'
poi_cols = ['POI', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Name', 'Credit']
exclude_folder = ['.shp', '.temp']
directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

# Processing directories
if os.path.isfile(path+poi_file):
    os.remove(path+poi_file)
df = pd.DataFrame()
print('Directories:', directories)
for i in directories:
    if i not in exclude_folder:
        poi_path = path+i+'/'+poi_file
        print('Processing: %s' %poi_path)
        df1 = pd.read_csv(poi_path)  # Esri shapefile does not support datetime fields with parse_dates=['Date']
        df1['POI'] = i
        df = pd.concat([df, df1], ignore_index=True)
df = df[poi_cols]  # Reordering cols
print(df)
df.to_csv(path+poi_file, encoding='utf-8', index=False)

gdf = geopandas.GeoDataFrame(df)
gdf.set_geometry(
    geopandas.points_from_xy(gdf['Longitude'], gdf['Latitude']),
    inplace=True, crs='EPSG:4326')
gdf.drop(['Latitude', 'Longitude'], axis=1, inplace=True)  # optional
gdf.to_file('.shp/poi.shp')

# Picture properties sample
img_path = '7/PXL_20230503_190031280.jpg'
image_coordinates(img_path)

# https://medium.com/spatial-data-science/how-to-extract-gps-coordinates-from-images-in-python-e66e542af354
# https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
# https://www.geeksforgeeks.org/python-list-files-in-a-directory/
# https://gis.stackexchange.com/questions/147156/making-shapefile-from-pandas-dataframe