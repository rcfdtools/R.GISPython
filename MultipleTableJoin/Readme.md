## Join multiple separated tables into a unique unpivot table

Isolated time-serie file parameters, has to be joined in a unique table if you want to use dynamic ArcGIS map views, related with gauge stations or basin polygons.  

### CAMELS-BR

Reference: Vinícius B. P. Chagas, Pedro L. B. Chaffe, Nans Addor, Fernando M. Fan, Ayan S. Fleischmann, Rodrigo C. D. Paiva, & Vinícius A. Siqueira. (2020). CAMELS-BR: Hydrometeorological time series and landscape attributes for 897 catchments in Brazil - link to files. (1.1) [Data set]. Zenodo. https://zenodo.org/record/3964745

* Script [MultipleTableJoin_CAMELS_BR.py](MultipleTableJoin_CAMELS_BR.py)  
* [Local CAMELS-BR dataset.](CAMELS_BR/Source)  
* [Local joined files Amazon Basin.](CAMELS_BR/Joined)

```
# -*- coding: UTF-8 -*-
# Name: MultipleTableJoin_CAMELS_BR.py
# Description: this script join multiple separated tables into a unique unpivot table.
# Repository: https://github.com/rcfdtools/R.GISPython/tree/main/MultipleTableJoin
# License: https://github.com/rcfdtools/R.GISPython/wiki/License
# Requirements: Python 3+, Pandas,

# Libraries
import glob
import os
import pandas as pd
import shutil

# Functions
def processing_file(file):
    print('Processing %s' % file[len_input_path:9999])
    df = pd.read_csv(file, sep=column_separator)
    df[station_id] = file[len_input_path:len_input_path + gauge_id_digits]
    df['date'] = pd.to_datetime(df[[year_column, month_column, day_column]])
    df.to_csv(temp_path + file[len_input_path:9999], encoding='utf-8', index=False)

# General parameters
input_path = 'Input/'  # Your local input file folder
temp_path = 'Temp/'  # Your local output temporal folder
stations_file = 'Stations.csv'  # File with the stations list to process. If the list contains repeated values, transformed files is posted only one time in the temporal output folder.
camels_br_type = '_streamflow_m3s'  # _streamflow_m3s, _streamflow_mm, _simulated_streamflow, _precipitation_chirps, _precipitation_mswep, _precipitation_cpc, _evapotransp_gleam, _evapotransp_mgb, _potential_evapotransp_gleam, _temperature_min, _temperature_mean, _temperature_max
format_file = '.txt'  # CAMELS-BR use .txt files
joined_file = 'camels_br' + camels_br_type + '.csv'  # Joined file name to import in ArcGIS
column_separator = ' '  # Separator used in the CAMELS-BR files
year_column = 'year'
month_column = 'month'
day_column = 'day'
station_id = 'gauge_id'
gauge_id_digits = 8  # For CAMELS-BR, the gauge ID is the first eight digits of the file name
process_all = False  # Process all the stations. True ignore the file Stations.csv. False process only the list included in Stations.csv

# Procedure
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
len_input_path = len(input_path)
if os.path.isfile(joined_file):
    os.remove(joined_file)
print('Processing all files contained in the %s folder: %s' % (input_path, process_all))
founded = 0
if not process_all:
    df_stations = pd.read_csv(stations_file, sep=column_separator)  # Station list to process
    n_stations = len(df_stations)
    print('Stations list: %s\nStations to process: %d\n\nStarting...' % (stations_file, n_stations))
    for j in range(len(df_stations)):
        station_file = input_path + str(df_stations[station_id][j]) + camels_br_type + format_file
        if os.path.isfile(station_file):
            processing_file(station_file)
            founded += 1
        else:
            print('Processing %s - file not available' % station_file[len_input_path:9999])
    print('%d stations founded of %d required (%f%%)' %(founded, n_stations, (founded/n_stations)*100))
else:
    table_files = glob.glob(input_path + '*' + format_file)
    print('Files founded: %d\n\nStarting...' % len(table_files))
    for i in table_files:
        processing_file(i)
print('Process acomplished...')
table_files = glob.glob(temp_path + '*' + format_file)
df = pd.concat(map(pd.read_csv, table_files), ignore_index=True)
df.to_csv(joined_file, encoding='utf-8', index=False)
shutil.rmtree(temp_path)
os.mkdir(temp_path, 0o666)
print('\nJoined dataframe sample\n', df)
print('\nJoined file: %s\n' % joined_file)
```


#### Specifications

* `input_path` & `temp_path`: user can define the input and the temporal processing folder.
* `stations_file`: [Stations.csv](Stations.csv) contains a list of the stations to be joined. The parameter `process_all = False` has to be established in False, otherwise, all the files founded in the Input folder will be joined. 
* `camels_br_type`: user have to specify the kind of file to process, e.g.: _streamflow_m3s, _streamflow_mm, _simulated_streamflow, _precipitation_chirps, _precipitation_mswep, _precipitation_cpc, _evapotransp_gleam, _evapotransp_mgb, _potential_evapotransp_gleam, _temperature_min, _temperature_mean, _temperature_max.
* `process_all`: all the files contained in the Input folder will be joined if this parameter is `True`, with `False` only the stations includes in Stations.csv will be joined.   

> For this example, Stations.csv contains all the Amazon basin stations.




### ANA Brasil


## References

* https://stackoverflow.com/questions/19350806/how-to-convert-columns-into-one-datetime-column-in-pandas
* https://essd.copernicus.org/articles/12/2075/2020/
* https://www.ufrgs.br/samewater/2020/12/02/camels-br/
* https://zenodo.org/record/3964745
* https://www.skytowner.com/explore/replacing_values_with_nans_in_pandas_dataframe
* https://sparkbyexamples.com/pandas/pandas-replace-by-examples/

