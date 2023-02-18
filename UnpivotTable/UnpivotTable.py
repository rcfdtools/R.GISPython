# -*- coding: UTF-8 -*-
# Name: UnpivotTable.py
# Description: unpivot a multiple column table in a series tables
# Requirements: Python 3+, pandas

# Libraries
import pandas as pd

# General variables
pivot_table = 'df_prec_ANA_20230216.csv'  # Current IDEAM records file
date_field = 'Date'
var_name = 'Codigo'
value_name = 'Valor'

# Procedure
df = pd.read_csv(pivot_table, low_memory=False, parse_dates=[date_field], dayfirst=True) # Check your right day position in the date field
print(df.info(), '\n')
print(df.dtypes, '\n')
print(df, '\n')
df_unpivot = pd.melt(df, id_vars=date_field, var_name=var_name, value_name=value_name, ignore_index = True)
print(df_unpivot, '\n')
df_unpivot.index.name = 'Id'
df_unpivot.to_csv('unpivot_'+pivot_table)


# References
# https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e
# https://www.statology.org/pandas-unpivot/
# https://sparkbyexamples.com/pandas/pandas-unpivot-dataframe/