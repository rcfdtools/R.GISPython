# -*- coding: UTF-8 -*-

import math
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import pearson3
from scipy.stats import gumbel_r
from scipy.stats import gumbel_l
from scipy.stats import genextreme
from scipy.stats import alpha
from scipy.stats import beta
from scipy.stats import betaprime
from scipy.stats import bradford
from scipy.stats import burr
from scipy.stats import burr12
from scipy.stats import cauchy
from scipy.stats import chi2
from scipy.stats import crystalball
from scipy.stats import gamma
from scipy.stats import dgamma
from scipy.stats import dweibull
from scipy.stats import expon
from scipy.stats import exponnorm
from scipy.stats import exponweib
from scipy.stats import exponpow
from scipy.stats import f
from scipy.stats import fisk
from scipy.stats import foldcauchy
from scipy.stats import foldnorm
from scipy.stats import genlogistic
from scipy.stats import gennorm
from scipy.stats import genpareto


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def fTestKolmogorov(x, F_Dist):  # Kolmogorov-Smirnov fit test
    dFP = pd.DataFrame()
    dFP['dFP'] = abs(x['weibull']-x[F_Dist])
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
    eval = 'Δo %s Δ, %s' % (operator, fit)
    vDeltaKolmogorovData = [station_name, F_Dist, delta, deltao, eval]
    vDeltaKolmogorov.loc[len(vDeltaKolmogorov)] = vDeltaKolmogorovData

def pdist_weibull(x):  # Función de distribución: Weibull (empírica)
    x['weibull'] = x['OID'] / (len(x[station_name])+1)

def pdist_gumbel(x):  # Función de distribución: Gumbel
    scale = math.sqrt(6) * x[station_name].std(ddof=ddof)/math.pi
    loc = x[station_name].mean() - 0.57721/scale
    print('* Gumbel distribution (gumbel) >> Loc: %f, Scale: %f' % (loc, scale))
    x['gumbel'] = np.exp(-np.exp(-(x[station_name] - loc) / scale))
    fTestKolmogorov(x, 'gumbel')

def pdist_loggumbel(x):  # Función de distribución: Log-Gumbel
    scale = math.sqrt(6)*np.std(np.log(x[station_name]))/math.pi
    loc = np.mean(np.log(x[station_name]))-0.57721*scale
    print('* Log Gumbel distribution (loggumbel) >> Loc: %f, Scale: %f' % (loc, scale))
    x['loggumbel'] = np.exp(-np.exp(-(np.log(x[station_name])-loc)/scale))
    fTestKolmogorov(x, 'loggumbel')

def pdist_scipy(x, p_dist, n_parameter, fit_method, p_dist_tag):
    # x: dataset to eval
    # p_dist: probability distribution function name in SciPy
    # n_parameter: # parameters required
    # fit_method: parameter estimation method. (MLE) Maximum likelihood method or (MM) L-moments
    # p_dist_tag: probability distribution label for reports
    if n_parameter == 2:
        loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Loc: %f, Scale: %f' % (p_dist_tag, p_dist, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], loc, scale)  # Cumulative distribution function
    elif n_parameter == 3:
        shape, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, loc, scale)  # Cumulative distribution function
    elif n_parameter == 4:
        shape, shape1, loc, scale = eval(p_dist).fit(x[station_name], method=fit_method)
        print('* %s (%s) >> Shape: %f, Shape 1: %f, Loc: %f, Scale: %f' % (p_dist_tag, p_dist, shape, shape1, loc, scale))
        x[p_dist] = eval(p_dist).cdf(x[station_name], shape, shape1, loc, scale)  # Cumulative distribution function
    else:
        print('%s\n* Error: check the # shape parameters entered ')
    fTestKolmogorov(x, p_dist)

# General
input_path = 'station/'  # Your local input file folder
station_file = input_path + '25020230.csv'
station_name = Path(station_file).stem
# l_pdist_scipy requires: ([Distribution, parameters, fit method, label, active)]
l_pdist_scipy = ([['gumbel_l', 2, 'MM', 'Gumbel Left Skew', False],
                  ['gumbel_r', 2, 'MM', 'Gumbel Right Skew', False],
                  ['norm', 2, 'MM', 'Normal', True],
                  ['lognorm', 3, 'MLE', 'Log-Normal', False],
                  ['foldnorm', 3, 'MM', 'Fold Normal', False],
                  ['gennorm', 3, 'MLE', 'Generalized Normal', True],
                  ['pearson3', 3, 'MM', 'Pearson III', True],
                  ['genextreme', 3, 'MLE', 'Generalized exponential', False],
                  ['alpha', 3, 'MLE', 'Alpha', True],
                  ['beta', 4, 'MLE', 'Beta', False],
                  ['betaprime', 4, 'MLE', 'Beta prime', False],
                  ['bradford ', 3, 'MLE', 'Bradford', False],
                  ['burr', 4, 'MLE', 'Burr (Type III)', False],
                  ['burr12', 4, 'MLE', 'Burr (Type III) 12', False],
                  ['cauchy', 2, 'MLE', 'Cauchy', False],
                  ['foldcauchy ', 3, 'MLE', 'Fold Cauchy', False],
                  ['chi2', 3, 'MLE', 'Chi²', False],
                  ['crystalball', 4, 'MLE', 'Crystalball', False],
                  ['gamma', 3, 'MLE', 'Gamma', False],
                  ['dgamma', 3, 'MLE', 'Double gamma', False],
                  ['dweibull', 3, 'MLE', 'Double Weibull', False],
                  ['expon', 2, 'MLE', 'Exponential', False],
                  ['exponnorm', 3, 'MLE', 'Exponentially modified Normal', False],
                  ['exponweib', 4, 'MLE', 'Exponentiated Weibull', False],
                  ['exponpow', 3, 'MLE', 'Exponential power', False],
                  ['f', 4, 'MLE', 'F', True],
                  ['fisk', 3, 'MLE', 'Fisk', True],
                  ['genlogistic', 3, 'MLE', 'Generalized logistic', True],
                  ['genpareto', 3, 'MLE', 'Generalized Pareto', True]
                  ])
print('## Station: %s' %station_name)
ddof = 1  # Standard deviation normalized
vDeltaKolmogorov = pd.DataFrame(columns=['Station', 'Dp', 'Delta', 'Deltao', 'Eval'])
DNMR = pd.DataFrame(columns=['DNMR'])
df = pd.read_csv(station_file, delimiter=',')
df = df.dropna()
df = df.sort_values(by=station_name)
df = df.reset_index(drop=True)
df['OID'] = df.index+1
print('\n### Basic stats\n\n* n: %d\n* mean: %f\n* std(%d): %f\n* min: %f\n* max: %f' % (df[station_name].count(), df[station_name].mean(), ddof, df[station_name].std(ddof=ddof), df[station_name].min(), df[station_name].max()))
print('\n### Probability distributions\n')
pdist_weibull(df)
pdist_gumbel(df)
#pdist_loggumbel(df)
for i in l_pdist_scipy:
    #print(i[0])
    if i[4]:
        pdist_scipy(df, i[0], i[1], i[2], i[3])

#df = df.drop(columns=['z_score'])
print('\n### Cumulative distribution values - CDF\n\n %s' % df)
print('\n### Kolmogorov-Smirnov fit test - Δ values\n\n%s' % vDeltaKolmogorov)

#print(df.to_csv(index=False))