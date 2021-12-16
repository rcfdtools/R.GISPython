# R.GISPython

import pandas as pd
import numpy as np

# Simple array evaluation with numpy
data = np.array([[1,'Alto'],[2,'Medio'],[3,'Bajo']])
print(pd.DataFrame(data,columns=['A','B']))

# Simple array evaluation without numpy
data1 = [[1,'Alto'],[2,'Medio'],[3,'Bajo']]
for i in data1[:]:
    print(i[0])


# Date time basics
from datetime import date
currentDate = date.today()
print(str(currentDate.year)+str(currentDate.month)+str(currentDate.day))

# Basic jenks eval
jenksVal = (2380.173697,9038.960497,20170.29529,65187.50527)
def JenksEval(value, iAux=1):
    for i in jenksVal:
        if value <= i:
            return iAux
        iAux+=1
print('Valor en rango: '+str(JenksEval(175.4)))