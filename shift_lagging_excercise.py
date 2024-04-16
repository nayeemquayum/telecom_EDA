import pandas as pd
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col='Date')
print(f"original df: {df}")
#the DatetimeIndex is missing the frequencey.
# Let's change the frequency to B
changed_df= df.asfreq(freq='B')
print(changed_df.index)
changed_df.index=changed_df.index.shift(1)
print(f"After shifting index: {changed_df}")
#print (df_index_shifted)
'''
df_shifted_back = df_shifted.shift(-1)
print (df_shifted_back)

tshift_df = df.tshift(1)
print (tshift_df)'''