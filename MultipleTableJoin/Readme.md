# Join multiple separated tables into a unique unpivot table


## [CAMELS-BR](https://zenodo.org/record/3964745)

Reference: Vinícius B. P. Chagas, Pedro L. B. Chaffe, Nans Addor, Fernando M. Fan, Ayan S. Fleischmann, Rodrigo C. D. Paiva, & Vinícius A. Siqueira. (2020). CAMELS-BR: Hydrometeorological time series and landscape attributes for 897 catchments in Brazil - link to files. (1.1) [Data set]. Zenodo.

Script: [MultipleTableJoin_CAMELS_BR.py](MultipleTableJoin_CAMELS_BR.py)


### Specifications

* `input_path` & `temp_path`: user can define the input and the temporal processing folder.
* `stations_file`: [Stations.csv](Stations.csv) contains a list of the stations to be joined. The parameter `process_all = False` has to be established in False, otherwise, all the files founded in the Input folder will be joined. 
* `camels_br_type`: user have to specify the kind of file to process, e.g.: _streamflow_m3s, _streamflow_mm, _simulated_streamflow, _precipitation_chirps, _precipitation_mswep, _precipitation_cpc, _evapotransp_gleam, _evapotransp_mgb, _potential_evapotransp_gleam, _temperature_min, _temperature_mean, _temperature_max.
* `process_all`: all the files contained in the Input folder will be joined if this parameter is `True`, with `False` only the stations includes in Stations.csv will be joined.   

> For this example, Stations.csv contains all the Amazonas basin stations.


## ANA Brasil


## References

* https://stackoverflow.com/questions/19350806/how-to-convert-columns-into-one-datetime-column-in-pandas
* https://essd.copernicus.org/articles/12/2075/2020/
* https://www.ufrgs.br/samewater/2020/12/02/camels-br/
* https://zenodo.org/record/3964745

