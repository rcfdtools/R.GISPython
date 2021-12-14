




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

* [Python program to print current year, month and day](https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/)
* [Data Analysis with Python for Excel Users - Full Course](https://www.youtube.com/watch?v=WcDaZ67TVRo&t=84s)
* [How to extract year from date in pandas](https://www.codegrepper.com/code-examples/python/how+to+extract+year+from+date+in+pandas)
* [How to display all rows from data frame using pandas](https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha)
* [How to rotate x-axis tick labels in Pandas barplot](https://stackoverflow.com/questions/32244019/how-to-rotate-x-axis-tick-labels-in-pandas-barplot)
* [Pandas dataframe plot bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)