# -*- coding: UTF-8 -*-

import math
import numpy as np
import pandas as pd
from pathlib import Path


#Función de distribución: Gumbel
def fDistGumbel(x):
    print('\n### Distribución de Gumbel (Station: %s)' %station_name)
    #Parameter calculation, Method o f Moments
    vDistID = 2 # Distribution ID
    alph = math.sqrt(6) * np.std(x[station_name])/math.pi
    mu = x[station_name].mean() - 0.57721/alph
    print('\nn: %f\nmean: %f\nalpha: %f\nmu: %f' % (x[station_name].count(), x[station_name].mean(), alph ,mu))
    #F_DGumbel = c()
    #for (i in 1:n) {F_DGumbel[i] <- exp(-exp(-(x[i]-mu)/alph))}
    #for i in x:
    #F_DGumbel[i] = math.exp(-math.exp(-(x[i] - mu) / alph))
    #F_DGumbel = F_DGumbel #Set as global var
    x['F_DGumbel'] = np.exp(-np.exp(-(x[station_name] - mu) / alph))
    print('\n %s' %df)
    #print(data.frame(x, P_E, F_DGumbel))
    vGraphTitle = ("GUMBEL DISTRIBUTION (Id: ",vStationName,")")
    #plot (x, F_DGumbel, type="l", pch=20, col="red", lty=2, xlab="", ylab="Cumulative probability", cex.main=vGrphTitSize, main=vGraphTitle)
    #lines (x, P_E, pch=18, col="blue", type="b", lty=1)
    #grid()
    #legend ("bottomright", legend=c("Gumbel Distribution", "Empirical Distribution"),
    #        lty=1:2, col=c("red", "blue"), cex=0.8 , text.font=3, title= "r.cfdtools@gmail.com")
    #D.GUMBEL>> Cálculo de probabilidades y quantiles - Precipitación para diferentes periodos de retorno
    #XTrDGumbel = mu-log((-log(p, exp(1))), exp(1)) * alph
    #print("\n")
    #print(data.frame(Tr, pt, XTrDGumbel)) #Tabla de resultados
    #vMaxXTr[2] = max(XTrDGumbel)
    #vMinXTr[2] = min(XTrDGumbel)
    #vGraphTitle = ("XTrDGumbel vs Return period (Id: ",vStationName,")")
    #plot(Tr, XTrDGumbel, pch=20, col="#000099", bg="#FF6666", type="b" , lty=1, ylab = "XTrDGumbel", xlab = "Return period (years)", cex.main=vGrphTitSize, main = vGraphTitle)
    #grid()
    #fTestKolmogorov(vDistID,P_E,F_DGumbel)

#Función de distribución: empírica propuesta por Weibull
def fDistEmpWeibull(x):
  '''P_E = c()
  for (i in 1:n) {P_E[i] <- i / (n+1)};
  cat("\n")
  print(data.frame(x, P_E))                     #Mostrar los valores ordenados de x y la distribucion empirica de Weibull
  P_E <<- P_E                                   #Definir P_E como global
  '''
  x['P_E'] = x[station_name] / (x.len()+1)



# General
input_path = 'station/'  # Your local input file folder
station_file = input_path + '25020230.csv'
station_name = Path(station_file).stem
print('Station: %s' %station_name)
df = pd.read_csv(station_file, delimiter=',')
df = df.dropna()
df = df.sort_values(by=station_name)
print(df)
#print(df['year'])
df['F_DGumbel'] = np.nan
fDistEmpWeibull(df)
fDistGumbel(df,station_name)