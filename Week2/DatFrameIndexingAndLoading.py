# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:51:22 2017
In The name of Allah,The Beneficent and The Merciful
@author: TINA
"""

import pandas as p


order1 = p.Series({'Name': 'Tina','Item Purchased': 'Pastry','Cost': 175})
order2 = p.Series({'Name': 'Johra','Item Purchased': 'Cookie','Cost': 76})
order3 = p.Series({'Name': 'Jui','Item Purchased': 'Cake','Cost': 150})
order4 = p.Series({'Name': 'Juthy','Item Purchased': 'Doughnut','Cost': 80})


df = p.DataFrame([order1, order2, order3,order4], index=['store1', 'store2', 'store2','store3'])
print(df.head())


costs=df['Cost'] ##returns the columns of costs
print("Printing costs only \n",costs)

costs+=3
print("After increasing costs by 3 \n",costs)
print("After increasing costs by 3 Original DataFrame\n",df.head())  ##it affects the main data frame too

##!cat train.csv

file=p.read_csv("train.csv")
print(" Printing the csv file \n",file.head())


file=p.read_csv('train.csv',index_col=0,skiprows=1)
print(" Printing the csv file \n",file.head())

print(" Printing the columns \n",file.columns)

#####Skipping Rows
df = p.read_csv('train.csv', index_col = 0, skiprows=3)
print("\n After Skipping Rows \n",df.head())
