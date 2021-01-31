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
#p = np.linspace(1, 100, n) #first generate another arrays to add, with random values
#m1 = np.append(m, p, axis=1)
#m4 = np.column_stack((m1,p))
#print ("New matrix M: \n" , m)
#print ("\n New matrix M2: \n" , m1)

#Prueba
