# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 08:35:17 2017
In The name of Allah,The Beneficent and The Merciful 
@author: TINA
"""

########Formatting Strings
sales_record={"Name":"Tanjilla","No of Items":34,"Bought":"Chocolate","PriceEach":3}
statement="Our customer {} Bought Item {} total {} piece, Per piece price {} So in total she should pay {}"
print(statement.format(sales_record["Name"],
                       sales_record["Bought"],
                       sales_record["No of Items"],
                       sales_record["PriceEach"],
                       sales_record["PriceEach"]*sales_record["No of Items"]))   
##########