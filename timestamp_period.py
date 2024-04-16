import pandas as pd
import numpy as np
#quarterly period
period = pd.period_range(start='2023',periods=10,freq='M')
print (f"period length: {len(period)}")
print(period.to_timestamp())
#create a dataframe with the priod_range index
df=pd.DataFrame(np.random.randn(len(period)),index=period)
#sort the df
df.sort_index(inplace=True)
print(df.loc['2023-1': '2023-03'])