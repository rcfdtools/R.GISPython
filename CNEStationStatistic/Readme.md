




Data sample with Pandas from https://www.codegrepper.com/
```
df['date'] = pd.to_datetime(df['date'],format='%Y%m%d')
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month

#Exctract month and create a dedicated column df["Month"] from a 
#column in datetime format df["Date"]
df['Month'] = pd.DatetimeIndex(df['Date']).month
```


### Referencias

* [Data Analysis with Python for Excel Users - Full Course](https://www.youtube.com/watch?v=WcDaZ67TVRo&t=84s)
* [Python program to print current year, month and day](https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/)
* [How to extract year from date in pandas](https://www.codegrepper.com/code-examples/python/how+to+extract+year+from+date+in+pandas)
* [How to display all rows from data frame using pandas](https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha)
* [How to rotate x-axis tick labels in Pandas barplot](https://stackoverflow.com/questions/32244019/how-to-rotate-x-axis-tick-labels-in-pandas-barplot)
* [Pandas dataFrame plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot)
* [Pandas dataframe plot bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
* [Pandas DataFrame Plot - Pie Chart](https://kontext.tech/column/code-snippets/402/pandas-dataframe-plot-pie-chart)
* [Make Better Bar Charts in Python using Pandas Plot](https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/)
* [Annotate bars with values on Pandas bar plots](https://stackoverflow.com/questions/25447700/annotate-bars-with-values-on-pandas-bar-plots)
* [Pandas pie plot actual values for multiple graphs](https://stackoverflow.com/questions/48299254/pandas-pie-plot-actual-values-for-multiple-graphs)
* [IDEAM Colombia - Clasificación de los climas (clima-text.pdf)](http://atlas.ideam.gov.co/basefiles/clima-text.pdf)
* [IDEAM Colombia - Clasificación climática de Caldas](http://www.ideam.gov.co/documents/10182/599272/Clasificacion+Climatica+de+Caldas+2014.pdf/d4ffa383-e60b-4ec5-8aa2-1b553d23b44f?version=1.0)
* [Pisos térmicos en Costa Rica](https://www.mep.go.cr/sites/default/files/recursos/recursos-interactivos/clima_tiempo/pdf/pisos_termicos.pdf)