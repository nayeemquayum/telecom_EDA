#import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "ice_cream_data.csv"

#read the file
try:
    df_ice_cream = pd.read_csv(file_name)
except BaseException as e:
    print('Error! The exception: {}'.format(e))
else:
    print ("Data loaded successfully")
    #print(f"{file_name} read successfully")
#finally: block not needed since pd.read_csv closes the file automatically


#rename the headers
df_ice_cream.rename(columns={'Base Flavor' : 'Base_Flavor',
                     'Flavor Rating' : 'Flavor_Rating',
                     'Texture Rating': 'Texture_Rating',
                     'Total Rating' : 'Total_Rating'}, inplace=True)
#print(f"columns after renaming:{df_ice_cream.columns}")
print (df_ice_cream.info())
grouped_df=df_ice_cream.groupby('Base_Flavor')\
                .agg({'Flavor_Rating' : ['mean','max','count'],
                      'Texture_Rating' : ['mean','max','count']})
print (f"{grouped_df}")