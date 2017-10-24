# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:03:17 2017

In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

#####Lambda Function
'''
here is a list of Faculty teaching,
write a function and apply it writing a map() to get the faculty titles and last names
but, using lambda() 
'''    
MyFunction=lambda a,b,c: a+b #Similar to C++'s inline function after lambda comes parametres and then the return value
print(MyFunction(3,4,5))

#################################
##Previous function in Lambda
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


#########################

########List Comprehension

li=list()

for number in range (1,100):
    if number%3==0:
        li.append(number)

for i in li:
    print(i)
    
#######this can be done in a sigle line
Mylist=[number for number in range (1,100) if number%3==0]
print("Printing using in-line:",Mylist) 

####Another Example
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst 
print(times_tables())

###UpperFuntin in a single line
times_tables() == [j*i for i in range(10) for j in range(10)]
print("list comprehension",times_tables()) 

########### 

        
    