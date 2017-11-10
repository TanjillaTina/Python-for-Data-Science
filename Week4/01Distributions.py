# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 18:25:58 2017

In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

import pandas as p
import numpy as n

'''
Here we ask for a number from
the NumPy binomial distribution. We have two parameters to pass in. The first is the number of
times we want it to run. The second is the chance we get a zero,
which we will use to represent heads here. 
'''
print(n.random.binomial(1,.9))

'''
run the simulation
a thousand times and divided the result by a thousand. 
'''
print(n.random.binomial(1000,.5)/1000)

'''
chance of going out tomorrow. So maybe there a hundredth of a percentage chance. We can put this into a binomial
distribution as a weighting in NumPy. If we run this 100,000 times we see
there are pretty minimal going out events. 
'''

goingOut=.01/100 #chance of event
print(n.random.binomial(1000,goingOut))

'''
'''
ChaneOfTor=.01
TorEvents=n.random.binomial(1,ChaneOfTor,10000)
TwoDaysInARow=0

for i in range(1,len(TorEvents)-1):
    if TorEvents[i]==1:
        TwoDaysInARow+=1
        
print('Total ',TwoDaysInARow,' Out of ',len(TorEvents) );

