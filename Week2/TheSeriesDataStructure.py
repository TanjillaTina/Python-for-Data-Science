# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 07:45:01 2017
In The name of Allah,The Beneficent and The Merciful
@author: TINA
"""
import pandas as p

name=["book","laptop","chocolate"] #creating a list
s=p.Series(name)  ##rturns a series object
print(s)
#we can also convert nuber list
num=[3,4,6]
n=p.Series(num)
print(n)

##########we can also assign None
name=["book","laptop",None] #creating a list
s=p.Series(name)  ##rturns a series object
print(s)
#we can also convert nuber list
num=[3,4,None]
n=p.Series(num) #it returns a floating dtype series object
print(n)


#############Series can be created from dictionaries too
d={'Book':3,"Laptop":1,"Chocolate":2}
ds=p.Series(d)
print(ds)

print("Printing index: ",ds.index)

###########Series can also be created from
s=p.Series([3,1,2],index=['Book','Laptop','Chocolate'])
print(s)

##########Cutting iNDEX

d={'Book':3,"Laptop":1,"Chocolate":2}
ds=p.Series(d,index=['Book','Laptop'])
print(ds)

