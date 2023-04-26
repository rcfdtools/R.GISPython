# -*- coding: UTF-8 -*-

import glob
import vaex
import matplotlib.pylab as plt

input_path = 'I:/IDEAM_CO/csv_files/'
out_path = 'I:/IDEAM_CO/hdf5_files/'
hdf5_convert = False

if hdf5_convert:
    csv_files = glob.glob(input_path+'*.csv')
    for i, csv_file in enumerate(csv_files, 1):
        for j, df in enumerate(vaex.from_csv(csv_file, chunk_size=5_000_000), 1):
            print('Exporting %d %s to hdf5 part %d' % (i, csv_file, j))
            df.export_hdf5(f'I:/IDEAM_CO/hdf5_files/ideam_{i:02}_{j:02}.hdf5')

df = vaex.open(out_path+'*.hdf5')
print(df.head())
print(df.tail())
quantile = df.percentile_approx('ValorObservado', 25)
print(quantile)
#df = df[df.CodigoEstacion == 21185080]
print(df.head(100))
group_res = df.groupby(by=df.CodigoEstacion, agg={'ValorObservado_mean': vaex.agg.mean('ValorObservado')})
print(group_res)

df = df[df.CodigoEstacion == 21185080]
#plot = df.viz.histogram(df.ValorObservado, what='count(*)', limits=[0, 100])
plt.plot(df.ValorObservado)
#plt.plot(df.FechaObservacion, df.ValorObservado)
plt.show()

counts_stations = df.count(binby=df.ValorObservado, limits=[-1000, 1000], shape=64)
print(counts_stations)




# https://www.kdnuggets.com/2021/03/pandas-big-data-better-options.html
# https://vaex.readthedocs.io/en/docs/tutorial.html
# https://towardsdatascience.com/process-dataset-with-200-million-rows-using-vaex-ad4839710d3b