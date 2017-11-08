# -*- coding: utf-8 -*-
"""
Created on Wed Oct  25 19:35:20 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:16:34 2017

@author: TINA

In The Name of Allah, The Beneficent and The Merciful
"""
import pandas as p


order1 = p.Series({'Name': 'Tina','Item Purchased': 'Pastry','Cost': 175})
order2 = p.Series({'Name': 'Johra','Item Purchased': 'Cookie','Cost': 76})
order3 = p.Series({'Name': 'Jui','Item Purchased': 'Cake','Cost': 150})
order4 = p.Series({'Name': 'Juthy','Item Purchased': 'Doughnut','Cost': 80})


df = p.DataFrame([order1, order2, order3,order4], index=['store1', 'store2', 'store2','store3'])
print("Printing DataFrame \n",df)

#Meging data
df['Date']=['Jan211','Jan212','Jan213','Jan214']
print("Printing DataFrame After adding a new column \n",df)

#if all values of the dic are unknown for the new index
df['TableNo']=True
print("Printing DataFrame \n",df)


######when values of the dic are known for the new index,add None for the unknowns
#Using None values
df['TableNo']=[1,None,1,None]
print(df)

#Using indexed values
adf = df.reset_index()
adf['Date'] = p.Series({0: 'dec11', 2: 'dec222'})
adf['TableNo'] = p.Series({1: '23', 3: '45'})
print(adf)


######################Joining two Larger DataFrames together

#creating new dataframes


staff_df = p.DataFrame([{'Name': 'Kelly', 'Role': 'Director'},
{'Name': 'Sally', 'Role': 'Course lia'},
{'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
print("Printing Staff DataFrame \n",staff_df)

student_df = p.DataFrame([{'Name': 'James', 'School': 'Business'},
{'Name': 'Mike', 'School': 'Law'},
{'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print("Printing Student DataFrame \n",staff_df)


##Outer Join (same as DBMS) or union in set theory
##getting all saved info wether stuff or student
outerjoin=p.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print("Printing DataFrame After Outer Join \n",outerjoin)


##Inner Join (same as DBMS) or intersection in set theory
##finding who are both stuff and student
innerjoin=p.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print("Printing DataFrame After Inner Join \n",innerjoin)

#####if staffs are students as well, printing their student info details, to do this we are gonna use left join
leftjoin=p.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print("Printing DataFrame After leftjoin \n",leftjoin)

#####print all the students in a row if they are also stuff
rightjoin=p.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print("Printing DataFrame After rightjoin \n",rightjoin)

##########3Instead of using indedecies we can also use the column 
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
usingCol=p.merge(staff_df, student_df, how='outer', left_on='Name', right_on='Name')
print("Printing DataFrame After merging them into by clmns \n",usingCol)

##########################################Conflicts between Data Frames
#creating new dataframes
df.set_index('Name')
cust_info1 = p.Series({'Name': 'Tina','Uni': 'RU_CSE','Year':4})
cust_info2 = p.Series({'Name': 'Johra','Uni': 'RU_CSE','Year':4})


df2 = p.DataFrame([cust_info1,cust_info2], index=['store1', 'store2'])
df2.set_index('Name')
print("Printing new DataFrame \n",df2)
##Outer Join (same as DBMS) _x is always left and _y is always right
outerjoin=p.merge(df,df2, how='outer', left_index=True, right_index=True)
print("Printing DataFrame After Outer Join \n",outerjoin)

################################################3Multi Indexing in Multiple Columns


