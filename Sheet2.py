import csv
import pandas as pd
import matplotlib.pyplot as Mplt
import numpy as np


#Reading the manually downloaded file
IrisCVS_readerM = pd.read_csv('iris.csv')

#Reading the csv from a remote link

IrisCVS_readerR = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
 #Creating subplots 3*2 from matlab
fig, ax = Mplt.subplots(3, 2)

#Geting the key from csv species
species =np.unique(IrisCVS_readerR['species'])

#list of colors to use on plot
colors=['r','g','b']

#filling axes ploters
for i in range (3):
    for j in range (2):

        if(j==1):
            ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[i]].petal_length,
                         IrisCVS_readerR[IrisCVS_readerR['species']==species[i]].petal_width,
                         s=10,c=colors[i])

        else:
            ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[i]].sepal_length,
                         IrisCVS_readerR[IrisCVS_readerR['species']==species[i]].sepal_width,
                         s=10,c=colors[i])


#Adding legend to general plot
fig.legend(["Setosa","Setosa","Versicolor","Versicolor","Virginica","Virginica"])
#Showing up the plot generated
Mplt.show()
#Saving the plot to an pdf called iris_scatter as pdf
fig.savefig("iris_scatter.pdf", bbox_inches='tight')
