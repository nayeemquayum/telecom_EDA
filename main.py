#import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
file_name = "coaster_db.csv"
#lets change the number of columns to be displayed in output
pd.set_option('display.max_columns',56)
#read the file
try:
    df_coaster_db= pd.read_csv(file_name)
except BaseException as e:
    print('Error! The exception: {}'.format(e))
else:
    print ("Data loaded successfully")
    #print(f"{file_name} read successfully")
#finally: block not needed since pd.read_csv closes the file automatically

#Display the column headers
print (f"df_coaster_db columns: {df_coaster_db.columns}")
print (f"df_coaster_db shape: {df_coaster_db.shape }")
print ("################info()############################")
print(f"df_coaster_db info:{df_coaster_db.info()}")
#print (f"df_coaster_db head: {df_coaster_db.head(20)}")
#check if any column has duplicated values
print ("################check duplicates#####################")
#find number of duplicates in column coaster_name
print (f"number of duplicates in coaster_name column {df_coaster_db.duplicated(subset=['coaster_name']).sum()}")
#find the second or subsequent occurences of the duplicats values
#print(df_coaster_db.loc[df_coaster_db.duplicated(subset=['coaster_name','Length','Speed'])])
#print ("################query duplicates#####################")
#print(df_coaster_db.query('coaster_name == "Crystal Beach Cyclone"'))
#drop the second or subsequent occurences of duplicated values
non_duplicated_coaster_db=df_coaster_db.loc[~df_coaster_db.duplicated(subset=['coaster_name',\
                                                                              'Length',\
                                                                              'Speed'])]\
                                                                              .reset_index(drop=True).copy()
print (f"after dropping duplicates from dataframe the dimension is:{non_duplicated_coaster_db.shape}")

#change plot style
plt.style.use('ggplot')
print ("#####################Multivariate analysis#############################")
#print (f"Speed stats:{non_duplicated_coaster_db.Speed.describe()}")
#get the non null Speed data with location
non_null_speed=non_duplicated_coaster_db[~non_duplicated_coaster_db['speed_mph'].isna()]\
                                                                            .loc[:,["Location","speed_mph"]]\
                                                                            .copy()
print (f"non_null_speed:{non_null_speed.head()}")
#find the locations with fastes rollar coasters
df=non_null_speed.query("Location != 'Other'").groupby('Location')['speed_mph']\
                                              .agg(['mean','count'])\
                                              .query('count >=10')\
                                              .sort_values('mean',ascending=False)
#test=df.groupby('Location').agg(['mean','count'])
print (f"df:{df}")


#show the plot
#plt.show()