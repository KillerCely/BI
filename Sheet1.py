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
