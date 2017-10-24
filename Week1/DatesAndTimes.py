# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:18:24 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""
###it's commonly Used in data science for sliding windows
import datetime as dt
import time as ti

print(ti.time())

curtime=dt.datetime.fromtimestamp(ti.time())
print(curtime)

print("Year: ",curtime.year," Month: ",curtime.month," Day: ",curtime.day)
print("Hour: ",curtime.hour," Minute: ",curtime.minute," Second: ",curtime.second) 

######
delta=dt.timedelta(days=22)
print(delta)

####
today=dt.date.today();
print("Delta Today ",today-delta)  ##getting the difference

print(today>today-delta)


######
