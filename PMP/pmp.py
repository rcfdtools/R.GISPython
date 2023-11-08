# -*- coding: UTF-8 -*-

import math
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import norm

#Prueba de bondad de ajuste usando el método de Kolmogorov-Smirnov usando una función
def fTestKolmogorov(x, F_Dist):
    dFP = pd.DataFrame()
    dFP['dFP'] = abs(x['P_E']-x[F_Dist])
    dFP = dFP.sort_values(by='dFP', ascending=[False])
    dFP = dFP.reset_index(drop=True)
    n = len(dFP)
    if (n < 35):
        deltao = 0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
    else:
        deltao = 1.36/math.sqrt(n)
    delta = dFP['dFP'][0]
    if (deltao > delta):
        fit, operator = 'fit', '>'
    else:
        fit, operator = 'doesn’t fit', '<='
    print('* Kolmogorov-Smirnov test (Δo > Δ): %f %s %f (distribution %s the empirical curve)' % (deltao, operator, dFP['dFP'][0], fit))
    vDeltaKolmogorovData = [station_name, F_Dist, delta]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData


# Función de distribución: Gumbel
# Parameter calculation, Method of Moments
def fDistGumbel(x):
    print('\nGumbel distribution')
    alph = math.sqrt(6) * x[station_name].std(ddof=ddof)/math.pi
    mu = x[station_name].mean() - 0.57721/alph
    print('* α: %f\n* μ: %f' % (alph ,mu))
    x['F_DGumbel'] = np.exp(-np.exp(-(x[station_name] - mu) / alph))
    fTestKolmogorov(x, 'F_DGumbel')

def fDistNormal(x):
    print('\nNormal distribution')
    mu = x[station_name].mean()
    std = x[station_name].std(ddof=ddof)
    print('* μ: %f\n* σ: %f' % (mu, std))
    x['z_score'] = (x[station_name] - mu) / std
    x['F_DNormal'] = norm.cdf(x['z_score'])
    fTestKolmogorov(x, 'F_DNormal')


#Función de distribución: Weibull (empírica)
def fDistEmpWeibull(x):
    x['P_E'] = x['index'] / (len(x[station_name])+1)


# General
input_path = 'station/'  # Your local input file folder
station_file = input_path + '25020230.csv'
station_name = Path(station_file).stem
print('## Station: %s' %station_name)
ddof = 1  # Standard deviation normalized
vDeltaKolmogorov = pd.DataFrame(columns=['Station', 'Dp', 'Delta'])
df = pd.read_csv(station_file, delimiter=',')
df = df.dropna()
df = df.sort_values(by=station_name)
df = df.reset_index(drop=True)
df['index'] = df.index+1
print('\nBasic stats\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[station_name].count(), df[station_name].mean(), ddof, df[station_name].std(ddof=ddof), df[station_name].min(), df[station_name].max()))
fDistEmpWeibull(df)
fDistGumbel(df)
fDistNormal(df)
df = df.drop(columns=['z_score'])
print('\n %s' % df)
print('\nKolmogorov-Smirnov Δ values\n%s' % vDeltaKolmogorov)

#print(df.to_csv(index=False))