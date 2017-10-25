# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:49:20 2017
In The name of Allah,The Beneficent and The Merciful
@author: TINA
"""
import pandas as p
import numpy as np
##########Starting "How to get data out of the Series" ###############
d={'Book':3,"Laptop":1,"Chocolate":2}
ds=p.Series(d)
print(ds)

print("the 2nd element: ",ds.iloc[2]) ##returns the iloc[n] nth element's value
print("the value by index 'Chocolate'",ds.loc['Chocolate']) #returns the value of that index
####iloc and loc are attributes not methods

print(ds[2]) ##similar to iloc
print(ds['Chocolate']) #similar to loc

##########Ending "How to get data out of the Series" ###############

##########Starting "Working with the data of the Series" ###############

price=[23,56,3,45,2]
ps=p.Series(price)
#iterate over series data
sum=0
for i in ps:
    sum+=i
print("Sum is ",sum)

##upper summation can also be done using numpy
sum=np.sum(ps)    
print("Sum is (Using Numpy) ",sum)    
    
#this creates a big series of random numbers
s = p.Series(np.random.randint(0,1000,10000))
print(s.head())
print("Length ",len(s))

####Getting the runtime
'''
%%timeit -n 100
summary = 0
for item in s:
    summary+=item
    ######Another one
%%timeit -n 100
summary = np.sum(s)

##Second one is much faster
   '''
   
##Increase each number in s by 2
s+=2
print("After Increasing ",s.head())

####We can also add elements at the end the datatype isn't a concern

ds.loc['Tina']='Laptop'
print("After adding : \n",ds)  

###Till now, we created series with unique index values no, we are gonna make non-unique index values
s=p.Series([5,3,6],index=['Book','Book','Book'])
print(s)

d={'Book':3,"Laptop":1,"Chocolate":2}
ds=p.Series(d)
MySeries=ds.append(s)
print(MySeries) 
print("it dosent change the original ds series \n",ds)

##########Ending "Working with the data of the Series" ###############
