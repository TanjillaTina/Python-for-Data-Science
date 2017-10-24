# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:36:55 2017

@author: TINA
"""

print("In The Name of Allah, The Beneficent and The Merciful");

st1="Tanjilla";
st2="Tina";
st=st1+" "+st2;
print(st);

##if a cgharacter exist in the String

if 'T' in st:
    print("Yes");
    
####String Comparison

s1="Tanjilla";
s2="Tina";

if s1==s2:
    print("Equal");
else:    
    print("Not Equal");


########## String Greater Than and Less Than (Counts and add the ascii value of each character and then compare it)
if s1>s2:
    print("Tanjilla is Greater than Tina");
else:
    print("Tanjilla is Less than Tina");
    
########String Library

s=s1+" "+s2;
bb="TINA";
print(bb.lower()); ##UpperToLower
ss="tina";
print(bb.upper()); ##LowerToUpper


######Search and Replace
nn=s.replace("Tina","Sarkar");##(A String)Find and replace:: format:: string.replace(replaceWhat,ReplaceWith)
print(nn);

nn2=s.replace('a','u');##(A Character)Find and replace:: format:: string.replace(replaceWhat,ReplaceWith)
print(nn2);

#####Strippint Whitespaces
s3="  "+s1+" "+s2+"  ";
print(s3);
print(s3.strip()); ##Strips spaces from Left and Right
print(s3.lstrip()); ##Strips spaces from Left
print(s3.rstrip()); ##Strips spaces from Right

##Prefixes::Is this line Starts with a particular String or Character??
s3=nn;
if s3.startswith("Tanjilla"):
    print("Yup");
else:
    print("Nop");
    
if s3.startswith("T"):
    print("Yup");
else:
    print("Nop");


####Prsing and Extracting
    
st="this mail is from tina@softtech.net date=20/10/2017"
Starting_postion=st.find('@');
print(Starting_postion);
Ending_postion=st.find(" ",Starting_postion); ##st.find("StringToFind",FromWhichPositionTheSearchingShouldStart);
print(Ending_postion);
host=st[Starting_postion+1:Ending_postion];
print(host);

#####


########