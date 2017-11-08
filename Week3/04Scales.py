# -*- coding: utf-8 -*-
"""
Created on Wed Oct  26 06:01:12 2017
In The name of Allah,The Beneficent and The Merciful 

@author: TINA
"""
import pandas as p

'''
nominal data, which in Pandas is called categorical data. Panda is actually has a built in type for
categorical data and you could set a column of your data to categorical data by using the as type method. 
'''
#categorical data
df = p.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                ## [':D', ':))', ':)', ':||', ':|', ':|', ':3', ':3', ':3', ':/', '://'],
index=['exc', 'exc', 'exc', 'good', 'good', 'good','not good','not good','not good','very bad','very bad'])

df.rename(columns={0: 'Grades'}, inplace=True)
#df['Grades'].astype('category').head()
print('Printing dataframe \n',df)
print('Printing dataframe \n',df['Grades'].astype('category').head())

#######
grades = df['Grades'].astype('category',categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+','A-','A','A+'],ordered=True)
print(grades.head())
print(grades>'C+') #boolean opertaions, ordinal data has ordering to help u with thw boolean masking


'''
Variables with a Boolean value are typically called dummy variables. And pandas has a built-in
function called get dummies, which will convert the values of a single column into multiple columns of 0's and 1's, 
indicating the presence of a dummy variable. 
'''
'''
panda says a function called cut,
which takes in argument which is some real like structure of a column or
a data frame or a series. It also takes a number of bins to be used
and all bins are kept at equal spacing. 
'''
