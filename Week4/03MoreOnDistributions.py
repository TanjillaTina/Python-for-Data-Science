# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 18:47:02 2017

In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

import pandas as p
import numpy as n
import scipy.stats as st

'''
The standard deviation is simply
a measure of how different each item, in our sample, is from the mean.
'''

distribution=n.random.normal(.75,size=10000)
print(n.sqrt(n.sum((n.mean(distribution)-distribution)**2)/len(distribution)))

#builtin function for satndard deviation upper one was raw code

print(n.std(distribution))

'''
There's a couple more measures of
distribution that are interesting to talk about. One of these is the shape of
the tales of the distribution and this is called the kurtosis. We can measure the kurtosis using the
statistics functions in the SciPy package. A negative value means
the curve is slightly more flat than a normal distribution, and
a positive value means the curve is slightly more peaky than
a normal distribution. Remember that we aren't measuring the
kurtosis of the distribution per se, but of the thousand values which we
sampled out of the distribution. 
'''
print(st.kurtosis(distribution))


###############Chi-Square

chisdf2=n.random.chisquare(2,size=10000)  #df,size
st.skew(chisdf2)



