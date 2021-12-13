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

