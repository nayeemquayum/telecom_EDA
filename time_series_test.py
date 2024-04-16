import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
usb= CustomBusinessDay(calendar=USFederalHolidayCalendar())

generate_dates = pd.date_range(start='1-Jun-17',\
                               end='30-Jun-17',\
                               freq=usb)

file_name="aapl.csv"
#read file as time series
try:
    #df_apple_stock = pd.read_csv('aapl.csv',parse_dates=[0]) #first column with index 0 is parsed as date
    df_apple_stock= pd.read_csv('aapl.csv'\
                                ,parse_dates=['Date']\
                                ,index_col='Date')
except BaseException as e:
    print('Error! The exception: {}'.format(e))
else:
    print(f"{file_name} read successfully")
#finally: block not needed since pd.read_csv closes the file automatically
#to query subset of data using date index we have to sort by date index
df_apple_stock.sort_index(inplace=True)
print (f"index of the dataframe: {df_apple_stock.index}")
#print (f"df_apple_stock:{df_apple_stock.head(10)}")
print (f"get subset data using range of date index {df_apple_stock.loc['11-Jul-16':'13-Jul-16']}")
print(f"mean data for 2017-07:{df_apple_stock.loc['2017-07'].Close.mean()}")
#resampling
#lets say instead of getting daily data, we want montly or weekly data.
#we could do that using resample method
print (f"mothly data: {df_apple_stock.resample("W").Close.mean()} ")
df_apple_stock.resample("Q").Close.mean().plot()
'''range = pd.date_range(start='1-Jun-17',end='30-Jun-17',freq='B')
print(f"range: {range}")
df_apple_stock.set_index(range, inplace=True)
df_apple_stock.asfreq('W', method='pad')
print (f"after adding date the data:{df_apple_stock.head(10)}")

#matlib plot starts
plt.figure(figsize=(8,6))
df_apple_stock.Close.plot()'''
#show the plot
plt.show()