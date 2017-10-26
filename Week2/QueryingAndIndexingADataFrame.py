# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:22:43 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""
import pandas as p
import numpy as np
import csv

#################################Querying A Data Frame########################################

##Now we are interested to see only the names of survived passengers in the train
##Using Boolean Masking, returns only Bollean results, either true/false
df = p.read_csv('train.csv')
print("The indexes are \n",df.columns)

print("The Survivers list \n")

print(df['Survived']== 1)

print("Printing Female Passengeres \n")
print(df['Sex']=='female')
'''
#####Overlaying the mask on a data frame, it can be done using a where function

We can do this using the where function. The where function takes a Boolean mask as a condition,
applies it to the data frame or series,
and returns a new data frame or series of the same shape.
'''

Survivers=df.where(df['Survived']== 1)
print("Printing Tickets \,")
print("State: ",Survivers['Survived'],"Ticket No: ",Survivers['Ticket'],"\n")
print("Printing Total no of Survived Passesngers :",Survivers['Survived'].count(),"Where total no. of Passengers were: ",df['Survived'].count())
##creating complex queries ( get th length, use the len function )
print("Total no. of Female pasengers who Survived ",len(df[(df['Survived']== 1) & (df['Sex'] == 'female')]))
print("Total no. of Male pasengers who Survived ",len(df[(df['Survived']== 1) & (df['Sex'] == 'male')]))


print("printing Survived Female Passengers ",(df[(df['Survived']== 1) & (df['Sex'] == 'female')]))


'''
Often we want to drop those rows which have no data. 
To do this, we can use the drop NA function.
You can optionally provide drop NA the axes it should be considering.
Remember that the axes is just an indicator for the columns or rows and that the default is zero, which means rows. 
'''
only_Cabin = df.where(df['Cabin']!='Nan')
print(only_Cabin.head())
only_Cabin = only_Cabin.dropna()  ##Dropping the Nan values
print('Printing Passengers who took only Cabibns \n',only_Cabin)
print("Total No. of Passengers who took cabins: ",len(only_Cabin))




########################################################Indexing A Data Frame#####################################

##Setting The Index (changing the index from "PassengerId" to 'Ticket')

df['PassengerId'] = df.index
df = df.set_index('Ticket')

print("Printing after setting the Index \n",df.head())
#######Seseting the Index
df = df.reset_index()

print("Printing after resetting the Index \n",df.head())


'''
One nice feature of pandas is that it has the option to do multi-level indexing. 
This is similar to composite keys in relational database systems. To create a multi-level index,
we simply call set index and give it a list of columns that we're interested in promoting to an index. 
'''

#######Practice Set
'''
Reindex the purchase records dataframe to be indexed heirarchically, first by store ,then by person.
Name these indexes 'Location' and 'Name'. Then add a new entry to it with the value of
Name:Kevyn and Location: 'Store2','Item Purchased': 'Kitty Food','Cost': 3.00
'''
#defining the data frame
purchase_1 = p.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = p.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = p.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = p.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

##Solutiion
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(p.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print("Printing Data Frame \n",df)


#############