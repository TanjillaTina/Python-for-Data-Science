# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:08:38 2017
In The name of Allah,The Beneficent and The Merciful
@author: TINA
"""
'''
The DataFrame is conceptually a two-dimensional series object, where there's an index and multiple columns of content,
 with each column having a label. In fact, the distinction between a column and a row is really only a conceptual distinction.
 And you can think of the DataFrame itself as simply a two-axes labeled array. 
'''
import pandas as p


order1 = p.Series({'Name': 'Tina','Item Purchased': 'Pastry','Cost': 175})
order2 = p.Series({'Name': 'Johra','Item Purchased': 'Cookie','Cost': 76})
order3 = p.Series({'Name': 'Jui','Item Purchased': 'Cake','Cost': 150})
order4 = p.Series({'Name': 'Juthy','Item Purchased': 'Doughnut','Cost': 80})


df = p.DataFrame([order1, order2, order3,order4], index=['store1', 'store2', 'store2','store3'])
print(df.head())

###Select data asociate to stores
print("Printing data of store2 \n",df.loc['store2']) ## the name of the series is returned as the row index value, while the column name is included in the output as well
print("Printing all the Item Purchased \n",df.loc[:,['Item Purchased']].values) 
##another way
print("Another way \n",df['Item Purchased'])

print("PRINTING all the costs of store 2\n ",df.loc['store2','Cost'])

'''
What if we just wanted to do column selection and just get a list of all of the costs?
 Well, there's a couple of options. 
 First, you can get a transpose of the DataFrame, using the capital T attribute,
 which swaps all of the columns and rows. This essentially turns your column names into indices.
 And we can then use the .lock method.
 This works, but it's pretty ugly.
 Here is the Example
'''
print("Printing a list of all costs \n",df.T.loc['Cost'])
##the same thing using pandas
print("Printing a list of all costs \n",df.loc['store2']['Cost']) ##rowindex and column
print("Select all rows and show the values selected by column index \n ",df.loc[:,['Name', 'Cost']])

#######Deleting data
print(df.drop('store1'))

copy_df = df.copy()
copy_df = copy_df.drop('store2')
print("Coppied one \n ",copy_df)  ##performs operation on the copy
print("Original One",df.head()) ##original one remains unchanged
############# 

######Updating the dataframe , all the costs by two
df['Cost'] *= 0.8
print("After incrementing all the costs by 20% \n",df)

'''
Drop has two interesting optional parameters.
 The first is called in place, and if it's set to true, the DataFrame will be updated in place, 
 instead of a copy being returned. The second parameter is the axes,
 which should be dropped. By default, this value is 0, indicating the row axes. 
But you could change it to 1 if you want to drop a column. 
'''
del copy_df['Cost'] #this will direcly affect the data frame,instead of craeting a copy
print("After deleting Cost \n",copy_df)

#############Adding a new collumn into tha data frame#####
df['Total No. of items'] = None
print("After adding a new column \n",df)


######Updating the dataframe , all the costs by two
df['Cost'] *= 0.8
print(df)