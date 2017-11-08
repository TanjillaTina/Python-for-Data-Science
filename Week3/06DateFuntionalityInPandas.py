# -*- coding: utf-8 -*-
"""
Created on Wed Oct  26 19:51:07 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

import pandas as p
import numpy as n

'''
Pandas has four main time related classes. Timestamp, DatetimeIndex,Period, and PeriodIndex. 
'''
#######Timestamp: represents a single timestamp and associates values with points in time. Timestamp is interchangeable with Python's datetime in most cases
print('Timestamp ',p.Timestamp('9/1/2016 10:05AM'))

'''
 Suppose we weren't interested in a specific point in time, and instead wanted a span of time.
 This is where Period comes into play. Period represents a single time span,
such as a specific day or month. 
'''

######Period :
print('Period ',p.Period('1/1996'))
print('Period ',p.Period('21/01/1996'))


##DateTimeIndex

ti= p.Series(list('ab'), [p.Timestamp('2016-1-1'), p.Timestamp('2016-02-02')])
print('DateTimeIndex ',ti ,' Type ',type(ti.index) )


############PeriodIndex

ti2 = p.Series(list('lj'), [p.Period('2016-07'), p.Period('2016-08')])
print('DateTimeIndex ',ti2 ,' Type ',type(ti2.index) )

####Converting to Datetime

d = ['21 January 1996', 'Jan 05, 1970', '2017-02-02', '5/12/11']
ti3 = p.DataFrame(n.random.randint(10, 100, (4,2)), index=d, columns=list('ab'))
print('Converting to Datetime ',ti3 ,' Type ',type(ti3.index) )


ti3.index = p.to_datetime(ti3.index)
print('Afer Formatting standard format of Datetime \n ',ti3)
p.to_datetime('4.7.12', dayfirst=True)


########Timedeltas

##differneces between time

print('Differnce between days ',p.Timestamp('9/3/2016')-p.Timestamp('9/1/2016'))
print('Differnce between days ',p.Timestamp('9/2/2016 8:10AM') + p.Timedelta('12D 3H'))


######Working with Dates in a Dataframe

dates = p.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)

#########
df = p.DataFrame({'Count 1': 100 + n.random.randint(-5, 10, 9).cumsum(),'Count 2': 120 + n.random.randint(-5, 10, 9)}, index=dates)
print(df)
print('Printing weekly name values \n',df.index.weekday_name)
print('Difference ro between each dtes \n',df.diff())
print('Printing partial value indexing year \n',df['2017'])
print('Printing partial value indexing year and month \n',df['2016-12'])
print('Printing partial value indexing after 2016-12 and onwards \n',df['2016-12':])

########changing frequency of oyr dataframe using asfreq
print('After changing frequency \n',df.asfreq('W', method='ffill'))

import matplotlib.pyplot as plt
#matplotlib inline
df.plot()