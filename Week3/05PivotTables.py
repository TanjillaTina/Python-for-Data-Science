# -*- coding: utf-8 -*-
"""
Created on Wed Oct  26 07:31:57 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""
'''
A pivot table allows us to pivot out one of these columns into a new column headers
and compare it against another column as row indices. 
'''
import csv
import numpy as np
import pandas as pd

df = pd.read_csv('carss.csv')
print(df.head())

'''
let's say we wanted to compare the makes
of electric vehicles versus (mpg) the models and that we wanted to do this comparison
in terms of hp. To do this, we tell pandas we
want the values to be hp, the index to be the model and
the columns to be the mpg Then we specify that
the aggregation function, and here we'll use the NumPy mean. 
'''
print('After categorization \n ',df.pivot_table(values='hp', index='model', columns='mpg', aggfunc=np.mean))

