import pandas as pd
import numpy as np

wmt_df=pd.read_csv('wmt.csv')
print(wmt_df.head())
#print(wmt_df.info())
wmt_df.set_index('Line Item',inplace=True)
print(f"after changing the index wmt_df: {wmt_df.head()}")
wmt_df=wmt_df.T
print(f"after T wmt_df: {wmt_df.head()} and index:{wmt_df.index}")
#to change the object index to period index
wmt_df.index=pd.PeriodIndex(wmt_df.index,freq='Q-JAN')
print(f"after changing the index wmt_df:\n {wmt_df.head()} and index:{wmt_df.index}")
#create a column for start dates for each quarter
wmt_df["start_date"]= wmt_df.index.map(lambda time_period: time_period.start_time)
wmt_df["end_date"]= wmt_df.index.map(lambda time_period: time_period.end_time)
print(wmt_df.head())