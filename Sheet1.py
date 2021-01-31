import numpy as np
print ("\n Exercise 1, Method 1: np.lib")
print ("\n -------------------")
n = int (input("\n Please, insert a number: "))
x = np.ones(n).astype(int) #numpy.ones return a new array of given shape and type, filled with ones.
y = np.arange(3,n*3+1,3) #numpy.arange([start, stop, step])
print ("\n Vector of 1 with width n: \n " , x)
print ("\n Vector 3n: \n " , y)
print ("\n -------------------------")
print ("\n Method 2: np.funtions")
n = int (input ("\n Please, insert a number: "))
x = np.linspace(1, 1, n) #one for arrays with only 1
y = np.linspace(3, n*3, n)
print("\n Vector of 1 with width n: \n" , x)
print("\n Vector 3n: \n" , y)
print ("\n Part two --------- Apply a funtion")
y2=np.array(15*np.sin(y)).astype(int)
print ("\n Apply 15*Sin(y): \n", y2)
print ("\n Now, looking for numbers greater than 6. -------------")
y3 = np.array(y2 > 6).astype(int)
print ("\n List of numbers: \n" , y3)
print ("\n Elements equals 5: ")
y4 = np.array(y2 == 5).astype(int)
print ("\n The Elements are: \n" , y4)
print ("\n ---------------------------------------------------------------------------------------")
print ("\n Now matrix, with w and y2 1.2")
m = np.column_stack((y,y2)) #Stack 1-D arrays as columns into a 2-D array.
print ("\n The matrix is: \n" , m)
print("\n Second method of matrix: \n" )
m1 = np.row_stack((y,y2)) #Stack 1-D arrays as row into a 2-D array.
print("\n The second matrix is: \n" , m1)
yt = np.transpose(m)
print ("\n Transpose M: \n" , yt)
yt2 = np.asmatrix(m1).T
print ("\n Transpose M2: \n" , yt2)
print("\n Add Columns and rows into M and M2: \n")
p = np.linspace(1, 100, n)#first generate another arrays to add, with random values
print("\n" , p)
m1 = np.row_stack((m1, p))
print ("\n New row for m2: \n " , m1)
pt=np.transpose(p) #saco la transpuesta
m=np.column_stack((m, pt))
print ("\n New columns for m: \n", m)


#Exercise 2:
#2.1
import pandas as pd
print ("\n Ejercicio 2: Pandas \n ")
data = {'Name': ['Alexander' , 'Jane'], 'Age': [19,36] , 'Sex': ['male' , 'female'] , 'profession':['student', 'physician']}
data1 = {'Name': ['Eric' , 'Laura'], 'Age': [22,48] , 'Sex': ['male' , 'female'] , 'profession':['lawyer', 'teacher']}
data2 = {'Name': ['Peter' , 'Julia'], 'Age': [31,24] , 'Sex': ['male' , 'female'] , 'profession':['engineer', 'consultant']}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print (df)
print ("\n" ,df1)
print ("\n" ,df2)

#2.2
print ("\n Union of three")
dfc = pd.concat([df, df1, df2])
print ("\n", dfc)

#2.3
print ("\n new dataframe")
data3 = {'Name':['Alexander', 'Jane', 'Eric', 'Laura', 'Peter', 'Julia'],
        'Size':[181,162,178,183,173,169],
        'Salary':[600,4200,4000,3400,5200,3600]}
df4= pd.DataFrame(data3)
dff= pd.merge(dfc, df4, on='Name', how='outer')
print ("\n", dff)

#2.4
print("\n Ajust Size on the dataframe")
dff['Size']=dff['Size'].apply(lambda x: x-1)
print("\n" ,dff)

#2.5
print ("\n Mayores a 30 años: ")
print ("\n Using a funtion Loc")
print ("\n" , dff.loc[dff['Age']>30])
print ("\n Using a Condicional")
dffc=list(filter(lambda x: x>30, dff['Age']))
print("\n" , dffc) #Aqui falta corregir xd

#2.6
print("\n Order by Salary")
dff.sort_values(by=['Salary'])
print("\n", dff)

#2.7
print("\n Group of people according the sex: ")
dfg = dff.groupby('Sex')
print ("\n" , dfg.get_group('female'))
print ("\n" , dfg.get_group('male'))

#Exercise 3

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


from mpl_toolkits import mplot3d
fig = Mplt.figure()
ax = Mplt.axes(projection='3d')




ax.scatter3D(IrisCVS_readerR['sepal_length'], IrisCVS_readerR['sepal_width'], cmap='Greens');
Mplt.show()
