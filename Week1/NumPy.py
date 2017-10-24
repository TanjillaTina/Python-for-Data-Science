# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:31:27 2017

In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""
"""
Numpy, a package widely used in the data science community which lets us work efficiently with arrays and matrices in Python.
"""

import numpy as np

##Creating a list and converting it into an array

listt=[1,2,3,4,5]
arra=np.array(listt)
print(arra)

##Creating a multidiensional array
y=np.array([1,2,3,4])
print(y)
Array2D=np.array([[1,2,3,4,5],[5,6,7,8,9]]) 
print("Array2d",Array2D)

print("Dimension of Array2D : ",Array2D.shape) ##shape returns the dimension of array

####creation array of values with specified range
ar2=np.arange(0,30,2)  ##arange(startingValue,endingValue,increment or decrement)
print("printing array of values with certain range :",ar2)  


######Suppose, we want to convert ar2 into a 3*5 dimensional array,we can use reshape to do that

ar2reshape=ar2.reshape(3,5)
print("3*5 array : ",ar2reshape)

#####Another way to reshape the array
o1=np.linspace(0,4,9) ##linespace(starting value,ending value,the total no. of points u want within this range)
print("Printing array o: ",o1)
ors=o1.resize(3,3)
print("resizing array o :",ors)

###########Several built-In functions for creating arrays
one=np.ones((3,5))  ##returns array of (n,n) dimensional array of value 1
print(one)

zero=np.zeros((3,5))
print(zero)

diag=np.eye(4,5) ###returns a diagonal array 
print(diag)

z=[2,4,5,6]
arz=np.array(z)
print(z)
diag2=np.diag(z)
print(diag2) ## returns a diagonal array with values of array z


######repeat function
k=np.array([1,2,3]*3) #repeat an oneD array with these calues repeated in *n times
print("k: ","\n",k)

#####

k2=np.repeat([1,2,3],3) #repeat an oneD array with these calues repeated in ,n times,but,the frst value ntimes then 2nd value n times and soo on
print("k2: ","\n",k2)


######Creating ones array and Multiply it by 4
onee=np.ones([3,5],int)
print("Onee: ","\n",onee)
mul=np.vstack([onee*4])  ###vstack() multiplies vertically
print("Printing Vertically Multiplied array: ",mul)
mul=np.hstack([onee*4])   ###hstack() multiplies horizontally
print("Printing Horizontally Multiplied array: ",mul)
########

#######################Operations we can do with numpy arrays


z1=[2,4,5,6]
arz1=np.array(z1)
print("Printing arz1 ","\n",arz1)

z2=[1,2,3,6]
arz2=np.array(z2)
print("Printing arz1 ","\n",arz2)

##we can simply add,multiply,power these arrays
print("adding arrays: ",arz1+arz2)
print("Power array : ",arz1**2)
summ=arz1.dot(arz2)
print("Linear point to point multiplication and sum: ",summ)

z3=np.array([arz2**2])  #again power array 
print("z3 : \n ",z3)

####Getting the transpose array
print("2D Array: \n",Array2D)
print("Transpose array: \n",Array2D.T,"\n and transpose array's shape :",Array2D.T.shape," it's value type: ",Array2D.dtype)
Array2D=Array2D.astype('f') ##changing the type of array from int to float
print("Now Type : ",Array2D.dtype)

########Other operations on aray
a = np.array([4, 2, 1, 6, 5])
print("Sum : ",a.sum()," min: ",a.min()," max: ",a.max()," mean: ",a.mean()," Standard deviation ",a.std())

print("Maximum and Minumum value's index: ",a.argmax(),"and ",a.argmin())









########################################Indexing and Slicing Arrays#########################################
s = np.arange(13)**2  ##crate array from range 0to13 and pow 2
print("Array s:\n",s)
print("First and 5th elements are : ",s[0]," and ",s[4])##indexing starts from 0

print("Elements from 1to 10: ",s[0:10]) ##to indicate a range. array[starting:ending]

print("Counting from back: ",s[-5:])  ##getting last 5 elements

print("starting 5th element from the end, and counting backwards by 1 until the beginning of the array is reached \n",s[-5::-1])

###################Multidimensional Array#################
r = np.arange(36)
r.resize((6, 6))
print("Again 2d array: \n",r)
print("Getting 3-3 element",r[2, 2])
print("Printing a range of rows and collums \n",r[3, 0:6]) ##r[rowNumber,fromelement:toelement]














