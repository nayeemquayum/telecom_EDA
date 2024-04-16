import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')
iris['variety'].replace({'Setosa':0,'Versicolor':1,'Virginica':2},inplace=True)
#create the frame with size
'''Option 1
plt.figure(figsize=(15,7))
#draw graph
plt.scatter(iris['sepal.length'],iris['petal.length'],c=iris['variety'],cmap='jet',alpha=0.7)
#set x and y label
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.colorbar()
#show the graph
plt.show()'''
#Alter native way of doing the same
#create the frame and canvas
fig,ax = plt.subplots(figsize=(15,7))
#add graph to the canvas
ax.scatter(iris['sepal.length'],iris['petal.length'],c=iris['variety'],cmap='jet',alpha=0.7)
#set x and y label
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Petal Length')
fig.colorbar()
#show the canvas
fig.show()
