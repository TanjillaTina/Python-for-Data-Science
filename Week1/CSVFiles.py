# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 08:37:27 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA

"""
######Data files and Summary Statistics
#######Reading a 'csv' file
import csv
#precision 2
with open('train.csv') as CSVFile:

    train=list(csv.DictReader(CSVFile))
'''
n=0       
for i in train:
    n+=1
    print("Passenger no:",n,"Deatils ",i,"\n")
'''
##########Total length
print("Total Passengers in the train ",len(train))

########Getting the Collum names
print("Saved Informations based on: ",train[0].keys())

#####Getting the total fare
Total_Fare=sum(float(d['Fare']) for d in train)
print("Total fare the train got is ",round(Total_Fare,2)," Taka")  #Rounding the folating value using builtInMethod round


######getting the average

avg=Total_Fare/len(train)
print("Average Value ",round(avg,2))

#########Getting the set of Unique values returns a list(gives us the unique levels)
ps=set(d['Sex'] for d in train)
print("What kind of Passengers were in the train :",ps)
Passenger_Class=set(d2['Pclass'] for d2 in train)
print("What kind of Passengers were divided into class :",Passenger_Class)


##########Calculating the total fares obtained from each individual class passengers
Total_Fare_Class1=0
Total_Fare_Class2=0
Total_Fare_Class3=0
No_Of_Passengers_Class1=0
No_Of_Passengers_Class2=0
No_Of_Passengers_Class3=0
for d in train:
    if d['Pclass']=='1':
      Total_Fare_Class1 += float(d['Fare'])
      No_Of_Passengers_Class1+=1
    if d['Pclass']=='2':
      Total_Fare_Class2 += float(d['Fare'])
      No_Of_Passengers_Class2+=1
    if d['Pclass']=='3':
      Total_Fare_Class3 += float(d['Fare'])
      No_Of_Passengers_Class3+=1

print("Total Fare from class 1 :",round(Total_Fare_Class1,2))
print("Total Fare from class 2 :",round(Total_Fare_Class2,2))
print("Total Fare from class 3 :",round(Total_Fare_Class3,2))
print("Fare per head: ")
print("Class 1: ",round((Total_Fare_Class1/No_Of_Passengers_Class1),2))
print("Class 2: ",round((Total_Fare_Class2/No_Of_Passengers_Class2),2))
print("Class 3: ",round((Total_Fare_Class3/No_Of_Passengers_Class3),2))

########### Same problem a more convenient way
fare=dict()
no_p=dict()
No_Passenger=dict() 
Fare_per_Head=dict()
for pc in Passenger_Class:
    pno=0
    tf=0
    for far in train:
        if far['Pclass']==str(pc):
            tf+=float(far['Fare'])
            pno+=1
    fare[pc]=round(tf,2)            ##Getting the total fare of passenger classwise 
    No_Passenger[pc]=pno   ##Getting the total no of passengers classwise     
    Fare_per_Head[pc]=round(tf/pno,2)
print("Total fare for each class :","\n",fare)
print("Total passenger from each class :","\n",No_Passenger)
print("Total Fare per head for each class :","\n",Fare_per_Head)
########
