# -*- coding: utf-8 -*-
"""
Created on Wed Oct  25 19:43:06 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

####Using Idioms we can add several operations on our dataframe using a single line
import pandas as p
import numpy as np

 
df = p.read_csv('train.csv')
#print(df)
print("Indicies are : ",df.head())


##using more efficient Method Chaining
processed=(df.where(df['Sex']=='female').dropna().set_index(['Ticket','Cabin']).rename(columns={'Age': 'Ages'}))
print("Printing after processing", processed) #now it shows on 88 rows based on these operations where actual are 889


####upper operations in old traditional way, equires total three lines istead of oneso, upper one is more efficient

df2 = df[df['Sex']=='female']
df2.set_index(['Ticket','Cabin'], inplace=True)
df2.rename(columns={'Age': 'Ages'})
print("Printing using traditional method ",df2.head())




##############Using Apply
#here we compare two data values and compare them and get two new indices min and max having the min and max values of these data
def min_max(row):
   data = row[['Age','Fare']]
   return p.Series({'min': np.min(data), 'max': np.max(data)})


print("Printing data",df.apply(min_max, axis=1))

#######using another form

def min_max2(row):
   data = row[['Age','Fare']]
   row['max'] = np.max(data)
   row['min'] = np.min(data)
   return row


print("Printing data again ",df.apply(min_max2, axis=1))


###########################Same thing using lambdas

rows = ['Age','Fare',]
print("Using the lambda",df.apply(lambda x: np.max(x[rows]), axis=1))



