#libraries to import for graph

import matplotlib.pyplot as plt
import seaborn as sns

#load tips data
df= sns.load_dataset('tips')
print (df.info())
plt.scatter(data=df,\
            x='total_bill',\
            y='tip',\
            s=df['size']*10)
plt.show()