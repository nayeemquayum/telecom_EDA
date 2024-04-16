import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#load cars dataset
tips = sns.load_dataset('tips')
iris = pd.read_csv('iris.csv')
print (tips.head())
#cars = sns.load_dataset('mpg').dropna()
#print (cars.info())
#select only 4,6 and 8 cylinder data
#sub_cars=cars[cars.cylinders.isin([4,6,8])]
#print (sub_cars.info())
sns.jointplot(data=tips,x='total_bill',y='tip',kind='his',hue='sex')
plt.show()