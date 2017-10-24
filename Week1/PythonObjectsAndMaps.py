# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:01:47 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA

advanced Python Objects and Maps
"""
##Objects in Python don't have any private or protected members,if u instantiate a  class u can have access to the entire class 
class Person:
    department="Computer Science and Engineering"
    name=None
    location=None
    def set_name(self,new_name):
         self.name=new_name
      
    def set_Location(self,new_location):
        self.location=new_location   

########Map function is one of the basis for the "Funtional Programming" in Python

'''
The map function is one of the basis for functional programming in Python. Functional programming is a programming paradigm in which you explicitly declare all parameters which could change through execution of a given function.
 Thus functional programming is referred to as being side-effect free, because there is a software contract that describes what can actually change by calling a function.
 Now, Python isn't a functional programming language in the pure sense. Since you can have many side effects of functions, and certainly you don't have to pass in the parameters of everything that you're interested in changing.
'''

'''
 So, functional programming methods are often used in Python, 
 and it's not uncommon to see a parameter for a function, be a function itself.
 The map built-in function is one example of a functional programming feature of Python, 
 that I think ties together a number of aspects of the language. The map function signature looks like this
'''

store1={27,56,23,55,99}
store2={43,65,12,33,65}
cheapSet=map(min,store1,store2)
print(cheapSet) ##Map function always returns a map Object
for i in cheapSet:
    print(i)
    
#######
'''
here is a list of Faculty teaching,
write a function and apply it writing a map() to get the faculty titles and last names 
'''    

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

li=list(map(split_title_and_name, people))
for i in li:
    print(i)
    
    
