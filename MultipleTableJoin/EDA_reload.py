# -*- coding: UTF-8 -*-

import glob
import vaex
import matplotlib.pylab as plt

input_path = 'I:/IDEAM_CO/csv_files/'
out_path = 'I:/IDEAM_CO/hdf5_files/'
station_code = 'CodigoEstacion'
sensor_code = 'CodigoSensor'
date_name = 'FechaObservacion'
value_name = 'ValorObservado'
station_name = 'NombreEstacion'
state_name = 'Departamento'
countie_name = 'Municipio'
hdg_zone_name = 'ZonaHidrografica'
latitude_name = 'Latitud'
longitude_name = 'Longitud'
parameter_name = 'DescripcionSensor'
unit_name = 'UnidadMedida'
hdf5_convert = True

'''
dtype = {station_code: 'str', sensor_code: 'str', value_name: 'float',
         station_name: 'str', state_name: 'str', countie_name: 'str',
         hdg_zone_name: 'str', latitude_name: 'float', longitude_name: 'float',
         parameter_name: 'str', unit_name: 'str'}
'''

dtype = {station_code: 'str', sensor_code: 'str'}

# Convert to HDF5 format
if hdf5_convert:
    csv_files = glob.glob(input_path+'*.csv')
    for i, csv_file in enumerate(csv_files, 1):
        #for j, df in enumerate(vaex.from_csv(csv_file, chunk_size=5_000_000, dtype=dtype, parse_dates=[date_name], low_memory=False), 1):  # Parse dates increase the processing time to hours
        for j, df in enumerate(vaex.from_csv(csv_file, chunk_size=5_000_000, dtype=dtype, low_memory=False), 1):  # Parse dates increase the processing time to hours
            print('Exporting %d %s to hdf5 part %d' % (i, csv_file, j))
            df.export_hdf5(f'I:/IDEAM_CO/hdf5_files/Precipitacion_{i:02}_{j:02}.hdf5')

# Dataframe
df = vaex.open(out_path+'*.hdf5')
print('Dataframe head\n ', df.head())
print('\nDataframe tail\n ', df.tail())
quantile = df.percentile_approx(value_name, 25)
print('\nFull percentile 25: %s\n' %quantile)
group_res = df.groupby(by=df[station_code], agg={value_name+'_mean': vaex.agg.mean(value_name)})
print('Group by \n ',group_res)
print(df.dtypes)

#counts_stations = df.count(binby=df.ValorObservado, limits=[-1000, 1000], shape=64)
#print(counts_stations)

df = df[df.CodigoEstacion == '2804500076']
df.sort(by=[date_name], ascending=[True])
print(df)
#df.sort(by=[station_code, date_name], ascending=[True, True])
#df.sort_values(by=date_name)
#plot = df.viz.histogram(df.ValorObservado, what='count(*)', limits=[0, 100])
#plt.plot(df[date_name], df[value_name])
plt.plot(df[value_name])
plt.xticks(rotation = 25)
plt.show()
plt.close('all')





# https://vaex.readthedocs.io/en/docs/tutorial.html
# https://www.kdnuggets.com/2021/03/pandas-big-data-better-options.html
# https://towardsdatascience.com/process-dataset-with-200-million-rows-using-vaex-ad4839710d3b
# https://stackabuse.com/rotate-axis-labels-in-matplotlib/

