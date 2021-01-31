import csv
import pandas as pd
import matplotlib.pyplot as Mplt
import numpy as np


print("----------------Punto 3 ----------------------------------------------------------")
print("---------Secciones 1,2,3-----------")

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
        for n in range(0,len(species)):
            if(i==0):

                if(j==0):
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_length,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_width,
                                s=10,c=colors[n])
                else:
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_width,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_length,
                                s=10,c=colors[n])

            elif(i==1):

                if(j==1):
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_length,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_length,
                                s=10,c=colors[n])
                else:
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_width,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_width,
                                s=10,c=colors[n])
            elif(i==2):

                if(j==1):
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].sepal_length,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_width,
                                s=10,c=colors[n])
                else:
                    ax[i,j].scatter(IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_length,IrisCVS_readerR[IrisCVS_readerR['species']==species[n]].petal_width,                                
                                s=10,c=colors[n])



#Adding legend to general plot
fig.legend(["Setosa","Versicolor","Virginica"])
#Showing up the plot generated
Mplt.show()
#Saving the plot to an pdf called iris_scatter as pdf
print("\n")
fig.savefig("iris_scatter.pdf", bbox_inches='tight')
print("Plot saved as iris_scatter.pdf")
print("\n")
print("\n")

print("---------Secciones 4 -------------")

#Creating a plot
fig, ax =Mplt.subplots()


#Merge of data
data =  [IrisCVS_readerR['sepal_length'],IrisCVS_readerR['sepal_width'],IrisCVS_readerR['petal_length'], IrisCVS_readerR['petal_width'] ]

#generate boxplot
ax.boxplot(data)


#Showing up the general plot
Mplt.show()


print("---------Secciones 5 -------------")
